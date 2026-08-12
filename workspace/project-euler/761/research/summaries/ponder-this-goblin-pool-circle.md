# Ponder This May 2001 — Goblin chase in a circular pool (the circle critical speed)

Source: https://research.ibm.com/blog/ponder-this-may-2001 (IBM Research Ponder This,
May 2001). Full text: `research/sources/ponder-this-goblin-pool-circle.full.md`.

## What it settles (for PE 761)

This is the primary, authoritative treatment of the **circle** case of the
runner-and-swimmer game — exactly the case the open request
`exact-derivation-identity-e375` asks about, and the template the hexagon
derivation generalizes.

Setup identical to PE 761: swimmer starts at the center of a circular lake of
radius R, swims at speed 1 in any direction; a runner ("goblin") starts at the
edge and runs along the circumference at speed k (in PE's notation, the runner
speed is v). Escape = reach an edge point before the runner gets there.

## The governing identity (the exact result)

The critical runner speed V (PE's V_Circle) is the solution of the two coupled
equations

    cos(B) = 1/V
    sin(B) = (1/V)·(π + B)

giving B = 1.3518168 rad (77.453398°) and V = V_Circle = 4.6033388.

Optimal play: two phases.
1. A semicircular arc of radius R/(2V), keeping the swimmer diametrically
   opposite the runner; this flips the runner to the opposite side.
2. A straight chord to shore, hitting the edge at angle B from the normal. The
   swimmer's remaining distance is R·sin(B), while the runner must travel
   R(π+B) around the edge. The runner catches exactly when
   R·sin(B) = (1/V)·R(π+B), i.e. the second equation; the first fixes
   cos(B)=1/V geometrically.

The "goblin's advantage" function GA = (time for swimmer to reach chosen edge
point P) − (time for runner to reach P) is the Lyapunov function: it never
increases under swimmer play and never decreases under runner play at the
critical B, so at k = V the GA stays 0 (dead heat); for k < V it starts
negative and stays negative, so the swimmer always escapes.

- **answers: exact-derivation-identity-e375** — this note closes the open
  request `exact-derivation-identity-e375`.

## Relevance / note

- This source gives V_Circle = 4.60333885 (matches PE's oracle to 8 digits),
  confirming the boundary-time comparison is the right structural mechanism for
  the circle.
- It predates PE 761 (which uses the same game for square and hexagon), so it
  is a legitimate governing reference, not a published answer to a contest
  problem.
- The mechanism generalizes: for the square/hexagon the swimmer starts at the
  center and the runner at an edge midpoint, and the same "equalize swimmer
  time to a boundary point against runner perimeter time" comparison should
  give V_Square and V_Hexagon. V_Square ≈ 5.78859314 (still to be derived from
  this template).
