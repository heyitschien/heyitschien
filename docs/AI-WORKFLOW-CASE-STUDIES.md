# AI Workflow Case Studies

Public-safe case studies showing how I combine human judgment, AI reasoning, documentation, repositories, and implementation tools.

Flagship trio for recruiters:

```text
Support judgment
+ shipped product ownership
+ AI-assisted technical validation
```

Methodology overview: [AI-Orchestrated Systems Engineering](AI-ORCHESTRATED-SYSTEMS-ENGINEERING.md). Attribution: [Model and tool attribution](MODEL-AND-TOOL-ATTRIBUTION.md).

---

## Flagship 1 — Product Support Triage Sample

**What it is**  
A synthetic support sample (no private customer data) showing ticket ownership from report through investigation, customer communication, escalation, and documentation.

**My responsibility**  
I defined the scenario, structured the investigation, separated customer-facing communication from internal notes, and made the escalation actionable so the next owner would not restart the work.

**Distinct decisions**

- keep the case synthetic and recruiter-safe;
- distinguish confirmed facts from hypotheses;
- communicate status before final resolution;
- close with a documentation-improvement proposal.

**Evidence**

| Artifact | Link |
| --- | --- |
| Full case outcome | [CASE-OUTCOME.md](https://github.com/heyitschien/product-support-triage-sample/blob/main/CASE-OUTCOME.md) |
| Customer reply | [customer-reply.md](https://github.com/heyitschien/product-support-triage-sample/blob/main/customer-reply.md) |
| Escalation handoff | [internal-escalation-note.md](https://github.com/heyitschien/product-support-triage-sample/blob/main/internal-escalation-note.md) |
| Role mapping | [ROLE-MAPPING.md](https://github.com/heyitschien/product-support-triage-sample/blob/main/ROLE-MAPPING.md) |

**Result**  
Clear public proof of calm support ownership and structured technical communication.

**Limitation**  
Synthetic sample — not a live employer ticket history.

**Lesson**  
Good support work is a systems discipline: reduce ambiguity, preserve evidence, communicate clearly, hand off without losing context.

---

## Flagship 2 — Cousin Radio

**What it is**  
A shipped family music product — live at [cousinradio.com](https://cousinradio.com) — with mobile-first discovery, persistent playback, deployment ownership, and ongoing iteration.

**My responsibility**  
I led product direction, clarified the family use case, made scope and architecture decisions, coordinated implementation, reviewed behavior, and managed deployment concerns.

**Distinct decisions**

- prioritize a mobile-first family experience;
- separate public exploration from private/family controls;
- preserve persistent playback across navigation;
- use staged validation and branch protection rather than uncontrolled changes.

**Evidence**

| Artifact | Link |
| --- | --- |
| Live product | [cousinradio.com](https://cousinradio.com) |
| Employer proof | [EMPLOYER-PROOF.md](https://github.com/heyitschien/cousin-radio/blob/main/docs/EMPLOYER-PROOF.md) |
| Repository | [cousin-radio](https://github.com/heyitschien/cousin-radio) |

**Result**  
A real deployed product rather than a static demo.

**Limitation**  
Public beta / family product — not an enterprise SaaS case study.

**Lesson**  
AI can accelerate implementation; product coherence still depends on sustained human decisions about users, scope, quality, and integration.

---

## Flagship 3 — Chrome Extension Tester MCP

**What it is**  
A working open-source MCP tool for AI-assisted Chrome extension QA: real browser control, screenshots, UI interaction, and console evidence. Published on npm; CI present.

**My responsibility**  
I shaped the use case around repeatable AI-assisted QA, set workflow boundaries, coordinated implementation, and insisted on observable browser behavior instead of trusting generated code alone.

**Distinct decisions**

- treat the tool as QA support, not an authority;
- preserve repeatable test steps;
- collect evidence from actual browser behavior;
- keep human review responsible for acceptance.

**Evidence**

| Artifact | Link |
| --- | --- |
| Support / QA use case | [SUPPORT-USE-CASE.md](https://github.com/heyitschien/chrome-extension-tester-mcp/blob/main/docs/SUPPORT-USE-CASE.md) |
| CI workflow | [ci.yml](https://github.com/heyitschien/chrome-extension-tester-mcp/blob/main/.github/workflows/ci.yml) |
| Repository | [chrome-extension-tester-mcp](https://github.com/heyitschien/chrome-extension-tester-mcp) |

**Result**  
A practical example of connecting AI assistance to an evidence-producing test process.

**Limitation**  
Working tool and concept demo — not an enterprise QA platform.

**Lesson**  
Automation is most valuable when it makes verification repeatable, not when it merely generates more output.

---

## Supporting examples

| Project | What it shows | Best evidence | Scope note |
| --- | --- | --- | --- |
| **Chapter Reader** | Local-first Mac utility: offline TTS, one-command install, privacy-first writing review | [Repository](https://github.com/heyitschien/chapter-reader) · [install-mac-app.sh](https://github.com/heyitschien/chapter-reader/blob/main/install-mac-app.sh) | Personal productivity utility, not a SaaS product |
| **LingoPilot public demo** | GitHub-native localization QA: pseudo-loc, screenshots, reviewable automation output | [sample-bot-pr.md](https://github.com/heyitschien/next-i18next-sample/blob/main/docs/sample-bot-pr.md) | Public demo; private engine/dashboard not published |
| **AI YouTube Content** | Content-system design: standards, episode packages, production and publishing workflows | [production-workflow.md](https://github.com/heyitschien/ai-youtube-content/blob/main/docs/production-workflow.md) | Content operations system, not a shipped app |
| **Career Operating System** | Private job-search operating system: role research, proof routing, follow-ups — same ambiguity → evidence → decision loop | Summarized on the [public profile](https://github.com/heyitschien) only | Private; no application data published |

---

## Shared pattern

```text
Question → research → challenge → synthesis → architecture
→ implementation → evidence → revision
```

Depth varies by project. Models accelerate parts of the work. I remain responsible for coherence and what is accepted.
