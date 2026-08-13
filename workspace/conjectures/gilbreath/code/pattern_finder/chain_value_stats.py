#!/usr/bin/env python3
"""Chain-value statistics for the 15 giants at width 3e8 (streaming, depth 240).

At each (2,4)-event the jump = length of the initial 1-Lipschitz chain of the
halved row past the block (smooth-run law, verified 74/74).  Question: are the
giant chains long FLAT stretches (mostly 0-steps, few ±1) or long WANDERING
chains (many ±1)?  Compute for each giant:
  L        = chain length (jump)
  steps0   = number of 0-steps (halved diff == 0)
  steps1   = number of +-1 steps (halved diff == 1)
  vmin,vmax= min/max halved value along the chain (excludes the intruder=2 start)
  A        = amplitude (vmax - vmin)
A random 1-Lipschitz walk confined to amplitude A survives ~A^2 steps; a chain
of 4.3M steps with tiny amplitude must be almost entirely 0-steps.
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
    stats = []
    for k in range(1, depth + 1):
        nxt = np.abs(np.diff(cur))
        b = bp(cur)
        if k <= 238:
            assert b == stored["b"][k-1], (k, b, stored["b"][k-1])
        if k < depth:
            e = int(cur[b]); c = int(cur[b+1]) if b+1 < len(cur) else None
            j = bp(nxt) - b
            if (e, c) == (2, 4) and j >= 1000:
                # walk the 1-Lipschitz chain, halved values
                col = b + 1
                steps0 = steps1 = 0
                vals = []
                while col + 1 < len(cur) and abs(int(cur[col]) - int(cur[col+1])) in (0, 2):
                    h = int(cur[col]) // 2
                    hn = int(cur[col+1]) // 2
                    d = abs(hn - h)
                    steps0 += (d == 0); steps1 += (d == 1)
                    vals.append(h)
                    col += 1
                # chain length L = j; vals has L values (intruder at col=b+1 included
                # only if the chain advanced at least once; L = j)
                vmin = min(vals) if vals else None
                vmax = max(vals) if vals else None
                past = int(cur[col+1])//2 if col+1 < len(cur) else None
                stats.append((k, j, b, steps0, steps1, vmin, vmax, past))
        del cur
        cur = nxt
    print(f"giants: {len(stats)}")
    print("row     jump      b_k    steps0   steps1  vmin vmax past amp  frac1")
    for (k, j, b, s0, s1, vmin, vmax, past) in stats:
        amp = (vmax - vmin) if vmin is not None else None
        print(f"{k:3d} {j:>9} {b:>10} {s0:>8} {s1:>7} {str(vmin):>4} {str(vmax):>4} "
              f"{str(past):>4} {str(amp):>4} {s1/j:.6f}")
    print(f"elapsed {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
