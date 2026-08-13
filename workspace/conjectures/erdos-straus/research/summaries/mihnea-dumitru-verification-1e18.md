# Mihnea & Dumitru, "Further verification and empirical evidence for the Erdős–Straus conjecture"

Source: arXiv:2509.00128 (submitted 29 Aug 2025), HTML: https://arxiv.org/html/2509.00128v1
Full text: `research/sources/mihnea-dumitru-verification-1e18.full.md`

## What it establishes (sourced, primary)

- **Verification bound raised from `10^17` to `10^18`**: extends Salez's
  modular-filter approach with the extra filter `S_29`, producing a set `R_8` of
  2,101,514 residue classes modulo `G_8 = 25,878,772,920` that must be checked.
  The check is over batches `B_k = {r + k·G_8 : r ∈ R_8}`, k up to 38,641,709.
  Any integer escaping the filters was saved and none was prime, so the residual
  non-prime candidates are handled by the prime reduction.
  Ran ~2 weeks on a medium setup, Python for residue generation (arbitrary
  precision), GMP-backed C++ for the remaining checks.
  This resolves the `[MiDu25]` citation flagged as unverified in erdosproblems
  #242: the 10^18 bound is real and this is its source.
- **Solution counting on the six open classes**: for the 66,737 primes
  `p ≡ r (mod 840)`, `r ∈ {1,121,169,289,361,529}`, up to `p ≤ 3.5×10^7`,
  evaluated f(p) via Bradford's conditions (divisor d | x², one of two
  identities for Type-1/Type-2 relative to x). Of ~29.86×10^12 divisor checks,
  18,601,583 produced a valid solution: 12,763,383 Type-1, 5,838,200 Type-2.
  Empirically f(p) appears increasing, consistent with Elsholtz–Tao's
  polylogarithmic upper bound, and Type-1 solutions are ~2.2× more common than
  Type-2 for these primes.
- Confirms: prime reduction, the six-residue residual set, Salez as the best
  prior sieve. Cites Bradford [3] (Elemental Patterns, 2024) as the framework
  for divisor-based counting.

```claim
id: verification-1e18
statement: The Erdős–Straus conjecture holds for all n up to 10^18 (Mihnea–Dumitru 2025, extending Salez's modular-filter method with the S_29 filter).
hypotheses: none (computational verification).
holds-here: true — this is the current best verification bound; the previous 10^17 (Salez 2014) and 10^14 (Swett 1999) are subsumed.
status: sourced (arXiv:2509.00128; computational, not a proof).
bearing: any family must be checked against n up to 10^18 before a "new" claim; the run should not try to beat this bound computationally.
anchor: research/sources/mihnea-dumitru-verification-1e18.full.md
```

```claim
id: bradford-divisor-counting-open-classes
statement: For the 66,737 primes p ≡ r (mod 840) with r in {1,121,169,289,361,529} and p ≤ 3.5×10^7, every p has a solution, and f(p) grows with p; Type-1 solutions are about 2.2 times more numerous than Type-2.
hypotheses: primes in the six open classes, p ≤ 3.5×10^7.
holds-here: true — direct evidence the open classes are solvable pointwise, even though no polynomial identity covers them.
status: sourced (Mihnea–Dumitru 2025, empirical computation).
bearing: the open classes have abundant solutions; the obstruction is to covering the whole class by one polynomial identity, not to producing per-n solutions.
anchor: research/sources/mihnea-dumitru-verification-1e18.full.md
```