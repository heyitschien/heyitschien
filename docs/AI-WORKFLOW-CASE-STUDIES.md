# AI Workflow Case Studies

These concise case studies show how I combine human judgment, AI reasoning, documentation, repositories, and implementation tools. They focus on my responsibility and verifiable public evidence rather than broad claims.

## 1. Cousin Radio

**Context**  
A family music product needed to move from an emotional idea into a usable, mobile-first experience with age-aware discovery, reliable playback, deployment, and ongoing iteration.

**My responsibility**  
I led product direction, clarified the user experience, made scope and architecture decisions, coordinated implementation, reviewed behavior, managed deployment concerns, and kept the project aligned with the family use case.

**AI and tool roles**

- reasoning models for UX exploration, architecture discussion, and documentation;
- coding agents for implementation and refactoring;
- GitHub for pull requests, protected branches, review history, and CI;
- Vercel and Supabase for deployment and application services.

**Decisions I made**

- prioritize a mobile-first family experience;
- separate public exploration from private/family controls;
- preserve persistent playback across navigation;
- use staged validation and branch protection rather than direct uncontrolled changes.

**Evidence produced**

- shipped public repository;
- live product;
- employer-facing project documentation;
- versioned implementation and deployment history.

**Result**  
A real, deployed product rather than a static demo.

**What I learned**  
AI can accelerate implementation, but product coherence still depends on sustained human decisions about users, scope, quality, and integration.

Evidence: [repository](https://github.com/heyitschien/cousin-radio) · [live product](https://cousinradio.com)

---

## 2. Product Support Triage Sample

**Context**  
Employers needed concrete proof that I could own a technical support issue from initial report through investigation, communication, escalation, and documentation.

**My responsibility**  
I defined the support scenario, structured the investigation, separated customer-facing communication from internal technical notes, and translated the result into a recruiter-safe artifact.

**AI and tool roles**

- reasoning models for scenario challenge and communication review;
- GitHub for transparent structure and evidence;
- Markdown for reusable support artifacts.

**Decisions I made**

- keep the scenario synthetic and free of private customer data;
- distinguish confirmed facts from hypotheses;
- communicate status before final resolution;
- make the escalation actionable so the next owner would not restart the investigation.

**Evidence produced**

- customer reply;
- investigation notes;
- escalation handoff;
- documentation-improvement proposal;
- role-mapping document.

**Result**  
A public portfolio artifact that demonstrates calm support ownership and structured technical communication.

**What I learned**  
Good support work is a systems discipline: reduce ambiguity, preserve evidence, communicate clearly, and hand off without losing context.

Evidence: [repository](https://github.com/heyitschien/product-support-triage-sample)

---

## 3. Chrome Extension Tester MCP

**Context**  
Browser-extension testing can become repetitive and inconsistent when every check is performed manually.

**My responsibility**  
I shaped the use case around repeatable AI-assisted QA, selected the workflow boundaries, coordinated implementation, and emphasized observable test behavior instead of trusting generated code alone.

**AI and tool roles**

- coding agents for implementation;
- model reasoning for test design and failure analysis;
- GitHub for source control and review;
- browser tooling for observable validation.

**Decisions I made**

- treat the tool as QA support rather than an authority;
- preserve repeatable test steps;
- collect evidence from actual browser behavior;
- keep human review responsible for acceptance.

**Evidence produced**

- public codebase;
- documented test workflow;
- reusable tooling for technical support and QA scenarios.

**Result**  
A practical example of connecting AI assistance to an evidence-producing test process.

**What I learned**  
Automation is most valuable when it makes verification repeatable, not when it merely generates more output.

Evidence: [repository](https://github.com/heyitschien/chrome-extension-tester-mcp)

---

## 4. LingoPilot Public Demo

**Context**  
Localization changes are difficult to review when configuration, pseudo-localization, screenshots, and GitHub collaboration are disconnected.

**My responsibility**  
I helped define a GitHub-native workflow that makes localization problems visible before launch and presents the work in a reviewable public demo.

**AI and tool roles**

- reasoning models for workflow and configuration analysis;
- coding agents for implementation support;
- GitHub pull requests for reviewable automation output;
- screenshots and pseudo-localization as validation artifacts.

**Decisions I made**

- make the workflow visible through GitHub rather than a hidden black box;
- prioritize pre-launch QA;
- separate the public proof from private engine components;
- document the sample bot behavior for recruiters and reviewers.

**Evidence produced**

- public sample application;
- example automation PR documentation;
- localization QA workflow.

**Result**  
A focused demonstration of configuration discipline, automation, and reviewable quality checks.

**What I learned**  
A strong automation system should leave understandable evidence for the people responsible for approving the change.

Evidence: [repository](https://github.com/heyitschien/next-i18next-sample)

---

## 5. Chapter Reader

**Context**  
Reviewing long-form writing only on screen made it harder to hear pacing, repetition, and awkward language.

**My responsibility**  
I turned that personal workflow need into a local Mac utility, made privacy and simple installation part of the product design, and documented it as a usable tool rather than a tutorial exercise.

**AI and tool roles**

- models for product clarification, implementation support, and documentation review;
- coding agents for application development;
- GitHub for source, releases, and issue history;
- local operating-system speech for offline use.

**Decisions I made**

- keep text-to-speech local rather than requiring cloud APIs;
- prioritize simple Mac installation;
- make the utility useful for real writing review;
- document privacy and setup clearly.

**Evidence produced**

- public application repository;
- one-command installation;
- local-first technical design;
- user-facing documentation.

**Result**  
A shipped personal productivity utility that solves a concrete problem.

**What I learned**  
Small tools become credible products when implementation, setup, privacy, and user explanation are designed together.

Evidence: [repository](https://github.com/heyitschien/chapter-reader)

---

## 6. Career Operating System

**Context**  
Job search and career operations are easy to treat as ad-hoc messaging. I needed a durable system for role research, proof artifacts, follow-up tracking, interview prep, and application packages without exposing private application data publicly.

**My responsibility**  
I designed the workflow, defined what belongs in durable documentation versus private notes, structured how AI assistance should accelerate research and drafting, and kept final judgment, prioritization, and outreach decisions human-owned.

**AI and tool roles**

- reasoning models for role research synthesis, interview prep drafts, and communication refinement;
- Cursor and coding agents for repository structure, documentation updates, and workflow tooling;
- GitHub and Markdown as versioned operating memory;
- issue-style tracking for priorities and follow-ups.

**Decisions I made**

- treat career work as an operating system, not a pile of prompts;
- keep private application details out of public portfolio materials;
- reuse the same ambiguity → evidence → decision → documentation loop used in support and product work;
- make proof artifacts easy to route to recruiters from the public profile.

**Evidence produced**

- public profile routing to recruiter-safe proof;
- private workflow practice summarized without confidential contents;
- transferable operating pattern shared with implementation, onboarding, and product support work.

**Result**  
A repeatable career-operations method that demonstrates workflow design under ambiguity, without publishing private application records.

**What I learned**  
The same orchestration discipline that ships products also makes job search and interview prep more coherent: clarify the goal, compare evidence, decide, document, and revise.

Evidence: summarized on the [public profile](https://github.com/heyitschien) — private repository contents are not published

---

## Shared operating pattern

Across these projects, the repeated capability is:

```text
clarify the real problem
→ compare evidence and perspectives
→ make an accountable decision
→ translate it into tracked work
→ use specialized AI tools for execution
→ review observable results
→ document what changed
→ revise when evidence disagrees
```

The models accelerate parts of the work. My responsibility is to create coherence across the parts and decide what is accepted.