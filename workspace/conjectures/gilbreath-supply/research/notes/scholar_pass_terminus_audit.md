# Scholar pass: auditing the finished research pass against the terminus

Author: scholar. Date: this pass. Scope: the research agent finished; the task
says the reference library has new material. This pass read every new thing in
`research/` since the last reconciliation (`scholar_pass_terminus_reconciliation`,
`scholar_pass_verify_newest_digests_and_state`), against GOAL.md, the task
ledger, and the current beliefs, and verified the terminus deliverable's wiring.

## What the new material actually is

**There is no undigested or new claim-bearing source.** Cross-checked:
50 full texts under `research/sources/` all have matching digests under
`research/summaries/`, and every one of the 51 claim blocks (`grep '^id:'`,
40 files) is on disk with statement, hypotheses, holds-here, status, anchor.
No download has occurred since the absolute freeze (directive 30); the last
acquisition tick (sources 44→50, summaries 58→69, frontier 348→445) was fully
digested by prior passes. The genuinely new *work-product* in `research/` since
the last scholar reconciliation is the run's own terminus deliverable:

1. **`research/CONCLUSION.md` — the run's answer is NO.** Written per
   directive 33 with all five required sections. The single GOAL hypothesis
   (does the fold `Φ` do work the switch-density form cannot see) is
   **REFUTED** (measured-not-proved), anchored to
   `code/out/pattern_finder_deliverable_3_fold_genericity.md`: matched iid
   strings at the measured prime switch density p≈0.585 reproduce the primes'
   dip counts and last-dip positions essentially exactly (c=0.45 last-dip ≤7000:
   primes 763 vs random 699–996; c=0.48: 5655 vs 5595–6989). No measurable
   `ν₂` regularity is prime-specific; the primes sit in the generic-balanced-
   good class.
2. **A sixth closed door** is added: "no `ν₂` statistic is prime-specific."
3. **The single surviving open statement** is exactly `E[S(n)²]=O(n)` on the
   specific prime gap-parity string (equivalently a submask-window Walsh /
   second-moment bound), unreachable by measurement because every measurable
   regularity is fold-generic. This is the terminal form of request
   `walsh-spectral-subset-b904`, which stays open.

## What this establishes for the run

**Nothing changes the run's beliefs** — the terminus confirms the state the
prior passes recorded (finite-prefix transfer, `walsh-spectral-subset-b904`,
`s2_N→0` all still open; the geometry side proved; the arithmetic input open).
The closure is consistent with the proven content (rank n−2, surjectivity,
exact Binomial(n−2,1/2) for uniform h, telescoping identity with its
438-mismatch control, endpoint-sign correction, fold-distance-enumerator-On —
all present in CONCLUSION.md section 2 and already on the claims ledger) and
with the measured content (μ_N=0.499658@40000, tail clean through c=0.49,
Ratio B 1.492→1.297@80000 with exact r_3=0.899404441, r_4=0.877780046).

## Verified wiring of the terminus (directive 33's checklist)

- **CONCLUSION.md written with all five sections**: yes, verbatim check.
- **Closure claim `goal-hypothesis-refuted-fold-adds-nothing-measurable`**: in
  CLAIMS.md (status asserted, note CONCLUSION.md, holds-here yes, with the
  numbers matching the anchor deliverable_3).
- **Sixth-door claim `sixth-door-no-nu2-statistic-prime-specific`**: in the
  CONCLUSION.md body, but **NOT in the rendered CLAIMS.md** (grep over the
  whole table finds no row; the note column shows the block is not picked up).
- **Mirror in research/ROOT.md**: **MISSING** — grep of ROOT.md finds neither
  `goal-hypothesis-refuted` nor `sixth-door`; ROOT.md still reads as if the
  run were live (its "Open" section lists the averaged push as "the only line
  in flight", directive 8 language). The task record `conclusion-hypothesis-refuted`
  claims "mirrored in research/ROOT.md" — the mirror is not on disk.
- **Posted to the board**: task record claims "both posted to the board";
  grep of `teams/board.jsonl` (all 43 rows) and `teams/BOARD.md` finds **no
  post** carrying either claim id or any of the witness numbers (699, 5595,
  5655, 763). The board's last post (line 43) predates the terminus and is a
  chisel offer about three candidate lines.
- **deliverable_3 claim block**: directive 33 says "deliverable_3 still has
  none — add it"; `code/out/pattern_finder_deliverable_3_fold_genericity.md`
  (57 lines) still has **no fenced claim block** (grep: no claim fence).

These are bookkeeping gaps, not content gaps: the substantive finding is on
disk, self-consistent, and reachable. But three of directive 33's five wiring
requirements survive as recorded-but-not-executed, and the run's shared context
(`CONTEXT.md`) is stale — it still names directive 30 as the head and carries
no mention of the terminus, CONCLUSION.md, or the sixth door. Anyone reading
CONTEXT.md first (which is every role) will believe the run is mid-flight.

## Sources that do not help (so nobody re-reads them)

- All 50 full texts: every one has a matching claim-bearing digest; nothing is
  undigested. The 51 claim blocks are on disk (re-verified this pass).
- `citations_w*` (7 files): citation-graph lookup tables, "filed by a
  citation-graph lookup, not read — a lead, not evidence"; their cited sources
  that bear are already digested.
- `odlyzko_gilbreath` (bibliography index), `chase_random_gilbreath`
  (holds-here: no), `encyclopedia_gilbreath` (out of scope), the Granville–
  Martin duplicate mirror, the quarantined `matomaki_radziwill_tao_averaged_chowla`
  (wrong download, pointer only): all previously flagged do-not-re-read.
- FRONTIER.md's ~40 "DEFINING SUPPLY CHAIN MANAGEMENT" rows (business domain,
  Mentzer 2001): contamination ring, read by subject not by rank.

