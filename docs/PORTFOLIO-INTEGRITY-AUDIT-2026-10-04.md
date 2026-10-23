# Portfolio Integrity Audit — 2026-10-04

> Audit-only deliverable for Phase 1 of
> [heyitschien/heyitschien#31](https://github.com/heyitschien/heyitschien/issues/31).
> No links, claims, designs, project pages, or assets were changed as part of this audit.

| Audit field | Value |
| --- | --- |
| Coordination work order | [career-development#149 comment](https://github.com/heyitschien/career-development/issues/149#issuecomment-5985733606) |
| Canonical roadmap | [career-development#257](https://github.com/heyitschien/career-development/issues/257) |
| Review issue | [heyitschien#31](https://github.com/heyitschien/heyitschien/issues/31) |
| ChatGPT audit input | [Latest audit comment on #31](https://github.com/heyitschien/heyitschien/issues/31#issuecomment-5985731602) |
| Audit cycle | `CD-PORTFOLIO-INTEGRITY-20261004-01` |
| Baseline | `main` at `c0263095311a7247d59a0187fdd7168aded29972` |
| Test date | 2026-10-04 (America/Los_Angeles) |

The source work-order comment did not include a handoff ID. The audit-cycle label above was
assigned for this user-authorized, bounded execution.

## Executive verdict

**The GitHub profile front door passes, but the complete recruiter trust path does not yet
pass.** The current README presents the intended five projects in the right order, its local
links and images resolve, and its desktop and mobile layouts are usable. Two deeper public
destinations are broken or misleading enough to be **BLOCKING**:

1. Can AI Yet's live footer sends an unauthenticated visitor to a private repository and a
   GitHub 404 page.
2. Cousin Radio exposes a visible **Pricing** navigation item whose destination is `#`.

Six supporting profile documents also preserve an older portfolio hierarchy. They do not
break the main README, but they create contradictory evidence paths for a recruiter who reads
deeper. The Autonomous Lab pages work as styled HTML, including the four clean routes named in
the issue; however, their visible product naming is behind the current public name, and the
implementation walkthrough overflows slightly on a 390-pixel mobile viewport.

### Result summary

| Area | Result |
| --- | --- |
| Current README front door | **PASS** |
| Local README/docs/image/anchor integrity | **PASS — 99/99 checked references resolved** |
| Required public HTTP destinations | **PASS — all nine required HTTPS URLs returned 200** |
| Required desktop rendering | **PASS**, except the dead destinations described below |
| Required mobile rendering | **PASS**, except implementation-walkthrough horizontal overflow |
| Claims and public/private boundaries | **PASS**, except Can AI Yet's private-repo footer link |
| Full recruiter trust path | **FAIL — 2 BLOCKING defects** |

## Scope and method

The audit began at the current public-facing README and followed the recruiter path through the
five featured projects, the evidence links used by the capability table, and one useful layer
beyond each primary destination. Validation included:

- source inspection of README and linked Markdown;
- a repository-wide check of relative links, image paths, and Markdown anchors in the audited
  path;
- unauthenticated HTTP requests, including redirect checks;
- desktop browser checks at 1440 pixels wide;
- mobile browser checks at 390 pixels wide where practical;
- image decode, horizontal-overflow, raw-Markdown, dead-navigation, and route checks;
- GitHub API checks for repository visibility, pull-request state, merge state, and checks;
- a public-safety review of claims, employment language, private-source boundaries, and status.

This was an integrity audit, not a content rewrite or visual review. No defects were corrected.

## Required HTTP and browser results

| Destination | HTTP / redirect result | Browser result |
| --- | --- | --- |
| [canaiyet.com](https://canaiyet.com/) | HTTPS `200`; HTTP and `www` each `308` to canonical HTTPS apex | Correct Can AI Yet experience; no horizontal overflow on desktop or 390px mobile; no broken visual assets observed |
| [Autonomous Lab root](https://heyitschien.github.io/autonomous-lab-case-study/) | HTTPS `200`; HTTP `301` to HTTPS | Styled case-study root; no raw Markdown links, broken images, or horizontal overflow |
| [Full case study](https://heyitschien.github.io/autonomous-lab-case-study/full-case-study/) | HTTPS `200` | Styled HTML, Mermaid diagram rendered, working return/repository navigation, desktop and mobile usable |
| [Implementation walkthrough](https://heyitschien.github.io/autonomous-lab-case-study/implementation-walkthrough/) | HTTPS `200` | Styled HTML and working exits; 390px viewport overflows to 404px because the H1 does not wrap safely |
| [Validation and risk gates](https://heyitschien.github.io/autonomous-lab-case-study/validation-and-risk-gates/) | HTTPS `200` | Styled HTML, table present, navigation works, no desktop/mobile overflow observed |
| [Attribution and limitations](https://heyitschien.github.io/autonomous-lab-case-study/attribution-and-limitations/) | HTTPS `200` | Styled HTML, public-safety boundaries visible, navigation works, no desktop/mobile overflow observed |
| [cousinradio.com](https://cousinradio.com/) | HTTPS `200`; HTTP `308` to HTTPS | Correct product page; 38 images decoded, no horizontal overflow on desktop or mobile; visible Pricing link is inert |
| [Hack for LA PR #3531](https://github.com/hackforla/tdm-calculator/pull/3531) | HTTPS `200`; GitHub state `MERGED` | Correct upstream PR and title; merged 2026-09-25; desktop rendering usable |
| [Hack for LA PR #3576](https://github.com/hackforla/tdm-calculator/pull/3576) | HTTPS `200`; GitHub state `OPEN`, not draft | Correct upstream PR and title; current checks green; desktop/mobile rendering usable |

Additional redirect and boundary observations:

- `https://www.cousinradio.com/` serves a separate `200` response instead of redirecting to the
  apex and has no canonical link tag. This is not a broken recruiter path, but it weakens URL
  consistency.
- LinkedIn's unauthenticated browser flow reached the expected LinkedIn authentication wall
  with the correct profile encoded in `sessionRedirect`. Command-line requests received
  LinkedIn's expected anti-bot response and were not treated as a portfolio defect.
- All five current Start Here images decoded on the live GitHub profile. The README and direct
  evidence documents produced no missing local image or document paths.

## Findings

### BLOCKING

#### B-01 — Can AI Yet sends public visitors to a private repository

The **GitHub** link in the footer of both the Can AI Yet root page and its methodology page points
to `https://github.com/heyitschien/can-ai-yet`. GitHub reports that repository as private. An
unauthenticated request returns `404`, and an unauthenticated browser lands on GitHub's
**Page not found** screen.

This contradicts the live site's public navigation and creates a recruiter trust failure. The
separate public-safe repository at
`https://github.com/heyitschien/can-ai-yet-case-study` is reachable with `200`.

**Bounded correction:** change the live footer link to the public case-study repository, or
remove the link if the public case study should not be presented there. Do not expose or change
the visibility of the private product repository.

#### B-02 — Cousin Radio's visible Pricing destination is dead

The live header presents **Pricing** as navigation, but its `href` is `#`. It does not lead to a
pricing section or page. The same inert destination is present on both the apex and `www`
versions.

The entry page remains usable, but a visible primary navigation promise that goes nowhere is a
dead-end recruiter/product path under the issue's BLOCKING definition.

**Bounded correction:** link Pricing to a real public destination, or remove/disable the item
until one exists.

### SHOULD FIX

#### S-01 — `docs/README.md` preserves the retired portfolio hierarchy

Its suggested order is Paid Implementation, Can AI Yet, Autonomous Systems, Cousin Radio, and
Chrome Extension Tester MCP. It also says not to promote Hack for LA until evidence merges,
although PR #3531 is now merged and PR #3576 is open under review.

#### S-02 — `docs/WHY-HOW-WHAT.md` contradicts the current front door

It uses **Autonomous Systems Lab**, elevates Chrome Extension Tester MCP, omits Can AI Yet and
Hack for LA from the evidence set, and uses the title-shaped wording **AI Implementation
Specialist** instead of the stable role-family language adopted by the README.

#### S-03 — `docs/CAPABILITY-EVIDENCE-MAP.md` points at weaker default evidence

It uses the old Autonomous Systems name, relies heavily on Chrome Extension Tester MCP and the
Product Support Triage Sample, and does not use Hack for LA as the strongest proof for real team
engineering, peer review, and scoped implementation.

#### S-04 — `docs/IMPLEMENTATION-AI-SYSTEMS.md` has stale proof and status language

It uses the old Autonomous Systems name, features Chrome Extension Tester MCP and Product
Support Triage as primary proof, retains title-shaped role wording, and describes Can AI Yet as
a public-beta product while the current public README describes an early alpha.

#### S-05 — `docs/AI-WORKFLOW-CASE-STUDIES.md` retains the retired flagship five

It uses the previous project order, retains Chrome Extension Tester MCP as a flagship project,
and omits Hack for LA from the primary set.

#### S-06 — `docs/AI-ORCHESTRATED-SYSTEMS-ENGINEERING.md` retains stale naming and support work

It uses the old Autonomous Systems name and an older supporting-project set that no longer
matches the stable recruiter-facing evidence system.

#### S-07 — Autonomous Lab's visible metadata is behind the canonical project name

The live case-study pages still use **Autonomous Lab** in page titles, headers, and document
titles. The current public profile names the project **Autonomous Trading Systems Lab**. The
repository slug may remain stable; the visible naming should be aligned so a recruiter can tell
that the profile card and the case study are the same project.

#### S-08 — Implementation Walkthrough overflows on a 390px viewport

At a 390px viewport, the document has a 404px scroll width. The long
**Implementation Walkthrough** H1 is the offender: its content does not wrap within the mobile
heading width. Other required Autonomous Lab routes did not show the same overflow.

### POLISH

#### P-01 — `assets/portfolio/README.md` no longer describes the current image inventory

The inventory omits the newer `start-here/` feature images and describes older preview images as
if they were the current front-door assets. The images themselves resolve correctly.

#### P-02 — Some supporting documents do not provide an explicit return path

The strongest Can AI Yet and paid-client documents include useful next-step links. A few older
supporting documents rely on GitHub's surrounding interface instead of offering a clear return
to the profile or related proof. This is not a true dead end, but consistent exits would reduce
recruiter friction.

#### P-03 — Cousin Radio serves duplicate apex and `www` entry URLs without a canonical signal

Both hosts return `200`, and no canonical link tag was observed. Choose a preferred host and
redirect or declare it canonically when that deployment is next maintained.

## Claim and public-safety consistency

The following checks passed:

- The current README presents Hack for LA as a **volunteer contribution, not employment**.
- Hack for LA PR #3531 is verifiably merged; PR #3576 is verifiably open and under review.
- No duplicate Hack for LA case-study repository was found or created.
- Can AI Yet's public claims remain bounded to an active early alpha and a defined evaluation
  surface; no customer, revenue, enterprise, or autonomous-operation claim was observed.
- The paid-client case study states that commercial proof exists privately and does not expose
  client-sensitive implementation details.
- The Autonomous Trading Systems Lab evidence keeps consequential action behind a human gate
  and separates public-safe patterns from private operational details.
- Cousin Radio's employer evidence distinguishes product work from SaaS support employment and
  keeps the source repository private.
- No secret, credential, private local path, client identity, or private operational
  configuration was found in the audited public path.

## Recommended bounded correction scope

The next phase should be one integrity-focused correction PR, not a redesign and not a new case
study build:

1. Correct Can AI Yet's public footer repository destination without changing private-repository
   visibility.
2. Remove or correctly route Cousin Radio's inert Pricing navigation item.
3. Fix the implementation-walkthrough mobile H1 overflow.
4. Align the six stale profile documents to the stable five-project order, current project
   names and statuses, role-family wording, and strongest evidence assignments.
5. Align visible Autonomous Lab page metadata and headings to **Autonomous Trading Systems Lab**
   while preserving stable URLs and the repository slug.
6. Refresh the portfolio image inventory and add consistent return navigation only where it can
   be done without expanding the correction into a redesign.

Explicitly out of scope for that correction: redesigning project images, creating a Hack for LA
case-study repository, exposing private source, building the Can AI Yet web case study, building
the paid-client web case study, or rewriting unrelated README sections.

## Audit limitations

- HTTP and browser checks describe the public state observed on 2026-10-04 and can change after
  publication.
- The audit followed the defined recruiter trust path and one useful layer beyond it; it was not
  a crawl of every page in every external product.
- Private repositories and private commercial evidence were checked only for stated boundary
  consistency. Their private contents were not reproduced or evaluated here.
- GitHub and LinkedIn can vary unauthenticated behavior by session and bot protection. Status
  claims were cross-checked with GitHub's API where applicable.
