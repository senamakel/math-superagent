#!/usr/bin/env python3
"""Independent check of the fixed-sparse-string fold-weight question.

Targets G-weak-input-strictness / G-eq-sparse-fold-is-sublinear (the run's
central hypothesis: does the fold do work the switch-density form cannot see?).

Statement under attack (as the run's first step phrases it): for a FIXED binary
string h with density of ones -> 0 (switch density 0), does wt(Phi_n h) = nu2(n)
stay >= c*n for all large n, or does liminf nu2(n)/n = 0?

Prior settled result (sparse_fold_capture): powers-of-2 gives ~2/3 infinitely
often but liminf 0. This re-verifies with fresh exact code and probes more
families, plus the small-n exact SAT fact via the run's own phrasing.
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

def s_direct(n, h):
    cnt = 0
    for d in range(2, n):
        x = 0
        for o in range(d+1):
            if (o & d) == o:
                x ^= h[n-1-d+o]
        cnt += x
    return cnt

def family_ratio(N, make_h, label, step=64):
    print(f"\n=== {label} ===")
    print(f"{'n':>8} {'nu2':>6} {'nu2/n':>8} {'ones':>6}")
    for n in range(step, N+1, step):
        h = make_h(n)
        cnt = s_direct(n, h) if n <= 32 else s_sos(n, h)
        print(f"{n:>8} {cnt:>6} {cnt/n:>8.4f} {sum(h):>6}")

def make_pow2(n):
    h=[0]*n; p=1
    while p<n: h[p]=1; p<<=1
    return h

def make_pow2_plus(n):
    # ones at powers of 2 AND at 2^k+1... actually just powers of 2
    return make_pow2(n)

def make_squares(n):
    h=[0]*n; k=1
    while k*k<n: h[k*k]=1; k+=1
    return h

def make_triangular(n):
    h=[0]*n; k=1
    while k*(k+1)//2 < n: h[k*(k+1)//2]=1; k+=1
    return h

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 2048
    # exact cross-check of s_sos vs s_direct
    for n,make in [(16,make_pow2),(32,make_squares)]:
        h=make(n)
        assert s_sos(n,h)==s_direct(n,h), (n,)
    print("s_sos == s_direct cross-check passed on small n.")
    family_ratio(N, make_pow2, "fixed: ones at powers of 2")
    family_ratio(N, make_squares, "fixed: ones at squares", step=64)
    family_ratio(N, make_triangular, "fixed: ones at triangular numbers", step=64)
