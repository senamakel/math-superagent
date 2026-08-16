"""Verify the Bacher mod-2 symmetric-Pascal determinant claims (bacher-pascal-det-mod2).

The claim's `holds-here` is flagged unchecked: Bacher states det formulas for the
SYMMETRIC Pascal matrix P(n) with entries C(s+t, s) mod 2, but this problem's fold
Phi_n is the rectangular offset matrix with entries C(k-1, j-(n-k)) mod 2. This
checks (a) the Bacher det formulas as stated, and (b) whether they have any bearing
on the actual Phi_n used here.

Exact integer arithmetic via sympy binomials + Python ints.
"""
import sympy

def sym_pascal(n, mod=2):
    """Symmetric Pascal matrix P(n): Ps,t = C(s+t, s) mod `mod`, 0<=s,t<n."""
    return sympy.Matrix([
        [sympy.binomial(s + t, s) % mod for t in range(n)]
        for s in range(n)
    ])

def fold_matrix(n):
    """The fold Phi_n from problem.md: entries C(k-1, j-(n-k)) mod 2.
    Phi_n maps h in F2^n to a vector; the diagonal cells are wt(Phi_n h).
    Rows k = 1..n-1 (the cells), columns j = 0..n-1.
    We use the same shape as established fact (3): rank Phi_n = n-3, nullity 1.
    """
    rows, cols = [], n
    # Phi_n is (n-1) x n as described: the map whose image weight IS nu2.
    # Established fact (3) says rank = n-3, nullity 1. Nullity 1 of an (n-1)x n
    # matrix means rank = n-1 - ... let's just compute the actual rank and nullity.
    return sympy.Matrix([
        [int(sympy.binomial(k - 1, j - (n - k))
             % 2) if 0 <= j - (n - k) <= k - 1 else 0
         for j in range(n)]
        for k in range(1, n)
    ])

def int_rank(M):
    return M.rank() if hasattr(M, "rank") else \
        sympy.Matrix(M.tolist()).rank()

print("== Bacher symmetric Pascal det ==")
for n in [1, 2, 4, 8, 16]:
    d_even = sym_pascal(2 * n).det()
    ds = bin(n).count("1")
    d_odd = sym_pascal(2 * n + 1).det()
    expect_even = (-1) ** n
    expect_odd = (-1) ** (n + ds)
    print(f"n={n:2d}  det P(2n)={int(d_even):6d} expect {int(expect_even):6d} match={d_even==expect_even}"
          f" | det P(2n+1)={int(d_odd):6d} expect {int(expect_odd):6d} match={d_odd==expect_odd}")

print("\n== This problem's fold matrix Phi_n (rank / nullity) ==")
for n in range(2, 11):
    M = fold_matrix(n)
    # rank over F2
    Mf2 = sympy.Matrix(M.tolist()).applyfunc(lambda x: x % 2)
    r = Mf2.rank()
    nullity = n - r
    print(f"n={n:2d}  Phi_n is {M.rows}x{M.cols}  rank={r} (n-3={n-3})  nullity={nullity}")

# Check the known fact: rank Phi_n = n-3 for n=2..20 (established fact (3))
print("\n== rank Phi_n = n-3 up to n=20? ==")
ok = True
for n in range(2, 21):
    M = sympy.Matrix(fold_matrix(n).tolist()).applyfunc(lambda x: x % 2)
    r = M.rank()
    if r != n - 3:
        ok = False
        print(f"  n={n} rank={r} != n-3")
print("all n in 2..20 rank=n-3:", ok)
