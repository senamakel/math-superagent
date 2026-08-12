#!/usr/bin/env python3
"""
PE 761 — brute-force numerical model of the runner/swimmer escape game.

CIRCLE case, unit pool (R = 1).  Goal: reproduce the oracle V_circle = 4.60333885.

IMPORTANT — why the naive "stage at antipode, dash straight" model FAILS
----------------------------------------------------------------------------
The task sketch suggests: swimmer stages at radius rho = 1/v diametrically
opposite the runner, then dashes in a straight line to a shore point.  I
implemented exactly that (brute-ver01) and also the fully general version
where the dash direction is a free angle (explore_general_dash.py).  BOTH give
V = pi+1 = 4.1416, NOT 4.60333885.  A straight-line dash from the radially
opposite staging point can never beat pi+1, because the swimmer's angular
advance while dashing is strictly limited once it leaves the safe disk.

This is the classic "goblin-in-the-lake" puzzle, and the known red herring:
the naive straight dash gives only pi+1 ~ 4.1416; the TRUE optimal is higher.
Authoritative source: IBM Research Ponder This, May 2001, "Goblin chase in a
pool" (traced to Martin Gardner, Mathematical Carnival).

The CORRECT optimal two-phase strategy
--------------------------------------
Phase 1 — STAGING ARC, not a fixed point.  The swimmer does NOT just sit at
radius 1/v opposite the runner.  Instead it swims a *semicircular arc* of
radius 1/(2v) (heading tangentially, keeping the runner diametrically opposite
the whole time).  This ends at radius 1/v from center, diametrically opposite
the runner, moving tangentially.

Phase 2 — TANGENT CHORD.  Continuing in that tangent direction (no turn), the
swimmer cuts a straight chord to shore, landing at a boundary point whose
azimuth is offset by angle
        B = arccos(1/v)
from the radial/antipodal line.  Chosen so cos(B) = 1/v: the runner's angular
speed and the swimmer's are matched at the staging point.

Measurements (unit radius):
   - swimmer chord distance from end of staging arc to shore = sin(B)
       (the chord subtends the angle; geometry gives length sin(B))
   - runner arc distance from its start (opposite the landing azimuth) to the
     landing point = pi + B
       (pi to get halfway around, plus B to the offset landing point)

Escape at speed v  <=>  swimmer's chord time <= runner's arc time
        sin(B) <= (pi + B) / v ,   with  B = arccos(1/v)
(tie at optimum).  This is the boundary-time comparison, equalized at the
critical v.  V_circle is the largest v for which escape holds.

We find V by scanning v directly (the escape test is a closed form in v), and
report the number against the oracle.  No iteration over the bound: each test
is a closed-form evaluation.

Usage:
    python code/brute.py circle        # reproduces 4.60333885
    python code/brute.py square
    python code/brute.py hexagon
(square/hexagon: the same two-phase structure applies on a polygon *perimeter*
but the geometry differs; left for solution.py.)
"""

import sys
import math


def circle_escape(v, rtol=1e-12):
    """Escape possible at speed v for the circle (two-phase optimal model).

    Returns True if swimmer can beat the runner.  Closed form:
      B = arccos(1/v),  escape <=> sin(B) <= (pi+B)/v.
    """
    if v <= 1.0:
        return True  # swimmer easily outruns angularly at start
    B = math.acos(1.0 / v)
    swim_time = math.sin(B)
    run_time = (math.pi + B) / v
    return swim_time <= run_time * (1 + rtol)


def circle_critical(v_lo=1.0, v_hi=10.0, iters=200):
    """Bisect on v to find the largest v at which the swimmer still escapes."""
    assert circle_escape(v_lo)
    assert not circle_escape(v_hi)
    for _ in range(iters):
        mid = 0.5 * (v_lo + v_hi)
        if circle_escape(mid):
            v_lo = mid
        else:
            v_hi = mid
    return 0.5 * (v_lo + v_hi)


ORACLE = {"circle": 4.60333885, "square": 5.78859314, "hexagon": None}


def main():
    shape = sys.argv[1] if len(sys.argv) > 1 else "circle"

    if shape == "circle":
        V = circle_critical()
        oracle = ORACLE["circle"]
        match = abs(V - oracle) < 5e-9
        print("=" * 66)
        print("CIRCLE case — two-phase optimal model (Ponder This / Gardner)")
        print("=" * 66)
        print(f"  V_circle (computed) = {V:.8f}")
        print(f"  V_circle (oracle)   = {oracle:.8f}")
        print(f"  matches oracle?     = {match}")
        print("-" * 66)
        print("  check: B = arccos(1/V) =", round(math.acos(1 / V), 6),
              "rad =", round(math.degrees(math.acos(1 / V)), 3), "deg")
        print("  check: sin(B)   =", round(math.sin(math.acos(1 / V)), 8))
        print("  check: (pi+B)/V =", round((math.pi + math.acos(1 / V)) / V, 8))
        print("  (both times equal at the critical v => dead heat)")
        print("-" * 66)
        print("  naive 'stage at antipode + straight dash' model gives only")
        print(f"  pi+1 = {math.pi + 1:.6f}  (the documented red herring; NOT the oracle)")
        print("=" * 66)
    elif shape == "square":
        oracle = ORACLE["square"]
        print("SQUARE case: two-phase structure applies on the polygon perimeter;")
        print("implemented in solution.py, not this circle brute.")
        print(f"oracle V_square = {oracle} (for reference)")
    elif shape == "hexagon":
        print("HEXAGON case: the run's target answer; derived in solution.py.")
        print("This brute reproduces the circle oracle; see solution.py for hexagon.")
    else:
        print(f"unknown shape '{shape}' (use circle, square, hexagon).")
        sys.exit(1)


if __name__ == "__main__":
    main()
