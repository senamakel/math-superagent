#!/usr/bin/env python3
"""KEY TEST: the d-sequence (division-count-per-level) characterization.

Each division performed at level k (k = x+y+z) removes ONE cell from level k
and adds THREE at level k+1. Let d_k = #{divisions performed at level k}.
Then the final level-histogram is determined by
   a_0 = 1 - d_0,  a_k = 3*d_{k-1} - d_k  (k>=1).
Feasibility: a_k >= 0  <=>  d_k <= 3*d_{k-1}.  Sum d_k = N; top level M has
a_M = 3 => d_{M-1} = 1 and d_M = 0; a_0 = 0 => d_0 = 1.

So candidate histograms <-> sequences (d_0=1, d_1, ..., d_{M-1}=1) with
   0 <= d_k <= 3 d_{k-1},  sum d_k = N.

TEST: is the set of histograms arising from such d-sequences EXACTLY the
observed reachable-histogram set for every N=2..14?  If yes, D(N) = sum over
d-sequences of the per-level product weight, and a DP over (sum, last d)
reaches N=10000 polynomially.
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

# observed reachable histograms
obs = {}   # N -> set of hist tuples (0,...)
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    hs = set()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        hs.add(tuple(map(int, hist.strip().split())))
    obs[n] = hs
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); m_i = line.index('mult=')
    hist_str = line[h+5:m_i].strip()
    vals = [int(x) for x in hist_str.split()]
    while vals and vals[-1] == 0: vals.pop()
    obs.setdefault(n, set()).add(tuple(vals))

def hist_from_d(d):
    """d = [d_0, d_1, ..., d_{M-1}]; returns histogram (a_0,..,a_M)."""
    a = [1 - d[0]]
    for k in range(1, len(d)):
        a.append(3*d[k-1] - d[k])
    a.append(3*d[-1])          # a_M = 3*d_{M-1}
    return tuple(a)

def feasible_d(N):
    """d-sequences with d_0=1, d_{M-1}=1, sum=N, all interior levels nonempty
    (a_k>=1), and a_k <= 7 (observed bound on level values)."""
    res = []
    def rec(d, s):
        if s > N: return
        if len(d) > N+1: return
        if d[-1] == 0: return
        if len(d) >= 2:
            a_prev = 3*d[-2] - d[-1]
            if a_prev < 1 or a_prev > 7: return
        if d[-1] == 1 and s == N:
            res.append(tuple(d)); return
        lst = d[-1]
        for nxt in range(0, 3*lst + 1):
            if s + nxt <= N:
                rec(d + [nxt], s + nxt)
    rec([1], 1)
    return res

print("N | observed histograms | d-seq histograms | set equal?")
ok_all = True
for n in sorted(obs):
    hs = obs[n]
    dhs = set(hist_from_d(d) for d in feasible_d(n))
    eq = (dhs == hs)
    if not eq:
        ok_all = False
        extra = dhs - hs
        missing = hs - dhs
        print(f"{n:>2} | {len(hs):>18} | {len(dhs):>16} | {eq}")
        print(f"      extra (d-seq but NOT observed): {sorted(extra)[:6]}")
        print(f"      missing (observed but NOT d-seq): {sorted(missing)[:6]}")
    else:
        print(f"{n:>2} | {len(hs):>18} | {len(dhs):>16} | {eq}")
print("\nALL EQUAL:", ok_all)