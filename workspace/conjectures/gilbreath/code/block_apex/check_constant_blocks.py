#!/usr/bin/env python3
"""Empirical probe for the block-apex-parity-forcing approach.

Question: do the leading {0,2} blocks of the PRIME Gilbreath triangle ever
become constant (all-0 or all-2), beyond small size? And how long are the
terminal constant suffixes of each block (the object the boundary/x-value
mechanism actually depends on)?

Method: exact integer sieve to 20,000,000 (reproducing blocks_depth1000.json's
source), one row at a time, numpy vectorized. For each row k=1..D:
  b(k)   = length of leading {0,2} block
  s(k)   = A_k(1)
  y(k)   = intruder (first entry past the block; None if block reaches row end)
  whole  = 'const0' / 'const2' / 'mixed'  (block constant or not)
  tails  = length of the longest constant {0,2} suffix of the block
  runs0, runs2 = longest run of consecutive 0s / 2s anywhere in the block
For k <= 161 (the live regime, before width exhaustion) the full bit pattern is
stored in bits[k-1] as a bytes object (0x00/0x02 halved to 0/1).

Declared cost: O(sum over rows of row length) time = O(D*W/2) ~ 6e8 numpy ops,
O(max block) memory. Bound: timeout 540, D=1000, W=1,270,607.
"""
import json
import sys
import time

import numpy as np

from lib.gilbreath import primes_up_to

D = 1000
SIEVE = 20_000_000
LIVE = 161  # last live row (before width exhaustion) per regeneration_data.md


def main():
    t0 = time.time()
    primes = primes_up_to(SIEVE)
    print(f"sieve to {SIEVE}: {len(primes)} primes in {time.time()-t0:.1f}s",
          flush=True)

    cur = np.array(primes, dtype=np.int64)
    rec = {"D": D, "sieve": SIEVE, "rows": []}
    bits = []
    for k in range(1, D + 1):
        cur = np.abs(np.diff(cur))
        body = cur[1:]                     # positions 1..  (A_k(1..))
        # first index in body not in {0,2}
        bad = np.flatnonzero((body != 0) & (body != 2))
        if bad.size == 0:
            b = int(body.size)
            y = None
        else:
            b = int(bad[0])
            y = int(body[b]) if b < body.size else None
        block = body[:b] if b > 0 else np.array([], dtype=np.int64)
        s = int(cur[0])
        if b == 0:
            whole = "empty"
            tail = 0
            r0 = r2 = 0
        else:
            first = int(block[0])
            whole = "const2" if first == 2 else "const0"
            if np.any(block != first):
                whole = "mixed"
            # terminal constant run length
            tail = 1
            for j in range(b - 2, -1, -1):
                if block[j] == block[b - 1]:
                    tail += 1
                else:
                    break
            # longest run of 0s / 2s
            r0 = r2 = 0
            run = 1
            for j in range(1, b):
                if block[j] == block[j - 1]:
                    run += 1
                else:
                    if block[j - 1] == 0:
                        r0 = max(r0, run)
                    else:
                        r2 = max(r2, run)
                    run = 1
            if block[b - 1] == 0:
                r0 = max(r0, run)
            else:
                r2 = max(r2, run)
        rec["rows"].append({
            "k": k, "b": b, "s": s, "y": y,
            "whole": whole, "tail": tail, "r0": r0, "r2": r2,
        })
        if k <= LIVE and b > 0:
            bits.append(bytes(int(v // 2) for v in block))
        elif k <= LIVE:
            bits.append(b"")
        if k % 50 == 0:
            print(f"row {k}: b={b} whole={whole} tail={tail} "
                  f"({time.time()-t0:.1f}s)", flush=True)

    stats = {
        "const_rows": [r["k"] for r in rec["rows"] if r["whole"] == "const0"],
        "const_rows_2": [r["k"] for r in rec["rows"] if r["whole"] == "const2"],
        "min_b": min(r["b"] for r in rec["rows"]),
        "max_b": max(r["b"] for r in rec["rows"]),
        "max_tail": max(r["tail"] for r in rec["rows"]),
        "max_tail_k": max(rec["rows"], key=lambda r: r["tail"])["k"],
        "max_r0": max(r["r0"] for r in rec["rows"]),
        "max_r2": max(r["r2"] for r in rec["rows"]),
        "live": LIVE,
    }
    rec["stats"] = stats
    rec.pop("rows")  # keep the JSON small; rows are printed below instead

    # live-regime verdict lines
    live = [r for r in rec["rows"]]  # rows were popped; recompute from local
    live = [{"k": r["k"], "b": r["b"], "whole": r["whole"], "tail": r["tail"],
             "r0": r["r0"], "r2": r["r2"]} for r in live]
    out_path = "code/out/block_constancy.json"
    with open(out_path, "w") as f:
        json.dump({"stats": stats, "live_rows": live}, f)

    print("\nSTATS:", json.dumps(stats, indent=1))
    print("\nLive-regime rows with whole-block constant:")
    for r in live:
        if r["whole"] != "mixed":
            print("  ", r)
    print("\nLive-regime rows with terminal constant suffix >= 3:")
    for r in live:
        if r["tail"] >= 3:
            print("  ", r)
    print("\nLongest terminal suffixes (top 15 live rows):")
    for r in sorted(live, key=lambda r: -r["tail"])[:15]:
        print("  ", r)
    print(f"\nwrote {out_path}; total {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()