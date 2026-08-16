#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
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

def make_pow2(n):
    h=[0]*n; p=1
    while p<n: h[p]=1; p<<=1
    return h

def make_squares(n):
    h=[0]*n; k=1
    while k*k<n: h[k*k]=1; k+=1
    return h

def make_triangular(n):
    h=[0]*n; k=1
    while k*(k+1)//2 < n: h[k*(k+1)//2]=1; k+=1
    return h

def family_ratio(N, make_h, label, step=64):
    print(f"\n=== {label} ===")
    print(f"{'n':>8} {'nu2':>7} {'nu2/n':>8} {'ones':>6}")
    for n in range(step, N+1, step):
        h = make_h(n)
        cnt = s_direct(n, h) if n <= 32 else s_sos(n, h)
        print(f"{n:>8} {cnt:>7} {cnt/n:>8.4f} {sum(h):>6}")

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv)>1 else 2048
    for n,make in [(16,make_pow2),(32,make_squares)]:
        h=make(n)
        assert s_sos(n,h)==s_direct(n,h), (n,)
    print("s_sos == s_direct cross-check passed on small n.")
    family_ratio(N, make_pow2, "fixed: ones at powers of 2")
    family_ratio(N, make_squares, "fixed: ones at squares", step=64)
    family_ratio(N, make_triangular, "fixed: ones at triangular numbers", step=64)
