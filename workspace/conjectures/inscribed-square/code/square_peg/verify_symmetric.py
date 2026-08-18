"""Exact verification for symmetric and irregular polygon square pegs.

Evidence for the Nielsen--Wright symmetric-continuum square case and for the
sanity examples in code/brute.py.  All polygon arithmetic is Fraction-based;
this script reports no floating-point coordinates.
"""
from fractions import Fraction

from lib.geometry import Q, sub, cross, on_segment
from square_peg.oracle import find_squares, naive_vertex_squares

OUT = "code/out/verify_symmetric.txt"


def vertices(xs):
    return [(Q(x), Q(y)) for x, y in xs]


def orient(a, b, c):
    return cross(sub(b, a), sub(c, a))


def segments_intersect(a, b, c, d):
    """Exact closed-segment intersection, including collinear touching."""
    o1, o2 = orient(a, b, c), orient(a, b, d)
    o3, o4 = orient(c, d, a), orient(c, d, b)
    if o1 == 0 and on_segment(c, a, b):
        return True
    if o2 == 0 and on_segment(d, a, b):
        return True
    if o3 == 0 and on_segment(a, c, d):
        return True
    if o4 == 0 and on_segment(b, c, d):
        return True
    return ((o1 > 0) != (o2 > 0)) and ((o3 > 0) != (o4 > 0))


def is_jordan_polygon(vs):
    """Check distinct vertices and pairwise disjoint nonadjacent edges."""
    n = len(vs)
    if n < 3 or len(set(vs)) != n:
        return False
    edges = [(vs[i], vs[(i + 1) % n]) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if j == i + 1 or (i == 0 and j == n - 1):
                continue
            if segments_intersect(*edges[i], *edges[j]):
                return False
    return True


def fmt_square(square):
    return "(" + ", ".join("(" + str(x) + ", " + str(y) + ")" for x, y in square) + ")"


def main():
    lines = []
    def emit(*parts):
        line = " ".join(str(p) for p in parts)
        lines.append(line)
        print(line)

    emit("verify_symmetric — exact Fraction arithmetic")
    emit("sanity cases from code/brute.py")
    cases = [
        ("unit square", [(0, 0), (1, 0), (1, 1), (0, 1)], 1),
        ("2x1 rectangle", [(0, 0), (2, 0), (2, 1), (0, 1)], 0),
        ("diamond", [(1, 0), (0, 1), (-1, 0), (0, -1)], 1),
    ]
    for name, raw, expected in cases:
        vs = vertices(raw)
        found = find_squares(vs)
        vertex_found = naive_vertex_squares(vs)
        ok = len(found) == expected and len(vertex_found) == expected
        emit(("PASS" if ok else "FAIL"), name,
             "find_squares=", len(found), "naive_vertex_squares=", len(vertex_found),
             "expected=", expected)
        for square in found:
            emit("  square:", fmt_square(square))

    symmetric = vertices([(0, 0), (2, 0), (3, 1), (2, 2), (0, 2), (-1, 1)])
    emit("Nielsen–Wright line-symmetric hexagon")
    jordan = is_jordan_polygon(symmetric)
    emit(("PASS" if jordan else "FAIL"), "Jordan polygon:", jordan,
         "vertices distinct and nonadjacent edges disjoint")
    symmetric_squares = find_squares(symmetric)
    emit("exact squares found:", len(symmetric_squares))
    for square in symmetric_squares:
        emit("  square:", fmt_square(square))

    irregular = vertices([(0, 0), (3, 0), (4, 1), (1, 3), (0, 2)])
    irregular_squares = find_squares(irregular)
    emit("non-symmetric irregular pentagon")
    emit("squares found:", len(irregular_squares),
         "yes" if irregular_squares else "no")
    for square in irregular_squares:
        emit("  square:", fmt_square(square))

    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
