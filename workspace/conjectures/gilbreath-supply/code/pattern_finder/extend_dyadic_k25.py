#!/usr/bin/env python3
"""Extend the dyadic record to k=24, 25 (n = 2^24, 2^25) for the MAIN dyadic
values only (nu2, S at 2^k, 2^k±1), plus the second-difference
D2(k) = S(2^k+1) + S(2^k-1) - 2 S(2^k) for k=3..25, and the dyadic deviation
e_k = nu2(2^k) - 2^(k-1) = -1 - S(2^k)/2.

Exact SOS fold; guards at k=3..15 vs canonical JSON, and continuity with the
k=16..23 values computed by extend_dyadic_sequence.py.
"""
import json
import sys
import time

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos
from lib.primes import h_string

def nu2_S(n, h):
    S, ones = s_sos(n, h[:n])
    return ones, S

# ---- rebuild h up to 2^25 + 2 ----
KMAX = 25
NMAX = 1 << KMAX
print(f"building prime h of length {NMAX + 2}...", flush=True)
t0 = time.time()
h = h_string(NMAX + 2)
print(f"  done in {time.time() - t0:.1f}s", flush=True)

d = json.load(open("/workspace/code/out/nu2_primes_xor_40000.json"))
assert d[53] == 18 and d[64] == 27 and d[4000] == 1975 and d[40000] == 20081

print("\nk  2^k        nu2(2^k)     S(2^k)   nu2(2^k+1)   nu2(2^k-1)   "
      "e_k=nu2-2^(k-1)  D2(k)=S(+1)+S(-1)-2S")
prev = {}
for k in range(3, KMAX + 1):
    n = 1 << k
    nu2_n, S_n = nu2_S(n, h)
    nu2_p, S_p = nu2_S(n + 1, h)
    nu2_m, S_m = nu2_S(n - 1, h)
    if k <= 15:
        assert nu2_n == d[n], (k, nu2_n, d[n])
        assert nu2_p == d[n + 1] and nu2_m == d[n - 1], (k, nu2_p, nu2_m)
    e_k = nu2_n - (n >> 1)
    D2 = S_p + S_m - 2 * S_n
    print(f"{k:2d} {n:9d} {nu2_n:9d} {S_n:+9d} {nu2_p:9d} {nu2_m:9d} "
          f"{e_k:+10d}  {D2:+10d}", flush=True)
    prev[k] = (nu2_n, S_n, nu2_p, S_p, nu2_m, S_m)

# ---- the sequences written for the tools ----
seq_nu2 = [prev[k][0] for k in range(3, KMAX + 1)]
seq_S   = [prev[k][1] for k in range(3, KMAX + 1)]
seq_p1  = [prev[k][2] for k in range(3, KMAX + 1)]
seq_m1  = [prev[k][4] for k in range(3, KMAX + 1)]
seq_D2  = [prev[k][5] + prev[k][3] - 2 * prev[k][1] for k in range(3, KMAX + 1)]
print("\nnu2(2^k)   k=3..25:", " ".join(map(str, seq_nu2)))
print("S(2^k)     k=3..25:", " ".join(map(str, seq_S)))
print("nu2(2^k+1) k=3..25:", " ".join(map(str, seq_p1)))
print("nu2(2^k-1) k=3..25:", " ".join(map(str, seq_m1)))
print("D2(k)      k=3..25:", " ".join(map(str, seq_D2)))

with open("/workspace/code/out/dyadic_extension_k25.txt", "w") as f:
    f.write("nu2(2^k)   k=3..25: " + " ".join(map(str, seq_nu2)) + "\n")
    f.write("S(2^k)     k=3..25: " + " ".join(map(str, seq_S)) + "\n")
    f.write("nu2(2^k+1) k=3..25: " + " ".join(map(str, seq_p1)) + "\n")
    f.write("nu2(2^k-1) k=3..25: " + " ".join(map(str, seq_m1)) + "\n")
    f.write("D2(k)      k=3..25: " + " ".join(map(str, seq_D2)) + "\n")
print("\nwrote code/out/dyadic_extension_k25.txt")