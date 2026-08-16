# SUPPLY — the ladder of weakened targets

One ladder for the SUPPLY conjecture. Weakest rung first; each rung is the goal
with named difficulties switched off. The bottom rungs anchor the two branches:
the finite-numerical branch (real primes, small n) and the generic-model branch
(random h, the fold in isolation). They meet at the submask rungs and climb to
the full conjecture through the primes-on rungs.

```ladder
goal: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n, where ν₂(n) = wt(Φ_n h) over F₂, h[j] = ((q_{j+1} − q_j)/2) mod 2, and Φ_n is the Pascal-mod-2 fold of problem.md.
difficulties: primes-input, pointwise-all-n, unconditional-effective, fold-collapse, submask-read
status: open
```

- `primes-input` — the real h is the prime gap-parity string; unconditional
  control of it is the parity barrier (positive mod-4 switch density is open,
  ABGS 2011 §9).
- `pointwise-all-n` — ν₂(n) ≥ c·n must hold for every n past one threshold, not
  merely on a density-1 set, in expectation, or a.s. for a random input.
- `unconditional-effective` — c > 0 must be explicit and effective, and the
  proof may use no unproved arithmetic input (Shiu 2000 is held conditionally).
- `fold-collapse` — Φ has low-weight images on structurally rich inputs, so no
  hypothesis of the form "h is complicated enough" can work (the five closed
  doors in problem.md).
- `submask-read` — Lucas confines Φ_n to reading h only along binary-submask
  XORs ⟨h, χ_S⟩; usable input must concern those specific linear forms, not
  global complexity.

```rung
id: R-finite-verified
statement: For the real prime string h (floor convention at index 2), ν₂(n)/n ≥ 0.42 for every n with 275 ≤ n ≤ 4000, and the full exceptional set {n ≤ 4000 : ν₂(n)/n < 0.42} is {53, 56, 62, 71, 103, 105, 145, 153, 210, 274}, deepest ν₂(53)/53 = 0.3585. Numerical evidence, not a theorem. (The earlier reading "ν₂/n ≥ 0.42 for every 50 ≤ n ≤ 4000" is FALSE — those 10 dips violate it.)
off: pointwise-all-n
stance: settled
merge: Turn `pointwise-all-n` back on: extend the range past 4000. First move is R-averaged-supply (density-1 set), the first primes-on statement beyond the finite prefix; a bare computation cannot reach a proof and this rung is the oracle anchor, not a stepping stone. Settled by dip-boundary-effect-small-n and dip-sparsity-to-20000; the contradiction claim r-finite-verified-contradicted records the correction to the range.
```

```rung
id: R-random-expectation
statement: For h uniform on the domain of Φ_n, with rank Φ_n = n−2 (corrected; full row rank of the operative (n−2)×n matrix, rows d=2..n−1 — see fold-rank-is-n-2-nullity-2-alternating), E_h[wt(Φ_n h)] = (n−2)/2 ≥ n/3 for all n ≥ 6. The fold imposes no weight obstruction on generic input; a linear lower bound is the generic behaviour.
off: primes-input, pointwise-all-n, unconditional-effective
stance: settled
merge: Turn `pointwise-all-n` back on: promote the expectation to concentration around (n−2)/2. First move is R-random-pointwise. Caveat (checked): concentration does not follow from "uniform on a rank-(n−2) subspace" alone — a rank-2 subspace span{e_1, (0,1,…,1)} has E[wt] = n/2 but only half its vectors of weight ≥ n/4 — so the argument must use Φ_n's Lucas/submask structure, which is precisely R-random-pointwise's content.
```

```rung
id: R-random-pointwise
statement: For h uniform on the domain of Φ_n, wt(Φ_n h) ≥ n/4 holds with probability 1 − exp(−Ω(n)); in particular for all but an exponentially small fraction of h. The fold's weight is linear on random input, not merely in expectation.
off: primes-input, unconditional-effective
stance: open
merge: Settle by the concentration argument named above, which must use Φ_n-specific structure (Lucas), not the bare rank. Turn `primes-input` back on: replace "h random" with a deterministic condition C(h) phrased only in the submask-XOR coordinates ⟨h, χ_S⟩. First move — enumerate which submask-XOR patterns force a positive density of odd depths from the Lucas row structure, and check C(h) is not implied by any closed-door hypothesis (all-ones, Thue–Morse, balanced anti-dyadic strings are the negative controls). That is R-submask-sufficiency.
```

```rung
id: R-submask-sufficiency
statement: There exists a condition C(h), stated entirely in the submask-XOR coordinates that Lucas makes Φ_n read, strictly weaker than positive mod-4 switch density, such that C(h) implies ν₂(n) = wt(Φ_n h) ≥ c·n for all sufficiently large n. Concretely: some binary string h with switch density 0 (gaps ≡ 2 mod 4 of density 0) still has ν₂(n) ≥ c·n.
off: primes-input
stance: open
merge: Turn `primes-input` back on: now h is the real prime gap-parity string, so C(h) must be a provable property of the primes. First move — price which arithmetic input (bounded autocorrelation of h, a second-moment or Walsh-coefficient bound, or an input along submask sets) implies C(h). If the only answer is "positive switch density itself", the honest output is the rival rung R-switch-equivalence (GOAL.md priority 3).
```

```rung
id: R-switch-equivalence
statement: For every binary string h, if ν₂(n) ≥ c·n for all sufficiently large n then h has positive mod-4 switch density. Equivalently: every h with switch density 0 has ν₂(n) = o(n). If true, the fold adds nothing beyond switch density and SUPPLY is equivalent to it. Rival of R-submask-sufficiency: at most one can be settled true.
off: primes-input
stance: open
merge: This rung is itself the honest negative close if settled (GOAL.md priority 3). If instead a counterexample h is found — switch density 0 yet ν₂(n) ≥ c·n — that settles the positive rung R-submask-sufficiency, and merging means naming C(h) from that witness and turning `primes-input` back on.
```

```rung
id: R-averaged-supply
statement: There is c > 0 and a set S of natural density 1 such that ν₂(n) ≥ c·n for every n ∈ S, where h is the real prime gap-parity string. The parity barrier is pointwise and is sometimes porous on average.
off: pointwise-all-n
stance: open
merge: Turn `pointwise-all-n` back on: promote the density-1 set S to a cofinite one (all n ≥ N₀). First move — find the structure of the exceptional set; if it is finite or sparse enough to bound, the promotion is free, else name exactly what makes a density-1 set fail to be cofinite. Incomparable with R-conditional-pointwise (this one unconditional-but-averaged, that one conditional-but-pointwise).
```

```rung
id: R-conditional-pointwise
statement: ν₂(n) ≥ c·n for all sufficiently large n, conditional on one named weak arithmetic input about the real prime string h — for instance Shiu 2000 (held abstract in problem.md), or a stated second-moment / Walsh-coefficient bound on h. The goal with `unconditional-effective` switched off: c is explicit, but one arithmetic hypothesis may be assumed.
off: unconditional-effective
stance: open
merge: Turn `unconditional-effective` back on: prove the named input unconditionally or replace it with one that is, else SUPPLY stays conditional and the honest result is "SUPPLY is equivalent to that input". Incomparable with R-averaged-supply, as noted there.
```

```rung
id: R-full-supply
statement: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n — the full SUPPLY conjecture, no difficulty switched off.
off:
stance: open
merge: Nothing left to switch off. If every previous rung merges back, this rung is reached and the ladder is exhausted. Expected last bite: `primes-input` (the parity barrier), reached through `submask-read`.
```
