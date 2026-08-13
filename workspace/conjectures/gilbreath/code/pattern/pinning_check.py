#!/usr/bin/env python3
"""Test the pinning conjecture: if at row k there is a visible intruder y(k)
(the block is not full-width), so the erosion track is forced by the last two
block entries and the intruder, then the block regenerates within finitely
many rows -- and check the in-window bound.

Vulnerable case: erosion run starting at small b with large y. Each erosion
step consumes one row; x==2 steps drop y by 2. So regen is delayed by
(roughly) the number of rows until the (y/2 - 1)-th x==2 occurrence... but a
run might also just die (b hits 1) before y reaches 4. This script checks:
given the exact rows, for every row k with a visible intruder, whether regen
occurs before b would hit 1, and records the max y-and-small-b combination
that is "dangerous".

The FULL question -- regeneration always beats consumption -- can only ever be
verified on the finite window, so this script reports the in-window floor of
b and the worst y at each small b. That is the honest bound.
"""
import json

import numpy as np

D = 1000
LIMIT = 20_000_000


def main():
    sieve = bytearray(b"\x01") * LIMIT
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i < LIMIT:
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((LIMIT - 1 - i * i) // i) + 1)
        i += 1
    primes = np.nonzero(np.frombuffer(sieve, dtype=np.uint8))[0].astype(np.int64)

    with open("code/out/witnesses.json") as f:
        wit = json.load(f)
    prof = wit["block_profile_first_40"]
    want_b = [e["block"] for e in prof]
    want_s = [e["second"] for e in prof]

    prev_row = primes.copy()
    rows = [primes]  # keep all rows: memory ~ sum(W-k) = D*W/2 int64 ~ 5GB -- NO
    # Don't store all rows; instead store per-row (b, x, y) only.
    raise SystemExit("avoid storing all rows; rewrite per-row stats only")


if __name__ == "__main__":
    main()