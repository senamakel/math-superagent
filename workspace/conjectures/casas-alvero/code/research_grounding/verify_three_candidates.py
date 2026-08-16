"""Verify the load-bearing computational claims of the three candidate
approaches moment-hankel-rank, hessian-covariant-transvectant, and
q-derivative-deformation.

Grounding, not proof: confirm the classical facts the candidates rest on and
check the char-p break claims, so the approach files carry computed facts.

Exact arithmetic only (sympy over QQ / GF(p)).
"""
from math import comb
from sympy import Poly, symbols, GF, QQ, Matrix, prod, factorial

x, y = symbols("x y")


def newton_power_sums(coeffs, char, upto):
    """coeffs: [a_0..a_n] of monic f = a_0 x^n + a_1 x^{n-1} + ... + a_n,
    so a_0=1.  Return p_0..p_upto where p_k = sum_j beta_j^k (multiplicity-
    weighted power sums of roots), by Newton's identities:
      p_0 = n;  k p_k + sum_{j=1..k} a_j p_{k-j} = 0  (a_j = 0 for j > n).
    """
    dom = QQ if char == 0 else GF(char)
    n = len(coeffs) - 1
    p = [dom(0)] * (upto + 1)
    p[0] = dom(n)
    for k in range(1, upto + 1):
        s = dom(0)
        for j in range(1, k + 1):
            a = dom(coeffs[j]) if j <= n else dom(0)
            s += a * p[k - j]
        p[k] = -s / dom(k)
    return p


def hankel_rank_from_coeffs(coeffs, char, r):
    """Rank of the r x r Hankel [p_{a+b}] built from Newton power sums of the
    roots of a monic degree-(len(coeffs)-1) polynomial with coefficients
    coeffs."""
    dom = QQ if char == 0 else GF(char)
    p = newton_power_sums(coeffs, char, 2 * r - 1)
    rows = [[dom(p[a + b]) for b in range(r)] for a in range(r)]
    M = Matrix(rows)
    return M.rank()


def hessian_homog(Fxy, char):
    """Hessian determinant of the homogeneous form F(x,y):
       H = F_xx*F_yy - (F_xy)^2,  for forms of degree n in x,y."""
    F = Fxy.expand()
    dom = QQ if char == 0 else GF(char)
    Fxx = F.diff(x, 2)
    Fxyy = F.diff(x).diff(y)
    Fyy = F.diff(y, 2)
    H = (Fxx * Fyy - Fxyy * Fxyy).expand()
    if char != 0:
        H = Poly(H, x, y, domain=dom).as_expr()
    return H


def gaus_binom(k, i, q):
    """Gaussian binomial [k choose i]_q as a rational function in q."""
    if i < 0 or i > k:
        return 0
    num = prod((1 - q ** (k - t)) for t in range(i))
    den = prod((1 - q ** (t + 1)) for t in range(i))
    return num / den


print("=== Candidate 1: moment-hankel-rank ===")
# (x-1)^n over QQ: roots {1} mult n -> rank 1 (use 2x2 Hankel)
for n in [4, 5, 6]:
    coeffs = [comb(n, j) * (-1) ** j for j in range(n + 1)]  # (x-1)^n
    r = hankel_rank_from_coeffs(coeffs, 0, 2)
    print(f"(x-1)^{n}: 2x2 Hankel rank = {r} (expect 1)")
# (x-1)(x-2)(x-3): roots 1,2,3 distinct -> rank 3 (3x3 Hankel)
coeffs = [1, -6, 11, -6]
print(f"(x-1)(x-2)(x-3): 3x3 Hankel rank = "
      f"{hankel_rank_from_coeffs(coeffs, 0, 3)} (expect 3)")
# char-p witness x^{p+1}-x^p: monic coeffs, a_p = -1
for p_ in [2, 3, 5]:
    coeffs = [0] * (p_ + 2)
    coeffs[0] = 1
    coeffs[p_] = -1
    r = hankel_rank_from_coeffs(coeffs, p_, 2)
    print(f"x^{p_+1}-x^{p_} over GF({p_}): 2x2 Hankel rank = {r} (expect 2)")

print()
print("=== Candidate 2: hessian-covariant-transvectant ===")
for n in [3, 4, 5]:
    for (a_, b_) in [(1, 0), (2, 1), (1, 3)]:
        F = (a_ * x + b_ * y) ** n
        H = hessian_homog(F, 0)
        print(f"(a x + b y)^{n} (a,b)=({a_},{b_}): Hessian {'== 0' if H == 0 else '!= 0'}")
# char-p witness F = x^{p+1} - x^p y (homogenized x^{p+1}-x^p)
for p_ in [2, 3, 5]:
    F = x ** (p_ + 1) - x ** p_ * y
    H = hessian_homog(F, p_)
    print(f"F = x^{p_+1} - x^{p_}y over GF({p_}): Hessian "
          f"{'== 0' if H == 0 else '!= 0'} (NOT a pure power: roots of x^{p+1}-x^p are 0 and 1)")

print()
print("=== Candidate 3: q-derivative-deformation ===")
q = symbols("q")
for p_ in [3, 5]:
    n = p_ + 1
    print(f"witness deg {n} (p={p_}): Gaussian binomials [p choose i]_q, i=1..p-1")
    for i in range(1, p_):
        gb = gaus_binom(p_, i, q)
        print(f"   [{p_} choose {i}]_q = {'nonzero rational fn of q' if gb != 0 else 'ZERO'}")
    print(f"   At q=1: [{p_} choose i]_1 = {gaus_binom(p_, 1, q).subs(q, 1)} "
          f"for i=1, and [p choose i]_1 for 1<=i<=p-1 is "
          f"{[int(gaus_binom(p_, i, q).subs(q,1)) for i in range(1,p_)]}")
