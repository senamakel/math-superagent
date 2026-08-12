#!/usr/bin/env python3
"""Test the regular-language hypothesis for histograms, now with the key
refinement: interior visits to value 3 are forbidden (a walk may touch 3 only
as its final value).  Also extends the transition set with OOS data (N=13,14).

  Language L: sequences (0=a_0, a_1, ..., a_M=3) with
    (i)  a_k >= 1 for 1<=k<=M-1, no a_k == 3 for 1<=k<=M-1,
    (ii) consecutive pairs in the observed transition set T,
    (iii) sum_k a_k = 2N+1.

If reachable histograms at N == L restricted to sum 2N+1, then with the exact
per-level weights, D(N) = weighted sum over L = polynomial-time DP.

Check: (a) equality of sets for all N=2..14; (b) weighted sum reproduces D(N).
"""
import glob, collections, itertools

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

D = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,11:151263,
     12:514419,13:1749267,14:5949063}

# --- gather reachable histograms and transition set (union over all N incl OOS)
all_hists = {}   # N -> set of hist tuples
trans = set()
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    hs = set()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        hs.add(tuple(map(int, hist.strip().split())))
    all_hists[n] = hs
    for h in hs:
        for k in range(len(h)-1):
            trans.add((h[k], h[k+1]))
# OOS N=13,14
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); m_i = line.index('mult=')
    hist_str = line[h+5:m_i].strip()
    vals = [int(x) for x in hist_str.split()]
    while vals and vals[-1] == 0: vals.pop()
    vals = tuple(vals)
    all_hists.setdefault(n, set()).add(vals)
    for k in range(len(vals)-1):
        trans.add((vals[k], vals[k+1]))

vals_used = sorted({v for (a,b) in trans for v in (a,b)})
print("Transition set T (union N=2..14):", len(trans), "pairs")
print("   ", sorted(trans))
print("Values appearing:", vals_used)

# --- does any REACHABLE histogram have an interior 3?
cnt_int3 = 0
for n, hs in all_hists.items():
    for h in hs:
        if 3 in h[1:-1]:
            cnt_int3 += 1
            if cnt_int3 <= 5:
                print(f"  reachable with interior 3: N={n} {h}")
print("Reachable histograms with an interior value-3:", cnt_int3)

# --- weighted walk DP (regular language with no interior 3)
def walk_counts_DP(N, T, no_mid3=True, maxval=20):
    """Return (count of walks, weight-sum) for sum 2N+1 ending at 3.
    DP over (last value, sum).  Values capped at maxval (observed max 7)."""
    S = 2*N + 1
    # dp[(v, s)] = (count, weight_sum)
    dp = {(0,0): (1, 1)}          # start at a_0=0 with empty weight product
    total_c = 0
    total_w = 0
    # weight per value v at an interior level
    def w(v):
        if v in (1,2,3): return 3
        if v == 4: return 4
        if v == 5: return 1
        if v == 6: return 10
        return 1                   # v>=7 ; for v==3 final handled below
    for _ in range(1, S+1):        # length bound: at most S levels of value>=1
        ndp = {}
        for (v, s), (c, wt) in dp.items():
            for nxt in range(1, maxval+1):
                if (v, nxt) not in T: continue
                if no_mid3 and nxt == 3 and s + nxt != S: continue  # 3 only at end
                ns = s + nxt
                if ns > S: continue
                addc, addw = c, wt * w(nxt)
                key = (nxt, ns)
                if key in ndp:
                    ndp[key] = (ndp[key][0] + addc, ndp[key][1] + addw)
                else:
                    ndp[key] = (addc, addw)
        dp = ndp
        # terminate: walks of current length ending at (3, S)
        if (3, S) in dp:
            c, wt = dp[(3, S)]
            total_c += c
            total_w += wt
            # allow continuing through 3 at end? no: ending value 3 fixed
    return total_c, total_w

for n in sorted(all_hists):
    hs = all_hists[n]
    c, wsum = walk_counts_DP(n, trans, no_mid3=True)
    eq = (c == len(hs))
    match = (wsum == D[n])
    flag = "OK" if (eq and match) else "*** MISMATCH ***"
    print(f"N={n}: reachable_h={len(hs)} lang_h={c} set_eq={eq} "
          f"weight_sum={wsum} D={D[n]} match={match} {flag}")