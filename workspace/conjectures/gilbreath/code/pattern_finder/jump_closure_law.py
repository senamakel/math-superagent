#!/usr/bin/env python3
"""Verify the jump-closure law exactly over real prime rows.

Claim (mechanism localization): at a (2,4)-regeneration event of row k with
block length b_k, the jump j_k = b_{k+1} - b_k equals the length of the
run of {0,2} entries in row k+1 starting at column b_k+1, i.e.

  j_k = 1 + L_k   where L_k = #{t>=2 : |A_k[b_k+t] - A_k[b_k+t+1]| in {0,2}, consecutive}

Equivalently: j_k = 0 iff A_k[b_k+2] not in {4,6}; otherwise j_k counts how
many consecutive iterated-difference pairs past the intruder differ by at
most 2.  The jump is determined ENTIRELY by row-k values strictly beyond the
block; nothing inside the block matters except the edge x=A_k[b_k]=2.

Oracle: sieve to 20,000,000 (1,270,607 primes, same as blocks_depth1000.json),
depth 165, numpy int64; b profile compared against the stored record.
"""
import json
import numpy as np
from math import isqrt
import sys, time

def primes_up_to(n):
    if n < 2: return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, isqrt(n) + 1):
        if sieve[i]:
            sieve[i*i::i] = b"\x00" * (((n - i*i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]

def block_profile(row):
    # row[0] is the leading 1; block = run of {0,2} starting at position 1
    n = 0
    for x in row[1:]:
        if x in (0, 2): n += 1
        else: break
    return n

def main():
    t0 = time.time()
    LIM = 20_000_000
    depth = 165
    print(f"sieve to {LIM} ...", flush=True)
    primes = primes_up_to(LIM)
    print(f"primes: {len(primes)}", flush=True)
    stored = json.load(open("/workspace/code/out/blocks_depth1000.json"))
    sb = stored["b"]
    assert len(sb) >= depth + 1
    assert stored["sieve_limit"] == LIM and stored["num_primes"] == len(primes)

    cur = np.array(primes, dtype=np.int64)
    # rows: cur is A_k (0-based k=0 is the prime row); we need A_k for k=1..depth
    # A_1 = diff of primes
    cur = np.abs(np.diff(cur))
    b_rec = []
    events = []   # (k, j, intruder) with jump j = b_{k+1}-b_k > 0 or == 0 stalls recorded
    for k in range(1, depth + 1):
        b = block_profile(cur)
        b_rec.append(b)
        # intruder: first entry past the block (may not exist near the end)
        intr = cur[b + 1] if b + 1 < len(cur) else None
        if k < depth:
            nxt = np.abs(np.diff(cur))
            bn = block_profile(nxt)
            events.append((k, bn - b, intr, b))
            cur = nxt
        else:
            # also compute next for the record? not needed
            pass
    # compare stored block profile
    matches = sum(1 for k in range(depth) if b_rec[k] == sb[k])
    print(f"depth {depth}: b-profile matches stored record: {matches}/{depth}")
    assert matches == depth, "b mismatch — oracle disagreement, aborting"

    # Now verify the jump-closure law on the recorded (k, j, intr, b) events.
    # Recompute rows again cleanly to have both A_k and A_{k+1}.
    allok = True
    fails = []
    detail = []
    cur = np.abs(np.diff(np.array(primes, dtype=np.int64)))
    rows = [None] * (depth + 2)
    rows[1] = cur
    for k in range(1, depth + 1):
        rows[k + 1] = np.abs(np.diff(rows[k]))
    for (k, j, intr, b) in events:
        if intr is None or k + 1 > depth:
            continue
        Ak = rows[k]; Ak1 = rows[k + 1]
        # closure run of row k+1 starting at column b+1 (0-based index b+1 since
        # row[0] is leading 1 and block positions are 1..b)
        # column c (1-based) is index c in the array
        run = 0
        c = b + 1
        while c < len(Ak1) and Ak1[c] in (0, 2):
            run += 1; c += 1
        law_ok = (run == j)
        if not law_ok:
            allok = False
            fails.append((k, j, run))
        # row-k characterization: j-1 extra positions need consecutive pair
        # differences in {0,2} starting at column b+2
        L = 0
        if j >= 1:
            t = 2
            while t <= j:   # need |Ak[b+t]-Ak[b+t+1]| in {0,2} for t=2..j
                if b + t + 1 < len(Ak) and abs(int(Ak[b+t]) - int(Ak[b+t+1])) in (0, 2):
                    L += 1; t += 1
                else:
                    break
        char_ok = (L == j - 1)
        if not char_ok:
            allok = False
            fails.append((k, "char", j, L))
        detail.append((k, j, intr, b, run, L, int(Ak[b+2]) if b+2 < len(Ak) else None))
    print(f"closure-run law (jump == next-row {{0,2}}-run past block): {'ALL PASS' if allok else 'FAIL'}")
    if fails:
        print("failures:", fails[:10])
    # summarized detail rows
    print(f"\n{'k':>4} {'j':>7} {'intr':>4} {'b':>9} {'runA':>5} {'L':>5} {'Ak[b+2]':>8}")
    for (k, j, intr, b, run, L, a2) in detail:
        print(f"{k:>4} {j:>7} {intr:>4} {b:>9} {run:>5} {L:>5} {str(a2):>8}")

    # Distribution check: are big jumps associated with "flat" row-k windows?
    big = [d for d in detail if d[1] >= 1000]
    small = [d for d in detail if 0 < d[1] < 1000]
    stall = [d for d in detail if d[1] == 0]
    print(f"\nevents: {len(detail)} total, big(j>=1000): {len(big)}, small(0<j<1000): {len(small)}, stall(j=0): {len(stall)}")
    print("stall rows Ak[b+2] values:", sorted(set(d[6] for d in stall)))
    print("nonstall rows Ak[b+2] values:", sorted(set(d[6] for d in detail if d[1] > 0)))
    print(f"elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()