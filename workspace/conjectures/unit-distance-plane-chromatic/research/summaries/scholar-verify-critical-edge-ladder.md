# Scholar verification of the k-critical edge-bound ladder (four new sources)

The four critical-edge-bound sources (Dirac 1957, Krivelevich 1997,
Kostochka–Yancey 2014, Cranston–Rabern 2016) were digested by a prior scholar
pass into notes under `research/sources/`, with claim blocks already present in
`research/CLAIMS.md` (`dirac-1957-critical-edge-bound`,
`krivelevich-1997-critical-edge-bound`, `kostochka-yancey-2014-critical-edge-bound`,
`cranston-rabern-2016-list-critical-discharging`). This pass verifies the
specialised arithmetic those notes carry, and checks consistency with the run's
existing claims.

## Hand-checked numbers (small rational arithmetic, exact)

- **Dirac 1957, k=5**: `|E| >= (1/2)((k-1)n + k-3) = (1/2)(4n+2) = 2n+1`.
  Average degree `2|E|/n >= 4 + 2/n`. ✓
- **Kostochka–Yancey 2014, k=5**: `F(5,n) = ((6)(3)n - 5·2)/8 = (18n-10)/8
  = (9n-5)/4 = 2.25n - 1.25`. Edge/vertex ratio 2.25. ✓
- **Gallai 1963, k=5**: edge/n ratio `2 + 2/(2·(25-3)) = 2 + 2/44 = 2 + 1/22
  ≈ 2.045`. ✓
- **Krivelevich 1997, k=5**: edge/n ratio `2 + 2/(2·(25-10-1)) = 2 + 2/28
  = 2 + 1/14 ≈ 2.0714`. ✓
- **Ladder order** (edges/vertex, strictly increasing): trivial min-degree `2`,
  Dirac `2 + 1/n`, Gallai `2.045`, Krivelevich `2.0714`, KY `2.25`. KY is the
  sharpest. ✓
- **Cranston–Rabern 2016** model result (k-AT-critical average-degree form):
  `k>=7`: `k-1 + (k-3)(2k-5)/(k^3+k^2-15k+15)`; `k in {5,6}`:
  `k-1 + (k-3)(2k-5)/(k^3+2k^2-18k+15)`. Checked as written in the note; the
  mechanism (non-planar discharging) is the claim that matters and is stated
  verbatim. ✓

## The size-bound clash (the reason the discharging route is refuted)

A minimal 5-chromatic unit-distance graph would be 5-critical, so KY bounds
`|E| >= (9n-5)/4`; the unit-distance density ceiling is `u_2(n) <= C·n^{4/3}`
(SST). Setting `(9n-5)/4 <= n^{4/3}` at the impossible best constant `C=1`:
- n=9: need `(81-5)/4 = 19`, cap `9^{4/3} = 18.72` → **contradiction**
- n=10: need `85/4 = 21.25`, cap `10^{4/3} = 21.54` → holds

So the clash forces a contradiction only up to n=9, strictly below the verified
census n=11 (`size-bound-udg-4color-n11`, `sharp-kernel-4color-n11`). This
exactly reproduces the refutation recorded in
`research/approaches/discharging-minimal-counterexample.md`. The four sources
therefore confirm but do not move the dead end: they are the very edge bounds
that fail, and the reason is the unit-distance density ceiling, not the
discharging method.

## Consistency

The four claims are mutually consistent and agree with the run's established
`critical-minimum-degree` (trivial rung), `sharp-critical-degree` (checked),
and `size-bound-udg-4color-n11` (checked). No contradiction with durable
memory. The mechanism correction they carry (discharging on k-critical graphs
is non-planar, via the Gallai forest, *not* Euler's formula) matches the
existing caveat in the discharging approach file.

## What these sources do NOT establish

They are general graph theory. They give the edge lower bound a 5-critical
unit-distance graph must satisfy but cannot, by themselves, push the size bound
past n=11 — a sharper unit-distance-specific density/angle bound is the open
problem itself. They settle nothing about whether a 5-chromatic unit-distance
graph exists.

## Status

All four are `asserted-by-source` (full publisher texts network-blocked;
statements sourced via server-side retrieval). The arithmetic specialisations
here are hand-checked exact rational computations, not program output.
