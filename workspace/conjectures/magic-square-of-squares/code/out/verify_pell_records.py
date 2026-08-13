#!/usr/bin/env python3
"""Verify the Pell-pair structure of Phi's largest values.

Claims from scratch/phi.py to test:
  C1.  For Pell numbers P_1=1,P_2=2,P_3=5,... the pair (m,n)=(P_k,P_{k-1})
       satisfies  f(m,n) = 1 - 1/P_{2k-1}^2   EXACTLY for all k.
  C2.  Over the box {primitive m>n>=1, m<=M}, the global max of f is attained
       at a consecutive Pell pair (P_k, P_{k-1}), for each M.
  C3.  f(m,n) < 1 for all integer m>n>=1 (sup=1 at irrational t=tan(pi/8)),
       and in particular every f in Phi lies in (0,1).

All exact integer arithmetic.
"""
from math import gcd, isqrt


def f_pair(m, n):
    m2, n2 = m * m, n * n
    num = 4 * m * n * (m2 - n2)
    den = (m2 + n2) ** 2
    g = gcd(num, den)
    return (num // g, den // g)


def pell(k):
    if k <= 1:
        return 1
    p0, p1 = 1, 2
    for _ in range(2, k):
        p0, p1 = p1, 2 * p1 + p0
    return p1


def sqrt_ok(x):
    r = isqrt(x)
    return r * r == x


# --- C1: verify the closed form f(P_k,P_{k-1}) = 1 - 1/P_{2k-1}^2 ---
print("C1: f(P_k,P_{k-1}) == 1 - 1/P_{2k-1}^2")
bad = 0
for k in range(2, 60):
    m, n = pell(k), pell(k - 1)
    A, B = f_pair(m, n)
    P = pell(2 * k - 1)
    # 1 - 1/P^2 = (P^2-1)/P^2
    rhs = (P * P - 1, P * P)
    if (A, B) != rhs:
        bad += 1
        print(f"  k={k}: f={A}/{B} rhs={rhs[0]}/{rhs[1]} MISMATCH")
print(f"  C1 {'PASS' if bad == 0 else str(bad)+' FAILS'} (k=2..59)")
# also verify the supporting identity P_{2k-1} = P_k^2 + P_{k-1}^2
b2 = 0
for k in range(2, 60):
    if pell(2 * k - 1) != pell(k) ** 2 + pell(k - 1) ** 2:
        b2 += 1
print(f"  supporting identity P_{{2k-1}}=P_k^2+P_{{k-1}}^2: "
      f"{'PASS' if b2==0 else str(b2)+' FAILS'}")

# --- C2: is the global max over m<=M attained at a Pell pair? ---
print("\nC2: argmax of f over primitive m>n>=1, m<=M")
prev_k = None
for M in (20, 100, 500, 1000):
    best_num, best_den, best_pair = -1, 1, None
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            A, B = f_pair(m, n)
            if A * best_den > best_num * B:
                best_num, best_den, best_pair = A, B, (m, n)
    # is best_pair a consecutive Pell pair (P_k,P_{k-1})?
    k_found = None
    for k in range(2, 60):
        if best_pair == (pell(k), pell(k - 1)):
            k_found = k
            break
    print(f"  M={M}: argmax={best_pair} = {best_num}/{best_den}"
          f"{'  = (P_%d,P_%d) PELL'%(k_found,k_found-1) if k_found else '  NOT A PELL PAIR'}")
    if k_found:
        prev_k = k_found

# --- C3: f < 1 for all primitive m>n>=1, over a big box ---
print("\nC3: f(m,n)<1 over m<=5000 box")
worst = (0, 1, None)
for m in range(2, 5001):
    m2 = m * m
    for n in range(1, m):
        A, B = f_pair(m, n)
        if A >= B:
            print(f"  VIOLATION at ({m},{n}): {A}/{B} >= 1")
            raise SystemExit(1)
        if A * worst[1] > worst[0] * B:
            worst = (A, B, (m, n))
print(f"  max f over m<=5000 = {worst[0]}/{worst[1]} at {worst[2]} "
      f"(=1-1/{isqrt(worst[1])}^2 if sqrt-den is integer)")
print("  C3 PASS (no f>=1 found)")
