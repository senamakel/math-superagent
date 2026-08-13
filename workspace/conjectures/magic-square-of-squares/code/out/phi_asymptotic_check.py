#!/usr/bin/env python3
"""Estimate the asymptotic constant of |Phi(B)| from its exact closed form.

|Phi(B)| = sum_{M even <= B} phi(M) + (1/2) sum_{M odd <= B} phi(M)
(verified exact vs direct enumeration for B <= 1200 in phi_identity_verify).

Compare |Phi(B)|/B^2 against candidate constants: 2/pi^2, 3/(2pi^2), etc.
"""
from math import isqrt

def phi_up_to(N):
    phi = list(range(N + 1))
    for p in range(2, N + 1):
        if phi[p] == p:  # prime
            for m in range(p, N + 1, p):
                phi[m] -= phi[m] // p
    return phi

B = 2_000_000
phi = phi_up_to(B)
E = [0]*(B+1); O = [0]*(B+1)
se = so = 0
for M in range(1, B+1):
    if M % 2 == 0:
        se += phi[M]
    else:
        so += phi[M]
    E[M] = se; O[M] = so

from math import pi
for n in [10**3, 10**4, 10**5, 10**6, B]:
    Phi = E[n] + O[n]//2          # 1/2 * odd sum (odd sums over odd M, integer)
    Phi = E[n] + (O[n] + 1)//2 if O[n] % 2 else E[n] + O[n]//2
    # exact: |Phi| = E + O/2 ; halving of O is exact only if O even
    Phi_exact = 2*E[n] + O[n]
    ratio = Phi_exact / (2*n*n)
    print(f"B={n:>9}: E+O/2 = {E[n]} + {O[n]}/2, "
          f"2|Phi| = {Phi_exact}, |Phi|/B^2 = {Phi_exact/(2*n*n):.6f}")
    print(f"       2/pi^2 = {2/pi**2:.6f}, 3/(2pi^2) = {3/(2*pi**2):.6f}, "
          f"3/pi^2 = {3/pi**2:.6f}, 6/pi^2={6/pi**2:.6f}")
