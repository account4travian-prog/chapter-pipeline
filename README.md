# Chapter pipeline — a layered grader stack for long-form generation

A production pipeline that treats every novel chapter as an evaluation task: **the planning packet is the task specification, the model's draft is the attempt, and a stack of independent graders scores it.** Built for the serials Ghost Weights and Glyphbound, published at [reader.wardenlog.org](https://reader.wardenlog.org).

**My role:** designer of the pipeline and its graders, and acceptance authority. Creative decisions and the packet belong to Sol (GPT); prose drafts are written by Claude from the locked packet; orchestration and verification are run by Atlas. Nothing is accepted on a score — my verdict binds the chapter's exact text hash, and any later edit voids the acceptance.

## The grader stack
Intake → packet gate → draft → independent critique (Reviews Board) → diagnostic read → **16-pass revision ladder** (mechanical/tool-grounded passes split from judgement passes) → **technical-accuracy pass that tries to disprove the text's claims** → blind reader gate → hash-bound freeze → release with publish-effect verification (the live page is checked by identity and text hash).

## The measurement layer
- Defect density per 1,000 words, by class and by round
- **Escape rate** — how often one round misses what a later round catches (grader recall)
- Rounds-to-acceptance, gate pass/fail
- An **Avoid Database** of defect checks in tiers: law, tripwires, judgement mechanisms, watchlist — and a **refuted tier**: checks the data disproved, barred from use. Calibrated on 36,431 words of accepted chapters.

## The post-mortem that changed the rules
Chapter 13 was accepted, published — and then failed my full read. I reversed the acceptance (the text stayed live until the accepted fix swapped in; that is now a standing rule), and the acceptance gate was rebuilt hash-bound around the failure. The record of that reversal is part of this repo's point: **graders get graded here, and false passes are kept on the books.**

## Outcomes
- Ghost Weights: 15 chapters accepted through the pipeline (by 2026-10-18)
- Glyphbound: chapters 1–5 accepted and released, hash-verified on Royal Road, Wattpad, and the reader
- Chapter 16: frozen mid-revision at my pause — not accepted, not published, and recorded as exactly that

No chapter prose lives in this repo — the pipeline, its rules, and its scorecards only.
