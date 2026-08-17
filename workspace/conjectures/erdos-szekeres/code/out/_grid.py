from fractions import Fraction
from functools import cmp_to_key
from lib.es_construct import es_set_blocks
from lib.es_geom import orient

pts, blocks = es_set_blocks(7)
N = len(pts)

def circular_order(points, O):
    def half(idx):
        dx = points[idx][0] - O[0]; dy = points[idx][1] - O[1]
        return 0 if (dy > 0 or (dy == 0 and dx > 0)) else 1
    def cmp(a, b):
        ha, hb = half(a), half(b)
        if ha != hb: return -1 if ha < hb else 1
        return -1 if orient(O, points[a], points[b]) > 0 else 1
    return tuple(sorted(range(len(points)), key=cmp_to_key(cmp)))

# bounding box
xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
xmin, xmax = min(xs), max(xs)
ymin, ymax = min(ys), max(ys)
print("bbox x:", xmin, xmax, " y:", ymin, ymax)

# 21x21 grid + probe
apexes = [(Fraction(2500), Fraction(2750))]
for i in range(21):
    x = xmin + (xmax - xmin) * Fraction(i, 20)
    for j in range(21):
        y = ymin + (ymax - ymin) * Fraction(j, 20)
        # skip exact duplicates of probe
        if (x, y) == (Fraction(2500), Fraction(2750)):
            continue
        apexes.append((x, y))
print("total grid+probe apexes:", len(apexes))

# dedupe by circular order
orders = {}
nongeneral = 0
for O in apexes:
    # check general position: no two points collinear with apex
    ties = 0
    for a in range(N):
        for b in range(a+1, N):
            if orient(O, pts[a], pts[b]) == 0:
                ties += 1
    if ties:
        nongeneral += 1
        continue
    ord_t = circular_order(pts, O)
    orders.setdefault(ord_t, []).append(O)
print("non-general apexes skipped:", nongeneral)
print("distinct circular orders among grid+probe:", len(orders))
print("representatives:", len(orders))
