#!/usr/bin/env python3
"""PE622 solution: sum of even n with s(n)=60.

s(n) = ord_{n-1}(2) (Diaconis-Graham-Kantor).  So we need all odd m = n-1 with
ord_m(2)=60, then sum n = m+1.

ord_m(2)=60  <=>  m | 2^60 - 1  AND  no proper divisor d of 60 has 2^d == 1 (mod m).
"""
import sympy


def solve(order=60):
    M = 2**order - 1
    divisors = sympy.divisors(M)
    total = 0
    count = 0
    for m in divisors:
        if sympy.n_order(2, m) == order:
            n = m + 1
            total += n
            count += 1
    return count, total


count8, sum8 = solve(8)
print("order 8: count =", count8, "sum of n =", sum8)
assert sum8 == 412, sum8

count60, sum60 = solve(60)
print("order 60: count =", count60)
print("ANSWER sum of n =", sum60)

# Independent route: directly use the minimal-power criterion without n_order.
def ord_min(m, order=60):
    # exact order == order iff 2^order==1 mod m and no proper divisor d works
    if (2**order - 1) % m != 0:
        return False
    for d in sympy.divisors(order):
        if d == order:
            continue
        if (2**d - 1) % m == 0:
            return False
    return True


M = 2**60 - 1
total2, count2 = 0, 0
for m in sympy.divisors(M):
    if ord_min(m):
        total2 += m + 1
        count2 += 1
print("independent route: count =", count2, "sum =", total2)
assert total2 == sum60 and count2 == count60
print("Both routes agree.")
