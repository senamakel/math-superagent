# SUPPLY — the correlation-order ladder (reopened)

This is the SUPPLY ladder re-built against the reopened question in
`research/REOPENED.md` and `GOAL.md`. The first pass closed on "every second-moment
route collapses at g=0 to mod-4 switch-pair correlation, so equivalence to switch
density is indicated". That collapse is refuted: `Φ` provably sees structure up to
correlation order `K*(n) ≈ ⌈n/2⌉` (explicit witness at n=8), so the eight collapses
were a weakness of the eight routes, not a law about the fold. This ladder names that
weakness as a difficulty (`k1-collapse`), records the failed K=1 rung, and climbs from
the settled generic/finite rungs through a K>1 functional to full SUPPLY.

It supersedes the difficulty decomposition in `supply.md` (which predates REOPENED.md)
but keeps every rung there. Where a rung is settled, the claim that settles it is named.

```ladder
goal: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n, where ν₂(n) = wt(Φ_n h) over F₂, h[j] = ((q_{j+1} − q_j)/2) mod 2, and Φ_n is the Pascal-mod-2 (submask-XOR) fold of problem.md.
difficulties: primes-input, pointwise-all-n, unconditional-effective, k1-collapse, submask-read
status: open
```

- `primes-input` — the real h is the prime gap-parity string; unconditional control of
  its correlations is the parity barrier (positive mod-4 switch density is open, ABGS
  2011 §9).
- `pointwise-all-n` — ν₂(n) ≥ c·n must hold for every n past one threshold, not merely on
  a density-1 set, in expectation, or a.s. for a random input.
- `unconditional-effective` — c > 0 must be explicit and effective, and the proof may use
  no unproved arithmetic hypothesis (Shiu 2000 is held only conditionally).
- `k1-collapse` — any functional sensitive only to correlation order K=1 collapses at the
  g=0 dyadic scale to the mod-4 switch-pair correlation; eight independent second-moment
  routes shared this weakness. Beating switch density needs sensitivity to order
  1 < K ≲ n/2 (REOPENED.md: K*(n) ≈ ⌈n/2⌉, witness at n=8).
- `submask-read` — Lucas confines Φ_n to reading h only along binary-submask XORs
  ⟨h, χ_S⟩; the usable input must be stated in those coordinates, and "h is complicated
  enough" hypotheses are dead (the five closed doors in problem.md).

```rung
id: R-random-expectation
statement: For h uniform on F₂ⁿ, E_h[wt(Φ_n h)] = (n−2)/2 ≥ n/3 for every n ≥ 6, by rank Φ_n = n−2 (full row rank of the operative (n−2)×n matrix, rows d=2..n−1). The fold imposes no weight obstruction on generic input.
off: primes-input, pointwise-all-n, unconditional-effective
stance: settled
merge: Turn `pointwise-all-n` back on: promote the expectation to concentration. That is R-random-pointwise, and it is already closed (next rung) — no further work here. Settled by C-fold-generic-expectation and fold-rank-n-minus-2-binomial-proved.
```

```rung
id: R-random-pointwise
statement: For h uniform on F₂ⁿ, wt(Φ_n h) ≥ c·n with probability 1 − exp(−Ω_c(n)) for every fixed c < 1/2; in particular wt(Φ_n h) ≥ n/4 w.h.p. The fold's weight is linear on generic input, not merely in expectation.
off: primes-input, unconditional-effective
stance: settled
merge: Nothing left on the generic side: rank Φ_n = n−2 (nullity 2) makes Φ_n surjective onto F₂^{n−2}, so wt(Φ_n h) is exactly Binomial(n−2, 1/2) and Chernoff closes the concentration. Turn `primes-input` back on: replace "h random" with a deterministic condition C(h) in submask-XOR coordinates. Settled by uniform-random-h-supply-whp, fair-model-exact-binomial, and r-random-pointwise-closed-by-exact-binomial (which also disposes of the old merge-caveat: the rank-2 map F₂²→F₂ⁿ was the wrong direction — surjectivity into the (n−2)-image is already enough).
```

```rung
id: R-finite-verified
statement: For the real prime string h (floored convention, index 2), ν₂(n)/n ≥ 0.42 for every n with 50 ≤ n ≤ 4000, c = 0.42 explicit. Numerical evidence, not a theorem.
off: pointwise-all-n
stance: settled
merge: Turn `pointwise-all-n` back on: extend the range past 4000, or promote to a density-1 set (R-averaged-supply). A bare computation cannot reach a proof; this rung is the oracle anchor, not a stepping stone. Settled by the n=4000 sweep; sharpened numerically by dip-boundary-effect-small-n and exceptional-sets-finite-through-40000.
```

