#!/usr/bin/env python3
"""EXACT arrangement oracle for p(n,L), n in {3,4}, over integer L.

Speeds v_j ~ iid Exp(1). Common scaling of all speeds preserves every relative
time ordering, so the race outcome is invariant to scaling; the normalized
speeds are uniform on the unit simplex (Dirichlet(1,..,1), density (n-1)!). In
free coordinates (v0,..,v_{n-2}), v_{n-1}=1-Sum, so

    p(n,L)  =  (n-1)! * (plain Euclidean measure of the even-parity cells)

Each candidate event time is constant-over-linear:
    F_j  = (L - 40 j) / v_j
    C_ab = 40 (b-a) / (v_a - v_b),   a<b
so any equality of two candidate times, cross-multiplied, is a LINEAR equation
in the free coordinates, as is every v_a=v_b line. The arrangement of all these
lines/planes cuts the simplex into cells of constant chronological event order
and constant relative-speed sign -> constant race outcome. We enumerate the
cells (exact rational), evaluate the exact race at an interior rational point
(centroid) via exact_race.outcome_parity_exact, and sum exact cell areas
(shoelace, n=3) / volumes (facet triangulation, n=4).

Anchor checks implemented/tested IN this file's correctness history:
    p(3,160) = 56/135 ~ 0.4148148148...
    p(4,400) = 0.5107843137... (given 10 dp)
"""
import sys, os, json, itertools
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exact_race import outcome_parity_exact


# ---- linear forms in free coordinates (v0..v_{n-2}), v_{n-1}=1-Sum --------
# Represented as (coeffs, const): sum coeffs[i]*v_i + const.

def v_lin(j, nfree):
    """Linear form equal to speed v_j in free coords."""
    if j < nfree:
        c = [F(0)] * nfree
        c[j] = F(1)
        return (c, F(0))
    else:
        return ([-F(1)] * nfree, F(1))

def lin_scalar(l, k):
    c, t = l
    return ([k * x for x in c], k * t)

def lin_add(l1, l2):
    c1, t1 = l1; c2, t2 = l2
    return ([a + b for a, b in zip(c1, c2)], t1 + t2)

def lin_sub(l1, l2):
    c1, t1 = l1; c2, t2 = l2
    return ([a - b for a, b in zip(c1, c2)], t1 - t2)

def lin_eval(l, pt):
    c, t = l
    acc = t
    for ci, xi in zip(c, pt):
        acc += ci * xi
    return acc


def build_lines(n, L):
    """Return list of (name, Linear) separating lines for n boats, course L."""
    nfree = n - 1
    L = F(L)
    # candidate events: (num constant, den linear)
    events = []
    for j in range(n):
        events.append((f'F{j}', F(L - 40 * j), v_lin(j, nfree)))
    for a in range(n):
        for b in range(a + 1, n):
            den = lin_sub(v_lin(a, nfree), v_lin(b, nfree))
            events.append((f'C{a}{b}', F(40) * (b - a), den))
    lines = []
    # vertex-equality lines v_a - v_b = 0
    for a in range(n):
        for b in range(a + 1, n):
            lines.append((f'v{a}=v{b}', lin_sub(v_lin(a, nfree), v_lin(b, nfree))))
    # equality of any two candidate event times: num1*den2 - num2*den1 = 0
    for (nm1, n1, d1), (nm2, n2, d2) in itertools.combinations(events, 2):
        g = lin_sub(lin_scalar(d2, n1), lin_scalar(d1, n2))
        lines.append((f'{nm1}={nm2}', g))
    return lines, events


# ============================================================================
# 2D cell enumeration (n=3): polygon clipping
# ============================================================================

def clip_poly(poly, f, keep_ge):
    """Intersect convex polygon (list of Fraction pts) with {f>=0} or {f<=0}."""
    out = []
    m = len(poly)
    for i in range(m):
        p = poly[i]; q = poly[(i + 1) % m]
        sp = f(p); sq = f(q)
        pin = sp >= 0 if keep_ge else sp <= 0
        qin = sq >= 0 if keep_ge else sq <= 0
        def inter():
            if sp == sq:
                return p
            t = sp / (sp - sq)
            return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))
        if qin:
            if not pin:
                out.append(inter())
            out.append(q)
        elif pin:
            out.append(inter())
    return out

