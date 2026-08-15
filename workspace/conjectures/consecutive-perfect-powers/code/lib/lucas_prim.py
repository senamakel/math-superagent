"""Lucas-sequence / primitive-prime-divisor machinery for x^p - y^q = 1.

Imports: `from lib.lucas_prim import (lucas_U, phi_p, phi_q_neg,
gcd_lemma_value, primitive_prime_divisor, primitive_prime_divisor_mirror)`.

Exact integer arithmetic only (Python ints, sympy for symbolic identities and
for factorisation). No floats.

The two Lucas identities at the base of the approach:
    Phi_p(x)   = (x^p - 1)/(x - 1)  ==  U_p(x + 1, x)
    Phi_q(-y)  = (y^q + 1)/(y + 1)  ==  U_q(y - 1, -y)      (q odd)
where U_n is the Lucas sequence U_0=0, U_1=1, U_{k+1} = P U_k - Q U_{k-1},
whose n-th term is (a^n - b^n)/(a - b) with a,b the roots of z^2 - P z + Q = 0
(a = x, b = 1 for the first; a = y, b = -1 for the second).  The second
identity uses Phi_q(-y) = ((-y)^q - 1)/((-y) - 1).

The primitive-divisor (Zsigmondy/BHV) claim: for odd prime p and x >= 2,
Phi_p(x) has a primitive prime divisor r: r | Phi_p(x), r does not divide
(x - 1), and the order of x mod r is exactly p, hence r ≡ 1 (mod p).  Since
for a solution y^q = (x - 1) Phi_p(x), such r divides y.  The mirror
Phi_q(-y) for q odd, y >= 1, has a primitive divisor s | Phi_q(-y) with
s ∤ (y + 1) and s ≡ 1 (mod q); for a solution x^p = (y + 1) Phi_q(-y), s | x.

Correctness: verified (this run) against the brute-force/Lucas identities on
ranges in code/primitive_div/verify_primitive_div.py and its captured output
code/out/primitive_div.captured.txt.
"""
import sympy as sp


def lucas_U(n, P, Q):
    """The n-th Lucas term with U_0=0, U_1=1, U_{k+1} = P U_k - Q U_{k-1}.
    Returns exact int when P, Q are ints, else a sympy expression (expanded:
    each step calls sp.expand, so the return is a fully-expanded polynomial).
    Verify: U_n = (a^n - b^n)/(a - b) for roots a, b of z^2 - P z + Q = 0."""
    U0, U1 = 0, 1
    if n == 0:
        return 0
    for _ in range(2, n + 1):
        U0, U1 = U1, sp.expand(P * U1 - Q * U0)
    return U1


def phi_p(p, x):
    """(x^p - 1)/(x - 1) as an exact integer; p >= 2, x >= 2."""
    return (x ** p - 1) // (x - 1)


def phi_q_neg(q, y):
    """(y^q + 1)/(y + 1) as an exact integer; q an odd integer >= 3, y >= 1.
    Equals ((-y)^q - 1)/((-y) - 1), i.e. Phi_q evaluated at -y."""
    return (y ** q + 1) // (y + 1)


def gcd_lemma_value(p, x):
    """Return (gcd(x-1, Phi_p(x)), gcd(x-1, p)); these are equal for p an odd
    prime (the gcd lemma). Exact integer arithmetic."""
    from math import gcd
    return (gcd(x - 1, phi_p(p, x)), gcd(x - 1, p))


def primitive_prime_divisor(p, x):
    """Find a primitive prime divisor r of Phi_p(x) for odd prime p, x >= 2.

    Returns (r, factors): r | Phi_p(x), r does not divide (x-1), order of x
    mod r is exactly p (so r ≡ 1 (mod p)); factors = sympy.factorint(Phi_p(x)).
    If no such r exists (should not happen for odd prime p, x >= 2 by
    Zsigmondy/BHV), returns (None, factors).  Exact integers throughout.

    Why r ∤ (x-1) implies order exactly p: r | Phi_p(x) | x^p - 1, so the
    order of x mod r divides the prime p; it is 1 iff x ≡ 1 (mod r) iff
    r | (x-1).  So a prime r | Phi_p(x) with r ∤ (x-1) automatically has
    order p and satisfies r ≡ 1 (mod p); both are asserted inside."""
    facts = sp.factorint(phi_p(p, x))
    for r in sorted(facts):
        if (x - 1) % r != 0:
            assert pow(x % r, p, r) == 1          # order divides p
            assert pow(x % r, 1, r) != 1           # order != 1 (primitive)
            assert r % p == 1                      # r ≡ 1 (mod p)
            return r, facts
    return None, facts


def primitive_prime_divisor_mirror(q, y):
    """Find a primitive divisor s of Phi_q(-y) = (y^q + 1)/(y + 1) for odd q,
    y >= 1.  Returns (s, factors) with s | Phi_q(-y), s ∤ (y+1), order of
    (-y) mod s exactly q (so s ≡ 1 (mod q)); factors = factorint(Phi_q(-y)).
    Returns (None, factors) if none (exceptional cases exist, e.g. q=3, y=2:
    Phi_3(-2)=3, order of -2 mod 3 is 1).  Exact integers."""
    facts = sp.factorint(phi_q_neg(q, y))
    for s in sorted(facts):
        if (y + 1) % s != 0:
            assert pow((-y) % s, q, s) == 1        # (-y)^q ≡ 1 (mod s)
            assert pow((-y) % s, 1, s) != 1         # order != 1 (primitive)
            assert s % q == 1                       # s ≡ 1 (mod q)
            return s, facts
    return None, facts
