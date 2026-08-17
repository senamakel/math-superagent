"""Validate the srg-quotient orbit-matrix equation on the BvLS control.

An automorphism phi of order 3, fixed-point-free, acting on an srg(v,k,lam,mu)
gives an orbit matrix M (m x m, m = v/3 orbits, all point-orbits of length 3)
with A P = P M (P = orbit indicator), and the srg equation A^2 = kI + lam*A +
mu*(J-I-A) pulled back yields the NECESSARY condition

      M^2 = (k-mu) I + (lam-mu) M + mu * n_j   (constant row mu*n_j = mu*3)

i.e.  M^2_ij = (k-mu) delta_ij + (lam-mu) M_ij + mu*3  for all i,j.

GATE (directive 27.2): before ANY 99 verdict is believed, this encoder/equation
must be validated to recover BvLS's genuine order-3 (translation) action. BvLS
is srg(243,22,1,2): k=22, lam=1, mu=2, so it must satisfy M^2 = 20 I - M + 6 J33
(here row count m = 81, all-one matrix J shape 81x81, and off-eigenvalues mu*n=6).

We compute the ACTUAL orbit matrix of the bvls_z3 translation (from
lib.srg.orbit_matrix) and check the equation in exact integer arithmetic. If it
holds, the orbit-matrix/quotient machinery is validated on a real positive
control; the SAME code path then applies to the 99 case.

Ring: exact integer arithmetic (numpy int64 + Python int). No floats.
"""
import numpy as np
from lib.srg import bvls_graph, orbit_matrix, orbit_matrix_is_constant

# ---- reuse the order-3 translation automorphism on BvLS ----
def _prod_idx(s):
    return s[0] * 81 + s[1] * 27 + s[2] * 9 + s[3] * 3 + s[4]

def bvls_z3():
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

def check_orbit_equation(C, k, mu):
    """C is m x m (not yet an orbit matrix). Check C^2 = (k-mu)I + (0)M + mu*3 J."""
    m = C.shape[0]
    J = np.ones((m, m), dtype=np.int64)
    C2 = C @ C
    rhs = (k - mu) * np.eye(m, dtype=np.int64) - C + mu * 3 * J   # lam-mu = -1 here (lam=1,mu=2)
    # NOTE: lam-mu = -1 for this family, so the M term is -M.
    diff = C2 - rhs
    return bool(np.all(diff == 0)), int(np.max(np.abs(diff))), m

def main():
    A = bvls_graph()
    v, k, lam, mu = 243, 22, 1, 2
    g = bvls_z3()
    print("=== GATE: validate the orbit-matrix srg-quotient equation on BvLS ===")
    print("BvLS is_srg(243,22,1,2):", __import__('lib.srg', fromlist=['is_srg']).is_srg(A, v, k, lam, mu)[0])
    print("z3 translation is a genuine automorphism:", _is_aut(A, g))

    orbits, lengths, M = orbit_matrix(A, g)
    m = len(orbits)
    print(f"orbits = {m}, all lengths equal 3: {set(lengths) == {3}}")
    print(f"orbit matrix row sums all = k={k}:",
          bool(np.all(M.sum(axis=1) == k)), list(M.sum(axis=1))[:3], "...")
    ok_const, rep = orbit_matrix_is_constant(M, A, g)
    print("orbit matrix constant on orbits:", ok_const, f"[{rep}]")

    # the equation, lam-mu = -1
    ok, maxdiff, m2 = check_orbit_equation(M, k, mu)
    print(f"\nCheck  M^2 = (k-mu)I + (lam-mu)M + mu*3*J   with k={k},lam={lam},mu={mu}")
    print(f"  -> M^2 = {k-mu} I - M + {mu*3} J  (lam-mu = {lam-mu})")
    print(f"  EQUATION HOLDS: {ok}   (max |entry diff| = {maxdiff}, m={m2})")

    # Also verify symmetry & diagonal structure (3-vertex orbits: diag in {0,2})
    diag = np.diag(M)
    print(f"  M symmetric: {bool(np.all(M == M.T))}")
    print(f"  diagonal values (must be in {{0,2}} for 3-vertex orbit): "
          f"{sorted(set(diag.tolist()))}")

    # eigenvalue sanity: off the all-ones, M's eigenvalues are in {4, -5}?
    # For BvLS the srg eigenvalues are k=22, r=4, s=-5 (v=243,k=22: lambda=1,mu=2
    # -> r,s = (lam-mu +/- sqrt((lam-mu)^2+4(k-mu)))/2 = (-1 +/- sqrt(1+80))/2
    #        = (-1 +/- 9)/2 = 4, -5).  Off-ones eigenvalues of M in {4,-5}.
    ev = np.linalg.eigvalsh(M.astype(float))
    evr = np.round(ev).astype(int)
    offs = evr[np.argsort(-evr)[1:]]  # drop largest (the 14/22 eigenvalue)
    from collections import Counter
    print(f"  M spectrum (rounded) = {Counter(evr.tolist())}")
    print(f"  residual off-ones spectrum after dropping largest: "
          f"{Counter(offs.tolist())}  (should be within {{4,-5}} for BvLS)")

def _is_aut(A, g):
    n = A.shape[0]
    for v in range(n):
        for w in range(n):
            if A[g[v], g[w]] != A[v, w]:
                return False
    return True

if __name__ == "__main__":
    main()
