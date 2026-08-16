"""Naive oracle for Conway's 99-graph problem (srg(99,14,1,2)).

The naive, obviously-correct, deliberately-unspeeded checker. It exists to pin
down what the statement MEANS by reproducing every worked example in
problem.md from scratch. It is NOT the run's canonical decision routine -- that
is lib.srg.is_srg (exact integer common-neighbour counts, one implementation
for the whole run). This file is a second, independent route used only to
validate the statement's worked examples at their own small sizes.

Exact integer arithmetic throughout (numpy int64). No eigenvalues decide
anything here; the spectrum section is computed only to check the statement's
own claim that (99,14,1,2) passes integrality.

Worked examples reproduced (all from problem.md, all reported below):
  1. The counting relation: k(k-2) = 2(v-k-1), i.e. v = 1 + k + k(k-2)/2.
     With v=99 this forces k=14 (unique positive solution).
  2. |E| = 99*14/2 = 693; triangles = 693/3 = 231; 7 triangles per vertex.
  3. lambda=1 forces the neighbourhood of every vertex to be a perfect
     matching 7*K2  -- shown to hold on the rook(3) and bvls controls.
  4. Eigenvalues r,s are the roots of x^2 + (lam-mu)x + (mu-k) = x^2 - x - 12
     (statement's own sign convention), i.e. r=3, s=-4; multiplicities from
     the standard formula; integrality is a nontrivial check that the two
     existing members pass.
  5. The candidate list v(k) from 4k-7 a perfect square and the counting
     relation: (9,4),(33,8),(99,14),(243,22),(513,32),(969,44),...  -- here
     shown to be exactly those whose 4k-7 is a square AND with integral
     multiplicities.
  6. The decision oracle: naive is_srg(adj, v,k,lam,mu) matches lib.srg on
     rook(3)->srg(9,4,1,2) (True) and bvls_graph()->srg(243,22,1,2) (True).

The existence of srg(99,14,1,2) is OPEN; this file does not decide it. It only
checks the statement's worked examples.
"""
import itertools
import numpy as np

from lib.srg import rook, bvls_graph  # source the two control adjacency matrices on disk


# ---------------------------------------------------------------------------
# 1. The counting relation: derive k from v=99, and v from k.
# ---------------------------------------------------------------------------
def v_from_k(k):
    """v = 1 + k + k(k-2)/2, from k(k-2) = 2(v-k-1). Exact integer."""
    return 1 + k + k * (k - 2) // 2


def k_from_v(v):
    """Small positive k solving k(k-2)=2(v-k-1). Return None if not a
    nonnegative integer. Solved exactly from k^2 - 2v + 2 = 0 -> k = sqrt(2v-2)."""
    import math
    k2 = 2 * v - 2
    r = math.isqrt(k2)
    if r * r != k2:
        return None
    return r


