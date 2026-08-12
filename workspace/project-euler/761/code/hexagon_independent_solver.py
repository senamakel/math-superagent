#!/usr/bin/env python3
"""
PE 761 — INDEPENDENT two-phase (staging + dashed-exit) critical-speed solver.

Constraint: must NOT use the stewbasic K/alpha formula (code/solution.py).
This file contains NO K-index and NO arccos formula.  It encodes the game
geometry directly:

  Phase 1 (staging).  The swimmer swims outward from the centre along the
  edge-midpoint direction directly away from the runner, keeping the centre
  on the line to the runner, until it reaches the stage point
        S = (-rho, 0)        (inradius = 1, runner start at (1, 0))
  with the runner meanwhile running half the perimeter (P/2) to stay
  diametrically opposite.  The stage radius is rho = 1/v, because the
  runner's perimetral speed v and the swimmer's radial speed 1 must match
  the runner's P/2 journey:  (P/2)/v = rho  =>  rho = P/(2v).  For the
  circle P/2 = pi (radius 1), giving the classic rho = pi/v, which is the
  largest radius at which the swimmer can keep opposite the runner.

  Phase 2 (dash).  From S the swimmer dashes in a straight line to a
  boundary point P at azimuth offset angle b from the antipodal radial
  line.  The runner at the antipodal boundary point runs the shorter
  perimeter arc of length dist(A, P) (for the circle: pi + b, the
  B-offset tangent-chord geometry of Ponder This / Gardner).  At the
  critical speed, swimmer dash time = runner arc time:

        |S - P|  =  dist_bdry(antipode(A), P) / v

  Critical speed V(shape) = the fixed point of
        v  =  max over boundary points P of  dist_bdry(antipode(A), P) / |S-P|
  located by bisection on v (each v fixes rho = P/(2v), S = (-rho,0), and a
  dense 1-D scan of the boundary gives the max ratio).  This is exactly the
  "equalise swimmer straight-line time vs runner boundary time" min-max of
  the two-phase model.

The boundary scan is a 1-D loop over arc-length (the boundary is a curve,
polygon edges or circle), so this is a polynomial method: O(n_grid) per
v-test, ~60 bisection iterations.  No search over the answer space.

References (all read into research/ before writing this):
  - research/summaries/ponder-this-goblin-pool-circle.md  (B-chord identity)
  - research/summaries/mathfactor-princess-beast-optimal-escape.md (staged arc)
  - code/brute.py  (circle two-phase oracle model)
  - code/explore_general_dash.py  (the naive straight-dash dead end, pi+1)

Usage:
    python code/hexagon_independent_solver.py
(prints circle, square, hexagon and n=10000 limits; captures all values)
"""

import math

# ---------------------------------------------------------------------------
# Boundary geometry: shapes with inradius 1, runner start at (-1,0)... we use
# runner start at A = (1, 0), antipode at (-1, 0) on the circle; for polygons
# the runner starts at an edge midpoint (inradius-1 polygon, so edge midpoint
# at radial distance 1 from centre, sitting on the +x axis).
# ---------------------------------------------------------------------------


def polygon(n):
    """Regular n-gon, inradius 1, first edge midpoint at (1,0).

    Returns (verts, edge_len, perimeter, point(s)) with point(s) the
    boundary point at arc-length s from the first edge midpoint.
    """
    th = math.pi / n
    R = 1.0 / math.cos(th)               # circumradius
    # edge i has midpoint at angle 2*pi*i/n; vertices at midpoint angle +/- th
    verts = []
    for k in range(n):
        ang = 2.0 * math.pi * k / n + th   # vertex after midpoint k
        verts.append((R * math.cos(ang), R * math.sin(ang)))
    edge = math.dist(verts[0], verts[1])
    P = n * edge

    def point(s):
        s = s % P
        idx = int(s // edge)
        if idx >= n:
            idx = n - 1
        t = (s - idx * edge) / edge
        a, b = verts[idx], verts[(idx + 1) % n]
        return (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)

    return verts, edge, P, point


def circle():
    R = 1.0
    P = 2.0 * math.pi
    return None, None, P, (lambda s: (math.cos(s), math.sin(s)))


# ---------------------------------------------------------------------------
# Core escape test for a fixed v
# ---------------------------------------------------------------------------

def max_ratio(shape, v, n_grid=200001):
    """Max over boundary points P of dist_bdry(A->P both ways) / |S - P|.

    A = runner start (edge midpoint at (1,0), or circle angle 0).
    S = stage point = antipode of A at stage radius rho = P/(2v):
        S = (-rho, 0) on the circle; for the polygon, the antipodal edge
        midpoint is at angle pi i.e. point (-1, 0) radially, so
        S = (-rho, 0) with rho = P/(2v).
    Returns the max ratio at this v.
    """
    if shape == 'circle':
        P, point = 2.0 * math.pi, (lambda s: (math.cos(s), math.sin(s)))
        A = (1.0, 0.0)
    else:
        n = {'square': 4, 'hexagon': 6, 'n10000': 10000}[shape]
        _, _, P, point = polygon(n)
        A = (1.0, 0.0)
    rho = P / (2.0 * v)
    S = (-rho, 0.0)
    best = 0.0
    for i in range(n_grid):
        s = P * i / n_grid
        qx, qy = point(s)
        d_r = min(s, P - s)          # runner's shorter arc from A=(1,0) at s=0
        d_s = math.hypot(qx - S[0], qy - S[1])  # swimmer chord from S
        if d_s <= 0:
            continue
        r = d_r / d_s
        if r > best:
            best = r
    return best


def critical_speed(shape, v_lo=1.0, v_hi=40.0, iters=60, n_grid=200001):
    """Bisect on v for the fixed point v = max_ratio(shape, v)."""
    # max_ratio decreases with v (larger v -> smaller rho -> S closer to centre
    # -> shorter chords, and runner time /v in the definition is already the
    # ratio form: dist_bdry / |S-P| is what must equal v; as v grows, rho
    # shrinks so |S-P| grows, ratio drops).
    gl = max_ratio(shape, v_lo, n_grid)
    while gl < v_lo:      # safety: widen hi range a bit if needed
        v_lo *= 0.9
        gl = max_ratio(shape, v_lo, n_grid)
    gh = max_ratio(shape, v_hi, n_grid)
    while gh > v_hi and v_hi < 1e6:
        v_hi *= 1.5
        gh = max_ratio(shape, v_hi, n_grid)
    for _ in range(iters):
        mid = 0.5 * (v_lo + v_hi)
        gm = max_ratio(shape, mid, n_grid)
        if gm > mid:      # ratio exceeds v: swimmer still wins at mid
            v_lo = mid
        else:
            v_hi = mid
    return 0.5 * (v_lo + v_hi)


if __name__ == "__main__":
    print("=" * 72)
    print("PE 761 independent two-phase solver (staging + dashed exit)")
    print("NO stewbasic K/alpha formula; NO naive pi+1 straight dash.")
    print("=" * 72)
    for shape, oracle in [('circle', 4.60333885),
                          ('square', 5.78859314),
                          ('hexagon', 5.05505046),
                          ('n10000', 4.60333885)]:
        V = critical_speed(shape)
        print(f"{shape:8s}  V = {V:.8f}   oracle {oracle:.8f}   "
              f"diff {abs(V-oracle):.3e}")
    print("=" * 72)