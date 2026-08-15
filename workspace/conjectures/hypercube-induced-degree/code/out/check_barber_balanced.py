#!/usr/bin/env python3
"""Oracle check for Barber's balanced-independent-set formula (arXiv:1210.4029).

Settles the transcription contradiction in the library: the source prose and the
claim block disagree on the odd-n constant, and the even formula looks wrong at
n=2 (Q_2 is a 4-cycle whose true max balanced independent set is 0, since every
even vertex is adjacent to both odd vertices).

For n=2..5 brute-force the TRUE maximum size of a *balanced* independent set of
Q_n (equal # even and # odd vertices, no edges between them) and compare with:

  even: 2^(n-1) - 2^(n-3)*(n-2)
  odd v1 (source prose/abstract): 2^(n-1) - 2^(n-2)*(n-1)
  odd v2 (source theorem text / summary / claim block): 2^(n-1) - 2^(n-2)*(n-1)/2

Reduction: parity class X_0 (even weight) is independent, X_1 independent.
A maximal balanced set = A ⊆ X_0, B ⊆ X_1, |A|=|B|=k, no A-B edges.  B can be any
subset of X_1 \ N(A), so given A the best k = min(|A|, |X_1| - |N(A)|); maximise 2k
over all A ⊆ X_0.  Exhaustive over all A ⊆ X_0 (m = 2^(n-1), fine for n <= 5).

Run:  sh code/out/run_barber_check.sh
"""
from itertools import combinations

def popcount(v): return bin(v).count("1")

def truth(n):
    N = 1 << n
    X0 = [v for v in range(N) if popcount(v) % 2 == 0]
    X1 = [v for v in range(N) if popcount(v) % 2 == 1]
    X1set = set(X1)
    nhood = {u: {u ^ (1 << i) for i in range(n) if (u ^ (1 << i)) in X1set}
             for u in X0}
    best = 0
    m = len(X0)
    for r in range(m + 1):
        for comb in combinations(X0, r):
            un = set()
            for u in comb:
                un |= nhood[u]
            k = min(r, len(X1) - len(un))
            if k > best:
                best = k
    return 2 * best

for n in range(2, 6):
    t = truth(n)
    even = 2**(n-1) - 2**(n-3)*(n-2)
    v1 = 2**(n-1) - 2**(n-2)*(n-1)
    v2 = 2**(n-1) - (2**(n-2)*(n-1))//2
    print(f"n={n}  true_balanced_max={t}  even_formula={even}  odd_v1={v1}  odd_v2={v2}")
