#!/usr/bin/env python3
"""Extract the C(k) (ord-count) and S(k) (ord-sum) sequences for k=1..N
and print them as comma/space lists for the sequence tools and OEIS lookup.
"""
import sympy

def C_S(k):
    C = sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(k))
    return C, S

N = 24
Cs, Ss = [], []
for k in range(1, N + 1):
    C, S = C_S(k)
    Cs.append(C)
    Ss.append(S)

print("C(k) k=1..%d:" % N)
print(", ".join(map(str, Cs)))
print()
print("S(k) k=1..%d:" % N)
print(", ".join(map(str, Ss)))
