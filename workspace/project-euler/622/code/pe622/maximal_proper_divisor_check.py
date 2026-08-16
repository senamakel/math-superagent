#!/usr/bin/env python3
"""Verify the structural coincidence that powers the PE622 inclusion-exclusion:
every proper divisor of 60 divides one of its MAXIMAL proper divisors
{30,20,12}.  Then ask how general it is across k.
"""
import sympy


def maximal_proper_divisors(k):
    """d|k, d<k, and d does not divide any larger proper divisor of k."""
    props = [d for d in sympy.divisors(k) if 0 < d < k]
    maximal = [d for d in props
               if not any(e > d and e % d == 0 for e in props)]
    return maximal


def every_divisor_divides_some_maximal(k):
    maxs = maximal_proper_divisors(k)
    props = [d for d in sympy.divisors(k) if 0 < d < k]
    return all(any(m % d == 0 for m in maxs) for d in props)


def main():
    k = 60
    maxs = maximal_proper_divisors(k)
    print(f"maximal proper divisors of {k}: {maxs}")
    ok = every_divisor_divides_some_maximal(k)
    print(f"every proper divisor of {k} divides one of these? {ok}")
    if ok:
        print("  -> order-k set = divisors(N) \\ (union of A_m over maximal m),"
              "\n     a 2^{len(maxs)} inclusion-exclusion (only true maximal "
              "divisors matter).")
    print()

    good = [kk for kk in range(2, 121) if every_divisor_divides_some_maximal(kk)]
    print("k in 2..120 where every proper divisor divides some maximal proper divisor:")
    print(good)
    print()
    print("maximal proper divisors for some sample k:")
    for kk in [30, 60, 90, 120, 72]:
        print(f"  k={kk}: {maximal_proper_divisors(kk)}")


if __name__ == "__main__":
    main()
