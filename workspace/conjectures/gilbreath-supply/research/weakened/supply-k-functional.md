# SUPPLY — the correlation-order ladder (reopened, corrected)

This is the SUPPLY ladder for the reopened question in `research/REOPENED.md` and
`GOAL.md`. The first pass closed believing every second-moment route collapsed at
the coarsest dyadic scale `g=0` to the mod-4 switch-pair correlation, so
equivalence to switch density was "indicated". `REOPENED.md` refuted that collapse
with an explicit witness (`n=8`: `h=00000010`, `h'=00000100` share
`C₁=(5,1,1,0)` but have `S²=0` vs `4`), and measured witnesses up to correlation
order `K*(n) ≈ ⌈n/2⌉` for `n=4..20`. The eight collapses were a property of the
eight routes, not a law about `Φ`.

This ladder supersedes the difficulty decomposition in `supply.md` (which predates
`REOPENED.md`) but keeps every rung there. It names the two new difficulties the
reopening created — `k1-collapse` (a K=1 functional cannot beat switch density)
and `order-budget-unproved` (the `⌈n/2⌉` sensitivity budget is a measurement, not
a theorem) — and it corrects the false finite-verified rung.

```ladder
goal: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n, where ν₂(n) = wt(Φ_n h) over F₂, h[j] = ((q_{j+1} − q_j)/2) mod 2, and Φ_n is the Pascal-mod-2 (submask-XOR) fold of problem.md.
difficulties: primes-input, pointwise-all-n, unconditional-effective, k1-collapse, order-budget-unproved, submask-read
status: open
```

- `primes-input` — the real h is the prime gap-parity string; unconditional control
  of its index-domain correlations at order ≥ 2 sits behind the parity barrier
  (ABGS 2011 §9: consecutive-pair class frequencies are open and L-function-
  inaccessible).
- `pointwise-all-n` — ν₂(n) ≥ c·n must hold for every n past one threshold, not
  merely on a density-1 set, in expectation, a.s. for a random input, or on a
  finite prefix.
- `unconditional-effective` — c > 0 must be explicit and effective, and the proof
  may use no unproved arithmetic hypothesis (Shiu 2000 is held only conditionally).
- `k1-collapse` — any functional sensitive only to correlation order K=1 factors
  through the mod-4 switch-pair correlation at the g=0 dyadic scale (eight
  independent routes shared this weakness). Beating switch density needs
  sensitivity to order 1 < K ≲ n/2; the live risk is that the sensitivity
  re-collapses to K=1 as n grows.
- `order-budget-unproved` — K*(n) ≈ ⌈n/2⌉ is measured only to n=20; the closed
  form is unproved and n=5 is a mismatch (K*(5)=2, not 3). "A functional reaches
  order ~n/2 for all n" is a measurement, not a theorem, until the budget is
  established.
- `submask-read` — Lucas confines Φ_n to reading h only along binary-submask XORs
  ⟨h, χ_S⟩; usable input must be stated in those coordinates, and "h is
  complicated enough" hypotheses are dead (the five closed doors in problem.md).

```rung
id: R-random-expectation
statement: For h uniform on F₂ⁿ, E_h[wt(Φ_n h)] = (n−2)/2 ≥ n/3 for every n ≥ 6, by rank Φ_n = n−2 (full row rank of the operative (n−2)×n matrix, rows d=2..n−1). The fold imposes no weight obstruction on generic input.
off: primes-input, pointwise-all-n, unconditional-effective
stance: settled
merge: Settled by C-fold-generic-expectation and fold-rank-n-minus-2-binomial-proved. Turn `pointwise-all-n` back on → R-random-pointwise, which is already settled, so no further work on the generic side.
```

