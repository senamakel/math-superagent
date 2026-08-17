# Naive oracle — derivation

Statement the oracle bears on: *claimed existence / count of limit cycles in
radially symmetric planar polynomial fields* (exact, rational arithmetic),
which is the self-contained tractable core of H16.2 for this pass
(GOAL.md item 3a). The brute-force objects: a field `X = P∂x + Q∂y`, an
annulus band of radii, and the **displacement function** `D(r)` — return map
minus identity along a ray — restricted to exact solvability.

## Exact structure used (and honest about its limits)

For a field of the form

    x' = A(r²)x − B(r²)y        y' = B(r²)x + A(r²)y

with `A, B ∈ Q[u]`, `u = r²`, polar coordinates give:

    dr/dt = r·A(r²)                     ("radial rate")
    dθ/dt = B(r²)                       ("angular rate")

Over one full revolution (Δθ = 2π), the radial displacement is

    Δr = 2π·r·A(r²)/B(r²)

so the displacement function `D(r)` has the SAME SIGN as `A(r²)` wherever
`B(r²) > 0` on the band. Hence limit cycles correspond exactly to roots of
`A(u)` on `u > 0`; a root where `A` changes sign is a hyperbolic (transversal)
isolated cycle, a double root needs the next term to decide.

Faithful oracle (no float, no integration, no sampling): pass a band
`[U1, U2]` (u-honest), list all roots of `A(u)` in it exactly via exact
square-free factoring (sympy `nroots`/`factor` over QQ), classify each by sign
change of `A`, and give the certified count of hyperbolic limit cycles in the
band. The radicially symmetric family is the exact analogue of the
textbook/graphics normal-form example, and matches the "displacement function =
return map minus identity" frame.

## What the oracle reports honestly

- `is_radial(P, Q)`: is `(xP+yQ)/(x²+y²)`, `(xQ−yP)/(x²+y²)` polynomial in
  `x²+y²`? (exact division). If not, the oracle DOES NOT count — it reports
  `non-radial`, because the displacement-sign argument does not apply. This is
  the oracle's guard set: it checks the hypothesis class before asserting.
- `limit_cycles_in_band(P, Q, u1, u2)`: count of sign-changing roots of
  `A(u)` in the band; declares stable/hyperbolic cycles.
- `verify_all()`: reproduces every worked example (cubic field, linear centre,
  linear no-cycle field) — the guard set the oracle must pass before any
  experiment uses it (AGENTS.md rules).

## Worked examples (from the statement)

1. Cubic field `x' = −y + x(1−x²−y²)`, `y' = x + y(1−x²−y²)`:
   `r·dr/dt = r²(1−r²)` ⇒ `A(u) = 1−u`, root `u=1` (r=1), sign + to − ⇒
   exactly ONE hyperbolic limit cycle. This is the "textbook case with known
   count" from GOAL.md item 3a.
2. Linear centre `x'=−y, y'=x`: `A ≡ 0` ⇒ zero limit cycles (negative
   control: a centre must NOT report a limit cycle).
3. Linear ``x' = x, y' = −y`` (saddle, no periodic orbit): `A(u) = 1, B(u)=0`.
   The identity field rotates nothing — `B ≡ 0` means no closed orbit can
   exist (θ constant); count = 0. Also tests the `B=0` branch.
4. Van der Pol missing rotational symmetry (x) ⇒ `is_radial` = False ⇒ the
   oracle refuses, honestly, rather than giving a wrong count. This is the
   probe of what the naive method cannot do.

## Run record

Command: `cd /workspace && timeout 120 python code/brute.py` — exit 0, ran in
seconds (timeout not hit). All 7 worked examples PASS:

| case | certified count | roots (u=r²) |
| --- | --- | --- |
| cubic normal form `x'=−y+x(1−x²−y²)`, `y'=x+y(1−x²−y²)` | 1 | 1.0000 |
| linear centre `x'=−y, y'=x` (A≡0) | 0 | — |
| linear expanding focus `x'=x−2y, y'=2x+y` (A≡1) | 0 | — |
| van der Pol-like `x'=y, y'=(1−x²−y²)y−x` | refused (non-radial) | — |
| linear saddle `x'=x, y'=−y` | refused (non-radial) | — |
| A=(1−u)(2−u), B=1 (two cycles) | 2 | 1, 2 |
| A=(1−u)²(2−u), B=1 (semi-stable at u=1) | 1 | 2 |

Excluded correctly: circle u=1 in the semi-stable case (double root, no sign
change — not a hyperbolic limit cycle); gcd(A,B) exclusion branch for rings of
equilibria is exercised by construction in cases 6–7 with gcd=1. Runs at
worked-example sizes only (degree ≤ 3, one band), as required: the oracle pins
down the meaning and does not attack the statement's bound.