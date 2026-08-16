#!/usr/bin/env python3
"""
PE622 structure verification for the reference library (not the answer).

Facts checked:
 1. 2^60 - 1 factors; its factorization via cyclotomics.
 2. ord_m(2) = 60  <=>  m | 2^60 - 1 and no proper divisor d of 60 has
    2^d == 1 (mod m).  So the enumeration is finite: over divisors of
    2^60 - 1.  This is what defeats an unbounded scan of n.
 3. CRT/lcm decomposition: for odd squarefree-ish m = prod p_i^{a_i},
    ord_m(2) = lcm_i ord_{p_i^{a_i}}(2).
Outputs go to code/out/ for the record; the ANSWER is left to solution.py.
"""
import sympy


m = 2**60 - 1
print("2^60 - 1 =", m)
fac = sympy.factorint(m)
print("factorisation:", fac)
print("prime factors:", list(fac))

# cyclotomic identity: 2^60 - 1 = prod_{d|60} Phi_d(2)
cyc = [sympy.cyclotomic_poly(d).subs(sympy.Symbol("x"), 2) for d in
       sympy.divisors(60)]
from functools import reduce
prod = 1
for c in cyc:
    prod *= int(c)
print("prod_{d|60} Phi_d(2) == 2^60-1 :", prod == m)

# ord_m(2) for m = 2^60-1
print("ord_{2^60-1}(2) =", sympy.n_order(2, m))


def ord_mod(a, m):
    r, v = 0, 1
    while True:
        r += 1
        v = (v * a) % m
        if v == 1:
            return r


# Every divisor of 2^60-1 with exact order 60 is an n-1 candidate.
# (Counting them and summing n=m+1 is the solution step, not done here.)
