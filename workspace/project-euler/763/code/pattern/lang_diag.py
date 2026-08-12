#!/usr/bin/env python3
"""Diagnose the over-generation: which walks at N are NOT reachable histograms,
and what distinguishes them? Check hypotheses:
  H1: extra walks pass through the value 3 mid-way (visit 3 twice).
  H2: extra walks exceed the max reachable length M at that N.
  H3: extra walks use a transition that appears only at higher N (union too loose).
"""
import glob, collections

def sorted_key(p):
    return int(p.split('level_')[1].split('.')[0])

all_hists = {}
for path in sorted(glob.glob('data/level_*.txt'), key=sorted_key):
    n = sorted_key(path)
    hs = set()
    for line in open(path):
        hist, M, bbox = line.rstrip().split('|')
        hs.add(tuple(map(int, hist.strip().split())))
    all_hists[n] = hs

# union transitions + per-N transitions
trans_all = set()
trans_byN = {}
for n, hs in all_hists.items():
    T = set()
    for h in hs:
        for k in range(len(h)-1):
            T.add((h[k], h[k+1]))
    trans_byN[n] = T
    trans_all |= T

def enumerate_walks(transet, target_sum, maxlen):
    res = []
    def rec(cur, L, s, path):
        if L > maxlen: return
        if cur == 3 and s == target_sum:
            res.append(tuple(path)); return
        if s > target_sum: return
        for nxt in range(0,9):
            if (cur, nxt) in transet:
                rec(nxt, L+1, s+nxt, path+[nxt])
    rec(0,0,0,[0])
    return set(res)

for n in (9, 10):
    hs = all_hists[n]
    S = 2*n+1
    maxlen = max(len(h) for h in hs)
    extra = enumerate_walks(trans_all, S, maxlen) - hs
    print(f"=== N={n} (S={S}, maxlen={maxlen}): {len(extra)} extra walks")
    for w in sorted(extra):
        passes3 = w.count(3) > 1
        # transitions used by this walk that are NOT in trans_byN[n]
        newtrans = [(w[j],w[j+1]) for j in range(len(w)-1) if (w[j],w[j+1]) not in trans_byN[n]]
        print(f"   {w}  passes3={passes3}  uses_N>=9_trans={newtrans}")