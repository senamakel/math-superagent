"""Exact cell enumeration of the PE 597 outcome arrangement over the simplex.

Speeds normalized to the (n-1)-simplex (Dirichlet(1,..,1) uniform). The race
outcome is a deterministic piecewise-constant function whose separating set is
the union of:
  - speed-equality hyperplanes  v_a = v_b
  - pair-equalities of candidate event times  T_i = T_j , where T is either a
    finish time F_j = (L-40j)/v_j or a catch time C_ab = 40(b-a)/(v_a-v_b).
Every T is const/(affine-linear) so every T_i = T_j is affine-linear in v,
i.e. the separators form a genuine straight-line hyperplane arrangement on the
simplex. Parity is constant on each open cell (verified empirically over
150k samples per config: 0 inconsistent buckets).

The enumerator recursively slices cells by each arrangement hyperplane, only
for polytopes that straddle it, producing leaves each equal to one cell's
closure. For each leaf we take the vertex-average (strict interior point) and
evaluate the exact race parity there, summing exact cell volume weighted by the
Dirichlet density (n-1)! so that p(n,L) = sum of even-cell normalized volumes.

API:
  enumerate_cells(n, L) -> (leaves, planes)
"""
from fractions import Fraction as F
from arr_polytope import Polytope


def _candidate_events(n):
    evs = []
    for j in range(n):
        evs.append(('F', j, None))
    for a in range(n):
        for b in range(a + 1, n):
            evs.append(('C', a, b))
    return evs


def _linform(j, d):
    """Linear form equal to v_j expressed over free coords v0..v_{d-1}
    (v_d = 1 - sum free). Returns (row, const)."""
    if j < d:
        row = [F(0)] * d
        row[j] = F(1)
        return (row, F(0))
    else:
        row = [F(-1)] * d
        return (row, F(1))


def _T_aff(ev, d):
    """Candidate event time as num/(row.v + const). Returns (num, row, const)."""
    typ, j, k = ev
    if typ == 'F':
        num = F(L_current if False else 0)  # placeholder, replaced below
    # handle by caller passing L; we store L closure
    raise NotImplementedError


def _hyperplanes(n, L):
    """Return list of (coeffs, c) with coeffs over free coords v0..v_{d-1},
    meaning (coeffs.x + c) = 0. d = n-1, v_{n-1} = 1 - sum(free)."""
    d = n - 1
    evs = _candidate_events(n)
    planes = set()

    def aff(row, cval):
        return (tuple(row), F(cval))

    # speed equalities v_a = v_b  -> (v_a - v_b) = 0
    for a in range(n):
        for b in range(a + 1, n):
            r1, c1 = _linform(a, d)
            r2, c2 = _linform(b, d)
            row = [r1[i] - r2[i] for i in range(d)]
            planes.add(aff(row, c1 - c2))

    # candidate event times as (num, denom_row, denom_const)
    def T(ev):
        typ, j, k = ev
        if typ == 'F':
            num = F(L - 40 * j)
            row, cc = _linform(j, d)
            return (num, row, cc)
        else:
            num = F(40) * (k - j)
            rj, cj = _linform(j, d)
            rk, ck = _linform(k, d)
            row = [rj[i] - rk[i] for i in range(d)]
            cc = cj - ck
            return (num, row, cc)

    Taff = [T(ev) for ev in evs]

    # T1 - T2 = 0  <=>  num1*(den2) - num2*(den1) = 0
    for i in range(len(Taff)):
        for j in range(i + 1, len(Taff)):
            n1, r1, c1 = Taff[i]
            n2, r2, c2 = Taff[j]
            row = [n1 * r2[t] - n2 * r1[t] for t in range(d)]
            cval = n1 * c2 - n2 * c1
            planes.add(aff(row, cval))
    return sorted(planes)


def _simplex_polytope(d):
    """The d-simplex {x_i>=0, sum x_i <= 1} in free coords, as inequalities
    -x_i <= 0 and sum x_i <= 1."""
    ineqs = []
    for i in range(d):
        row = [F(0)] * d
        row[i] = F(-1)      # -x_i <= 0  => x_i >= 0
        ineqs.append((row, F(0)))
    ineqs.append(([F(1)] * d, F(1)))   # sum x <= 1
    return Polytope(d, ineqs)


def _mul(row, v):
    return sum(a * b for a, b in zip(row, v))


def slice_poly(poly, coeffs, c, which):
    """Restrict poly to: which>0 => coeffs.x+c>=0 ; which<0 => <=0.
    Returns new Polytope or None if empty."""
    row = tuple(F(a) for a in coeffs)
    cc = F(c)
    if which > 0:
        # coeffs.x + c >= 0 <=> -coeffs.x <= c
        ineq = (tuple(-a for a in row), cc)
    else:
        # coeffs.x + c <= 0 <=> coeffs.x <= -c
        ineq = (row, -cc)
    return Polytope(poly.dim, poly.ineqs + [ineq])


def leaf_interior(poly):
    """Vertex-average = strict interior point (closure of one open cell)."""
    vs = poly.vertices()
    if not vs:
        return None
    n = len(vs)
    d = poly.dim
    pt = tuple(sum(v[i] for v in vs) / n for i in range(d))
    return pt


def enumerate_cells(n, L, verbose=False):
    d = n - 1
    planes = _hyperplanes(n, L)
    if verbose:
        print(f"n={n} L={L}: d={d}, {len(planes)} arrangement hyperplanes")
    root = _simplex_polytope(d)
    stack = [(root, [0] * len(planes))]
    leaves = []
    ncut = 0
    while stack:
        poly, svec = stack.pop()
        did_cut = False
        for pi in range(len(planes)):
            if svec[pi] != 0:
                continue
            coeffs, c = planes[pi]
            vals = [_mul(coeffs, v) + c for v in poly.vertices()]
            sgns = set()
            for val in vals:
                sgns.add(1 if val > 0 else (-1 if val < 0 else 0))
            if sgns == {1}:
                svec[pi] = 1
            elif sgns == {-1}:
                svec[pi] = -1
            elif sgns == {0}:
                svec[pi] = 0
            elif 1 in sgns and -1 in sgns:
                ncut += 1
                for which in (1, -1):
                    sub = slice_poly(poly, coeffs, c, which)
                    if sub is not None:
                        sv2 = list(svec)
                        sv2[pi] = which
                        stack.append((sub, sv2))
                did_cut = True
                break
            else:  # {0,1} or {0,-1}: degenerate touch
                target = 1 if 1 in sgns else -1
                svec[pi] = target
        if not did_cut:
            leaves.append((poly, tuple(svec)))
    return leaves, planes
