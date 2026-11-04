

# Chapter Workflow

Repeatable end-to-end cycle for one chapter: intake → pre-flight →
planning → drafting → **independent critique (external gradient)** →
diagnostic read → **split revision ladder** → deterministic audit gate →
**hardened blind A/B** → release. Each phase has a gate; nothing is
declared done until every phase's gate passes. Built from the chapter-6
pilot; redesigned 2026-09-23 after research into why the ladder failed to
close the Atlas-versus-Sol-High gap. Self-sustainable by design: no phase
requires a stronger model's output.

**Research basis (2026-09-23, verified sources).**
- Same-model opinion self-critique without external feedback is net-zero
  to net-negative and amplifies self-bias (Huang et al., ICLR 2024,
  https://arxiv.org/abs/2310.01798; Xu et al., ACL 2024,
  https://arxiv.org/abs/2402.11436). → Opinion passes require an external
  gradient; they may never self-diagnose.
- Critique works when grounded in tools and deterministic evidence
  (CRITIC, Gou et al., ICLR 2024, https://arxiv.org/abs/2305.11738).
  → Mechanical checks stay tool-grounded and run ungated.
- Judgment improves when it is independent, blinded, and rubric-narrowed
  — even at the same capability tier. Blind peer review with independent
  revision improved short fiction, with smaller models using the framework
  reportedly surpassing larger single-agent models (LLM Review, 2026,
  https://arxiv.org/abs/2601.08003 — short fiction only, modest human
  study; correlated blind spots remain when critic and drafter share a
  model family, so keep diagnosis separate from revision and narrow
  judgment to dimensional tests). → Independent critique (Phase 4) is the
  core correction mechanism, not the ladder — and the gradient comes from
  role separation and restricted context, not from a better text.
- Planning-first with a detailed hierarchical outline plus an
  adherence control beats adding more revision passes (DOC, Yang et al.,
  ACL 2023, https://arxiv.org/abs/2212.10077: +22.5% coherence, +28.2%
  outline relevance, +20.7% interestingness — reported, not independently
  verified). → Beat-level packet + adherence check during drafting.
- Independent revision with blind peer review beats discussion loops;
  naive collaboration homogenizes output (LLM Review, 2026,
  https://arxiv.org/abs/2601.08003). → Critic notes stay independent;
  no homogenizing loops.
- Count wrong→correct vs correct→wrong transitions per pass; retire
  net-zero passes (Huang framing). → Per-pass transition accounting.
- Harden judging: blinded judges with dimensional rubrics (TTCW 14
  binary tests, Chakrabarty et al., 2024,
  https://arxiv.org/abs/2309.14556); do not disclose AI authorship to
  judges (attribution penalty, Marco et al., 2024); never the drafter as
  judge (self-preference, Panickssery et al.).
- Stated plainly: no published study directly tests
  weaker-model-plus-process vs stronger model on long-form fiction, and
  none of the above was validated on novel chapters. Our blind A/B
  infrastructure is the experiment. The system is self-sustainable: no
  phase requires a stronger model's output. A stronger draft, when one
  happens to exist, is optional calibration only.

Component references (do not duplicate their content here; read them when
the phase calls for them):

- Revision ladder (this workflow's Phase 6):
  `~/workspace/custom-skills/local-prose-revision-ladder/SKILL.md`
- Defect log: `~/workspace/auditions/AtlasMuse/defect-log.md`
- Blind A/B protocol: `~/workspace/auditions/AtlasMuse/blind-ab-protocol.md`
- Blind A/B results: `~/workspace/auditions/AtlasMuse/blind-ab-results.md`
- Moves catalog: `~/workspace/auditions/AtlasMuse/moves-catalog.md`
- Deterministic audit: the project's own `scripts/chapter-control-audit.ps1`,
  run via the Linux shim at `~/workspace/tools/chapter-audit/` (pwsh 7,
  installed 2026-09-25; only path-separator lines adapted — all check
  logic byte-identical; see the shim README). The Python port
  `chapter_audit.py` remains as a fast pre-check only.

## Run file layout

Every chapter run lives in `~/workspace/auditions/AtlasMuse/` with this
fixed set (`NN` = chapter number, `<slug>` = short chapter slug):

| File | Phase | Contents |
|---|---|---|
| `NN-<slug>-packet.md` | 2 | chapter packet (contract, beat sheet, ledgers, moves, defect-risk map, word budget) |
| `NN-<slug>-draft.md` | 3 | the chapter prose |
| `NN-critique-log.md` | 4 | dimension → gap → revision → evidence (gaps from independent critique) |
| `NN-diagnostic-read.md` | 5 | fresh read (blindness labeled) + serial continuity |
| `NN-revision-log.md` | 6 | one change-ledger entry per pass: finding ID, exact span, intended reader effect, old/new wording, regression check |
| `NN-audit-record.md` | 7 | deterministic audit release-stage result |
| `NN-feedback-*.md` | 8 | blind-read feedback (TTCW rubric where used) |
| `NN-release-checklist.md` | 9 | release checklist + retrospective + pass-delta rollup |
| `NN-run-manifest.md` | all | phase dates, gate results, freeze hash/commit, watched adjudications, evidence pointers |

Shared across runs (never duplicated per chapter): the defect log, the
blind A/B protocol and its results table, the moves catalog.

**Status line.** Every run file carries the chapter's status:
`**Status:** PROPOSED EXPERIMENT — not manuscript canon.` until the author
accepts it. No canonical manuscript or continuity file is touched by any phase.

## Phase 0 — Intake

Before anything else, confirm the inputs exist:

1. The chapter's movement/outline (plot authority for this chapter).
2. The immediately preceding chapter (serial state).
3. The writer/voice profile and the project's writing guide.
4. Affected bible records (characters, locations, magic rules, calendar).
5. The originality receipt for this chapter's packet (`continuity/originality-register.md`): decision must be PASS — REVISE or UNCERTAIN blocks the packet, and the draft later gets its own written comparison against the searched examples (house rule, ch.7+).
6. Exposure manifest: for shared-packet experiments, record commit, source
   hash, and the actual material seen of the other side's planning,
   notes, or prose — and when. No draft begins until exposure is logged
   in the run manifest (Sol's freeze protocol). Mark any accidental view
   of the other draft immediately. A mismatch between the manifest and
   what was actually seen downgrades a model comparison to an editorial
   comparison; a similarity detector cannot establish independence
   (Sol review 2026-09-25).

**Gate:** all six present. Missing one → stop and say which, do not
improvise it.

## Phase 1 — Pre-flight

1. Read the writer/voice profile and the preceding chapter (not from memory).
2. Read the defect log; select the three most relevant open/guarded defects
   for this chapter (house rule). For each, name its preventive control
   **and the exact point in the draft (scene/beat) where the control will
   be verified**, and put all three controls into the packet. A risk named
   without a verifiable control is not mitigated (zero-recurrence contract,
   user-stated 2026-09-25).
3. Name the chapter's set piece and its arc in one sentence each.
4. Record Phase 1 in the run manifest, including the exposure log: for
   shared-packet work, what of the other side's planning/notes/prose was
   visible and when (hashes where available). No draft begins until the
   exposure log is written.
5. Dependency retrieval list: name every older passage the chapter depends
   on, each with its exact source and line range where known (Sol's ch.9
   movement pattern, 2026-09-25: `ai-manuscripts/07-the-straps-ai-completion.md:61-81,85-129`
   style citations). "The plan" is never prose evidence — retrieve the
   passages, don't cite the outline.

**Gate:** set piece and arc sentences written down. No prose yet.

## Phase 2 — Planning (chapter packet)

Write `NN-<slug>-packet.md` before a single line of prose. Packet skeleton:

```
# Chapter NN "<Title>" — Atlas packet
Status / Run / Authority / Source-fairness note
## Chapter contract (the hard commit)
- Immediate want / Obstacle / Material change / Relationship change /
  End change / Irreplaceable function / Causal summary (because X, Y happens)
## Scene spine — per scene: goal → conflict → turn; reaction → dilemma → decision
## Beat sheet (concrete craft beats, not plot summary) — per scene:
- Sensory-evidence beats: what the viewpoint body perceives, in order
- Instruments planted: object or instruction that will be used later, and how
- Question designs: for any interrogation/teaching scene, state the trap
  (why there is no safe answer), not just the topic
- Belief- or consequence-spread staging where the spine requires it
## Ledgers
### Calendar ### Physical/resource (split: required state vs. optional narrated
setup — interface actions need narration only when the scene's consequence
depends on them; 2026-10-11) ### Knowledge/viewpoint (entry + exit state;
every authority/evidence row carries one sentence: "what the returning reader
must understand here," in ordinary language, not the institutional label;
2026-10-11)
### Records custody (what each character writes down; whose private news lands
in whose book, and the on-page grant for it) ### Question/payoff
### Visual recognition ### Older dependencies
## Moves selection — 2–3 catalog moves, placed at specific beats
## Set-piece checks (planning gates — all three answered before drafting)
- Canon proximity: the closest canonical/franchise scene to this chapter's
  set piece; why the overlap is load-bearing or how the set piece differs.
  A set piece that replays an iconic scene needs a reason stronger than
  convenience. (Learned 2026-09-23: Sol's team retired the needle lesson
  for exactly this — "do not replay Harry's lesson.")
- Verdict legibility: the on-page instrument or test that makes the central
  trial's outcome legible without a character announcing it. A verdict that
  only exists in dialogue is a verdict the draft hasn't earned.
- Serial rhyme: the earlier chapter this trial inverts, echoes, or rhymes
  with — named explicitly, not assumed. (Sol's strap inverts ch.1's trammel:
  looked too poor and held / looks sound and fails.)
## Defect-risk map — the three selected risks, each with one preventive
   control and its draft verification point (house rule; zero-recurrence
   contract)
## Word budget per scene
## Extended fields — next-chapter hand-off; threads touched / deliberately
   untouched; reader-question ledger with payoff horizons; canon claims marked
   verified / inferred / proposed / unresolved; exit-state capsule fields;
   private scene-intent note per scene (withheld from blind readers);
   originality receipt ID + decision (PASS required); pressure beyond the
   packet (the most useful dramatic gap the packet doesn't state, one
   sentence); voice anchors — one or two **with authority status stated**:
   accepted author prose where it exists; where none exists, provisional
   attention anchors are hypotheses about attention and cadence only, never
   phrases to imitate (Sol's source-boundary formulation, 2026-09-25); lines advanced — two or
   more of external problem, capability, relationship, institution, home,
   mystery, self-understanding; forbidden imports — revelations, themes, or
   later knowledge the chapter must not import
## Reader promise and enjoyment target — what should be pleasurable,
   intriguing, moving, or wondrous in the lived reading experience, plus
   the intended continuation pull. Name at least one intended source of
   wonder, warmth, amusement, suspense, curiosity, or emotional attachment,
   and one concrete reason the reader should want the next scene. Name one
   honest deferred verdict: an observation whose outcome the chapter
   genuinely leaves open for a later scene (no manufactured cliffhanger —
   the plant's tomorrow, not a withheld shock). Targets for the prose, not
   permission for decorative incidents. (House workflow 2026-09-25, Sol
   commit 41b367654; deferred verdict grafted from the ch.9 blind read,
   2026-09-25.)
## Staged-test ledger — for any repeated practical test, one row per trial:
   operation, input, held constant, changed, visible result, sample
   provenance, fixture, load path, licensed conclusion. Check the prose's
   attempt count and causal inference against this ledger after any
   expansion (house control board; D28). A test that changes two variables
   licenses no single-variable conclusion.
## Preventive controls — movement-specific checks this chapter must satisfy
```

A beat the packet cannot name concretely is a beat the draft will
summarize — flag it as such in the packet rather than discovering it in
prose. Do not pre-write polished dialogue in the packet; a packet that
pre-writes prose is a draft wearing a packet's name.

**Gate:** packet file exists with every section filled, beat sheet
concrete. "No packet, no draft."

## Phase 3 — Drafting

1. Draft one scene at a time, reinjecting only the current scene spine,
   current story state, and necessary records. Full bible in context every
   scene is how contradictions breed.
2. Reach the scene's change before polishing: the turn must be on the page
   before any sentence gets a second pass.
3. Record any useful departure from the plan before continuing — a
   discovered better beat is kept, a silent one is drift.
4. **Beat-adherence check:** after the full draft, walk the beat sheet:
   each planned beat → `landed` / `drifted` / `missing` **with a draft line
   citation for every landed beat. A beat with no citation is missing by
   construction, not by judgment** — the drafter's memory of intending it
   does not count. (07b, 2026-09-23: the shared plan's Rupert-debt beat had
   no on-page passage and the loose check passed the draft anyway.)
   A drifted or missing beat is either revised into the draft now or
   recorded with a reason in the run manifest. Do not proceed with silent
   drift.
5. Run the draft-stage deterministic audit (the project's ps1 via the
   Linux shim): an **error** blocks further work until corrected; a
   **warning** requires inspection and a recorded judgement.
6. **Reader-delivery check (2026-10-11, Sol ch.12 prevention, author-authorized).**
   Re-read WITHOUT the packet's explanations in mind: every speaker
   identifiable at every authority change; institutional shorthand replaced
   with checked facts and actual permissions; repeated scene openings
   compared within the chapter; repaired paragraphs and the ending re-read
   for recoverable literal meaning. Completed ledgers and zero pattern
   hits are never clarity evidence.

**Gate:** full draft written, `NN-<slug>-draft.md` saved, adherence check
written, draft-stage audit errors zero. Freezing happens after Phase 7 —
see Freeze; do not treat a complete draft as frozen.

## Phase 4 — Independent critique (the external gradient)

**Routed through the Reviews board (2026-10-10, the author's isolated-reviewer decision).** Atlas is never the critic — independence is structural (separate agent, separate context), never asserted. Critique runs as isolated review jobs on the PC:

1. Atlas creates one job folder per persona under `C:/Users/<user>/Documents/Reviews/jobs/<job-id>/` (contract: `jobs/README.md`): `TASK.md` (names the persona file), `draft.md` (byte-identical to the frozen candidate; SHA recorded), `registry-excerpt.md` (Atlas-curated, minimal — only what the draft touches; follow the curation rules in `Reviews/README.md`: disambiguate same-date deadlines, distinguish knowledge-of-path/existence/contents/terms).
2. Atlas points the reviewer seat at the job folder: **fresh Sol** runs `personas/senior-reviewer.md` (the full craft + mechanics critic — the senior second opinion); **Luna fleet and/or DSH** run the pointed personas (`beat-adherence.md`, `continuity-registry.md`, `prose-defects.md`, `forbidden-shortcuts.md`). One persona per folder; reviewers never see each other's folders or findings.
3. The reviewer reads its persona file (isolation protocol baked in: the job folder is its entire world; diagnosis only, no rewritten prose) and writes `findings.md` back in the same folder.
4. Atlas collects `findings.md` and dispositions every finding (accept → numbered revision list; reject → recorded reason; deliberate-zone → diagnostic-only), then merges into the critique log.

No stronger model required. The gradient comes from independence and role separation, not from a better text.

> **SUPERSEDED 2026-10-10 (pipeline v1.0.1/B14):** the procedure below
> is retired. Critique runs through the Reviews board (steps 1–4 above) —
> isolated job folders, separate reviewer seats. Retained for the audit
> trail; do not follow.

1. ~~Spawn TWO restricted critics with complementary briefs — Critic C
   (craft) and Critic M (mechanics).~~ Each receives ONLY: the packet, the
   draft, the defect log's open entries (as plain defect descriptions,
   without Atlas-identifying framing), **the project's standings files
   (`~/workspace/standings/rulings-global.md` + `rulings-<project>.md`)
   as required context — a standing ruling is a defect class, not
   background (2026-10-09: the ch.4 critic missed R-G1 "fitted"→"fit"
   because it never saw the rulings)**, and its rubric below. Neither
   receives: revision history, ladder logs, the run manifest, or any
   knowledge of who wrote the draft. Present the draft as written by an
   external submitter — never "your draft," "our draft," or Atlas's
   (Tsui 2025: models correct identical errors framed as external at far
   higher rates; the measured self-correction blind spot is 64.5%).
   Diagnosis only; neither critic writes revised prose. The two critics
   never see each other's notes (LLM Review 2026: unconstrained
   interaction homogenizes output; independent critique + private
   revision is the active ingredient). **Never instruct a critic to
   "contradict" the draft** — that rewards invented opposition (Sol,
   2026-09-28). Ask each critic to try to **falsify a bounded claim**
   and to report an empty result when the claim holds: "up to five
   substantiated findings; for each: evidence, reader effect,
   uncertainty. Stop when none remain." Quotas manufacture findings;
   the honest empty result is signal.
2. Critic C scores each craft dimension as `works` or `gap: <one
   sentence>` with quoted evidence: sensory/body evidence; dialogue
   voice separation; set-piece staging (operation vs summary); question
   design (trap vs direct); consequence and stakes; thematic
   demonstration (shown vs argued); protagonist agency at the turn
   (active choice vs passive/concealing — does the decisive beat come
   from the protagonist's choice, and does that choice match the arc?).
   Critic M checks each mechanical claim with quoted evidence:
   physical-transfer trace (quote the exact sentence moving the set
   piece's key object at each handoff — no quoted sentence = missing);
   calendar/time consistency; permission and records custody (every
   character restatement checked against the authority's literal
   wording); exact-source fidelity (no invented dialogue, no
   memory-summaries); staged-test ledger (attempt counts and licensed
   conclusions match the prose).
3. Merge both critics' notes into `NN-critique-log.md` as RANKED
   findings, each = {finding ID, severity (critical/major/minor),
   evidence quote, concrete revision instruction}. **Tag each finding at
   merge:** (a) its claim type — asserted-vs-demonstrated /
   operational-semantics / character-knowledge / momentum / style
   (2026-09-28: two lenses filing the same claim type on one anchor get
   routed to the jurisdiction owner instead of double-counted); (b) a
   **doctrine pre-tag** — findings in zones the project marks deliberate
   (e.g. a chosen slow-burn aftermath) are labeled diagnostic-only before
   adjudication, not argued into defects later. Rank by severity,
   then by load-bearing order; the single most critical issue goes
   first. Unranked laundry lists are the measured failure mode of story
   feedback (Stahl et al., Findings of EMNLP 2026) — actionability is
   what makes feedback constructive. The revision column is filled in
   Phase 6 — the critics do not revise.
4. Where the critics disagree on a load-bearing beat (set piece, ending,
   exposure scene), or either marks itself uncertain, run a micro
   self-contrastive A/B: draft two variants of the beat and have a third
   restricted critic — or the user, if the critics disagree — judge
   blind between them on the named dimension only. Bound: at most 3
   micro-A/Bs per chapter.
5. If a stronger-model draft of the same packet happens to exist, it may
   be used as additional contrast — optional calibration, never required.
   Record whether it was used.~~

Honest limitation (superseded 2026-10-10 by the Reviews board): in-process critics used to inherit the transcript, so independence was asserted, not proven. Critique now runs in isolated PC job folders with separate reviewer seats (fresh Sol / Luna / DSH) — correlated blind spots are structurally reduced, not merely briefed away. The user remains the final independent judge; the blind A/B (Phase 8) is where that judgment lands.

**Gate:** ranked critique findings logged with IDs, severity, evidence
quotes, and concrete revision instructions. Tier O passes may target
ONLY gaps named by an external gradient: the critique log, the
diagnostic read, reader acceptance answers, the user's targeted
judgment, or — only when one happens to exist — a stronger-draft
comparison. No other gap, no pass. The writer may log a self-noticed
defect as a **hypothesis** — it authorizes a Tier O pass only after a
quoted contradiction, a tool result, or a reader response confirms it;
writer confidence never closes a defect on its own (Sol review
2026-09-25: do not prohibit useful self-diagnosis, but do not let it
close anything).

## Phase 5 — Diagnostic read (before the ladder)

Purpose is now explicit: produce targets for the ladder's opinion passes —
not to certify quality.

- Section A: read the full draft end to end in one sitting. Record what
  works, what was fixed during the read, remaining honest defects. Label
  `UNBLINDED` unless the reader genuinely hasn't seen the draft or packet.
  Standing question: at the chapter's decisive beat, does the protagonist
  take the most active choice available, or a concealing/passive one — and
  does the choice match the arc? (07b, 2026-09-23: Thomas palmed the
  half-matches; Sol's Thomas volunteered his strap for the load test.)
  Then the summary view: compare the chapter's want, turns, and end state
  against the first-year outline — a summary must state its causal turn
  without listing itinerary stations (house rule; local and summary views
  never replace each other).
- Section B: a SEPARATE serial-continuity pass with restricted context —
  draft + preceding chapter + movement + retrieved exact dependency
  passages only (no packet, no revision history, no scene-intent notes).
  Run it as a subagent with that restricted brief; if run by the drafter,
  label it `UNBLINDED-SELF`. **Register-freshness pin (hard pre-check,
  2026-09-28):** before the continuity pass runs, read the continuity
  register's declared "reconciled through" point and compare it against
  the chapter under review. A register that does not yet reconcile the
  chapter's accepted predecessors is stale — route any register-only
  finding to a register queue, never to the chapter verdict. Fifteen
  readers times one stale register is one unanimous false defect
  (fleet test 2026-09-28, INDEX.md C7). Every cross-chapter claim cites
  the supplied passage that supports it and distinguishes direct evidence
  from inference; a rolling summary is never proof (house bounded-review
  rule).
- Section C: **confusion-first cold read (2026-10-11, Sol ch.12 prevention,
  author-authorized).** A reader who has not seen the packet reads the draft
  cold. Record their UNPROMPTED confusion first, before any directed
  questions. Then ask them to paraphrase, in ordinary language: the
  consequential permissions (who may do what), the evidence limits (what
  the records establish and cannot establish), and the ending (what changed
  for the protagonist). The reader must NOT have specialist domain knowledge
  for this pass — if they do, note it as a limitation. Do NOT prime them
  with known findings or the packet's answers. Record the exact candidate
  SHA and the context supplied.

**Gate:** sections A and B written to `NN-diagnostic-read.md`; remaining
defects named, not resolved here. The file must exist under its fixed
name — a diagnostic read kept only in chat or folded into another file
is a skipped phase (ch.9 2026-09-25: no separate diagnostic-read file
was produced).

**Board boundary (2026-10-10, isolated-reviewer decision):** the Phase 5
diagnostic subagent (Section B) is NOT the Reviews board critic — it is
a same-workflow continuity read. Only findings recorded in the formal
`NN-diagnostic-read.md` document — not the subagent's informal
observations — may authorize Tier O passes, per the ladder's gradient
rules (critique log, diagnostic read, reader acceptance, user judgment).

## Phase 6 — Revision ladder

Run the ladder skill's sixteen passes in fixed order, in two tiers (full
rules in the ladder skill). Defect classes throughout are the canonical
taxonomy — `~/workspace/custom-skills/local-serial-workflow/defect-taxonomy.md` — one
taxonomy, referenced, never copied.

- **Tier M (mechanical, tool-grounded):** forbidden-shortcut grep,
  geometry/resource trace, calendar/time ledger verification, canon/history
  record checks, **flashback-medium check** (any flashback to a canon scene
  restates that scene's medium — video vs in-person — before the prose
  writes movement verbs; ch.5 2026-09-28: "walked out" staged a physical
  office for a 1:1 that ch.2 canon staged as a video call, and it slipped
  through every review round), **negative-claim inventory** (extract every
  nobody/never/no-way/"didn't say" sentence; check whether an on-page
  search or audit artifact accompanies it — fleet test 2026-09-28 C1/C2/C6),
  **standings-sweep** — the ladder skill's pass 5M-standings (defined
  once, there; this phase references it, never redefines it).
  Run every chapter; same-model execution is fine because
  the check is the tool, not the opinion.
- **Tier O (opinion, gradient-gated):** premise/causality, body-evidence
  quality, viewpoint/voice (Tier O half only), dialogue separation, visual
  recognition, story function, question/payoff, relationship consequence,
  readability, enjoyment/attachment, anti-padding/value, local language,
  reader-burden. An opinion pass may ONLY target gaps named by an external
  gradient — the critique log (Phase 4), the diagnostic read (Phase 5),
  reader acceptance answers (Phase 8), the user's targeted judgment, or —
  only when one happens to exist — a stronger-draft comparison. A pass
  that diagnoses its own gaps and fixes them is the D9 failure mode — log
  it as such and revert the pass.
- Log each pass as a change ledger: finding ID, exact span, intended
  reader effect, old/new wording or scene action, and a regression check
  for affected facts (spot-check every changed line). Record a zero-change
  pass only when it guards a current top-three defect-log risk; otherwise
  a clean pass is one line (Sol review 2026-09-25). **Pass ledger
  (2026-09-28):** confirmations ("worked" lines) from every review round
  are preserved in a per-chapter pass ledger; after any revision, re-run
  the ledger as regression checks proportionate to the change. A changed
  candidate gets a proportionate regression check — verified-clean items
  are tripwires, not trivia.
- Do not re-run a pass that produced no change — a no-change pass is
  evidence the class is clean, not an invitation to run it again. A
  second run of any pass requires new external evidence (Self-Refine:
  gains plateau by iteration 3; Huang/Xu: extra self-revision rounds
  degrade accuracy or inflate perceived quality without real gains).
- Later passes do not redo earlier passes' jobs.
- **After a substantial prose expansion** (new attempts, new apparatus, or
  >10% word growth), re-run the affected Tier M passes (physical,
  calendar, canon) and story-function, check the prose's attempt count and
  causal inference against the staged-test ledger, and obtain fresh reader
  attention before release. "Insertions only" does not establish that the
  chapter's causal or continuity state survived (house rule; ch.8's inert
  bridge is what this prevents).

**Gate:** sixteen log entries as change ledgers; residual-defects
list written honestly.

## Phase 7 — Deterministic audit gate (release stage)

Run the project's `chapter-control-audit.ps1` at release stage via the
Linux shim (`~/workspace/tools/chapter-audit/`). Record the full result in
`NN-audit-record.md`. An error blocks release; a warning cleared without
a recorded reason is a lie in the ledger. The shim's only changes vs the
project scripts are path-separator lines (documented in its README); the
Python port is a pre-check only and is never presented as the audit.

**Gate:** exit 0, result recorded.

## Freeze — the point of no return (after Phase 7, before Phase 8)

Freezing is a distinct, recorded act — not a side effect of finishing the
draft. A draft is not frozen, committed, or submitted for comparison until
every item below passes.

1. **Residual list clean:** the ladder's residual-defects list names no
   open flagged defect — flagged = blocking (D29, ch.8 2026-09-25: two
   exact-source errors I had flagged myself shipped into a blind
   comparison and were then confirmed at high confidence).
2. **Load-bearing factual defects resolved; watched items labeled.**
   Every factual worry in the residual list — quotable contradiction,
   ledger mismatch, tool failure — is resolved before freezing; facts
   close on evidence, not confidence (ch.9 2026-09-25: three shipped
   "watched" items were confirmed by the blind reader because the watched
   list was never routed to a reader). Aesthetic worries (taste, pacing
   feel, warmth) are recorded with the writer's assumption and confidence
   and labeled **unresolved**; they travel with the draft into comparison
   as disclosed limitations and do not block freezing while no reader is
   available (Sol review 2026-09-25). When a reader is available, the
   watched list goes to the **acceptance reader** (single-draft read) as
   hypotheses — one targeted question per worry, quoted with its line —
   never to the A/B comparison judge; see the acceptance brief template
   in `blind-ab-protocol.md`. Adjudication uses the best available reader,
   labeled: restricted-context subagent < fresh same-family reader <
   independent reader (human or different family). A same-family-only
   adjudication is provisional — the item is re-adjudicated when an
   independent reader is available, and the freeze record says so.
3. **Pre-freeze self-check** (Sol's "local checks" pattern, ch.8
   2026-09-25): on-page premise stated; attempt/object counts exact;
   object movement staged; custody closed at every boundary — including
   records custody: no character's private news appears in another
   character's book or record without an on-page grant (ch.9 2026-09-25:
   Thomas's closing record wrote Lydia's invitation into his own book);
   calendar verified; any recalled wording or conversation checked against
   its exact earlier passage (D30, D31 — no invented dialogue, no
   memory-summaries) — including a character's restatement of an
   instruction given earlier in the same chapter, checked against the
   instruction's literal wording (D35, ch.9: "she said to ask" vs the
   actual ask-before-cutting/watering-twice rule); retained items
   accounted for; close-third inference clean; next-chapter handoff
   intact. Sol caught an invented Rupert conversation and a
   mis-summarized Laynes exchange in its own self-passes before freezing
   — run the same passes before any freeze.
4. **Audit recorded:** deterministic audit release-stage exit 0, full
   result in `NN-audit-record.md`.
5. **Provenance recorded:** SHA-256 of the frozen draft file computed and
   written to the run manifest; draft committed; commit hash recorded.
   The frozen file is retained unchanged as the comparison record —
   post-comparison revisions become new frozen candidates, never edits
   to the judged file.

**Gate:** all five recorded in the run manifest. A draft that cannot pass
item 2 for lack of any reader stays "draft complete, awaiting reader" —
it is not frozen, and stop condition 10 keeps it out of comparisons.

## Phase 8 — Blind A/B (hardened)

Follow `blind-ab-protocol.md` plus these hardening rules:

- Judges are blinded to draft origin; **do not disclose AI authorship to
  judges** (attribution penalty, Marco et al., 2024).
- Score the **TTCW 14 binary tests** (Fluency / Flexibility / Originality /
  Elaboration, Chakrabarty et al., 2024) as dimensional diagnostics
  alongside the preference verdict — pairwise votes hide where the gap
  lives. Administration: use the 14-test **aggregate**, never single tests
  (per-test Fleiss κ=0.41, aggregate r=0.69); keep each test's written
  rationale; the writer-model never administers TTCW on its own draft
  (LLM–expert correlation ≈ 0). With fewer than 3 raters, treat TTCW as
  diagnostics, not a score.
- Never the drafter as judge; never a single same-family model as the sole
  judge (self-preference, Panickssery et al.).
- **Anonymization checklist** (as run 2026-09-25): strip model names, file
  paths, timestamps, and status lines; supply only a short neutral premise
  (≤4 sentences); withhold plans, manifests, run artifacts, and repository
  paths; label drafts "Version A"/"Version B" with randomized assignment;
  the reader submits the comparison before the key is revealed.
- **Symmetric provenance:** both drafts frozen with recorded hashes/commits
  before judging — no draft judged from an uncommitted or unfrozen state.
- **Audit symmetry:** every compared draft must have a recorded
  deterministic-audit run. "Audit not run" blocks comparison; it is not a
  footnote (ch.8 2026-09-25: Sol's draft carried a draft-mode audit with
  zero errors; mine carried none, and I froze anyway).
- **Key-sealing order:** record all reader verdicts before unsealing the
  key. The user deferred their own anonymous reads indefinitely on
  2026-09-25 — comparisons proceed on independent readers only; no
  named-comparison report waits on a user read. If the user later provides
  one, record it against the sealed key.
- **Verify findings before cataloging:** check each blind finding against
  exact passages and the calendar. Agreement is not automatic acceptance;
  disagreement requires a reason (house rule). Only verified findings
  become defect-log entries or grafts.
- **Reader count:** one or two readings are individual editorial evidence,
  not a statistical model verdict — label them so, record disagreement
  and exact reasons, and never present either as a model ranking (Sol
  review 2026-09-25: even an 80/20 underlying preference needs ~29
  decisive judgments at stated power; the ch.8 run was one reader — one
  data point).
- **Normalize:** both candidates get the same brief, the same word range
  and stopping point, and the same revision opportunity. Report each
  reader's preference **and expected rewrite burden** without a
  statistical claim.
- **Serial reviewer (separate):** exact-passage evidence for continuity
  claims comes from a dedicated serial read, not from the preference
  judge — the judge judges, the serial reader cites.
- **Reader-experience acceptance questions** (graft: house workflow
  2026-09-25, Sol commit 41b367654): every blind/local reader answers
  these separately, with evidence rather than a score —
  1. Could I follow the chapter's immediate goal, physical action, time movement, and emotional turn on a first read?
  2. Where, if anywhere, did I feel confusion, drag, or prose that seemed to be filling space?
  3. Did the chapter give me at least one experienced moment of wonder, warmth, amusement, curiosity, tension, or attachment, as appropriate to its promise?
  4. Did I want to continue into the next chapter or scene? If not, where did that desire fail?
  5. Could I describe what changed in the characters or their situation without consulting the outline?
  The chapter does not pass its reader-experience gate merely because the
  reader can summarise it or because the deterministic audit is clean. A
  "would continue" answer is evidence, not a substitute for reasons; a
  negative or qualified answer requires a targeted revision or an explicit
  author-facing deferral. Do not average these answers into a composite
  quality number.
- **Watched-list adjudication** (ch.9 2026-09-25): when a reader is
  available, the writer's residual watched list goes to the **acceptance
  reader** (the single-draft reader answering the acceptance questions
  above) as hypotheses — one targeted question per self-diagnosed worry,
  quoted with its line — using the acceptance brief template in
  `blind-ab-protocol.md`. It NEVER goes to the A/B comparison judge:
  handing one side's worry list to a comparative judge breaks symmetry
  and blinding. Each item comes back adjudicated: confirmed (→ targeted
  fix) or rejected with reason (→ retired with the reader's words as
  evidence). Factual worries must be resolved before freezing; aesthetic
  worries with no reader available are labeled unresolved with assumption
  + confidence per the Freeze section, not silently dropped. Reader
  independence is labeled per the Freeze section's reader ladder.
- Record each judge's model family. A sole same-family judge downgrades the
  run to provisional evidence.
- Findings carry dispositions; drafts stay frozen — no finding triggers an
  automatic rewrite.
- **Post-comparison revision rules** (ch.9 2026-09-25): comparison findings
  carry IDs and dispositions; the revision targets the report's named items
  only — never splice the other draft's prose into the revision (build from
  the findings, not from the competitor's sentences); a fresh restricted
  reader verifies the revision against the finding list before it replaces
  the frozen candidate. That repair read checks named repairs only — it
  does **not** establish a new preference; the frozen A/B result stands
  until a new blind comparison runs (Sol review 2026-09-25). The frozen
  pre-comparison draft is retained as the comparison record; a later
  revision gets a new identity.
- Record the verdict **before** unsealing; feed every lost dimension into
  the defect log as defect → fix → evidence → detection stage.

**Gate:** verdict + TTCW scores recorded in the protocol's results table,
or an explicit note that no blind judge was available (which the release
checklist must carry honestly — never claim a blind read that did not
happen).

## Phase 9 — Release

Write `NN-release-checklist.md` from this template:

```
## Release-readiness checklist
- [ ] Chapter contract honoured (want/obstacle/material/end/relationship/irreplaceable function)
- [ ] Timestamps complete; scene count matches breaks + 1
- [ ] Knowledge audit: every name/rule/comparison traceable to an on-page source
- [ ] Physical routing closed at every boundary; end states accounted for
- [ ] Beat adherence verified (landed/drifted/missing accounted for)
- [ ] Critique log complete; every Tier O revision traces to a named gap
- [ ] Forbidden shortcuts absent (grep + manual read)
- [ ] Dialogue fingerprints distinct; shared polish controlled
- [ ] Aftermath restraint; ending on evidence, not maxim
- [ ] Proposal boundary line present; no canonical files touched
- [ ] Deterministic audit release-stage: exit 0 (recorded)
- [ ] Blind-read status stated honestly (done / not available); TTCW scores where run
- [ ] Reader-experience acceptance answers recorded (Phase 8); any negative/qualified answer has a targeted revision or an explicit author-facing deferral — no composite quality number
- [ ] Author acceptance — REQUIRED; nothing is canon until the user accepts it
- [ ] Publication/Studio visibility — Atlas's automatic job once the author accepts; verify live and report the receipt

## Retrospective
- What the critique phase (or blind A/B) taught: which dimensions moved, which didn't
- What the first draft got wrong (with detection stages)
- What the final improved
- What the user wanted preserved
- Watched-item adjudication: each pre-freeze worry → reader verdict
  (confirmed/fixed, or rejected/retired with the reader's reason quoted).
  A worry retired by reader evidence is logged so it does not resurface
  as a fresh worry next chapter.
- Grafts: when a comparison draft exists (blind A/B loser, stronger-draft
  calibration, or a parallel draft like Sol's), list what it did better as
  portable items — specific beats or techniques that could transfer to the
  winner without its premise. A comparison that names no grafts was skimmed.
- First-draft risk count: how many instances of the three selected risks
  the first draft showed, vs the previous chapter (house measure — the
  goal is fewer, not a longer report)
- Per-pass change ledger for this chapter (finding ID, span, intended
  reader effect, old/new wording, regression check per pass)
- Pass retirement review (at movement boundaries): any pass that produced
  no accepted findings across the movement is a retirement candidate
  (it reopens if a judged chapter proves it needed)
- Author rewrite burden (n/a until accepted)
```

Then: update the defect log (new defects in, detection stages recorded,
statuses current), **append discarded findings + reasons to the
per-project kill-list** (2026-09-28: a retained list of manufactured or
falsified findings — e.g. the midnight-dateline arithmetic allegation,
slow-burn-as-defect, simile-count-as-defect — so the next fleet or the
next chapter does not re-spend adjudication budget re-litigating them),
record every material finding to the project's shared
`continuity/feedback-catalog.md` (attributed to Atlas, with dispositions —
that is the record both sides read; a private run may only *propose*
catalog entries — the project owner reconciles them against the canonical
file, Sol review 2026-09-25), refresh the defect-risk map for the
next chapter, and close the run manifest with dates and gate evidence.

**Gate:** checklist complete except the author-side items, which are marked
as author-side — never faked.

## Handover bundle

Hand the user: the packet, the draft, the critique log, the diagnostic
read, the revision log, the audit record, the freeze record (hash, commit,
watched adjudications with reader independence labeled), the release
checklist + retrospective. State plainly what is still outstanding (blind
read, author acceptance, publication). Do not manufacture a composite
quality score. A handover that omits the critique log or the transition
counts is incomplete.

## Roles

- **Atlas:** runs Phases 0–7 and 9; prepares everything a blind judge needs.
- **Author (the user):** sets feedback dispositions, accepts or rejects prose,
  performs Studio/publication verification, gives targeted judgment at the
  Phase 4 fallback and Phase 6 gradient gates. The user deferred their own
  reads indefinitely on 2026-09-25 — they are **not** the fallback judge.
  Blind judgment comes from independent readers (≥2 per the protocol).
- **Blind reader:** anyone who has not seen the draft, the packet, or the key.
  My own reads are unblinded by construction — label them so.
- **Critics:** isolated reviewer seats on the Reviews board (2026-10-10):
  fresh Sol runs the senior-reviewer persona; Luna/DSH run the pointed
  personas. Each works in its own job folder (TASK.md, draft.md,
  registry-excerpt.md, rulings.md, optional beat-sheet.md) — the folder
  is the reviewer's entire world. Findings come back as findings.md;
  Atlas collects and dispositions. Diagnosis only; reviewers never
  revise, never see each other's folders. Independence is structural
  (separate agent, separate context), never asserted.

## Stop conditions

1. Do not draft through an unresolved premise involving money, permission,
   route, chronology, or character knowledge — research or decide it first.
2. Do not act on unexplained aesthetic preference, mine or a reader's;
   disagreement requires a reason.
3. Do not add more process when the missing input is a user decision or
   source fact — ask.
4. Do not use an automated score as acceptance evidence.
5. Do not present the Python port's output as the audit. The project's
   `chapter-control-audit.ps1` runs on this VM via the Linux shim at
   `~/workspace/tools/chapter-audit/` (pwsh 7; only path-separator lines
   adapted — check logic byte-identical).
6. Do not claim a draft is finished while the reader-burden check still
   lists defects.
7. **Do not run an opinion pass without a named external gap**
   (critique log, user judgment, or — only when one exists — a
   stronger-draft comparison).
8. **Do not revise toward a self-diagnosed gap** — name it in the residual
   list AND route it to the next external reader as a targeted question
   (Phase 8 watched-list adjudication). Factual watched items must be
   resolved before freezing; aesthetic ones are labeled unresolved with
   assumption + confidence (Freeze §2). Stop condition 9 applies to
   unadjudicated factual items, not just flagged ones (ch.9 2026-09-25).
9. **Do not freeze a draft while flagged defects remain open** (D29).
10. **Do not run a named comparison until both drafts are frozen with
    recorded hashes, both audits are recorded, and the key-sealing order
    is in place** (user's anonymous read before unsealing). "Frozen" means
    the Freeze gate passed — including watched-item adjudication — not
    merely that a draft file exists.

## Retirement

A `guarded` defect-log entry with no recurrence in the last 3 judged drafts
becomes `retired`; a retired entry that recurs reopens as `open`. At each
movement boundary, review the ladder: a pass that produced no accepted
findings across the movement is a retirement candidate; decorative passes
retire (it reopens if a judged chapter proves it needed). Rules that never
fire are decoration. (More passes ≠ better: LLM Review 2026 rounds peak at
R=3 then decline; Self-Refine plateaus by iteration 3; Sol review
2026-09-25: the research does not validate sixteen fixed passes — keep
mandatory source/mechanics gates, run only opinion passes tied to a
high-priority observed reader effect. Retire aggressively, never add a
"just in case" pass.)

## Changelog

- 2026-09-29 (Operation "Iron the prose"): Phase 6 references the
  canonical defect taxonomy
  (`~/workspace/custom-skills/local-serial-workflow/defect-taxonomy.md`) — one
  taxonomy, referenced, never copied. Sources: the author's ch.6 notes,
  Sol/DSH synthesis.
- 2026-10-11 (Sol ch.12 prevention, author-authorized, all projects):
  Phase 2 packet ledgers gain returning-reader rows (Knowledge/viewpoint)
  and state-vs-setup separation (Physical/resource); Phase 3 drafting
  gains the reader-delivery check (step 6); Phase 5 diagnostic read gains
  Section C confusion-first cold read; ladder Rule 3c inherited from the
  ladder skill. TRIAL: three chapters before permanent adoption.
## Available connectors

Use `muse.connector_search` to find the current connector docs before following
recovered instructions.