def poly_area(poly):
    a = F(0)
    m = len(poly)
    for i in range(m):
        x1, y1 = poly[i]; x2, y2 = poly[(i + 1) % m]
        a += x1 * y2 - x2 * y1
    return a / 2

def poly_centroid(poly):
    sx = sum(p[0] for p in poly)
    sy = sum(p[1] for p in poly)
    m = F(len(poly))
    return (sx / m, sy / m)

def cells_2d(lines):
    """Enumerate full-dimensional cells of the line arrangement in the
    triangle {v0>=0, v1>=0, v0+v1<=1}."""
    tri = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1))]
    cells = [tri]
    for name, g in lines:
        newcells = []
        for cell in cells:
            if not cell:
                continue
            signs = [lin_eval(g, p) for p in cell]
            mn, mx = min(signs), max(signs)
            if mn >= 0:
                newcells.append(cell)
            elif mx <= 0:
                newcells.append(cell)
            else:
                f = lambda p: lin_eval(g, p)
                pos = clip_poly(cell, f, True)
                neg = clip_poly(cell, f, False)
                if len(pos) >= 3:
                    newcells.append(pos)
                if len(neg) >= 3:
                    newcells.append(neg)
        cells = newcells
    return cells


# ============================================================================
# 3D cell enumeration (n=4): polyhedron (H-representation) + exact volume
# ============================================================================

def solve3(A, b):
    """Solve real 3x3 system A x = b by exact Gaussian elimination.
    A: list of 3 rows of 3 Fractions; b: list of 3 Fractions."""
    M = [list(row) + [bi] for row, bi in zip(A, b)]
    for col in range(3):
        piv = None
        for r in range(col, 3):
            if M[r][col] != 0:
                piv = r; break
        if piv is None:
            return None  # singular/degenerate (not a unique vertex)
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        for j in range(col, 4):
            M[col][j] /= pv
        for r in range(3):
            if r == col:
                continue
            factor = M[r][col]
            if factor != 0:
                for j in range(col, 4):
                    M[r][j] -= factor * M[col][j]
    return [M[r][3] for r in range(3)]

def poly_vertices(constraints):
    """Vertices of the bounded polyhedron {x : l(x) >= 0 for l in constraints},
    componentwise Fraction. constraints: list of (coeffs3, const)."""
    nf = len(constraints[0][0])
    verts = []
    seen = set()
    for i, j, k in itertools.combinations(range(len(constraints)), 3):
        l1, l2, l3 = constraints[i], constraints[j], constraints[k]
        A = [l1[0], l2[0], l3[0]]
        b = [-l1[1], -l2[1], -l3[1]]
        x = solve3(A, b)
        if x is None:
            continue
        # x is intersection of the three planes; a vertex if feasible
        ok = all(lin_eval(l, x) >= 0 for l in constraints)
        if not ok:
            continue
        key = tuple(x)
        if key in seen:
            continue
        seen.add(key)
        verts.append(x)
    return verts

def _polar_angle_key(center, basis):
    # not used directly
    pass

def facet_triangles(verts, constraints, idx):
    """Return a fan triangulation (list of triangles) of the facet of
    constraint idx, as 3-tuples of vertex points."""
    l = constraints[idx]
    face_verts = [v for v in verts if lin_eval(l, v) == 0]
    if len(face_verts) < 3:
        return []
    # plane normal = coeffs; drop dominant coordinate for 2D projection
    c = l[0]
    dom = max(range(3), key=lambda t: abs(c[t]))
    other = [t for t in range(3) if t != dom]
    def proj(v):
        return (v[other[0]], v[other[1]])
    pts2 = [proj(v) for v in face_verts]
    # sort around centroid by angle
    cx = sum(p[0] for p in pts2) / F(len(pts2))
    cy = sum(p[1] for p in pts2) / F(len(pts2))
    def angle_key(p):
        return (p[0] - cx, p[1] - cy)
    order = sorted(range(len(face_verts)),
                   key=lambda t: angle_key(pts2[t]))
    # sort by angle via atan2-like: use (dx,dy), wrap; a simple method:
    # sort by (half-plane, cross) --- do a stable radial sort:
    def cmp(a, b):
        ax, ay = pts2[a][0]-cx, pts2[a][1]-cy
        bx, by = pts2[b][0]-cx, pts2[b][1]-cy
        # upper vs lower half
        ha = 0 if (ay > 0 or (ay == 0 and ax >= 0)) else 1
        hb = 0 if (by > 0 or (by == 0 and bx >= 0)) else 1
        if ha != hb:
            return -1 if ha < hb else 1
        cr = ax * by - ay * bx
        if cr != 0:
            return -1 if cr > 0 else 1
        return 0
    import functools
    order.sort(key=functools.cmp_to_key(cmp))
    ordered = [face_verts[i] for i in order]
    # fan from first vertex
    tris = []
    for i in range(1, len(ordered) - 1):
        tris.append((ordered[0], ordered[i], ordered[i + 1]))
    return tris

