#!/usr/bin/env python3
"""Independent check of the diagonal-subtriangle membership claim.

Claim (A repeated): if row A_k has leading {0,2} block of length n, then for
each d in 0..n-1 the entry A_{k+d}(1) is guaranteed in {0,2} (it sits on the
diagonal of the block), and moreover the whole subtriangle of positions
{1..n-d} in row k+d for d=0..n is entirely in {0,2}.

We check the diagonal membership on EVERY block bit-pattern of every length,
with several distinct adversarial even completions, and confirm the largest d
with a forced {0,2} at position 1 is exactly n-1 (row k+n-1), while offset n
uses index n+1 (outside the block) and is NOT forced.
"""
import random


def triangle_in_02(block, tail, n):
    """Returns (diag_ok_offsets, full_ok) for a row [1, block..., tail...].
    diag_ok_offsets = list of d in 0..n-1 such that position 1 of row (offset d)
    is in {0,2}; full_ok_d = largest d such that the whole active subtriangle of
    positions 1..(n-d) is in {0,2}."""
    row = [1] + list(block) + list(tail)
    diag_ok = []
    full_ok = -1
    cur = list(row)
    for d in range(0, n + 2):
        # position-1 value at offset d
        v1 = cur[1] if len(cur) > 1 else None
        if v1 is not None and len(cur) >= 2:
            if v1 in (0, 2) and d < n:
                diag_ok.append(d)
        # whole active subtriangle of positions 1..(n-d) in {0,2}
        if len(cur) >= 2:
            if all(x in (0, 2) for x in cur[1:max(2, n - d + 1)]):
                full_ok = d
        if len(cur) > 1:
            cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
        else:
            break
    return diag_ok, full_ok


def main():
    random.seed(20240214)
    n_fail_diag = 0
    n_fail_full = 0
    total = 0
    for n in range(1, 12):
        for bits in range(1 << n):
            block = [2 * ((bits >> (n - 1 - j)) & 1) for j in range(n)]
            for _ in range(30):
                tail = [random.choice([4, 6, 8, 10, 12]) for _ in range(30)]
                diag_ok, full_ok = triangle_in_02(block, tail, n)
                # diag rows 0..n-1 must all be in {0,2}: diag_ok == list(range(n))
                exp_diag = list(range(n))
                if diag_ok != exp_diag:
                    n_fail_diag += 1
                # full subtriangle: full_ok should be at least n-1 (positions 1..1
                # of row n-1); we only assert it's >= n-1
                if full_ok < n - 1:
                    n_fail_full += 1
                total += 1
    print(f"checked {total} (block-pattern, adversarial-tail) pairs, n=1..11")
    print(f"diagonal rows 0..n-1 all in {{0,2}}: "
          f"{'PASS' if n_fail_diag == 0 else f'FAIL ({n_fail_diag})'}")
    print(f"full active subtriangle in {{0,2}} through row n-1: "
          f"{'PASS' if n_fail_full == 0 else f'FAIL ({n_fail_full})'}")
    # sharpness: offset n uses index n+1; show it is NOT forced
    # (find a pattern+tail where position 1 at offset n escapes)
    escapes = []
    for n in range(1, 9):
        found = False
        for bits in range(1 << n):
            block = [2 * ((bits >> (n - 1 - j)) & 1) for j in range(n)]
            for _ in range(200):
                # adversarial completion putting a big even right after block
                tail = [random.choice([4, 6, 8])] + [random.choice([4, 6, 8]) for _ in range(15)]
                row = [1] + block + tail
                cur = list(row)
                for d in range(0, n + 2):
                    if d == n:
                        if len(cur) > 1 and cur[1] not in (0, 2):
                            found = True
                    cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)] if len(cur) > 1 else cur
        print(f"  n={n}: offset-n position-1 CAN leave {{0,2}}: {found}  (sharpness)")
        escapes.append(found)
    print("all sharp (n=1..8):", all(escapes))


if __name__ == "__main__":
    main()
