# Bertók–Hajdu / Dimitrov–Howe cross-modulus ladder for the Erdős S-unit equation

```approach
idea: The conjecture is equivalent to the exponential Diophantine equation
  2^n = sum_{a in A} 3^a   (A a finite set of distinct nonneg integers, |A|
  UNBOUNDED) having exactly the three solutions {0}, {0,1}, {0,1,2,5}
  (n = 0, 2, 8). This is the S-unit framing of candidate
  sunit-subspace-level-decomposition -- correct, non-degenerate, rank-2 group
  U_{2,3}. The NEW route is the uniformity mechanism, taken from the library:
  Dimitrov-Howe (2021, Rocky Mountain J. Math) solved the <= 25-ones case not
  by any uniform Subspace bound but by a chain of MIXED moduli
  M_1 | M_2 | ... | M_t, M = 2^u 3^v M' with M' coprime to 6, whose 2/3-cross
  order structure makes every solution mod M_i "determinate" and hence lift
  uniquely. Their Lemma 3.1 states the local criterion for a modulus to carry
  extraneous (non-lifting) solutions. The run's own counting obstruction
  |A_k| = 2^(k-1) is the DEGENERATE instance of that criterion (M = 3^k, so
  M' = 1 and both cross-orders are trivial), and the 2^(k-1) - 3 non-witness
  survivor classes ARE the extraneous solutions. So the sieve cannot close
  because it is pure 3-adic; the route to uniformity is to mix in primes with
  large cross-orders. This is exactly the Bertok-Hajdu conjecture specialized
  to the Erdos equation.
mechanism: (a) candidate 1's non-degeneracy is proved and survives: for every
  digit-2-free power the S-unit equation 2^n - sum_{a in A} 3^a = 0 has no
  vanishing proper sub-sum, so it lies in the class where modular lifting is
  controlled. (b) Dimitrov-Howe Lemma 3.1 (read from the full text, lines
  330-362) gives the local obstruction to lifting: a solution with an
  indeterminate power of 2 or 3 exists mod M whenever the cross-orders O'_3(M),
  O'_2(M) fail a stated divisibility. (c) The counting obstruction |A_k| =
  2^(k-1) is the extreme of that obstruction at M = 3^k (M' = 1 => O'_2 =
  O'_3 = 1); it is no longer an independent mystery -- it is one point in a
  one-parameter family of degeneracies indexed by M'. (d) The full-strength
  statement "a single modulus M lifts uniquely for ALL |A|" is the
  Bertok-Hajdu conjecture specialized here (sourced, DH intro lines 215-230);
  attacking it is attacking the conjecture, but the FIRST rung is provable and
  new: generalise Lemma 3.1 from its 3-term equation 3^y = c + 2^x to the full
  k+1-term equation sum_{a in A} 3^a = 2^n.
status: adopted
precedent:
  - "Dimitrov-Howe 2021 (arXiv:2105.06440v4, Rocky Mountain J. Math) Theorem
     1.2: the only powers of 2 writable as a sum of <= 25 distinct powers of 3
     are 2^0, 2^2, 2^8. Method: elementary nested moduli M_1 | M_2 | ... with
     M = 2^u 3^v M'. [DIMITROV-HOWE-26-ONES]"
  - "Dimitrov-Howe Section 3, Lemma 3.1 (full text lines 330-362): for M = 2^u
     3^v M', if 3^y = c + 2^x (mod M) with x > 2, y > 0, and O'_3(M) is not
     divisible by 2^(x-1) while O'_2(M) is not divisible by 3^y, then there are
     x', y' with 3^(y') = c + 2^(x') (mod M) where 2^(x'), 3^(y') are
     indeterminate powers. Verified here by reading the full text."
  - "Determinate power (DH Def 2.2): p^i is determinate mod M iff M is divisible
     by p^(i+1); the tail-and-loop diagram has v_p(M) tail + O_p(M) loop
     elements. For the sieve M = 3^k: no power of 2 is determinate, and only
     3^0..3^(k-1) are determinate."
  - "Bertok-Hajdu conjecture (cited in DH intro): an exponential Diophantine
     equation with finitely many solutions has an integer M such that solutions
     mod M lift uniquely to the integer solutions. DH explicitly offer their
     work as evidence for it. This is the uniformity statement candidate 1 was
     missing."
  - "Candidate 1's ESS per-level bound (Evertse-Schlickewei-Schmidt 2002,
     Ann. Math 155) is retained only as the finite-support fallback; it gives
     no uniformity in |A|, which is why it is NOT the adopted mechanism."
first-step: tool_builder-ready, three programs in order:
  1. Re-prove |A_k| = 2^(k-1) mechanically (the one-time re-check GOAL.md
     demands): sieve over r mod 2*3^(k-1), work mod 3^k only, never build 2^n
     whole; capture the count for k = 1..26.
  2. Implement the determinacy classifier: given M = 2^u 3^v M' (M' coprime to
     6), list the determinate powers of 2 and 3, compute O'_2(M) = ord of 2 in
     (Z/M'Z)^x and O'_3(M) = ord of 3 in (Z/M'Z)^x. Reproduce DH's two worked
     examples: M1 = 5440 = 2^6*5*17 (extraneous solutions present) and
     M = 2^7*5*17*257 (no extraneous solutions) for the n=3 equation
     3^x = 2^a1 + 2^a2 + 2^a3. **DONE (hand-verified this run, see
     research/summaries/dh-n3-and-cross-modulus-gap.md, claim DH-N3-EXAMPLES-VERIFIED):
     M1 has the three residue-class solutions and (6)'s 2^6 is indeterminate on
     the 8-loop; M2 is clean with 2^0,2^4,2^6 all determinate (tail length 7) and
     ord_257(3)=256 (multiple of 2^5). The enumeration program
     code/out/verify_dh_n3.py is written; the harness should execute it to
     capture the machine confirmation.**
  3. Use the classifier to GENERALISE Lemma 3.1: for the full equation
     sum_{a in A} 3^a = 2^n (mod M), |A| = k, derive the threshold on
     (v_2(O'_3(M)), v_3(O'_2(M))) below which a genuine solution forces an
     extraneous sibling. Target lemma: "M = 3^k is the maximally degenerate
     case, and |A_k| = 2^(k-1) is its extraneous-solution count." Falsification
     gate: the generalisation must reproduce DH's n=3 examples and the sieve
     count before it is trusted for anything else.

## Literature status of the unbounded case (research pass, this run)

- **Grounded:** the DH method itself, its Definitions/Notation (2.2, 2.3) and Lemma 3.1
  are verified this run (exact statements with line numbers and the two n=3 examples
  reproduced; see `DH-STATEMENTS-EXACT`, `DH-N3-EXAMPLES-VERIFIED`).
- **Open with no precedent (`CROSS-MODULUS-UNBOUNDED-OPEN`):** no published paper applies the
  mixed-modulus / cross-order ladder, or the Bertók–Hajdu / Skolem lifting conjecture, to the
  unbounded-|A| case of `2^x = Σ_{a∈A} 3^a`. No result mixes primes other than 3 into the
  modulus to push `|A_k|` below `2^(k-1)`. The >25-ones case is exactly the residual open
  case of Erdős, so extending the ladder there would be new. Source audits: Lagarias 2009,
  Saye 2022, Li–Zhao 2026, Roettger–Ren 2025, Bertók–Hajdu 2015 (Hasse-type/Skolem), and DH
  themselves.
- **The route is therefore a genuine partial-result candidate, not a re-derivation:** the
  first rung (k+1-term generalisation of Lemma 3.1 with the same threshold structure,
  `CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES` H2) is not in the published literature as far as
  this run can establish. Its falsification gate is stated: it must reproduce the DH n=3
  examples and the sieve count, and a mixed modulus must actually drive the survivor count
  below `2^(k-1)`.
```

