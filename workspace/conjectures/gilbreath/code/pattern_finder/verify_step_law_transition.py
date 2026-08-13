#!/usr/bin/env python3
"""Verify the step law at the suspicious transition 238 -> 239
(recorded b: 10,655,260 -> 16,252,085), keeping ONE row at a time.

Step law: b_{k+1} >= b_k iff (e_k, c_k) = (2, 4), else b_{k+1} = b_k - 1,
where e_k = A_k[b_k] (last {0,2} block entry), c_k = A_k[b_k + 1] (intruder).
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
del sieve, buf
P = len(idx)
print(f"primes: {P} ({time.time()-t0:.1f}s)", flush=True)


def block_len(row):
    arr = row[1:]
    bad = np.flatnonzero((arr != 0) & (arr != 2))
    return int(bad[0]) if bad.size else len(arr) - 1


# keep rows 237 and 238; then 239, 240 on the fly
cur = idx
prev = None
for k in range(1, 239):          # produce rows 1..238
    nxt = np.abs(np.diff(cur))
    prev = cur
    cur = nxt
    if k % 60 == 0:
        print(f"row {k} len={len(cur)} ({time.time()-t0:.0f}s)", flush=True)
r237 = prev  # row 237
r238 = cur   # row 238
print(f"rows 237,238 computed len={len(r237)},{len(r238)} ({time.time()-t0:.1f}s)",
      flush=True)

bb = block_len(r238)
e = int(r238[bb])
c = int(r238[bb + 1])
print(f"\nb_238 = {bb}, e_238 = {e}, c_238 = {c}")

r239 = np.abs(np.diff(r238))
b239 = block_len(r239)
print(f"b_239 = {b239}")
print(f"A_239[{bb}] = {int(r239[bb])}  (|e-c| = {abs(e-c)})")
print(f"A_239[{bb+1}] = {int(r239[bb+1])}, A_239[{bb+2}] = {int(r239[bb+2])}")
print(f"step law: (b_239 >= b_238) iff (e,c)==(2,4): "
      f"{(b239 >= bb) == (e == 2 and c == 4)}")
print(f"recorded b_238, b_239 = 10655260, 16252085; recomputed: {bb}, {b239}",
      flush=True)

r240 = np.abs(np.diff(r239))
bb9 = block_len(r239)
e9 = int(r239[bb9])
c9 = int(r239[bb9 + 1]) if bb9 + 1 <= len(r239) - 1 else None
b240 = block_len(r240)
print(f"\nb_239 = {bb9}, e = {e9}, c = {c9}, b_240 = {b240}")
print(f"step law 239->240: {(b240 >= bb9) == (e9 == 2 and c9 == 4)}")
print(f"recorded b_240 = 16252084; recomputed: {b240}",
      flush=True)