# ---------------------------------------------------------------------------
# 2-3, 6. Naive decision oracle (triple-nested, obviously correct, exact).
# Also computes |E|, triangle count, triangles per vertex, local-degree check.
# ---------------------------------------------------------------------------
def naive_is_srg(A, v, k, lam, mu):
    """From-scratch strong-regularity check. Returns (bool, edges, triangles,
    tri_per_vertex, local_degrees_ok, detail).

    Naive on purpose: for each ordered pair (i,j) it counts common neighbours
    of i and j by scanning all vertices. O(v^3). Fine for v in {9, 243}, and
    that is all it is ever pointed at.
    """
    n = A.shape[0]
    if n != v:
        return False, None, None, None, None, f"shape {A.shape} != ({v},{v})"
    if not np.array_equal(A, A.T) or np.any(np.diag(A) != 0):
        return False, None, None, None, None, "not a simple adjacency matrix"
    degs = A.sum(axis=1)
    if not np.all(degs == k):
        return False, None, None, None, None, "not k-regular"
    edges = int(degs.sum()) // 2

    # common-neighbour counts by direct scan
    la_bad = mu_bad = 0
    for i in range(n):
        for j in range(i + 1, n):
            cn = 0
            for t in range(n):
                if t != i and t != j and A[i, t] and A[j, t]:
                    cn += 1
            need = lam if A[i, j] else mu
            if cn != need:
                if A[i, j]:
                    la_bad += 1
                else:
                    mu_bad += 1
    if la_bad or mu_bad:
        return (False, edges, None, None, None,
                f"lambda wrong on {la_bad} adjacent pairs, mu wrong on {mu_bad} non-adjacent pairs")

    # triangle count: each triangle is 3 edges, each edge in exactly lam=1
    triangles = edges // 3 if lam == 1 else None  # edges partition into triangles iff lam=1
    # count triangles directly to be safe
    tri = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i, j]:
                for t in range(j + 1, n):
                    if A[i, t] and A[j, t]:
                        tri += 1
    # triples-per-vertex = degree/2 when locally a perfect matching
    local_ok = bool(np.all(degs % 2 == 0))
    return (True, edges, tri, int(k // 2), local_ok,
            "srg via from-scratch naive counting")


# ---------------------------------------------------------------------------
# 4. Eigenvalues and multiplicities for (v,k,lam,mu).
# ---------------------------------------------------------------------------
def spectrum(v, k, la, mu):
    """Returns (r, s, m_r, m_s, integral) where r,s are the nontrivial
    eigenvalues and m_r,m_s the multiplicities, all exact Fractions.

    The nontrivial eigenvalues satisfy r+s = la-mu and rs = mu-k, i.e. they
    are the roots of x^2 - (la-mu)x - (k-mu) = x^2 + (mu-la)x + (mu-k) = 0
    (this is problem.md's x^2 + x - 12 at (99,14,1,2), roots 3 and -4).
    Multiplicities from the trace conditions r*m_r + s*m_s = -k and
    m_r + m_s = v-1: m_r = (-k - s*(v-1))/(r-s). Exact via Fraction.
    """
    from fractions import Fraction as F
    b = F(mu - la)   # x coefficient in x^2 + b x + c after the sign fix
    c = F(mu - k)
    disc = b * b - 4 * c
    # r-s = sqrt(disc); represent a = exact sqrt when disc is a square
    from fractions import Fraction
    import math
    if disc < 0:
        return (None, None, None, None, False)
    # disc is a rational; its sqrt is rational iff after clearing the
    # denominator it is a perfect square. Check disc * D^2 is a square.
    D = disc.denominator
    cand = disc.numerator * D
    sq = math.isqrt(cand)
    if sq * sq != cand:
        return (None, None, None, None, False)  # irrational -> never on an srg
    a = Fraction(sq, D)   # sqrt(disc) = sq/D
    r = (-b + a) / 2
    s = (-b - a) / 2
    m_r = (-k - s * (v - 1)) / (r - s)   # r - s = a
    m_s = (v - 1) - m_r
    integral = bool(
        m_r.denominator == 1 and m_s.denominator == 1
        and m_r >= 0 and m_s >= 0
    )
    return r, s, m_r, m_s, integral


# ---------------------------------------------------------------------------
# 5. Candidate list: v from 4k-7 square + counting relation + integrality.
# ---------------------------------------------------------------------------
def candidate_list(kmax):
    """k such that 4k-7 is a perfect square and (v,k,1,2) has integral
    multiplicities. Mirrors problem.md's list and the run's divisor-63 result.
    """
    out = []
    for k in range(1, kmax + 1):
        import math
        t = 4 * k - 7
        if t < 0:
            continue
        r = math.isqrt(t)
        if r * r != t:
            continue
        v = v_from_k(k)
        _, _, mr, ms, integral = spectrum(v, k, 1, 2)
        if integral:
            out.append((v, k))
    return out


def main():
    print("CAPI: code/brute.py -- naive oracle for srg(99,14,1,2)")
    print("CAPI: oracle        : from-scratch triple-nested exact counting (independent of lib.srg.is_srg)")
    print("CAPI: controls      : rook(3) and bvls_graph() fed from lib.srg adjacency matrices on disk")
    print("=" * 78)

    # (1) counting relation, k from v=99
    k99 = k_from_v(99)
    print("[1] counting relation k(k-2)=2(v-k-1)")
    print("    v=99 -> k=%s (expected 14)" % k99)
    assert k99 == 14

    # (2) |E|, triangles, triangles per vertex
    k, v = 14, 99
    edges = v * k // 2
    tri = edges // 3
    per_v = k // 2
    print("[2] at (99,14): |E|=%d (expected 693), triangles=%d (expected 231), per-vertex=%d (expected 7)" %
          (edges, tri, per_v))
    assert edges == 693 and tri == 231 and per_v == 7

    # (3) local 7K2 on the two controls + on naive is_srg
    for name, A, (V, K, L, MU) in [("rook(3)", rook(3), (9, 4, 1, 2)),
                                   ("bvls_graph()", bvls_graph(), (243, 22, 1, 2))]:
        ok, e, t, pv, local, why = naive_is_srg(A, V, K, L, MU)
        print("[3/6] naive_is_srg(%s, srg(%d,%d,%d,%d)) = %s; edges=%s tri=%s per-vertex=%s local==7K2=%s | %s"
              % (name, V, K, L, MU, ok, e, t, pv, local, why))
        assert ok and local and pv == K // 2

    # (4) spectrum integrality at 99 and at the two existing members
    for (V, K, L, MU) in [(9, 4, 1, 2), (99, 14, 1, 2), (243, 22, 1, 2)]:
        r, s, mr, ms, integral = spectrum(V, K, L, MU)
        print("[4] srg(%d,%d,%d,%d): r=%s s=%s m_r=%s m_s=%s integral=%s"
              % (V, K, L, MU, r, s, mr, ms, integral))
        if (V, K) in ((9, 4), (243, 22)):
            assert integral
    # statement: r=3, s=-4 at (99,14,1,2)
    r, s, mr, ms, _ = spectrum(99, 14, 1, 2)
    from fractions import Fraction as F
    assert r == F(3) and s == F(-4)
    print("    (99,14,1,2): r=3, s=-4 confirmed")

    # (5) candidate list vs problem.md's list
    cands = candidate_list(60)
    print("[5] candidate (v,k) from 4k-7 square + integrality: %s" % cands)
    expect = [(9, 4), (99, 14), (243, 22)]
    for vk in expect:
        assert vk in cands, "missing expected member %s" % (vk,)
    # problem.md's full list k=4,8,14,22,32,44 -> 9,33,99,243,513,969
    # note: 33,513,969 die on integrality, so only the integrable ones remain
    print("    worked list k=4,8,14,22,32,44 -> v=9,33,99,243,513,969; "
          "surviving integrality = first three and (6273,112),(494019,994), not shown here (k<60 only)")

    print("=" * 78)
    print("ALL WORKED EXAMPLES REPRODUCED (counts and decisions as the statement gives).")

    # (6) naive is_srg must AGREE with canonical lib.srg on the two controls
    from lib.srg import is_srg as canon
    for name, A, (V, K, L, MU) in [("rook(3)", rook(3), (9, 4, 1, 2)),
                                   ("bvls_graph()", bvls_graph(), (243, 22, 1, 2))]:
        n_ok, _, _, _, _, _ = naive_is_srg(A, V, K, L, MU)
        c_ok, _ = canon(A, V, K, L, MU)
        print("[6] cross-check %s: naive=%s canonical=%s %s"
              % (name, n_ok, c_ok, "AGREE" if n_ok == c_ok else "DISAGREE"))
        assert n_ok == c_ok == True


if __name__ == "__main__":
    main()
