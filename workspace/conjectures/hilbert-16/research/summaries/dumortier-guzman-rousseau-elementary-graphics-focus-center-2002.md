# Dumortier, Guzmán, Rousseau — "Finite cyclicity of elementary graphics surrounding a focus or center in quadratic systems"

<!-- source: http://www.dms.umontreal.ca/~rousseac/DGR.pdf | Qual. Theory Dyn. Syst. 3 (2002) 123–154 -->
Full text: `research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`

## What this is

Part of the DRR program. Reduces [in [3], i.e. DRR 1994] H(2)<∞ to finite
cyclicity of 121 graphics; this paper nearly finishes the **elementary
graphics** part of the program, proving finite cyclicity for specific
hemicycles and graphics surrounding a focus/center in the DRR notation [3].

## The claimed results (each with its hypothesis)

- **Theorem 3.1/3.2**: (H³₄) and (H³₅) have cyclicity ≤ 2 — irrational (3.1)
  and rational (3.2) hyperbolic-saddle ratios at infinity respectively.
- **Theorem 3.3**: (H³₆) has cyclicity ≤ 2 if r(0) ≠ 1, ≤ 3 if r(0) = 1.
- **Theorem 4.1**: (I²₂₇) has cyclicity ≤ 2.
- **Theorem 5.1**: (I²₁₄a) and (I²₁₅a) have finite cyclicity; Lemma 5.2:
  (R(x))^r is not an affine map and has a nonvanishing higher derivative.
- **Theorem 5.3**: (I²₁₅b) has cyclicity ≤ 2.
- Generic machinery: **Theorems 2.1/2.2** give finite-cyclicity criteria for a
  hemicycle graphic Γ with two opposite hyperbolic saddles P1,P2 (irrational,
  resp. rational ratios with r1·r2 ≡ 1), one attracting and one repelling
  saddle-node P3,P4 on the equator, both connections central. C^k integrable
  normal forms near each singular point; transition maps on transversal
  sections.

## Why it is in the library and what it establishes for THIS run

This is a primary text on the **elementary** DRR graphics — the class that the
Shan 2013 Table 1.1 ledger reports as "nearly all done, only (I6a) elementary
non-hyperbolic open." It supplies the exact hypotheses and cyclicity bounds for
seven named graphics and the normal-form/transition-map method behind them.
It lets a later pass verify (rather than report) the elementary-graphics
closures: the (H³₄),(H³₅),(H³₆) and I²-family rows now have a held primary
source with explicit cyclicity bounds and the r(0)=1 special case.

## Bound to record

Cyclicity bounds here are explicit small integers (2 or 3), not existential —
these are among the few DRR rows where an exact number is proved, matching the
run's preference for statements Lean can carry.

## Caveats / what it does NOT do

- Only elementary graphics; nilpotent and degenerate (triple-point, line-of-
  zeros) graphics — the run's current open targets ((H³₁₄), (I⁶b¹), (H¹³₃),
  (DI₂b), the 11 degenerate) — are outside its scope.
- Terminology: "graphics surrounding a focus or center." Does not settle the
  121-vs-125 discrepancy.
- The 1994 list [3] is cited by DRR notation; the primary DRR 1994 list still
  not held.
