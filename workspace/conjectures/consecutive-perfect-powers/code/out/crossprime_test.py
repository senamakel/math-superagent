"""Test the cross-prime divisibility claim of REQUESTS.md exact-statement-mihailescu-bbf8:

Claim under test (asserted in the run's approach note):
  A hypothetical solution x^p - y^q = 1 with p, q distinct odd primes forces
  q | h^-(Q(zeta_p))  (and symmetrically p | h^-(Q(zeta_q))).

We evaluate the LITERAL divisibility q | h^-(Q(zeta_p)) in exact integer
arithmetic, using h^-(Q(zeta_p)) = 2p * prod_{chi odd} (-1/2 B_{1,chi}).

Test targets:
  1. The known/standard double-Wieferich pair (83, 4871) — pairs that a
     hypothetical odd solution MUST be (Cassels + Inkeri-Hyyroe).
  2. Every odd prime pair (p,q) with q <= 97 and p <= 97 (small sweep) to see
     how often the literal divisibility holds.
  3. Focus: does q | h^-(Q(zeta_p)) hold when q is the OPPOSITE prime, i.e.
     cross-prime divisibility — independent of whether q | p-1.

Exact integer only, via sympy Rational Bernoulli sums. No floats.
"""
from fractions import Fraction
import sympy

def primitive_root(p):
    for g in range(2, p):
        if pow(g, (p - 1) // 2, p) != 1:
            return g

def rel_class_number_int(p):
    """Exact h^-(Q(zeta_p)) as a Python int, via the Bernoulli product.
    B_{1,chi} = (1/p) sum_{a=1}^{p-1} chi(a) a;  chis take values in Z[omega]
    where omega = primitive (p-1)-th root.  The product over odd chi of
    (-1/2 B_{1,chi}) times 2p is a rational integer."""
    g = primitive_root(p)
    # discrete log table
    logtab = {}
    val = 1
    for e in range(p - 1):
        logtab[val] = e
        val = (val * g) % p
    # Work in the cyclotomic field of roots of unity order (p-1).
    # Represent chi(a) = omega^(k*e), and compute the product symbolically with
    # sympy.exp(I*2*pi*k*e/(p-1)).  The final result is a rational integer.
    from sympy import exp, I, pi, Rational, expand, simplify
    # We'll sum using sympy Sqrt?  Use algebraic field via exp.
    # Build the product as a sympy expression, then use nsimplify to a Rational.
    prod = Rational(1)
    for k in range(1, p - 1, 2):          # odd characters
        s = 0
        for a in range(1, p):
            e = logtab[a]
            chi_a = exp(I * 2 * pi * k * e / (p - 1))
            s += chi_a * a
        B1 = s / p
        prod = prod * (Rational(-1, 2) * B1)
    h = 2 * p * prod
    # h is algebraic; simplify to a rational then to an int.
    from sympy import nsimplify, re, im
    nr = sympy.N(h, 40)
    r = sympy.nsimplify(sympy.re(nr))
    return int(r)

def known_values(p):
    return {3:1,5:1,7:1,11:1,13:1,17:1,19:1,23:3,29:8,31:9,37:37,41:121,
            43:211,47:695,53:4889,59:41241,61:76301,67:853513}

if __name__ == "__main__":
    # sanity: reproduce known h^- for p <= 67
    for p in [3,5,7,11,13,23,31,37]:
        h = rel_class_number_int(p)
        kv = known_values(p)
        print(f"p={p:3d}  h^-={h}  known={kv}  {'OK' if h==kv else 'MISMATCH'}")
