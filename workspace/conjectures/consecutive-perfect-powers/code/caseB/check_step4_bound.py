#!/usr/bin/env python3
"""Verify the crux of the Lebesgue elementary proof (step 4):

    |Im((c +/- i)^p)| >= 2  for all integers c >= 1, p odd prime >= 3.

This is the claim that lets us conclude, from Im((c+di)^p) = 1 and d = +/-1,
that c must be 0. If instead |Im((c±i)^p)| could be 1 for some c >= 1, the
elementary proof fails; this program hunts for exactly that.

Exact integer arithmetic throughout (Python ints + lib.gaussint). Not a proof
of the unbounded claim -- a numerical falsifier over a large box, plus a check
of the two structural sub-cases:
  c = 1  : Im((1+i)^p) = ±2^((p-1)/2), |.| >= 2 always.
  c >= 2 : leading binomial term is p·c^{p-1}, tail is much smaller (checked
           below over the box); no |.| < 2 found.
"""

import sys
import lib.gaussint as gi


def odd_primes_below(n):
    out = []
    for p in range(3, n, 2):
        ok = True
        for d in range(3, int(p ** 0.5) + 1, 2):
            if p % d == 0:
                ok = False
                break
        if ok:
            out.append(p)
    return out


def main():
    cmax = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    pmax = int(sys.argv[2]) if len(sys.argv) > 2 else 401
    primes = odd_primes_below(pmax + 1)

    min_abs = None
    violations = []          # (c, p, Im) with |Im| < 2
    hits_one = []            # (c, p, Im) with Im == +/-1

    # structural check for c = 1: Im((1+i)^p) = +/- 2^((p-1)/2)
    c1_ok = True
    for p in primes:
        im = gi.binom_re_im((1, 1), p)[1]
        if abs(im) != 2 ** ((p - 1) // 2):
            c1_ok = False

    n_pairs = 0
    for c in range(1, cmax + 1):
        for p in primes:
            n_pairs += 1
            im = gi.binom_re_im((c, 1), p)[1]
            a = abs(im)
            if min_abs is None or a < min_abs:
                min_abs = a
            if a < 2:
                violations.append((c, p, im))
            if a == 1:
                hits_one.append((c, p, im))

    print(f"box: c in [1,{cmax}], odd primes p in [3,{pmax}]  ({len(primes)} primes, "
          f"{n_pairs} pairs)")
    print(f"c=1 structural: |Im((1+i)^p)| = 2^((p-1)/2) for all p?  {c1_ok}")
    print(f"minimum |Im((c+i)^p)| over the box: {min_abs}")
    print(f"violations (|Im|<2):  {len(violations)}")
    print(f"hits |Im|==1:         {len(hits_one)}")
    if violations:
        print("  first violations:", violations[:10])
    if hits_one:
        print("  first hits ==1:", hits_one[:10])

    ok = c1_ok and len(violations) == 0
    print("VERDICT:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
