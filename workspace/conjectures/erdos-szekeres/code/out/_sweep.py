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

xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
ymin, ymax = min(ys), max(ys)
ycenter = (ymin + ymax) / 2
print("ycenter:", ycenter)

def vertical_sweep_orders(x0, ylo, yhi):
    # y-coordinates where each pair-line crosses x=x0
    crossings = set()
    for a in range(N):
        for b in range(a+1, N):
            px, py = pts[a]; qx, qy = pts[b]
            if qx == px:
                continue  # vertical pair line: no crossing at vertical apex line
            # y at x=x0
            t = Fraction(x0 - px, qx - px)
            y = py + (qy - py) * t
            crossings.add(y)
    ys_sorted = sorted(y for y in crossings if ylo < y < yhi)
    # sample apex between consecutive crossings
    samples = []
    prev = ylo
    for y in ys_sorted:
        mid = (prev + y) / 2
        samples.append((Fraction(x0), mid))
        prev = y
    mid = (prev + yhi) / 2
    samples.append((Fraction(x0), mid))
    return samples, len(ys_sorted)

def horizontal_sweep_orders(y0, xlo, xhi):
    crossings = set()
    for a in range(N):
        for b in range(a+1, N):
            px, py = pts[a]; qx, qy = pts[b]
            if qy == py:
                continue
            t = Fraction(y0 - py, qy - py)
            x = px + (qx - px) * t
            crossings.add(x)
    xs_sorted = sorted(x for x in crossings if xlo < x < xhi)
    samples = []
    prev = xlo
    for x in xs_sorted:
        mid = (prev + x) / 2
        samples.append((mid, Fraction(y0)))
        prev = x
    mid = (prev + xhi) / 2
    samples.append((mid, Fraction(y0)))
    return samples, len(xs_sorted)

# vertical sweep at x=2500 over full y-range of box (or slightly beyond)
samples_v, nv = vertical_sweep_orders(Fraction(2500), ymin, ymax)
print("vertical sweep x=2500: crossings in box:", nv, " sampled:", len(samples_v))
samples_h, nh = horizontal_sweep_orders(ycenter, Fraction(0), Fraction(5000))
print("horizontal sweep y=ycenter: crossings in box:", nh, " sampled:", len(samples_h))

# distinct orders from all samples
orders = set()
nong = 0
for O in samples_v + samples_h:
    ties = 0
    for a in range(N):
        for b in range(a+1, N):
            if orient(O, pts[a], pts[b]) == 0:
                ties += 1
    if ties:
        nong += 1
        continue
    orders.add(circular_order(pts, O))
print("non-general sweep samples:", nong)
print("distinct circular orders from sweeps:", len(orders))
