#!/usr/bin/env python3
"""Exact verification of the Jump = Smooth-Run law at all regeneration events.

Statement (proved from the operator definition, verified here over the real
prime rows): at a row k with block length b_k whose edge is 2 and intruder is
4 (the (2,4)-event, the ONLY regeneration mechanism per the step law), write
h = halved row A_k/2 (all entries even). Then the next row's block length is

    b_{k+1} = b_k + L_k

where L_k = (length of the maximal run of positions starting at b_k+1 whose
consecutive halved entries differ by at most 1) - 1.  I.e. the jump is the
length of the initial 1-Lipschitz run of the halved row past the block,
minus one.  In unhalved terms: L_k = #{i>=1 : |A_k[b+i] - A_k[b+i+1]| in {0,2}}.

Equivalently the jump is determined ENTIRELY by row-k values in the window
[b_k+1, b_k+j+2]: a one-row local fact, the same locality as the step law.

Consequences verified exactly:
  * jump == {0,2}-run of row k+1 starting at column b_k+1 (closure-run form)
  * jump == number of consecutive |halved diff| <= 1 starting at b_k+1 (chain form)
  * stall (jump 0) iff A_k[b_k+2] == 0 (halved value 0, |4-0|=4 not in {0,2})

Oracle: same sieve as blocks_depth1000.json (2e7, 1270607 primes), numpy
int64, depth 165; b-profile compared against the stored record.
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
    LIM = 20_000_000; depth = 165
    stored = json.load(open("/workspace/code/out/blocks_depth1000.json"))
    print(f"sieve {LIM}; primes {stored['num_primes']}; depth {depth}")
    primes = primes_up_to(LIM)
    assert len(primes) == stored["num_primes"]
    rows = [None] * (depth + 2)
    rows[1] = np.abs(np.diff(np.array(primes, dtype=np.int64)))
    for k in range(1, depth + 1):
        rows[k + 1] = np.abs(np.diff(rows[k]))
    # oracle check
    ok = all(bp(rows[k]) == stored["b"][k - 1] for k in range(1, depth + 1))
    print(f"b-profile matches stored record: {ok}")
    assert ok

    ev = []   # (k, j, edge, intr, runA, chainN)
    for k in range(1, depth):   # k -> k+1 transitions
        Ak = rows[k]; nxt = rows[k + 1]
        b = bp(Ak); e = int(Ak[b]); c = int(Ak[b + 1]) if b + 1 < len(Ak) else None
        j = bp(nxt) - b
        if (e, c) != (2, 4):
            assert j < 0 or (j == 0 and False), f"non-(2,4) event at k={k}: e={e} c={c} j={j}"
            continue   # erosion rows: not events
        # closure run of nxt from column b+1
        run = 0; col = b + 1
        while col < len(nxt) and nxt[col] in (0, 2): run += 1; col += 1
        # chain: consecutive unhalved diffs in {0,2} from column b+1, i.e. halved
        # diffs <= 1, starting at b+1 (intruder halved = 2).  j valid edges
        # corresponds to j+1 values in the chain.
        chainN = 1  # the intruder itself, halved value 2
        col = b + 1
        while col + 1 < len(Ak) and abs(int(Ak[col]) - int(Ak[col + 1])) in (0, 2):
            chainN += 1; col += 1
        L = chainN - 1
        ev.append((k, j, e, c, run, L, int(Ak[b + 2]) if b + 2 < len(Ak) else None))

    print(f"\nregeneration events (2,4)-rows with j>=0: {len(ev)}")
    print("checks: jump==closure-run  |  jump==chain-1  |  stall iff Ak[b+2]==0")
    fail_run = [x for x in ev if x[1] != x[4]]
    fail_chain = [x for x in ev if x[1] != x[5]]
    fail_stall = [x for x in ev if (x[1] == 0) != (x[6] == 0)]
    print(f"jump==closure-run : {'ALL PASS' if not fail_run else 'FAIL ' + str(fail_run[:3])}")
    print(f"jump==chain-1     : {'ALL PASS' if not fail_chain else 'FAIL ' + str(fail_chain[:3])}")
    print(f"stall iff Ak[b+2]==0: {'ALL PASS' if not fail_stall else 'FAIL ' + str(fail_stall[:3])}")

    jvals = [x[1] for x in ev]
    print(f"\njump values at events: min={min(jvals)} max={max(jvals)} "
          f"stalls={sum(1 for j in jvals if j==0)} positive={sum(1 for j in jvals if j>0)}")
    # what terminates a big chain? tabulate the (halved) value just past the chain
    print("\nk    j         run  b_k   A_k[b+2]   halved-past-chain")
    for (k, j, e, c, run, L, a2) in ev:
        Ak = rows[k]
        b = bp(Ak)
        col = b + 1
        while col + 1 < len(Ak) and abs(int(Ak[col]) - int(Ak[col + 1])) in (0, 2):
            col += 1
        past = int(Ak[col + 1]) if col + 1 < len(Ak) else None
        if j >= 1000 or j <= 1:
            print(f"{k:>3} {j:>9} {run:>9} {b:>8}   {str(a2):>4}      {str(past):>8}")
    # stats: chain termination marginal value histogram
    from collections import Counter
    cnt = Counter()
    for (k, j, e, c, run, L, a2) in ev:
        Ak = rows[k]; b = bp(Ak); col = b + 1
        while col + 1 < len(Ak) and abs(int(Ak[col]) - int(Ak[col + 1])) in (0, 2):
            col += 1
        past = int(Ak[col + 1]) if col + 1 < len(Ak) else None
        cnt[past] += 1
    print("\nhalved value past chain end, histogram:",
          dict(sorted(cnt.items(), key=lambda kv: (kv[0] is None, kv[0]))))
    print(f"elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()