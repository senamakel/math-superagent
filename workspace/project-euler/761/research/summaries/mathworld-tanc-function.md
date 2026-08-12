# MathWorld — Tanc Function

Source: https://mathworld.wolfram.com/TancFunction.html | converted from HTML.
Full text: `research/sources/mathworld-tanc-function.full.md`.

## Relevance
Directly relevant to the circle case of this run. The circle critical speed
solves a transcendental equation of exactly the `tan x = x` family (for a
circle of radius R, the critical condition is `sin B = (π+B)/V` with
`cos B = 1/V`, i.e. `tan B = π+B`; equivalently `tan x = x` at
`x = B+π ≈ 4.493409458`). Tanc is the named function whose roots are these
values.

## What it establishes
- Defines `tanc(z) = tan(z)/z` (Weisstein's coinage; no prior name exists).
- The first positive root of `tanc(x) = 1`, i.e. of **`tan x = x`**,
  is `x ≈ 4.4934094579090641753…` — this is the smallest positive root used by
  this run (circle constant `V_circle = sqrt(1+x^2) ≈ 4.60333885`). This root
  is catalogued in OEIS **A115365** (already held in this library as a
  summary).
- Derivative `dtanc/dz = sec²z/z − tanz/z²`; the indefinite integral has no
  closed form in conventional functions.
- Roots table: n=2 → 7.72525…, n=3 → 10.90412…, n=4 → 14.06619…, n=5 →
  17.22076… (successive solutions of `tan x = x`, approaching (n+½)π).

## What it implies for this problem
- It names and fixes the transcendental object behind V_circle: the root of
  `tan x = x` at `x≈4.493409458`, matching A115365 (held). This corroborates
  `research/notes/circle-critical-speed-identity.md` and the OEIS A115365
  summary already in the library.
- It does NOT give the polygon (square/hexagon) general-n formula; that remains
  sourced from Math.SE stewbasic + Abel et al. "Escaping a Polygon" (both
  held). Tanc is circle-specific corroboration, not an independent hexagon
  route.

```claim
id: tanc-root-tan-x-equals-x-a115365
statement: The smallest positive solution of tan(x)=x is x≈4.4934094579090641753, catalogued in OEIS A115365; this is the root the circle critical speed V_circle=sqrt(1+x^2)≈4.60333885 is built on. MathWorld's tanc(z)=tan(z)/z is the named function whose value 1 gives these roots.
hypotheses: tan(x)=x transcendental equation; x positive with (n+1/2)π < x < (n+1)π.
holds-here: yes — the circle case (V_circle=4.60333885) is exactly this.
status: sourced (MathWorld + OEIS A115365, both held).
bearing: corroborates the circle identity already established; no bearing on the hexagon value itself.
anchor: research/sources/mathworld-tanc-function.full.md
```