## Why this beats the other two candidates and the original form of candidate 1

- **Candidate 1 (uniform S-unit / Subspace):** correct framing, but its uniformity
  step has **no precedent** and is exactly the conjecture; the dual problem
  `s_2(3^n)` unbounded was settled by Baker-type linear-forms-in-logarithms
  (Stewart 1980), *not* by a uniform Subspace bound. Retained only as the
  non-degeneracy and finite-support backbone. The adopted line replaces its dead
  uniformity step with a mechanism that the library shows actually works in the
  sparse regime.
- **Candidate 2 (run/Zsigmondy):** refuted — the valuation identity is vacuous
  (holds for every integer, never uses the digit hypothesis) and the `n=8`
  decomposition was miscomputed. Nothing survives.
- **Candidate 3 (rotation/CF):** refuted — "n is a convergent denominator" is
  necessary-but-insufficient (denominators 1,3,19,… all fail), and the cited
  metric theory is average/measure, never pointwise.

The adopted line is the only one that (a) keeps a proved structural fact
(non-degeneracy of the S-unit equation), (b) names a mechanism for the
uniformity-in-k gap rather than asserting it, and (c) absorbs the run's central
obstruction `|A_k| = 2^(k-1)` as a *corollary* of a known lemma instead of leaving
it as an unexplained wall.

## Honest statement of what is and is not established

- **Non-degeneracy** of the equation for every digit-2-free power: *proved* (this
  run, hand; see `research/candidate-precedent-handcheck.md`,
  `CAND1-NONDEGENERATE-PROVED`).
- **ESS per-level finiteness**: *sourced* (asserted by source, bound quoted not
  re-derived).
- **DH Lemma 3.1 and the determinate-power definition**: *sourced*, read from the
  held full text (lines 330–362, 294–306).
- **Bertók–Hajdu conjecture**: *sourced* (cited in DH introduction, lines 215–230).
- **"M = 3^k is the degenerate instance; `|A_k| = 2^{k-1}` counts extraneous
  solutions"**: *derived here, unverified* — this is the claim the first-step
  programs are built to check. It is elementary (M′ = 1 ⇒ `O′₂ = O′₃ = 1` is a
  trivial ring fact) but the *connection* to the sieve count is the load-bearing
  step and must be machine-checked before anything is built on it.
- **Full-strength "one modulus lifts uniquely for all |A|"**: *conjectured*
  (Bertók–Hajdu specialized); attacking it directly is attacking Erdős.
