#!/usr/bin/env python3
"""Probe the two facts that make step 4 (|Im((c+i)^p)| >= 2 for |c|>=1,
p odd prime) provable elementarily:

  (E) evenness:   Im((c+i)^p) is even for all integers c, odd prime p>=3.
      reason: Im = sum_j (-1)^j C(p,2j+1) c^{p-2j-1}; mod 2 all signs vanish,
      sum of odd binomial coefficients is 2^{p-1} which is even for p>=3.

  (N) nonzero:    Im((c+i)^p) != 0 for c != 0.
      reason: if Im=0 then (c+i)^p=(c-i)^p so alpha=((c+i)/(c-i)) satisfies
      alpha^p=1, a root of unity in Q(i); the only roots of unity in Q(i) are
      {1,-1,i,-i}, none of which satisfies z^p=1 for odd prime p>=3 except
      z=1, and z=1 would force i=-i.

Verified here numerically over a box as a check of (E) and (N); the proof is
the parity/binomial sum + roots-of-unity-in-Q(i) argument above.
"""
import sys
import lib.gaussint as gi


def odd_primes(n):
    out = []
    for p in range(3, n + 1, 2):
        ok = True
        for d in range(3, int(p ** 0.5) + 1, 2):
            if p % d == 0:
                ok = False
                break
        if ok:
            out.append(p)
    return out


def main():
    cmax = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    pmax = int(sys.argv[2]) if len(sys.argv) > 2 else 401
    primes = odd_primes(pmax)

    even_fail = []     # (c,p) with Im odd
    nonzero_fail = []  # (c,p), c!=0, with Im == 0
    n = 0
    for c in range(-cmax, cmax + 1):
        if c == 0:
            continue
        for p in primes:
            n += 1
            im = gi.binom_re_im((c, 1), p)[1]
            if im % 2 != 0:
                even_fail.append((c, p, im))
            if im == 0:
                nonzero_fail.append((c, p))
    print(f"c in [-{cmax},{cmax}]\\{{0}}, odd primes in [3,{pmax}] ({len(primes)}): "
          f"{n} pairs")
    print(f"(E) evenness:  failures = {len(even_fail)}  {even_fail[:5]}")
    print(f"(N) nonzero:   failures = {len(nonzero_fail)}  {nonzero_fail[:5]}")
    # binomial parity identity independent check: sum_{j} C(p,2j+1) == 2^{p-1}
    import math
    ident_ok = all(sum(math.comb(p, 2*j+1) for j in range((p+1)//2)) == 2**(p-1)
                   for p in primes)
    print(f"(E) sum of odd binomial coefficients = 2^(p-1) for all p? {ident_ok}")
    ok = not even_fail and not nonzero_fail and ident_ok
    print("VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
