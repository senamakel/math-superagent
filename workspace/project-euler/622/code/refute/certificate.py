#!/usr/bin/env python3
"""Final independent certificate: verify the answer 3010983666182123972 by
multiplication from FIRST PRINCIPLES, no divisor functions at all.

sigma(p^k) = (p^{k+1}-1)/(p-1); tau(p^k) = k+1; multiplicativity.
All factorization used: 
  N      = 2^60-1     = 3^2 * 5^2 * 7 * 11 * 13 * 31 * 41 * 61 * 151 * 331 * 1321
  2^12-1 = 4095       = 3^2 * 5 * 7 * 13
  2^20-1 = 1048575    = 3 * 5^2 * 11 * 31 * 41
  2^30-1 = 1073741823 = 3^2 * 7 * 11 * 31 * 151 * 331
  15=3*5, 63=3^2*7, 1023=3*11*31, 3=3.
"""
from math import prod
from functools import reduce

def sigma_pk(p, k):
    return (p**(k+1) - 1) // (p - 1)

def sig_from(factors):
    # factors: list of (p, k)
    return prod(sigma_pk(p, k) for (p, k) in factors)

def tau_from(factors):
    return prod(k + 1 for (p, k) in factors)

F = {
 "N":      [(3,2),(5,2),(7,1),(11,1),(13,1),(31,1),(41,1),(61,1),(151,1),(331,1),(1321,1)],
 "4095":   [(3,2),(5,1),(7,1),(13,1)],
 "1048575":[(3,1),(5,2),(11,1),(31,1),(41,1)],
 "1073741823":[(3,2),(7,1),(11,1),(31,1),(151,1),(331,1)],
 "15":     [(3,1),(5,1)],
 "63":     [(3,2),(7,1)],
 "1023":   [(3,1),(11,1),(31,1)],
 "3":      [(3,1)],
}

sig = {k: sig_from(v) for k, v in F.items()}
tau = {k: tau_from(v) for k, v in F.items()}
for k in sig:
    print("%-11s sigma=%d tau=%d" % (k, sig[k], tau[k]))

S = (sig["N"] - sig["4095"] - sig["1048575"] - sig["1073741823"]
     + sig["15"] + sig["63"] + sig["1023"] - sig["3"])
C = (tau["N"] - tau["4095"] - tau["1048575"] - tau["1073741823"]
     + tau["15"] + tau["63"] + tau["1023"] - tau["3"])
answer = S + C
print("\nS =", S)
print("C =", C)
print("ANSWER = S + C =", answer)
assert answer == 3010983666182123972, answer
print("\nANSWER 3010983666182123972 CONFIRMED by first-principles multiplication.")

# worked example: order-8 decks are n = m+1 for m | 255 with ord_m(2)=8
# divisors of 255: 3,5,15,17,51,85,255; those with ord=8: {17,51,85,255}
m8 = [17, 51, 85, 255]
print("\norder-8 decks n:", [m+1 for m in m8], " sum =", sum(m+1 for m in m8))
assert sum(m+1 for m in m8) == 412
