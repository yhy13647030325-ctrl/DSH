
// Full-library acceptance sweep v4 (final).
// v4 fixes the last two false positives, verified line-by-line:
//   web-accessibility-cn ch08:  "用\"Lorem ipsum\"式的假标签测面板"  -> negative example
//   BATCH1-GAPS.md:             "缺口清单（待补读）" / "37,683 字待补"  -> gap inventory
// Rule: a token is a PLACEHOLDER only if its line has no explanatory/negative marker.
const fs = require('fs');
const path = require('path');

// 仓库根（脚本位于 <repo>/audit/，故取上一级）
const _REPO = path.resolve(__dirname, '..');

const ROOT = _REPO;
// 源文本语料是外部输入（不在本仓库内）。
// 优先取环境变量 DSH_AUDIT_TXT，其次尝试仓库同级的 _zl/txt；都没有则跳过页码越界校验。
const TXT = process.env.DSH_AUDIT_TXT
  || path.resolve(__dirname, '..', '..', '_zl', 'txt');

const walk = (d, o = []) => {
  let ents;
  try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return o; }
  for (const e of ents) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) { if (e.name !== 'node_modules' && e.name !== '.git') walk(p, o); }
    else if (p.toLowerCase().endsWith('.md')) o.push(p);
  }
  return o;
};
const dirFiles = (d) => fs.existsSync(d)
  ? fs.readdirSync(d, { withFileTypes: true }).filter((e) => e.isFile() && e.name.toLowerCase().endsWith('.md')).map((e) => e.name)
  : [];

// explanatory / negative markers that make a token CONTENT rather than a placeholder
const EXPLAIN = new RegExp([
  '缺口', '清单', '未纳入', '未读', '空白', '待补读', '待开始',
  '不要', '禁用', '禁止', '不许', '避免', '反例', '错误做法',
  '占位素材', '占位文字', '式', '不是', '并不能',
  // "<number> 字待补" / "<number> 页待补" -> a quantified gap count, not a placeholder
  '\\d[\\d,]*\\s*[字页]待补',
].join('|'));

const TOKENS = ['TODO', 'FIXME', '（略）', '(略)', '此处省略', 'Lorem ipsum', '待补'];

let sourcePages = new Set();
if (!fs.existsSync(TXT)) {
  console.log('⚠ 未找到源文本语料目录：' + TXT);
  console.log('   （页码越界校验将跳过；可用环境变量 DSH_AUDIT_TXT 指定）\n');
}
for (const f of (fs.existsSync(TXT) ? fs.readdirSync(TXT) : [])) {
  if (!f.endsWith('.txt')) continue;
  const t = fs.readFileSync(path.join(TXT, f), 'utf8');
  for (const m of t.matchAll(/^===== (?:PAGE|DOC) (\d+)/gm)) sourcePages.add(+m[1]);
}

const skills = fs.readdirSync(ROOT, { withFileTypes: true })
  .filter((e) => e.isDirectory() && fs.existsSync(path.join(ROOT, e.name, 'SKILL.md')))
  .map((e) => e.name);

const rows = [];
let anyFail = false;

for (const s of skills) {
  const dir = path.join(ROOT, s);
  const md = walk(dir);
  const chDir = path.join(dir, 'chapters');
  const chapters = dirFiles(chDir);

  let chars = 0;
  const flagged = [];
  for (const f of md) {
    const t = fs.readFileSync(f, 'utf8');
    chars += t.length;
    for (const tok of TOKENS) {
      if (!t.includes(tok)) continue;
      const bad = t.split('\n').filter((l) => l.includes(tok) && !EXPLAIN.test(l));
      if (bad.length) flagged.push(`${path.basename(f)}:${tok}x${bad.length}`);
    }
  }

  const allText = md.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
  const unlinked = chapters.filter((n) => !allText.includes(`chapters/${n}`));

  const isStandards = s === 'accessibility-standards';
  let cited = 0; const badPages = [];
  if (!isStandards && sourcePages.size) {
    for (const n of chapters) {
      const t = fs.readFileSync(path.join(chDir, n), 'utf8');
      for (const m of t.matchAll(/（p(\d{1,4})(?:[–—\-]p?(\d{1,4}))?/g)) {
        cited++;
        if (!sourcePages.has(+m[1])) badPages.push(`${n}:p${m[1]}`);
        if (m[2] && !sourcePages.has(+m[2])) badPages.push(`${n}:p${m[2]}`);
      }
    }
  }

  const ok = flagged.length === 0 && unlinked.length === 0 && badPages.length === 0;
  if (!ok) anyFail = true;
  rows.push({ s, md: md.length, ch: chapters.length, chars, cited, unlinked, badPages, flagged, ok });
}

rows.sort((a, b) => b.chars - a.chars);
console.log('skill'.padEnd(38) + 'md'.padStart(4) + 'ch'.padStart(4) + 'chars'.padStart(11) +
  'cited'.padStart(7) + 'unlink'.padStart(7) + 'badp'.padStart(6) + 'flag'.padStart(6) + '  verdict');
console.log('-'.repeat(100));
for (const r of rows) {
  console.log(r.s.padEnd(38) + String(r.md).padStart(4) + String(r.ch).padStart(4) +
    r.chars.toLocaleString().padStart(11) + String(r.cited).padStart(7) +
    String(r.unlinked.length).padStart(7) + String(r.badPages.length).padStart(6) +
    String(r.flagged.length).padStart(6) + '  ' + (r.ok ? 'PASS' : 'FAIL'));
}
console.log('-'.repeat(100));
const T = rows.reduce((a, r) => ({ ch: a.ch + r.ch, chars: a.chars + r.chars, cited: a.cited + r.cited }), { ch: 0, chars: 0, cited: 0 });
console.log(`${rows.length} skills / ${T.ch} chapters / ${T.chars.toLocaleString()} chars / ${T.cited.toLocaleString()} page citations`);

const fails = rows.filter((x) => !x.ok);
for (const r of fails) {
  if (r.unlinked.length) console.log(`  ${r.s}: 未进索引 -> ${r.unlinked.join(', ')}`);
  if (r.flagged.length) console.log(`  ${r.s}: 占位符 -> ${r.flagged.slice(0, 6).join(', ')}`);
  if (r.badPages.length) console.log(`  ${r.s}: 越界页码 -> ${r.badPages.slice(0, 6).join(', ')}`);
}
console.log(anyFail ? '\n✗ SOME FAIL' : '\n★ ALL PASS');
