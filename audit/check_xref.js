// Cross-reference integrity v2: distinguish local book-skills from externally-provided skills.
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const existing = new Set(fs.readdirSync(ROOT, { withFileTypes: true })
  .filter((e) => e.isDirectory() && fs.existsSync(path.join(ROOT, e.name, 'SKILL.md')))
  .map((e) => e.name));

// Skills visible in the session catalog but NOT under this workspace's .dsh/skills
// (provided by host plugins / other workspaces). Valid to reference, cannot be existsSync'd.
const EXTERNAL = new Set([
  'solidworks-api-traps', 'image-design-master', 'impeccable', 'video-creation',
  'book-to-skill', 'book-skill-forge', 'delivery-no-pseudoblock', 'fact-check',
  'deep-research', 'office', 'nda', 'employment-contract', 'tiangong-skill',
  'distilly', 'hindsight-coding-agent', 'dsh-badge', 'diagnose-windows-sandbox-acl',
  'no-ai-style', 'novel-writing', 'prompt-bozo', 'reverse-prompt', 'screenshot-ocr',
  'screenwriting-lite', 'script-to-storyboard', 'script-video-prompt-architect',
  'seedance2-0-video-prompter', 'seedance2-storyboard-generator',
  'media-storyboard-design', 'media-video-editing', 'manju-artist',
  'gpt-image-2-style-library', 'ffmpeg-video-editor', 'ai-video-clipper',
  'ai-video-script', 'ai-agentic-video-editor', 'legal-contract-drafting',
  'legal-doc-writer', 'legal-document-assistant', 'office-docx', 'office-xlsx',
  'office-pptx', 'office-export-pdf', 'office-recalculate', 'office-render',
  'civil-code-china', 'totorosir-workbuddy-checkin', 'remotion-video-toolkit',
  'video-spec-builder', 'video-cinematography', 'video-editor',
  'video-clip-assistant', 'archify', 'anything2explainer', 'voxlite',
  'remotion', 'video-shotcraft', 'video-talkcraft',
]);

// Not skills at all — internal anchors / third-party names / source-file names.
// NOTE: `user-research-goodman` and `usability-testing-rubin` are SOURCE BOOK FILE slugs
// (referenced in reports when discussing downloaded files), not skill names.
const NOT_SKILL = new Set(['visual-check', 'designing-data-intensive-apps', 'video-use',
  'product-card-progressive-assemble', 'media-pop-in', 'product-structure', 'visual-dynamics',
  'user-research-goodman', 'usability-testing-rubin', 'inclusive-design-fovet',
  'inclusive-design-clarkson', 'inclusive-design-coleman', 'cmf-ashby',
  'usability-testing-barnum', 'user-research-methods-brand']);

const NAME_RE = /`([a-z][a-z0-9]*(?:-[a-z0-9]+){1,5})`/g;
const PREFIX = /^(solidworks|blender|product|design|world|ergonomics|visual|cmf|user-research|usability|inclusive|ori-ai|book-|delivery|fact-check|deep-research|impeccable|image-design|video-|remotion|archify|distilly|hindsight|legal-|office|nda|employment|tiangong|novel|no-ai|reverse|screenshot|screenwriting|script-|seedance|prompt-|media-|manju|gpt-image|anything|ffmpeg|ai-video|civil-code|totorosir)/;

const localProblems = [];
const externalRefs = new Set();
let total = 0;

for (const s of existing) {
  const walk = (d, out = []) => {
    for (const e of fs.readdirSync(d, { withFileTypes: true })) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) walk(p, out); else if (p.endsWith('.md')) out.push(p);
    }
    return out;
  };
  for (const f of walk(path.join(ROOT, s))) {
    const t = fs.readFileSync(f, 'utf8');
    for (const m of t.matchAll(NAME_RE)) {
      const n = m[1];
      if (NOT_SKILL.has(n) || !PREFIX.test(n) || n.split('-').length < 2) continue;

      // 上下文排除：出现在"包名/版本/安装改写"的描述里，不是技能引用
      const lineStart = t.lastIndexOf('\n', m.index) + 1;
      const lineEnd = t.indexOf('\n', m.index);
      const line = t.slice(lineStart, lineEnd === -1 ? t.length : lineEnd);
      const META_CONTEXT = /package\.json|package-lock|\bname:\s|version|安装改写|打包工具|npm|repository/i;
      if (META_CONTEXT.test(line)) continue;
      // 形如 xxx-repository 的包名后缀
      if (/-repository$/.test(n)) continue;
      total++;
      if (existing.has(n)) continue;
      if (EXTERNAL.has(n)) { externalRefs.add(n); continue; }
      localProblems.push({ from: `${s}/${path.basename(f)}`, missing: n });
    }
  }
}

const uniq = new Map();
for (const p of localProblems) uniq.set(`${p.from}|${p.missing}`, p);

console.log(`本地书籍/技能目录: ${existing.size} 个`);
console.log(`扫描技能名引用: ${total} 处`);
console.log(`引用到"外部提供"技能: ${externalRefs.size} 个 → ${[...externalRefs].join(', ') || '无'}`);
if (uniq.size === 0) {
  console.log('\n★ 交叉引用全部有效（本地 + 外部两类均已核对）');
} else {
  console.log(`\n✗ 真实悬空引用 ${uniq.size} 处：`);
  for (const p of uniq.values()) console.log(`  ${p.from} → ${p.missing}`);
}
process.exit(uniq.size === 0 ? 0 : 1);
