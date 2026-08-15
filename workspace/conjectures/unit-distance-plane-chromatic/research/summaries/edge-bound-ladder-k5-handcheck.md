# Hand-check of the k=5 critical-edge-count ladder arithmetic

This note records a **paper-and-pencil rational simplification** of the
edge-count formulae in `research/sources/` (Dirac 1957, Gallai 1963,
Krivelevich 1997, Kostochka–Yancey 2014). It is NOT a machine run: the
scholar environment this session has no exec tool. The script
`code/scholar_check_edge_bounds.py` reproduces the same arithmetic exactly
and awaits an executor to produce captured output (`code/out/`).

The purpose is to confirm that the numeric coefficients repeated across the
size-bound direction (the edge-count clash with the unit-distance ceiling) are
the correct specialisation of each source's formula for k = 5. All are pure
rational algebra directly from the stated formulae.

## Dirac 1957
Statement: `|E(G)| >= (1/2)((k-1)n + k - 3)` for k-colour-critical graphs,
n >= k+2.
k=5: `(1/2)(4n + 2) = 2n + 1`. Note says `2n+1` — **consistent.**

## Gallai 1963
Statement: `|E| >= ((k-1)/2 + (k-3)/(2(k^2-3)))·n`.
k=5: `2 + 2/(2·22) = 2 + 1/22 = 45/22 ≈ 2.045` edges/vertex (avg degree 4.091).
Note says `2 + 2/(2·22)=2.045` — **consistent.**

## Krivelevich 1997
Statement: `|E| >= ((k-1)/2 + (k-3)/(2(k^2-2k-1)))·n`.
k=5: `2 + 2/(2·14) = 2 + 1/14 = 29/14 ≈ 2.0714` edges/vertex, avg degree
`58/14 = 29/7 ≈ 4.143`. Note says `2 + 1/14 ≈ 2.0714`, avg `≈ 4.143` —
**consistent.** (KY strictly sharper.)

## Kostochka–Yancey 2014
Statement: `f_k(n) >= F(k,n) = ((k+1)(k-2)n - k(k-3))/(2(k-1))`, k>=4, n>=k,
n != k+1.
k=5: `(6·3n - 5·2)/(2·4) = (18n-10)/8 = (9n-5)/4 ≈ 2.25n`.
Note says `f_5(n) >= (9n-5)/4` — **consistent.**

## The n=9..10 clash (recorded in the discharging approach as a dead end)
`(9n-5)/4 <= C·n^{4/3}` with the impossible constant C=1:
- n=8: (72-5)/4 = 16.75 vs 8^(4/3)=16 -> KY>SST
- n=9: (81-5)/4 = 19   vs 9^(4/3)≈18.72 -> KY>SST
- n=10: (90-5)/4 = 21.25 vs 10^(4/3)≈21.54 -> SST>KY (clash stops)
So the clash first stops between n=9 and n=10 — consistent with the approach
note ("fails to force a contradiction past n=9").

## Status
These are simplifications of formulae *stated by the cited sources*. The
theorems themselves remain `asserted-by-source` (general graph theory, not
re-derived); what is hand-checked here is only that the k=5 specialisations
used in the size-bound clash match each source's formula. A machine run of
`code/scholar_check_edge_bounds.py` (exact fractions) should be captured to
upgrade this from hand-check to `checked`.
