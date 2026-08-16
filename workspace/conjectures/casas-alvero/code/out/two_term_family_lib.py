"""Independent lib-oracle confirmation of the two-term-FAMILY submask law.

Family F(a,n) = x^a (x+1)^{n-a} over F2 (NOT the 2-monomial x^a+x^n; this
expands to popcount(n-a)+1 monomials in general).  Conjecture:
   F(a,n) is a Hasse-CA counterexample  iff  a is a proper nonempty submask
   of n (a's set bits subset of n's set bits, 1<=a<=n-1).

Uses lib.casas_alvero.is_ca_hasse / is_pure_power (sympy) as the independent
route (two_term_rule.py used the bit-parallel is_ca_f2).  Computes
x^a*(x+1)^(n-a) exactly over GF(2).
"""
import sys
from math import comb
from sympy import symbols, Poly, GF, expand
from lib.casas_alvero import is_ca_hasse, is_pure_power

x = symbols("x")

def submask(n, a):
    return (a & ~n) == 0

def build_family(a, n):
    # expand x^a (x+1)^{n-a} over GF(2) exactly
    base = Poly((x + 1) ** (n - a), x, domain=GF(2))
    f = Poly((x ** a) * base.as_expr(), x, domain=GF(2))
    return f

def main(nmax):
    ok = True
    for n in range(3, nmax + 1):
        for a in range(1, n):
            f = build_family(a, n)
            ce = is_ca_hasse(f, 2) and not is_pure_power(f, 2)
            expect = submask(n, a)
            if ce != expect:
                print(f"BREAK n={n} a={a}: expect={expect} got={ce}")
                ok = False
    print(f"two-term-FAMILY submask law n=3..{nmax}: "
          f"{'PASS (lib route)' if ok else 'FAIL'}")
    return ok

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 30)
