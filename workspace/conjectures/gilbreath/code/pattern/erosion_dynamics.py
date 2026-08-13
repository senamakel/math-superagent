#!/usr/bin/env python3
"""Verify the erosion-track dynamics exactly, over every erosion row.

Setup: b(k) = length of the leading {0,2} block of A_k (positions 1..b after
A_k(0)=1), x(k) = A_k(b(k)) = last block entry, y(k) = A_k(b(k)+1) = first
entry past the block ('intruder', even, >= 4) when one exists in width.

During an erosion step (b(k+1) == b(k)-1), with p(k)=A_k(b(k)-1) in {0,2}:
   x(k+1) = |p(k) - x(k)|
   y(k+1) = |x(k) - y(k)| = y(k) - 2*[x(k)==2]     (y even, stays >= 4)
i.e. each x==2 inside the block decrements the intruder by 2; x==0 leaves y.
Regeneration (b(k+1) >= b(k)) happens iff x(k)==2 AND y(k)==4.

Indices: row A_k is 0-based numpy; A_k(0)=1, block = row[1..b(k)],
x(k)=row[b(k)], y(k)=row[b(k)+1], p(k)=row[b(k)-1].
Erosion: b(k+1)=b-1, so x(k+1)=row_{k+1}[b-1], y(k+1)=row_{k+1}[b].

The check: for every erosion step k-1 -> k in the computed window, compare
predicted (x(k),y(k)) from row_{k-1} against actual. Also confirm the regen
trigger condition over every row (boundary lemma, second check here).
Oracle on k=1..40. Holds two consecutive rows: O(W) memory.
"""
import json
import time

import numpy as np

D = 1000
LIMIT = 20_000_000


def main():
    t0 = time.time()
    sieve = bytearray(b"\x01") * LIMIT
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i < LIMIT:
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((LIMIT - 1 - i * i) // i) + 1)
        i += 1
    primes = np.nonzero(np.frombuffer(sieve, dtype=np.uint8))[0].astype(np.int64)
    print(f"sieve {len(primes)} primes in {time.time() - t0:.1f}s")

    with open("code/out/witnesses.json") as f:
        wit = json.load(f)
    prof = wit["block_profile_first_40"]
    want_b = [e["block"] for e in prof]
    want_s = [e["second"] for e in prof]

    prev_row = primes.copy()
    prev_b = None
    b_list, s_list = [], []
    erosion_steps = 0
    x_pred_ok = y_pred_ok = 0
    fails = []
    regen_rows = regen_ok = 0
    intruders = []
    t1 = time.time()
    for k in range(1, D + 1):
        row = np.abs(prev_row[:-1] - prev_row[1:])
        sel = row[1:]
        in02 = (sel == 0) | (sel == 2)
        if bool(in02.all()):
            blk = len(sel)
            intr = None
        else:
            blk = int(np.argmax(~in02))
            intr = int(sel[blk])
        intruders.append(intr)
        if k > 1:
            d = blk - prev_b
            if d == -1 and prev_b + 1 < len(prev_row):
                # erosion step k-1 -> k, with an intruder visible at k-1
                erosion_steps += 1
                p = int(prev_row[prev_b - 1])    # A_{k-1}(b-1)
                x = int(prev_row[prev_b])        # A_{k-1}(b)
                y = int(prev_row[prev_b + 1])    # A_{k-1}(b+1)
                x_pred = abs(p - x)
                y_pred = abs(x - y)
                x_act = int(row[prev_b - 1])     # A_k(b-1): x(k)
                y_act = int(row[prev_b])         # A_k(b): y(k)
                if x_pred == x_act and y_pred == y_act and y_act >= 4:
                    x_pred_ok += 1
                    y_pred_ok += 1
                else:
                    fails.append((k, p, x, y, x_pred, y_pred, x_act, y_act))
            # regen trigger at row k-1: b changes from prev_b to blk
            if d >= 0:
                regen_rows += 1
                if prev_b + 1 < len(prev_row):
                    x = int(prev_row[prev_b])
                    y = int(prev_row[prev_b + 1])
                    if x == 2 and y == 4:
                        regen_ok += 1
        b_list.append(blk)
        s_list.append(int(row[1]))
        prev_row = row
        prev_b = blk
    t_rows = time.time()
    assert b_list[:40] == want_b and s_list[:40] == want_s, "oracle mismatch"
    print(f"rows to depth {len(b_list)} in {t_rows - t1:.1f}s; oracle ok k=1..40")
    print(f"erosion steps checked: {erosion_steps}; track predictions correct: "
          f"{x_pred_ok}/{erosion_steps}")
    if fails:
        print(f"FAILURES {len(fails)}: first 5 = {fails[:5]}")
    print(f"regen rows: {regen_rows}; with (x==2,y==4) trigger visible: {regen_ok}")
    intr = [i for i in intruders if i is not None]
    print(f"intruder y(k) over k with visible intruder: min {min(intr)}, "
          f"max {max(intr)}, n={len(intr)}")
    from collections import Counter
    print("intruder value counts:", sorted(Counter(intr).items()))


if __name__ == "__main__":
    main()