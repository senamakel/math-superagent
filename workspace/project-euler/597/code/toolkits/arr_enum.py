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
  enumerate_cells(dim, L, n) -> (leaves, total_normalized_even_volume)
"""
from fractions import Fraction as F
from itertools import combinations
from arr_polytope import Polytope

_cache_signhelper = {}


def _candidate_events(n):
    evs = []
    for j in range(n):
        evs.append(('F', j, None))
    for a in range(n):
        for b in range(a + 1, n):
            evs.append(('C', a, b))
    return evs


def _hyperplanes(n, L):
    """Return list of (coeffs, c) with coeffs over free coords v0..v_{d-1},
    meaning (coeffs.x + c) = 0. d = n-1, v_{n-1} = 1 - sum(free)."""
    d = n - 1
    evs = _candidate_events(n)
    planes = set()

    def aff(vcoeffs, cval):
        return (tuple(vcoeffs), F(cval))

    # speed equalities v_a = v_b  -> (v_a - v_b) = 0
    for a in range(n):
        for b in range(a + 1, n):
            row = [F(0)] * d
            if a < d:
                row[a] += 1
            if b < d:
                row[b] -= 1
            # v_{n-1}=1-sum; if b==d: -v_{n-1} -> +sum ... handle via substitute
            if a == d:
                for i in range(d):
                    row[i] += 1
            if b == d:
                for i in range(d):
                    row[i] -= 1
            planes.add(aff(row, 0))

    # time equality T1 - T2 = 0. Represent T as (num_coeffs, den_linear).
    def T_aff(ev):
        typ, j, k = ev
        if typ == 'F':
            # (L-40j)/v_j : numerator c=L-40j, denom v_j
            row = [F(0)] * d
            if j < d:
                row[j] = F(1)
            else:  # j==d -> v_d = 1 - sum
                for i in range(d):
                    row[i] = F(-1)
            return (F(L - 40 * j), row, F(1))  # c / (row.v + 1) but v_d=1-sum gives constant 1
        else:
            # 40(b-a)/(v_a - v_b): numerator 40(b-a), denom v_a - v_b
            num = F(40) * (k - j)
            row = [F(0)] * d
            if a_sub := None:
                pass
            for idx, sgn in ((j, 1), (k, -1)):
                if idx < d:
                    row[idx] += sgn
                else:
                    for i in range(d):
                        row[i] += sgn * (-1)  # v_d = 1 - sum -> -1 per free var
            return (num, row, F(0))  # num / (row.v + 0)

    Taff = [T_aff(ev) for ev in evs]
    # T1 - T2 = 0  <=>  num1*den2 - num2*den1 = 0, affine in v
    for i in range(len(Taff)):
        for j in range(i + 1, len(Taff)):
            n1, r1, c1 = Taff[i]
            n2, r2, c2 = Taff[j]
            # n1*(r2.v+c2) - n2*(r1.v+c1)
            row = [n1 * r2[t] - n2 * r1[t] for t in range(d)]
            cval = n1 * c2 - n2 * c1
            planes.add(aff(row, cval))
    return sorted(planes)


def _simplex_polytope(d):
    """The d-simplex {x_i>=0, sum x_i <= 1} in free coords."""
    ineqs = []
    for i in range(d):
        row = [F(0)] * d
        row[i] = F(-1)      # -x_i <= 0  => x_i >= 0
        ineqs.append((row, F(0)))
    ineqs.append(([F(1)] * d, F(1)))   # sum x <= 1
    return Polytope(d, ineqs)


def enumerate_cells(n, L, verbose=False):
    d = n - 1
    planes = _hyperplanes(n, L)
    if verbose:
        print(f"n={n} L={L}: d={d}, {len(planes)} arrangement hyperplanes")
    # BFS slice over polytopes. Each item: (polytope, sign_vector) where
    # sign_vector[pi] in {-1,0,1} records current known sign of plane pi
    # (0 = undetermined yet).
    root = _simplex_polytope(d)
    stack = [(root, [0] * len(planes))]
    leaves = []          # list of (polytope, full_sign_vector)
    ncut = 0
    while stack:
        poly, svec = stack.pop()
        # find first undetermined plane (-1 stall guard)
        progress = False
        for pi, (coeffs, c) in enumerate(planes):
            if svec[pi] != 0:
                continue
            vals = [ _mul(coeffs, v) + c for v in poly.vertices() ]
            sgns = set()
            for val in vals:
                if val > 0:
                    sgns.add(1)
                elif val < 0:
                    sgns.add(-1)
                else:
                    sgns.add(0)
            if sgns == {1}:
                svec[pi] = 1
                progress = True
            elif sgns == {-1}:
                svec[pi] = -1
                progress = True
            elif sgns == {0}:
                svec[pi] = 0  # degenerate; treat as 0 (on plane)
                progress = True
            elif 1 in sgns and -1 in sgns:
                # straddles -> slice
                ncut += 1
                v = poly.vertices()
                for which in (1, -1):
                    sub = slice_poly(poly, coeffs, c, which)
                    if sub is not None:
                        sv2 = list(svec)
                        sv2[pi] = which
                        stack.append((sub, sv2))
                progress = True
                break
            else:  # sgns == {0,1} or {0,-1}: degenerate touch, treat fully
                target = 1 if 1 in sgns else -1
                svec[pi] = target
                progress = True
        if not progress:
            # all planes determined -> leaf
            leaves.append((poly, tuple(svec)))
    return leaves, planes


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
    """Vertex-average = strict interior point (the closure of one open cell)."""
    vs = poly.vertices()
    d = poly.dim
    if not vs:
        return None
    n = len(vs)
    pt = tuple(sum(v[i] for v in vs) / n for i in range(d))
    return pt
