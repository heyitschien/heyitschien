# Portfolio Evidence Registry

This registry connects recruiter-facing claims to the repository, work order,
public artifact, and validation result that support them. It is a publication
control, not a claim that every source repository is public or every packet is
approved.

**Last audited:** 2026-08-31  
**Controlling brief:** [Linear HEY-361](https://linear.app/heyitschien/issue/HEY-361/publish-ai-implementation-and-systems-builder-portfolio-v1) · [GitHub issue #17](https://github.com/heyitschien/heyitschien/issues/17)

## Status key

- `not-started` — no source audit or usable artifact yet
- `source-audited` — source and current public surface inspected
- `evidence-ready` — public artifact meets the current evidence contract
- `draft-pr` — a focused draft change exists and awaits review
- `human-approved` — a human approved the public-safe packet
- `published` — the approved artifact is live and linked
- `blocked` — a permission, privacy, readiness, or validation gate remains

## Recruiter path

| Profile claim | Owning source | Work order / provenance | Public artifact | Status | Validation / boundary |
| --- | --- | --- | --- | --- | --- |
| Paid independent client implementation | Private `cindy-read-room`; public summary in this repository | Private work order `cindy-read-room#1`; [HEY-385](https://linear.app/heyitschien/issue/HEY-385/portfolio-v1-paid-client-implementation-evidence-and-public-case-study) | [Public-safe case study](PAID-CLIENT-IMPLEMENTATION-CASE-STUDY.md) | `blocked` | Summary exists, but claim ledger, client permission, redaction review, and artifact approval are not evidenced. Do not identify the client or expose the client-specific preview until approved. |
| Public-safe complex systems case study | `trading` source; `autonomous-lab-case-study` public surface at `42e2873d21fa5b22ec86071da725f15f6f05efe2` | [autonomous-lab-case-study #2](https://github.com/heyitschien/autonomous-lab-case-study/issues/2) · private source PR `trading#183` · [HEY-365](https://linear.app/heyitschien/issue/HEY-365/flagship-case-study-1-autonomous-lab-autonomous-trading-system) | [Case-study repository](https://github.com/heyitschien/autonomous-lab-case-study) · [implementation walkthrough](https://github.com/heyitschien/autonomous-lab-case-study/blob/main/docs/IMPLEMENTATION-WALKTHROUGH.md) · [validation and risk gates](https://github.com/heyitschien/autonomous-lab-case-study/blob/main/docs/VALIDATION-AND-RISK-GATES.md) | `source-audited` | Public packet is reviewable and clearly non-production; source PR is still draft/dirty and the publication gate remains open. No strategy, credentials, financial data, or live-trading claim. |
| Shipped public-beta product delivery | Private `family-jukebox` source; public `cousin-radio` showcase at `e02cbc414d807e21c0dc8f961191257965c9dc57` | [cousin-radio #2](https://github.com/heyitschien/cousin-radio/issues/2) · [HEY-367](https://linear.app/heyitschien/issue/HEY-367/flagship-case-study-2-cousin-radio-product-orchestration) | [Live product](https://cousinradio.com) · [employer proof](https://github.com/heyitschien/cousin-radio/blob/main/docs/EMPLOYER-PROOF.md) · [engineering overview](https://github.com/heyitschien/cousin-radio/blob/main/docs/ENGINEERING.md) | `source-audited` | Live URL and public proof resolve. Family, invitation, authentication, and security-sensitive details remain out of the profile. Full case-study package is queued behind flagship sequencing. |
| Working open-source AI browser-QA tool | `chrome-extension-tester-mcp` at `938204444e811eabb9d36179cba375d907ff98eb` | [chrome-extension-tester-mcp #2](https://github.com/heyitschien/chrome-extension-tester-mcp/issues/2) · [HEY-387](https://linear.app/heyitschien/issue/HEY-387/portfolio-v1-chrome-extension-tester-mcp-implementation-case-study) | [Repository](https://github.com/heyitschien/chrome-extension-tester-mcp) · [QA walkthrough](https://github.com/heyitschien/chrome-extension-tester-mcp/blob/main/docs/SUPPORT-USE-CASE.md) · [CI run](https://github.com/heyitschien/chrome-extension-tester-mcp/actions/runs/29670849954) | `source-audited` | Source, screenshots, console evidence, CI, and merged PR are public. The linked npm identity does not match this repository, so npm is not used as proof until corrected. |

## Supporting proof

| Capability / project | Owning source and provenance | Public artifact | Status | Validation / boundary |
| --- | --- | --- | --- | --- |
| Workflow coordination and human gates | Private `career-development` | [Public-safe Career OS case study](CAREER-OPERATING-SYSTEM-CASE-STUDY.md) · [HEY-386](https://linear.app/heyitschien/issue/HEY-386/supporting-evidence-career-development-os-public-safe-capsule) · private work order `career-development#125` | `blocked` | Summary is intentionally sanitized; private applications, employer correspondence, salary strategy, schedules, and records are not public evidence. |
| Support judgment and escalation | `product-support-triage-sample` at `a2524e870c828963c6f7d2cf2f2e6b0dafd64225` | [Completed case](https://github.com/heyitschien/product-support-triage-sample/blob/main/CASE-OUTCOME.md) · [customer response](https://github.com/heyitschien/product-support-triage-sample/blob/main/customer-reply.md) | `evidence-ready` | Synthetic educational material, not live employer ticket history. The public `internal-escalation-note.md` is not used as a recruiter link. |
| Localization configuration and QA | `next-i18next-sample` at `02a764794c29a42b95749b099749d6f257077eb8` | [Sample review](https://github.com/heyitschien/next-i18next-sample/blob/main/docs/sample-bot-pr.md) · [configuration](https://github.com/heyitschien/next-i18next-sample/blob/main/.lingopilot.yml) | `source-audited` | Public demo with four locales and pseudo-localization; no production adoption or public automation claim. |
| Local-first desktop delivery | `chapter-reader` at `22584c06de3c3216454a9ac647260e992f2da8c5` | [Repository and install path](https://github.com/heyitschien/chapter-reader) · [Mac installer](https://github.com/heyitschien/chapter-reader/blob/main/install-mac-app.sh) | `source-audited` | Public local utility. A prior private `printing-intelligence-on-sand` destination is not used. |
| Content-system design | `ai-youtube-content` at `de172515db0a76a08f3994960314cfa8ea1eea55` | [Production workflow](https://github.com/heyitschien/ai-youtube-content/blob/main/docs/production-workflow.md) · [content calendar](https://github.com/heyitschien/ai-youtube-content/blob/main/planning/content-calendar.md) | `source-audited` | Active pre-production system; episode packages are drafts and are not represented as published videos. |

## Alias map

| Working name | Repository or surface | Interpretation |
| --- | --- | --- |
| Autonomous Systems Lab | `trading` → `autonomous-lab-case-study` | Private implementation source and public-safe case-study surface; not the same as a public production trading application. |
| Cousin Radio | `family-jukebox` → `cousin-radio` | Private application source and public showcase; public links point only to the showcase and live product. |
| Paid client implementation | `cindy-read-room` → this profile repository | Private read room and public-safe summary; publication remains permission-gated. |
| Career Development OS | `career-development` → this profile repository | Private operating system and sanitized public capsule; no private repository link belongs in recruiter navigation. |
| Localization QA / LingoPilot | `next-i18next-sample` | Public demo label for the repository; the repository name remains the canonical URL. |

## Link audit

The following public URLs returned HTTP 200 during the 2026-08-31 audit:

- `cousinradio.com`
- Cousin Radio employer proof and engineering overview
- Autonomous Lab public repository and walkthrough documents
- Chrome Extension Tester MCP repository, QA walkthrough, and CI run
- Product Support Triage completed case and customer response
- Localization sample review and configuration
- Chapter Reader repository and installer
- AI YouTube production workflow and content calendar

LinkedIn is retained in the profile contact section, but automated validation
received an anti-bot response rather than a reliable link result. That is not
evidence that the URL is dead.

## Publication gates still open

1. Obtain human approval for the paid-client sanitized packet and image use.
2. Resolve the draft/dirty Autonomous Lab source PR and close its public-case-study gate.
3. Complete the Cousin Radio and MCP evidence work orders before calling their full packages portfolio-ready.
4. Keep all private-source summaries, profile sidebar changes, repository pins,
   merges, and external messages under human approval.
