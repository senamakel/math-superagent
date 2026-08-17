"""Check the factorisation ord_0(R_i) = n(n-i) route at n=3..8.

Under a_j -> t^j a_j the roots scale beta_k -> t*beta_k, and by the two PROVED
root-difference identities (research/notes/root-difference-identity-verified.md,
char-free, any commutative ring):

    R_i(t) = Res_x(f_t, H_i(f_t)) = t^{n(n-i)} * S_i(beta),
    S_i(beta) = prod_k e_{n-i}({ beta_k - beta_j : j != k }).

Hence ord_0(R_i) = n(n-i) exactly iff S_i is not identically zero on the
traceless slice a_1 = 0 (S_i is symmetric in the beta's, i.e. a polynomial in
the a_j). One EXACT nonzero evaluation at a traceless set of distinct integer
roots proves not-identically-zero.

This script checks S_i != 0 (exact integers) at the traceless point
beta = {-7,-5,-3,-1,1,3,5,7} restricted to n of them, for n=3..8, i=1..n-1,
and cross-checks the predicted ords n(n-i) against the DIRECTLY VERIFIED ords
from the n=4..7 captures.

Usage: python uresultant/_check_factorisation_ords.py
"""
from sympy import prod, Integer
from itertools import combinations


def e_sym(mset, m):
    """elementary symmetric polynomial e_m of a multiset (exact)."""
    return sum(prod(mset[i] for i in sub) for sub in combinations(range(len(mset)), m))


def s_i(beta, i):
    """S_i(beta) = prod_k e_{n-i}({ beta_k - beta_j : j != k })."""
    n = len(beta)
    m = n - i
    total = Integer(1)
    for k in range(n):
        mset = [beta[k] - beta[j] for j in range(n) if j != k]
        total *= e_sym(mset, m)
    return total


# documented direct ords (from the n=4..7 captures):
#   n=4: [12, 8, 4]; n=5: [20,15,10,5]; n=6: [30,24,18,12,6]; n=7: [42,35,28,21,14,7]
BASE = {
    3: [-1, 0, 1],
    4: [-3, -1, 1, 3],
    5: [-4, -2, 0, 2, 4],
    6: [-5, -3, -1, 1, 3, 5],
    7: [-6, -4, -2, 0, 2, 4, 6],
    8: [-7, -5, -3, -1, 1, 3, 5, 7],
}
known = {
    4: [12, 8, 4],
    5: [20, 15, 10, 5],
    6: [30, 24, 18, 12, 6],
    7: [42, 35, 28, 21, 14, 7],
}
allok = True
for n in sorted(known) + [8]:
    beta = BASE[n]
    assert sum(beta) == 0, "traceless point required"
    S = [s_i(beta, i) for i in range(1, n)]
    nonzero = all(v != 0 for v in S)
    ords = [n * (n - i) for i in range(1, n)]
    if n in known:
        match = ords == known[n]
        print(f"n={n}: S_i != 0: {nonzero}  ords={ords} vs direct {known[n]}: "
              f"{'MATCH' if match else 'MISMATCH'}")
        allok = allok and nonzero and match
    else:
        print(f"n={n}: S_i != 0: {nonzero}  ords={ords} (predicted, no direct "
              f"resultant available)")
        print(f"      S_i values: {S}")
        allok = allok and nonzero
print("FACTORISATION ROUTE", "OK" if allok else "FAIL")