#!/usr/bin/env python3
"""Gauge the per-cell slab candidate count for n=7 in the stated box."""
from fractions import Fraction
from itertools import combinations
from lib.es_construct import es_set_blocks

n = 7
pts, blocks = es_set_blocks(n)
N = len(pts)

xs = [p[0] for p in pts]
ys = [p[1] for p in pts]
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)
PAD = Fraction(2000)
box = (xmin - PAD, xmax + PAD, ymin - PAD, ymax + PAD)
bx0, bx1, by0, by1 = box
print("box x: [%s, %s]" % (bx0, bx1))
print("box y: [%s, %s]" % (by0, by1))

# collect all pairwise line intersection x-coordinates
# line through pts[a], pts[b]: param - only need x where two lines cross.
lines = list(combinations(range(N), 2))
M = len(lines)
print("M lines =", M, "-> pairs of lines =", M*(M-1)//2)

# For speed: represent each line as (A,B,C) with A x + B y + C = 0
def line_coeff(i, j):
    (ax, ay), (bx, by) = pts[i], pts[j]
    # A = dy, B = -dx, C = dx*ay - dy*ax   -> A x + B y + C = 0
    dx = bx - ax
    dy = by - ay
    A = dy
    B = -dx
    C = dx * ay - dy * ax
    return A, B, C

coeffs = [line_coeff(i, j) for (i, j) in lines]

event_x = set()
# clamp: we only need events inside [bx0-?, bx1+?]; events outside box can be
# represented by clamping to box edges for the slab structure, but to be exact
# compute all and filter in-box for the slabs.
count_total = 0
inbox_events = set()
for p in range(M):
    A1, B1, C1 = coeffs[p]
    for q in range(p+1, M):
        A2, B2, C2 = coeffs[q]
        den = A1*B2 - A2*B1
        if den == 0:
            continue  # parallel
        # x = (B1*C2 - B2*C1)/den
        xnum = B1*C2 - B2*C1
        x = Fraction(xnum, den)
        count_total += 1
        if bx0 < x < bx1:
            inbox_events.add(x)

print("total line-pair intersections:", count_total)
print("distinct in-box event x:", len(inbox_events))

ev = sorted(inbox_events)
print("min event x:", ev[0], "max event x:", ev[-1])
print("clamped box [%s, %s]" % (bx0, bx1))

# scanline x's: midpoints between consecutive events, plus ends within box
scan = []
if bx0 < ev[0]:
    scan.append((bx0 + ev[0])/2)
for i in range(len(ev)-1):
    scan.append((ev[i] + ev[i+1])/2)
if ev[-1] < bx1:
    scan.append((ev[-1] + bx1)/2)
print("scanlines:", len(scan))
if len(scan) < 30:
    for s in scan[:30]:
        print("  ", s)
else:
    print("  first 5:", scan[:5])
    print("  last 5:", scan[-5:])

# total candidate apexes (rough): per scanline, crossing y count ~ M
# but many out of box
print("M per scanline ~", M)
print("upper bound on candidates (scanlines * (M+1)):", len(scan)*(M+1))
