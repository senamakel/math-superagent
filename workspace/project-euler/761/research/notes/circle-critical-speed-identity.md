# Circle critical speed: source and exact governing equation

**Question.** The classical swimmer-vs-runner (goblin-on-edge / man-in-cirular-lake)
escape problem: swimmer at the center of a radius-R circular lake speed 1, runner on
the shore at speed factor v. Find the critical v separating escape (v < V) from capture
(v > V), and the exact identity whose solution gives V_circle ≈ 4.60333885. Also:
confirm the geometry (stage at radius 1/v diametrically opposite, then dash) and the
general form a regular polygon would use.

## Primary source

**IBM Research Ponder This, May 2001, "Goblin chase in a pool."**
URL: https://research.ibm.com/blog/ponder-this-may-2001
(filename: `research/sources/ponder-this-goblin-pool-circle.full.md`)

Traces to Martin Gardner, *Mathematical Carnival* (1965 Scientific American column).

The threshold is T = 4.6033388, the solution of the pair of equations

    cos(B) = 1/T
    sin(B) = (1/T) * (pi + B)

with B ≈ 1.3518168 rad (= 77.453398°). Equivalently tan(B) = pi + B.

## Exact identity / closed form

Let `x = pi + B`. Then `tan(x) = x`, so x is the smallest positive root of tan(x) = x,
x ≈ 4.493409458. Then:

    B  = x - pi    ≈ 1.3518168
    T  = 1/cos(B) = sqrt(1 + x^2)  ≈ 4.60333885

Derivation: eliminating T gives sin(B) = cos(B)(pi+B), i.e. tan(B)=pi+B; with
x=pi+B, tan(x-pi)=tan(x)=x. And 1/cos(B) = 1/cos(x-pi) = -1/cos(x) = |sec(x)|
= sqrt(1+x^2). (Analytic confirmation, exact; x^2+1 = sqrt(21.190729...)=4.603339,
matching the stated 4.60333885 to 8 dp.)

## Geometry: staging-then-dash — CONFIRMED, with a caveat

The classic optimal strategy is a **two-phase** path, not a naive single dash:

1. **Phase 1.** The swimmer spirals outward keeping *diametrically opposite* the
   runner (center between swimmer and runner), along a semicircular arc of radius
   R/(2v), ending at radius **R/v = 1/v·R** from the center. ("Stage at radius 1/v
   diametrically opposite" is correct as the staging condition.)
2. **Phase 2.** The swimmer dashes in a **straight chord** to a shore point whose
   azimuth is at angle **B** off the antipodal/radial line (B = arccos(1/v)).

The escape point is NOT the diametrically opposite boundary point: it is offset by
angle B. Criticality is the equality of the two travel times to that landing point
(swimmer chord time = runner arc time, both must arrive simultaneously). This is
exactly the "v = max over boundary points of (runner-arc-time)/(swimmer-distance)"
min-max principle — the runner's choice of direction, swimmer's choice of landing
point — and the optimum lands on the B-offset point.

Critical equality (from Ponder This, second phase): swimmer travels distance R·sin(B);
runner travels R·(pi + B). Tie when R·sin(B) = (R/v)(pi+B), i.e. sin(B) = (pi+B)/v,
together with cos(B) = 1/v. ✓

Naive bound: staging at R/v then dashing *radially* to the nearest shore point gives
only T = pi + 1 ≈ 4.1416 (inferior; a red herring the Ponder This page explicitly
warns against). T = 4.6033 uses the B-offset chord.

## Corroborating independent sources (same value, same equations)

- Quanta Magazine, "Math Can, in Theory, Help You Escape a Hungry Bear" (2021-08-25),
  https://www.quantamagazine.org/math-can-in-theory-help-you-escape-a-hungry-bear-20210825/
  — restates the Martin Gardner classic; threshold 4.6033, sqrt(4.6033^2-1)≈4.4934,
  arccos(1/4.6033)≈1.3518, pi+1.3518≈4.4934.
- dfeng.github.io "Goblin Chase Puzzle", http://dfeng.github.io/2012/goblin-chase-puzzle
  — identical equations sin(B) = (pi+B)cos(B), cos(B)=1/k, B≈1.3518168, T≈4.6033388.
- Puzzling.SE "The lake monster" (2014), https://puzzling.stackexchange.com/questions/2155/the-lake-monster
  — explains pi+1 naive bound vs the better ~4.6 strategy.

## Regular polygon generalization

The circle is the *continuous* analog of a regular polygon's boundary. All sources
treat only the circle. The structural principle the polygon version inherits:
staging radius R/v shielding angular speed, then a chord dash to an edge point at an
optimum azimuth B; criticality from equalizing swimmer travel time and runner perimeter
time (arc length = perimeter distance along polygon edges) to a common landing point.
For a square the analogous constant is V_square ≈ 5.78859314 (given in the run's
context; larger than circle because the square boundary is longer per unit and has
corners to run around, so the runner needs more speed to cover it). The regular
hexagon is the run's target. This polygon-specific derivation is NOT in any found
source — it is the run's own work to carry out; only the structural principle is sourced.

## Sourced claim

```claim
id: circle-critical-speed-identity-e375
statement: The critical runner speed for escape from a circular pool (swimmer at center,
speed 1; runner on boundary at speed factor v) is V_circle = sqrt(1+x^2) ≈ 4.60333885
where x ≈ 4.493409458 is the smallest positive root of tan(x) = x; equivalently V = 1/cos(B)
with B the solution of tan(B) = pi + B (B ≈ 1.3518168 rad).
hypotheses: circular pool of any radius (scale-invariant); swimmer starts at center,
runner starts at an arbitrary edge point; both players optimal with instant reaction;
swimmer speed normalized to 1, runner speed factor v; escape = swimmer reaches some
boundary point before the runner does.
holds-here: yes — identical to the run's circle case (V_circle ≈ 4.60333885).
status: sourced (IBM Ponder This May 2001 + independent corroboration) and analytically
confirmed.
bearing: this is the exact identity/closed form the run's step 2 needed; it is the
template whose min-max boundary-time structure the square and regular-hexagon
derivations generalize.
anchor: research/sources/ponder-this-goblin-pool-circle.full.md
```
