#!/usr/bin/env python3
"""Compute nu2 and w (mod-4 transfer) for small n on the prime rows.

nu2 = number of 2s in the maximal {0,2} suffix of the right diagonal
w   = Hamming weight of the halved-gap bit window h[j] = (gap_j/2) mod 2 over
      j in [2, n-1]  (1 iff gap == 2 mod 4)
Check the transfer nu2 >= w/2 (S1) and nu2 >= (2/3)w (G-supply).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib.gilbreath import primes_up_to

BOUND = 50000
P = primes_up_to(BOUND)
MAX_N = 3999
rows = [P[:MAX_N+2]]
for k in range(1, MAX_N):
    prev = rows[-1]
    rows.append([abs(prev[i+1]-prev[i]) for i in range(len(prev)-1)])

def diag(n):
    return [rows[k][n-k] for k in range(n)]

hbits = [((P[i+1]-P[i])//2) % 2 for i in range(len(P)-1)]

def nu2_and_w(n):
    d = diag(n)
    tail = d[2:-1]
    i = len(tail)
    while i > 0 and tail[i-1] in (0,2):
        i -= 1
    cyc = tail[i:]
    nu2 = cyc.count(2)
    w = sum(hbits[2:n])
    return nu2, w

bad = []
for n in range(4, 1000):
    nu2, w = nu2_and_w(n)
    if w == 0:
        continue
    if nu2 < w/2:
        bad.append((n, nu2, w, nu2/w))
    # check the exact identity nu2 = wt(Phi_n h)?  we'd need Phi_n. skip here.

print("violations of nu2 >= w/2:", bad[:20], "count", len(bad))
min_ratio, argmin = 1e9, None
for n in range(4, 1000):
    nu2, w = nu2_and_w(n)
    if w:
        if nu2/w < min_ratio:
            min_ratio, argmin = nu2/w, (n, nu2, w)
print("min nu2/w over n<1000:", min_ratio, argmin)
