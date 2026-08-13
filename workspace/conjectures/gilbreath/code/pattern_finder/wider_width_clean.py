#!/usr/bin/env python3
"""Clean recomputation of the live-regime analysis at sieve 300M, ONE row at
a time, exact int64. Fixes the corrupted tail of wider_width_b.json (the
saved intruder/b arrays disagreed with a clean recomputation at row 238:
saved intruder 6, truth 4; saved b_239 16252085, truth 16252084).

Computes:
  b_k, s_k (second entry), intruder c_k, block-edge e_k/2, next-to-edge i_k/2
  events (b_{k+1} >= b_k), giants (jump > 1000), threshold gaps,
  all-time-max records, step-law verification over every live transition.
"""
from math import isqrt
import time
import json
import numpy as np

LIMIT = 300_000_000
DEPTH = 300
t0 = time.time()
sieve = bytearray(b"\x01") * (LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(LIMIT) + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((LIMIT - i * i) // i) + 1)
buf = np.frombuffer(sieve, dtype=np.uint8)
idx = np.nonzero(buf[2:])[0].astype(np.int64) + 2
del sieve, buf
P = int(len(idx))
print(f"primes: {P} ({time.time()-t0:.1f}s)", flush=True)


def block_len(row):
    arr = row[1:]
    bad = np.flatnonzero((arr != 0) & (arr != 2))
    return int(bad[0]) if bad.size else len(arr) - 1


b_list, s_list, intr, ebits, ibits = [], [], [], [], []
step_fail = 0
cur = idx
for k in range(1, DEPTH + 1):
    nxt = np.abs(np.diff(cur))
    arr = nxt
    bb = block_len(arr)
    live = bb + 1 <= len(arr) - 1
    c = int(arr[bb + 1]) if live else None
    e = int(arr[bb]) // 2 if bb <= len(arr) - 1 else None
    i = int(arr[bb - 1]) // 2
    n = len(nxt)
    if k > 1:
        prev_b = b_list[-1]
        pred = (bb >= prev_b) == (ebits[k - 2] == 1 and intr[k - 2] == 4)
        if not pred:
            step_fail += 1
            print(f"STEP-LAW FAIL at transition {k-1}->{k}")
    b_list.append(bb)
    s_list.append(int(nxt[1]))
    intr.append(c)
    ebits.append(e)
    ibits.append(i)
    cur = nxt
    if k % 60 == 0:
        print(f"row {k}: b={bb} intruder={c} ({time.time()-t0:.0f}s)", flush=True)
print(f"done ({time.time()-t0:.1f}s); step-law failures: {step_fail}", flush=True)

print(f"\nmax b: {max(b_list)}")
k_star = next((k for k in range(2, DEPTH + 1)
               if b_list[k - 1] + (k + 1) >= P), None)
print(f"k* (first row with no intruder): {k_star}")

# events on live transitions k-1->k (k<=k_star)
events = []
for k in range(2, min(DEPTH, (k_star or DEPTH)) + 1):
    d = b_list[k - 1] - b_list[k - 2]
    if d >= 0:
        events.append((k, d, b_list[k - 2]))
print(f"live events: {len(events)}  (jumps: {[e[1] for e in events]})")

giants = [e for e in events if e[1] > 1000]
print(f"\ngiants (jump>1000): {len(giants)}")
gro = [e[0] for e in giants]
print("giant rows:", gro)
if len(gro) >= 2:
    print("gaps:", [gro[i+1]-gro[i] for i in range(len(gro)-1)],
          "max:", max(gro[i+1]-gro[i] for i in range(len(gro)-1)))

print("\nthreshold gaps:")
for J in (100, 1000, 10000, 100000):
    rows = [e[0] for e in events if e[1] > J]
    gaps = [rows[i+1]-rows[i] for i in range(len(rows)-1)]
    print(f"  J={J:>6}: count {len(rows):2d} max-gap {max(gaps) if gaps else 'n/a'} rows {rows}")

recmax = 0
nrec = 0
for (k, j, bk) in events:
    land = bk + j
    if land > recmax:
        recmax = land
        nrec += 1
print(f"\nevents setting new all-time max: {nrec}/{len(events)}")
print("all giants set new max:", all(
    (bk + j) > max(events[:i], default=(0, 0, -1))[2] + max(
        (e[1] for e in events[:i]), default=0)
    for i, (_, j, bk) in enumerate(events) if j > 1000))

# second-entry check
print(f"all s in {{0,2}}: {all(x in (0, 2) for x in s_list)}")

out = {"limit": LIMIT, "num_primes": P, "depth": DEPTH, "k_star": k_star,
       "b": b_list, "s": s_list, "intruder": intr}
with open("code/out/wider_width_b_clean.json", "w") as f:
    json.dump(out, f)
print("wrote code/out/wider_width_b_clean.json")