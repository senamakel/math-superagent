#!/usr/bin/env python3
"""proof certificate for the mod-8 claim.  The probe (probe_T_exact_mod8.py)
showed numerically that T(c,p) = sum_{k=0}^{p-1}(c^2+1)^k is never a square
for c odd.  This program turns that into a PROOF certificate:

Claim (proved here): for c odd (integer c >= 1) and any odd prime p >= 3,
    T(c,p) == 7 (mod 8),
so T(c,p) is never a square (square residues mod 8 are {0,1,4}).

Hand proof the program checks exactly:
  c odd  =>  c^2 == 1 (mod 8)  =>  x = c^2+1 == 2 (mod 8).
  For a integer u == 2 (mod 8): u^0 == 1, u^1 == 2, u^2 == 4 (mod 8), and
  u^k == 0 (mod 8) for every k >= 3 (2^k is a multiple of 8, and u^k == 2^k
  mod 8 since u == 2 mod 8 and exponentiation is compatible with reduction;
  more directly u = 8m+2, u^k divisible by 2^k, and k>=3 gives 8 | 2^3 |
  u^k).  Hence for any p >= 3,
    T(c,p) == 1 + u + u^2 == 1 + 2 + 4 == 7 (mod 8),
  independent of p.  And 7 not in {0,1,4} = square residues mod 8, so
  T(c,p) is not a square.

The program verifies each ingredient on exact integers over wide ranges:
  (a) x = c^2+1 == 2 (mod 8) for every odd c in [1, 10^6].
  (b) c^2 == 1 (mod 8) for every odd c in [1, 10^6]   (1^2=1,3^2=9=1,...).
  (c) u^k == 0 (mod 8) for every k in [3, 60] with u == 2 (mod 8) and
      u in {2, 10, 18, ..., 8*10+2}  (i.e. u == 2 mod 8).
  (d) T(c,p) == 7 (mod 8) computed directly as an EXACT integer
      (x^p - 1)//(x - 1) for every odd c in [1, 3000] and every odd prime
      p in [3, 101]  -- 0 mismatches.
  (e) {u^2 mod 8 : u in 0..7} == {0,1,4}, i.e. 7 is a non-square mod 8.

All arithmetic exact (Python ints); no floats anywhere.
"""
from math import isqrt


def is_odd_prime(n):
    if n < 3:
        return False
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def T_exact(c, p):
    """T(c,p) = (x^p - 1)//(x - 1), x = c^2+1, exact integer (x>=2)."""
    x = c * c + 1
    return (x ** p - 1) // (x - 1)


def main():
    ok = True
    print("=== Proof certificate: c odd => T(c,p) == 7 (mod 8), never a square ===\n")

    # (a),(b) c odd => c^2 == 1 (mod 8) => x = c^2+1 == 2 (mod 8)
    b_ok = all(c * c % 8 == 1 for c in range(1, 10 ** 6, 2))
    print(f"(b) c^2 == 1 (mod 8) for all odd c in [1,1e6):  {b_ok}")
    x_ok = all((c * c + 1) % 8 == 2 for c in range(1, 10 ** 6, 2))
    print(f"(a) x = c^2+1 == 2 (mod 8) for all odd c in [1,1e6):  {x_ok}")
    ok = ok and b_ok and x_ok

    # (c) u == 2 mod 8 => u^k == 0 (mod 8) for k >= 3
    tail_ok = all((u ** k) % 8 == 0
                  for u in range(2, 8 * 10 + 2, 8)
                  for k in range(3, 61))
    print(f"(c) u^k == 0 (mod 8) for k in [3,60], u==2 (mod 8), u<=82:  {tail_ok}")
    ok = ok and tail_ok

    # (d) direct exact: T(c,p) == 7 (mod 8) for every odd c, odd prime p
    d_bad = 0
    d_cnt = 0
    for c in range(1, 3001, 2):
        for p in range(3, 102):
            if not is_odd_prime(p):
                continue
            d_cnt += 1
            if T_exact(c, p) % 8 != 7:
                d_bad += 1
    print(f"(d) T(c,p) == 7 (mod 8) directly for odd c<=3000, odd prime p<=101:"
          f"\n     {d_cnt} pairs checked, {d_bad} mismatches")
    ok = ok and d_bad == 0

    # (e) square residues mod 8 = {0,1,4}; 7 is a non-square
    sq8 = {u * u % 8 for u in range(8)}
    print(f"(e) square residues mod 8 = {sorted(sq8)}; 7 in set? {7 in sq8}")
    ok = ok and sq8 == {0, 1, 4} and 7 not in sq8

    # independent: no (c,p) in a big box has T(c,p) a perfect square
    bad2 = 0
    cnt2 = 0
    for c in range(1, 4001, 2):
        for p in (3, 5, 7, 11, 13, 17, 19, 23, 29):
            cnt2 += 1
            t = T_exact(c, p)
            r = isqrt(t)
            if r * r == t:
                bad2 += 1
    print(f"(f) [independent] direct isqrt square-test, odd c<=4000, "
          f"p in {[3,5,7,11,13,17,19,23,29]}: {cnt2} checked, {bad2} squares")

    print("\nRESULT:", "PROOF-INGREDIENTS ALL HOLD" if ok else "FAILED")
    print("Conclusion: for c odd and any odd prime p>=3, T(c,p) == 7 (mod 8),")
    print("and 7 is a non-square mod 8, so T(c,p) is never a perfect square.")
    return 0 if (ok and bad2 == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())
