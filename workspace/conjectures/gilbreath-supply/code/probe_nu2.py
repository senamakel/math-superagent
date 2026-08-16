#!/usr/bin/env python3
"""Fast nu2(n) via the fold form, extended range, with residue/structural probes.

nu2(n) = #{ d in [2, n-1] : T(n,d)=1 },  T(n,d) = XOR over submasks o of d
         of h[n-1-d+o], h = prime gap-parity string.

Key optimization: enumerate submasks of d via (sub-1)&d. For each d this is
2^{popcount(d)} iterations. For n up to a few thousand that's fine.

We also emit:
  - nu2 sequence
  - switch density of h (freq of 1s in h)
  - nu2(n) for n a power of two (dyadic collapse test: should be O(1))
  - sub-sequences nu2(n) restricted to n mod 8 classes
"""

import sys
from math import isqrt

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok = True
        r = isqrt(cand)
        for p in ps:
            if p > r: break
            if cand % p == 0: ok = False; break
        if ok: ps.append(cand)
        cand += 2
    return ps

def main():
    N = int(sys.argv[1]) if len(sys.argv)>1 else 1000
    H = primes_upto_index(N+4)
    # h over first gaps
    h = [((H[j+1]-H[j])//2) % 2 for j in range(N+2)]
    seq = []
    for n in range(2, N+1):
        cnt = 0
        for d in range(2, n):
            total = 0
            sub = d
            base = (n-1-d)
            while True:
                total ^= h[base + sub]
                if sub == 0: break
                sub = (sub-1) & d
            cnt += total
        seq.append(cnt)
    print("nu2[2..%d]:" % N)
    print(seq)

    # switch density of h
    ones = sum(h)
    print("switch density of h (first %d gaps): %.4f  (%d/%d)" % (len(h), ones/len(h), ones, len(h)))

    # powers of two
    print("nu2 at powers of two:")
    p2 = 2
    while p2 <= N:
        print(f"  n=2^{p2.bit_length()-1}={p2}: nu2={seq[p2-2]}")
        p2 *= 2

    # dyadic subset: nu2 at 2^k and 2^k-1 small (collapse test)
    print("nu2 / (n) at n=2^k (should stay bounded if dyadic collapse):")
    p2 = 2
    while p2 <= N:
        print(f"  n={p2}: ratio {seq[p2-2]/p2:.4f}")
        p2 *= 2

if __name__ == "__main__":
    main()
