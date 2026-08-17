#!/usr/bin/env python3
"""Debug the restricted-permutation replay on S=[1,2,3,4] at n=6.

Compares the sequence-derived 'first or last' extremes per point against an
independent DIRECT computation: p is extreme in conv(S) iff there exists a
direction u (exact rational) with p.u > q.u for all other q in S.  That is a
theorem, so a mismatch means the replay in restricted_permutations is buggy
(the theorem never is).  All arithmetic exact.
"""
from fractions import Fraction
from math import atan2, cos, sin, pi
import sys
sys.path.insert(0, "/workspace/code")
sys.path.insert(0, "/workspace")

from lib.es_construct import es_set_blocks
from lib.es_geom import convex_hull, in_convex_position
from allseq_adjudicate import (build_sequence, restricted_permutations)
import allseq_adjudicate as mod

points, blocks = es_set_blocks(6)
N = len(points)
events, init, permlist, counts = build_sequence(points)
xdict_global = {i: points[i][0] for i in range(N)}
mod.xdict_global = xdict_global

S = [1, 2, 3, 4]
orc = in_convex_position([points[i] for i in S])
print("oracle in_convex_position(S):", orc)
print("hull of S:", convex_hull([points[i] for i in S]))


def per_point_extremes(S, events):
    """Set of points that are first-or-last in some S-restricted permutation."""
    permsS = restricted_permutations(S, events)
    firsts, lasts = set(), set()
    for perm in permsS[1:]:
        firsts.add(perm[0])
        lasts.add(perm[-1])
    return firsts | lasts


def direct_extreme(p_idx, S):
    """p extreme in conv(S) iff some direction u (exact) separates it:
    (p - q) . u > 0 for all q in S, q != p.  Checked over a fine fan of
    candidate directions built from the pair-difference normals and their
    mid-angles, all converted to exact integer vectors."""
    p = points[p_idx]
    others = [points[i] for i in S if i != p_idx]
    if not others:
        return True
    # normals of the difference vectors (where ties happen) and midpoints
    cands = []
    for q in others:
        dx, dy = q[0] - p[0], q[1] - p[1]
        cands.append((dy, -dx))
        cands.append((-dy, dx))
    angles = sorted(set(atan2(u[1], u[0]) for u in cands))
    tests = []
    for a in angles:
        tests.append((round(10 ** 6 * cos(a)), round(10 ** 6 * sin(a))))
    for a1, a2 in zip(angles, angles[1:] + [angles[0] + 2 * pi]):
        am = (a1 + a2) / 2
        t = (round(10 ** 6 * cos(am)), round(10 ** 6 * sin(am)))
        # normalize
        g = _gcd(abs(t[0]), abs(t[1]))
        tests.append((t[0] // g, t[1] // g))
    def sep(u):
        return all((others[k][0]-p[0])*u[0] + (others[k][1]-p[1])*u[1] > 0
                   for k in range(len(others)))
    return any(sep(u) for u in tests)


def _gcd(a, b):
    while b:
        a, b = b, a % b
    return a


seq_extremes = per_point_extremes(S, events)
print("sequence-derived extreme points:", sorted(seq_extremes))
direct = {p_idx: direct_extreme(p_idx, S) for p_idx in S}
print("direct extreme points:", sorted(p for p, v in direct.items() if v))
for p_idx in S:
    print(f"  point {p_idx}: seq-extreme={p_idx in seq_extremes} "
          f"direct-extreme={direct[p_idx]}")