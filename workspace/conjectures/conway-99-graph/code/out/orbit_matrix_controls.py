"""Orbit-matrix checker for the Conway 99-graph controls.

Verifies the orbit-matrix machinery (code/lib/srg.py::orbit_matrix) on the
two positive controls, rook(3)=srg(9,4,1,2) and bvls_graph()=srg(243,22,1,2),
under a Z2 involution and a Z3 rotation each control possesses.

For each (control, automorphism) we check, in exact integer arithmetic:
  (a) orbit-matrix row sums reproduce the degree k (4 and 22);
  (b) the orbit matrix is constant on orbits (checked per-vertex);
  (c) the De Winter-Kamischke-Wang congruence
          k - s = -s*f + g   (mod sqrt(Delta))
      i.e. (k - s) - (-s*f + g) is divisible by sqrt(Delta),
      where f = # fixed vertices, g = # vertices mapped to an adjacent
      vertex, s = negative eigenvalue (rook s=-2, bvls s=-5).

Automorphisms, constructed by inspection from each graph's structure:
  rook(3): vertices = cells (i,j) of the 3x3 grid, index 3i+j.
      Z2  = transpose  (i,j) -> (j,i)   [order 2]
      Z3  = row shift  (i,j) -> ((i+1)%3, j)  [order 3]
  bvls(243): vertices = syndromes in F3^5 (product order, index
      s0*81+s1*27+s2*9+s3*3+s4); adjacency iff difference is +/- a column of H.
      Z3  = translation s -> s + a, a=(1,0,0,0,0)   [order 3]
      Z2  = negation     s -> -s                    [order 2] (maps each column
            c_j to -c_j in {+/- columns}, so preserves adjacency)
Each is checked to be a genuine automorphism (adjacency preserved) before use.
"""
import numpy as np
from lib.srg import (rook, bvls_graph, is_srg,
                     orbit_matrix, orbit_matrix_is_constant)


# ---------------------------------------------------------------------------
# Automorphisms by inspection

def rook_z2():
    """(i,j)->(j,i); index 3i+j -> 3j+i."""
    g = [0] * 9
    for i in range(3):
        for j in range(3):
            g[3 * i + j] = 3 * j + i
    return g


def rook_z3():
    """(i,j)->((i+1)%3, j); index 3i+j -> 3*((i+1)%3)+j."""
    g = [0] * 9
    for i in range(3):
        for j in range(3):
            g[3 * i + j] = 3 * ((i + 1) % 3) + j
    return g


def _prod_idx(s):
    return s[0] * 81 + s[1] * 27 + s[2] * 9 + s[3] * 3 + s[4]


def bvls_z3():
    """Translation by a=(1,0,0,0,0) in F3^5 (order 3)."""
    a = (1, 0, 0, 0, 0)
    g = [0] * 243
    for s0 in range(3):
        for s1 in range(3):
            for s2 in range(3):
                for s3 in range(3):
                    for s4 in range(3):
                        s = (s0, s1, s2, s3, s4)
                        t = tuple((s[k] + a[k]) % 3 for k in range(5))
                        g[_prod_idx(s)] = _prod_idx(t)
    return g


def bvls_z2():
    """Negation s->-s in F3^5 (order 2)."""
    g = [0] * 243
    for s0 in range(3):
        for s1 in range(3):
            for s2 in range(3):
                for s3 in range(3):
                    for s4 in range(3):
                        s = (s0, s1, s2, s3, s4)
                        t = tuple((-s[k]) % 3 for k in range(5))
                        g[_prod_idx(s)] = _prod_idx(t)
    return g


# ---------------------------------------------------------------------------
# Helpers

def is_automorphism(A, g):
    """True iff g is a genuine automorphism of A (adjacency preserved)."""
    n = A.shape[0]
    for v in range(n):
        for w in range(n):
            if A[g[v], g[w]] != A[v, w]:
                return False
    return True


