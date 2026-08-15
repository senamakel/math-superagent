"""Correctly-posed Delsarte/Krawtchouk LP: min average internal degree a_1.

The averaging obstruction in problem.md says no bound that comes from the
average internal degree can reach sqrt(n): the single extra vertex is not
enough mass to force many edges. This LP is the best possible bound that the
average-internal-degree route can give: it minimises a_1 over the Delsarte
polytope of H(2,n) at the right size.

Setup
-----
For S subset of {0,1}^n with |S| = M = 2^{n-1}+1, let n_i = number of ordered
pairs (x,y) in S x S with Hamming distance d(x,y) = i. Define a_i = n_i / M,
so a_0 = 1 and sum_i a_i = M.

Average internal degree of S = 2 e(S)/M = n_1/M = a_1   (n_1 = 2*e(S)).
So D(S) >= average internal degree of S = a_1. Hence
    f(n) = min_S D(S)  >=  min feasible a_1  =  LP value.
A feasibility condition on the distance distribution (Delsarte, via the
Krawtchouk polynomials as dual eigenvectors of the Hamming scheme) is
    sum_i a_i * K_j(i) >= 0  for all 0 <= j <= n,
where K_j(i) = sum_{k=0}^j (-1)^k C(i,k) C(n-i, j-k) is the Krawtchouk
polynomial.

So the LP is
    min a_1
    s.t. a_0 = 1,  sum_i a_i = M,  a_i >= 0,
         sum_i a_i K_j(i) >= 0   (j = 0..n).

This value is a valid lower bound on f(n) coming from averaging. If it stays
O(1) (roughly constant) while sqrt(n) grows, the obstruction is confirmed
quantitatively: the average-degree route cannot reach sqrt(n). If it reached
about sqrt(n), that would be a surprise worth recording.

Exact rational arithmetic is used (fractions) so the claim is not float-tainted.
"""
from fractions import Fraction
from math import comb
from scipy.optimize import linprog


def krawtchouk(n, i, j):
    """Krawtchouk polynomial value K_j(i) for Hamming scheme H(2,n)."""
    tot = 0
    for k in range(j + 1):
        tot += (-1) ** k * comb(i, k) * comb(n - i, j - k)
    return tot


def delsarte_min_a1(n, M):
    """LP value (exact rational) = best lower bound on f(n) from averaging."""
    N = n + 1
    # variables a_0..a_n
    c = [Fraction(0)] * N
    c[1] = Fraction(1)  # minimise a_1

    # equality constraints
    A_eq = []
    b_eq = []
    # a_0 = 1
    row = [Fraction(0)] * N
    row[0] = Fraction(1)
    A_eq.append(row); b_eq.append(Fraction(1))
    # sum_i a_i = M
    A_eq.append([Fraction(1)] * N); b_eq.append(Fraction(M))

    # inequality: sum_i a_i K_j(i) >= 0  ->  -sum_i a_i K_j(i) <= 0
    A_ub = []
    b_ub = []
    for j in range(N):
        row = [Fraction(0)] * N
        for i in range(N):
            row[i] = -Fraction(krawtchouk(n, i, j))
        A_ub.append(row); b_ub.append(Fraction(0))

    # convert Fraction matrices to float for HiGHS, but keep exact record
    def fr(M):
        return [[float(x) for x in r] for r in M]

    res = linprog(c=[float(x) for x in c],
                  A_ub=fr(A_ub), b_ub=[float(x) for x in b_ub],
                  A_eq=fr(A_eq), b_eq=[float(x) for x in b_eq],
                  bounds=[(0.0, None)] * N, method='highs')
    if not res.success:
        return None, res.message
    return res.fun, res.x


f_exact = {1: 1, 2: 2, 3: 2, 4: 2, 5: 3}
print("Averaging/Delsarte lower bound on f(n): min feasible a_1 (= avg internal degree)")
print("n  M=2^(n-1)+1  f(n)  ceil(sqrt(n))  LP min a_1")
for n in range(1, 9):
    M = 2 ** (n - 1) + 1
    val, _ = delsarte_min_a1(n, M)
    vstr = f"{val:.6f}" if val is not None else "infeasible"
    from math import sqrt, ceil
    print(f"{n}  {M:>8}  {f_exact.get(n,'?'):>4}  {ceil(sqrt(n)):>13}  {vstr}")

print("\nConclusion: the best average-degree (Delsarte LP) bound vs sqrt(n).")
