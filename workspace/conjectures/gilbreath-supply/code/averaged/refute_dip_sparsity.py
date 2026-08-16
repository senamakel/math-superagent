#!/usr/bin/env python3
"""Independent refutation check of the dip-sparsity / M(N)-monotonicity claim.

Attack the tool_builder's claim that, for the prime switch-bit h,
    { n : nu2(n)/n < c }  is sparse (density -> 0)  for c = 0.40,
and that the averaged mean M(N) = (1/N) sum_{n=2..N} nu2(n)/n is monotone
(or at least bounded below on a density-1 set).

Three concrete failure modes are hunted:

  (i)  BOUNDARY EFFECT: are the dips (nu2/n < c) all at small n, so a
       density computed against the huge clean tail is misleading? We compare
       the dip-count in [50, 1000] against the dip-count in (1000, N] and,
       crucially, track whether *new* dips keep appearing past every fixed
       bound as N grows (a dip at growing n proves the set is not finite).

  (ii) THRESHOLD: is the set {n : nu2/n < c} actually sparse for c just
       above 0.40 -- c = 0.45, 0.48, 0.49 -- or does a positive fraction of n
       dip below those?  The claim pins sparsity at 0.40; if it is dense at
       any nearby c the margin of the claim is what is really at stake.

  (iii) MONOTONICITY of M(N): count and list upward violations
       (M(n) > M(n+1)), and test whether violations persist/grow with N
       rather than being a small-n transient.

All nu2(n) are computed exactly by the submask-product SOS transform
(lib.supply_fold.s_sos), verified against the literal oracle s_direct at the
start and re-verified at ANY spot marked suspicious (a dip) -- the c=0.40 dip
set is re-checked by the independent brute oracle.  The whole thing is one
parameterised script:

    python refute_dip_sparsity.py [N] [dmin]

Streams nu2(50)..nu2(N) one n at a time (never materialising a triangle).
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string


def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j = 0..n-1 (length n).
    Matches the lib convention (supply_fold reads h through index n-1)."""
    return h_string(n + 2)[:n]


def nu2_sos(n, h, dmin):
    S, ones = s_sos(n, h[:n])
    return ones


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100000
    dmin = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    n0 = 50

    # ---- independent oracle sanity on a spread of n ----
    ok = all(s_sos(n, prime_h(n))[1] == s_direct(n, prime_h(n))[1]
             for n in range(8, 61))
    print(f"oracle check s_sos==s_direct on n=8..60: {'OK' if ok else 'FAIL'}")

    h = prime_h(N)
    thresholds = [0.40, 0.45, 0.48, 0.49, 0.495]
    dips = {c: [] for c in thresholds}   # list of (n, ratio) below c
    # monotonicity: track M(n) and record upward violations
    m = 0.0
    count = 0
    prev_M = None
    viol = []                  # (n, M(n-1), M(n), delta) upward violations
    min_M = 1e9
    argmin_M = None
    # boundary bookkeeping
    tail_dips = {c: 0 for c in thresholds}     # dips in (1000, N]
    head_dips = {c: 0 for c in thresholds}     # dips in [50, 1000]
    first_beyond = {}          # largest n with a dip below each c (recurrence)

    for n in range(2, N + 1):
        v = nu2_sos(n, h, dmin)
        r = v / n
        count += 1
        m += r
        M = m / count          # M over the values counted (n=2..N)
        # track M over n=50..N convention as well -> use running mean from 50:
        if prev_M is None:
            prev_M = M
        else:
            if M < prev_M:
                viol.append((n, prev_M, M, M - prev_M))
            prev_M = M

        if M < min_M:
            min_M, argmin_M = M, n

        if n < n0:
            continue
        for c in thresholds:
            if r < c:
                dips[c].append((n, r))
                if c == 0.40:
                    first_beyond[c] = n
                if n <= 1000:
                    head_dips[c] += 1
                else:
                    tail_dips[c] += 1

    print(f"N = {N}, d in [{dmin}, n-1]")
    print(f"min M over n=2..{N}: {min_M:.4f} at n={argmin_M}")

    # ---- threshold sparsity ----
    print("\n--- (ii) threshold dip-counts (set {n: nu2/n < c}) ---")
    span = N - n0 + 1
    for c in thresholds:
        cnt = sum(1 for (n, _) in dips[c] if n >= n0)
        # max gap between consecutive dips >= n0 -> recurrence measure
        ns = [n for (n, _) in dips[c] if n >= n0]
        maxgap = 0
        if len(ns) >= 2:
            maxgap = max(ns[i] - ns[i - 1] for i in range(1, len(ns)))
        print(f"  c={c:<5} count={cnt:6d}  density={cnt/span:.4f}  "
              f"head[50,1000]={head_dips[c]}  tail(1000,{N}]={tail_dips[c]}  "
              f"maxgap={maxgap}  last dip at n={ns[-1] if ns else '--'}")

    # ---- (i) boundary: do new dips keep appearing for c=0.40? ----
    print("\n--- (i) c=0.40 dip growth with N (is the dip set dense/finite?) ---")
    d40 = [n for (n, _) in dips[0.40] if n >= n0]
    last10 = d40[-10:] if len(d40) >= 10 else d40
    print(f"  total c=0.40 dips in [50,{N}]: {len(d40)}, last 10 at n = {last10}")
    # cumulative count against N at several checkpoints -> linear vs sublinear
    chk = [1000, 2000, 5000, 10000, 20000, 50000, 100000]
    for k in chk:
        if k > N:
            break
        cntk = sum(1 for n in d40 if n <= k)
        # density among [50,k] *and* slope vs previous checkpoint
        print(f"    N={k:7d}: dip-count={cntk:5d}  "
              f"density in [50,{k}]={cntk/(k-49):.4f}")

    # ---- (iii) monotonicity of M(N) ----
    print("\n--- (iii) M(N) monotonicity violations ---")
    up = viol
    print(f"  upward violations of M (M(n)<M(n-1)): {len(up)}")
    print(f"  first 5: {up[:5]}")
    print(f"  last 5 (did violations recur at large N?): {up[-5:] if up else 'none'}")
    big = [x for x in up if x[0] > N // 2]
    print(f"  violations with n > N/2 = {N//2}: {len(big)} (persist at scale?)")

    # ---- independent re-check of every c=0.40 dip via the literal oracle ----
    print("\n--- independent oracle re-check of c=0.40 dips ---")
    bad = []
    for (n, r) in dips[0.40]:
        _, ones_direct = s_direct(n, prime_h(n))
        if ones_direct != nu2_sos(n, h, dmin):
            bad.append((n, ones_direct, nu2_sos(n, h, dmin)))
    print(f"  c=0.40 dips re-computed by s_direct: {len(dips[0.40])} spots, "
          f"{'ALL MATCH' if not bad else ('MISMATCH ' + str(bad))}")

    # also re-check a spread of 'clean' (non-dip) spots independently
    import random
    random.seed(1)
    spots = random.sample(range(60, N + 1), min(40, N - 59))
    mism = 0
    for n in spots:
        if s_direct(n, prime_h(n))[1] != nu2_sos(n, h, dmin):
            mism += 1
    print(f"  spot re-check on 40 random n in [60,{N}]: {mism} mismatches")


if __name__ == "__main__":
    main()