def order(g):
    """Order of permutation g as a function (exact integer)."""
    n = len(g)
    seen = [False] * n
    o = 1
    for v in range(n):
        if not seen[v]:
            u = v
            cyc = 0
            while not seen[u]:
                seen[u] = True
                cyc += 1
                u = g[u]
            from math import lcm
            o = lcm(o, cyc)
    return o


def f_and_g(A, g):
    """f = # fixed vertices; g = # vertices mapped to an adjacent vertex."""
    n = A.shape[0]
    f = sum(1 for v in range(n) if g[v] == v)
    gcount = sum(1 for v in range(n) if A[v, g[v]] == 1)
    return f, gcount


def congruence(A, v, k, s, lam, mu, g):
    """Check (k-s) - (-s*f + g) divisible by sqrt(Delta). Returns (ok, f, g, rem)."""
    Delta = (lam - mu) ** 2 + 4 * (k - mu)
    root = int(round(Delta ** 0.5))
    assert root * root == Delta, f"Delta={Delta} not a perfect square"
    f, gc = f_and_g(A, g)
    lhs = k - s
    rhs = (-s) * f + gc
    diff = lhs - rhs
    return (diff % root == 0), f, gc, diff, root


def run_control(name, A, v, k, s, lam, mu, autos):
    print(f"=== {name}: srg({v},{k},{lam},{mu}), negative eigenvalue s={s} ===")
    # sanity: degree reproduces k
    degs = A.sum(axis=1)
    print(f"  sanity degree check: min deg = {degs.min()}, max deg = {degs.max()}, expected k={k}",
          "OK" if (degs.min() == degs.max() == k) else "FAIL")
    print(f"  sanity is_srg: {is_srg(A, v, k, lam, mu)[0]}")
    for label, g in autos:
        print(f"  --- automorphism '{label}' order={order(g)} "
              f"(genuine automorphism: {is_automorphism(A, g)})")
        orbits, lengths, M = orbit_matrix(A, g)
        print(f"      orbit count = {len(orbits)}, orbit lengths = {list(lengths)}")
        # (a) row sums reproduce degree
        rowsums = M.sum(axis=1)
        print(f"      (a) orbit-matrix row sums all equal degree k={k}:",
              "OK" if all(rs == k for rs in rowsums) else f"FAIL {list(rowsums)}")
        # (b) entries constant on orbits
        ok_c, rep = orbit_matrix_is_constant(M, A, g)
        print(f"      (b) orbit matrix constant on orbits: {ok_c}  [{rep}]")
        print(f"      orbit matrix M ({len(orbits)}x{len(orbits)}):")
        for row in M.tolist():
            print("         " + " ".join(f"{x:2d}" for x in row))
        # (c) De Winter-Kamischke-Wang congruence
        ok_cong, f, gc, diff, root = congruence(A, v, k, s, lam, mu, g)
        print(f"      (c) f(fixed)={f}, g(mapped-to-adjacent)={gc}")
        print(f"          Delta=(lam-mu)^2+4(k-mu)=({lam}-{mu})^2+4({k}-{mu}) "
              f"-> {root * root}, sqrt(Delta)={root}")
        print(f"          (k-s)-(-s*f+g) = ({k}-({s})) - ({-s}*{f}+{gc}) = "
              f"{k - s - ((-s) * f + gc)}")
        print(f"          DKW congruence k-s ≡ -s*f+g (mod {root}):",
              "OK  (divisible)" if ok_cong else "FAIL  (residue != 0)")
    print()


if __name__ == "__main__":
    R = rook(3)
    run_control("rook(3)", R, 9, 4, -2, 1, 2,
                [("Z2 transpose", rook_z2()), ("Z3 row-shift", rook_z3())])

    B = bvls_graph()
    run_control("bvls_graph()", B, 243, 22, -5, 1, 2,
                [("Z2 negation", bvls_z2()), ("Z3 translation", bvls_z3())])
