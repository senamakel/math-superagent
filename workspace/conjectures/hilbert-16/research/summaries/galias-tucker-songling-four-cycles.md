# Galias–Tucker, "The Songling system has exactly four limit cycles"

<!-- source: http://www.zet.agh.edu.pl/~galias/ps/amc2022.pdf | Appl. Math. Comput. 415 (2022) 126691, open access CC BY -->

**Shi Songling's H(2)≥4 example, certified.** This paper proves by rigorous
interval arithmetic that the quadratic Songling system

```
ẋ = λx − y − 10x² + (5+δ)xy + y²
ẏ = x + x² + (−25 + 8ε − 9δ)xy
```

with the extreme parameter scales δ ≈ −10⁻¹³, ε ≈ −10⁻⁵², λ ≈ −10⁻²⁰⁰, has
**exactly four limit cycles**.

## What it establishes

- **Theorem 1**: the Songling system has exactly four limit cycles (not merely
  ≥ 4).
- Method: adaptive-precision interval arithmetic. The four limit cycles live at
  wildly different scales (y ≈ 0.0427, 6.7·10⁻⁸, 2.2·10⁻²¹, 7.1·10⁻⁷⁵), so a
  fixed-precision integration cannot separate them. Galias–Tucker localize each
  via a Poincaré (P-)map, prove each interval contains a single fixed point of P
  (Lems 2–3, 6, 8), and prove absence of further fixed points on the remaining
  chunks (Lems 4, 5, 7, 9, 10).
- Gives explicit positional bounds for all four limit cycles, with the P-map
  derivative bounds showing stability (P′ < 1 stable, P′ > 1 unstable).

## Implication for this problem

**H(2) ≥ 4 is now certified in this library**, not merely asserted-by-source.
The exact configuration and the extreme separation of scales are explicit. This
is the model oracle for GOAL.md's "certified limit-cycle counter": a
trapping/return-map argument with an interval-arithmetic sign-change verdict.
The extreme scale separation is precisely why numerics without certificates fail
here — a lesson for this run's own oracle (adaptive precision is essential).

**Evidence class**: verified-computationally (rigorous, reflexive, interval).
**Falsifier**: a defect in one interval-arithmetic branch or a corrected count.
**Holds-here**: yes — confirms H(2) ≥ 4 with more strength (exactly four) than
the historical lower bound.

Claims ledger: `h16-four-cycles-songling-galias-tucker`.
