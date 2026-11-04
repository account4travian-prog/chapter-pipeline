

# Prose Revision Ladder

This skill is Phase 6 (revision passes) of the full chapter workflow —
`~/workspace/custom-skills/local-chapter-workflow/SKILL.md`. For a complete chapter run
(intake → packet → draft → independent critique → diagnostic read → passes →
audit → blind A/B → release), start there.

## Purpose

When a first-pass draft loses to a stronger draft on specific dimensions, do not re-roll the same prompt. Run the full workflow: plan from the packet, draft scene by scene, then run sixteen narrow passes in fixed order, each allowed to touch only its defect class, with a revision log. Narrow passes on ~4,000 words cost less than one higher-tier first pass.

## Authority order

1. The user's latest direct prose and decisions.
2. Canonical manuscript prose and dated project decisions.
3. The project's writing guide, focus, relevant movement, and affected bible records.
4. Cataloged feedback with an accepted or modified disposition.
5. The writer profile and this defect log as process aids.
6. My proposals and outside examples.

No lower source silently overrules a higher one. My drafts are PROPOSED EXPERIMENT — not manuscript canon — until the user accepts them.

## Workflow

**Pre-flight (before drafting):**
1. Read the project's writer/voice profile and the immediately preceding chapter.
2. No draft without the chapter packet. If no packet exists, say so and stop — do not draft from a summary or from memory of the plot.
3. Read the personal defect log (`~/workspace/auditions/AtlasMuse/defect-log.md`) and note which of your recurring failure modes this draft is at risk of.
4. Name the chapter's set piece and its arc in one sentence each before writing.

**Planning (after pre-flight, before drafting a word of prose):**
1. Chapter contract — one line each: the viewpoint character's immediate want, the obstacle, the material change, the relationship change, the end change, the chapter's irreplaceable function, and the causal summary (because X, Y happens).
2. Scene spine — per scene, one line each: goal → conflict → turn (catalog move 9) and reaction → dilemma → decision (move 10). If a scene's turn is "nothing changes," cut or combine it.
3. Ledgers — calendar, physical/resource, knowledge/viewpoint (entry and exit state), visual recognition, dependencies on older chapters. Verify every proper name, rule, and comparison against the project records (writer profile, continuity, bible, prior chapters); never invent a fact the records don't support.
4. Moves selection — pick 2–3 catalog moves and name exactly where each lands in the spine.
5. Defect-risk map — select the three most relevant defect-log entries for
   this draft (house rule); each with one preventive control AND the exact
   scene/beat where the control will be verified (zero-recurrence
   contract).
