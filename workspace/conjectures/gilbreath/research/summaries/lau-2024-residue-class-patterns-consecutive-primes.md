# Lau 2024, "Residue class patterns of consecutive primes" (arXiv:2409.12819)

<!-- source: https://arxiv.org/abs/2409.12819 | full text at research/sources/lau-2024-residue-class-patterns-consecutive-primes.full.md -->

## What it establishes

- **The gap between conjecture and proof.** Dickson's / Hardy–Littlewood
  predict every reduced residue pattern mod q occurs infinitely often, but
  even a **single non-constant** m-term pattern occurring infinitely often is
  beyond present methods (abstract).
- **Unconditional (Dirichlet + Shiu 2000):** for any m,q ∈ ℕ, q ≥ 3, at least
  mφ(q) residue patterns of length m are attained by infinitely many
  consecutive primes.
- **Main theorems (via Banks–Freiberg–Maynard r-th moment Maynard–Tao sieve +
  Erdős–Rankin).** If q is squarefree: every prescribed sequence of at least
  60m·log m reduced residues mod q contains, in order, an m-term block pattern
  occurring infinitely often, each constant block of length ≤ ⌈log m⌉.
  Recursively, if q ≫ (log m)² then at least ≫ m/(log m)^10 · φ(q)², and
  ≫ e^{−O(m log₂m/log m)} φ(q)^{m/⌈log m⌉}, patterns occur infinitely often.

## What it does NOT say

The results are **existence/counting of distinct patterns**, never a
**frequency** lower bound on how often a given prescribed pattern (e.g. the
mod-4 switch (1,3) or (3,1)) occurs. "At least mφ(q) patterns are attained" is
about the number of distinct patterns, not the density of n where a specified
switch happens.

## Consequence for this run (Route B ν_2 supply)

The atomic bit feeding Granville's ν_2, [p_{n+1} ≢ p_n mod 4], is exactly the
kind of two-point consecutive-pair object Lau studies. Lau confirms that a
one-sided **frequency** forcing at the consecutive-pair level is NOT available
from unconditional sieve/analytic number theory; it remains at Hardy–Littlewood
/ Lemke Oliver–Soundararajan conjecture level. Consistent with the adopted
`chebyshev-bias-granville-nu2-supply` approach's conclusion (two-point) and
with `gap-bounds-cannot-force-block-growth`.

```claim
id: lau-2024-consecutive-residue-patterns-existence-only
statement: No single non-constant consecutive-prime residue pattern is known to occur infinitely often; unconditionally at least mφ(q) length-m patterns occur infinitely often, and for squarefree q ≫ (log m)² at least ≫ m/(log m)^10 · φ(q)² patterns occur—but always counting distinct patterns, never a frequency lower bound on a prescribed pattern.
hypotheses: primes; q squarefree for the quantitative theorems; Dirichlet+Shiu for the mφ(q) bound.
holds-here: yes (primes; the mod-4 two-point consecutive-pair statistic)
status: proved (for what it asserts)
bearing: caps Route B's ν_2 supply frequency at conjecture level; confirms no unconditional one-sided forcing of the mod-4 switch.
anchor: research/sources/lau-2024-residue-class-patterns-consecutive-primes.full.md
answers: supply-frequency-vs-existence
```

## Added note: the "Lau 2026 v2" timestamp

The arXiv listing shows the abstract revised 13 Jul 2026 (v2); the underlying
theorems are as of the 2024 submission. The run verifies claims against the
full text, so the v2 revision does not change the above.
