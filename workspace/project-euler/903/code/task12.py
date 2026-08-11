#!/usr/bin/env python3
"""task12.py — verify the gap-constant chain against the statement oracle,
and print the clean A_n/B_n/c_n table with prime factorizations.

Task 1: Load A_n = f(0), B_n = f(1)-f(0) from extend_f.json and run
solution.q_from_ab to reproduce:
  Q(10) mod p == 468421536   (the statement oracle)
  Q(6)  == 133103808
  Q(8)  == 798047424
Task 2: print A_n, B_n, c_n = |B_n|/(n-1)! and factorizations of A_n, |B_n|
for n = 2..11.
"""
import json
import math
import sys

sys.path.insert(0, "/workspace/code")
from solution import q_from_ab

MODP = 1_000_000_007

# exact Q values mod p known from brute (memory.md) for the oracle/chain check
KNOWN = {
    6: 133103808,
    8: 798047424,
    10: 468421536,
}


def factor(n):
    x = abs(n)
    out = {}
    d = 2
    while d * d <= x:
        while x % d == 0:
            out[d] = out.get(d, 0) + 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        out[x] = out.get(x, 0) + 1
    return out


def fmt_fact(f):
    return " * ".join(f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(f.items()))


def main():
    with open("/workspace/code/out/extend_f.json") as fh:
        data = json.load(fh)

    print("=" * 78)
    print("TASK 1 : chain Q(n) = (n!)^2 + A*(n!-1) + (B/2)*T  vs known values")
    print("=" * 78)
    all_ok = True
    for n in sorted(KNOWN):
        row = data[str(n)]
        A = row[0]
        B = row[1] - row[0] if len(row) >= 2 else 0
        got = q_from_ab(n, A, B, MODP)
        want = KNOWN[n]
        ok = got == want
        all_ok = all_ok and ok
        print(f"n={n:2d}  A={A:22d}  B={B:22d}  "
              f"Q mod p = {got:10d}   expected {want:10d}  [{'OK' if ok else 'FAIL'}]")
    print("ALL OK" if all_ok else "SOME FAILED")

    print()
    print("=" * 78)
    print("TASK 2 : A_n = f(0), B_n = f(1)-f(0), c_n=|B_n|/(n-1)!, factorizations")
    print("=" * 78)
    hdr = f"{'n':>3} | {'A_n':>22} | {'abs(B_n)':>22} | {'c_n=|B_n|/(n-1)!':>16}"
    print(hdr)
    print("-" * 78)
    for n in range(2, 12):
        row = data[str(n)]
        A = row[0]
        B = row[1] - row[0] if len(row) >= 2 else 0
        c = abs(B) // math.factorial(n - 1) if (n >= 2 and abs(B) % math.factorial(n - 1) == 0) else None
        cstr = f"{c}" if c is not None else "not-int"
        print(f"{n:>3} | {A:>22} | {abs(B):>22} | {cstr:>16}")

    print()
    print("Prime factorizations of A_n:")
    for n in range(2, 12):
        A = data[str(n)][0]
        print(f"  A_{n} = {A} = {fmt_fact(factor(A))}")
    print()
    print("Prime factorizations of |B_n|:")
    for n in range(3, 12):
        row = data[str(n)]
        B = abs(row[1] - row[0])
        print(f"  |B_{n}| = {B} = {fmt_fact(factor(B))}")

    print()
    print("c_n = |B_n|/(n-1)! factorization (only where division is exact):")
    for n in range(3, 12):
        row = data[str(n)]
        B = abs(row[1] - row[0])
        d = math.factorial(n - 1)
        q, r = divmod(B, d)
        if r == 0:
            print(f"  c_{n} = {q} = {fmt_fact(factor(q))}")
        else:
            print(f"  c_{n} = {B}/{d}  (not an integer: remainder {r})")


if __name__ == "__main__":
    main()
