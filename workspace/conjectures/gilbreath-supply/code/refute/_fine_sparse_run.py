#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
import math

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

def pow2(n):
    h=[0]*n; p=1
    while p<n: h[p]=1; p<<=1
    return h
def near_pow2(n):
    h=[0]*n; p=1
    while p<n:
        h[p]=1
        if p+1<n: h[p+1]=1
        p<<=1
    return h
def dense_boundary(n):
    h=[0]*n; p=1
    while p<n:
        for dd in (-1,0,1):
            if 0<=p+dd<n: h[p+dd]=1
        p<<=1
    return h

def fine_sweep(N, make_h, label):
    print(f"\n=== {label} ===")
    mn=1.0; argmin=0
    # track liminf separately on tail half
    for n in range(8, N+1):
        cnt = s_sos(n, make_h(n))
        r = cnt/n
        if r<mn: mn,argmin=r,n
    print(f"running min ratio over [8,{N}] = {mn:.4f} at n={argmin}")

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 2048
    for mk,lbl in [(pow2,"ones at powers of 2"),(near_pow2,"ones at 2^k and 2^k+1"),(dense_boundary,"ones at 2^k-1,2^k,2^k+1")]:
        fine_sweep(N, mk, lbl)
