#!/usr/bin/env python3
"""Exact oracle for the block-apex-parity-forcing approach's central claim.

Claim under test: "every mixed {0,2} block has an internal 0<->2 transition,
which forces the last entry (the erosion front, the value that meets the
intruder) to be 2 at some descendant row" — i.e. for every non-constant bit
pattern of length n, some offset d in 1..n-1 has front value 2.

Mechanics (halved, exact): block bits b_1..b_n in {0,1} (0->0, 2->1). The
subtriangle over positions 1..n evolves by XOR (Rule 90): value at (k+d, j)
= XOR_{t=0..d} [C(d,t) mod 2] * b_{j+t}. The erosion front at offset d is the
entry that meets the intruder at row k+d: position j = n-d, i.e.
  front(d) = XOR_{t=0..d} [C(d,t) mod 2] * b_{n-d+t}.

We enumerate ALL 2^n patterns, n = 1..11, and compute:
  - constant patterns (all bits equal)
  - mixed patterns whose front(d) == 0 for EVERY offset 1..n-1
    (intruder passes unreduced through the whole block lifetime)
  - mixed patterns whose front(d) == 2 for some offset in 1..n-2 (the
    earliest offsets; d = n-1 uses the full block and is pattern-dependent)
Declared cost: sum 2^n * n^2 <= 2^11 * 121 ~ 2.5e5 ops — trivial.
This is a brute-force oracle on small instances (explicitly allowed), not a
search over the answer space: it decides a finite structural claim.
"""
from math import comb


def front_sequence(bits):
    """front(d) for d = 0..n-1 under halved XOR dynamics."""
    n = len(bits)
    f = []
    for d in range(n):
        x = 0
        for t in range(d + 1):
            if comb(d, t) % 2 == 1:
                x ^= bits[n - d + t]
        f.append(x)
    return f


def main():
    print("n | all | constant | mixed | mixed with front=0 for ALL d=1..n-1"
          " | mixed with front=0 for d=1..n-2")
    for n in range(1, 12):
        total = 1 << n
        const = mixed = 0
        front0_all = []   # mixed patterns, front=0 for every d=1..n-1
        front0_early = [] # mixed patterns, front=0 for every d=1..n-2
        for m in range(total):
            bits = [(m >> i) & 1 for i in range(n)]
            if all(b == bits[0] for b in bits):
                const += 1
                continue
            mixed += 1
            f = front_sequence(bits)
            if all(f[d] == 0 for d in range(1, n)):
                front0_all.append(bits)
            if all(f[d] == 0 for d in range(1, n - 1)):
                front0_early.append(bits)
        print(f"{n:2d} | {total:4d} | {const:4d} | {mixed:4d} | "
              f"{len(front0_all):4d} | {len(front0_early):4d}")
        if front0_early and n <= 6:
            pass  # details printed below
    # Exhibit the smallest refuting patterns in detail
    for n in (3, 4, 5, 6):
        for m in range(1 << n):
            bits = [(m >> i) & 1 for i in range(n)]
            if all(b == bits[0] for b in bits):
                continue
            f = front_sequence(bits)
            if all(f[d] == 0 for d in range(1, n - 1)):
                print(f"\nrefuter n={n}: bits={bits} front={f}")
                break


if __name__ == "__main__":
    main()