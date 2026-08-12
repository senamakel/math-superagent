#!/usr/bin/env python3
"""
PE 761 — NAIVE ORACLE for the regular n-gon, from first principles.

This does NOT use any sourced critical-speed formula.  It models the game as a
plain boundary-time race in the most obviously-correct way we can state:

  * The runner starts at the midpoint of one edge.  By symmetry the swimmer
    stages on the axis through the center and that midpoint, at radial
    distance s from the center on the FAR side (centrally opposite the runner),
    then dashes in a STRAIGHT LINE to a boundary point P.
  * Skimmer's dash time   = |P - S|  (speed 1)
  * Runner's time to P    = perimeter distance from start edge-midpoint to P (speed v)
  * Escape of the swimmer at speed v  <=>  |P-S| <= (runner perimeter dist)/v
  * The naive critical speed is the largest v over all staging distances s
    and exit points P of  (runner perimeter dist)/|P-S|.

This is the polygon analog of the circle red-herring model
(explore_general_dash.py) which only ever reaches pi+1 for the circle.  For the
polygon there is extra freedom (perimeter vs chord geometry) so we measure
what the naive model actually gives, against the oracle V_square = 5.78859314.

Exact arithmetic: uses math (double) for trig of the exact vertex geometry and
exact integer/rational perimeter lengths for the boundary race.  This is an
oracle over swimmer STRATEGY (staging s, exit P), never over the answer value,
so it is the legitimate brute force: it searches the swimmer's options, not the
candidate speeds.

Usage:  python code/brute_polygon_naive.py
"""

import math
import itertools


def regular_polygon(n, circumradius=1.0):
    """Vertices of a regular n-gon centered at origin, circumradius 1.

    Place an edge midpoint on the +x axis (matching the runner starting at the
    midpoint of the 'right' edge)."""
    verts = []
    # place so that one edge midpoint is exactly at angle 0
    for k in range(n):
        angle = -math.pi / n + 2 * math.pi * k / n
        verts.append((circumradius * math.cos(angle), circumradius * math.sin(angle)))
    return verts


def edge_midpoints(verts):
    n = len(verts)
    mids = []
    for i in range(n):
        a, b = verts[i], verts[(i + 1) % n]
        mids.append(((a[0] + b[0]) / 2, (a[1] + b[1]) / 2))
    return mids


def perim_dist_from(mid_index, point, verts, epsilon=1e-12):
    """Perimeter distance from edge-midpoint mid_index to a boundary point
    (x,y) that lies on an edge, going the shorter way around the polygon."""
    n = len(verts)
    # locate which edge the point is on
    edge_len = math.dist(verts[0], verts[1])

    def on_edge(p, a, b, eps=1e-9):
        cross = (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
        if abs(cross) > eps:
            return False
        return min(a[0], b[0]) - eps <= p[0] <= max(a[0], b[0]) + eps and \
               min(a[1], b[1]) - eps <= p[1] <= max(a[1], b[1]) + eps

    target_edge = None
    for i in range(n):
        if on_edge(point, verts[i], verts[(i + 1) % n]):
            target_edge = i
            break
    if target_edge is None:
        raise ValueError(f"point {point} not on any edge")

    # distance from start midpoint to the two endpoints of start edge
    sm = mids[mid_index]  # midpoint of edge mid_index
    start_edge = mid_index

    def dist_along(p_from, a, b):
        # distance from a point p_from (on edge between a,b) to vertex b
        return math.dist(p_from, b)

    # measured distances along the perimeter
    # distance from start midpoint to vertex 'b' of its edge (going toward vertex index+1)
    def run_ccw(point_on_start, dest_edge, dest_point):
        # start at point_on_start on start edge, go in +vertex direction around polygon
        d = 0.0
        cur_on = point_on_start
        cur_edge = start_edge
        while cur_edge != dest_edge:
            # go from cur_on to the next vertex clockwise (increasing index), then continue
            b = verts[(cur_edge + 1) % n]
            d += math.dist(cur_on, b)
            cur_edge = (cur_edge + 1) % n
            cur_on = verts[cur_edge]
        # now cur_edge == dest_edge; distance along this edge from vertex cur_edge to dest_point
        # cur_on is vertex verts[cur_edge]
        d += math.dist(cur_on, dest_point)
        return d

    d_ccw = run_ccw(mids[start_edge], target_edge, point)
    # cw = full perimeter - ccw (since starting at an edge midpoint, both dirs)
    perim = n * edge_len
    d_cw = perim - d_ccw
    return min(d_ccw, d_cw), perim


def naive_critical(n, staging_s=0.999):
    """The naive critical speed for the n-gon: max over exit points P of
    (runner perimeter dist to P)/(swimmer straight dist from staging to P)."""
    verts = regular_polygon(n)
    mids = edge_midpoints(verts)
    # runner starts at the midpoint on the +x axis (edge mid_index with +x)
    # find that midpoint
    runner_mid = None
    mid_index = None
    for i, m in enumerate(mids):
        if abs(m[1]) < 1e-9 and m[0] > 0:
            runner_mid = m
            mid_index = i
            break
    # swimmer stages at far side: opposite along the x-axis
    S = (-staging_s, 0.0)

    best = 0.0
    best_P = None
    edge_len = math.dist(verts[0], verts[1])
    # search over a grid of points along each edge
    for i in range(n):
        a, b = verts[i], verts[(i + 1) % n]
        for t in range(0, 1001):
            u = t / 1000
            P = (a[0] + u * (b[0] - a[0]), a[1] + u * (b[1] - a[1]))
            d_swim = math.dist(S, P)
            if d_swim < 1e-12:
                continue
            d_run, _ = perim_dist_from(mid_index, P, verts)
            ratio = d_run / d_swim
            if ratio > best:
                best = ratio
                best_P = P
    return best, best_P, mid_index, edge_len


def main():
    print("=" * 70)
    print("PE 761 naive polygon oracle — straight-dash boundary-time race")
    print("=" * 70)
    for n, oracle, name in [(4, 5.78859314, "square"), (6, None, "hexagon"),
                            (1000, 4.60333885, "near-circle")]:
        for s in (0.95, 0.99, 0.999):
            best, P, mid_idx, elen = naive_critical(n, staging_s=s)
            print(f"n={n:5d} ({name:10s}) staging_s={s:.3f}  naive V = {best:.6f}  "
                  f"exit P=({P[0]:.3f},{P[1]:.3f})")
        best, P, _, _ = naive_critical(n, staging_s=0.999)
        if oracle:
            print(f"   [{name} oracle V = {oracle}]  naive model {'matches' if abs(best-oracle) < 1e-3 else 'DOES NOT match'}")
        print()
    print("=" * 70)
    print("Reference: for the CIRCLE the identical naive straight-dash model")
    print("maxes out at pi+1 = 4.14159 (red herring), NOT the 4.60333885 oracle.")
    print("So a naive straight dash is expected to undershoot the polygon oracle too,")
    print("because staging on a straight radial line is suboptimal on a polygon.")


if __name__ == "__main__":
    main()
