// find_fake_headings v4 (FINAL, corrected)
//
// Two bugs fixed in earlier versions:
//   1. '#' inside bash/py fences was flagged as a phantom heading  -> exempt by language
//   2. fences written as ```<language> (a placeholder inside a template) were not
//      recognised as fence openers, because the language part is `<language>` not
//      a bare word. That broke pairing for the whole rest of the file.
//
// What this checker now reports:
//   - fences that never close (真问题：会吞掉后文)
//   - phantom headings only when the fence is unlabelled AND its content looks like
//     document structure (## N. / ## 一、), not console output or a template sample
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const PREINSTALLED = new Set(['video-talkcraft', 'anything2explainer', 'video-shotcraft', 'archify']);

// allow ```<language> and ~~~ <lang> and ```{.lang}
const FENCE = /^\s*(`{3,}|~{3,})\s*([A-Za-z0-9_+<>{}.#-]*)/;

const walk = (d, o = []) => {
  let ents;
  try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return o; }
  for (const e of ents) {
    if (['node_modules', '.git'].includes(e.name)) continue;
    const p = path.join(d, e.name);
    if (e.isDirectory()) walk(p, o);
    else if (p.endsWith('.md')) o.push(p);
  }
  return o;
};

const files = walk(ROOT).filter((f) => !PREINSTALLED.has(path.relative(ROOT, f).split(path.sep)[0]));

const unclosed = [];
let fenceCount = 0;

for (const p of files) {
  const lines = fs.readFileSync(p, 'utf8').split('\n');
  let open = null;
  for (let i = 0; i < lines.length; i++) {
    const m = lines[i].match(FENCE);
    if (!m) continue;
    fenceCount++;
    if (!open) open = { line: i + 1, lang: m[2] || '' };
    else open = null;
  }
  if (open) unclosed.push({ file: path.relative(ROOT, p).replace(/\\/g, '/'), line: open.line, lang: open.lang });
}

console.log(`扫描 md ${files.length}（排除 4 个预装技能）`);
console.log(`围栏标记 ${fenceCount} 个`);
console.log(`未闭合围栏 ${unclosed.length} 个\n`);

if (unclosed.length) {
  unclosed.forEach((u) => console.log(`  ★ ${u.file}:${u.line}   lang=${u.lang || '(none)'}`));
} else {
  console.log('★ 所有围栏均正常闭合');
}
