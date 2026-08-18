"""Naive exact oracle for inscribed squares on polygonal Jordan curves.

Claim supported: the worked polygon examples in problem.md, and the formal
configuration-space statement intended for code/lean/Lib/Statement.lean.
This is deliberately factorial/exponential and only an oracle for tiny polygons.
"""
from itertools import combinations
from fractions import Fraction


def cross(a, b):
    return a[0]*b[1] - a[1]*b[0]


def sub(a, b):
    return (a[0]-b[0], a[1]-b[1])


def is_square(points):
    ds = []
    for i in range(4):
        for j in range(i+1, 4):
            d = sub(points[i], points[j])
            ds.append(d[0]*d[0] + d[1]*d[1])
    ds.sort()
    return ds[0] > 0 and ds[0] == ds[1] == ds[2] == ds[3] and ds[4] == ds[5] == 2*ds[0]


def point_on_segment(p, a, b):
    ab = sub(b, a)
    ap = sub(p, a)
    return cross(ab, ap) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])


def oracle(vertices):
    """Return all 4-vertex subsets forming exact nondegenerate squares."""
    found = []
    for inds in combinations(range(len(vertices)), 4):
        pts = [vertices[i] for i in inds]
        if is_square(pts):
            found.append(inds)
    return found


EXAMPLES = {
    "unit square": [(Fraction(0), Fraction(0)), (Fraction(1), Fraction(0)),
                    (Fraction(1), Fraction(1)), (Fraction(0), Fraction(1))],
    "rectangle 2x1": [(Fraction(0), Fraction(0)), (Fraction(2), Fraction(0)),
                       (Fraction(2), Fraction(1)), (Fraction(0), Fraction(1))],
    "diamond": [(Fraction(1), Fraction(0)), (Fraction(0), Fraction(1)),
                (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(-1))],
}

if __name__ == "__main__":
    for name, polygon in EXAMPLES.items():
        print(name, oracle(polygon))
