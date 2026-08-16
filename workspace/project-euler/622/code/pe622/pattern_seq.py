#!/usr/bin/env python3
"""Extract the integer sequences behind PE622 for pattern analysis.

s(n) = ord_{n-1}(2).  We need odd m = n-1 with ord_m(2)=60, then sum n = m+1.

Enumerate over divisors of N = 2^60 - 1 (fast, no unbounded scan).  Also emit
the sequence of GOOD m (candidates), the resulting n = m+1, and the count/sum.
Additionally emit the sequence of counts C(k) = #{m : ord_m(2)=k} and sums
S(k) over divisors of 2^k - 1 for small k, to look for structure.
"""
import sympy


def good_m_for(order):
    N = 2**order - 1
    good = []
    for m in sympy.divisors(N):
        if m > 1 and sympy.n_order(2, m) == order:
            good.append(m)
    return good


# --- target: order 60 ---
good60 = good_m_for(60)
n60 = [m + 1 for m in good60]
print("order 60: count C =", len(good60))
print("candidate m  =", good60)
print("candidate n  =", n60)
print("sum of m   S =", sum(good60))
print("sum of n     =", sum(n60))
print()

# --- sequence of counts/sums over small orders k ---
print("k : C(k)  S(k)  sum_n(k)")
for k in range(1, 25):
    good = good_m_for(k)
    C = len(good)
    S = sum(good)
    print(k, C, S, S + C)
