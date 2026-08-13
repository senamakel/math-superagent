# Survey note — Higgs-origin search and repeated-divisor literature (cycle 7)

## Higgs-origin: nothing to acquire beyond held sources

Fresh English/POLICY searches for a paper by Denis Higgs defining the
"Higgs prime" sequences return only particle-physics noise (Higgs mass from
prime structure, Higgs cohomology, etc.). The term is OEIS A057447's ("3-Higgs
primes", Muljadi 2005 comment) and the sequences are constructed in Burris &
Yeats, *The Saga of the High School Identities*, Algebra Universalis 52 (2004)
325–342 (held: `research/sources/burris-yeats-saga-high-school-identities.full.md`),
which defines `Σ_a` (p₁ = 2, `(p_{i+1}−1) | (p₁⋯p_i)^a`). **Conclusion: the
origin/definition tier is complete; no separate "Higgs 1967 paper" exists to
fetch.** Do not re-search this.

## Repeated-prime-power divisors of cyclotomic values — adjacent computational attack

The run's sharpest witness edge is the repeated odd kernels `3^2` (in 90) and
`5^4` (fifth UPN), and the paper's bounded-box enumeration classifies source
kernels of the odd dependency graph. The classical adjacent item is

- **McDaniel, *On multiple prime divisors of cyclotomic polynomials*, Math.
  Comp. 28 (1974), DOI 10.2307/2005707** — tables all triples (p, n, q),
  q prime < 150, with `p^f | Φ_n(q)`, f > 1, using `a^(p−1) ≡ 1 (mod p^2)`
  tables (Brillhart–Tonascia–Weinberger; Riesel). **Paywalled** (JSTOR); not
  fetched. It concerns *base* `q < 150` cyclotomic *values* `Φ_n(q)`; the run's
  value is `Φ_{4p}(2)` (base 2), whose repeated-divisor behaviour is governed
  by Wieferich-type `2^{p−1} ≡ 1 (mod p^2)` primes. Recorded as context only:
  if the run ever needs a "no repeated odd prime power in Φ_{4p}(2)" lemma
  checked against tables, this is the shape the literature has; the base-2
  case is not tabled there.
- **Moree/Kloosterman et al. (Beiter thread)** — coefficient-side results on
  `Φ_n`, NOT residue classes of prime divisors; already correctly excluded in
  cycle 6. Confirmed again.
- **Primitive prime divisors & the nth cyclotomic polynomial (J. Aust. Math.
  Soc., 2015, DOI 10.1017/S1446788715000269)** — algorithmic determination of
  `Φ*_n(q)`, Hering-correction; group-theoretic application. Not fetched; not
  needed (the run already holds BHV 2001 primitive-divisor machinery and the
  Aurifeuillean split).

## Bearing

Nothing here changes the library's shape: the divisor-level gap the paper names
(residue-class / transference control of prime divisors of a single `Φ_{4p}(2)`)
remains unmatched in the literature, which is exactly why the run's adopted
`second-moment-character-mod16` approach is aimed there. This survey just
confirms the neighbouring classical items are (a) about coefficients, (b) about
small-base repeated divisors, or (c) paywalled — none supplies the missing
divisor-transference theorem.