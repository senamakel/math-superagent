#!/usr/bin/env python3
"""Extend the Jump = Smooth-Run law (jump_closure_law.py / jump_smooth_run_law.py,
established to depth 165 at sieve 2e7) to the wider record: sieve 3e8, depth 240.

At a (2,4)-event (row k, edge A_k[b]=2, intruder A_k[b+1]=4, b = block length),
the jump j = b_{k+1} - b_k must equal
    L_k = (length of the maximal run of positions starting at b_k+1 whose
           consecutive halved entries differ by at most 1) - 1
i.e. the length of the initial 1-Lipschitz run of the halved row past the block,
minus one.  This is a one-row local fact.

Key extension: at sieve 2e7 the row-161 event was width-truncated (jump
recorded 176,181 = floor).  Here at sieve 3e8 the same event has EXACT jump
4,323,712 (landing 5,417,975, flooring 10,834,187), and the row-174 event is
new (jump 5,237,310, flooring 5,596,863).  Both must satisfy the law.

Oracle: b-profile rows 1..238 must match wider_width_b.json exactly (that
record is itself verified against blocks_depth1000.json rows 1..161 and by
two independent runs).
"""
import json
import numpy as np
from math import isqrt
import time

def primes_up_to(n):
    if n < 2: return []
    s = bytearray(b"\x01") * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = b"\x00" * (((n - i*i) // i) + 1)
    return [i for i in range(2, n + 1) if s[i]]

def bp(row):
    n = 0
    for x in row[1:]:
        if x in (0, 2): n += 1
        else: break
    return n

def main():
    t0 = time.time()
    LIM = 300_000_000; depth = 240
    stored = json.load(open("/workspace/code/out/wider_width_b.json"))
    print(f"sieve {LIM}; primes {stored['num_primes']}; depth {depth}")
    primes = primes_up_to(LIM)
    assert len(primes) == stored["num_primes"], (len(primes), stored["num_primes"])
    rows = [None] * (depth + 2)
    rows[1] = np.abs(np.diff(np.array(primes, dtype=np.int64)))
    for k in range(1, depth + 1):
        rows[k + 1] = np.abs(np.diff(rows[k]))
    ok = all(bp(rows[k]) == stored["b"][k - 1] for k in range(1, depth + 1))
    print(f"b-profile matches stored record (depth 240): {ok}")
    assert ok

    ev = []
    for k in range(1, depth):   # k -> k+1 transitions
        Ak = rows[k]; nxt = rows[k + 1]
        b = bp(Ak); e = int(Ak[b]); c = int(Ak[b + 1]) if b + 1 < len(Ak) else None
        j = bp(nxt) - b
        if (e, c) != (2, 4):
            continue   # erosion rows are not events
        # closure run of nxt from column b+1
        run = 0; col = b + 1
        while col < len(nxt) and nxt[col] in (0, 2): run += 1; col += 1
        # 1-Lipschitz chain of the halved row: unhalved consecutive diffs in {0,2}
        chainN = 1  # the intruder itself (halved 2)
        col = b + 1
        while col + 1 < len(Ak) and abs(int(Ak[col]) - int(Ak[col + 1])) in (0, 2):
            chainN += 1; col += 1
        L = chainN - 1
        past = int(Ak[col + 1]) if col + 1 < len(Ak) else None
        ev.append((k, j, run, L, int(Ak[b + 2]) if b + 2 < len(Ak) else None, past, b))

    print(f"(2,4)-events to depth 240: {len(ev)}")
    fail_run   = [x for x in ev if x[1] != x[2]]
    fail_chain = [x for x in ev if x[1] != x[3]]
    fail_stall = [x for x in ev if (x[1] == 0) != (x[4] == 0)]
    print(f"jump==closure-run : {'ALL PASS' if not fail_run else 'FAIL ' + str(fail_run[:3])}")
    print(f"jump==chain-1     : {'ALL PASS' if not fail_chain else 'FAIL ' + str(fail_chain[:3])}")
    print(f"stall iff Ak[b+2]==0: {'ALL PASS' if not fail_stall else 'FAIL ' + str(fail_stall[:3])}")

    print("\nall events with jump >= 1000 (giants), exact:")
    for (k, j, run, L, a2, past, b) in ev:
        if j >= 1000:
            print(f"  row {k:3d}: b_k={b:>9}  jump={j:>9}  closure-run={run:>9}  "
                  f"chain-1={L:>9}  match={j==run and j==L}  A_k[b+2]={a2}  past-chain(halved)={past}")

    print("\nall events at rows >= 155 (beyond old depth-165 exact regime):")
    for (k, j, run, L, a2, past, b) in ev:
        if k >= 155:
            print(f"  row {k:3d}: b_k={b:>9}  jump={j:>9}  closure-run={run:>9}  chain-1={L:>9}  "
                  f"match={j==run and j==L}  A_k[b+2]={a2}  past-chain(halved)={past}")
    print(f"elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
