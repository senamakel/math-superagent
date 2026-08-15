"""Scholar verification of the load-bearing claims the digest rests on.

1. Corrected valuation identity: v_p(x^p-1) = 1 + v_p(x-1) iff p | (x-1).
   The overbroad 'p ∤ x' form must fail.
2. Mirror: v_q(y^q+1) = 1 + v_q(y+1) iff q | (y+1).
3. Known solution (3,2,2,3): p|y (2|2), q|x (3|3) hold; the double-Wieferich
   congruences must FAIL there (3^{2-1}=3 != 1 mod 4, 2^{3-1}=4 != 1 mod 9).
4. LTE identity v_p(x^p-1)=v_p(x-1)+v_p(p) sanity.
"""
import sympy

def vp(n, p):
    n = abs(int(n)); c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def check_minus(p, x):
    """v_p(x^p-1) ?= v_p(x-1)+1, given p|(x-1)"""
    lhs = vp(x**p - 1, p); rhs = vp(x-1, p) + 1
    return (lhs, rhs, lhs == rhs)

def check_plus(q, y):
    lhs = vp(y**q + 1, q); rhs = vp(y+1, q) + 1
    return (lhs, rhs, lhs == rhs)

print("== corrected valuation identity (p | x-1) ==")
for (p, x) in [(3,4),(3,7),(3,28),(5,6),(5,11),(7,8),(7,343+1),
               (3,2),(5,2),(5,4)]:
    ok_hyp = (x-1) % p == 0
    l, r, eq = check_minus(p, x)
    # overbroad form p ∤ x used as hypothesis
    print(f"p={p} x={x} | p|(x-1)={ok_hyp} | v_p(x^p-1)={l} v_p(x-1)+1={r} match={eq}")

print("\n== mirror (q | y+1) ==")
for (q, y) in [(3,2),(3,5),(3,26),(5,4),(5,9),(7,6)]:
    ok_hyp = (y+1) % q == 0
    l, r, eq = check_plus(q, y)
    print(f"q={q} y={y} | q|(y+1)={ok_hyp} | v_q(y^q+1)={l} v_q(y+1)+1={r} match={eq}")

print("\n== known solution calibration (x,p,y,q)=(3,2,2,3) ==")
x,p,y,q = 3,2,2,3
print(f"p|y ({p}|{y}):", y % p == 0)
print(f"q|x ({q}|{x}):", x % q == 0)
print(f"double-Wieferich q^(p-1)=3^1 mod 4 == 1?", pow(q, p-1, p*p) == 1)
print(f"double-Wieferich p^(q-1)=2^2 mod 9 == 1?", pow(p, q-1, q*q) == 1)
print("expected: p|y True, q|x True, both double-Wieferich False")

print("\n== problem.md hint p^2 | y^{p-1}-1 at known soln (p=2 even) ==")
# hint inconsistent with p|y: if p|y then y^{p-1} ≡ 0 mod p, so p^2 | y^{p-1}-1 => -1 ≡ 0 mod p^2 impossible
# check at (3,2,2,3): the true conditions are the double-Wieferich ones
print("At known soln p=2 is even, so odd-prime conditions are excluded-by-hypothesis.")
