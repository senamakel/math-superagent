#!/usr/bin/env python3
"""Diagnose the P=2 power-of-2 count discrepancy: literal scan says nu2=1,
host stage-1 says 2.  Dump the exact right diagonal for P=2 word=01 at a few
n and show the maximal {0,2} suffix under both the literal (i>=0) and the
i>2 conventions, plus where the 2s sit.
"""
import sys
sys.path.insert(0, '/workspace/code')

def build_q(h_pattern, n_terms):
    P = len(h_pattern)
    q = [2, 3]
    while len(q) < n_terms:
        bit = h_pattern[(len(q) - 2) % P]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]

def full_triangle(q):
    rows = [list(q)]
    while len(rows[-1]) > 1:
        r = rows[-1]
        rows.append([abs(r[i]-r[i+1]) for i in range(len(r)-1)])
    return rows

for P, word in [(2,[0,1]),(4,[0,0,0,1]),(8,[0,0,0,0,0,0,0,1]),(1,[1])]:
    print("="*60)
    print(f"P={P} word={''.join(map(str,word))}")
    q = build_q(word, 20)
    print("q    =", q[:12])
    rows = full_triangle(q)
    for n in (5, 9, 12):
        diag = [rows[k][n-k] for k in range(n+1)]
        body = diag[:-1]
        # literal suffix
        i = len(body)-1
        while i >= 0 and body[i] in (0,2):
            i -= 1
        lit_suffix = body[i+1:]
        # i>2 suffix
        j = len(body)-1
        while j > 2 and body[j] in (0,2):
            j -= 1
        cyc_suffix = body[j+1:]
        print(f" n={n} diag={diag}")
        print(f"     literal suffix={lit_suffix} (#2={lit_suffix.count(2)})")
        print(f"     i>2     suffix={cyc_suffix} (#2={cyc_suffix.count(2)})")
