from fractions import Fraction
from math import ceil

# S_k = 4^{k-1}(k - 13/6) + (2k-1)/3 : guaranteed limit cycles of PH_k
# (Buzzi-Novaes / Li et al. corrected Christopher-Lloyd family, degree 2k-1).
def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

C = [int(ceil(S(k))) for k in range(1, 201)]  # ceil(S_k), k=1..200

# ---- Claim A: fractional-part periodicity.
# 6 S_k = 4^{k-1}(6k-13) + 4k - 2 ; for k >= 2, 4^{k-1} = 4 (mod 6), so
# 6 S_k = 28k - 54 = 4k (mod 6).  Hence:
#   k = 0 mod 3 -> 6 S_k = 0 (mod 6) -> S_k integer
#   k = 1 mod 3 -> 6 S_k = 4 (mod 6) -> frac = 2/3
#   k = 2 mod 3 -> 6 S_k = 2 (mod 6) -> frac = 1/3
bad_frac = []
for k in range(2, 201):
    frac = S(k) - S(k).__floor__() if S(k) >= 0 else S(k) - int(S(k))  # frac in [0,1)
    # Python Fraction has no __floor__ attribute issue; use numerator//denominator
    q = S(k).numerator // S(k).denominator
    frac = S(k) - q
    pred = {0: Fraction(0), 1: Fraction(2,3), 2: Fraction(1,3)}[k % 3]
    if frac != pred:
        bad_frac.append((k, frac, pred))
print("Claim A (frac part of S_k periodic mod 3, k>=2): failures =", len(bad_frac), bad_frac[:3])

# ---- Claim B: delta_k = ceil(S_k) - S_k has period 3 for k >= 2.
bad_delta = []
for k in range(2, 201):
    delta = Fraction(ceil(S(k))) - S(k)
    pred = {0: Fraction(0), 1: Fraction(1,3), 2: Fraction(2,3)}[k % 3]
    if delta != pred:
        bad_delta.append((k, delta, pred))
print("Claim B (delta_k period 3, k>=2): failures =", len(bad_delta), bad_delta[:3])
print("  delta_1 (exception):", Fraction(ceil(S(1))) - S(1))

# ---- Claim C: ceil(S_k) satisfies the order-6 constant-coefficient recurrence
# with annihilator (E-4)^2 (E-1)^2 (E^2+E+1) = E^6 -9E^5 +24E^4 -17E^3 +9E^2 -24E +16,
# for all k >= 2 (indexed from the start of the computed sequence, i.e. terms
# C[k] with k>=2).
coeffs = [1, -9, 24, -17, 9, -24, 16]  # C_{k+6}, C_{k+5}, ..., C_k
bad_rec = []
# C[j] = ceil(S_{j+1}) for j = 0..199; recurrence at index k (k>=2 in problem
# index) uses C[k-1]..C[k+5] i.e. S_{k}..S_{k+6}.
for k in range(2, 195):   # problem-index k; needs C[k+5] <= C[199] -> k <= 194
    lhs = sum(c * C[k+6-i-1] for i, c in enumerate(coeffs))
    if lhs != 0:
        bad_rec.append((k, lhs))
print("Claim C (order-6 annihilator on ceil(S_k), k=2..199): failures =",
      len(bad_rec), bad_rec[:5])
first_fail = min((k for k, _ in bad_rec), default=None)
print("  first failing k:", first_fail)

# ---- Claim D: order 5 does NOT annihilate ceil(S_k) (minimality), checked by
# exact elimination: solve order-5 recurrence on the first 5 equations and
# verify on the remaining terms.
def solve_rec(seq, order, n_eqs=None):
    # seq[0], seq[1], ... ; find c1..c_order with a_{n} = sum c_i a_{n-i}
    import sympy as sp
    N = len(seq)
    eqs = n_eqs or order
    cs = sp.symbols('c1:' + str(order+1))
    A = sp.zeros(eqs, order); b = sp.zeros(eqs, 1)
    for r in range(eqs):
        for c in range(order):
            A[r, c] = seq[order + r - 1 - c]
        b[r] = seq[order + r]
    sol = sp.solve_linear_system(A.row_join(b), *cs)
    if sol is None:
        return ('nosol',)
    coeff = [sp.simplify(sol[c]) for c in cs]
    for r in range(eqs, N - order):
        lhs = seq[order + r]
        rhs = sum(coeff[c] * seq[order + r - 1 - c] for c in range(order))
        if sp.simplify(lhs - rhs) != 0:
            return ('fail', r)
    return coeff

from sympy import Rational
Crat = [Rational(x, 1) for x in C[:30]]  # exact, ceil(S_k) for k=1..30
print("order-5 fit over k=1..30:", solve_rec(Crat, 5))
print("order-6 fit over k=1..30:", solve_rec(Crat, 6))

# ---- Also confirm the raw integer-subsequence identity inside ceil:
# ceil(S_k) == S_k exactly when 3 | k (so the a_j guaranteed counts are the
# subsequence of ceil at indices 3j).
bad_sub = [k for k in range(3, 201, 3) if ceil(S(k)) != int(S(k))]
print("Claim E (ceil(S_k) = S_k for 3|k): failures =", len(bad_sub), bad_sub[:3])
print()
print("ceil(S_k), k=1..16:", [int(ceil(S(k))) for k in range(1, 17)])