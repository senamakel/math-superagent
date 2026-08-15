# Bhat–Cobeli–Zaharescu 2023, quasi-periodicity in Proth–Gilbreath triangles

**Full text:** `[[bhat-cobeli-zaharescu-quasi-periodicity-html.full]]` (arXiv:2307.11776v1, 19 Jul 2023; Bull. Math. Soc. Sci. Math. Roumaine 67(115)(2024) 3–21). Read in full this cycle because the Directive-58 dyadic-periodicity thread touches exactly this territory.

## What the source establishes (fixed-point classification of the halved operator)

Works on the **halved/binary** Proth–Gilbreath operator, where |a−b| = a+b
over F2 (their Eq. (6), φ(Ψ(α)) = ((1+X)φ(α)−α0)/X — the Pascal/rule-90
addition, the same system as this run's rule90-interior-xor). Defines a
quotient ≍ where rows are equivalent if they coincide after removing finite
prefixes, and studies the fixed points of the induced operator Ψ̂.

- **Theorem 2**: a binary row α is ultimately replicated identically in the
  next PG line iff its F2 generating function is
  φ(α) = P(X)/(1+X+X^r)  or  P(X)/(X^r(1+X)+1),  r≥0, P∈F2[X].
- **Theorem 5**: α is ultimately identical with Ψ(α) (a fixed class of Ψ̂) iff
  φ(α) = G(X)/(1−X^{2^d−1}). The denominator 2^d−1 is Fermat/Mersenne-shaped
  because the recurrence's roots satisfy η^{2^d−1}=1 (Lemma 2: f_r(X)=X^r+X+1
  has distinct roots; the smallest extension containing them has |K^×|=2^d−1).
- **Lemma 3 / Theorem 6** (leap fixed points): α repeats in the l-th following
  row iff φ(α)=P_l(X)/((1+X)^l+X^r) or P_l(X)/(X^r(1+X)^l+1). Theorem 4: if a
  series repeats with periods l_1..l_m then it repeats with period gcd(l_i).
- **Proposition 1**: Fibonacci rows (mod 2) give left edge 1,1,0,1,1,0,…;
  the powers-of-two row (1,2,4,8,…) gives an all-ones left edge.
- **Theorem 1** (Bhat): an infinite subsequence of square-primes generates a
  triangle whose left edge is 1 at every other position.
- **Table 1** (empirical): on the first 50,000 primes, along the first five
  rays parallel to the left edge, #0 ≈ #2 (mod 4), |z−t| < √N in all five
  cases — corroborates this run's mod-4/ν2 ≈ n/2 concentration, but is
  empirical, not a theorem.

## What it does NOT establish (important — don't over-read)

- It classifies **rows that repeat under PG** (fixed classes). It is NOT a
  statement that "an eventually periodic *input* collapses." A periodic input
  need not be a PG fixed class — BCZ's own example T=(0,1,1,1,0,...) has
  φ=X(1+X+X²)/(1+X⁴), is periodic, is NOT fixed (its triangle dies to zeros).
  So do NOT cite BCZ Thm 5 as the collapse mechanism for the dyadic dichotomy.

## Hypotheses and holds-here

Binary rows, F2 coefficients, the operator = |a−b| = a+b mod 2. This is exactly
the halved {0,1} part of the prime triangle's entries (all even / 2), so the
correspondence holds here for that subsystem. It is structure theory of the
binary regime; it does NOT settle GC (the boundary/intruder regeneration is
integer, not binary).

## Bearing on this run

- **Collapse side of Directive 58** is rule90-interior-xor (proved), not BCZ
  Thm 5. BCZ's value here is the *fixed-point classification* if a future
  invariant targets row-repetition in the halved triangle.
- The empirical 0≈2 ray statistic corroborates the mod-4 / ν2≈n/2 concentration
  but is not a theorem about the conjecture.
- Does not help the growth side (odd-factor periods) of the dichotomy at all.

## Stored
- `pg-theorem5-periodic-iff-fixed-class` claim replaced by the corrected
  `rule90-periodic-window-collapse` in `research/notes/scholar-dyadic-periodicity-collapse.md`.
- `pg-fixed-points-rational-form`, `pg-fibonacci-powers-of-two` claims
  (already held) are the accurate record of what this source proves.
