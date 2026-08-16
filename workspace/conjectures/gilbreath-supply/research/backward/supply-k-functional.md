# SUPPLY via a correlation-order-K functional (the reopened question, positive branch)

This skeleton decomposes the single question GOAL.md reopened this pass for:

> Is there a functional of the fold, sensitive to correlation order `K` with
> `1 < K ≲ n/2`, that is controllable by an arithmetic input strictly weaker
> than pointwise mod-4 switch density?

It refines `weak-input-fold.md` (whose condition C is unpriced and can be K=1)
and is the positive rival of the priority-4 negative theorem. The functional is
**not** to be invented ex nihilo: the collapse-refutation witness
(`research/witness-crosscheck-imported.txt`, `n=8`: `h=00000010` and
`h'=00000100` share the order-1 correlation vector `C₁=(5,1,1,0)` yet have
`S²=0` and `S²=4`) already identifies the separating functional as
`S²(n) = (Σ_{d=2}^{n−1} (−1)^{T(n,d)})²` — the signed-excess square. The job is
to generalize that witness, price S², and control it.

```skeleton
goal: The reopened question answered YES (problem.md result 4, sharpened by
  REOPENED.md): the signed-excess square S²(n) = (Σ_{d=2}^{n−1}(−1)^{T(n,d)})²
  is a functional of the fold sensitive to correlation order K for every
  2 ≤ K ≤ ⌈n/2⌉−1 (so it beats the k1-collapse that killed the eight first-pass
  routes), and there is an arithmetic input I(h) on the prime gap-parity string
  h, strictly weaker than positive mod-4 switch density, with I(h) ⇒ S²(n)=O(n)
  for all large n. Consequently ν₂(n)/n → 1/2 on a density-1 set — density-1
  SUPPLY from a strictly weaker input than the dead-end reduction.
implies: Lemma G-kstar-budget identifies S² as the K>1 functional: for every
  n ≥ 6 it is not a function of the order-K correlation vector C_K for any
  K < ⌈n/2⌉, so it reads correlation order strictly above 1 (priority 1 and 3
  of GOAL.md). Lemma G-k-functional-price exhibits the input I: by the exact
  identity squared-excess-run-endpoint-product,
  S²(n) = (n−2) + Σ_{d≠d'} ∏_{R∈runs(M_d△M_{d'})} χ(r_{a_R})χ(r_{b_R}), and
  the weight of this off-diagonal sum is O(n) geometry by
  fold-distance-enumerator-On, so a bound I on the run-endpoint character
  products (an order ≥ 2 object by no-standalone-switch-sign-in-squared-excess)
  gives I ⇒ S²(n)=O(n). Lemma G-k-functional-strictness proves I is strictly
  weaker than switch density by exhibiting a switch-density-0 string satisfying
  I with S²(n)=Ω(n). Lemma G-k-functional-primes supplies I(h) for the real
  prime string, unconditionally or on a named input at least as weak. Chaining:
  I(h) ⇒ S²(n)=O(n); by excess-is-negative-character-sum,
  S² = (n−2−2ν₂)², so Chebyshev over n ≤ N gives
  |{n≤N : ν₂(n) < c·n}|/N ≤ O(1/(c²n)) → 0 for every c < 1/2 — density-1
  SUPPLY — and the chain does not collapse to the switch-density reduction
  because G-k-functional-strictness shows I is strictly weaker. If instead
  G-k-functional-primes is forced into a length-K pattern-frequency statement,
  that is the parity barrier itself and the honest output is the priority-4
  negative theorem (this skeleton's rival), not a claim of result 4.
status: sketched
rests-on: excess-is-negative-character-sum, fold-distance-enumerator-On,
  no-standalone-switch-sign-in-squared-excess,
  squared-excess-run-endpoint-product (asserted, needs machine check),
  downset-row-intersection-meet-formula, a2-is-theta-log-squared-confirmed,
  fair-model-exact-binomial
```

```gap
id: G-kstar-budget
lemma: For n ≥ 2 let C_K(h) be the order-K correlation vector of h ∈ F₂ⁿ (the
  counts of every binary word of length K+1 in h, overlapping windows), and let
  K*(n) be the largest K < n−1 for which there exist h,h′ with C_K(h)=C_K(h′)
  but S²(h) ≠ S²(h′). Then K*(n) = ⌈n/2⌉ for all n ≥ 6 — equivalently S² is a
  function of C_K iff K ≥ ⌈n/2⌉, and for every 2 ≤ K ≤ ⌈n/2⌉−1 there is a pair
  agreeing on C_{K−1} but separated by S². In particular S² is sensitive to
  correlation order K for every 1 < K ≲ n/2, which is exactly the
  k1-collapse-free territory of GOAL priority 1. The small-n deviations
  K*(3)=1 and K*(5)=2 (both ⌊n/2⌋) are part of the statement to explain, not
  exceptions to be swept under the rug.
status: open
next: Two moves, both runnable today. (a) tool_builder: extend the witness hunt
  `research/witness-hunt-n20-imported.txt` (currently n ≤ 20) to n ≤ 64 using
  the canonical oracle (`code/lib`, `assert_supply_guard`), and for each n
  report the minimal K with a C_K-separating pair plus whether K*(n)=⌈n/2⌉; the
  capture states its range and carries a negative control (a deliberately
  wrong closed form) shown failing. (b) theorem_prover/lean_prover: derive the
  sharp bound from the binary Steinhaus horizontal-symmetry dimension
  ⌈n/2⌉ (source binary_steinhaus_triangles_rule90): the C_K-fiber of h is the
  projection onto order-≤K correlations, and S² factors through C_K exactly
  when the off-diagonal Gram contributions vanish on that fiber — connect the
  ⌈n/2⌉-symmetry space to the meet formula
  downset-row-intersection-meet-formula and formalise the statement with
  #print axioms and no sorryAx.
```

