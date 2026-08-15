#!/usr/bin/env python3
"""Fresh independent check of the recharge-surplus monotonicity S_k >= 0 and the
conjecture-equivalent S_k >= k-2, on fresh rows beyond the depth-1000 record.

S_k = b_k - b_1 + (k-1), with b_k = leading {0,2} block length of row k.
Conjecture is exactly S_k >= k-2 for all k (equivalently b_k >= b_1 - 1 ... ).
Also test: does b_k ever return to near b_1=2 / near the floor 0 in a fresh deep run.
Exact ints, one row live.
"""
from lib.gilbreath import primes_up_to

def block_length(row):
    # leading run of {0,2} starting at index 1 (entry 1 = second entry)
    b = 0
    for x in row[1:]:
        if x in (0, 2): b += 1
        else: break
    return b

def run(primes, depth):
    row = primes[:]
    b = [None]*(depth+1)
    # b[k] = leading {0,2} block length of row k (row 1 = first differences)
    for k in range(1, depth+1):
        nxt = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
        row = nxt
        b[k] = block_length(row)
    return b

primes = primes_up_to(20000000)  # 1,270,607 primes
depth = 600
b = run(primes, depth)
b1 = b[1]
S = [b[k] - b1 + (k-1) for k in range(1, depth+1)]
viol_mono = 0
viol_conj = 0
viol_margin = 0
for k in range(1, depth+1):
    if S[k-1] < 0: viol_mono += 1
    if S[k-1] < k-2: viol_conj += 1
    # margin: S_k - (k-1) = b_k - b_1 ; conjecture needs this >= -1
    if b[k] - b1 < -1: viol_margin += 1
print(f"fresh depth-{depth}, sieve 2e7, b_1={b1}")
print(f"S monotone (S_k>=0) violations: {viol_mono}")
print(f"conjecture form (S_k>=k-2) violations: {viol_conj}")
print(f"b_k < b_1-1 violations: {viol_margin}")
print(f"min b over rows: {min(b[1:])}, min S: {min(S)}, final S: {S[-1]}")
print(f"b_1={b[1]}, b_2={b[2]}, ... b_40={b[40]}")
