# SUPPLY via the order-K squared excess — the unexplored 1 < K ≲ n/2 territory

This is the second-pass goal (GOAL.md, REOPENED.md) decomposed into what would
suffice. Every prior skeleton lives at correlation order K = 1 (first moment,
`wt(Φ_n h) ≥ c·n`, or the raw switch density). The reopen refuted the belief
that every functional of the fold factors through pair correlations: at `n = 8`
the strings `h = e_6` and `h' = e_5` share the pair-correlation vector
`C₁ = (5,1,1,0)` yet have `S² = 0` and `S² = 4`. So the *squared excess*
`S² = ((n−2) − 2ν₂(n))²` is a functional sensitive to correlation order `> 1`,
and the measured threshold is `K*(n) ≈ ⌈n/2⌉` (`n = 4..20`, `n = 5` mismatches).
This skeleton prices exactly that functional.

```skeleton
goal: There is an arithmetic input C(h) on the prime gap-parity string, strictly weaker than pointwise mod-4 switch density, whose satisfaction forces ν₂(n) ≥ c·n on a density-1 set (second moment) or pointwise (fourth moment); the carrying functional is the squared excess S², sensitive to correlation order 1 < K ≲ n/2.
implies: G-functional-form expands S² in run-endpoint switch-sign products of order ≥2; G-order-k-sensitivity certifies S² is not K=1; G-input-price fixes C(h) ⇒ E[S²]=O(n); G-prime-satisfies-input gives C(h) for the real primes; G-control-implies-supply turns E[S²]=O(n) into density-1 SUPPLY; G-orderk-input-strictness certifies C is strictly weaker than switch density.
rests-on: excess-is-negative-character-sum, squared-excess-run-endpoint-product, no-standalone-switch-sign-in-squared-excess, fold-distance-enumerator-On, downset-row-intersection-meet-formula, endpoint-sign-corrected-identity, fourth-moment-plateau-3n2
status: sketched
```

```gap
id: G-functional-form
lemma: >
  S(n)² = (n−2) + Σ_{d≠d'} ∏_{R ∈ runs(M_d △ M_{d'})} χ(r_{a_R}) χ(r_{b_R}),
  and every off-diagonal product carries ≥ 2 factors of the switch sign — no
  standalone switch sign — so S² is a functional of correlation order ≥ 2.
status: discharged
discharged-by: >
  squared-excess-run-endpoint-product (the exact run-endpoint expansion; note:
  status asserted, the mechanical identity still wants a verification capture —
  that is a task, not a gap) and no-standalone-switch-sign-in-squared-excess
  (proved — the |M_d △ M_{d'}| is always even for d,d' ≥ 2, so no singleton, and
  the distance-2 stratum is products of exactly two non-adjacent switch signs).
```

```gap
id: G-control-implies-supply
lemma: >
  E[S(n)²] = O(n) (equivalently Z(n) = S(n)/√n has bounded second moment) forces
  ν₂(n)/n → 1/2 on a density-1 set; the strengthening E[S(n)⁴] = O(n²) plus
  summability forces a finite exceptional set {n : ν₂/n < c} for every c < 1/2,
  i.e. pointwise SUPPLY.
status: discharged
discharged-by: >
  fold-distance-enumerator-On (proved — F_n(z) = O(n) is the geometry that
  reduces density-1 SUPPLY to exactly this second-moment input; see also
  downset-row-intersection-meet-formula), excess-is-negative-character-sum
  (checked — the S ↔ ν₂ identity), and the Chebyshev / fourth-moment glue is
  elementary, stated in research/CONCLUSION.md §5; the fourth-moment plateau is
  measured (fourth-moment-plateau-3n2), not proved, so the pointwise upgrade's
  *premise* E[S⁴] = O(n²) remains arithmetic, but the glue premise⇒conclusion
  is settled.
```

