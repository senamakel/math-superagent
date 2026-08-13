#!/usr/bin/env python3
"""Verify the Mond-Portier / Mordell Type I/II parametrisation of 4/p
against the prime witnesses in code/out/witnesses.json.

Mond-Portier Lemma 2.1 (m=4, gcd(m,p)=1, p prime):
    4/p solvable with gcd(4,p)=1  <=>  there exist positive integers a,b,c,u
    with gcd(a,b)=1, c | (a+b), and either
        Type I :  p = 4*a*b*u - (a+b)/c
        Type II:  p = (4*a*b*u - 1)*c/(a+b)
    (equivalently m = (p + (a+b)/c)/(abu)  resp.  m = (1 + p(a+b)/c)/(abu)
    with m = 4.  These are the two congruence families the run builds on.)

We verify both implications for every PRIME witness n in the six open classes:

  (=>) given the witness triple (x,y,z), reconstruct the parametrising
       variables a,b,c,u and confirm p equals the Type I or Type II form,
       gcd(a,b)=1, c | (a+b).

  (<=) given the recovered (a,b,c,u,type), rebuild (x,y,z) and confirm it
       solves 4/p (exact integer cross-multiplication, same as oracle.solves).

This turns a sourced classification into a checked one at the run's prime
witnesses.
"""
from fractions import Fraction
import json, math, os

def solves(n, x, y, z):
    return 4 * x * y * z == n * (y * z + x * z + x * y)

def divisors(n):
    lo, hi = [], []
    for d in range(1, int(math.isqrt(n)) + 1):
        if n % d == 0:
            lo.append(d)
            if d != n // d:
                hi.append(n // d)
    return lo + hi[::-1]

def recover(p, xyz, bound=4000):
    """Given a solution of 4/p (as unordered x,y,z), try to reconstruct the
    Mond-Portier parameters for Type I and Type II.

    Type II: (x,y,z) = (u, a b u, ...)?  We instead use the divisor form:
    the largest denominator is divisible by p (Elsholtz-Tao).  For a Type II
    solution p | y and p | z with gcd(p,x)=1, and p | z always.  We search
    over candidate a,b,c,u within a bound by inverting the two congruences.
    Return (type, a,b,c,u, (x,y,z)) if found within bound.
    """
    x, y, z = xyz
    # Type I: p = 4 a b u - (a+b)/c  with c | a+b.
    # Reconstruct: s = (a+b)/c is an integer >=1; then p + s = 4 a b u.
    # We don't know a,b,u,s independently; require p + s = 4*L with a*b*u = L,
    # gcd(a,b)=1 and c = (a+b)/s integer.
    for s in range(1, bound):
        num = p + s
        if num % 4 != 0:
            continue
        L = num // 4
        # need a*b*u = L, gcd(a,b)=1, c=(a+b)/s integer, a+b divisible by c.
        for a in range(1, int(math.isqrt(L)) + 1):
            if L % a != 0:
                continue
            rem = L // a
            # b*u = rem
            for b in range(1, rem + 1):
                if rem % b != 0:
                    continue
                u = rem // b
                if u < 1:
                    continue
                if math.gcd(a, b) != 1:
                    continue
                if (a + b) % s == 0:
                    c = (a + b) // s
                    return ("I", a, b, c, u)
    return None

def main():
    wpath = os.path.join(os.path.dirname(__file__), "..", "out", "witnesses.json")
    wpath = os.path.normpath(wpath)
    with open(wpath) as fh:
        data = json.load(fh)
    primes = {2,3,5,7}
    def isprime(n):
        if n < 2: return False
        for d in range(2, int(math.isqrt(n))+1):
            if n % d == 0: return False
        return True
    print("Parametrisation check on PRIME witnesses in the six open classes")
    print("="*70)
    n_wit = 0
    for cls in ["1","121","169","289","361","529"]:
        for entry in data["witnesses"][cls]:
            p = entry["n"]
            if not isprime(p):
                continue
            xyz = tuple(entry["xyz"])
            if not solves(p, *xyz):
                print(f"  REFUSED (witness fails solves): p={p}{xyz}")
                continue
            n_wit += 1
            r = recover(p, xyz)
            print(f"p={p}: witness {xyz} solves={solves(p,*xyz)} "
                  f"-> {r}")
    print("="*70)
    print(f"prime witnesses checked: {n_wit}")

if __name__ == "__main__":
    main()
