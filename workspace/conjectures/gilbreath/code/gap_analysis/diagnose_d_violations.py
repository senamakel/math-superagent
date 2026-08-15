#!/usr/bin/env python3
"""
Diagnose the (D) constant-1 erosion ``c_n >= c_{n-1} - 1`` violations from
reduction_audit.py.  Where do they happen?  At small n only, or throughout?
And by how much does c drop (d = -2, -3, ...)?

`c_n` is defined in the audit as: length of the maximal SUFFIX of delta(q_n)
(all entries in {0,2}) excluding the final (bottom) entry of the diagonal.

Reuses the exact same construction (same primes, same diagonal recurrence,
same zero_two_suffix_length) so a mismatch can only be in our reading, not in
two programs disagreeing.
"""
import sys

def primes_up_to(n):
    if n < 2:
        return []
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = b'\x00' * (((n - i * i) // i) + 1)
    return [i for i in range(n + 1) if sieve[i]]

def build_diagonals(ps, N):
    prev = None
    diags = [None]
    for n in range(1, N + 1):
        qn = ps[n - 1]
        cur = [0] * n
        cur[0] = qn
        if prev is not None:
            for k in range(1, n):
                cur[k] = abs(cur[k - 1] - prev[k - 1])
        diags.append(cur)
        prev = cur
    return diags

def zero_two_suffix_length(vec, exclude_last=False):
    end = len(vec)
    if exclude_last:
        end -= 1
    i = end - 1
    while i >= 0 and vec[i] in (0, 2):
        i -= 1
    return end - 1 - i

def main():
    N = 10001
    ps = primes_up_to(200000)[:N]
    N = len(ps)
    diags = build_diagonals(ps, N)
    c = [0] * (N + 1)
    for n in range(2, N + 1):
        c[n] = zero_two_suffix_length(diags[n], exclude_last=True)

    # distribution of d = c_n - c_{n-1}
    from collections import Counter
    dist = Counter()
    viol_n = []
    for n in range(3, N + 1):
        d = c[n] - c[n - 1]
        dist[d] += 1
        if d < -1:
            viol_n.append((n, d, c[n - 1], c[n]))
    print("distribution of d = c_n - c_{n-1}:")
    for d in sorted(dist):
        print(f"  d={d:4d}: {dist[d]}")
    print(f"\ntotal violations (d < -1): {len(viol_n)}")

    # how are violations distributed in n?
    if viol_n:
        ns = [v[0] for v in viol_n]
        print(f"violation n-range: min n={min(ns)}, max n={max(ns)}")
        print(f"violations with n <= 100: {sum(1 for v in viol_n if v[0] <= 100)}")
        print(f"violations with n <= 1000: {sum(1 for v in viol_n if v[0] <= 1000)}")
        print("first 20 violations (n, d, c_{n-1}, c_n):")
        for v in viol_n[:20]:
            print("  ", v)

    # how big are the drop magnitudes?
    drops = Counter(v[1] for v in viol_n)
    print("\ndrop-magnitude distribution among violations:")
    for d in sorted(drops):
        print(f"  d={d:4d}: {drops[d]}")

    # what does the diagonal itself look like at a few violating n?
    for n, d, cp, cn in list(viol_n)[:3]:
        print(f"\n--- violation at n={n}, d={d}, c_prev={cp}, c_cur={cn} ---")
        print("  delta(q_n) tail (last 12):", diags[n][-12:])
        print("  delta(q_{n-1}) tail (last 12):", diags[n - 1][-12:])
        print("  delta(q_{n-2}) tail (last 12):", diags[n - 2][-12:])

if __name__ == "__main__":
    main()
