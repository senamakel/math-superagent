#!/usr/bin/env python3
"""Core identity check for sign-coherence and riordan approaches.

Both approaches claim A_k(i) = |Delta_k(i)| where Delta_k is the k-th
signed forward difference. Test this exhaustively on small sequences.
"""
from math import comb
from itertools import product

def signed_fwd_diff(seq, k, i):
    return sum(((-1)**(k-j)) * comb(k,j) * seq[i+j] for j in range(k+1))

def absdiff_entry(seq, k, i):
    row = list(seq)
    for _ in range(k):
        row = [abs(row[j]-row[j+1]) for j in range(len(row)-1)]
    return row[i]

print("Demo counterexample: seq = [5,1,6]")
print("  A_2(0) =", absdiff_entry([5,1,6],2,0),
      " |signed fwd diff Delta_2(0)| =", abs(signed_fwd_diff([5,1,6],2,0)))
print("  (A_2(0)=|5-1-6|... let's see  A_1=[4,5], A_2=[1])")

n_mism = 0
first = []
total = 0
for L in range(2,6):
    for seq in product(range(6), repeat=L):
        for k in range(1, L):
            for i in range(L-k):
                total += 1
                absval = absdiff_entry(seq,k,i)
                fd = signed_fwd_diff(seq,k,i)
                if absval != abs(fd):
                    n_mism += 1
                    if len(first) < 10:
                        first.append((list(seq),k,i,absval,abs(fd)))
print(f"Checked {total} (seq,k,i) triples, L<=5 values 0..5")
print("Total mismatches:", n_mism)
for f in first:
    print("  ", f)
