#!/usr/bin/env python3
"""The local step law of the leading {0,2} block — exact derivation support.

THEOREM (valid for ANY absolute-difference array; no parity, no primes):
  Let A_{k+1}(j) = |A_k(j) - A_k(j+1)| with nonnegative integer entries,
  b_k = length of the leading {0,2} block of A_k (positions 1..b_k in
  {0,2}, maximal), and suppose A_k has an intruder y_k = A_k(b_k+1)
  (finite row; block does not reach the row end).  Define the edge
  x_k = A_k(b_k) in {0,2} (needs b_k >= 1).  Then

     b_{k+1} >= b_k   <=>   (x_k, y_k) = (2, 4),
     b_{k+1}  = b_k - 1  otherwise            (so b_{k+1} >= b_k - 1 always).

  Proof: positions 1..b_k-1 of row k+1 are |{0,2} - {0,2}| subset {0,2}
  (that closure is the only arithmetic used).  Position b_k of row k+1 is
  |x_k - y_k|.  Hence b_{k+1} >= b_k  <=>  |x_k - y_k| in {0,2}.  With
  x_k in {0,2} and y_k notin {0,2}:  x=0 gives |0-y| = y notin {0,2}
  (as y notin {0,2});  x=2 gives |2-y| in {0,2} <=> y in {0,2,4}, and by
  maximality y=4.  So the iff holds; and since nothing can make
  b_{k+1} < b_k - 1, the complementary case is exactly b_{k+1} = b_k - 1.

  DRAIN LAW: on an erosion step b_{k+1} = b_k - 1, the new intruder is
  y_{k+1} = A_{k+1}(b_{k+1}+1) = A_{k+1}(b_k) = |x_k - y_k| = y_k - 2*[x_k==2]
  (y_{k+1} >= 4 whenever y_k >= 4: monotone non-increasing during erosion).

  RECHARGE IDENTITY: for every k, with events = rows i < k at (x,y)=(2,4)
  and j_i = b_{i+1} - b_i >= 0 at events:  b_k = b_1 + sum_events (j_i+1) - k + 1.
  So for a parity-shape array (rows >= 1 even after position 0, e.g. the
  primes), Gilbreath's conjecture (b_k >= 1 for all k) is equivalent to
     sum_{events i < k} (j_i + 1) >= k - b_1   for all k.
  (For the primes b_1 = 2, so the buffer must be recharged by at least
  k - 2 over the first k-1 rows; each (2,4)-event contributes j_i + 1 >= 1.)

Checks executed here (exact, oracle-checked):
  1. Real prime rows, sieve 2e7 (1,270,607 primes), depth 1000:
     step law over all 998 transitions (with and without intruder),
     drain law over the 101 erosion steps with an intruder,
     recharge identity at every k=2..1000.
  2. General-class brute force: 400 random nonnegative-integer arrays
     (200 "even-shape" and 200 completely arbitrary), depth 40:
     step law must hold at every row with b_k >= 1 and an intruder.
     No primes, no parity used.
"""
import json
import random
import time

import numpy as np

D = 1000
LIMIT = 20_000_000


def block_profile(row):
    n = 0
    for x in row[1:]:
        if x == 0 or x == 2:
            n += 1
        else:
            break
    return n


def check_step_law(b, b_next, row, width):
    """Return (ok, kind) for one transition, or None if no intruder."""
    if b == 0:
        return None  # hypothesis of the theorem; primes have b >= 2
    if b + 1 >= width:
        # no intruder: law is b_next == b - 1 (truncation)
        return (b_next == b - 1, "no-intruder")
    x = int(row[b])
    y = int(row[b + 1])
    event = (x == 2 and y == 4)
    if event:
        return (b_next >= b, "event")
    return (b_next == b - 1, "non-event")


