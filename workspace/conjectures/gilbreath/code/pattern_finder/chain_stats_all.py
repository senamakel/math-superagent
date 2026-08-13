#!/usr/bin/env python3
"""Chain statistics for ALL (2,4)-events at width 3e8, depth 240 (streaming).

For each event (row k, block b, edge 2, intruder 4):
  L        = jump (chain length = #consecutive halved diffs <= 1 from col b+1)
  s0,sup,sdn = step counts (halved): 0-steps, +1 steps, -1 steps
  vmin,vmax  = range of halved values along the chain
  endpoint   = last halved value of the chain
  exit_gap   = |exit - endpoint| (halved), >= 2 by definition
  past       = halved value just past the chain end
Question: is amplitude <= 2 and/or s0 == sup+sdn universal over all events,
or a property only of the giants (L large)?
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
    idx = primes_idx(LIM)
    assert len(idx) == stored["num_primes"]
    primes = idx.astype(np.int64)
    cur = np.abs(np.diff(primes))
    rows_data = []
    for k in range(1, depth + 1):
        nxt = np.abs(np.diff(cur))
        b = bp(cur)
        if k <= 238:
            assert b == stored["b"][k-1], (k, b, stored["b"][k-1])
        if k < depth:
            e = int(cur[b]); c = int(cur[b+1]) if b+1 < len(cur) else None
            j = bp(nxt) - b
            if (e, c) == (2, 4):
                s0 = sup = sdn = 0
                col = b + 1
                vals = [int(cur[b+1])//2]
                while col + 1 < len(cur) and abs(int(cur[col]) - int(cur[col+1])) in (0, 2):
                    h  = int(cur[col])//2
                    hn = int(cur[col+1])//2
                    d = hn - h
                    s0 += (d == 0); sup += (d > 0); sdn += (d < 0)
                    vals.append(hn)
                    col += 1
                endpoint = vals[-1]
                past = int(cur[col+1])//2 if col+1 < len(cur) else None
                exit_gap = abs(past - endpoint) if past is not None else None
                rows_data.append((k, j, b, s0, sup, sdn, min(vals), max(vals),
                                  endpoint, exit_gap, past))
        del cur
        cur = nxt

    print(f"events: {len(rows_data)}")
    print("row    jump      b_k    s0      sup    sdn   vmin vmax end exit past | sup+sdn==s0 | vmax<=2")
    unbal = []
    amp_hi = []
    for (k, j, b, s0, sup, sdn, vmin, vmax, end, eg, past) in rows_data:
        bal = (sup + sdn == s0)
        amp2 = vmax <= 2
        if not bal: unbal.append((k, j, s0, sup, sdn))
        if not amp2: amp_hi.append((k, j, vmin, vmax))
        tag = ""
        if j >= 1000: tag = "  <== giant"
        print(f"{k:3d} {j:>7} {b:>10} {s0:>6} {sup:>6} {sdn:>6}  {vmin:>2}  {vmax:>2}  {end:>2} {str(eg):>3} {str(past):>3}   {bal}  {amp2}{tag}")

    print(f"\nnon-balanced (s0 != sup+sdn): {len(unbal)} -> {unbal[:10]}")
    print(f"amplitude > 2: {len(amp_hi)} -> {amp_hi[:10]}")
    # summary: balanced share among giants vs small
    giants = [r for r in rows_data if r[1] >= 1000]
    small  = [r for r in rows_data if 0 < r[1] < 1000]
    stalls = [r for r in rows_data if r[1] == 0]
    print(f"giants: {len(giants)}, balanced {sum(1 for r in giants if r[3]==r[4]+r[5])}, amp<=2 {sum(1 for r in giants if r[7]<=2)}")
    print(f"small : {len(small)}, balanced {sum(1 for r in small if r[3]==r[4]+r[5])}, amp<=2 {sum(1 for r in small if r[7]<=2)}")
    print(f"stalls: {len(stalls)}")
    # exit gap histogram
    from collections import Counter
    print("exit-gap (halved) histogram:", dict(sorted(Counter(r[9] for r in rows_data if r[9] is not None).items())))
    print("endpoint histogram:", dict(sorted(Counter(r[8] for r in rows_data).items())))
    print("vmax histogram:", dict(sorted(Counter(r[7] for r in rows_data).items())))
    print(f"elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
