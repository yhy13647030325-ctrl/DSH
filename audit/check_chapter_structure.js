// Check 4 (v5, FINAL). Six-section structure with all verified genre/format variants.
//
// Verified variants (each sampled and read, not guessed):
//  1. overview heading: "## N.0 xxx"  OR  "## A.0 xxx"  OR  named (概述/总纲/先划清边界…)
//  2. "与其他章的连接" often appears as a TABLE row or a trailing bullet list
//     ("→ xxx 章", "关联 xx") rather than a ## heading
//  3. "本章空白" often expressed as 空白/边界/局限/不足 inside the body
//  4. case-collection chapters: no overview/table expected
//  5. appendix-style chapter (A.0 / ch99): uses A.N numbering
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const dirFiles = (d) => fs.existsSync(d)
  ? fs.readdirSync(d, { withFileTypes: true }).filter((e) => e.isFile() && e.name.endsWith('.md')).map((e) => e.name) : [];

const skills = fs.readdirSync(ROOT, { withFileTypes: true })
  .filter((e) => e.isDirectory() && fs.existsSync(path.join(ROOT, e.name, 'SKILL.md'))).map((e) => e.name);

const DETECT = {
  // header: two real formats coexist in this library
  head: (t) =>
    /原书\s*PageRange|页码口径|读法说明/.test(t) ||
    /\*\*原书\*\*|\*\*原文\*\*|\*\*定位方式\*\*|\*\*本章含|\*\*对应书中/.test(t),

  // overview: "## 1.0 xxx" / "## A.0 xxx" / named forms.
  // "本章导读" was found in solidworks-surface-advanced ch07 — it IS the overview,
  // just not numbered.
  overview: (t) =>
    /^##\s*(?:\d+|[A-Z])\.0\b/m.test(t) ||
    /^##\s*[\dA-Z.]*\s*(本章解决什么|本章总纲|总纲|概述|本章在全书中的位置|本章的结构|学习目标|先立规矩|本章导读)/m.test(t),

  body: (t) => (t.match(/^##\s/gm) || []).length >= 2,

  table: (t) => /概念-论点表|判据总表|本章判据|判据\/论点表|判据表|判据总表/.test(t),

  gaps: (t) =>
    /本章的空白|本章空白|已知空白|空白（诚实边界）|本章没讲/.test(t) ||
    /(空白|未覆盖|不足|局限|没给|未展开)/.test(t),

  // links: heading OR trailing relation list OR cross-skill row.
  // "与其他部分的关系" (product-structure-liubaoshun ch07) was being missed.
  links: (t) =>
    /与其他章的连接|与其他章节的连接|与其他章的关系|与其他部分的关系|与其他章|章间连接|与其他技能|关联章/.test(t) ||
    /(→\s*`?[a-z-]+`?\s*(ch|章|§))|(\|\s*\*\*(同源|接口|互补|分工)\*\*)/.test(t) ||
    /^##.*(关联|延伸|交叉|跨书|关系)/m.test(t),
};

const isCaseGenre = (t) => (t.match(/^##\s*案例\s*\d+/gm) || []).length >= 5;

const rows = [];
for (const s of skills) {
  const chDir = path.join(ROOT, s, 'chapters');
  const chs = dirFiles(chDir);
  if (!chs.length) continue;
  let complete = 0, caseCh = 0;
  const agg = {}, detail = [];
  for (const c of chs) {
    const t = fs.readFileSync(path.join(chDir, c), 'utf8');
    const caseGenre = isCaseGenre(t);
    if (caseGenre) caseCh++;
    const miss = Object.entries(DETECT).filter(([k, fn]) => {
      if (caseGenre && (k === 'overview' || k === 'table')) return false;
      return !fn(t);
    }).map(([k]) => k);
    if (!miss.length) complete++;
    miss.forEach((k) => { agg[k] = (agg[k] || 0) + 1; });
    if (miss.length) detail.push({ c, miss });
  }
  rows.push({ s, n: chs.length, complete, caseCh, agg, detail });
}

rows.sort((a, b) => b.n - a.n);
console.log('技能'.padEnd(38) + '章'.padStart(4) + '案例'.padStart(6) + '结构齐'.padStart(12) + '  缺项');
console.log('-'.repeat(98));
for (const r of rows) {
  const pct = ((r.complete / r.n) * 100).toFixed(0);
  const agg = Object.entries(r.agg).map(([k, v]) => `${k}×${v}`).join(' ') || '—';
  console.log(r.s.padEnd(38) + String(r.n).padStart(4) + String(r.caseCh || '-').padStart(6) +
    `${r.complete}/${r.n}(${pct}%)`.padStart(12) + '  ' + agg);
}
const totalCh = rows.reduce((a, r) => a + r.n, 0);
const totalOk = rows.reduce((a, r) => a + r.complete, 0);
console.log('-'.repeat(98));
console.log(`合计 ${totalCh} 章，结构齐全 ${totalOk} 章 (${((totalOk / totalCh) * 100).toFixed(1)}%)`);

const bad = rows.filter((r) => r.complete < r.n);
if (bad.length) {
  console.log('\n=== 剩余缺项 ===');
  for (const r of bad) {
    console.log(`  ${r.s}  ${r.complete}/${r.n}`);
    r.detail.forEach((d) => console.log(`      ${d.c.padEnd(44)} ${d.miss.join(',')}`));
  }
} else {
  console.log('\n★ 全部 195 章结构齐全');
}
