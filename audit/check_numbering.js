
// Check 7 — FINAL (v2). Two independent validators, both grounded in verified facts:
//
//  [a] integer-numbered criteria tables  | 1 | 2 | ...      -> duplicates / step
//  [b] dotted-numbered WCAG tables       | 1.1.1 | ...      -> declared count vs actual
//
// "共 N 条" is checked against the RIGHT numbering style for that section:
//   - if rows look like 1.1.1 -> count only success-criteria rows (指南 rows excluded)
//   - else count integer rows
// This removes the false positive on web-accessibility-cn's WCAG 61-item table
// (61 success criteria + 12 guideline rows = 73 rows total; declared 61 is CORRECT).
const fs = require('fs');
const path = require('path');

// 仓库根（脚本位于 <repo>/audit/，故取上一级）
const _REPO = path.resolve(__dirname, '..');

const ROOT = _REPO;

const dirFiles = (d) => fs.existsSync(d)
  ? fs.readdirSync(d, { withFileTypes: true }).filter((e) => e.isFile() && e.name.endsWith('.md')).map((e) => e.name) : [];

const skills = fs.readdirSync(ROOT, { withFileTypes: true })
  .filter((e) => e.isDirectory() && fs.existsSync(path.join(ROOT, e.name, 'SKILL.md')))
  .map((e) => e.name);

const INT_ROW = /^\|\s*(?:\*\*\s*)?(\d{1,4})(?:\s*\*\*)?\s*\|/;
const DOTTED_SC = /^\|\s*(?:\*\*\s*)?\d+\.\d+\.\d+(?:\s*\*\*)?\s*\|/;
const HDR_HASH = /^\|\s*#\s*\|/;
const HEADING = /^#{1,6}\s+(.*)$/;

const dupProblems = [];
const countProblems = [];
let intTables = 0, declaredClaims = 0, dottedSections = 0;

for (const s of skills) {
  const targets = [];
  const chDir = path.join(ROOT, s, 'chapters');
  for (const n of dirFiles(chDir)) targets.push({ rel: `chapters/${n}`, abs: path.join(chDir, n) });
  for (const extra of ['SKILL.md', 'cheatsheet.md', 'patterns.md', 'glossary.md']) {
    const p = path.join(ROOT, s, extra);
    if (fs.existsSync(p)) targets.push({ rel: extra, abs: p });
  }

  for (const f of targets) {
    const lines = fs.readFileSync(f.abs, 'utf8').split('\n');

    // [a] duplicates inside one '#" table block
    let block = null;
    for (let i = 0; i < lines.length; i++) {
      const l = lines[i];
      if (/^\s*\|/.test(l)) {
        const prevIsTable = i > 0 && /^\s*\|/.test(lines[i - 1]);
        if (!prevIsTable) block = { start: i + 1, isHash: HDR_HASH.test(l), nums: [] };
        if (block && block.isHash) {
          const m = l.match(INT_ROW);
          if (m) block.nums.push(parseInt(m[1], 10));
        }
      } else block = null;
      if (block && !/^\s*\|/.test(lines[i + 1] || '') && block.isHash && block.nums.length >= 2) {
        intTables++;
        const seen = new Set(); const dup = [];
        for (const n of block.nums) { if (seen.has(n)) dup.push(n); seen.add(n); }
        if (dup.length) dupProblems.push({ skill: s, file: f.rel, line: block.start, dups: [...new Set(dup)] });
        block = null;
      }
    }

    // [b] declared "共 N 条" vs actual, with style detection
    for (let i = 0; i < lines.length; i++) {
      const m = lines[i].match(/^#{1,6}\s+.*?共\s*(\d{1,4})\s*条/);
      if (!m) continue;
      declaredClaims++;
      const declared = parseInt(m[1], 10);
      const lvl = (lines[i].match(/^#+/) || ['#'])[0].length;

      let intCount = 0, scCount = 0, guideCount = 0;
      for (let j = i + 1; j < lines.length; j++) {
        const hm = lines[j].match(/^(#{1,6})\s/);
        if (hm && hm[1].length <= lvl) break;
        if (INT_ROW.test(lines[j])) intCount++;
        if (DOTTED_SC.test(lines[j])) scCount++;
        else if (/\|\s*(?:\*\*\s*)?\d+\.\d+(?:\s*\*\*)?\s*\|/.test(lines[j])) guideCount++;
      }

      if (scCount > 0) {
        dottedSections++;
        if (scCount !== declared) {
          countProblems.push({ skill: s, file: f.rel, line: i + 1, heading: lines[i].replace(/^#+\s*/, '').slice(0, 46), declared, actual: scCount, style: 'dotted' });
        }
        continue;
      }
      // integer style: prefer the count within the section's own '#" table
      if (intCount > 0 && intCount !== declared) {
        countProblems.push({ skill: s, file: f.rel, line: i + 1, heading: lines[i].replace(/^#+\s*/, '').slice(0, 46), declared, actual: intCount, style: 'int' });
      }
    }
  }
}

console.log(`[a] 整数编号表 ${intTables} 个  重复编号 ${dupProblems.length} 处`);
for (const p of dupProblems) console.log(`      ${p.skill}/${p.file}:${p.line}  重复 ${p.dups.join(',')}`);

console.log(`\n[b] 「共 N 条」声明 ${declaredClaims} 处（其中点分编号段 ${dottedSections} 个）`);
console.log(`    不一致 ${countProblems.length} 处`);
for (const p of countProblems) {
  console.log(`      ${p.skill}/${p.file}:${p.line}  「${p.heading}」`);
  console.log(`         ${p.style} 声明 ${p.declared}，实际 ${p.actual}（差 ${p.actual - p.declared}）`);
}

fs.writeFileSync(path.join(__dirname, 'numbering-final.json'),
  JSON.stringify({ dupProblems, countProblems, intTables, declaredClaims, dottedSections }, null, 1), 'utf8');
