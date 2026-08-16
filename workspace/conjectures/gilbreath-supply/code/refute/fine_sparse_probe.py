#!/usr/bin/env python3
"""Fine-resolution probe of fixed-sparse-string fold weight.

Q: does any FIXED binary string h with density of ones 0 (switch density 0)
give nu2(n)/n >= c for ALL large n (G-weak-input-strictness), or does every
such h have liminf nu2(n)/n = 0 (rival G-eq-sparse-fold-is-sublinear)?

Previous work sampled at step 64 and found powers-of-2 has ratio ~2/3 at
n=2^k+1 but ~0 at n=2^k. This probes EVERY n in a range to see how sharp the
drop is and whether any engineering keeps the ratio up. Exact arithmetic.
"""
import sys, math

def s_sos(n, h):
    b = [1 - 2*h[j] for j in range(n)]
    barray = [b[n-1-t] for t in range(n)]
    size = 1
    while size < n: size <<= 1
    g = [1]*size
    for t in range(n): g[t] = barray[t]
    bit = 1
    while bit < size:
        for x in range(size):
            if x & bit:
                g[x] *= g[x ^ bit]
        bit <<= 1
    return sum(1 for d in range(2, n) if g[d] == -1)

# support builders: return length-n prefix
def pow2(n):
    h=[0]*n; p=1
    while p<n: h[p]=1; p<<=1
    return h

def near_pow2(n):
    # ones at 2^k AND 2^k+1: so every n-1 near a power of two is covered?
    h=[0]*n; p=1
    while p<n:
        h[p]=1
        if p+1<n: h[p+1]=1
        p<<=1
    return h

def dense_boundary(n):
    # ones at 2^k-1 too (so n-1 = 2^k-1 covered -> but that's index 2^k-1)
    h=[0]*n; p=1
    while p<n:
        h[p]=1
        if p-1>=0: h[p-1]=1
        if p+1<n: h[p+1]=1
        p<<=1
    return h

def all_pow2_and_neighbors(n):
    h=[0]*n; p=1
    while p<n:
        for dd in (-1,0,1):
            if 0<=p+dd<n: h[p+dd]=1
        p<<=1
    return h

def fine_sweep(N, make_h, label):
    """report min ratio over [N/2,N], and the running min ratio up to N."""
    mn = 1.0
    argmin = 0
    blows = []  # n where ratio >= 0.5
    print(f"\n=== {label} ===")
    h_cache = {}
    for n in range(N//2, N+1):
        h = make_h(n)
        cnt = s_sos(n, h)
        r = cnt/n
        if r < mn:
            mn, argmin = r, n
        if r >= 0.5:
            blows.append((n, round(r,3)))
    print(f"window [{N//2},{N}]: min ratio = {mn:.4f} at n={argmin}")
    print(f"  #n with ratio>=0.5 in window: {len(blows)}", blows[:12], "..." if len(blows)>12 else "")
    # running min over full [2,N]
    mn=1.0; argmin=0
    for n in range(8, N+1):
        h = make_h(n)
        r = s_sos(n,h)/n
        if r<mn: mn,argmin=r,n
    print(f"running min over [8,{N}]: {mn:.4f} at n={argmin}")
    return mn

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 2048
    fine_sweep(N, pow2, "ones at powers of 2")
    fine_sweep(N, near_pow2, "ones at 2^k and 2^k+1")
    fine_sweep(N, dense_boundary, "ones at 2^k-1, 2^k, 2^k+1")
