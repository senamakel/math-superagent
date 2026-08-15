#!/usr/bin/env python3
"""Test the transfer claims UNIVERSALLY over all halved-gap bit strings.

Claims being tested (the decision fork of S1-nu2-transfer-weight, and
G-supply-transfer):
  (S1)  nu2 >= w/2      for ALL bit strings h    (case a: universal)
  (G)   nu2 >= (2/3)*w  for ALL bit strings h    (G-supply-transfer)

Construction: a 2-then-odds sequence with halved-gap bits h is built by
setting gaps G[i] = 2*(h_eff+1) in {2,4} so that (G[i]/2) mod 2 = h[i].
Concretely G[i] = 4 - 2*b[i] gives (G/2) mod 2 = b[i].

We take b over positions j = 2..n-1 (the ancestor window [2,n-1]).

For each h in {0,1}^{n-2} we build the full triangle to depth n-1, read the
right diagonal delta(q_n) = A_k[n-k], k = 0..n-1, take the maximal {0,2}
suffix of A_k[n-k] for k = 2..n-2, count the 2s = nu2, and compare to
w = weight(b).

Exact integer arithmetic, no floats.
"""
import itertools
from lib.gilbreath import diff_block


def build_triangle(bits, n):
    # A_0 = (2, 3, ...). Gaps after position 0: G[0]=1 (3-2), G[1]=? 
    # We need A_0[i+1]-A_0[i] for i>=2 to have halved bit bits[i-2].
    # For i>=1: gap G[i] = A_0[i+1]-A_0[i].  We want (G[i]/2)%2 = bit for i in
    # the window.  Simplest: G[0]=1 (so 3), then for the window positions set
    # G[i] = 4-2*bit.
    seq = [2, 3]
    # G[1] is the gap 3 -> x_1. Keep it 2 (halved 1) whatever.
    seq.append(seq[-1] + 2)
    # now positions i = 2..n-1 get gaps from bits window j=2..n-1
    for j in range(2, n):          # j = position index of the gap (G[j])
        bit = bits[j-2]            # bits indexed as h[j], j=2..n-1
        G = 4 - 2*bit
        seq.append(seq[-1] + G)
    # seq has length n+1  (indices 0..n). Build triangle.
    rows = [seq]
    for k in range(1, n):
        rows.append(diff_block(rows[-1]))
    return rows


def nu2_of(rows, n):
    # right diagonal delta(q_n): cells A_k[n-k], k=0..n-1
    d = [rows[k][n-k] for k in range(n)]
    tail = d[2:-1]                # k = 2..n-2
    i = len(tail)
    while i > 0 and tail[i-1] in (0, 2):
        i -= 1
    cyc = tail[i:]
    return cyc.count(2)


def main():
    for n in range(4, 15):
        total = 0
        viol_half = []
        viol_23 = []
        min_ratio = 1e9
        for bits in itertools.product([0,1], repeat=n-2):
            rows = build_triangle(bits, n)
            nu2 = nu2_of(rows, n)
            w = sum(bits)
            if w == 0:
                continue
            total += 1
            if nu2/w < min_ratio:
                min_ratio = nu2/w
            if nu2 < w/2:
                viol_half.append((bits, nu2, w))
            if nu2 < (2/3)*w:
                viol_23.append((bits, nu2, w))
        print(f"n={n}: strings={2**(n-2)} nonzero-w={total} min nu2/w={min_ratio:.3f} "
              f"viol nu2<w/2: {len(viol_half)}  viol nu2<(2/3)w: {len(viol_23)}")
        if viol_half:
            print("   first nu2<w/2 example:", viol_half[0])
        if viol_23:
            print("   first nu2<(2/3)w example:", viol_23[0])


if __name__ == "__main__":
    main()
