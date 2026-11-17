
// Comprehensive encoding audit across the whole skills library.
// Checks: leading BOM, stray U+FEFF anywhere, invalid UTF-8, mixed line endings.
const fs = require('fs');
const path = require('path');

// 仓库根（脚本位于 <repo>/audit/，故取上一级）
const _REPO = path.resolve(__dirname, '..');

const ROOT = _REPO;

const walk = (d, o = []) => {
  let ents;
  try { ents = fs.readdirSync(d, { withFileTypes: true }); } catch { return o; }
  for (const e of ents) {
    const p = path.join(d, e.name);
    if (e.isDirectory()) {
      if (e.name === 'node_modules' || e.name === '.git') continue;
      walk(p, o);
    } else if (p.toLowerCase().endsWith('.md')) o.push(p);
  }
  return o;
};

const files = walk(ROOT);
// 预装技能不参与编码审计（上游文件、不进版本控制）
const PREINSTALLED = new Set(['video-talkcraft', 'anything2explainer', 'video-shotcraft', 'archify', 'book-to-skill']);
const files2 = files.filter((f) => !PREINSTALLED.has(path.relative(ROOT || '.', f).split(path.sep)[0]));
const report = { leadingBom: [], strayBom: [], invalidUtf8: [], mixedEol: [], crlf: 0, lf: 0 };

for (const f of files2) {
  const rel = path.relative(ROOT, f);
  const buf = fs.readFileSync(f);

  // 1) leading BOM
  if (buf.length >= 3 && buf[0] === 0xef && buf[1] === 0xbb && buf[2] === 0xbf) report.leadingBom.push(rel);

  // 2) stray U+FEFF beyond position 0
  const text = buf.toString('utf8');
  const firstAt = text.indexOf('\uFEFF');
  if (firstAt > 0) report.strayBom.push({ file: rel, pos: firstAt });

  // 3) invalid UTF-8 round-trip
  if (Buffer.compare(Buffer.from(text, 'utf8'), buf) !== 0) report.invalidUtf8.push(rel);

  // 4) line endings
  const crlf = (text.match(/\r\n/g) || []).length;
  const lf = (text.match(/(?<!\r)\n/g) || []).length;
  if (crlf && lf) report.mixedEol.push({ file: rel, crlf, lf });
  if (crlf && !lf) report.crlf++;
  if (lf && !crlf) report.lf++;
}

console.log(`md files scanned : ${files.length}`);
console.log(`\n[1] leading BOM      : ${report.leadingBom.length}`);
report.leadingBom.forEach((f) => console.log('    ' + f));

console.log(`\n[2] stray U+FEFF     : ${report.strayBom.length}`);
report.strayBom.slice(0, 10).forEach((x) => console.log(`    ${x.file} @${x.pos}`));

console.log(`\n[3] invalid UTF-8    : ${report.invalidUtf8.length}`);
report.invalidUtf8.slice(0, 10).forEach((f) => console.log('    ' + f));

console.log(`\n[4] line endings     : pure-CRLF=${report.crlf}  pure-LF=${report.lf}  MIXED=${report.mixedEol.length}`);
report.mixedEol.slice(0, 10).forEach((x) => console.log(`    ${x.file}  CRLF=${x.crlf} LF=${x.lf}`));

fs.writeFileSync(path.join(__dirname, 'encoding_audit.json'), JSON.stringify(report, null, 1), 'utf8');
console.log('\nwrote encoding_audit.json');