```rung
id: R-random-pointwise
statement: For h uniform on F₂ⁿ, wt(Φ_n h) ≥ c·n with probability 1 − exp(−Ω_c(n)) for every fixed c < 1/2; in particular wt(Φ_n h) ≥ n/4 w.h.p. The fold's weight is linear on generic input, not merely in expectation.
off: primes-input, unconditional-effective
stance: settled
merge: Settled by uniform-random-h-supply-whp, fair-model-exact-binomial, and r-random-pointwise-closed-by-exact-binomial: rank Φ_n = n−2 (nullity 2) makes Φ_n surjective onto F₂^{n−2}, so wt(Φ_n h) is exactly Binomial(n−2,1/2) and Chernoff closes the concentration. The old merge-caveat (a rank-2 map F₂²→F₂ⁿ has half its vectors below n/4) is the wrong direction — surjectivity into the (n−2)-image is already enough. Turn `primes-input` back on: replace "h random" with a deterministic condition C(h) in submask-XOR coordinates, reached through R-k-functional-input below.
```

```rung
id: R-finite-verified
statement: For the real prime string h (floored convention, index 2), ν₂(n)/n ≥ 0.42 for every n with 275 ≤ n ≤ 40000, and the full exceptional set {n ≤ 40000 : ν₂(n)/n < 0.42} is exactly {53, 56, 62, 71, 103, 105, 145, 153, 210, 274}, with deepest dip ν₂(53)/53 = 0.3585. Numerical evidence, not a theorem. (The earlier reading "ν₂/n ≥ 0.42 for every 50 ≤ n ≤ 4000" is FALSE — those 10 dips in [50,274] violate it.)
off: pointwise-all-n
stance: settled
merge: Settled by dip-boundary-effect-small-n, dip-sparsity-to-20000, and exceptional-sets-finite-through-40000; the contradiction claim r-finite-verified-contradicted records the correction to the range. Turn `pointwise-all-n` back on → R-averaged-supply (density-1) or R-conditional-pointwise. A bare computation cannot reach a proof; this rung is the oracle anchor, not a stepping stone.
```

```rung
id: R-k1-functional
statement: There is a functional of the fold sensitive only to correlation order K=1 (pair correlations) that, together with an arithmetic input strictly weaker than positive mod-4 switch density, forces ν₂(n) ≥ c·n for all large n.
off: pointwise-all-n, unconditional-effective
stance: failed
failed-by: Eight independent K=1 second-moment routes all collapsed at g=0 to the mod-4 switch-pair correlation — the very object (positive switch density) such a functional would have to beat, so a K=1 functional cannot beat switch density. REOPENED.md shows the collapse is a property of those eight routes, not of Φ, but the K=1 route itself is spent.
merge: To climb, raise the order: R-budget-n32 establishes how far sensitivity reaches, R-k-functional generalises the witness.
```

```rung
id: R-budget-n32
statement: K*(n) = ⌈n/2⌉ for every n with 6 ≤ n ≤ 32, with n=5 the sole exception (K*(5)=2=⌈5/2⌉−1), where K*(n) is the largest K such that two strings with identical correlation vectors C₁,…,C_K (identical (K+1)-gram histograms) have different S(n)², and no such pair exists at K = K*(n). For each 6 ≤ n ≤ 32, explicit witness pairs exist for every K < K*(n).
off: primes-input, unconditional-effective, pointwise-all-n
stance: open
merge: Extend the n=4..20 witness hunt (research/witness-hunt-n20-imported.txt, already at K*=1,1,2,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10) to n=21..32 with the canonical floored oracle. First move is an algebraic reformulation to check, not assumed: with x_j = (−1)^{h_j}, the off-diagonal term of S(n)² is ∏_{j ∈ M_d △ M_{d'}} x_j, so S² is determined by C₁,…,C_K exactly when every symmetric-difference monomial has index-width ≤ K+1 — making K*(n) the maximum index-width of a monomial the C_K histogram fails to pin. Falsifier: any n in [6,32] with K*(n) ≠ ⌈n/2⌉ (or a second mismatch beyond n=5). Then push to n=128 and prove the closed form for all n (that is R-k-functional's prerequisite). Expected bite: `k1-collapse`, if the ⌈n/2⌉ growth is a small-n artifact and sensitivity re-collapses as n grows.
```

