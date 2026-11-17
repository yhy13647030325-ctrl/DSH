
// check_links v2: skip links that appear inside inline code spans or fenced blocks.
//
// Reason: several docs legitimately show link SYNTAX as examples inside backticks,
// e.g. `[词](/音标/)` or `[Redis](node:cache-read.redis)`. Those are not links.
// Flagging them forces authors to mangle their own documentation.
const fs = require('fs');
const path = require('path');

// 仓库根（脚本位于 <repo>/audit/，故取上一级）
const _REPO = path.resolve(__dirname, '..');

const ROOT = _REPO;

const walk = (d, o = []) => {
  for (const e of fs.readdirSync(d, { withFileTypes: true })) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) { if (!['node_modules', '.git'].includes(e.name)) walk(p, o); }
    else if (p.endsWith('.md')) o.push(p);
  }
  return o;
};

// mask out inline code spans and fenced blocks, preserving offsets
function maskCode(text) {
  let out = text;
  // fenced blocks
  out = out.replace(/```[\s\S]*?```/g, (m) => ' '.repeat(m.length));
  out = out.replace(/~~~[\s\S]*?~~~/g, (m) => ' '.repeat(m.length));
  // inline code spans (```...``` already gone); handle `a` and ``a``
  out = out.replace(/``[^`]*``/g, (m) => ' '.repeat(m.length));
  out = out.replace(/`[^`\n]*`/g, (m) => ' '.repeat(m.length));
  return out;
}

// 预装技能（上游维护、gitignored、不改）不参与断链审计
const PREINSTALLED = new Set(['video-talkcraft', 'anything2explainer', 'video-shotcraft', 'archify']);
const files = walk(ROOT).filter((f) => {
  const top = path.relative(ROOT, f).split(path.sep)[0];
  return !PREINSTALLED.has(top);
});
let checked = 0;
const broken = [];
const skipped = { anchorOnly: 0, external: 0 };

for (const f of files) {
  const raw = fs.readFileSync(f, 'utf8');
  const masked = maskCode(raw);
  const dir = path.dirname(f);

  for (const m of masked.matchAll(/\[([^\]]{0,140})\]\(([^)\s]+)(?:\s+"[^"]*")?\)/g)) {
    const target = m[2];
    if (/^(https?:|mailto:|ftp:|tel:|data:)/i.test(target)) { skipped.external++; continue; }
    if (target.startsWith('#')) { skipped.anchorOnly++; continue; }
    const clean = target.split('#')[0];
    if (!clean) { skipped.anchorOnly++; continue; }
    let decoded = clean;
    try { decoded = decodeURIComponent(clean); } catch { /* keep */ }
    checked++;
    const abs = path.resolve(dir, decoded);
    if (!fs.existsSync(abs)) {
      broken.push({
        file: path.relative(ROOT, f),
        target,
        line: raw.slice(0, m.index).split('\n').length,
      });
    }
  }
}

console.log(`扫描 md        : ${files.length}`);
console.log(`检查相对链接    : ${checked}`);
console.log(`跳过（外部/锚点）: external=${skipped.external} anchorOnly=${skipped.anchorOnly}`);
console.log(`断链            : ${broken.length}`);

if (broken.length) {
  console.log('\n=== 剩余断链 ===');
  for (const b of broken) {
    console.log(`  ${b.file}:${b.line} -> ${b.target}`);
  }
  fs.writeFileSync(path.join(__dirname, 'broken-links.json'), JSON.stringify(broken, null, 1), 'utf8');
} else {
  console.log('\n★ 无断链');
  fs.writeFileSync(path.join(__dirname, 'broken-links.json'), '[]', 'utf8');
}
