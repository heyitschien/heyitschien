# Visual case-study standard

Use this pattern for recruiter-facing “Read the summary” pages and deeper public showcase repositories.

## Two-surface model

### Summary surface

Goal: a recruiter understands the problem, method, evidence, and role fit in 30–60 seconds.

Target length: approximately 80–150 lines with no more than three major diagrams.

Required sequence:

```text
Hero + status
→ problem
→ system / workflow
→ evidence boundary
→ hiring signals
→ deeper public path
```

### Deep public repository

Goal: a technical reviewer can spend five minutes or longer understanding the architecture, method, evidence, and limitations without needing private source.

Recommended sections:

```text
Hero + product state
→ five-minute employer scan
→ problem
→ visual workflow
→ evidence model
→ agent / human ownership
→ high-level technical shape
→ current bounded status
→ deeper docs
→ privacy boundary
```

## Visual rules

- Use one coherent palette and typographic mood per case study.
- Prefer real product screenshots when the interface itself is evidence.
- Prefer clearly labeled concept diagrams when workflow, architecture, or validation is the evidence.
- Never style a conceptual diagram as if it were a real result screenshot.
- Keep one main idea per image.
- Include concise, specific alt text.
- Keep editable SVG source and render a PNG for reliable GitHub display.
- Use visual status labels only when the underlying evidence supports them.
- Do not fabricate dashboards, customers, usage, test results, or business impact.

## Content rules

Every page should answer:

1. What real problem or uncertainty existed?
2. What did Chien own?
3. What system or workflow was built?
4. How was expected behavior validated?
5. What evidence is public?
6. What remains private, incomplete, blocked, or unproven?
7. Why does this matter for the target role?

## Truth and privacy gate

Before publication:

- inspect current accepted evidence rather than relying on memory;
- separate current state from historical receipts;
- remove secrets, credentials, identifiers, private data, and raw evidence payloads;
- keep environment levels and proof states distinct;
- label alpha, beta, research, synthetic, sandbox, and production surfaces accurately;
- avoid enterprise, customer, revenue, or reliability claims without direct support;
- ensure every deeper link is publicly accessible.

## Can AI Yet? implementation

- Short visual summary: [CAN-AI-YET-CASE-STUDY.md](CAN-AI-YET-CASE-STUDY.md)
- Deep public case study: [heyitschien/can-ai-yet-case-study](https://github.com/heyitschien/can-ai-yet-case-study)
- Private product source: intentionally not linked from the public profile
- Live product: [can-ai-yet.vercel.app](https://can-ai-yet.vercel.app) — alpha / active development
