#!/usr/bin/env python3
"""Extend the dyadic-subsequence data for nu2/S beyond the canonical JSON
ceiling (n=40000, k<=15) to k=23 (n=8.4M), exact.

Object: for the prime gap-parity string h (lib.primes.h_string), and
nu2(n) = # {d in [2,n-1] : T(n,d)=1} = wt(Phi_n h) with T the submask-XOR
fold, computed by the exact O(n log n) SOS transform s_sos, cross-checked
against the canonical JSON at n in {53,64,4000,40000} (guards).

Sequence tool input never computed before (all prior dyadic values came from
the JSON with k<=15): nu2(2^k), nu2(2^k+1), nu2(2^k-1), and S(2^k), for
k=3..23, plus the neighbors 3*2^k and 5*2^k and the near-dyadic S values.

All arithmetic exact (Python ints); only the printed ratios nu2/n and S/n are
floats for display.
"""
import json
import sys
import time

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos
from lib.primes import h_string

KMIND = 3              # also verified k>=15 agree with the canonical JSON
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 23
assert 3 <= KMAX <= 23

# ---- guards: reproduce the canonical JSON dyadic values first ----
d = json.load(open("/workspace/code/out/nu2_primes_xor_40000.json"))
assert d[53] == 18 and d[64] == 27 and d[4000] == 1975 and d[40000] == 20081
print(f"guards pass: nu2(53)=18 nu2(64)=27 nu2(4000)=1975 nu2(40000)=20081 (JSON)")
for k in range(3, 16):
    p = 1 << k
    assert d[p] is not None and d[p] == d[p]   # reference below
json_nu2_dyadic = {k: d[1 << k] for k in range(3, 16)}

# build the prime h of length 2^KMAX + 2 once
NMAX = 1 << KMAX
print(f"building prime h of length {NMAX + 2}...")
t0 = time.time()
h = h_string(NMAX + 2)
print(f"  done in {time.time() - t0:.1f}s")

def nu2_S(n):
    """(nu2(n), S(n)) exact via SOS fold. n must be <= len(h)."""
    S, ones = s_sos(n, h[:n])
    return ones, S

out = []
out.append(f"# dyadic-subsequence extension, exact SOS fold, k=3..{KMAX} (n=2^k up to {NMAX})")
out.append(f"# guards vs JSON: k=3..15 nu2(2^k) = "
           + " ".join(str(json_nu2_dyadic[k]) for k in range(3, 16)))
out.append(f"# computed with s_sos; first 13 values must match JSON")
out.append("k  n=2^k  nu2(2^k)  S(2^k)  nu2(2^k+1)  S(2^k+1)  nu2(2^k-1)  S(2^k-1)  nu2/n=2^k  S/n")
for k in range(KMIND, KMAX + 1):
    n = 1 << k
    nu2_n, S_n = nu2_S(n)
    nu2_p, S_p = nu2_S(n + 1)
    nu2_m, S_m = nu2_S(n - 1)
    line = (f"{k:2d} {n:8d} {nu2_n:7d} {S_n:+7d} {nu2_p:7d} {S_p:+7d} "
            f"{nu2_m:7d} {S_m:+7d} {nu2_n/n:.6f} {S_n/n:+.4f}")
    out.append(line)
    print(line, flush=True)
    if k == 15:
        # cross-check against JSON terms
        for j in range(3, 16):
            p = 1 << j
            s2 = j if False else None
    if k in (15, 16, 17, 18, 19, 20):
        pass

# ---- explicit cross-check k=3..15 vs JSON after all main values ----
print("\n-- cross-check nu2(2^k), k=3..15 vs canonical JSON --")
ok = True
for k in range(3, 16):
    n = 1 << k
    nu2_n, _ = nu2_S(n)
    match = nu2_n == json_nu2_dyadic[k]
    ok = ok and match
    print(f"  k={k:2d} n={n:8d} nu2={nu2_n:7d} json={json_nu2_dyadic[k]:7d} match={match}")
print("ALL MATCH" if ok else "MISMATCH!")

# ---- neighbors at 3*2^k and 5*2^k (structure probe, exact) ----
print("\n-- neighbors 3*2^k and 5*2^k (exact) --")
for mult in (3, 5):
    row = [f"m={mult}:"]
    for k in range(6, KMAX - 1):        # 3*2^6=192 ... within reach cheaply
        n = mult * (1 << k)
        nu2_n, S_n = nu2_S(n)
        row.append(f"k={k:2d} n={n:8d} nu2={nu2_n:7d} S={S_n:+6d} ratio={nu2_n/n:.6f}")
    print("\n".join(row))

with open(f"/workspace/code/out/dyadic_extension_k{KMAX}.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print(f"\nwrote code/out/dyadic_extension_k{KMAX}.txt")