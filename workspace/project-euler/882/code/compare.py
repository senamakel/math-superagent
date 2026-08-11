#!/usr/bin/env python3
"""Compare real-game S(n) (brute.py) with counting-game S(n) (counting.py)."""
import sys
sys.path.insert(0, '/workspace')
from brute import S_real, initial_multiset
from counting import need_oneturn, A_of_n, B_of_n

def S_counting_n(n):
    A, B = A_of_n(n), B_of_n(n)
    v = need_oneturn(A, B, {}, {})
    return int(v)

print("n | real-game S | counting-game S | match")
all_ok = True
for n in range(1, 9):
    sr = S_real(n)[0]
    sc = S_counting_n(n)
    ok = (sr == sc)
    all_ok = all_ok and ok
    print(f"{n} | {sr:10d} | {sc:13d} | {'OK' if ok else 'MISMATCH'}")
print("ALL MATCH" if all_ok else "MISMATCH FOUND")