6. Word budget per scene from the packet's allocation.
7. Packet fields the plan must also carry: the causal hand-off to the *next* chapter; story threads advanced and threads deliberately left untouched; the reader-question ledger (evidence supplied, partial answers, intended payoff horizon); **the reader promise and enjoyment target** (graft: house workflow 2026-09-25, Sol commit 41b367654) — what should be pleasurable, intriguing, moving, or wondrous in the lived reading experience, plus the intended continuation pull; name at least one intended source of wonder, warmth, amusement, suspense, curiosity, or emotional attachment, and one concrete reason the reader should want the next scene — targets for the prose, not permission for decorative incidents; canon/history claims each marked verified, inferred, proposed, or unresolved; the exit-state capsule fields for review-state use; a private scene-intent note per scene (withheld from blind reviewers); the originality receipt ID + decision (PASS required); pressure beyond the packet (the most useful dramatic gap the packet doesn't state, one sentence); one or two voice anchors **with their authority status stated** — accepted author prose where it exists; where none exists (as in ch.1–8, whose manuscript files are placeholders or PROPOSED), provisional attention anchors are hypotheses about attention and cadence only, never phrases to imitate and never a substitute for the author's direct prose decisions (Sol's source-boundary formulation, commit 7a0e36ec7); lines advanced (two or more of external problem, capability, relationship, institution, home, mystery, self-understanding); forbidden imports (revelations, themes, later knowledge the chapter must not import); and for any repeated practical test, the staged-test ledger — one row per trial: operation, input, held constant, changed, visible result, sample provenance, fixture, load path, licensed conclusion.
8. Write the plan down as a chapter packet document before any prose. No prose until the plan exists. Do not pre-write polished dialogue in the plan.

**Drafting (scene by scene):**
1. Draft one scene from the packet while reinjecting only the current scene spine, current story state, and necessary records.
2. Reach the scene's change before polishing.
3. Record any useful departure from the plan before continuing, so later scenes do not follow a stale outline.

**The ladder (fixed order, one defect class per pass):**

Passes run in two tiers. **Tier M (mechanical, tool-grounded):** the check
is a tool or a ledger, not an opinion — same-model execution is fine.
**Tier O (opinion, gradient-gated):** the pass may ONLY target gaps named
by an external gradient — the workflow's critique log (Phase 4), the
diagnostic read (Phase 5), reader acceptance answers (Phase 8), the user's
targeted judgment, or — only when one happens to exist — a stronger-draft
comparison. A Tier O pass that diagnoses its own
gaps and fixes them is the D9 failure mode: fluent same-quality rewrites
that feel like improvement. Log it as such and revert the pass.

1. **[O] Premise and causality.** Every question, answer, reaction, and consequence has an on-page basis. No missing premises used as mystery; no effect without its shown cause. **Single-variable trial discipline** (D28, blind reader 2026-09-25): when a staged test's inference depends on isolating one variable, change exactly one operation per trial — list every physical change the trial makes; if more than one changed, the record must note both and the narration must narrow the inference to what the trial actually supports. **Certainty consistency** (ch.9 blind read 2026-09-25): a diagnosis the viewpoint character cannot verify stays provisional in thought, dialogue, and record alike — the record's conjecture column may not settle what the scene left open, and later narration may not reopen what was declared settled without new evidence.
2. **[O] Body-evidence.** Every inference available to the viewpoint character. One correction = one bodily input. No stock similes. No asserted measurements the character could not know. **No inference about another character's internal state, sensation, or history from a single observed action** (D23, blind reader 2026-09-25): one observed action licenses the action, never the interior — keep the ease seen and the viewpoint character's own missing point of comparison; leave the other's history and sensation unsettled.
3. **[M] Geometry and physical/resource continuity.** Lock orientation, route, and wind; trace every movement on the locked map. Trace bodies, clothing, carried objects, and their end states across scene boundaries. **Physical-account consistency** (D26, blind reader 2026-09-25): collect every claim about an object's state, handling, or location across the chapter — one settled account per scene; any pair that cannot both be true is an error, not a nuance. **Transfer quotation** (D34, ch.9 blind read 2026-09-25): for every physical transfer of a key object, quote the exact sentence that performs it — hand, source, destination. A transfer with no quoted sentence is missing by construction; a trace that summarizes the action instead of quoting it is not a trace. **Transition table** (Ghost Weights 2026-09-29, DSH-c / Sol-2): enumerate every scene boundary AND every intra-scene locative shift. A location change is legal only with a quoted movement sentence or a licensed time-break (recorded, not auto-passed). An intra-scene shift with no movement verb in the window is `MISSING-LINK` and blocks. The ledger records *states* (where objects are at entry/exit); the transition table records *edges* — states without edges pass teleports. Disputed ordinary-movement elisions escalate to Tier O; do not require a door-crossing sentence for every step. **Scene-grounding census (Council Session 4, 2026-09-30 — Class 9 Tier M control, required ladder artifact):** per scene, machine-generated with a SHA-headed receipt and a versioned lexicon — word/sentence counts; **E** (embodied verbs), **A** (ambient/sensory registered by the body), **X** (instrument-mediated tokens: screen action, log-reading, typing), **C** (cognition), object states changed by hand, longest ungrounded run, body trace quoted. X never counts as grounding; code/log blocks supply no grounding credit. Hard hits block until dispositioned (no embodied body-trace in a waking/sleep-onset scene; no human-action E verbs; ungrounded run beyond the calibrated threshold); soft hits escalate to Tier O. Thresholds are calibrated ONCE on accepted ch.1–6 and never used as a cross-chapter quality score — no hard ratio veto, no mandatory sensory detail per scene. Tier O dispositions: fix / intentional stillness (named, reasoned; a packet-declared still scene passes without insertion) / false positive. An undispositioned confirmed hit blocks the revision gate. Re-run after every fix landing per rule 3a-ext; a Class 9 fix names the declared physical-spine beat it serves, passes the relevance test, ships a census-delta receipt, and gets a rule-3b confirmation read of the changed passage and scene. Anti-padding guard: description that neither locates the body, carries state, marks time or cost, nor serves a declared motif is padding, not grounding.
4. **[M] Calendar and elapsed time.** Verify every timestamp, weekday obligation, meal, darkness cue, sleep interval, and accumulated change against the calendar ledger. Elapsed time between scenes must produce its effects. **Typed time notation** (Ghost Weights 2026-09-29, DSH-e / Sol-3): type every `HH:MM` token as CLOCK or DURATION. Mixed-unit same-notation in one clause blocks (require an explicit unit: `12 min 04 s`, `12:04 elapsed`); untyped narration times block; every duration gets an arithmetic receipt against its on-page clock pair (tolerance ±60 s); precision may not exceed its source. No bare `HH:MM` in narration. Note: colon tokens are invisible to quantity-regex sweeps — type them explicitly. **4M-predecessor-numbers** (Council Session 3, 2026-09-30): every number the draft carries across a scene boundary — counts, sums, dates, episode numbers, durations — is checked against `predecessor-facts.md`. The receipt is a table of number → predecessor-facts value + citation; zero unresolved mismatches.
5. **[M/O split] Viewpoint, voice, and forbidden shortcuts.** The grep sweep for banned phrases is Tier M — run it deterministically and fix every hit. Viewpoint/voice judgments (what the character could know, adult summaries) are Tier O — they need a named external gap. If no external gradient names a viewpoint/voice gap, the Tier O half is skipped and logged as skipped, not run on self-diagnosis. **Tier M sub-checks** (Ghost Weights 2026-09-29): **5M-recurrence** (DSH-a / Sol-8) — content n-gram sweep, n=3–6, eligible only with ≥2 non-stopword tokens, flag at 3/2/2/2 occurrences; skip-gram families (ordered content-token pairs, ≤2 intervening) and near-duplicate clusters (token-Jaccard ≥0.75). **Whitespace folding is mandatory** — line-wrapped recurrences undercount in line-based grep. A recurrence is licensed ONLY by a pre-existing packet motif row (log echo, declared motif, or diegetic marker + declaration); no packet row = hit. **5M-shape** (DSH-b) — sentence-shape signatures (subject/verb/polarity/object classes); T1 flags adjacent "X. He didn't." pairs (cognition/volition sentence + ≤5-token negated reply with no object); T2 flags consecutive same openers. **5M-abstraction** (DSH-d / Sol-7) — deterministic seed-pattern grep for vague-abstraction markers; every hit gets the four-question table (Q1 antecedent / Q2 payload-by-decompression / Q3 warrant / Q4 deletion). Verdict: HIT if Q2=restatement OR Q3=unwarranted OR Q4=nothing-lost; Q1 alone never licenses a keep. "No hits" means the scan ran; it does not certify the prose. **5M-standings** (2026-10-10, B2) — sweep the draft against every ruling in `~/workspace/standings/rulings-global.md` + `rulings-<project>.md`: grep where the ruling is lexical (e.g. R-G1 "fitted"→"fit"), careful read where qualitative. The receipt names the rulings file versions swept; any violation fails the gate. A standing ruling is a defect class, not background. **5M-negative-claims** (fleet test 2026-09-28 C1/C2/C6): extract every nobody/never/no-way/"didn't say" sentence; each must be accompanied by an on-page search or audit artifact — a universal claim with no accompanying evidence is a finding. The receipt is the inventory (quote + line) with the accompanying evidence named per item.
6. **[O] Dialogue separation.** Distinct syntax per speaker. Allow plain or incomplete replies. No shared polished buttons — no two speakers land the same kind of line. **Sentence-function check** (Ghost Weights 2026-09-29, Sol-9): for flagged dialogue, identify the intended function of each beat (what is said, what "meant it" refers to); read the paragraph aloud exactly as written and mark where the spoken intention changes.
7. **[O] Visual recognition.** Recurring people, animals, and important spaces must be picturable and consistent; description arrives through viewpoint and action, never inventory. Check against the visual ledger's anchors. **Character evidence check** (Ghost Weights 2026-09-29, Sol-10): for each supporting character with real presence, ask what they do, notice, want, or ask on the page that distinguishes them — appearance and interests separate from invented history. Whether the presence is enough is a senior/author judgment.
8. **[M] Canon and history.** Verify each scene-bearing claim against project records. Mark every historical or canon claim verified, inferred, proposed, or unresolved. Label project invention honestly. **Technical-warrant check** (serial-workflow 2026-09-28): for each load-bearing technical conclusion the viewpoint character states or acts on, the knowledge/viewpoint ledger must cite an accessible source — established skill, observed result, on-page record, named person's explanation, or earlier-passage learning; `missing warrant` blocks the ladder gate. Whether a warranted inference is technically sound is for the technical-accuracy pass, not this one. **Source-linked continuity comparison** (Ghost Weights 2026-09-29, Sol-1): pair every consequential claim with the accepted-passage source establishing its state; facts absent from accepted sources are marked **unknown**, never canon. Reconcile the register against accepted prose, not the reverse — a stale ledger ratifies contradictions. **First-mention referent check** (Ghost Weights 2026-09-29, DSH-f / Sol-4): `the X` is a hit when X's first chapter mention is definite with no prior non-definite/appositive mention and no gazetteer entry; alias clusters (`the file / the copy / the original`) need one grounded member before definite use. Most "it"/"that" instances are clear — this is a candidate generator, not a verdict. **8M-flashback-medium** (chapter-workflow Phase 6, 2026-09-28): any flashback to a canon scene restates that scene's medium — video vs in-person — before the prose writes movement verbs; pair each flashback with the accepted-passage source of the scene it recalls (ch.5 2026-09-28: "walked out" staged a physical office for a 1:1 that ch.2 canon staged as a video call, and it slipped through every review round). The receipt is per flashback: restated medium, canon source citation, match/mismatch verdict.
9. **[O] Story function.** Compare every beat with the movement; cut decorative beats that change nothing of choice, relationship, knowledge, or material condition. **What-changes test for expansion/bridge paragraphs** (D27, blind reader 2026-09-25): each must change at least one thing or carry exactly one load-bearing detail — otherwise cut, however smooth the prose. **Method exposition arrives while recording the observed attempt** (D25, blind reader 2026-09-25): never lecture→demonstrate→restate — each restatement must correct a specific overclaim or be cut, and a limit is stated once, where it changes what gets written or tried.
10. **[O] Question and payoff.** Ledger every reader question: evidence supplied, partial answers, intended payoff horizon. Distinguish intentional mystery from a missing premise. **Interpretation budget** (D24, blind reader 2026-09-25): after a staged result, narration gets one recognition beat (viewpoint-specific) — the record, the request, and dialogue carry the rest. Do not re-interpret the result the action already supplied; that steals the reader's inference.
11. **[O] Relationship consequence.** The ending must advance the central repair with a concrete forward use, not group warmth. If the ending could be swapped into another chapter, it fails. Where continuous intensity has flattened the chapter, restore ordinary contrast or aftermath (house pass 9) — a small normal beat that lets the change land.
12. **[O] Readability.** Read without the packet beside you (graft: house workflow 2026-09-25, Sol commit 41b367654). Check that the viewpoint goal, physical action, speaker identity, time movement, and immediate stakes can be followed on a first pass. Mark every place where a reader must reverse-engineer the premise, route, referent, or emotional change. Tier O: targets gaps named by the critic, the diagnostic read, or the reader acceptance answers (all valid external gradients). **Cause-to-choice bridge** (Ghost Weights 2026-09-29, Sol-6): for each consequential choice, a reviewer must be able to cite the passage supplying each link (new information → interpretation → choice → consequence) and describe the choice in one sentence without importing the packet. Deliberately withheld links are recorded as what the reader is meant to wonder about — a model may not fabricate motives from genre expectations.
13. **[O] Enjoyment and attachment.** Read for the experience of being in the story, not for compliance with the outline (house workflow 2026-09-25). Identify where the chapter offers the promised wonder, warmth, humour, curiosity, tension, relief, or emotional recognition. If the intended pleasure is only described in the plan and not felt in the prose, revise the scene rather than explaining its importance.
14. **[O] Anti-padding and value.** Challenge every paragraph and beat (house workflow 2026-09-25). Each must change a choice, relationship, knowledge state, material condition, reader question, or emotional meaning — or provide necessary lived texture that makes the world or attachment more vivid. Cut or compress material that only restates the plan, delays the next consequence, fills a word target, or explains a theme already visible in action.
15. **[O] Local language.** Repair antecedents, comparisons, repetition, rhythm, and sentence-level clarity. Last. **Abstract-claim voice decisions** (Ghost Weights 2026-09-29, Sol-7): decide the Tier M 5M-abstraction hits — a retained abstraction needs a stated scene function; a changed one is re-checked in context. **Aloud check** (Sol-9): read flagged paragraphs aloud exactly as written; mark the precise point of stumble or ambiguity. An aloud pass cannot certify continuity or motivation — sentence polish can conceal a missing story fact.
16. **[O] Reader-burden check.** List remaining defects honestly instead of declaring victory. A pass that finds nothing is a failed pass — look harder. **Watched-item adjudication:** every residual self-diagnosed worry must carry its external-reader verdict (confirmed → fixed; rejected → retired with the reader's reason quoted) or be marked as blocking the freeze. A retired worry is logged with evidence so it does not resurface as a fresh worry next chapter (ch.9 2026-09-25: the wand-box exit button, retired by blind-reader evidence).

**Deterministic audit gate:**
In the full chapter workflow, the draft-stage audit runs in Phase 3 (before
the ladder) and the release-stage audit in Phase 7 (after it) — both run
the project's own `chapter-control-audit.ps1` via the Linux shim at
`~/workspace/tools/chapter-audit/` (pwsh 7; only path-separator lines
adapted, check logic byte-identical). When the ladder is run standalone,
use the same shim: an error blocks reader review until corrected; a warning
requires inspection and a recorded judgement, not an automatic rewrite.
The Python port `chapter_audit.py` is a fast pre-check only.
**Record locations (2026-10-10, A14 — pinned, no drift):** serial pipeline —
full audit output + exit code pasted in the revision log; the em-dash
count (`grep -c '—'`, literal character — the `$'\u2014'` escape silently
matches nothing) recorded in the freeze record, per `serial-freeze`.
WriteProject chapter-workflow — full result in `NN-audit-record.md` per
its own Freeze convention.

**Blind A/B:**
After the ladder and a clean audit, the draft goes to blind A/B (`~/workspace/auditions/AtlasMuse/blind-ab-protocol.md`) before any claim about quality. Never grade your own draft against a known competitor. Reader feedback is evaluated against the authority order above; agreement is not automatic acceptance, and disagreement requires a reason.

**Release:**
1. Confirm the PROPOSED EXPERIMENT label is on the draft.
2. Run the audit at release stage; record the result.
3. Write the exit-state capsule fields the packet specified.
4. Write the chapter retrospective: what the first draft got wrong, where each defect was detected (detection stage), what the final improved, what the user wanted preserved.
5. Update the defect log from catalogued evidence: new defects in, detection stages recorded, statuses current.
6. Refresh the defect-risk map for the next chapter (the control board).
7. Hand over: the draft, the packet, the revision log, the residual-defects list, the audit result, the retrospective. Do not manufacture a composite quality score. Publication and Studio/Reader read-back verification are the author's steps — never claim them.

## Output Contract

- The chapter packet (planning output): contract, scene spine, ledgers, moves selection, defect-risk map, word budget, plus the extended packet fields (next-chapter hand-off, threads touched/untouched, question ledger, marked canon claims, exit-state capsule, private scene intent).
- One revision log entry per pass as a **change ledger**: finding ID,
  exact span, intended reader effect, old/new wording or scene action,
  and a regression check for affected facts (spot-check every changed
  line; a "fix" that breaks a different class is a regression, not a
  fix). Record a zero-change pass only when it guards a current top-three
  defect-log risk; otherwise a clean pass is one line.
- The revised draft.
- A residual-defects list: what is still wrong, named plainly.
- The audit result (draft stage, then release stage).
- The chapter retrospective with detection stages.

## Stop conditions

1. Do not draft through an unresolved premise involving money, permission, route, chronology, or character knowledge — research or decide it first.
2. Do not act on unexplained aesthetic preference, mine or a reader's; disagreement requires a reason.
3. Do not add more process when the missing input is a user decision or source fact — ask.
4. Do not use an automated score as acceptance evidence.
5. Do not present the Python port's output as the audit — the project's
   own ps1 runs on this VM via the Linux shim.
6. Do not claim a draft is finished while the reader-burden check still lists defects.
7. **Do not run a Tier O (opinion) pass without a named external gap** — a
   critique-log entry, the user's targeted judgment, or — only when one
   exists — a stronger-draft comparison. No gap, no pass.
8. **Do not revise toward a self-diagnosed gap.** Name it in the residual
   list AND route it to the next external reader as a targeted question
   (workflow Phase 8 watched-list adjudication). A watched item with no
   reader verdict blocks freezing.
9. **Do not freeze, commit, or submit a draft for comparison while the
   residual-defects list or completion notes name an open defect.**
   Flagged = blocking. A flagged defect that ships is not "deferred" —
   it is a defect you chose to publish (D29). Unadjudicated watched items
   count as open defects (ch.9 2026-09-25).

## Operating Rules

1. Never skip the order. A later pass may not redo an earlier pass's job.
2. **Re-read the full altered scene after all local fixes.** A correct
   sentence can still damage pacing or setup (house rule).
3. **After a substantial prose expansion** (new attempts, new apparatus, or
   >10% word growth), re-run the affected Tier M passes (physical,
   calendar, canon) and story-function, check the prose's attempt count
   and causal inference against the staged-test ledger, and obtain fresh
   reader attention before release. "Insertions only" does not establish
   that the chapter's causal or continuity state survived.
3a. **AI-ism phrase-family sweep re-runs after EVERY revision cut — no exceptions, including reader-wave fix landings.** (Council Session 2, 2026-09-29: the ch.7 r4 cut's receipts never showed the family greps re-run after the W-fixes landed, letting a author-flagged "shape" instance through.) The sweep covers the WHOLE Tier M phrase-family list (`\bshape[sd]?\b`, `\bthing\b`, `-shaped`, `what (that|it) meant`, `was the \w+est \w+`, the had/wanted frame, `the way [Name] would have`, `\bis the \w+ \w+ing\b` over narration AND dialogue — see the AI-ism field guide). Every hit gets a per-hit disposition filed as an artifact: fixed, or cleared-WITH-RECORDED-REASON (the ch.3 r2 lesson: unrecorded "cleared" hits are how flagged prose reaches the author). A grep hit alone never vetoes; adjudication runs the guide's point-and-show test. **RA-05 guard:** after fixing an AI-ism, re-run the family grep against the REPLACEMENT wording — a cleverer substitute reintroduces the defect in a new form.
3a-db. **Avoid Database Tier B sweep (2026-10-14, author-ratified after the council-poll + research + control-corpus calibration experiment; TRIAL ch.15–17).** Alongside Rule 3a, after every revision cut, run `~/workspace/tools/avoid-db/tier-b-scan.py <draft>` — the Tier B tripwire detectors from the ratified Avoid Database (`~/workspace/prose-avoid-db/DATABASE.md`). These detectors measured 0.00–0.35 hits per 1,000 words on the accepted ch.1–12 control corpus, which is what licenses them: a hit is rare in approved prose, so every hit gets a per-hit disposition filed with the revision log (fixed, or cleared-WITH-RECORDED-REASON, same discipline as 3a). **A Tier B hit is never a fail and never auto-blocks** — the database's Tier R list (fragments, micro-paragraphs, nominalization density, filler bans, burstiness scores…) is REFUTED by the control corpus and must not be reintroduced as checks by any pass. The scanner also prints Tier D watchlist values (C33 register density, C31, C46, C61); record them in the run's trial log (`~/workspace/prose-avoid-db/TRIAL.md`) — watchlist values require no disposition. Trial review after ch.17: entries whose hits are ~always cleared retire; promotions/demotions are the author's ratification only.
3a-ext. **Fix-step mutation gate (Council Session 3, 2026-09-30 — F2/F9).** Rule 3a's discipline extends to EVERY fix landing, including Council-ordered one-liners: the fix step is an ungated mutation surface (ch.7 W8 introduced the "shape" AI-ism at L41; the Council's own L73 fix introduced the coffee-cup defect). Receipts are **machine-generated, never hand-counted** (revision-log-r7 reported `\bthing\b` "5"; the file has 6). Every landed fix carries: the script-generated count receipt, the referent check on the replacement wording, and the regression re-read (Rule 3b).
3b. **Confirmation read — standing Council rule (Council Session 3, 2026-09-30).** After every cut, the defect's finder inspects the changed passage, the full scene, the setup, the callbacks, and the diff — checking both closure AND regression. A one-word prose change is not exempt. (Sol: the highest-value control in the set — it caught the Council's own L73 error.)
3c. **Post-repair paragraph + entry/exit reread (2026-10-11, Sol ch.12 prevention, author-authorized).** After ANY cut or replacement, reread the changed paragraph AND the affected scene's entry and exit. Record what the reread establishes (in the revision log) and any out-of-scope concern it surfaces — a concern outside the bounded contract is reported to Atlas for scope, never silently expanded. A closed finding is NOT evidence that adjacent prose is clear. An earlier candidate's reader pass does not transfer to the new revision — the reread is fresh every time.
4. A pass touches only its defect class. If pass 6 spots a geometry error, log it for pass 3's next run — do not fix it in pass 3.
5. Line-level polish is not a pass. If the draft's weakness is architecture (arc, set piece, sequence fit), spend passes there.
6. Every new defect found by a reader goes into the defect log with its fix, its detection stage, and its evidence, so the next draft's pre-flight catches it. Comparison-report findings are logged with their finding IDs; the revision that addresses them is verified by a fresh restricted reader against the finding list before it replaces the frozen candidate (ch.9 2026-09-25).
9. **Finding quotas (2026-09-28):** wherever this ladder or the workflow asks a reader or critic for findings, the quota is "up to five substantiated findings; for each: evidence, reader effect, uncertainty. Stop when none remain" — never "top N." "No findings in my lane" is an allowed, recorded outcome. (Binger pacing output and stylistic counts are diagnostic by construction — see the profiled-reader-fleet skill; they never enter the ladder as defect claims.)
7. Retirement: a `guarded` entry with no recurrence in the last 3 judged drafts becomes `retired`; a retired entry that recurs reopens as `open`. At movement boundaries, consolidate or lower stable controls. An endlessly growing checklist is not accumulated wisdom.
8. Pass retirement: at each movement boundary, review the ladder — a pass
   that produced no accepted findings across the movement is a retirement
   candidate; decorative passes retire. A retired pass reopens if a judged
   chapter proves it needed. (Sol review 2026-09-25: the research does not
   validate sixteen fixed passes; keep mandatory source/mechanics gates,
   run only opinion passes tied to a high-priority observed reader effect.)

## Changelog

- 2026-09-28 (Royal Road review-mining operation, Sol + DSH): pass 8
  gains the technical-warrant check — each load-bearing technical
  conclusion needs a ledger-cited accessible source; `missing warrant`
  blocks the ladder gate. No pass added, removed, or reordered.
- 2026-09-29 (Operation "Iron the prose" — the author's 50 ch.6 notes, 5 Luna
  research workers, Sol synthesis, DSH mechanical/adversarial): pass 3 gains
  the transition table (edges, not just states; intra-scene MISSING-LINK
  blocks); pass 4 gains typed HH:MM notation (mixed-unit/untyped block);
  pass 5 gains 5M-recurrence (n-gram + packet motif license), 5M-shape
  (T1/T2), 5M-abstraction (seed grep + four-question table); pass 8 gains
  source-linked continuity comparison and the first-mention referent check;
  Tier O methods mapped without new passes (dialogue sentence-function → 6,
  character evidence → 7, cause-to-choice bridge → 12, abstract-claim voice
  + aloud → 15). Canonical defect taxonomy:
  `~/workspace/custom-skills/local-serial-workflow/defect-taxonomy.md`. No pass added,
  removed, or reordered.

- 2026-09-29 (Council Session 2, ch.7 r4): new Operating Rule 3a —
  AI-ism phrase-family sweep re-runs after EVERY revision cut (no
  exceptions, incl. reader-wave fix landings); whole family list,
  per-hit dispositions filed, cleared-with-recorded-reason, grep hit
  alone never vetoes, RA-05 re-run guard on replacement wording.
- 2026-09-30 (Council Session 3, ch.7 process retrospective): Rule 3a-ext —
  fix-step mutation gate (every fix landing incl. Council one-liners;
  machine-generated receipts, never hand-counted; referent check on
  replacements — F2/F9); new Rule 3b — confirmation reads as a standing
  Council rule (finder inspects changed passage + scene + setup +
  callbacks + diff; no one-word exemption — F3).
- 2026-10-10 (pipeline advisory A1): pass 4 gains 4M-predecessor-numbers
  (every cross-boundary number checked against predecessor-facts.md,
  receipt = number → predecessor-facts value + citation); pass 5 gains
  5M-negative-claims (nobody/never/no-way/"didn't say" inventory, each
  item named with its accompanying on-page evidence); pass 8 gains
  8M-flashback-medium (each flashback's restated medium paired against
  the canon scene's accepted-passage source). Each ships its receipt in
  5M-standings style; no pass added, removed, or reordered.
- 2026-10-11 (Sol ch.12 prevention, author-authorized): new Rule 3c —
  post-repair paragraph + scene entry/exit reread after any cut or
  replacement, with out-of-scope concerns reported to Atlas. Trial over
  three chapters.
## Available connectors

Use `muse.connector_search` to find the current connector docs before following
recovered instructions.
