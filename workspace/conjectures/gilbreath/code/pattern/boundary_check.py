#!/usr/bin/env python3
"""Verify two exact structural claims about the Gilbreath block-length
sequence b(k) (leading {0,2} run of row A_k, counting entries after A_k(0)),
using the run's own exact row generator. Oracle: matches witnesses.json on
k=1..40, else refuses to extend.

Claim 1 (boundary lemma; elementary proof, here checked numerically):
b(k+1) - b(k) == -1  iff  NOT (x_last(k) == 2 AND y(k) == 4)
where x_last(k) = A_k(b(k)) is the last entry of the leading {0,2} block and
y(k) = A_k(b(k)+1) is the first entry past it (the 'intruder'), defined when
an intruder exists inside the computed width. Equivalently: the block
regenerates (b(k+1) >= b(k)) iff the block ends in 2 right before a 4.
Proof sketch: A_{k+1}(b(k)) = |x_last - y|; positions before that are {0,2}.
This is 2 iff (x_last,y) = (2,4) (y even, y >= 4 by definition of intruder),
and the block extends iff that entry is in {0,2}.

Claim 2 (full-computed-width absorption, window-only): let Kabs be the first k
with the block covering the entire visible row (b(k) == W - k - 1). For every
k in [Kabs, D], b(k) == W - k - 1 exactly (erosion by 1 = row shrinking). This
IS NOT an infinite-row claim: positions beyond the computed width are unknown.

Also records: s(k) = A_k(1), x_last(k), y(k), regen events, erosion runs.
"""
import json
import time

import numpy as np

D = 1000
LIMIT = 20_000_000
OUT = "code/out/boundary_check.json"


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
    W = len(primes)
    print(f"W = {W} primes below {LIMIT}")

    with open("code/out/witnesses.json") as f:
        wit = json.load(f)
    prof = wit["block_profile_first_40"]
    want_b = [e["block"] for e in prof]
    want_s = [e["second"] for e in prof]

    row = primes
    b_list, s_list = [], []
    x_last, y_list = [], []  # last block entry; intruder (None if none in width)
    Kabs = None
    t1 = time.time()
    for k in range(1, D + 1):
        row = np.abs(row[:-1] - row[1:])
        assert int(row[0]) == 1
        s = int(row[1])
        sel = row[1:]
        in02 = (sel == 0) | (sel == 2)
        if bool(in02.all()):
            blk = len(sel)
            xl = int(sel[-1])
            intr = None
        else:
            blk = int(np.argmax(~in02))
            xl = int(sel[blk - 1])
            intr = int(sel[blk])
        b_list.append(blk)
        s_list.append(s)
        x_last.append(xl)
        y_list.append(intr)
        if intr is None and Kabs is None:
            Kabs = k
    t_rows = time.time()
    print(f"rows to depth {D} in {t_rows - t1:.1f}s; Kabs (block covers full view) = {Kabs}")
    print(f"oracle agree k=1..40: {b_list[:40] == want_b and s_list[:40] == want_s}")
    assert b_list[:40] == want_b and s_list[:40] == want_s

    # -- Claim 2: tail linearity after Kabs, exactly over every term
    if Kabs is not None:
        tail_ok = all(b_list[k - 1] == W - k - 1 for k in range(Kabs, D + 1))
        first_tail = [(k, b_list[k - 1], W - k - 1)
                      for k in range(Kabs, min(Kabs + 3, D + 1))]
        print(f"tail linearity b(k) == W-k-1 exact for k = {Kabs}..{D}: {tail_ok}")
        print(f"  first tail terms: {first_tail}")
    else:
        tail_ok = False
        print("no full-width absorption within depth D")

    # -- Claim 1: boundary lemma over every k with an intruder in width
    lem_fail = []
    regen_pred, regen_obs = [], []
    for k in range(1, D):
        if y_list[k - 1] is not None:
            d = b_list[k] - b_list[k - 1]  # b(k+1) - b(k), 1-indexed
            pred_regen = (x_last[k - 1] == 2 and y_list[k - 1] == 4)
            obs_regen = d >= 0
            if pred_regen != obs_regen:
                lem_fail.append((k, d, x_last[k - 1], y_list[k - 1]))
            regen_pred.append(pred_regen)
            regen_obs.append(obs_regen)
    print(f"boundary lemma: {D - 1 - len(lem_fail)} of {D - 1} eligible rows agree"
          f" (rows with an intruder in width); failures: {lem_fail[:5]}")
    print(f"  regen predicted: {sum(regen_pred)}, observed: {sum(regen_obs)}")

    # -- erosion runs before Kabs and their exact positions
    runs, cur, start = [], 0, None
    for k in range(1, D):
        d = b_list[k] - b_list[k - 1]
        if d == -1:
            if cur == 0:
                start = k
            cur += 1
        else:
            if cur:
                runs.append((start, cur))
            cur = 0
    if cur:
        runs.append((start, cur))
    pre = [(s_, l) for (s_, l) in runs if s_ < (Kabs or D)]
    print(f"erosion runs pre-Kabs: {len(pre)}; lengths {[l for _, l in pre]}; "
          f"max {max((l for _, l in pre), default=0)}")
    mini = min(b_list[1:])
    print(f"min b over k=2..{D}: {mini} at k = {b_list[1:].index(mini) + 2}")
    print(f"s counts: zeros {sum(1 for x in s_list if x == 0)}, "
          f"twos {sum(1 for x in s_list if x == 2)}")

    out = {
        "D": D, "W": int(W), "Kabs": Kabs,
        "tail_linear_exact_from_Kabs": bool(tail_ok),
        "boundary_lemma_rows_checked": D - 1,
        "boundary_lemma_failures": lem_fail,
        "regen_pred": int(sum(regen_pred)), "regen_obs": int(sum(regen_obs)),
        "erosion_runs_pre_Kabs": pre,
        "min_b_over_k_ge_2": int(mini),
        "min_b_at_k": int(b_list[1:].index(mini) + 2),
    }
    with open(OUT, "w") as f:
        json.dump(out, f)
    print("wrote", OUT)


if __name__ == "__main__":
    main()