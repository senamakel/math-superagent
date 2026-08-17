# Scholar pass — library verification and durable findings (current)

Cognee (`remember_memory`) was DOWN for this whole pass (11 failed calls; health
report unanswered). Per the reflection directive, the durable store for this
pass is the workspace note + the claim store (`search_claims`), not memory. The
next pass that gets a working `remember_memory` should push the two durable
findings below into memory.

## What this pass verified (all via `search_claims`, the authoritative recall path)

The reference library is **complete and fully digested**. Every primary source
named in the run was probed; each returns a claim block with hypotheses,
holds-here, and bearing. No source in the library lacks a claim block. The
librarian's two deferred task items are both confirmed done in the store:

1. `file-coupling-inf-and-bb-feasibility-claims` — DONE. Claims
   `coupling-true-inf-crossing-4d` (verified-numerically, NON-rigorous) and
   `coupling-interval-bb-infeasible-10s` (checked, measured method boundary)
   are filed. Honest ceilings preserved: neither drifted to `proved`.
   `coupling-true-inf-crossing-0-3824` is a duplicate of the 4d one and both
   coexist — the 4d capture-precision variant is the authoritative one (task
   marked done).
2. `write-step4-verdicts-to-scores-jsonl` — DONE. STEP 4 verdicts written;
   `SEARCH.md` re-derived (0.421992 gone, Yu block 0.3823435642 on top);
   acceptance test recorded as PASS in `step4_verdicts_derived.captured.txt`
   (grep count 0). This was verified as already complete.

## Durable finding 1 — odd-filter uniqueness is FALSE

Odd-filter uniqueness for union-closed NON-Boolean families is refuted
(claim `odd-filter-max-density-extremal-nonboolean`, status asserted; capture
`code/out/odd_filter_minmax.captured.txt`, exhaustive n=2..4 by lib.uc oracle
plus an independent inline route; structural fact verified exact to n=8):

- min over non-Boolean UC families F of max_x density_x = 2^{n-1}/(2^n−1);
- attained by exactly **n+1** families for every n≥2: the odd filter
  2^[n]\{∅} PLUS the n power-set-minus-singleton families 2^[n]\{{x}},
  each of size m=2^n−1 with max density 2^{n-1}/(2^n−1);
- the value 2^{n-1}/(2^n−1) is correct; only the UNIQUENESS-of-the-odd-filter
  claim that the queued `verify-odd-filter-minmax` task asserted is false.

**Action:** the *open* task `verify-odd-filter-minmax` is stale — it instructs
the next worker to "assert min == 2^{n-1}/(2^n−1) and the UNIQUE minimizer is
the odd filter". Re-running it verbatim would re-assert a false uniqueness. If
kept, it must assert the corrected conclusion (n+1 minimizers). The claim store
already carries the truth; the task row is the only stale place.

## Durable finding 2 — the rebuilt coupon scorer landed on the honest frontier

From the STEP 1–4 rebuild captures (claims `coupling-true-inf-crossing-4d`,
`coupling-interval-bb-infeasible-10s`):

- With the inf over P taken internally (the correct sup-INF object), the
  two-atom coupling bound's true inf crosses 1 between t=0.3824 and 0.3825 at
  α=0.035, minimizer a≈0.3300622 (b2=1) — recovering the published Yu/Cambie
  frontier from the right object, NOT climbing past the proved ceiling. This is
  the regression confirmation that the objective inversion fix works.
- Generic rigorous interval B&B cannot certify t=0.38234 in a 10s budget
  (margin 8.89e-6, slope C~21 → cell width ~4.2e-7 in 4D, minimizer on the
  b2=1 boundary). This is a method-boundary measurement, not a failure of the
  theorem and not a UC result.

## No source-vs-memory contradiction

Every check against recalled durable knowledge agreed. In particular:
Spence's "Heavy Column Theorem false" does NOT contradict anything the run
holds (its matrix is not union-closed, and the paper itself says so);
`contradiction-sawin-ahs` is settled (iid vs dependent coupling are different
classes, not contradictory); `published-record-c` (Yu 0.38234, Entropy 2023)
is stable and the ceiling `cambie-question2-exact-0-3823455` is the correct
preprint ceiling the scorer clamps to.

## Sources that do not help (do not re-read)

OEIS A1xxxxx catalogue files, citation-graph files, the eccles-stability probe,
the Brown/semigroup-algebra `brown-semigroups-rings-markov-chains-2000`
(an 135 KB monograph — its Möbius-algebra section is claimed
`brown-idempotent-expansion`; nothing else in it is used), and the mislabeled
vaughan algebroids file. The two paywalled gaps (Samotij SIAM 2026;
Hachimori–Kashiwabara Graphs Combin 40:130, 2024) are recorded as
obtainable/not-obtained and are NOT in the library — do not cite their content.

## What the run still lacks (unchanged)

- A proven global sup over α>0 for Γ̂(1/2) — currently only the α=0 collapsed
  value φ/2 is proved (`yu-gamma-half-is-phi-over-2`), and the novel-ty of φ/2
  against Yu/Cambie remains unchecked (thread `yugamma-half-collapse`).
- A rigorous (non-numeric) certificate above ~0.38234 — claim
  `coupling-interval-bb-infeasible-10s` says what it would require.
- Folding Spence parity |F|=2k+1 and the tight-witness property into the oracle
  profile scan (thread `abundance-profile` next-step).
