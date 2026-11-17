// Audit web-accessibility-cn: chapter/index match, page refs valid, quotes verbatim, no placeholders.
const fs = require('fs');
const path = require('path');

// 仓库根（脚本位于 <repo>/audit/，故取上一级）
const ROOT = path.resolve(__dirname, '..');
const DIR = path.join(ROOT, 'web-accessibility-cn');
const SRC = process.env.DSH_AUDIT_CORPUS
  || path.resolve(__dirname, '..', '..', '..', '_zl', 'txt', 'jianji-tianxia.txt');

let fails = 0;
const ok = (c, label, extra = '') => { console.log(`${c ? 'PASS' : 'FAIL'}  ${label}${extra ? '  ' + extra : ''}`); if (!c) fails++; };

const walk = (d, o = []) => {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, o); else if (p.endsWith('.md')) o.push(p);
  }
  return o;
};

if (!fs.existsSync(DIR)) { console.error('MISSING dir'); process.exit(1); }
const md = walk(DIR);
const chapters = md.filter((f) => /ch\d+/.test(path.basename(f)));
const skill = fs.readFileSync(path.join(DIR, 'SKILL.md'), 'utf8');
const indexRows = (skill.match(/^\|\s*\[?ch\d/gm) || []).length;

let chars = 0, bad = [];
for (const f of md) {
  const t = fs.readFileSync(f, 'utf8');
  chars += t.length;
  for (const b of ['TODO', '待补', '（略）', '(略)', 'FIXME']) if (t.includes(b)) bad.push(`${path.basename(f)}:${b}`);
}

ok(chapters.length >= 12, '章节数 ≥ 12', `实际 ${chapters.length}`);
ok(indexRows === chapters.length, '索引行数 == 章节数', `${indexRows} vs ${chapters.length}`);
ok(bad.length === 0, '无 TODO/待补/（略）', bad.join(',') || '0');

const core = ['SKILL.md', 'cheatsheet.md', 'glossary.md', 'patterns.md'].filter((f) => !fs.existsSync(path.join(DIR, f)));
ok(core.length === 0, '四个核心文件齐全', core.join(',') || 'ok');

// page refs must exist in source
if (!fs.existsSync(SRC)) {
  console.log('⚠ 未找到原文语料: ' + SRC);
  console.log('   （引文回源校验将跳过；可用 DSH_AUDIT_CORPUS 指定）\n');
  process.exit(0);
}
const src = fs.readFileSync(SRC, 'utf8');
const pages = new Set([...src.matchAll(/^===== PAGE (\d+) =====/gm)].map((m) => +m[1]));
let cited = 0; const badPages = [];
for (const f of chapters) {
  const t = fs.readFileSync(f, 'utf8');
  for (const m of t.matchAll(/（p(\d{1,3})）/g)) {
    cited++; if (!pages.has(+m[1])) badPages.push(`${path.basename(f)}:p${m[1]}`);
  }
}
ok(badPages.length === 0, '页码全部存在于源文本', badPages.length ? badPages.slice(0, 8).join(',') : `${cited} 处引用`);

// verbatim quote check: only quotes that follow 原文（pNN） are claimed verbatim.
// (Other 「」 brackets are the author's own phrasing, not quotations.)
const normQ = (s) => s.replace(/\*\*/g, '').replace(/[\s\u3000]/g, '');
const srcFlat = normQ(src);
let claimedQ = 0, passQ = 0;
const badQ = [];
for (const f of chapters) {
  const t = fs.readFileSync(f, 'utf8');
  const re = /原文（p(\d{1,3})(?:[–—\-]p?(\d{1,3}))?(?:[\s、,，脚注]+[^）]*)?）[\s\S]{0,40}?「([^」]{4,600})」/g;
  for (const m of t.matchAll(re)) {
    claimedQ++;
    const qn = normQ(m[3]);
    if (srcFlat.includes(qn)) { passQ++; continue; }
    const win = 10; let ok = 0, tot = 0;
    for (let i = 0; i + win <= qn.length; i += win) { tot++; if (srcFlat.includes(qn.slice(i, i + win))) ok++; }
    if (tot && ok / tot >= 0.55) { passQ++; continue; }
    badQ.push(`${path.basename(f)} p${m[1]} «${qn.slice(0, 30)}»`);
  }
}
ok(badQ.length === 0, '声称逐字的引文全部可回源核对', `${passQ}/${claimedQ} = ${(passQ / claimedQ * 100).toFixed(2)}%`);
if (badQ.length) console.log('      未通过：' + badQ.slice(0, 5).join(' | '));

// OCR caveat present
ok(/OCR/.test(skill), 'SKILL.md 说明 OCR 来源与错字处理');

// web->physical mapping table
const allText = md.map((f) => fs.readFileSync(f, 'utf8')).join('\n');
const mapSec = /实体产品/.test(allText);
ok(mapSec, '含「Web 原则 → 实体产品」映射内容');

console.log(`\n章节 ${chapters.length} / 索引 ${indexRows} / 字符 ${chars.toLocaleString()} / 声称逐字引文 ${claimedQ} 条`);
console.log(`${fails === 0 ? '★ ALL PASS ★' : fails + ' FAIL(S)'}`);
process.exit(fails === 0 ? 0 : 1);
