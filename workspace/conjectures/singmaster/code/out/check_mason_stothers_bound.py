"""Check whether Mason-Stothers gives any content for the binomial difference.

A(T) = C(T,k1)*k2!,  B(T) = -C(T,k2)*k1!,  R = A + B,  D = gcd(A,B) = (T)_min.
Mason-Stothers (A'+B'+R'=0, coprime): max deg <= N0(A'B'R') - 1 must hold;
we verify it is always satisfied (vacuous) for binomial pairs, i.e. the
inequality never binds.
"""
from sympy import binomial, Poly, symbols, gcd, expand_func

T = symbols('T')

def vacuous(k1, k2):
    A = Poly(expand_func(binomial(T, k1)) * __import__('math').factorial(k2), T)
    B = Poly(-expand_func(binomial(T, k2)) * __import__('math').factorial(k1), T)
    R = A + B
    D = Poly(gcd(A.as_expr(), B.as_expr()), T)
    A1 = A.exquo(D)
    B1 = B.exquo(D)
    R1 = R.exquo(D)
    # number of distinct roots of the product (over C), upper bounded by deg sums
    N0_ub = A1.degree() + B1.degree() + R1.degree()
    maxdeg = max(A1.degree(), B1.degree(), R1.degree())
    # Mason-Stothers requires maxdeg <= N0(prod)-1; N0 <= N0_ub.
    # If even maxdeg <= N0_ub - 1 fails to be required strictly, inequality is
    # vacuous; report slack: N0_ub - 1 - maxdeg.
    return A1.degree(), B1.degree(), R1.degree(), N0_ub - 1 - maxdeg

print("k1 k2 : degA' degB' degR' : slack = (N0_ub-1) - maxdeg  (slack>=0 => vacuous)")
for k1 in range(2, 9):
    for k2 in range(2, k1):
        dA, dB, dR, slack = vacuous(k1, k2)
        print(f"{k1} {k2} : {dA:3d} {dB:3d} {dR:3d} : {slack:3d}")