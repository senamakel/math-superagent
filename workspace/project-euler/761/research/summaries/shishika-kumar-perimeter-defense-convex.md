# Shishika & Kumar — "Perimeter-defense Game on Arbitrary Convex Shapes"

Source: arXiv:1909.03989, PDF at https://arxiv.org/pdf/1909.03989. Full text:
`research/sources/shishika-kumar-perimeter-defense-convex.full.md`.

## What the paper establishes

This is a modern published (robotics/differential-games venue) treatment of
**the defender-constrained-to-perimeter game**, which is structurally the
same kind of game PE 761 instantiates (defender/runner confined to the
boundary of a convex region, attacker/swimmer moving in the interior). It
extends the well-studied *circular-perimeter* case to **any convex shape**
(polygons included).

- **1-defender vs 1-intruder, arbitrary convex shape.** Solved analytically
  (assuming the defender is at least as fast as the intruder in the
  appropriate scaling). The intruder's winning region R_A(s_D) and the
  defender's winning region are separated by a **barrier** = the zero level
  set of a value function V(s_D, x_A) (Theorem 1). The intruder win/lose is
  decided by a reachability / capture-region test computed via the
  defender's "left" and "right" reachable critical points s_L, s_R on the
  perimeter (Algorithm 1–2).
- **Optimal strategies.** Closed-loop controls for both players: the
  intruder heads to the nearer of two critical shoreline points; the
  defender always moves at full speed toward the relevant side (Theorem 3).
  This is exactly a *boundary-time / shortest-path equalization* structure:
  the partition of the perimeter by whether the intruder can reach a given
  shore point before the defender covers the perimeter arc to it.
- **Two defenders → pincer.** A pair of defenders can capture an intruder
  neither could alone, via a coordinated "pincer" (left/right = +1/−1)
  movement whose barriers are described by a pair value function (Theorems
  5–6).
- **Circular-perimeter specialization (Theorem 4, from ref [39]).** Recovers
  the classical circle result.

## Why it matters for this run

It is the **modern differential-game framework** for the exact boundary-game
PE 761 models, and it confirms (from an independent, peer-venue-adjacent
robotics source) the structural principle the run relies on: the critical
threshold is decided by comparing the attacker's shortest path to a boundary
point against the defender's perimeter-constrained path to that point, and
the winning/threshold boundary is a capture-region barrier, not an ad hoc
construction.

**Caveats:**
- It solves the game for **equal-speed / defender-at-least-as-fast**
  scalings and reports a **win/lose barrier**, not the numerical critical
  *speed ratio* for a salient-regular-n-gon with the swimmer starting at the
  exact center and the runner at an edge midpoint. In particular it does
  **not** give V_hexagon or V_square numerically.
- It is a differential-games reachability treatment rather than the
  combinatorial/analytic critical-speed formula of stewbasic / Abel et al.
  So it is corroborating theory and framework, not a source of the final
  number.

```claim
id: perimeter-defense-convex-barrier
statement: The one-defender-vs-one-intruder perimeter-defense game on an arbitrary convex shape (defender constrained to the boundary, intruder in the interior) has a capture barrier given by the zero level set of a value function V(D,x_A): the intruder wins iff it starts in its reaching region (beyond the barrier), decided by comparing its straight path to critical shoreline points against the defender's perimeter arcs. Optimal closed-loop strategies exist; two defenders can pincer an intruder no single defender could stop.
hypotheses: defender faster-or-equal under the model scaling, convex target shape, full information, game-of-kind (win/lose) objective.
holds-here: partially - the same boundary-vs-interior structure as PE 761 and the same shortest-path/perimeter comparison underlies the critical-speed formula; but the paper reports win/lose barriers for equal/faster defender scalings, not the numerical critical speed ratio for the center-started regular-n-gon, and no hexagon/square value.
status: peer-venue-adjacent arXiv paper, results are proved (formally stated lemmas/theorems).
bearing: corroborates the mechanism (perimeter-time equalization) from a modern differential-game source; not a route to the final 8-decimal hexagon answer.
anchor: research/sources/shishika-kumar-perimeter-defense-convex.full.md
```