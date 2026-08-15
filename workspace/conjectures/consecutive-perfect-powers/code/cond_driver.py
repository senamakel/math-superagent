#!/usr/bin/env python3
"""cond_driver.py — run the exact-integer evaluator of the necessary
divisibility conditions and the oracle sanity search.

   (a) check_conditions(2, 3) at the known solution 3^2 - 2^3 = 1.
   (b) double_wieferich_pairs for B = 200 and B = 500.
   (c) oracle solutions(10**8) == [(3,2,2,3)].

All exact integer arithmetic (pow(x, y, m)); no floats. Captured to
code/out/cond.captured.txt.
"""
import sys
import time

from lib.cond import check_conditions, double_wieferich_pairs
from scholar_oracle.oracle import solutions


def main():
    print("=" * 72)
    print("(a) check_conditions at the known solution 3^2 - 2^3 = 1, (p,q)=(2,3)")
    print("=" * 72)
    c = check_conditions(2, 3)
    for k, v in c.items():
        print(f"  {k:<22} = {v}")
    print()
    print("  Interpretation: is_odd_prime_pair=False because p=2 is even, so the")
    print("  Cassels/Wieferich conditions are EXCLUDED BY HYPOTHESIS for (2,3),")
    print("  NOT a rejection of the known solution. The conditions only speak")
    print("  about pairs (p,q) of odd primes.")
    print()
    print("  Cross-check on concrete values x=3, y=2 (the known solution):")
    c2 = check_conditions(2, 3, x=3, y=2)
    for k, v in c2.items():
        print(f"  {k:<22} = {v}")
    print("  -> with concrete x=3,y=2: vq_x = (3 % 3 == 0) = True (q=3 divides x=3),")
    print("     vp_y = (2 % 2 == 0) = True (p=2 divides y=2): the Cassels relations")
    print("     do hold at the known solution, but is_odd_prime_pair=False keeps")
    print("     the hypothesis gate closed.")
    print()

    print("=" * 72)
    print("(b) double-Wieferich odd-prime pairs (p<q) for p,q <= B")
    print("=" * 72)
    for B in (200, 500):
        t0 = time.time()
        pairs = double_wieferich_pairs(B)
        dt = time.time() - t0
        print(f"\nB={B}: {len(pairs)} double-Wieferich pair(s), {dt:.3f}s")
        for p, q in pairs:
            # recompute residues for the record
            r1 = pow(q, p - 1, p * p)
            r2 = pow(p, q - 1, q * q)
            print(f"  ({p}, {q}): q^(p-1) = {r1} (mod {p*p}), "
                  f"p^(q-1) = {r2} (mod {q*q})")
    print()

    print("=" * 72)
    print("(c) oracle sanity: solutions(10**8) must be exactly [(3,2,2,3)]")
    print("=" * 72)
    t0 = time.time()
    res = solutions(10 ** 8)
    dt = time.time() - t0
    ok = (res == [(3, 2, 2, 3)])
    print(f"  solutions(10**8) = {res}")
    print(f"  exact match [(3,2,2,3)]? {ok}   ({dt:.3f}s)")
    print()

    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("  check_conditions(2,3) at known solution: "
          f"is_odd_prime_pair={c['is_odd_prime_pair']} "
          f"(excluded-by-hypothesis; conditions silent, not violated)")
    print(f"  double-Wieferich pairs <= 200 : {len(double_wieferich_pairs(200))}")
    print(f"  double-Wieferich pairs <= 500 : {len(double_wieferich_pairs(500))}")
    print(f"  oracle solutions(10**8) == [(3,2,2,3)]: {ok}")

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
