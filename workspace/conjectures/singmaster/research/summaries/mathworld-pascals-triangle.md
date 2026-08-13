# MathWorld — Pascal's Triangle (encyclopedic tier)

Source: https://mathworld.wolfram.com/PascalsTriangle.html (Wolfram MathWorld, Stover & Weisstein).

Encyclopedic entry on Pascal's triangle. Fixes the statement, the history
(Tartaglia 1556, Pascal 1665, Yang Hui/Khayyam), the construction identity
`(n;r)=(n-1;r)+(n-1;r-1)`, and the standard figure-number/Fibonacci/shallow-diagonal
properties. Cited by three of this library's own sources (FRONTIER), so this is the
canonical encyclopedic reference tier and was the gap this cycle closed.

## What it establishes that bears on Singmaster's conjecture

- **The witness set, exactly.** By row 3003, `3003 = (14;6)=(14;8)=(15;5)=(15;10)=(78;2)=(78;76)=(3003;1)=(3003;3002)`, i.e. N(3003)=8 counting both mirrors plus the trivial pair. Confirms the run's witness (independent of Wikipedia).
- **The high-multiplicity catalogue.** The numbers that occur five or more times are
  1, 120, 210, 1540, 3003, 7140, 11628, 24310, ... (OEIS A003015), "with no others up to 33×10¹⁶" — corroborates the run's six N=6 values and the 2^23/2^48 verification bounds. 120, 210 appear six times by row 210; 1540 and 7140 also reach 6.
- **The infinite family, explicitly.** There are infinitely many numbers occurring at least 6 times, the solutions to `r=(n;m-1)=(n-1;m)` given by `m=F_2k-1·F_2k`, `n=F_2k·F_2k+1` (Singmaster 1975). First few r: 1, 3003, 61218182743304701891431482520, ... (OEIS A090162). This matches the run's verified parametrization `n=F_{2j+2}F_{2j+3}-1, k=F_{2j}F_{2j+3}-1` and the ~6.1e28 second member. Independent confirmation from a second encyclopedic source.
- **The O(log a) / conjecture frame.** Cites Singmaster 1971 (AMM 78, 385-386) and references de Weger 1997 (JNT 63, equal binomial coefficients).

## Evidence class

`asserted` by the encyclopedic source; the numerical witness statements (3003,
the N=6 list, the second family member) are consistent with, and independently
corroborate, this run's `checked` computations (witnesses.json, brute.py, the
Fibonacci-family verification). The infinite-family parametrization matches the
run's verified Pell/Fibonacci derivation. No new claim is asserted here that is
not already cross-checked in this workspace.

See also the full text at `research/sources/mathworld-pascals-triangle.full.md`.
