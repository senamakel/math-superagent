#!/usr/bin/env python3
"""Recompute rows 235..240 at sieve 300M and verify the step law at the
suspicious transition 238 -> 239 (recorded b: 10,655,260 -> 16,252,085).

Step law says: b_{k+1} >= b_k iff (e_k, c_k) = (2, 4), else b_{k+1} = b_k - 1,
where e_k = A_k[b_k] (last {0,2} block entry) and c_k = A_k[b_k + 1] (intruder).
Check it exactly here, entry by entry.
"""
from math import isqrt
import time
import numpy as np

LIMIT = 300_000_000
t0 = time.time()
sieve = bytearray(b"\x01") * (LIMIT + 1)
sieve[0] = sieve[1] = 0
for i in range(2, isqrt(LIMIT) + 1):
    if sieve[i]:
        sieve[i * i::i] = b"\x00" * (((LIMIT - i * i) // i) + 1)
buf = np.frombuffer(sieve, dtype=np.uint8)
idx = np.nonzero(buf[2:])[0].astype(np.int64) + 2
P = len(idx)
print(f"primes: {P} ({time.time()-t0:.1f}s)", flush=True)

rows = [idx]
cur = idx
for k in range(1, 241):
    cur = np.abs(np.diff(cur))
    rows.append(cur)
print(f"rows computed ({time.time()-t0:.1f}s)", flush=True)


def block_len(row):
    arr = row[1:]
    bad = np.flatnonzero((arr != 0) & (arr != 2))
    return int(bad[0]) if bad.size else len(arr) - 1


last = len(rows[-1])
print(f"row 241 len = {last}")
for k in range(235, 241):
    r = rows[k]
    bb = block_len(r)
    intr = int(r[bb + 1]) if bb + 1 <= len(r) - 1 else None
    print(f"row {k}: len={len(r)} b={bb} intruder={intr} "
          f"e={int(r[bb]) if bb <= len(r)-1 else '-'} "
          f"pos{b_238_plus1 if False else ''}", flush=True)

print("\n-- step-law check at transition 238 -> 239 --")
r238 = rows[238]
bb = block_len(r238)
e = int(r238[bb])
c = int(r238[bb + 1])
r239 = rows[239]
print(f"b_238 = {bb}, e_238 = {e}, c_238 = {c}")
print(f"A_239 position {bb} = |e - c| = {abs(e - c)}  (value in row 239 at that pos: {int(r239[bb])})")
print(f"A_239 position {bb+1} = {int(r239[bb+1])}")
b239 = block_len(r239)
print(f"b_239 = {b239}")
print(f"step law (b_239 >= b_238) iff (e,c)==(2,4): "
      f"{(b239 >= bb) == (e == 2 and c == 4)}")

print("\n-- also check 239 -> 240 --")
r239b = rows[239]
bb9 = block_len(r239b)
e9 = int(r239b[bb9])
c9 = int(r239b[bb9 + 1]) if bb9 + 1 <= len(r239b) - 1 else None
r240 = rows[240]
b240 = block_len(r240)
print(f"b_239 = {bb9}, e = {e9}, c = {c9}, b_240 = {b240}")
print(f"step law: {(b240 >= bb9) == (e9 == 2 and c9 == 4)}")

# also recompute the transition 238->239 from the saved b list
import json
rec = json.load(open("code/out/wider_width_b.json"))
b = rec["b"]
print("\nsaved b values: b[237] = b_238 =", b[237], " b[238] = b_239 =", b[238])
print("recomputed:      b_238 =", bb, " b_239 =", b239)