```rung
id: R-k-functional
statement: There exists a functional F of the fold, defined for all n, that is provably sensitive to correlation order K with 1 < K ≲ n/2 — i.e. for all large n some pair h, h′ with identical correlation vectors of order ≤ 1 have F_n(h) ≠ F_n(h′). S(n)² is the candidate; the n=8 witness (h=00000010, h′=00000100 share C₁=(5,1,1,0) but S²=0 vs 4) is the seed.
off: primes-input, unconditional-effective, pointwise-all-n
stance: open
merge: Generalise the n=8 witness via the monomial reformulation from R-budget-n32: exhibit, for all large n, a symmetric-difference monomial of index-width > 2 in S². Claim no-standalone-switch-sign-in-squared-excess already gives the start — every nonzero off-diagonal term has a single run of even length ≥ 4, so no term is a single switch sign. Then turn `primes-input` back on via R-k-functional-input. Expected bite: `k1-collapse` (does sensitivity re-collapse at larger n) and `submask-read` (F must live in ⟨h,χ_S⟩ coordinates and avoid the five closed doors).
```

```rung
id: R-k-functional-input
statement: There is a functional F of the fold, sensitive to correlation order K with 1 < K ≲ n/2 (so it beats k1-collapse), such that F(h) ≥ c·n is forced by an arithmetic input I(h) on the real prime gap-parity string strictly weaker than pointwise mod-4 switch density, and F(h) ≥ c·n implies ν₂(n) ≥ c′·n for all large n. This is GOAL.md priority 2.
off: unconditional-effective
stance: open
merge: Price the single open scalar S(n) = O(√n) for the prime h: claim squared-excess-run-endpoint-product rewrites it exactly as a submask-window second moment at correlation order ≥ 2, never a standalone switch sign (no-standalone-switch-sign-in-squared-excess). If the only input that implies it is switch density itself, the honest close is R-switch-equivalence (GOAL priority 4). Turn `unconditional-effective` back on: prove the named input unconditionally or replace it with one that is.
```

```rung
id: R-averaged-supply
statement: There is c > 0 and a set S of natural density 1 such that ν₂(n) ≥ c·n for every n ∈ S, where h is the real prime gap-parity string. Equivalent (Chebyshev) to E[S(n)²] = O(n). The parity barrier is pointwise and sometimes porous on average.
off: pointwise-all-n
stance: open
merge: Turn `pointwise-all-n` back on: promote the density-1 set S to a cofinite one. First move — find the structure of the exceptional set {n : ν₂(n)/n < c}; it is measured finite through 40000 (exceptional-sets-finite-through-40000), so name what would make a density-1 set fail to be cofinite, else the promotion is free. Incomparable with R-conditional-pointwise (unconditional-but-averaged vs conditional-but-pointwise).
```

```rung
id: R-conditional-pointwise
statement: ν₂(n) ≥ c·n for all sufficiently large n, conditional on one named weak arithmetic input about the real prime string h — for instance Shiu 2000 (held abstract in problem.md), or a stated second-moment / Walsh-coefficient bound on h. c is explicit; one arithmetic hypothesis may be assumed.
off: unconditional-effective
stance: open
merge: Turn `unconditional-effective` back on: prove the named input unconditionally or replace it with one that is, else SUPPLY stays conditional and the honest result is "SUPPLY is equivalent to that input". The K>1-flavored sharpening is R-k-functional-input; this rung admits any weak input including a K=1 one.
```

```rung
id: R-switch-equivalence
statement: For every binary string h, if ν₂(n) ≥ c·n for all sufficiently large n then h has positive mod-4 switch density. Equivalently: every h with switch density 0 has ν₂(n) = o(n). If true, the fold adds nothing beyond switch density and SUPPLY is equivalent to it. Rival of R-k-functional-input: at most one can be settled true.
off: primes-input
stance: open
merge: This rung is the honest negative close if settled (GOAL.md priority 4). If instead a counterexample h is found — switch density 0 yet ν₂(n) ≥ c·n — that settles R-k-functional-input positively, and merging means naming the functional F and the weak input from that witness, then turning `primes-input` back on. Note: the REOPENED witness does NOT settle this — it shows a K>1 functional exists, not that it beats switch density.
```

```rung
id: R-full-supply
statement: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n — the full SUPPLY conjecture, no difficulty switched off.
off:
stance: open
merge: Nothing left to switch off. If every previous rung merges back, this rung is reached and the ladder is exhausted. Expected last bite: `primes-input` (the parity barrier), reached through `submask-read` and a functional that beats `k1-collapse`.
```