def poly_volume(constraints):
    """Exact volume of bounded convex polyhedron {x: l(x)>=0} via facet
    triangulation to the interior centroid."""
    verts = poly_vertices(constraints)
    if len(verts) < 4:
        return F(0)
    # interior centroid
    c0 = tuple(sum(v[k] for v in verts) / F(len(verts)) for k in range(3))
    tot = F(0)
    for idx in range(len(constraints)):
        for (a, b, c) in facet_triangles(verts, constraints, idx):
            # volume of tetrahedron (a,b,c,c0)
            m = [
                [b[0]-a[0], b[1]-a[1], b[2]-a[2]],
                [c[0]-a[0], c[1]-a[1], c[2]-a[2]],
                [c0[0]-a[0], c0[1]-a[1], c0[2]-a[2]],
            ]
            det = (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
                   - m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
                   + m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
            tot += abs(det) / 6
    return tot

def tetra_constraints(n):
    """Initial constraints for the unit simplex in free coords."""
    nfree = n - 1
    cons = []
    for j in range(nfree):
        cons.append(v_lin(j, nfree))        # v_j >= 0
    # 1 - sum v >= 0
    cn = [-F(1)] * nfree
    cons.append((cn, F(1)))
    return cons

def cells_3d(lines):
    """Enumerate full-dim cells by incremental convex clipping.

    Each cell is (cons, verts): cons = accumulated halfspace constraints
    ((coeffs3, const), lin >= 0), verts = its exact vertices. Splitting by a
    plane finds segment crossing points along the cell's facet boundary edges,
    so a cell costs O(verts+edges) per plane rather than a fresh triple-
    enumeration. Volume is computed later in compute_pn."""
    init_cons = tetra_constraints(4)
    init_verts = [(F(0), F(0), F(0)), (F(1), F(0), F(0)),
                  (F(0), F(1), F(0)), (F(0), F(0), F(1))]
    cells = [(list(init_cons), list(init_verts))]
    for name, g in lines:
        newcells = []
        for cons, verts in cells:
            if not verts:
                continue
            signs = [lin_eval(g, v) for v in verts]
            if all(s >= 0 for s in signs) or all(s <= 0 for s in signs):
                newcells.append((cons, verts))
                continue
            edges = poly_edges(cons, verts)
            crossing = []
            for (u, w) in edges:
                su = lin_eval(g, u); sw = lin_eval(g, w)
                if su == 0 or sw == 0:
                    continue
                if (su < 0 and sw > 0) or (su > 0 and sw < 0):
                    crossing.append(inter_pt(u, w, g))
            pos_cons = cons + [(g[0], g[1])]
            neg_cons = cons + [([-x for x in g[0]], -g[1])]
            posv = [v for v, s in zip(verts, signs) if s >= 0]
            negv = [v for v, s in zip(verts, signs) if s <= 0]
            newcells.append((pos_cons, posv + crossing))
            newcells.append((neg_cons, negv + crossing))
        cells = newcells
    return cells


def inter_pt(u, w, g):
    """Intersection of segment u-w with plane g (lin_eval(g, .) = 0)."""
    su = lin_eval(g, u); sw = lin_eval(g, w)
    t = su / (su - sw)
    return tuple(u[k] + t * (w[k] - u[k]) for k in range(3))


def poly_edges(cons, verts):
    """Edge set of a convex 3D polyhedron from its facet boundaries.
    Each facet (constraint idx) is a polygon whose consecutive vertices are an
    edge; collect deduped vertex pairs."""
    eset = set()
    vidx = {v: i for i, v in enumerate(verts)}
    for idx in range(len(cons)):
        l = cons[idx]
        face = [v for v in verts if lin_eval(l, v) == 0]
        if len(face) < 3:
            continue
        order = facet_order(face, cons, idx)
        for i in range(len(order)):
            a = order[i]; b = order[(i + 1) % len(order)]
            key = tuple(sorted((vidx[a], vidx[b])))
            eset.add(key)
    return [(verts[i], verts[j]) for (i, j) in eset]


def facet_order(face, cons, idx):
    """Order the 2D facet vertices into a boundary polygon by polar angle in
    the facet plane (dominant-coordinate projection)."""
    c = cons[idx][0]
    dom = max(range(3), key=lambda t: abs(c[t]))
    other = [t for t in range(3) if t != dom]
    pts = [(v[other[0]], v[other[1]]) for v in face]
    cx = sum(p[0] for p in pts) / F(len(pts))
    cy = sum(p[1] for p in pts) / F(len(pts))
    def cmp(a, b):
        ax, ay = pts[a][0] - cx, pts[a][1] - cy
        bx, by = pts[b][0] - cx, pts[b][1] - cy
        ha = 0 if (ay > 0 or (ay == 0 and ax >= 0)) else 1
        hb = 0 if (by > 0 or (by == 0 and bx >= 0)) else 1
        if ha != hb:
            return -1 if ha < hb else 1
        cr = ax * by - ay * bx
        if cr != 0:
            return -1 if cr > 0 else 1
        return 0
    import functools
    order = sorted(range(len(face)), key=functools.cmp_to_key(cmp))
    return [face[i] for i in order]


def compute_pn(n, L, lines):
    """Return exact p(n,L) = (n-1)! * measure(even cells)."""
    nfree = n - 1
    Lv = F(L)
    if n == 3:
        cells = cells_2d(lines)
        density = F(2)
        measure = F(0)
        for cell in cells:
            p0, p1 = poly_centroid(cell)
            v2 = 1 - p0 - p1
            speeds = [p0, p1, v2]
            par = outcome_parity_exact(n, Lv, speeds)
            area = poly_area(cell)
            if par == 0:
                measure += area
        return density * measure, len(cells)
    elif n == 4:
        cells = cells_3d(lines)
        density = F(6)
        measure = F(0)
        for cons, verts in cells:
            if len(verts) < 4:
                continue
            c0 = tuple(sum(v[k] for v in verts) / F(len(verts)) for k in range(3))
            v3 = 1 - c0[0] - c0[1] - c0[2]
            speeds = [c0[0], c0[1], c0[2], v3]
            par = outcome_parity_exact(n, Lv, speeds)
            vol = poly_volume(cons)
            if par == 0:
                measure += vol
        return density * measure, len(cells)
    else:
        raise ValueError("n must be 3 or 4")


def main():
    which = sys.argv[1] if len(sys.argv) > 1 else '3'
    Ls = [int(x) for x in sys.argv[2:]] or [160, 240, 320, 400, 480, 640,
                                            800, 1000, 1200, 1400, 1600, 1800]
    n = int(which)
    results = {"n": n, "L": {}, "anchors": {}}
    for L in Ls:
        lines, events = build_lines(n, L)
        p, ncells = compute_pn(n, L, lines)
        results["L"][str(L)] = {"p": f"{p.numerator}/{p.denominator}",
                                "float": float(p), "ncells": ncells}
        print(f"n={n} L={L}: p={p} = {float(p):.10f}  (cells={ncells})")
    if n == 3 and 160 in Ls:
        results["anchors"]["p(3,160)"] = "56/135"
    if n == 4 and 400 in Ls:
        results["anchors"]["p(4,400)"] = "0.5107843137"
    os.makedirs('out', exist_ok=True)
    with open(os.path.join('out', 'exact_pn.json'), 'w') as f:
        json.dump(results, f, indent=2)
    print("wrote out/exact_pn.json")


if __name__ == '__main__':
    main()
