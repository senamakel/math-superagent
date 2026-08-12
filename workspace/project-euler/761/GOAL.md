# Goal

**Problem (PE 761):** A runner and a swimmer play in a pool. Runner moves along
the pool boundary at speed ≤ v (either direction); swimmer moves inside at
speed ≤ 1 (any direction); both react instantly; optimal play. Swimmer starts at
the pool center; runner starts at the midpoint of an edge (circle: anywhere on
the edge). Swimmer wins iff it reaches some boundary point before the runner
gets there.

**Critical speed V(shape):** the threshold runner speed. If v < V the swimmer
can always escape; if v > V the runner can always catch.

**Oracle values from the statement (must be reproduced before anything is
trusted):**
- `V_circle ≈ 4.60333885`
- `V_square ≈ 5.78859314`
- **Answer: V_hexagon**, rounded to 8 decimals.

## Symbols
- v: runner's max speed along the (polygon) boundary.
- V(shape): the critical v.
- Regular n-gon pool: θ = π/n. Swimmer at center, runner at edge midpoint.
- Critical speed formula (stewbasic, math.SE 1762665; corroborated by Abel et
  al. arXiv:2007.08965, "Escaping a Polygon"):
  - t = tan θ
  - K = largest integer in [0,n] with sin(Kθ) − (K+n)·t·cos(Kθ) < 0
    (== floor of the unique root of tan(xθ)−(x+n)t in [1, n/2))
  - α = ½·( Kθ + acos( 2·sin(Kθ)/((K+n)·t) − cos(Kθ) ) )
  - V(n) = 1/cos(α)

## Working model (mechanism)
The swimmer stages on an inner region homothetic to the pool (perimeter v times
smaller) keeping the center on the line to the runner ("centrally opposite"),
then dashes. Critical speed equalizes swimmer straight-line escape time to an
exit point against runner perimeter time to that point. On a polygon the
runner's angular speed is non-constant, so the safe region is a scaled copy of
the pool, not a circle.

## Completion criteria (all met)
1. [x] `code/brute.py` reproduces 4.60333885 (circle) — confirmed by tool_builder.
     The naive straight-dash model gives only π+1=4.1416; the correct two-phase
     (staging semicircular arc + tangent chord) gives the oracle. Falsifying
     check kept in `code/explore_general_dash.py`.
2. [x] Governing theory identified and sourced (research notes +
     math.SE full text + Abel et al. full text in research/).
3. [x] `code/solution.py` implements the exact formula with high precision and
     reproduces anchors n=3 (7.4049), n=4 (5.78859314), n→inf (4.60333885).
4. [x] `V_hexagon` produced to 8 decimals (claimed 5.05505046), verified by
     a second independent route (symbolic_math + scholar).

## Evidence so far
- `python code/brute.py circle` → V = 4.60333885 (matches oracle).
- steward/pattern prior: V(6) = 5.05505046330389... → 5.05505046.
- Published anchors reproduced by the exact formula (n=3,4,n→∞).