```gap
id: G-order-k-sensitivity
lemma: >
  S² is not determined by the order-1 (pair) correlation data of h: for a
  sequence of n → ∞ there exist binary strings h, h′ with identical order-1
  correlation vector C₁ but S²(h) ≠ S²(h′). Sharper target: K*(n) := min{ K :
  C_K determines S² on every C_K-fibre } satisfies K*(n) ≥ c·n for an absolute
  c > 0 (measured K*(n) ≈ ⌈n/2⌉ for n = 4..20; n = 5 gives K* = 2, mismatching
  ⌈n/2⌉ = 3, so the closed form is not yet right — GOAL priority 3).
status: open
next: >
  (a) Pin the definition of the correlation vector C_K from the external witness
  run (2628fcfb): the files research/witness-hunt-n20-imported.txt and
  research/witness-crosscheck-imported.txt carry the data but not the definition;
  file the n=8 witness (e_6 vs e_5, C₁=(5,1,1,0), S²=0 vs 4) as a claim.
  (b) tool_builder/sat_solver: for each (n,K) encode "∃ h,h′ ∈ F₂ⁿ with
  C_K(h)=C_K(h′) and S²(h)≠S²(h′)" as a SAT instance and push K*(n) past n=20 —
  the brute F₂ⁿ×F₂ⁿ fibre enumeration is exponential, so the SAT encoding is the
  right finite question (the C_K constraints are linear over F₂ in the
  coordinates of h,h′ up to the S² comparison, decidable at n ≤ 40).
  (c) theorem_prover: prove K*(n) ≥ c·n by an explicit witness family — the n=8
  witness is two single-1 strings, so compute C₁(e_j) and the read-count
  #{d : e_j read by depth d} in closed form (S²(e_j) = ((n−2) − 2·readcount)²)
  and find j, j′ with C₁(e_j) = C₁(e_{j′}) but different read-counts.
```

```gap
id: G-input-price
lemma: >
  There is an explicit arithmetic hypothesis C(h) on the prime gap-parity string
  h — a submask-window second-moment bound, or equivalently a Walsh/dual bound
  on the submask-XOR coordinates T(d) = ⨁_{i⊆d} h(i) — such that
  C(h) ⇒ E[S(n)²] = O(n), with the exact window family and the constant demanded
  of h stated. The implication is pure F₂ structure of the fold, no number theory.
status: open
next: >
  tool_builder + symbolic_math: expand E[S²] in the run-endpoint character
  products of G-functional-form and group terms by popcount / run structure, to
  name the exact window family whose correlations C(h) must bound — the
  distance-2 stratum reads the dyadic-lag autocorrelation
  (a2-is-theta-log-squared-confirmed), and the full sum is controlled by the
  popcount split already in fold-distance-enumerator-On. theorem_prover/lean:
  formalise "bound on these named submask-window correlations ⇒ E[S²] = O(n)"
  from downset-row-intersection-meet-formula — pure F₂, no number theory.
  Candidate inputs to price against are the ones named in GOAL.md priority 2:
  submask-window Walsh bound, dyadic-lag correlation decay; bounded raw
  autocorrelation is already priced out as non-discriminating
  (bounded-raw-autocorr-not-discriminating).
```

```gap
id: G-prime-satisfies-input
lemma: >
  The real prime gap-parity string h[j] = [q_{j+1} ≢ q_j mod 4] satisfies the
  condition C(h) of G-input-price, unconditionally or conditional on Shiu 2000.
  This is research/CONCLUSION.md §5's single surviving open statement, now as a
  *priced* input rather than an unpriced need.
status: open
next: >
  This is the arithmetic heart; its first move runs today independently of which
  C is fixed. tool_builder: compute the empirical Walsh coefficients and the
  submask-window (dyadic-lag) autocorrelations of h up to n = 10^6, and record
  each measured value against the threshold C(h) demands once G-input-price fixes
  it — the deliverable is a table "named input ⇒ measured value vs demanded
  threshold". lean_prover: formalise "C(h) ⇒ E[S²] = O(n)" for the *fixed* prime
  string with the arithmetic input named, no sorryAx. Honest negative exit: if
  the only input that implies E[S²] = O(n) is positive switch density itself,
  the output is the rival equivalence (result type 5), not a claim of this route.
```

```gap
id: G-orderk-input-strictness
lemma: >
  The input C(h) of G-input-price is strictly weaker than pointwise mod-4 switch
  density: there is a binary string h* with switch density 0
  (lim (1/n) Σ_{j<n} h*[j] = 0) that satisfies C(h*), so by G-input-price +
  G-control-implies-supply it has ν₂(h*)/n → 1/2 on a density-1 set while the
  raw switch-density form sees nothing — the fold does work the reduction
  discards.
status: open
next: >
  sat_solver/tool_builder: search for a sparse h ∈ F₂ⁿ with wt(h) ≤ δn and
  sublinear excess S(n) = O(√n) (equivalently E[S²] = O(n)), over a δ→0 grid,
  n = 8..64. The known sparse witness h = e_{2^m} (switch-equivalence.md's killed
  gap) has switch density 0 but S = Θ(n) at dyadic n, so it does NOT satisfy C;
  the strictness witness must keep S = O(√n) with wt = o(n). If instead the
  maximum fold weight over k-sparse inputs is sublinear in n uniformly in k/n,
  this gap is refuted and the skeleton dies into result type 5 — the two
  directions are the same finite computation, so the run should settle it once.
```
