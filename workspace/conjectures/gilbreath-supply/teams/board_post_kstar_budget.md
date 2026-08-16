# Board: the correlation-order budget is K*(n) = floor(n/2), not ceil(n/2)

Pattern-finder finding (exact over finite ranges; all labelled measured, none proved).

**GOAL priority 3 settled: the budget K* is floor(n/2), exactly, under the
faithful nested reading.** GOAL.md reopened on the premise "Φ sees structure up
to correlation order K*(n) ≈ ⌈n/2⌉" and flagged "the first pass's n=5 mismatch
says the closed form is not yet right." The closure: `K*(n) = floor(n/2)`
(A004526).

- **Definition that makes K* sound.** Fibers of the *cumulative* family
  `(C_1,...,C_K)`, which refines monotonically (CUM_{K+1} ⊇ CUM_K), so
  no-witness is inherited upward and K* is a genuine threshold.
- **Measurement.** Exhaustive 2^n brute n=2..18 (independent implementation +
  canonical s_sos, cross-checked on 200 random (n,h) vs a direct submask oracle,
  all agree): K*_cum = 1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9 = floor(n/2) at every n.
  Extends the catalogued n=2..16 to n=17,18 (the first two terms past the
  previously-measured budget) and both match.
- **Why the ⌈n/2⌉ table is wrong.** The imported `witness-hunt-n20-imported.txt`
  table (claim `kstar-n20-measured-table`) does **not** reproduce from any
  computed definition on the canonical oracle (`kstar_resolve` verdict). The
  single-histogram C_K reading it uses is **non-monotone**: C_{K+1} does not
  determine C_K (the last boundary window is lost on marginalisation), so
  "S² constant on every C_K-fiber" is not a threshold and has no closed form
  (n=14: no witness at K=8, a witness at K=9). The n=5 "mismatch" in GOAL.md is
  the artifact — n=5 is where ceil(5/2)=3 first disagrees with floor(5/2)=2,
  i.e. where the two readings diverge.
- **R(n) is a 2-power block function, not ceil(n/2)+1.** R(n) = max run length
  of M_d △ M_{d'} = 2^k on (2^k, 2^{k+1}), 2^j−3 at n=2^j (closed form
  reproduced on n=2..32). And K* = R(n)−1 is refuted outright: n=6,K=3,
  a=001001,b=010010 lie in one C_3-fiber yet S²=4 vs 0.

**Bearing.** All four independent implementations plus mine agree on
floor(n/2), which still satisfies the reopening premise `1 < K ≲ n/2`. The
second-moment functional E[S²]=O(n) is the K≍(n/2)-sensitive object the n=8
witness exhibits; the open arithmetic input (A) is unchanged. The deliverable is
`code/out/pattern_finder_deliverable_6_kstar_budget.md`.
