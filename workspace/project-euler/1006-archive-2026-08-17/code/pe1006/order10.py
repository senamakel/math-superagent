from sympy import factorint, mod_inverse
import sympy

M = 101001001
print("M factor:", factorint(M))
# Euler's totient of each prime power and lcm
fac = factorint(M)
phi_pk = [p**(e-1)*(p-1) for p, e in fac.items()]
from math import lcm
totient = 1
for v in phi_pk:
    totient = lcm(totient, v)
print("lambda(M) (carmichael) candidate:", totient)

# order of 10 mod M
# find by testing divisors of lambda
def divisors(n):
    out = set([1])
    for p, e in factorint(n).items():
        new = set()
        pp = 1
        for i in range(e+1):
            for d in out:
                new.add(d*pp)
            pp *= p
        out = new
    return sorted(out)

lam = totient
order = None
for d in divisors(lam):
    if pow(10, d, M) == 1:
        order = d
        break
print("order of 10 mod M =", order)

# Pisano period of Fibonacci mod M for comparison
def pisano(m):
    a, b = 0, 1
    period = 0
    seen = {}
    while True:
        key = (a, b)
        if key in seen:
            return period - seen[key]
        seen[key] = period
        a, b = b, (a+b) % m
        period += 1

print("pisano period mod M =", pisano(M))
# factor of pisano
print("pisano factor:", factorint(pisano(M)))
# lcm of order-10 and pisano-related
lc = 1
lc = lcm(lc, order)
print("lcm(order_10, ...)=", lc)
