#!/usr/bin/env python3
"""Verify the find_counterexample n=8 K=4 witness by the canonical oracle and
by hand, independent of the TPTP encoding."""
import sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos, t_direct

def c_k(h, K):
    n = len(h)
    counts = {}
    for start in range(n - K):
        w = 0
        for t in range(K + 1):
            w = (w << 1) | h[start + t]
        counts[w] = counts.get(w, 0) + 1
    return dict(sorted(counts.items()))

h  = [0,1,1,1,0,1,1,1]   # 01110111
hp = [1,0,1,1,1,0,1,1]   # 10111011
n = 8
S, ones = s_sos(n, h)
Sp, ones_p = s_sos(n, hp)
print("h  =", ''.join(map(str,h)),  " S=", S,  " S^2=", S*S,  " nu2=", ones)
print("h' =", ''.join(map(str,hp)), " S=", Sp, " S^2=", Sp*Sp, " nu2=", ones_p)
print("identical C_4 (5grams):", c_k(h,4)==c_k(hp,4))
print("C_4(h) :", c_k(h,4))
print("C_4(h'):", c_k(hp,4))
print("different S^2:", S*S != Sp*Sp)
# hand-verify each cell
print("h cells  :", [t_direct(n,d,h)  for d in range(2,8)])
print("h' cells :", [t_direct(n,d,hp) for d in range(2,8)])
