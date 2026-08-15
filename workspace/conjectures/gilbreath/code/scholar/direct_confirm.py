#!/usr/bin/env python3
import importlib.util, sys, os
os.environ.setdefault("PYTHONPATH", "/workspace/code")

# ensure lib is importable even without PYTHONPATH
sys.path.insert(0, "/workspace/code")
from lib.rightdiag import cycle_and_nu2
from math import comb

def build_2thenodds(word, n_terms):
    p = len(word)
    gaps = [2 if word[j % p] == 0 else 4 for j in range(n_terms)]
    q = [2, 3]
    for g in gaps:
        q.append(q[-1] + g)
    return q

def delta_diag(q):
    D = [q[0]]
    diags = [list(D)]
    for n in range(1, len(q)):
        nd = [0]*(n+1)
        nd[0] = q[n]
        for k in range(1, n+1):
            nd[k] = abs(nd[k-1] - D[k-1])
        D = nd
        diags.append(list(D))
    return diags

def nu2_for(word, n):
    q = build_2thenodds(word, n)
    diags = delta_diag(q)
    diag = diags[-1]
    tau, nu2 = cycle_and_nu2(diag)
    return nu2

n_vals = [200, 1000, 3000, 6000]
tests = [
    ("P=2 alt", [0,1]),
    ("P=2 tail1", [1,0]),
    ("P=3 tail1", [0,0,1]),
    ("P=4", [0,0,0,1]),
    ("P=5 tail1", [0,0,0,0,1]),
    ("P=7 tail1", [0,0,0,0,0,0,1]),
]
for name, word in tests:
    row = [nu2_for(word, n) for n in n_vals]
    print("%-14s %s" % (name, row))
