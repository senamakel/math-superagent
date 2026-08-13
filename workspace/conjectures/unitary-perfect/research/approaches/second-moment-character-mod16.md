# Second-moment character method for divisor equidistribution mod 16

```approach
idea: Reduce Conjecture 29 (the *proportional* statement #{r | Φ_{4p}(2) :
  r ≡ 1 mod 16} ≥ c·ω(Φ_{4p}(2))) to a second-moment (variance) bound on a
  multiplicative character sum over the primitive divisors, using Dirichlet
  character orthogonality on (Z/16Z)^* for the count and quartic reciprocity in
  Z[i] for the exact evaluation of the first moments.
mechanism: Orthogonality of the eight Dirichlet characters mod 16 gives
  #{r | Φ : r ≡ 1 (mod 16)} = (1/8) Σ_χ Σ_{r | Φ_{4p}(2)} χ(r). The principal
  character contributes ω(Φ)/8, so Conjecture 29 is exactly the statement that
  the nontrivial character sums S_χ := Σ_{r | Φ} χ(r) are not too negative: one
  needs (1/8)(ω + Σ_{χ≠1} S_χ) ≥ c·ω. The first moment is *exact*: for χ of
  order 4 (the quartic character), the generator argument in the adopted file
  gives χ(r) = (2/r)_4 = 1 ⟺ 4 | (r−1)/4p ⟺ r ≡ 1 mod 16p, so S_χ counts
  {r ≡ 1 mod 16p} minus {r ≡ 9 mod 16p}, and each term is computable from the
  Gaussian factorization 2^{2p}+1 = (2^p+i)(2^p−i). The new step is the *second
  moment*: since the primitive divisors of Φ_{4p}(2) are distinct primes
  (squarefree part), r ≠ r' are coprime, and Parseval/orthogonality gives
  Σ_χ |S_χ|² = 8·#{ordered pairs r,r' ≡ same class mod 16}. Bounding this
  variance from above (or the covariance via the Aurifeuillean split
  L_p·M_p = 2^{2p}+1 and the multiplicative structure) yields, by
  Cauchy–Schwarz / Paley–Zygmund, a lower bound on the mass in the class
  r ≡ 1 mod 16 — i.e. a positive proportion, which is the *proportional*
  Conjecture 29, not the mere existence the adopted quartic approach aimed at.
  This fixes the adopted approach's M1 flaw (existence vs proportionality) by
  construction, and works with the one-way implication only, avoiding its M2
  flaw. Named machinery: Dirichlet character orthogonality, the second-moment
  method, and quartic reciprocity for the explicit first moments.
status: proposed
first-step: For p = 3, 5, 7, 11, 13, 17, compute the full multiset of primitive
  prime divisors of Φ_{4p}(2) and tabulate, for each of the four non-trivial
  classes r mod 16 ∈ {1,5,9,13}, the counts and the character sums S_χ. Verify
  the orthogonality identity exactly, and measure the empirical variance
  Σ_χ|S_χ|² against the "unbiased" value ω(Φ). This establishes whether the
  divisors are already equidistributed mod 16 (variance ≈ ω) on the small cases,
  which is the hypothesis the second-moment bound must capture.
```

## Notes for the research check

- **Distinct from the adopted `biquadratic-character-divisors`**: the adopted
  file aims at *existence* of one r ≡ 1 mod 16 (a (H1)-type statement, strictly
  weaker than C29) via quartic reciprocity alone, and carries the M1/M2/M3
  mismatches documented in
  `research/notes/divisor-level-target-extraction.md` §7. This proposal's
  mechanism is *orthogonality + second moment*, and its deliverable is the
  *proportional* lower bound C29. The quartic character appears only as the
  explicit evaluation of the first moment, not as the whole method.
- **Falsifier**: if the divisors of Φ_{4p}(2) are *not* equidistributed mod 16 —
  i.e. the empirical variance shows systematic bias into the class r ≡ 9 mod 16
  (which would be a genuine conspiracy, since 9 ≡ 1 mod 8 so quartic characters
  cannot separate 1 from 9) — then C29 is false and this route dies with a
  located counterexample, which is itself a result.
- **Cost**: small; only the small-p divisor tables are needed to falsify/confirm
  the equidistribution premise.
- Speculative level: high — the variance of a multiplicative character over the
  prime support of a *single* integer is not standard, and it is not yet clear
  the Aurifeuillean split gives the needed covariance control.
