"""Probe the number of oriented induced P4 anchors in BvLS to estimate cost."""
import time
import numpy as np
from lib.srg import bvls_graph

B = bvls_graph()
A = np.asarray(B, dtype=np.int64)
N = A.astype(bool)
n = A.shape[0]

t0 = time.time()
total_p4 = 0
sample = 0
start = time.time()
for v1 in range(n):
    N1 = N[v1]
    for v2 in np.flatnonzero(N1):
        N2 = N[v2]
        cand3 = N2 & ~N1
        cand3[v1] = False
        for v3 in np.flatnonzero(cand3):
            N3 = N[v3]
            cand4 = N3 & ~N1 & ~N2
            cand4[v1] = cand4[v2] = False
            total_p4 += int(cand4.sum())
    if v1 == 4:
        sample = (time.time() - start)
        break
per_vertex_p4 = total_p4 / 5
print("oriented induced P4 per root vertex (first 5):", per_vertex_p4)
print("projected total over 243 roots:", per_vertex_p4 * 243)
print("time for first 5 roots:", round(sample, 2), "s")
print("projected full time", round(sample * 243 / 5, 1), "s")
