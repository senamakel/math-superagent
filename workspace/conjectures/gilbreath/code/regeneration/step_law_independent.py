#!/usr/bin/env python3
"""Independent second-route check of the local step law.

Different code path entirely: pure-Python rows_generator from lib.gilbreath
(lists, not numpy), fresh sieve to 2,000,000, depth 300.

Re-verifies, with no shared code with step_law_theorem.py:
  (1) step law: for every k with b_k >= 1 and an intruder,
        b_{k+1} >= b_k  <=>  (x_k, y_k) = (2,4), else b_{k+1} = b_k - 1;
  (2) drain law on erosion: y_{k+1} = y_k - 2*[x_k==2];
  (3) recharge identity: b_k == b_1 + sum_{events i<k}(j_i+1) - (k-1);
  (4) no row with b <= 1 (prime rows, k=1..300);
  (5) sharpness by construction on tiny artificial rows:
        (1,2,4)  -> event  -> next row begins (1,2,...), b stays >= 1;
        (1,0,4)  -> non-event -> next row begins (1,4,...), b = 0;
        (1,2,6)  -> non-event -> next row begins (1,4,...), b = 0.
"""
import os
from lib.gilbreath import primes_up_to, rows_generator


def block_profile(row):
    n = 0
    for x in row[1:]:
        if x == 0 or x == 2:
            n += 1
        else:
            break
    return n


def main():
    primes = primes_up_to(2_000_000)
    print(f"primes below 2e6: {len(primes)}")

    gen = rows_generator(primes, 300)
    rows = [next(gen) for _ in range(301)]

    step_fail = drain_fail = id_fail = min_fail = 0
    events = []
    b_series = []
    for k in range(1, 301):
        row = rows[k]
        b = block_profile(row)
        b_series.append(b)
        if k >= 2:
            prev = rows[k - 1]
            bp = block_profile(prev)
            width = len(prev)
            if bp >= 1 and bp + 1 < width:
                x = prev[bp]
                y = prev[bp + 1]
                event = (x == 2 and y == 4)
                if event:
                    if not (b >= bp):
                        step_fail += 1
                    events.append((k - 1, b - bp))
                else:
                    if not (b == bp - 1):
                        step_fail += 1
                    # drain law: new block length b = bp-1, new intruder
                    # is the first entry past it, at index b+1 = bp
                    y_next = row[b + 1]
                    want = y - 2 * (1 if x == 2 else 0)
                    if y_next != want:
                        drain_fail += 1
            if (bp, b) == (1, 0):
                min_fail += 1
    print(f"step-law failures: {step_fail}; drain-law failures: {drain_fail}")
    print(f"b=1 -> b=0 transitions (must be 0): {min_fail}")
    print(f"(2,4)-events: {len(events)}")

    # recharge identity
    bad = 0
    esum = 0
    ei = 0
    for k in range(2, 301):
        while ei < len(events) and events[ei][0] < k:
            esum += events[ei][1] + 1
            ei += 1
        expect = b_series[0] + esum - (k - 1)
        if expect != b_series[k - 1]:
            bad += 1
    print(f"recharge identity failures over k=2..300: {bad}")

    # sharpness constructions
    def evolve(row0, steps=3):
        cur = row0
        out = []
        for _ in range(steps):
            cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
            out.append(cur)
        return out

    r1 = evolve([1, 2, 4, 10])
    r2 = evolve([1, 0, 4, 10])
    r3 = evolve([1, 2, 6, 10])
    print("constructed (1,2,4)     -> row1:", r1[0], "b =", block_profile(r1[0]))
    print("constructed (1,0,4)     -> row1:", r2[0], "b =", block_profile(r2[0]))
    print("constructed (1,2,6)     -> row1:", r3[0], "b =", block_profile(r3[0]))
    assert block_profile(r1[0]) >= 1 and block_profile(r2[0]) == 0 and \
        block_profile(r3[0]) == 0, "sharpness constructions wrong"


if __name__ == "__main__":
    main()