"""Check the renewal-process-edge-flip-hitting-time approach's central lemma.

The edge e_d of a {0,2} block of halved length n (bit string h[0..n-1]),
after d erosion rows, is the Rule-90 (Pascal mod 2) convolution:

    e_d = XOR_{j=0}^{d} [C(d,j) mod 2] * h[b_k - d + j]

With h indexed 0-based, at erosion depth d the edge is at position n-1-d,
so e_d = XOR_{j=0}^{d} [C(d,j) mod 2] * h[(n-1-d)+j], for d = 0..n-1.

The approach conjectures the longest run of consecutive zeros in (e_0..e_{n-1})
is bounded (<= 2n claimed), for every nonzero halved block h.

We exhaustively test all 2^n strings for n=1..18 and report the WORST-CASE
zero-run and the achieving pattern, plus the count of strings whose all-zero
edge sequence (constant-0 block). This is the oracle check the approach's
first-step demands.
"""
import sys
from math import comb

def edge_sequence(h):
    """h: list of bits (halved block), length n. Return e_0..e_{n-1}."""
    n = len(h)
    e = []
    for d in range(n):  # d = erosion depth, block length remaining = n-d >= 1
        val = 0
        for j in range(d + 1):
            if comb(d, j) % 2:
                val ^= h[(n - 1 - d) + j]
        e.append(val)
    return e

def longest_zero_run(seq):
    m = 0
    cur = 0
    for x in seq:
        if x == 0:
            cur += 1
            m = max(m, cur)
        else:
            cur = 0
    return m

max_n = int(sys.argv[1]) if len(sys.argv) > 1 else 18
worst = {}
for n in range(1, max_n + 1):
    w = 0
    wpat = None
    allzero_count = 0
    total = 1 << n
    for mask in range(total):
        h = [(mask >> b) & 1 for b in range(n)]
        e = edge_sequence(h)
        r = longest_zero_run(e)
        if r > w:
            w = r
            wpat = h
        if r == n:  # all-zero edge sequence
            allzero_count += 1
    worst[n] = (w, wpat, allzero_count)
    print(f"n={n}: worst zero-run={w}  (2n={2*n})  allzero_edge_count={allzero_count}  pattern={wpat}")
print()
print("Summary: does worst zero-run stay <= n, <= 2n?")
for n in range(1, max_n + 1):
    w = worst[n][0]
    print(f"  n={n}: worst={w}  n={n} 2n={2*n}  '<=n':{w<=n} '<=2n':{w<=2*n}")
