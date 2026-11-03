# Chapter pipeline: a grader stack for long-form generation

Each chapter is an evaluation task: the planning packet is the task specification, the model's draft is the attempt, and a stack of independent graders scores it. Built for Ghost Weights and Glyphbound, published at [reader.wardenlog.org](https://reader.wardenlog.org).

**My role:** designer of the pipeline and its graders, and acceptance authority. Creative decisions and the packet belong to Sol (GPT); Claude writes the drafts from the locked packet; Atlas runs orchestration and verification. Nothing is accepted on a score: my verdict binds the chapter's exact text hash, and any later edit voids it.

## Measured grader quality
- Defect density per 1,000 words, by class and by round.
- **Escape rate, two-sided:** defects a round missed, and accepted fixes later reversed, with no wave-to-wave comparison at n=1. A re-screen of five accepted chapters found **8 real defects that had escaped acceptance**; all 8 were fixed on my order.
- Rounds-to-acceptance and gate pass/fail.
- An **Avoid Database** of defect checks in tiers: law, tripwires, judgment mechanisms, watchlist, and a **refuted tier** of checks the data disproved, barred from use. Calibrated on 36,431 words of accepted chapters; adopted checks sit at or below 0.35 hits per 1,000.

## The chapter 13 reversal
Chapter 13 passed the full gauntlet, I accepted it on 2026-10-14, and it published. My full read that evening reversed the verdict, with 22 notes, after every automated and model grader had passed it. I ruled the text stays public until an accepted fix swaps in, and the acceptance gate was rebuilt hash-bound around the failure. The rebuild failed the blind reader gate on a restatement loop the other gates could not see; the accepted r6 revision replaced it on all three platforms, swap verified 39/39. The record of that reversal stays in this repo on purpose.

## The gate stack
Intake, packet gate, draft, independent critique (Reviews Board), diagnostic read, a 16-pass revision ladder (mechanical passes split from judgment passes), a technical-accuracy pass that tries to disprove the text's claims, a blind reader gate, a hash-bound freeze, and release with publish-effect verification.

## Outcomes
- Ghost Weights: 15 chapters accepted through the pipeline (by 2026-10-18).
- Glyphbound: chapters 1 to 5 accepted and released, hash-verified on Royal Road, Wattpad, and the reader.
- Chapter 16: the r3 candidate was frozen on 2026-10-20 (2,825 words) and presented for verdict; the final small revision was written and not sent; chapters 17 to 20 are holds, with no acceptance and no release recorded.

No chapter prose is kept in this repo. It holds the pipeline, its rules, and its scorecards.
