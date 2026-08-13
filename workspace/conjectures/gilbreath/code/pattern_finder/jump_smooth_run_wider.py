#!/usr/bin/env python3
"""Extend the Jump = Smooth-Run law to the wider record: sieve 3e8, depth 240.

STREAMING version: keep only rows[k] and rows[k+1] at any time (each ~130MB
numpy int64 at width 16.2M), never the whole triangle.  Memory ~ 2 rows +
the prime index array.  (The first version OOM-killed by holding 240 rows.)

At a (2,4)-event (row k, edge A_k[b]=2, intruder A_k[b+1]=4, b = block length),
the jump j = b_{k+1} - b_k must equal
    L_k = (length of the maximal run of positions starting at b_k+1 whose
           consecutive halved entries differ by at most 1) - 1
i.e. length of the initial 1-Lipschitz run of the halved row past the block,
minus one.  One-row local fact (jump_smooth_run_law.py, verified to depth 165
at sieve 2e7 where row 161 was width-truncated).

Oracle: b-profile rows 1..238 must match wider_width_b.json.
"""
import json
import numpy as np
from math import isqrt
import time

def primes_idx(n):
    s = bytearray(b"\x01") * (n + 1); s[0] = s[1] = 0
    for i in range(2, isqrt(n) + 1):
        if s[i]: s[i*i::i] = b"\x00" * (((n - i*i) // i) + 1)
    return np.flatnonzero(np.frombuffer(s, dtype=np.uint8))

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
    print(f"sieve {LIM}; expected primes {stored['num_primes']}; depth {depth}")
    idx = primes_idx(LIM)
    print(f"primes: {len(idx)}  (expect {stored['num_primes']})")
    assert len(idx) == stored["num_primes"]
    primes = idx.astype(np.int64)

    cur = np.abs(np.diff(primes))          # row 1
    ev = []
    for k in range(1, depth + 1):
        nxt = np.abs(np.diff(cur))         # row k+1
        b = bp(cur)
        if k <= 238:
            assert b == stored["b"][k - 1], f"b mismatch at row {k}: {b} vs {stored['b'][k-1]}"
        if k < depth:
            e = int(cur[b]); c = int(cur[b + 1]) if b + 1 < len(cur) else None
            j = bp(nxt) - b
            if (e, c) == (2, 4):
                run = 0; col = b + 1
                while col < len(nxt) and nxt[col] in (0, 2): run += 1; col += 1
                chainN = 1; col = b + 1
                while col + 1 < len(cur) and abs(int(cur[col]) - int(cur[col + 1])) in (0, 2):
                    chainN += 1; col += 1
                L = chainN - 1
                past = int(cur[col + 1]) if col + 1 < len(cur) else None
                a2 = int(cur[b + 2]) if b + 2 < len(cur) else None
                ev.append((k, j, run, L, a2, past, b))
        del cur
        cur = nxt

    print(f"\n(2,4)-events to depth 240: {len(ev)}")
    fail_run   = [x for x in ev if x[1] != x[2]]
    fail_chain = [x for x in ev if x[1] != x[3]]
    fail_stall = [x for x in ev if (x[1] == 0) != (x[4] == 0)]
    print(f"jump==closure-run : {'ALL PASS' if not fail_run else 'FAIL ' + str(fail_run[:3])}")
    print(f"jump==chain-1     : {'ALL PASS' if not fail_chain else 'FAIL ' + str(fail_chain[:3])}")
    print(f"stall iff Ak[b+2]==0: {'ALL PASS' if not fail_stall else 'FAIL ' + str(fail_stall[:3])}")

    print("\ngiants (jump>=1000), exact:")
    for (k, j, run, L, a2, past, b) in ev:
        if j >= 1000:
            print(f"  row {k:3d}: b_k={b:>9}  jump={j:>9}  closure={run:>9}  chain-1={L:>9}  "
                  f"match={j==run and j==L}  A[b+2]={a2}  past-chain(halved)={past}")
    print("\nevents at rows >= 155:")
    for (k, j, run, L, a2, past, b) in ev:
        if k >= 155:
            print(f"  row {k:3d}: b_k={b:>9}  jump={j:>9}  closure={run:>9}  chain-1={L:>9}  "
                  f"match={j==run and j==L}  A[b+2]={a2}  past-chain(halved)={past}")
    print(f"elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
