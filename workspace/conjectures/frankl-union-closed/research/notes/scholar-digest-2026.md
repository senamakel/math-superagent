# Scholar digest — what this pass established

Date: current pass. Cognee was down for `remember_memory` (7 failed calls), so
this workspace note is the durable record; the claim store (`search_claims`) is
the authoritative source and already holds every finding below.

## Deferred filing tasks — both done and verified in the store

Confirmed via `search_claims`, not by grepping the capped `research/CLAIMS.md`:

- `file-coupling-inf-and-bb-feasibility-claims` — DONE. Claims
  `coupling-true-inf-crossing-4d` (asserted / verified-numerically) and
  `coupling-interval-bb-infeasible-10s` (checked / measured) are filed and
  returned by `search_claims`. Honest ceilings preserved: neither drifted to
  `proved`. Claim 1's capture precision a≈0.3300622 (rounded to 0.33001 in the
  directive) is recorded.
- `write-step4-verdicts-to-scores-jsonl` — DONE. scores.jsonl rewritten with
  STEP 4 verdicts (Yu block SCORE 0.3823435642 on top; c0024–c0032 INVALID
  above ceiling; c0033 INVALID degenerate atom), SEARCH.md re-derived via
  derive_search.py, and `step4_verdicts_derived.captured.txt` shows ACCEPTANCE
  TEST PASS (0.421992 grep count 0). The old numeric exploit is gone from the
  derived record.

Neither was the scholar's doing; both were verified as already complete.

## Contradiction found: open task vs filed claim

The open task `verify-odd-filter-minmax` states (stale) that the odd filter
`2^[n]\{∅}` should be asserted as the **unique** minimizer of min-max-density
over non-Boolean union-closed families. The already-filed claim
`odd-filter-max-density-extremal-nonboolean` and its capture
`code/out/odd_filter_minmax.captured.txt` **refute that uniqueness**: the
minimizers are exactly n+1 families — the odd filter plus, for every x∈[n],
the power-set-minus-singleton family `2^[n]\{{x}}`, each with m=2^n−1 and max
density 2^{n-1}/(2^n−1). Verified exhaustively n=2,3,4 by the oracle and by an
independent inline route, and the structural fact (only UC families of size
2^n−1 are 2^[n]\{T} with T=∅ or a singleton) holds for general n by exact
arithmetic, verified n=2..8.

**Action needed:** the `verify-odd-filter-minmax` task is stale and should not
be re-run as written (it would re-assert a false uniqueness). If it is to be
kept, it must assert the *corrected* conclusion: value 2^{n-1}/(2^n−1) correct,
uniqueness FALSE, n+1 minimizers.
This reached the claim store as `odd-filter-max-density-extremal-nonboolean`
(asserted), but was NOT in durable memory (recall returned nothing), consistent
with Cognee having been down when it was produced — so the durable gap is
closed only in this workspace record until Cognee recovers.

## What the rest of the reference library confirms (no action needed)

- Spence 2026 is digested (`spence-minimum-counterexample-odd`, asserted) and
  already in durable memory: a minimum-cardinality counterexample has odd
  |F|=2k+1, all element frequencies ≤ k, every admissibly-removable member
  omits a tight freq-k element (Thm 6.3/6.4); lattice form has every two
  meet-irreducibles sharing a lattice-tight join-irreducible (Thm 6.7). Compatible
  with (orthogonal to) ROOT's |F|≥51.
- The two Zenodo claimed proofs (Pompetzki "Lattice Lock"; Abdurakhmanov's
  algorithmic proof) are triaged: Pompetzki refused as not a primary treatment
  (`pompetzki-lattice-lock-refused`); Abdurakhmanov already covered by Spence's
  audit. Both are refused as citable mathematical results.
- The record is current and stable: published record Yu ≈0.38234 (Entropy 2023),
  Cambie ≈0.3823455 preprint, Liu ≈0.38271 conditional/unpublished; (3−√5)/2 is
  the iid-OR barrier only, escapable by dependent couplings.

## Durable findings this pass is responsible for (stored to workspace, not Cognee)

1. The stale-task contradiction above (task vs claim).
2. The odd-filter uniqueness-refutation, confirmed absent from durable memory
   and now recorded here.
3. The two deferred tasks verified complete.

These three are the extent of what this pass added; everything else in the
library was already digested and consistent.
