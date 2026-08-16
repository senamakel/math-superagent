#!/usr/bin/env python3
"""Fresh pattern checks for PE622 beyond what is on disk.

1. Confirm the inverse-pair (prefix-sum) identity exactly:
       sum_{d|k} C(d) == tau(2^k-1) - 1        over k=1..80
       sum_{d|k} S(d) == sigma(2^k-1) - 1      over k=1..80
2. Mersenne signature: when 2^k-1 is prime, C(k)=1 and S(k)=2^k-1  (k=1..80).
3. Factor the final answer 3010983666182123972 (certificate for Lean).
"""
import sympy


def C_S(k):
    C = sum(sympy.mobius(k // d) * (sympy.divisor_count(2**d - 1) - 1)
            for d in sympy.divisors(k))
    S = sum(sympy.mobius(k // d) * (sympy.divisor_sigma(2**d - 1, 1) - 1)
            for d in sympy.divisors(k))
    return C, S

# 1. prefix-sum inverse-pair identity, extended range k=1..80
bad1 = []
for k in range(1, 81):
    C, S = C_S(k)
    Cs = sum(C_S(d)[0] for d in sympy.divisors(k))
    Ss = sum(C_S(d)[1] for d in sympy.divisors(k))
    if Cs != sympy.divisor_count(2**k - 1) - 1:
        bad1.append(('C', k))
    if Ss != sympy.divisor_sigma(2**k - 1, 1) - 1:
        bad1.append(('S', k))
print("1. prefix-sum identity k=1..80 holds:", not bad1, bad1[:5])

# 2. Mersenne signature through k=80
bad2 = []
for k in range(1, 81):
    C, S = C_S(k)
    if sympy.isprime(2**k - 1):
        if C != 1 or S != 2**k - 1:
            bad2.append(k)
print("2. Mersenne signature holds at all Mersenne-prime k in 1..80:",
      not bad2, "bad:", bad2)

# 3. factor the final answer
ans = 3010983666182123972
print("3. answer factorization:", sympy.factorint(ans))
# also S and C separately
print("   S(60) =", C_S(60)[1], "=", sympy.factorint(C_S(60)[1]))
print("   C(60) =", C_S(60)[0], "=", sympy.factorint(C_S(60)[0]))
