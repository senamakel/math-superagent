# Scholar audit — contradiction resolved: verification scripts DID run

**Finding.** A durable Cognee memory claimed `code/scholar_verify_claims.py` and
`code/verify_sources.py` were "written but NEVER executed" with no captured
output, so the `checked` marking of three claims was "unsupported." That memory
is **false**. The captured outputs exist on disk and were read directly this run:

- `code/out/scholar_verify_claims.captured.txt` → "minkowski-sum distance-1
  identity: verified on 2000 exact random pairs over Q(sqrt3)";
  "eisenstein lattice N==1 iff a unit over [-12,12]^2"; "sat encoding
  4-colourable=True witness (0,1,2,0,1,2,3); 3-colourable=False";
  "ALL SCHOLAR CLAIM CHECKS PASSED".
- `code/out/verify_sources.captured.txt` → Eisenstein 6 unit vectors all
  `|z|^2=1`; Minkowski T+T = 6 vertices / 9 unit edges / chi=3.
- `code/out/scholar_verify_library.captured.txt` → K2..K7 min_degree=k-1 all
  true; "ALL LIBRARY CHECKS DONE".
- `code/out/crosscheck_triangle_sum.captured.txt` → "CROSS-CHECK: PASSED
  (agrees with verify_sources: n=6, m=9, chi=3)".

**Consequence.** CLAIMS.md's `status: checked` for
`minkowski-sum-unit-distance-condition`, `einstein-lattice-unit-distance`, and
`sat-k-colourability-encoding` is **correct** and legitimate. Agents should
trust the captured files over the stale memory. The Minkowski distance-1
identity and the Eisenstein lattice facts are machine-checked, not merely
asserted.

**What stays asserted-by-source (not machine-checked).**
`debruijn-erdos-1951`, `spencer-szemeredi-trotter` O(n^{4/3}), `maehara-1991`,
`kempe-universality`, `critical-minimum-degree`, `lovasz-sandwich-theta`,
`szemeredi-trotter-incidence`, the three graph-product results
(El-Zahar-Sauer, Tardif, Duffus-Sands-Woodrow), `barajas-serra-periodic-attainment`,
`liu-distance-graph-survey`, `minkowski-sum-dense-graphs`. These are general
graph theory / classical theorems treated as inputs, not re-derived here. That
is the correct status, not a defect.

Saved to Cognee via `remember_memory` (correction note; graph-product tier;
verified size-bound).
