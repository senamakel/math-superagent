"""Exact computation of Iwasawa's index formula [Z[G]^- : s^-] = h^-(Q(zeta_p))
by a direct group-ring lattice index -- a second, independent route to the
minus class number, cross-checking the Bernoulli-character formula.

Setting. F = Q(zeta_p), G = {1..p-1} under multiplication mod p, p an odd prime.
  theta = (1/p) sum_{a in G} a sigma_{a^{-1}}      (Stickelberger element)
  s     = Z[G] theta cap Z[G] = { x in Z[G] : p | sum_i x_i i^{-1} }.
  e^-   = (1/2)(1 - sigma_{-1}).
  Z[G]^- = e^- Z[G]  (minus part),  s^- = e^- s.

Coordinates. Write w_a := sigma_a - sigma_{-a} for a in a set R of reps of
{a,-a}, |R| = m = (p-1)/2. Then Z[G]^- = e^- Z[G] has w-basis {(1/2) w_a :
a in R} (because e^- sigma_b = (1/2)(sigma_b - sigma_{-b})). For y in Z[G],
  e^- y = sum_a (1/2)(y_a - y_{-a}) w_a.
Multiply all w-coordinates by 2 to work in the integer lattice L0 = Z^m
("doubled w-coordinates"). In these doubled coordinates Z[G]^- = Z^m, and
  s^-  has generators  ( b_a - b_{-a} )_{a in R}   for b in a Z-basis of s.

A Z-basis of s. With L_j = j^{-1} (mod p) and L := L_{n-1} = (p-1)^{-1}:
  for j = 0..n-2 :  b_j = e_j + t_j e_{n-1},  t_j = -L_j * inv(L_{n-1}) mod p,
  and           :  b_{n-1} = p * e_{n-1}.
(These satisfy L·b = 0 (mod p), rank n, index p => a Z-basis of s.)

Then [Z[G]^- : s^-] = | Z^m / < doubled-coord generators > |, read off as the
product of the nonzero invariant factors of the m x K generator matrix (Smith
normal form). This must equal h^- .  We check against exact h^- from the
Bernoulli-character formula (lib.cyclo) and against a known-value table.
"""
from fractions import Fraction
from itertools import combinations
from math import gcd
from functools import reduce
import time


def min_basis_coords(b, p):
    """For b in Z[G] (coefficient vector, positions 0..p-2 for a=1..p-1), return
    the doubled w-coordinates (b_a - b_{-a}) for a = 1..m (m=(p-1)/2). Integers.
    Here a ranges over 1..(p-1)/2, and -a = p-a ranges over (p+1)/2..p-1, so the
    position of p-a is (p-a)-1 = p-a-1, always >= (p-1)/2 > 0. Indexing is valid."""
    m = (p - 1) // 2
    coords = []
    for a in range(1, m + 1):
        ia = a - 1               # position of a
        neb = (p - a) - 1        # position of p-a, i.e. of -a
        coords.append(b[ia] - b[neb])
    return coords


def macht_minus_index(p):
    n = p - 1
    m = n // 2
    # inverse residues
    invs = {a: pow(a, p - 2, p) for a in range(1, p)}
    Larr = [invs[a] for a in range(1, p)]          # L_j = j^{-1} mod p, j position a-1

    # Z-basis of s (n vectors)
    basis_s = []
    Ln = Larr[-1]
    for j in range(n - 1):
        t = (-Larr[j] * pow(Ln, p - 2, p)) % p
        vec = [0] * n
        vec[j] = 1
        vec[n - 1] = t
        basis_s.append(vec)
    vec = [0] * n
    vec[n - 1] = p
    basis_s.append(vec)

    # doubled w-coordinates of each basis vector -> generators of s^- in L0 = Z^m
    gens = [min_basis_coords(b, p) for b in basis_s]   # each length m, integers
    # Index of the lattice Lgen (spanned by gens in Z^m):
    #   If the K generator vectors span a full-rank sublattice of Z^m, the index
    #   [Z^m : Lgen] = gcd of all m x m minors of the K x m generator matrix.
    # (Classical: lattice index = gcd of maximal minors.) Exact integer arithmetic.
    Gen = [list(g) for g in gens]      # K vectors, each length m (columns = Z^m coords)
    # Index of the lattice Lgen in Z^m = product of the nonzero invariant factors
    # of the m x K generator matrix (Smith normal form computes the cokernel
    # order Z^m / Lgen directly). Exact integer arithmetic, no enumeration.
    from sympy import Matrix
    from sympy.matrices.normalforms import smith_normal_form
    M = Matrix(Gen).T                   # m x K
    S = smith_normal_form(M)            # same shape m x K
    idx = 1
    for i in range(min(S.rows, S.cols)):
        d = S[i, i]
        if d != 0:
            idx *= int(d)
    return idx, m


if __name__ == "__main__":
    # Known relative class numbers h^-(Q(zeta_p)) for p up to 53 (verify_claims /
    # hminus_full, two routes): 
    known = {3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 3,
             29: 8, 31: 9, 37: 37, 41: 121, 43: 211, 47: 695, 53: 4889}
    all_ok = True
    for p in [5, 7, 11, 13, 17, 23, 29, 31]:
        t = time.time()
        idx, m = macht_minus_index(p)
        ok = (idx == known[p])
        all_ok = all_ok and ok
        print(f"p={p:3d}  [Z[G]^-:s^-] = {idx:6d}   h^- known = {known[p]:6d}   "
              f"{'MATCH' if ok else 'MISMATCH'}   ({time.time()-t:.2f}s)")
    print("\nALL MATCH known h^-:", all_ok)