```gap
id: G-k-functional-price
lemma: There is an explicit condition I(h) on the prime gap-parity string,
  stated as a bound on the run-endpoint character products
  ∏_{R∈runs(M_d△M_{d'})} χ(r_{a_R})χ(r_{b_R}) appearing in the exact identity
  squared-excess-run-endpoint-product, such that (i) I(h) ⇒ S²(n) = O(n) for
  all large n, and (ii) I(h) does not imply positive mod-4 switch density. The
  geometry half is discharged: the diagonal plus the O(n) weight of the
  off-diagonal sum is fold-distance-enumerator-On, so I only has to bound the
  character products at the classified run endpoints, and by
  no-standalone-switch-sign-in-squared-excess no summand is a single switch
  sign u_j = χ(r_j)χ(r_{j+1}) — the input is genuinely of order ≥ 2 in χ.
status: open
next: (a) tool_builder: from the exact identity, produce the pricing table GOAL
  priority 2 asks for — for each symmetric-difference stratum (popcount pair
  p,q, via downset-row-intersection-meet-formula), record the correlation order
  K of h that the term ∏_R χ(r_{a_R})χ(r_{b_R}) measures; the distance-2
  stratum is already known to be order 4 (a2-is-theta-log-squared-confirmed),
  and the claim to establish is that every stratum has order ≥ 2 with the bulk
  at order Θ(p+q). (b) theorem_prover: for the candidate
  I = "Σ over strata of order-K correlations is O(n)", formalise I ⇒ S²=O(n)
  as a first-order implication over F₂, refuting its negation with
  eprover/z3 on small n before scaling.
```

```gap
id: G-k-functional-strictness
lemma: There is a binary string h* realisable by a {1,3}-valued boundary (so it
  is a legitimate gap-parity string) with switch density 0 —
  #{j : h*[j]=1} = o(n) — that satisfies the input I(h*) of
  G-k-functional-price and has S²(h*) = Ω(n). This proves I is strictly weaker
  than pointwise mod-4 switch density: the fold has a linear-weight image on a
  sparse input, so the K>1 functional does work the switch-density reduction
  discards. Note the seed is already on disk: h = e_{2^m} has switch density 0
  and S² = n−O(1) — the witness that broke switch-equivalence.md — so the open
  content is only whether such a string satisfies the candidate I.
status: open
next: sat_solver / tool_builder: for n = 8..64, encode "∃ h ∈ F₂ⁿ with
  wt(h) ≤ δn, h satisfying the candidate I from G-k-functional-price, and
  wt(Φ_n h) ≥ εn" as a CP-SAT/SAT instance over a grid (δ,ε) with δ→0; report
  SAT witnesses or UNSAT thresholds, and separately check whether the e_{2^m}
  family satisfies I. This is the same finite computation as
  G-weak-input-strictness in weak-input-fold.md, now pinned to the K>1
  functional and its priced input. A UNSAT threshold at every reachable n is
  evidence (not proof) for the priority-4 rival.
```

```gap
id: G-k-functional-primes
lemma: The real prime gap-parity string h[j] = ((q_{j+1}−q_j)/2) mod 2 satisfies
  I(h) — the input from G-k-functional-price — unconditionally, or conditional
  only on a named arithmetic input at least as weak. This is the arithmetic
  heart: for the candidate I = "off-diagonal run-endpoint character sum is
  O(n)", I(h) is exactly the surviving open statement E[S²(n)]=O(n) for the
  specific prime string (research/CONCLUSION.md §5), in the K>1 run-endpoint
  coordinates rather than the collapsed g=0 switch form.
status: open
next: research + theorem_prover: reduce I to a named unconditional K>1 statement
  about consecutive-prime residues and price it against the parity barrier.
  Length-k non-constant patterns are open for every k ≥ 2
  (wu_nonuniform_residues_prime_sequences, lau-nonconstant-pattern-open), and
  the strongest unconditional K>1 constraint on disk — the Lacasa forbidden
  gap-block (lacasa-forbidden-gap-blocks-unconditional) — is invisible to the
  fold (lacasa_parity_projection_transfer), so the concrete first move is to
  write the exact K>1 character sum and state which side of the parity barrier
  it sits on. If it is a length-K pattern frequency, this gap is the parity
  barrier itself, this skeleton's positive branch dies, and the honest output
  is the priority-4 equivalence theorem.
```

The rival negative branch is GOAL priority 4 — *prove* (not observe) that every
order-K functional of the fold collapses to the switch-density object, with the
eight first-pass routes replaced by a theorem. If G-k-functional-primes prices
out as a length-K pattern frequency, that rival becomes the skeleton to open;
it is deliberately not opened here, because at most one of the two branches can
be discharged and the positive branch is the one GOAL.md says to try first.
