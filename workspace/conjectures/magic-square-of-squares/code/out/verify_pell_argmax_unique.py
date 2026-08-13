#!/usr/bin/env python3
"""Confirm the Pell-record structure of Phi's largest values:
  (1) the DERIVED identity f(P_k,P_{k-1}) = 1 - 1/P_{2k-1}^2, i.e.
      (m^2+n^2)^2 - 4mn(m^2-n^2) = 1 for consecutive Pell pairs (this is the
      exact algebra behind the record; verify it directly);
  (2) argmax of f over m<=M is a single consecutive Pell pair (uniqueness),
      with NO tie, for M up to a few thousand, and records are strictly
      increasing.
"""
from math import gcd

def pell(k):
    if k <= 1: return 1
    p0, p1 = 1, 2
    for _ in range(2, k):
        p0, p1 = p1, 2*p1 + p0
    return p1

def f_pair(m, n):
    m2, n2 = m*m, n*n
    num = 4*m*n*(m2-n2); den = (m2+n2)**2
    g = gcd(num, den)
    return (num//g, den//g)

# (1) exact algebra
print("(1) Pell algebra: (m^2+n^2)^2 - 4mn(m^2-n^2) == 1 for (P_k,P_{k-1})")
bad = 0
for k in range(2, 80):
    m, n = pell(k), pell(k-1)
    if (m*m+n*n)**2 - 4*m*n*(m*m-n*n) != 1:
        bad += 1; print(f"  k={k} FAIL")
print(f"   {'PASS' if bad==0 else str(bad)+' FAILS'}  k=2..79")
# also the reduced form is exactly 1 - 1/P_{2k-1}^2
bad2 = 0
for k in range(2, 80):
    A, B = f_pair(pell(k), pell(k-1))
    t = pell(2*k-1)
    if (A,B) != (t*t-1, t*t):
        bad2 += 1
print(f"   reduced == 1-1/P_{{2k-1}}^2: {'PASS' if bad2==0 else str(bad2)+' FAILS'}")

# (2) argmax uniqueness over several M, and strict increase of records
print("\n(2) argmax uniqueness & strictly increasing record f")
last_v = None
for M in (30, 60, 120, 240, 480, 960, 1920):
    best = (0, 1, None); ties = []
    for m in range(2, M+1):
        for n in range(1, m):
            A, B = f_pair(m, n)
            if A*best[1] > best[0]*B:
                best = (A, B, (m,n)); ties = [(m,n)]
            elif A*best[1] == best[0]*B:
                ties.append((m,n))
    # classify best as Pell pair
    k_ = None
    for k in range(2, 40):
        if best[2] == (pell(k), pell(k-1)):
            k_ = k; break
    val = best[0]/best[1]
    if last_v is not None:
        strict = val > last_v
    else:
        strict = True
    last_v = val
    print(f"  M<= {M:5d}: argmax {best[2]} = {best[0]}/{best[1]} "
          f"({'PELL P_%d'%(k_) if k_ else 'NOT PELL'}) "
          f"ties={len(ties)-1} record-strictly-increasing={strict}")
