// P3 verification: design-router structure + skill-name existence.
const fs = require('fs');
const path = require('path');

const SKILLS_ROOT = 'D:\\deepseek 工作\\.dsh\\skills';
const FILE = path.join(SKILLS_ROOT, 'design-router', 'SKILL.md');

if (!fs.existsSync(FILE)) {
  console.error('MISSING design-router/SKILL.md');
  process.exit(1);
}
const t = fs.readFileSync(FILE, 'utf8');

let fails = 0;
const ok = (cond, label, extra = '') => {
  console.log(`${cond ? 'PASS' : 'FAIL'}  ${label}${extra ? '  ' + extra : ''}`);
  if (!cond) fails++;
};

// 1) 37 themes
// count rows in the section headed by 37 主题
const sec = t.split(/^## /m).find((s) => /37\s*主题/.test(s.slice(0, 40)));
const themeRows = sec ? (sec.match(/^\|\s*\*{0,2}[^|]{2,40}?\*{0,2}\s*\|\s*\d+\s*\/\s*(?:13|17|18|19)\s*\|/gm) || []) : [];
ok(themeRows.length === 37, '37 主题表行数 == 37', `实际 ${themeRows.length}`);

// 2) every skill mentioned exists (skip known non-book / metaskill names)
const NON_BOOK_SKILLS = new Set(['solidworks-api-traps', 'design-router', 'impeccable', 'image-design-master', 'video-creation', 'book-to-skill', 'book-skill-forge', 'delivery-no-pseudoblock', 'fact-check', 'deep-research']);
const skillNames = [...new Set([...t.matchAll(/`([a-z0-9][a-z0-9-]{6,60})`/g)].map((m) => m[1]))]
  .filter((n) => /^(solidworks|blender|product|design|world|ergonomics|visual|cmf|user-research|usability|inclusive|ori-ai)/.test(n))
  .filter((n) => !NON_BOOK_SKILLS.has(n));
const missing = skillNames.filter((n) => !fs.existsSync(path.join(SKILLS_ROOT, n)));
ok(missing.length === 0, '所有引用的技能名都存在', missing.length ? 'missing: ' + missing.join(', ') : `共 ${skillNames.length} 个`);

// 3) no TODO
const bad = ['TODO', '待补', '（略）', '(略)', 'FIXME'].filter((b) => t.includes(b));
ok(bad.length === 0, '无 TODO/待补/（略）', bad.join(','));

// 4) boundary section retained
ok(/什么时候不用|不用本技能|边界/.test(t), '保留"什么时候不用本技能"边界段');

// 5) Ashby four steps must NOT say document
const ashby = /Translation[^]{0,400}Ranking/.test(t);
ok(ashby, "Ashby 四步用原文措辞 Translation→…→Screening+Ranking");
const badDoc = /translate\s*(→|->|—>)\s*screen/i.test(t) || /screen[^]{0,20}rank[^]{0,20}document/i.test(t);
ok(!badDoc, '未出现 translate→screen→rank→document 的错误写法');

// 6) description states the current skill count
const desc = (t.match(/^description:\s*(.+)$/m) || [, ''])[1];
const EXPECTED_COUNT = 19;
ok(new RegExp(`${EXPECTED_COUNT}\\s*个`).test(desc), `description 写的是 ${EXPECTED_COUNT} 个技能`, desc.slice(0, 60));

// 7) key sections present
for (const s of ['独占资产', '三层', '组合', '反问']) {
  ok(t.includes(s), `含「${s}」段`);
}

// 8) chapter/skill count sanity
const allSkills = fs.readdirSync(SKILLS_ROOT, { withFileTypes: true })
  .filter((e) => e.isDirectory() && fs.existsSync(path.join(SKILLS_ROOT, e.name, 'SKILL.md'))).length;
console.log(`\nINFO  技能目录总数（含非书籍类）= ${allSkills}`);
console.log(`INFO  design-router/SKILL.md 行数 = ${t.split('\n').length}, 字符 = ${t.length}`);
console.log(`\n${fails === 0 ? 'ALL PASS' : fails + ' FAIL(S)'}`);
process.exit(fails === 0 ? 0 : 1);
