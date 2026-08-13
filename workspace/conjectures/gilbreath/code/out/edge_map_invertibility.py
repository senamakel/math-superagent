#!/usr/bin/env python3
"""Edge-map invertibility: prove-and-check the sharpened edge-zero-run lemma.

The halved-edge map of a {0,2} block under pure erosion:
    e_d = XOR_{j=0}^{d} [C(d,j) mod 2] * h[n-1-d+j],   d = 0..n-1,
the value at the block-edge position after d erosion rows.  This is an
F2-linear map e = M_n h with M_n[d][c] = C(d, c-(n-1-d)) mod 2 for
c in [n-1-d, n-1], else 0.

Claim (upgrading check_edge_zero_run.py's vacuous <=2n bound):
  1. M_n is unitriangular in reversed column order c' = n-1-c
     (M[d][c'] = C(d, d-c') for c' <= d, diagonal M[d][d] = C(d,0) = 1),
     hence invertible over F2:  e == 0  <=>  h == 0.
  2. Therefore a nonzero block shows edge value 2 (unhalved) at least once
     during its first n-1 pure-erosion rows; worst zero-run <= n-1.
  3. Sharpness: worst zero-run for nonzero blocks is exactly n-1, achieved
     by [1,0,...,0] and one other pattern, listed for n = 2..12.

Checks performed exactly (no floats):
  A. unitriangular structure verified for n = 3..1024 (diagonal 1, zeros
     above the reversed diagonal);
  B. exhaustive nonzero worst zero-run for n = 1..18 (all 2^n - 1 blocks),
     two independent routes (Pascal-mod-2 convolution vs literal |a-b|
     erosion) must agree and both must agree with the matrix route;
  C. achiever patterns for n = 2..12 enumerated by back-substitution on
     the unitriangular system e = (0,...,0,1).
"""
import sys
from math import comb
from itertools import product


def parity_choose(d, j):
    """C(d,j) mod 2 via Lucas: odd iff j is a submask of d."""
    return 1 if (j & ~d) == 0 else 0


def matrix_entry(n, d, c):
    """M_n[d][c], c = 0..n-1 (original column order)."""
    if c < n - 1 - d or c > n - 1:
        return 0
    return parity_choose(d, c - (n - 1 - d))


def check_unitriangular(max_n):
    bad = []
    for n in range(3, max_n + 1):
        for d in range(n):
            for c in range(n):
                cp = n - 1 - c          # reversed column order
                v = matrix_entry(n, d, c)
                if cp > d and v != 0:   # above diagonal must be 0
                    bad.append((n, d, c, v))
                if cp == d and v != 1:  # diagonal must be 1
                    bad.append((n, d, c, v))
    return bad


def route1_edge_sequence(h):
    n = len(h)
    e = []
    for d in range(n):
        val = 0
        for j in range(d + 1):
            if comb(d, j) % 2:
                val ^= h[(n - 1 - d) + j]
        e.append(val)
    return e


def route2_edge_sequence(h):
    n = len(h)
    row = [1] + [2 * x for x in h]
    e = []
    for d in range(n):
        e.append(row[n - d] // 2)
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    return e


def matrix_route_edge_sequence(h):
    n = len(h)
    return [sum(matrix_entry(n, d, c) * h[c] for c in range(n)) % 2
            for d in range(n)]


def longest_zero_run(seq):
    m = cur = 0
    for x in seq:
        cur = cur + 1 if x == 0 else 0
        m = max(m, cur)
    return m


def achievers_by_backsub(n):
    """Unique h with e = (0,...,0,1): back-substitute the unitriangular
    system in reversed order.  e_{n-1} = XOR_j [C(n-1,j) odd] h[j] = 1."""
    # Use the inverse route instead: solve e = M h with e the unit vector.
    # In (d, c') coordinates M is lower triangular with 1s on the diagonal:
    #   e_d = XOR_{c'<=d} [C(d, d-c') odd] * h[n-1-c']
    # solve for h from c' = d downward.
    h = [0] * n
    for cp in range(n):                 # c' = n-1-c, process 0..n-1
        d = cp
        rhs = 1 if d == n - 1 else 0
        acc = 0
        for cpp in range(cp):           # already-solved columns c' < cp
            if parity_choose(d, d - cpp):
                acc ^= h[n - 1 - cpp]
        h[n - 1 - cp] = rhs ^ acc
    return h


def main():
    max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 18
    print("A. unitriangular structure M_n (reversed columns) for n = 3..1024")
    bad = check_unitriangular(1024)
    print(f"   violations: {len(bad)}   ->  M_n invertible over F2 for all n <= 1024")
    print("   hence: e == 0 (edge 0 for all n erosion rows)  <=>  h == 0 (all-zero block)")
    print("   consequence: every NONZERO {0,2} block shows edge 2 within its first n-1\n"
          "   pure-erosion rows; worst zero-run <= n-1 (vs the vacuous 2n).\n")

    print("B. exhaustive nonzero blocks, three routes agree (n = 1..%d)" % max_n)
    agree = True
    worst = {}
    for n in range(1, max_n + 1):
        w = 0
        wpat = None
        wcount = 0
        for mask in range(1, 1 << n):
            h = [(mask >> b) & 1 for b in range(n)]
            e1 = route1_edge_sequence(h)
            e2 = route2_edge_sequence(h)
            e3 = matrix_route_edge_sequence(h)
            if not (e1 == e2 == e3):
                agree = False
                print(f"   MISMATCH n={n} h={h} e1={e1} e2={e2} e3={e3}")
            r = longest_zero_run(e1)
            if r > w:
                w, wpat, wcount = r, h, 1
            elif r == w:
                wcount += 1
        worst[n] = (w, wpat, wcount)
    print("   routes agree on every pattern:", agree)
    for n in range(1, max_n + 1):
        w, wpat, wcount = worst[n]
        print(f"   n={n}: nonzero patterns={2**n-1}  worst zero-run={w}  "
              f"achiever h={wpat}  count={wcount}")
    print(f"   worst zero-run for nonzero blocks == n-1 for n = 2..{max_n}: "
          f"{all(worst[n][0] == n - 1 for n in range(2, max_n + 1))}\n")

    print("C. achievers for the worst zero-run n-1, n = 2..12 (back-substitution)")
    for n in range(2, 13):
        h = achievers_by_backsub(n)
        e = route1_edge_sequence(h)
        ok = (e == [0] * (n - 1) + [1]) and (longest_zero_run(e) == n - 1)
        print(f"   n={n}: h={h}  e={e}  valid={ok}")
    print("\nDONE")
    return 0 if (agree and not bad and
                 all(worst[n][0] == n - 1 for n in range(2, max_n + 1))) else 1


if __name__ == "__main__":
    sys.exit(main())