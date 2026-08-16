#!/usr/bin/env python3
"""Independent, first-principles verification of every committed arithmetic
claim in the run, WITHOUT sympy's divisor_sigma (to avoid reusing the same
library the run used).  Divisor sums computed by brute force / explicit
prime-power formula built from scratch (sympy used only for primality here).

Claims checked:
  A. G-ord-criterion: ord_m(2)=60 <=> (m|2^60-1 and not divide any of
     2^12-1, 2^20-1, 2^30-1) over every divisor m>1 of 2^60-1.
  B. G-divisor-sums literals (sigma/tau) via my own sigma.
  C. Final answer 3010983666182123972.
  D. R-sum8 worked example = 412.
  E. R-ord51-2: order of 2 mod 51 is 8.
"""
from math import gcd

def order2mod(m):
    """order of 2 mod m via direct power iteration (m odd)."""
    if gcd(2, m) != 1:
        return None
    v, r = 1, 0
    while True:
        r += 1
        v = (v * 2) % m
        if v == 1:
            return r

def divisors(n):
    ds = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            ds.append(i)
            if i != n // i:
                ds.append(n // i)
        i += 1
    return sorted(ds)

def sigma_brute(n):
    """sum of positive divisors of n, computed brute-force."""
    return sum(divisors(n))

def tau_brute(n):
    return len(divisors(n))

def is_prime(p):
    if p < 2: return False
    i = 2
    while i * i <= p:
        if p % i == 0: return False
        i += 1
    return True

N = 2**60 - 1

# ---------- A. ord-criterion over all divisors of N ----------
ds = divisors(N)
assert len(ds) == 4608, len(ds)
mism = 0
for m in ds:
    if m == 1:
        continue
    o = order2mod(m)
    lhs = (o == 60)
    rhs = ((N % m == 0)
           and (2**12 - 1) % m != 0
           and (2**20 - 1) % m != 0
           and (2**30 - 1) % m != 0)
    if lhs != rhs:
        mism += 1
        print("  CRITERION MISMATCH m=", m, "ord=", o)
print("A. ord-criterion: divisors checked =", len(ds)-1, "mismatches =", mism)

# ---------- B. G-divisor-sums literals (own sigma/tau) ----------
def own_sigma(n):
    return sum(d for d in divisors(n))

checks = {
 "sigma(N)": own_sigma(N),
 "tau(N)": tau_brute(N),
 "sigma(4095)": own_sigma(2**12-1), "tau(4095)": tau_brute(2**12-1),
 "sigma(1048575)": own_sigma(2**20-1), "tau(1048575)": tau_brute(2**20-1),
 "sigma(1073741823)": own_sigma(2**30-1), "tau(1073741823)": tau_brute(2**30-1),
 "sigma(15)": own_sigma(15), "tau(15)": tau_brute(15),
 "sigma(63)": own_sigma(63), "tau(63)": tau_brute(63),
 "sigma(1023)": own_sigma(1023), "tau(1023)": tau_brute(1023),
 "sigma(3)": own_sigma(3), "tau(3)": tau_brute(3),
}
run = {
 "sigma(N)":3010983668199456768, "tau(N)":4608,
 "sigma(4095)":8736, "tau(4095)":24,
 "sigma(1048575)":1999872, "tau(1048575)":48,
 "sigma(1073741823)":2015330304, "tau(1073741823)":96,
 "sigma(15)":24, "tau(15)":4, "sigma(63)":104, "tau(63)":6,
 "sigma(1023)":1536, "tau(1023)":8, "sigma(3)":4, "tau(3)":2,
}
print("\nB. G-divisor-sums literals (own computation vs run's):")
all_ok = True
for k, mine in checks.items():
    rv = run[k]
    ok = (mine == rv)
    all_ok &= ok
    if not ok:
        print("  MISMATCH %s: run=%d own=%d" % (k, rv, mine))
print("B. all literals match:", all_ok)

# ---------- C. final answer via own sigma/tau + inclusion-exclusion ----------
S = (own_sigma(N) - own_sigma(2**12-1) - own_sigma(2**20-1) - own_sigma(2**30-1)
     + own_sigma(15) + own_sigma(63) + own_sigma(1023) - own_sigma(3))
C = (tau_brute(N) - tau_brute(2**12-1) - tau_brute(2**20-1) - tau_brute(2**30-1)
     + tau_brute(15) + tau_brute(63) + tau_brute(1023) - tau_brute(3))
print("\nC. inclusion-exclusion with OWN sigma/tau: C =", C, " S =", S,
      " answer =", S + C)
assert S + C == 3010983666182123972, (S, C)

# cross-check answer by direct enumeration over divisors of N
good = [m for m in ds if m > 1 and order2mod(m) == 60]
print("C2. direct enumeration: C =", len(good),
      " S =", sum(good), " answer =", sum(good) + len(good))

# ---------- D. R-sum8 worked example ----------
good8 = [m for m in divisors(2**8-1) if m > 1 and order2mod(m) == 8]
print("\nD. order-8 worked example: m with ord=8 =", good8,
      " sum(m+1) =", sum(m+1 for m in good8))
assert sum(m+1 for m in good8) == 412

# ---------- E. R-ord51-2 ----------
print("\nE. order of 2 mod 51 =", order2mod(51))
assert order2mod(51) == 8

print("\nALL ARITHMETIC CLAIMS RE-VERIFIED FROM FIRST PRINCIPLES.")
