#!/usr/bin/env python3
"""Independent refutation-check of the run's committed arithmetic claims.

We re-derive, from first principles with no reference to the run's numbers:
  1. The final answer (sum of n with s(n)=60, n even) three independent ways.
  2. Every sigma / tau literal in G-divisor-sums.
  3. The G-ord-criterion (ord_m(2)=60  <=>  m|2^60-1 and not (m|2^12-1,m|2^20-1,m|2^30-1))
     over all 4608 divisors of 2^60-1.  This is the exact claim the run's
     inclusion-exclusion depends on; a single counterexample breaks it.
"""
import sympy
from math import gcd

N = 2**60 - 1

# ---- direct order computation (naive, exact) ----
def ord_mod(a, m):
    if gcd(a, m) != 1:
        return None
    r, val = 0, 1
    while True:
        r += 1
        val = (val * a) % m
        if val == 1:
            return r

# ---- 1. final answer by direct enumeration over divisors of N ----
divs = sympy.divisors(N)
assert len(divs) == 4608
good = [m for m in divs if m > 1 and ord_mod(2, m) == 60]
S = sum(good); C = len(good)
answer_direct = S + C
print("direct:  C =", C, " S =", S, " answer =", answer_direct)

# ---- 2. final answer by Möbius inversion ----
def answer_mobius(k):
    C = sum(sympy.mobius(k//d) * (sympy.divisor_count(2**d - 1) - 1) for d in sympy.divisors(k))
    S = sum(sympy.mobius(k//d) * (sympy.divisor_sigma(2**d - 1, 1) - 1) for d in sympy.divisors(k))
    return C, S
Cm, Sm = answer_mobius(60)
print("mobius: C =", Cm, " S =", Sm, " answer =", Sm + Cm)

# ---- 3. final answer by inclusion-exclusion (the run's closed form) ----
sg = lambda k: sympy.divisor_sigma(2**k - 1, 1)
tz = lambda k: sympy.divisor_count(2**k - 1)
S_ie = (sympy.divisor_sigma(N,1) - sg(12) - sg(20) - sg(30)
        + sg(4) + sg(6) + sg(10) - sg(2))
C_ie = (sympy.divisor_count(N) - tz(12) - tz(20) - tz(30)
        + tz(4) + tz(6) + tz(10) - tz(2))
print("iex:    C =", C_ie, " S =", S_ie, " answer =", S_ie + C_ie)

# ---- verify the run's G-divisor-sums literals ----
print("\nG-divisor-sums literals vs sympy:")
for label, val in [
    ("sigma(N)", sympy.divisor_sigma(N,1)),
    ("tau(N)", sympy.divisor_count(N)),
    ("sigma(2^12-1)", sympy.divisor_sigma(2**12-1,1)),
    ("tau(2^12-1)", sympy.divisor_count(2**12-1)),
    ("sigma(2^20-1)", sympy.divisor_sigma(2**20-1,1)),
    ("tau(2^20-1)", sympy.divisor_count(2**20-1)),
    ("sigma(2^30-1)", sympy.divisor_sigma(2**30-1,1)),
    ("tau(2^30-1)", sympy.divisor_count(2**30-1)),
    ("sigma(15)", sympy.divisor_sigma(15,1)),
    ("tau(15)", sympy.divisor_count(15)),
    ("sigma(63)", sympy.divisor_sigma(63,1)),
    ("tau(63)", sympy.divisor_count(63)),
    ("sigma(1023)", sympy.divisor_sigma(1023,1)),
    ("tau(1023)", sympy.divisor_count(1023)),
    ("sigma(3)", sympy.divisor_sigma(3,1)),
    ("tau(3)", sympy.divisor_count(3)),
]:
    print("  %-14s = %d" % (label, val))

run = {
 "sigma(N)":3010983668199456768, "tau(N)":4608,
 "sigma(2^12-1)":8736, "tau(2^12-1)":24,
 "sigma(2^20-1)":1999872, "tau(2^20-1)":48,
 "sigma(2^30-1)":2015330304, "tau(2^30-1)":96,
 "sigma(15)":24, "tau(15)":4, "sigma(63)":104, "tau(63)":6,
 "sigma(1023)":1536, "tau(1023)":8, "sigma(3)":4, "tau(3)":2,
}
for k,v in run.items():
    actual = {"sigma(N)":sympy.divisor_sigma(N,1),
     "tau(N)":sympy.divisor_count(N),
     "sigma(2^12-1)":sympy.divisor_sigma(2**12-1,1),
     "tau(2^12-1)":sympy.divisor_count(2**12-1),
     "sigma(2^20-1)":sympy.divisor_sigma(2**20-1,1),
     "tau(2^20-1)":sympy.divisor_count(2**20-1),
     "sigma(2^30-1)":sympy.divisor_sigma(2**30-1,1),
     "tau(2^30-1)":sympy.divisor_count(2**30-1),
     "sigma(15)":sympy.divisor_sigma(15,1), "tau(15)":sympy.divisor_count(15),
     "sigma(63)":sympy.divisor_sigma(63,1), "tau(63)":sympy.divisor_count(63),
     "sigma(1023)":sympy.divisor_sigma(1023,1), "tau(1023)":sympy.divisor_count(1023),
     "sigma(3)":sympy.divisor_sigma(3,1), "tau(3)":sympy.divisor_count(3)}[k]
    status = "OK" if actual == v else "MISMATCH"
    print("  %-14s run=%d computed=%d  %s" % (k, v, actual, status))

# ---- 4. G-ord-criterion over all divisors of N ----
print("\nG-ord-criterion check over all 4608 divisors of N:")
crit_bad = 0
for m in divs:
    if m == 1:
        continue
    o = ord_mod(2, m)
    lhs = (o == 60)
    rhs = ((N % m == 0)
           and ( (2**12-1) % m != 0)
           and ((2**20-1) % m != 0)
           and ((2**30-1) % m != 0))
    if lhs != rhs:
        crit_bad += 1
        print("  COUNTEREXAMPLE m=", m, "ord=", o, " lhs", lhs, " rhs", rhs)
print("cov divs checked =", len(divs)-1, " mismatches =", crit_bad)

# ---- 5. worked example sum for order 8 ----
good8 = [m for m in sympy.divisors(2**8-1) if m > 1 and ord_mod(2,m)==8]
print("\norder-8:  divisors of 255 with ord=8:", good8, " sum m+C =", sum(good8)+len(good8))