```rung
id: R-k1-functional
statement: There is a functional of the fold sensitive only to correlation order K=1 (pair correlations) that, together with an arithmetic input strictly weaker than positive mod-4 switch density, forces ν₂(n) ≥ c·n for all large n.
off: pointwise-all-n, unconditional-effective
stance: failed
merge: Failed as pursued — eight independent second-moment routes all collapsed at the g=0 dyadic scale to the mod-4 switch-pair correlation (this is the observation the first pass read as equivalence). This is NOT a proof of impossibility: REOPENED.md refutes exactly that reading (Φ sees structure to order ⌈n/2⌉). Do not re-propose a K=1 route; the fix is to raise the correlation order — R-k-functional. The finding: the collapse was a property of the eight routes, not of Φ.
```

```rung
id: R-k-functional
statement: There exists a functional F of the fold, defined for all n, that is provably sensitive to correlation order K with 1 < K ≲ n/2 — i.e. for all large n some pair h, h′ with identical correlation vectors of order ≤ 1 have F_n(h) ≠ F_n(h′). The n=8 witness (h = 00000010, h′ = 00000100 share C₁ = (5,1,1,0) but S² = 0 vs 4) is the seed to generalize; S² itself is the candidate functional.
off: primes-input, unconditional-effective, pointwise-all-n
stance: open
merge: Read off exactly what S² separates in the n=8 witness — the separating coordinate pattern in submask-XOR coordinates — and generalize it to a functional defined for all n. Then turn `primes-input` back on via R-k-functional-input: price what arithmetic input on the prime string forces F to be large. Expected bite: `submask-read` (the functional must live in ⟨h,χ_S⟩ coordinates and avoid the five closed doors), and the risk that the generalized functional collapses back to K=1 at larger n (`k1-collapse`).
```

```rung
id: R-k-functional-input
statement: There is a functional F of the fold, sensitive to correlation order K with 1 < K ≲ n/2 (so it beats k1-collapse), such that F(h) ≥ c·n is forced by an arithmetic input I(h) on the real prime gap-parity string strictly weaker than pointwise mod-4 switch density, and F(h) ≥ c·n implies ν₂(n) ≥ c′·n for all large n. This is GOAL.md priority 2.
off: unconditional-effective
stance: open
merge: Turn `unconditional-effective` back on: prove the named input unconditionally or replace it with one that is, else the honest result is "SUPPLY is equivalent to that input" (R-switch-equivalence). Sharpens R-conditional-pointwise by requiring the input to route through a K>1 functional rather than any weak input.
```

```rung
id: R-averaged-supply
statement: There is c > 0 and a set S of natural density 1 such that ν₂(n) ≥ c·n for every n ∈ S, where h is the real prime gap-parity string. The parity barrier is pointwise and sometimes porous on average.
off: pointwise-all-n
stance: open
merge: Turn `pointwise-all-n` back on: promote the density-1 set S to a cofinite one. First move — find the structure of the exceptional set; if it is finite or sparse enough, the promotion is free, else name what makes a density-1 set fail to be cofinite. Equivalent to proving E[S(n)²] = O(n) for the prime string (Chebyshev), which is open.
```

```rung
id: R-conditional-pointwise
statement: ν₂(n) ≥ c·n for all sufficiently large n, conditional on one named weak arithmetic input about the real prime string h — for instance Shiu 2000 (held abstract in problem.md), or a stated second-moment / Walsh-coefficient bound on h. c is explicit; one arithmetic hypothesis may be assumed.
off: unconditional-effective
stance: open
merge: Turn `unconditional-effective` back on: prove the named input unconditionally or replace it with one that is, else SUPPLY stays conditional. The K>1-flavored sharpening is R-k-functional-input; this rung admits any weak input including a K=1 one.
```

```rung
id: R-switch-equivalence
statement: For every binary string h, if ν₂(n) ≥ c·n for all sufficiently large n then h has positive mod-4 switch density. Equivalently: every h with switch density 0 has ν₂(n) = o(n). If true, the fold adds nothing beyond switch density and SUPPLY is equivalent to it. Rival of R-k-functional-input: at most one can be settled true.
off: primes-input
stance: open
merge: This rung is the honest negative close if settled (GOAL.md priority 3). If instead a counterexample h is found — switch density 0 yet ν₂(n) ≥ c·n — that settles R-k-functional-input positively, and merging means naming the functional F and the weak input from that witness, then turning `primes-input` back on. Note: the REOPENED witness does NOT settle this — it shows a K>1 functional exists, not that it beats switch density.
```

```rung
id: R-full-supply
statement: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n — the full SUPPLY conjecture, no difficulty switched off.
off:
stance: open
merge: Nothing left to switch off. If every previous rung merges back, this rung is reached and the ladder is exhausted. Expected last bite: `primes-input` (the parity barrier), reached through `submask-read` and a functional that beats `k1-collapse`.
```
