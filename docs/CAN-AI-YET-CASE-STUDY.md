# Can AI Yet? — AI Capability Evaluation Lab

<!-- markdownlint-disable MD033 -->
<p align="center">
  <a href="https://github.com/heyitschien/can-ai-yet-case-study">
    <img src="https://raw.githubusercontent.com/heyitschien/can-ai-yet-case-study/main/assets/hero.png" alt="Can AI Yet public-safe capability evaluation laboratory: real task to bounded contract, evidence, independent review, and honest proof state" width="920" />
  </a>
</p>

**Test the work. Keep the claim honest.**

| | |
| --- | --- |
| **What it is** | A working evaluation laboratory for testing AI agents and tool integrations against bounded business workflows |
| **What I own** | Eval design, requirements/contracts, integration validation, evidence, diagnosis, agent routing, review loops, and claim boundaries |
| **Product state** | **Alpha / active development** — the interface, catalog, and evidence will change |
| **Public boundary** | Private source, credentials, identifiers, raw receipts, and security-sensitive implementation details are omitted |

**[Explore the deeper public case study →](https://github.com/heyitschien/can-ai-yet-case-study)** · **[Open the live alpha →](https://canaiyet.com)**

---

## The real question

The useful question is not simply:

> “Can AI do this?”

It is:

> **What exactly must happen, what evidence would prove it, what failed, and what are we justified in claiming?**

If an agent says it updated a CRM but the target system did not change, the capability did not pass.

---

## From task to evidence

<p align="center">
  <img src="https://raw.githubusercontent.com/heyitschien/can-ai-yet-case-study/main/assets/evaluation-loop.png" alt="Six-stage evaluation loop: bound the task, freeze success, run safely, inspect reality, challenge independently, and label the proof state honestly" width="920" />
</p>

```text
real workflow
→ bounded contract
→ expected + forbidden outcomes
→ agent run with limited tools
→ authoritative world-state checks
→ machine receipts + visual corroboration
→ independent review / correction
→ explicit proof state
```

I combine **test-first work where truth is deterministic** with **evidence-first work where external reality is unknown**. Independent review challenges the assumptions that green tests may still encode incorrectly.

---

## Evidence levels stay separate

<p align="center">
  <img src="https://raw.githubusercontent.com/heyitschien/can-ai-yet-case-study/main/assets/evidence-ladder.png" alt="Evidence ladder separating claims, controlled simulation, real software sandbox, controlled pilot, and repeated production measurement" width="920" />
</p>

Can AI Yet? preserves explicit proof states:

| State | Meaning |
| --- | --- |
| **PROVEN** / bounded **LIVE_PROVEN** | Accepted evidence supports one narrow, named claim |
| **DRY-CERTIFIED** | A deterministic path passed controlled checks — **not** live-proven |
| **CONFIGURED_NOT_LIVE_PROVEN** | Configuration exists; live capability has not been established |
| **BLOCKED** | An explicit external or authorization boundary stops progress |
| **NOT_PROVEN** | The claim remains open and must not be presented as demonstrated |

Simulation is not a sandbox. A sandbox is not a pilot. Configured is not proven.

---

## What the current work demonstrates

- capability and scenario contracts for lead-follow-up workflows;
- deterministic expected-versus-forbidden world-state checks;
- a controlled mini-business for safe evaluation;
- real HubSpot sandbox/integration work with bounded schema evidence;
- dependency-injected dry certification before separately authorized live work;
- machine-readable evidence, authoritative rereads, and visual corroboration;
- TDD and regressions for evidence-critical behavior;
- independent review that has found and corrected false-positive risks;
- human control over objectives, privacy, spend, live actions, and final claims.

## Current boundary

The full HubSpot CAP-001 environment is **not** presented as end-to-end live-proven. Dry-certified lifecycle work is **not** presented as live-proven. Configured scenarios are **not** presented as production-ready.

This is not an enterprise-adoption, customer-deployment, revenue-impact, autonomous-operation, or generalized model-reliability claim.

---

## Hiring signal

| Capability | What this work shows |
| --- | --- |
| AI implementation | Turn a real workflow into contracts, tools, checks, and a usable evidence path |
| Integration validation | Separate API support, authorization, environment configuration, and live proof |
| Evaluation design | Test actions and world state rather than persuasive output alone |
| Diagnosis | Attribute failures to model, tool, auth, environment, adapter, or judge before fixing |
| Agent coordination | Route scouting, building, independent review, and publication through durable handoffs |
| Responsible delivery | Keep blocked and unproven work visible; require human approval for consequential actions |

---

## Go deeper

- **[Public case-study repository →](https://github.com/heyitschien/can-ai-yet-case-study)** — visual README, architecture, methodology, evidence boundaries, and public plan
- **[Live alpha →](https://canaiyet.com)** — early product surface under active development
- **[Reusable visual case-study standard →](VISUAL-CASE-STUDY-STANDARD.md)** — the pattern used for this summary

The private product repository remains the engineering source of truth and is intentionally not linked as a public evidence surface.
<!-- markdownlint-enable MD033 -->
