# OEIS A328227 — the circular-pool critical speed 4.6033388…

Source: https://oeis.org/A328227. Full record:
`research/sources/oeis-a328227-circle-critical-speed.full.md`.

## What the record is

A328227 is the **decimal expansion of the positive solution to
x² = 1 + (π + arccos(1/x))²**, i.e. the critical runner speed for the
goblin/dog/duck-in-a-round-pool escape problem.

- Value: 4.60333884875170035255658… = **V_circle**, exactly the constant
  used as an oracle in PE 761 and derived in this run's circle-critical-speed
  note (cos B = 1/V, sin B = (π+B)/V, tan B = π+B).
- The record's own comment states the goblin-lake interpretation ("This is
  the minimum value of k such that we will not be able to escape") and links
  IBM Ponder This May 2001 (which this run already holds at
  `research/sources/ponder-this-goblin-pool-circle.full.md`).
- Cross-references: x = -sec(y) where y is A115365 (smallest positive root
  of tan x = x, y ≈ 4.493409; so y = B + π where B ≈ 1.3518 is the escape
  angle); A328227 = 1/A213053, and A213053 is the absolute minimum of
  sinc(x) (negated), ≈ 0.2172336.

## Why it matters for this run

This is the **encyclopedic, catalogue-level confirmation** of the circle
identity the run already derived and sourced from IBM Ponder This. It fixes
the standard OEIS names for the circle constants and confirms, from an
independent curated source, that the circle critical speed is
4.603338848751700… . It corroborates that the run's reading of the circle
was correct.

**Caveat:** this is the *circle* constant. The PE 761 target is the regular
*hexagon* (−5.05505046), which is **not** in OEIS (see
`research/summaries/oeis-search-hexagon-critical-speed.md`: searched the
decimal, no result), and neither is the square constant 5.78859314.

```claim
id: oeis-a328227-circle-critical-speed
statement: The positive solution of x^2 = 1 + (Pi + arccos(1/x))^2 is 4.60333884875170035255... = V_circle, the critical runner speed for a round pool (goblin-lake / dog-and-duck / princess-and-beast problem); it equals -sec(y) with y the smallest positive root of tan(x)=x (A115365) and equals 1/A213053 (negative of the absolute minimum of sinc).
hypotheses: continuous pursuit on a circle; swimmer at center speed 1, runner on boundary at speed v; escape = reach boundary before the runner; optimal play.
holds-here: yes for the circle case (this is exactly this run's circle identity); does not give the hexagon value.
status: catalogued (OEIS, curated decimal-expansion record with the goblin-lake comment and Ponder-This link).
bearing: encyclopedic confirmation of V_circle; establishes the OEIS names A328227/A115365/A213053 for the circle constants; the hexagon and square constants are not catalogued.
anchor: research/sources/oeis-a328227-circle-critical-speed.full.md
```