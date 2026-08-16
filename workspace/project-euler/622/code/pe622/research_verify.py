"""Verify the arithmetic claims behind each proposed approach before grounding.

Checks:
1. 2^60-1 factorization and the order of 2 mod each of the 11 primes.
2. Wieferich lift condition: v_p(2^ord_p(2) - 1) == 1 for each prime (so
   ord_{p^a}(2) = ord_p(2)*p^(a-1) for all a), and that only 3,5 have a>=2.
3. The order-6 class really is empty (63 = 3^2*7, orders 2 and 3).
4. The Mobius-inversion identity S(k) = sum_{d|k} mu(k/d)(sigma(2^d-1)-1)
   evaluated at k=60 against direct enumeration, to confirm the S(60) value.
"""
import sympy

N = 2**60 - 1
print("2^60-1 =", N)
fac = sympy.factorint(N)
print("factorization:", fac)
print("tau =", sympy.divisor_count(N))

def ord_mod(prime, base=2):
    d = 1
    x = base % prime
    while x != 1:
        x = (x * base) % prime
        d += 1
    return d

# primes sorted by exponent in factorisation
primes = sorted(fac.keys())
print("\nPer prime: order of 2, v_p(2^ord-1), exponent in N, ord_{p^a} for max a")
orders = {}
for p in primes:
    d = ord_mod(p)
    orders[p] = d
    # v_p(2^d - 1)
    v = 0
    t = 2**d - 1
    while t % p == 0:
        t //= p
        v += 1
    a = fac[p]
    lifted = d * p**(a-1)
    print(f"p={p:5d} ord={d:3d}  v_p(2^ord-1)={v}  exp_in_N={a}  ord_{{p^{a}}}= {lifted}")

print("\norder-6 class check: 2^6-1 =", 2**6-1, "=", sympy.factorint(2**6-1))
for p in sympy.factorint(2**6-1).keys():
    print(f"  ord_{p}(2) = {ord_mod(p)}")

# Zsigmondy: for each d|60, d>=2, d!=6, phi_d(2) has a primitive prime divisor
# (order d). Check existence: a prime p whose order mod p equals d.
print("\nZsigmondy class-nonempty check for each d|60:")
s = sympy
divs = sorted(d for d in sympy.divisors(60))
for d in divs:
    if d == 1:
        continue
    # find a prime divisor of 2^d-1 with order exactly d (primitive)
    found = None
    for p in sympy.factorint(2**d - 1):
        if ord_mod(p) == d:
            found = p
            break
    print(f"  d={d:3d}: primitive order-d prime = {found}")

# Mobius-inversion identity S(k) at k=60, cross-check
from sympy import divisor_sigma, mobius, divisors
def S_mobius(k):
    total = 0
    for d in divisors(k):
        total += mobius(k//d) * (divisor_sigma(2**d - 1) - 1)
    return total
print("\nMobius S(60) =", S_mobius(60))
# direct enumeration of m | 2^60-1 with ord_m(2)=60
def ord_mod_m(m, base=2):
    d = 1; x = base % m
    while x != 1:
        x = (x*base) % m; d += 1
    return d
S_direct = 0; C_direct = 0
for m in sympy.divisors(N):
    om = ord_mod_m(m)
    if om == 60:
        S_direct += m
        C_direct += 1
print("Direct S(60) =", S_direct, " C(60) =", C_direct)
print("ANSWER = S + C =", S_direct + C_direct)
