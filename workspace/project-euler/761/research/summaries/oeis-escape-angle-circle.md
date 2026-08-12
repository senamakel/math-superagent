# OEIS A115365 & A213053 — the circle-escape angle and its reciprocal

Sources: https://oeis.org/A115365, https://oeis.org/A213053. Full records:
`research/sources/oeis-a115365-circle-escape-angle.full.md`,
`research/sources/oeis-a213053-reciprocal-critical-speed.full.md`.

## A115365 — smallest positive root of tan(x) = x

4.4934094579090641753… (also the first zero of j₁, the spherical Bessel
function, and the first positive root of sinc(3,x)). In this run's circle
derivation, the escape angle B satisfies tan(B) = π + B, i.e.
(B+π) = y with tan(y) = y, so **y = B + π = A115365**. The critical speed
V_circle = -sec(y) = √(y²+1) = √(1+(π+B)²) (A328227).

## A213053 — absolute minimum of sinc(x), negated

-0.21723362821122… = -sin(y)/y where y = A115365, attained at |x| = A115365.
A328227 = 1/A213053 (so 1/V_circle ≈ 0.2172336, the reciprocal critical
speed = cos(B) from the circle identity cos(B) = 1/V).

## Why it matters

Together with A328227 these three OEIS records are the catalogue names for
the circle-escape constants this run computes. They independently confirm
V_circle = 4.6033388… = √(1+(π+B)²). They are background/confirmation
for the circle case; none of them supplies the hexagon value (PE 761 target,
uncatalogued).

```claim
id: oeis-escape-angle-circle
statement: The circle escape angle: B satisfies tan(B) = pi + B, and y = B + pi is the smallest positive root of tan(x) = x (OEIS A115365, 4.4934094579...). V_circle = sqrt(1+(pi+B)^2) = -sec(y) = sqrt(1+y^2) = 1/A213053, where A213053 = -0.2172336... is the absolute minimum of sin(x)/x.
hypotheses: as in the circle escape game.
holds-here: yes for the circle; the hexagon value is not in OEIS.
status: catalogued (OEIS).
bearing: confirms V_circle via a second curated source and fixes OEIS names for the circle constants.
anchor: research/sources/oeis-a115365-circle-escape-angle.full.md, research/sources/oeis-a213053-reciprocal-critical-speed.full.md
```