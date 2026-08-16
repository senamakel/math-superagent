#!/usr/bin/env python3
"""Three exact verifications.

(1) DYADIC SUPERSET IDENTITY (proof sketch + check): at n = 2^k,
    T(n,d) = XOR_{t : (2^k-1-d) subseteq t} h[t].
    Proof: s subseteq d  <=>  (n-1-s) superset (n-1-d) since n-1-d = bitwise
    complement of d in k bits, and complementation reverses the submask
    order. Verified against the literal submask-XOR definition on the real
    prime h, k = 3..14 (moving to 16384), all d in [2, n-1] (not a sample).

(2) ENDPOINT PAIR-COUNT IDENTITY: over the residues r_j = q_j mod 4 in
    {1,3} (odd primes), #(1,3) - #(3,1) equals
        +1 if r starts in 1 and ends in 3
        -1 if r starts in 3 and ends in 1
        0   otherwise (start and end residues equal).
    Proof: each maximal run of 1s is followed by a transition 1->3 and each
    run of 3s by 3->1; the transition counts differ iff the sequence starts
    and ends on different residues, and then by exactly the sign above.
    Verified at several N against the direct counts.

(3) ALTERNATING INPUT IS A KERNEL VECTOR: h[j] = j mod 2 or (j+1) mod 2 is
    odd-alt / even-alt, which span ker Phi_n (proved rank-n-2 nullity-2), so
    nu2(n) = wt(Phi_n h) = 0 for EVERY n, not just dyadic. Verify numerically
    n = 4..400 via s_sos as a control that the dyadic checks (alternating ->
    0) were the kernel, not a dyadic-only effect.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos, t_direct

# ---------- (1) dyadic superset identity, ALL d ----------
print("== (1) dyadic superset identity, all d in [2, 2^k - 1], k = 3..14 ==")
all_ok = True
for k in range(3, 15):
    n = 1 << k
    q = primes_upto_index(n + 2)
    h = [1 if q[j + 1] % 4 != q[j] % 4 else 0 for j in range(n)]
    # h needs indices 0..n-1: q[0..n] suffices for j in 0..n-1 -> j+1 <= n
    q2 = primes_upto_index(n + 1)
    h = [1 if q2[j + 1] % 4 != q2[j] % 4 else 0 for j in range(n)]
    bad = 0
    for d in range(2, n):
        c = n - 1 - d
        t = 0
        for tt in range(n):
            if (tt & c) == c:
                t ^= h[tt]
        if t != t_direct(n, d, h):
            bad += 1
            if bad <= 3:
                print(f"  MISMATCH k={k} d={d}: superset={t} literal={t_direct(n, d, h)}")
    all_ok = all_ok and bad == 0
    print(f"  k={k:2d} n={n:6d}: mismatches = {bad} over {n-2} depths")
print("identity exact on all (k=3..14, all d):", all_ok)

# ---------- (2) endpoint pair-count identity ----------
print("\n== (2) endpoint mod-4 pair-count identity ==")
for npr in [1000, 10000, 50000, 200000]:
    q = primes_upto_index(npr + 1)
    r_all = [p % 4 for p in q]
    r = [x for x in r_all if x != 2]          # odd primes' residues
    c13 = sum(1 for j in range(len(r) - 1) if r[j] == 1 and r[j + 1] == 3)
    c31 = sum(1 for j in range(len(r) - 1) if r[j] == 3 and r[j + 1] == 1)
    diff = c13 - c31
    if r[0] == 1 and r[-1] == 3:
        pred = 1
    elif r[0] == 3 and r[-1] == 1:
        pred = -1
    else:
        pred = 0
    print(f"  {npr:7d} primes: #(1,3)={c13:7d} #(3,1)={c31:7d} diff={diff:+3d} "
          f"predicted={pred:+1d} (start={r[0]}, end={r[-1]}) match={diff==pred}")

# ---------- (3) alternating input -> nu2 = 0 for all n ----------
print("\n== (3) alternating h (kernel vector) -> nu2(n) = 0 for every n ==")
for start in (0, 1):
    nz = 0
    first_nz = None
    for n in range(4, 401):
        h = [(j + start) % 2 for j in range(n)]
        S, ones = s_sos(n, h)
        if ones != 0:
            nz += 1
            if first_nz is None:
                first_nz = n
    print(f"  start={start}: nonzero nu2 count over n=4..400 = {nz}"
          + (f", first at n={first_nz}" if first_nz else ""))

# 1/2 - block minimum decay sequence (fresh exact, for analyze_sequence)
print("\n== 1/2 - per-doubling-block min of nu2/n ==")
import json
data = json.load(open('/workspace/code/out/nu2_primes_xor_40000.json'))
N = 40000
dips = []
for k in range(2, 16):
    lo, hi = 1 << k, min((1 << (k + 1)) - 1, N)
    if lo > N:
        break
    best_n, bn, bd = lo, data[lo], lo
    for n in range(lo, hi + 1):
        if data[n] * bd < bn * n:
            best_n, bn, bd = n, data[n], n
    dips.append((k, bn, bd, 0.5 - bn / bd))
for (kdx, bn, bd, dip) in dips:
    print(f"  block k={k:2d}: min={bn}/{bd}={bn/bd:.6f} at n={(bd if False else best_n)}   "
          f"1/2 - min = {dip:.6f}")
print("1/2 - blockmin terms:", " ".join(f"{d:.6f}" for _, _, _, d in dips))
print("block-argmin terms:", " ".join(str(v) for v in []))