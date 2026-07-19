# Public Portfolio Audit

Recruiter-facing audit of the six primary public repositories referenced from this profile.

**Date:** 2026-07-19  
**Method:** Inspected each repository README and key docs via GitHub API; validated deep links with HTTP checks from this profile pass.  
**Scope:** Presentation and evidence routing — not a request to rewrite every repo in this PR.

Classification:

- **Critical** — confusing, broken, misleading, or missing essential proof
- **High value** — materially improves recruiter comprehension
- **Optional** — polish with limited conversion value
- **No change** — already strong for the 30-second scan

---

## Summary table

| Repository | Type | 30s clarity | Best evidence | Priority |
| --- | --- | --- | --- | --- |
| [product-support-triage-sample](https://github.com/heyitschien/product-support-triage-sample) | Synthetic sample | Strong | [CASE-OUTCOME.md](https://github.com/heyitschien/product-support-triage-sample/blob/main/CASE-OUTCOME.md) | No change |
| [cousin-radio](https://github.com/heyitschien/cousin-radio) | Shipped / public beta | Strong | [cousinradio.com](https://cousinradio.com) · [EMPLOYER-PROOF.md](https://github.com/heyitschien/cousin-radio/blob/main/docs/EMPLOYER-PROOF.md) | Optional |
| [chrome-extension-tester-mcp](https://github.com/heyitschien/chrome-extension-tester-mcp) | Working tool / concept demo | Strong | [SUPPORT-USE-CASE.md](https://github.com/heyitschien/chrome-extension-tester-mcp/blob/main/docs/SUPPORT-USE-CASE.md) · [screenshots](https://github.com/heyitschien/chrome-extension-tester-mcp/tree/main/docs/screenshots) | No change |
| [chapter-reader](https://github.com/heyitschien/chapter-reader) | Shipped local utility | Strong | [README](https://github.com/heyitschien/chapter-reader) · [install-mac-app.sh](https://github.com/heyitschien/chapter-reader/blob/main/install-mac-app.sh) | Optional |
| [next-i18next-sample](https://github.com/heyitschien/next-i18next-sample) | Concept demo | Strong | [sample-bot-pr.md](https://github.com/heyitschien/next-i18next-sample/blob/main/docs/sample-bot-pr.md) | Optional |
| [ai-youtube-content](https://github.com/heyitschien/ai-youtube-content) | Content system | Medium | [production-workflow.md](https://github.com/heyitschien/ai-youtube-content/blob/main/docs/production-workflow.md) | High value |

---

## 1. product-support-triage-sample

| Question | Finding |
| --- | --- |
| What it is | Synthetic product-support triage case |
| Capability | Ticket ownership, customer reply, escalation, documentation |
| Status | Synthetic / educational sample — explicitly not a real customer case |
| Fastest review path | CASE-OUTCOME → customer-reply → internal-escalation-note (~5 min) |
| Best evidence | `CASE-OUTCOME.md`, `customer-reply.md`, `internal-escalation-note.md`, `ROLE-MAPPING.md` |
| Demo / screenshot | Screenshots and triage-flow assets under `docs/screenshots/` |
| Limitations | Not live employer ticket history |

**Priority: No change** — already recruiter-optimized.

**Follow-up:** None required for profile clarity.

---

## 2. cousin-radio

| Question | Finding |
| --- | --- |
| What it is | Family-first music platform |
| Capability | Shipped product ownership, deployment, UX judgment, layered troubleshooting |
| Status | Live public beta at cousinradio.com |
| Fastest review path | Live site → EMPLOYER-PROOF.md |
| Best evidence | Live product, `docs/EMPLOYER-PROOF.md`, screenshot set under `assets/screenshots/` |
| Demo / screenshot | Live site + extensive screenshots |
| Limitations | Family product / public beta — not enterprise SaaS tenure proof |

**Priority: Optional**

**Follow-up (other repo):** Add a one-line “Hiring managers start here” link to `EMPLOYER-PROOF.md` near the top of the README if not already prominent after the hero.

---

## 3. chrome-extension-tester-mcp

| Question | Finding |
| --- | --- |
| What it is | MCP server for AI-assisted Chrome extension testing |
| Capability | AI-assisted QA, browser evidence, support instrumentation |
| Status | Working open-source tool + concept demo (npm + CI) |
| Fastest review path | Recruiter quick scan → SUPPORT-USE-CASE.md |
| Best evidence | `docs/SUPPORT-USE-CASE.md`, real screenshots under `docs/screenshots/`, console evidence under `docs/evidence/`, CI workflow |
| Demo / screenshot | Yes — working popup + blank-popup repro + browser session (`npm run capture-evidence`) |
| Limitations | Working tool and concept demo — not an enterprise QA platform |

**Priority: No change** (completed 2026-07-19)

**Follow-up (other repo):** Done — added filled screenshots, console logs, demo fixtures, and `npm run capture-evidence`. Preserve the “working tool / not enterprise platform” framing.

---

## 4. chapter-reader

| Question | Finding |
| --- | --- |
| What it is | Local Mac listening app for long-form drafts |
| Capability | Local application delivery, setup clarity, privacy-first design |
| Status | Shipped local utility (MIT) |
| Fastest review path | README Start here → install-mac-app.sh → Preview screenshots |
| Best evidence | README install path, `install-mac-app.sh`, `docs/screenshots/mac-app.png` |
| Demo / screenshot | Yes |
| Limitations | Personal productivity utility — not a multi-tenant product |

**Priority: Optional**

**Follow-up (other repo):** None critical. Optional: pin a one-line “Employer proof” blurb linking install + privacy claims.

---

## 5. next-i18next-sample (LingoPilot demo)

| Question | Finding |
| --- | --- |
| What it is | Public demo for GitHub-native localization QA |
| Capability | Configuration discipline, pseudo-loc, screenshot validation |
| Status | Concept demo — private engine/dashboard not public |
| Fastest review path | README → `docs/sample-bot-pr.md` → screenshots |
| Best evidence | `docs/sample-bot-pr.md`, `.lingopilot.yml`, `screenshots/` |
| Demo / screenshot | Yes (pseudo-loc route screenshots) |
| Limitations | Demo surface only; not a customer-facing localization product |

**Priority: Optional**

**Follow-up (other repo):** Ensure README “What this is / is not” remains above the fold (already strong).

---

## 6. ai-youtube-content

| Question | Finding |
| --- | --- |
| What it is | Content production system for an AI education YouTube channel |
| Capability | Content-system design, standards, production/publishing workflows |
| Status | Active content operations repository |
| Fastest review path | README mission → `docs/production-workflow.md` |
| Best evidence | `docs/production-workflow.md`, `docs/publishing-workflow.md`, templates |
| Demo / screenshot | Screenshot folder present but sparse |
| Limitations | Content system, not a software product demo; channel growth claims should stay evidence-backed |

**Priority: High value**

**Follow-up (other repo):**

1. Add a short **Recruiter quick path** (3 bullets) at the top of the README.
2. State explicitly: content operations system — not a shipped app or SaaS product.
3. Link `docs/production-workflow.md` in the first screen.

---

## Profile-repo changes in this PR

Implemented here (safe, in-profile only):

- tightened `README.md` as a routing page;
- elevated capability → evidence table with deep links;
- condensed case studies to three flagships + supporting table;
- added this audit document;
- updated docs index.

Deferred to other repositories (documented above, not edited in this PR):

- **Done:** MCP filled screenshots + console evidence ([chrome-extension-tester-mcp#1](https://github.com/heyitschien/chrome-extension-tester-mcp/pull/1))
- **High value (later):** AI YouTube Content recruiter quick path
- **Optional:** Cousin Radio / Chapter Reader polish

---

## Privacy boundary

This audit does not include private trading systems or collaborator-sensitive material. Public claims remain grounded in public-safe evidence only.
