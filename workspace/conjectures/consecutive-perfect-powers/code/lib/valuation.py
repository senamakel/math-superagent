"""Exact-integer valuation (LTE) helpers for the consecutive-perfect-powers
problem x^p - y^q = 1.

Imports: `from lib.valuation import v_p, lte_valuations_x, lte_valuations_y,
solutions`.

All arithmetic is exact integer arithmetic; no floats, no logs.

The two identities verified here are the valuation engine of the Cassels
divisibility step (G-odd-Cassels: p|y and q|x for an odd-prime solution).

For an odd prime p and integer x:
    v_p(x^p - 1) = v_p(x - 1) + [ p | (x-1) ]          (x-side, minus form)
For an odd prime q and integer y:
    v_q(y^q + 1) = v_q(y + 1) + [ q | (y+1) ]          (y-side, plus form)
where [P] is 1 if P holds else 0.

Justification (LTE): x^p-1 = (x-1)(1+x+...+x^{p-1}); if p | (x-1) then
1+x+...+x^{p-1} ≡ p (mod p^2), contributing exactly one more power of p, giving
v_p(x^p-1) = v_p(x-1)+1. If p \nmid (x-1) then x ≢ 1 (mod p) and Fermat gives
1+x+...+x^{p-1} ≡ 1 (mod p), so v_p(x^p-1) = v_p(x-1). The plus form is the
analogue with an alternating geometric sum (q odd). The overbroad hypothesis
"p \nmid x" is FALSE (p=3, x=2: 3 \nmid 2 but v_3(2^3-1)=v_3(7)=0, not 1); the
correct hypothesis is the LTE congruence x ≡ 1 (mod p) / y ≡ -1 (mod q).
"""


def v_p(n, p):
    """p-adic valuation of a nonzero integer n, exact.
    Raises ValueError on n == 0 (0 has infinite valuation)."""
    if n == 0:
        raise ValueError("v_p of 0 is undefined")
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def lte_xside(p, x):
    """Return (lhs, rhs, p_divides_xm1):
        lhs = v_p(x^p - 1)
        rhs = v_p(x - 1) + (1 if p | (x-1) else 0)
        p_divides_xm1 = (p | (x-1))
    and lhs == rhs when the (corrected) LTE hypothesis applies.
    p must be an odd prime and x >= 2 an integer with p \nmid x (so x-1 has
    finite p-adic self-consistency; x^p-1 and x-1 are both nonzero)."""
    assert p >= 3
    lhs = v_p(x ** p - 1, p)
    rhs = v_p(x - 1, p) + (1 if (x - 1) % p == 0 else 0)
    return lhs, rhs, (x - 1) % p == 0, x == 0 or x % p != 0  # last: p\nmid x


def lte_yside(q, y):
    """Return (lhs, rhs, q_divides_yplus1):
        lhs = v_q(y^q + 1)
        rhs = v_q(y + 1) + (1 if q | (y+1) else 0)
        q_divides_yplus1 = (q | (y+1))
    q an odd prime, y >= 1."""
    assert q >= 3 and y >= 1
    if y ** q + 1 == 0:
        raise ValueError("y^q+1 = 0")
    lhs = v_p(y ** q + 1, q)
    rhs = v_p(y + 1, q) + (1 if (y + 1) % q == 0 else 0)
    return lhs, rhs, (y + 1) % q == 0


def is_prime(n):
    """Trial-division primality, exact; n small in all uses here."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def perfect_powers_upto(N):
    """value -> [(base, exp)] for all perfect powers value=base^exp, base>=2,
    exp>=2, value <= N. Exact integer arithmetic only."""
    powers = {}
    x = 2
    while x * x <= N:
        v = x * x
        e = 2
        while v <= N:
            powers.setdefault(v, []).append((x, e))
            v *= x
            e += 1
        x += 1
    return powers


def solutions(N):
    """All (x,p,y,q), x,y>0, p,q>1, with x^p, y^q <= N and x^p - y^q = 1,
    by exact integer arithmetic. Must equal exactly {(3,2,2,3)} for every
    reachable N >= 9 (the oracle target)."""
    powers = perfect_powers_upto(N)
    result = set()
    for u in powers:          # u = x^p
        if u - 1 in powers:   # u - 1 = y^q
            for (x, p) in powers[u]:
                for (y, q) in powers[u - 1]:
                    if x ** p - y ** q == 1:
                        result.add((x, p, y, q))
    return sorted(result)
