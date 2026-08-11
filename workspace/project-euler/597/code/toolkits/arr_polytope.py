"""Exact rational convex polytope in free-coordinate form, plus cell slicing.

For PE 597 the speed simplex is parametrized by d = n-1 free coordinates
x = (v0, ..., v_{d-1}) with v_{n-1} = 1 - (v0 + ... + v_{d-1}). A convex
polytope in R^d is stored as H-representation: a list of inequalities
( A_row, b ) meaning A_row . x <= b, all Fractions. The d axes bounds
(x_i >= 0) and the simplex bound (sum x <= 1) are explicit inequalities.

Cell enumeration works by slicing: a new hyperplane a.x = c is folded into a
polytope only when the polytope's vertices lie on both open sides; otherwise
the polytope lies wholly on one side and its sign w.r.t. the hyperplane is
already determined (add nothing). Leaves are polytopes on which every
arrangement hyperplane has constant sign.

Exact area (d=2) and volume (d=3) are computed from the vertices of each leave
polytope, so even-parity cells can be summed with the Dirichlet density.

All arithmetic is Fraction (rational) exact.
"""
from fractions import Fraction as F
from itertools import combinations


def _mul_row(row, vec):
    return sum(a * b for a, b in zip(row, vec))


class Polytope:
    def __init__(self, dim, ineqs):
        """ineqs: iterable of (A_row, b) with A_row length `dim`, b Fraction."""
        self.dim = dim
        self.ineqs = [(tuple(F(c) for c in row), F(b)) for row, b in ineqs]
        self._verts = None

    def copy(self):
        return Polytope(self.dim, self.ineqs)

    def vertices(self):
        """All extreme / tight vertices (exact). Uses every subset of `dim`
        inequalities as a candidate boundary intersection."""
        if self._verts is not None:
            return self._verts
        d = self.dim
        m = len(self.ineqs)
        # candidates: solve d equations from each d-subset, keep those
        # satisfying all inequalities (<=) and that are actually vertices.
        verts = []
        for idxs in combinations(range(m), d):
            A = [self.ineqs[i][0] for i in idxs]
            b = [self.ineqs[i][1] for i in idxs]
            # solve A x = b with Fraction Gaussian elimination
            M = [list(A[i]) + [b[i]] for i in range(d)]
            for col in range(d):
                piv = None
                for r in range(col, d):
                    if M[r][col] != 0:
                        piv = r
                        break
                if piv is None:
                    break
                M[col], M[piv] = M[piv], M[col]
                pv = M[col][col]
                for c in range(col, d + 1):
                    M[col][c] = M[col][c] / pv
                for r in range(d):
                    if r != col and M[r][col] != 0:
                        f = M[r][col]
                        for c in range(col, d + 1):
                            M[r][c] = M[r][c] - f * M[col][c]
            pt = tuple(M[r][d] for r in range(d))
            ok = True
            for (row, bb) in self.ineqs:
                if _mul_row(row, pt) > bb:
                    ok = False
                    break
            if not ok:
                continue
            # vertex = at least d tight inequalities (rank d). Count tight.
            tight = [i for i in range(m) if _mul_row(self.ineqs[i][0], pt) == self.ineqs[i][1]]
            if len(set(tight) & set(idxs)) >= d and pt not in verts:
                verts.append(pt)
        self._verts = verts
        return verts

    def interior_vertex(self):
        """A vertex (used as representative point inside the closed cell)."""
        vs = self.vertices()
        if not vs:
            return None
        return vs[0]

    def eval_affine(self, coeffs, c):
        """Return value of coeffs.x + c at each vertex (list)."""
        out = []
        for v in self.vertices():
            out.append(_mul_row(coeffs, v) + c)
        return out

    def cut(self, coeffs, c, direction):
        """Return a new Polytope restricted to coeffs.x + c <= 0  (direction<0)
        or  coeffs.x + c >= 0 (direction>0)."""
        row = tuple(F(a) for a in coeffs)
        if direction < 0:
            new_ineq = (tuple(-a for a in row), -F(c))   # -row.x <= -c i.e. row.x>=c? no:
            # want row.x + c <= 0  <=>  row.x <= -c
            new_ineq = (row, -F(c))
        else:
            # row.x + c >= 0 <=> -row.x <= c
            new_ineq = (tuple(-a for a in row), F(c))
        return Polytope(self.dim, self.ineqs + [new_ineq])

    def area2(self):
        """Exact polygon area (d=2) via shoelace over CCW-ordered vertices."""
        vs = self.vertices()
        if len(vs) < 3:
            return F(0)
        # order by angle around centroid
        cx = sum(v[0] for v in vs) / len(vs)
        cy = sum(v[1] for v in vs) / len(vs)
        import math
        vs = sorted(vs, key=lambda v: math.atan2(float(v[1] - cy), float(v[0] - cx)))
        s = F(0)
        for i in range(len(vs)):
            x1, y1 = vs[i]
            x2, y2 = vs[(i + 1) % len(vs)]
            s += x1 * y2 - y1 * x2
        return abs(s) / 2

    def volume3(self):
        """Exact volume (d=3) of convex hull of vertices, by decomposition into
        tetrahedra from an interior point."""
        vs = self.vertices()
        if len(vs) < 4:
            return F(0)
        # Use scipy ConvexHull to get the correct triangular facet
        # triangulation of the polyhedron (robust for polygonal faces), then
        # compute exact tetra volumes from the exact Fraction vertices.
        try:
            from scipy.spatial import ConvexHull
        except ImportError:
            raise RuntimeError("scipy required for volume3")
        pts = [[float(v[0]), float(v[1]), float(v[2])] for v in vs]
        hull = ConvexHull(pts)
        # interior point
        n = len(vs)
        c = tuple(sum(v[i] for v in vs) / n for i in range(3))
        vol = F(0)
        for simplex in hull.simplices:
            a, b, cc = (vs[t] for t in simplex)
            m = [
                [a[0] - c[0], a[1] - c[1], a[2] - c[2]],
                [b[0] - c[0], b[1] - c[1], b[2] - c[2]],
                [cc[0] - c[0], cc[1] - c[1], cc[2] - c[2]],
            ]
            det = (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                   - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                   + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
            vol += abs(det)
        return vol / 6

    def volume(self):
        d = self.dim
        if d == 2:
            return self.area2()
        elif d == 3:
            return self.volume3()
        else:
            raise NotImplementedError(f"volume only for d in {{2,3}}, got {d}")