def main():
    t0 = time.time()
    # ---------------- 1. real prime rows ----------------
    sieve = bytearray(b"\x01") * LIMIT
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i < LIMIT:
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((LIMIT - 1 - i * i) // i) + 1)
        i += 1
    primes = np.nonzero(np.frombuffer(sieve, dtype=np.uint8))[0].astype(np.int64)
    print(f"sieve: {len(primes)} primes below {LIMIT} in {time.time()-t0:.1f}s")

    with open("code/out/witnesses.json") as f:
        wit = json.load(f)
    prof = wit["block_profile_first_40"]
    want_b = [e["block"] for e in prof]
    want_s = [e["second"] for e in prof]

    prev_row = primes.copy()
    prev_b = None
    step_fail = []
    drain_fail = []
    drain_ok = 0
    events = []          # (k, jump)
    b_series = []
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
        if k > 1:
            width = len(prev_row)
            res = check_step_law(prev_b, blk, prev_row, width)
            if res is None:
                step_fail.append((k, "b_k=0", prev_b, blk))
            elif not res[0]:
                step_fail.append((k, res[1], prev_b, blk))
            # drain law on erosion steps with an intruder
            if blk == prev_b - 1 and prev_b + 1 < width:
                x = int(prev_row[prev_b])
                y = int(prev_row[prev_b + 1])
                y_pred = abs(x - y)
                y_next = int(row[blk + 1]) if blk + 1 < len(row) else None
                if y_next is not None and y_next == y_pred:
                    drain_ok += 1
                else:
                    drain_fail.append((k, x, y, y_pred, y_next))
            if blk >= prev_b and prev_b + 1 < width:
                x = int(prev_row[prev_b]); y = int(prev_row[prev_b + 1])
                if (x, y) == (2, 4):
                    events.append((k - 1, blk - prev_b))
        b_series.append(blk)
        prev_row = row
        prev_b = blk
    t_rows = time.time()
    assert b_series[:40] == want_b, "oracle mismatch block lengths"
    print(f"rows to depth {len(b_series)} in {t_rows-t1:.1f}s; oracle k=1..40 ok")

    print("\n=== 1. real prime rows, depth 1000 ===")
    print(f"step-law failures over 999 transitions: {len(step_fail)}"
          + (f"  first: {step_fail[:3]}" if step_fail else ""))
    print(f"drain-law ok on erosion steps with intruder: {drain_ok}/101;"
          f" failures: {len(drain_fail)}" + (f" {drain_fail[:3]}" if drain_fail else ""))
    print(f"(2,4)-events in k=1..999: {len(events)} (expect 60)")

    # recharge identity: b_k == b_1 + sum_{events<k}(j+1) - (k-1)
    bad = 0
    esum = 0
    ei = 0
    for k in range(2, D + 1):
        while ei < len(events) and events[ei][0] < k:
            esum += events[ei][1] + 1
            ei += 1
        expect = b_series[0] + esum - (k - 1)
        if expect != b_series[k - 1]:
            bad += 1
            if bad <= 3:
                print(f"  recharge mismatch k={k}: b={b_series[k-1]} expect {expect}")
    print(f"recharge identity b_k = b_1 + sum_events(j+1) - (k-1): "
          f"failures {bad} over k=2..1000")
    total_recharge = sum(j + 1 for _, j in events)
    print(f"total recharge over events: {total_recharge}; k - b_1 at k=1000: "
          f"{D - b_series[0]}; surplus {total_recharge - (D - b_series[0])}")

    # ---------------- 2. general-class brute force ----------------
    print("\n=== 2. general-class brute force (random arrays, no primes) ===")
    rng = random.Random(20260712)
    total_rows = 0
    gfail = 0
    gevents = 0
    for trial in range(400):
        w = rng.randint(5, 60)
        if trial < 200:
            # even-shape starting row: [1] + evens
            row0 = [1] + [2 * rng.randint(0, 15) for _ in range(w - 1)]
        else:
            # completely arbitrary nonnegative entries
            row0 = [rng.randint(0, 30) for _ in range(w)]
        cur = row0
        for _ in range(40):
            nxt = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
            b = block_profile(cur)
            b_n = block_profile(nxt)
            if b >= 1 and b + 1 < len(cur):
                total_rows += 1
                x = cur[b]; y = cur[b + 1]
                event = (x == 2 and y == 4)
                if event:
                    gevents += 1
                    if not (b_n >= b):
                        gfail += 1
                else:
                    if not (b_n == b - 1):
                        gfail += 1
            cur = nxt
    print(f"rows checked (b>=1, intruder exists): {total_rows}; "
          f"(2,4)-events: {gevents}; step-law failures: {gfail}")


if __name__ == "__main__":
    main()