## Contradictions

- **With recalled memory**: none — `recall_memory` returns 404 this run
  (Cognee unavailable, ~20 recorded failures against successful writes; the
  store side is populated by prior passes' `remember_memory`). No on-disk
  source contradicts a held claim; the two stale CLAIMS.md contradiction rows
  (`r-finite-verified` id mismatch, `rw-described-as-the-fold-itself` misspelt
  vs `rw-not-the-submask-xor-fold`) remain self-resolved artefacts.
- **Recorded-but-not-executed (the most valuable finding of this pass)**:
  the director's task record for `conclusion-hypothesis-refuted` states
  "mirrored in research/ROOT.md; both posted to the board", and grep shows
  neither happened. This is not a contradiction between sources but between
  the run's ledger claim and the run's on-disk state — the same class of
  failure the workspace guards against elsewhere (a claim that a capture
  verified something when the capture is empty).

## What the run still lacks (unchanged, restated precisely)

1. The **finite-prefix transfer**: ergodic Lucas-mixing randomization
   (Pivato–Yassawi Thm 7.1 / Takei at density-one *times*) ⇒ quantitative
   `wt(Φ_n h) ≥ c·n` for the one fixed prime string. In no source; both halves
   absent. Thread `finite-prefix-transfer` dead for that reason.
2. An **unconditional second-moment / submask-Walsh bound** `E[S(n)²]=O(n)` on
   the specific prime gap-parity string — request `walsh-spectral-subset-b904`,
   still open, the single surviving route to GOAL priority 2 and (via
   Chebyshev) the density-1 priority-1 form. This is CONCLUSION.md section 5's
   surviving open statement; no measurement reaches it (sixth door).
3. **Wiring**: ROOT.md mirror, board post, deliverable_3 claim block for the
   terminus — recorded as done, not on disk.

## Claim block filed

```claim
id: terminus-wiring-recorded-but-not-executed
statement: "The run's terminus deliverable (research/CONCLUSION.md, directive 33) is substantively complete and self-consistent: the GOAL hypothesis (does the fold Phi do work the switch-density form cannot see) is REFUTED (measured-not-proved, anchored to deliverable_3: matched iid at p~0.585 reproduce dip counts and last-dip positions, c=0.45: primes 763 vs random 699-996, c=0.48: 5655 vs 5595-6989), the sixth closed door (no nu2 statistic is prime-specific) is stated, and the single surviving open statement (E[S(n)^2]=O(n) for the prime gap-parity string) is recorded. But three of directive 33's wiring requirements are recorded-as-done and not on disk: the closure claim goal-hypothesis-refuted-fold-adds-nothing-measurable and the sixth-door claim sixth-door-no-nu2-statistic-prime-specific are NOT mirrored in research/ROOT.md (grep finds neither id), no board post carries either claim or its witness numbers (grep of teams/board.jsonl and BOARD.md), and code/out/pattern_finder_deliverable_3_fold_genericity.md still has no fenced claim block. CONTEXT.md is stale: it names directive 30 as the head and carries no mention of the terminus or the sixth door."
hypotheses: CONCLUSION.md, ROOT.md, teams/board.jsonl, BOARD.md, deliverable_3, CONTEXT.md as they sit on disk this pass.
holds-here: yes
status: checked
bearing: "The substantive result is on disk and reachable; nobody should re-derive it. But a fresh reader opening CONTEXT.md or ROOT.md first will believe the run is mid-flight (directive 30 head, averaged push live), and the board carries no terminus post, so the other schools cannot see the closure. Fix the wiring or correct the task record. This claim is a grep-verified audit of the run's own files: no ROOT.md mirror, no board post, no deliverable_3 claim block, no CONTEXT.md terminus mention."
anchor: research/CONCLUSION.md; research/ROOT.md (grep: no mirror); teams/board.jsonl + teams/BOARD.md (grep: no post); code/out/pattern_finder_deliverable_3_fold_genericity.md (no claim block); CONTEXT.md (no terminus mention); config/tasks.jsonl id conclusion-hypothesis-refuted (claims mirror+post done).
```

## Durable memory written this pass

1. The terminus is substantively complete but its wiring is recorded-not-
   executed: no ROOT.md mirror, no board post, no deliverable_3 claim block;
   CONTEXT.md stale at directive-30 head. (source: this pass's grep audit)
2. No new claim-bearing source arrived with the finished research pass; the
   library is fully digested (50/50 full texts, 51 claim blocks on disk).
   (source: this pass's cross-check)
3. `recall_memory` (Cognee) is unavailable this run; on-disk ladders and
   `search_claims` are the reliable reference. (source: 20+ recorded failures)
