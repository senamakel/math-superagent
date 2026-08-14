# MathWorld — Visible Point

Source: https://mathworld.wolfram.com/VisiblePoint.html — full text at
`research/sources/mathworld-visible-point.full.md`
[[mathworld-visible-point.full]]

## What this source establishes

**Visibility criterion.** Two lattice points (x,y) and (x′,y′) are mutually
visible iff the segment joining them contains no further lattice points; this
holds iff gcd(x′−x, y′−y) = 1. For a point seen from the origin, visibility
from the origin iff gcd(x,y) = 1. Consequently a point with gcd(x,y) = g > 1
is hidden: (x/g, y/g) is a strictly closer lattice point on the same ray.

**Density.** The probability that a random lattice point is visible from the
origin is 6/π² (in 2 dimensions), equal to the probability that two random
integers are coprime; in n dimensions it is 1/ζ(n).

## Hypotheses

Integer lattice Z² (transferable to the triangular/hexagonal lattice, which is
a rank-2 lattice). Holds here.

## What it lets this run do

- The geometric-to-arithmetic bridge: "hidden from the centre" in the
  hexagonal orchard (PE 351) = gcd(a,b) > 1 in axial coordinates; the six
  sectors each contribute C(n+1,2) − Φ(n) hidden points, giving
  H(n) = 6·(C(n+1,2) − Φ(n)).
- The 6/π² density is the sanity anchor Φ(10⁸)/10¹⁶ = 0.303964 ≈ 3/π².

## What it does not settle

- No counting formula for a bounded hexagon (that is the run's derivation,
  verified by brute force, and A216453).

## Claims

```claim
id: coprimality-iff-visible
statement: A lattice point (x,y) is visible from the origin iff gcd(x,y) = 1;
a point is hidden iff its coordinates have gcd > 1, since then (x/g,y/g) is a
strictly closer lattice point on the same ray.
hypotheses: integer lattice Z^2, origin excluded.
holds-here: yes — the hexagonal lattice is a rank-2 lattice; brute.py's literal
hidden-point scan (no gcd) agrees with the gcd count for n ≤ 8.
status: checked — brute.py's literal hidden-point scan (no gcd, no number
theory) agrees with the gcd count for every n ≤ 8 and with H(5), H(10),
H(1000); general criterion sourced from MathWorld VisiblePoint.
bearing: reduces the geometric count to the totient identity
H(n) = 6(C(n+1,2) − Φ(n)).
anchor: research/summaries/mathworld-visible-point.md
```
