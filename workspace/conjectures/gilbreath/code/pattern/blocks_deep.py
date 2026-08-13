#!/usr/bin/env python3
"""Exact block-length and second-entry sequences of the Gilbreath
absolute-difference rows of the primes, one row at a time, to depth D.

Oracle check: rows k=1..40 must reproduce witnesses.json exactly (block
lengths b and second entries s); the program refuses to extend past a
mismatch. The generator here is independent of the witness generator: fresh
sieve, fresh row code, numpy int64 rows.

Rows: A_{k+1} = |diff(A_k)|, vectorized over the whole row; row k has
W - k entries where W = number of primes below LIMIT. Entries are differences
of primes < LIMIT so int64 is exact. No floats anywhere.

Cost: O(D*W) vectorized element ops, memory O(W).
A_k(0) is asserted == 1 at every row (parity theorem: leading entry is odd and
in fact 1 while the second entry is even; this catches any broken row
arithmetic).
A_k(1) in {0,2} failing would print a loud FAIL -- that is Gilbreath's
conjecture falsified at that row.

Saves code/out/blocks_depth<D>.json with b, s, the "intruder" value (the first
entry after the leading {0,2} block, row[b+1]), and summary stats.
"""
import json
import sys
import time

import numpy as np

D = 1000
LIMIT = 20_000_000
OUT = f"code/out/blocks_depth{D}.json"


def main():
    t0 = time.time()
    sieve = bytearray(b"\x01") * LIMIT
    sieve[0:2] = b"\x00\x00"
    i = 2
    while i * i < LIMIT:
        if sieve[i]:
            sieve[i * i::i] = b"\x00" * (((LIMIT - 1 - i * i) // i) + 1)
        i += 1
    arr = np.frombuffer(sieve, dtype=np.uint8)
    primes = np.nonzero(arr)[0].astype(np.int64)
    t_sieve = time.time()
    print(f"sieve: {len(primes)} primes below {LIMIT} in {t_sieve - t0:.1f}s")

    with open("code/out/witnesses.json") as f:
        wit = json.load(f)
    prof = wit["block_profile_first_40"]
    want_b = [e["block"] for e in prof]
    want_s = [e["second"] for e in prof]

    row = primes
    b_list, s_list, intruder = [], [], []
    bad = None
    t1 = time.time()
    for k in range(1, D + 1):
        row = np.abs(row[:-1] - row[1:])
        if int(row[0]) != 1:
            bad = (f"leading entry != 1 at k={k}", k)
            break
        s = int(row[1])
        sel = row[1:]
        in02 = (sel == 0) | (sel == 2)
        if bool(in02.all()):
            blk = int(len(sel))  # block reaches end of row; flag below via intruder=None
        else:
            blk = int(np.argmax(~in02))
        b_list.append(blk)
        s_list.append(s)
        if blk + 1 < len(row):
            intruder.append(int(row[blk + 1]))
        else:
            intruder.append(None)
        if s not in (0, 2):
            bad = (f"A_k(1) = {s} not in {{0,2}} at k={k} -- CONJECTURE FALSIFIED", k)
            break
    t_rows = time.time()
    print(f"rows to depth {len(b_list)} in {t_rows - t1:.1f}s; first_bad={bad}")

    agree = (b_list[:40] == want_b) and (s_list[:40] == want_s)
    print(f"oracle agree on k=1..40 (block lengths and second entries): {agree}")
    if not agree:
        for kk in range(40):
            if b_list[kk] != want_b[kk] or s_list[kk] != want_s[kk]:
                print(f"  mismatch k={kk+1}: got b={b_list[kk]} s={s_list[kk]}, "
                      f"want b={want_b[kk]} s={want_s[kk]}")
        sys.exit(1)

    b = b_list
    s = s_list
    diffs = [b[i + 1] - b[i] for i in range(len(b) - 1)]
    assert min(diffs) >= -1, "violates {0,2} closure theorem b(k+1) >= b(k)-1"
    minb, maxb = min(b), max(b)
    print(f"min b = {minb} at k={b.index(minb) + 1}; max b = {maxb} at k={b.index(maxb) + 1}")
    print(f"block diffs: min={min(diffs)} max={max(diffs)}")
    regen = [(i + 1, d) for i, d in enumerate(diffs) if d >= 0]
    print(f"regeneration rows (diff >= 0): {len(regen)} of {len(diffs)}; "
          f"max jump {max(diffs)} at k={diffs.index(max(diffs)) + 1}")
    er = best_er = 0
    for d in diffs:
        if d == -1:
            er += 1
            best_er = max(best_er, er)
        else:
            er = 0
    print(f"longest pure-erosion run (consecutive b(k+1)=b(k)-1): {best_er}")

    zeros = sum(1 for x in s if x == 0)
    print(f"s: {zeros} zeros and {len(s) - zeros} twos over k=1..{len(s)}")
    runs = []
    cur, clen = s[0], 1
    for x in s[1:]:
        if x == cur:
            clen += 1
        else:
            runs.append((cur, clen))
            cur, clen = x, 1
    runs.append((cur, clen))
    print("longest runs in s:", sorted(runs, key=lambda t: -t[1])[:5])

    intr = [x for x in intruder if x is not None]
    if intr:
        mod4 = {}
        for x in intr:
            m = x % 4
            mod4[m] = mod4.get(m, 0) + 1
        print(f"intruder (value just past the block): min {min(intr)}, "
              f"max {max(intr)}, share==4: {sum(1 for x in intr if x == 4) / len(intr):.3f}")
        print("intruder counts mod 4:", sorted(mod4.items()))
        print("first 40 intruders:", [int(x) for x in intr[:40]])
    else:
        print("no intruders recorded")

    out = {
        "D": len(b), "sieve_limit": LIMIT, "num_primes": int(len(primes)),
        "first_bad": bad, "oracle_agree_first_40": bool(agree),
        "b": b, "s": s,
        "intruder": [None if x is None else int(x) for x in intruder],
        "min_block": minb, "max_block": maxb,
    }
    with open(OUT, "w") as f:
        json.dump(out, f)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()