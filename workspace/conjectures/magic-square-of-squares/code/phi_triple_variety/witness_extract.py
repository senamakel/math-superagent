#!/usr/bin/env python3
"""Parallel, checkpointed exact-integer rescan of the M=800 side census that
RECORDS EVERY WITNESS (side_census_par.py only printed the first 5 of each
kind per chunk).  Mirrors side_census_par.py and lib/phi.py exactly:
same phi_pairs(M) generation, same exact cross-multiplication sort, same
pair loop and break condition.

For each pair q1 > q2 in Phi(800) (reduced positive integers, exact-sorted
ASCENDING), with q1 + q2 < 1:
    1-(q1+q2) rational square  -> minus witness
    1+(q1+q2) rational square  -> plus witness
    both                        -> one entry of each kind (both count)

Rational-square test is exact: gcd-reduce num/den, then both parts must be
perfect squares.  No floats anywhere.

Output  code/out/witnesses_M{M}.json — a JSON array of entries
        [ {"kind": "minus"|"plus", "q1": [A1,B1], "q2": [A2,B2]}, ... ]
        with A/B reduced positive integers, q1 > q2 as reduced fractions,
        q1+q2 < 1, in scan order (deterministic).

Checkpoint  code/out/witness_scan_stages_M{M}.jsonl — one record per
        completed chunk carrying that chunk's full witness list, so a
        resume rebuilds every witness found so far and never re-scans a
        completed range.  The record is appended only after the chunk
        completes, so a torn last line is skipped on reload.

Final verification (the rescan IS the census): the totals must EQUAL the
recorded complete census side_census_M800_complete.captured.txt —
    718 minus / 150 plus / 0 both over 2,509,516,913 pairs over the full
    outer index of 129870 values (|Phi(800)| after exact sort).
Every witness entry is also re-verified (gcd reduced, q1>q2, q1+q2<1,
rational-square test matches its kind).  Any deviation prints the
discrepancy and exits 1.

Usage:  witness_extract.py [M] [budget_s] [nproc]
"""
import sys
import time
import json
import os
from math import gcd, isqrt
from functools import cmp_to_key
from multiprocessing import Pool

from lib.phi import phi_pairs

# Recorded complete census values per M.  The M=800 figures are the primary
# ones (code/out/side_census_M800_complete.captured.txt); the M=100 and M=200
# figures were established identically (exact agreement of side_census_par.py
# with the serial side_census.py, in the folder index) and are used to
# validate this rescan on small instances before the full run.
EXPECTED = {
    100: {"index": 2040,  "pairs": 614165,    "minus": 46,  "plus": 5,  "both": 0},
    200: {"index": 8156,  "pairs": 9856010,   "minus": 132, "plus": 24, "both": 0},
    400: {"index": 32495, "pairs": 156988030, "minus": 325, "plus": 66, "both": 0},
    800: {"index": 129870, "pairs": 2509516913, "minus": 718, "plus": 150, "both": 0},
}


def rat_square(num, den):
    """Exact: is the fraction num/den (num,den > 0) a rational square?"""
    g = gcd(num, den)
    num //= g
    den //= g
    return (num > 0 and den > 0
            and isqrt(num) ** 2 == num and isqrt(den) ** 2 == den)


def frac_cmp(a, b):
    """Exact comparator between (A,B) fractions: a.A/a.B vs b.A/b.B."""
    lhs = a[0] * b[1]
    rhs = b[0] * a[1]
    return (lhs > rhs) - (lhs < rhs)


PAIRS = None  # set in main after sorting; fork inherits via copy-on-write


def chunk_work(chunk):
    """Serial inner loop over outer indices [lo, hi).  Returns
    (lo, hi, n, nminus, nplus, nboth, witnesses) with the COMPLETE witness
    list of the chunk (every witness, not a sample)."""
    lo, hi = chunk
    P = PAIRS
    n = nminus = nplus = nboth = 0
    witnesses = []
    for i in range(lo, hi):
        A1, B1 = P[i]
        for j in range(i):
            A2, B2 = P[j]
            num = A1 * B2 + A2 * B1
            den = B1 * B2
            if num >= den:          # q1+q2 >= 1: j grows from here -> break
                break
            n += 1
            ok_minus = rat_square(den - num, den)
            ok_plus = rat_square(den + num, den)
            if ok_minus:
                nminus += 1
                witnesses.append({"kind": "minus",
                                  "q1": [A1, B1], "q2": [A2, B2]})
            if ok_plus:
                nplus += 1
                witnesses.append({"kind": "plus",
                                  "q1": [A1, B1], "q2": [A2, B2]})
            if ok_minus and ok_plus:
                nboth += 1
    return lo, hi, n, nminus, nplus, nboth, witnesses


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 540.0
    nproc = int(sys.argv[3]) if len(sys.argv) > 3 else 26
    ckpt = f"code/out/witness_scan_stages_M{M}.jsonl"
    wfile = f"code/out/witnesses_M{M}.json"

    t0 = time.time()
    Phi = phi_pairs(M)
    pairs = sorted(Phi, key=cmp_to_key(frac_cmp))
    P = len(pairs)
    global PAIRS
    PAIRS = pairs
    del Phi

    # Reload checkpoint: resume past the furthest completed chunk, and
    # rebuild the witness list + totals from the completed chunk records.
    resume_i = 0
    witnesses = []
    total_pairs = total_minus = total_plus = total_both = 0
    if os.path.exists(ckpt):
        for line in open(ckpt):
            try:
                rec = json.loads(line)
            except ValueError:
                continue            # torn tail line: chunk never completed
            if rec.get("type") != "chunk":
                continue
            resume_i = max(resume_i, rec["hi"])
            total_pairs += rec["pairs"]
            total_minus += rec["minus"]
            total_plus += rec["plus"]
            total_both += rec["both"]
            witnesses.extend(rec.get("witnesses", []))

    if M not in EXPECTED:
        print(f"[FAIL] no recorded complete census for M={M}; "
              f"refusing to guess totals", flush=True)
        sys.exit(1)
    exp = EXPECTED[M]
    if P != exp["index"]:
        print(f"[FAIL] |Phi({M})| = {P}, expected {exp['index']}; "
              f"this is not the recorded census index for M={M}",
              flush=True)
        sys.exit(1)

    print(f"[M={M}] |Phi|={P}  exact-sorted index  resume_i={resume_i}  "
          f"nproc={nproc}  budget={budget}s", flush=True)

    nchunk = 4 * nproc
    chunks = []
    stride = max(1, (P - resume_i) // nchunk)
    lo = resume_i
    while lo < P:
        hi = min(P, lo + stride)
        if hi > lo:
            chunks.append((lo, hi))
        lo = hi

    os.makedirs(os.path.dirname(ckpt) or ".", exist_ok=True)
    reached = resume_i

    if chunks:
        with Pool(nproc) as pool:
            for (clo, chi, cn, cnmin, cnplus, cnboth, cwits) in \
                    pool.imap(chunk_work, chunks):
                rec = {"type": "chunk", "M": M, "lo": clo, "hi": chi,
                       "pairs": cn, "minus": cnmin, "plus": cnplus,
                       "both": cnboth, "witnesses": cwits}
                with open(ckpt, "a") as fh:
                    fh.write(json.dumps(rec) + "\n")
                total_pairs += cn
                total_minus += cnmin
                total_plus += cnplus
                total_both += cnboth
                witnesses.extend(cwits)
                reached = max(reached, chi)
                print(f"[M={M}] chunk {clo}-{chi}: pairs {cn} minus {cnmin} "
                      f"plus {cnplus} both {cnboth} | cumulative pairs "
                      f"{total_pairs} minus {total_minus} plus {total_plus} "
                      f"both {total_both} | {time.time()-t0:.0f}s",
                      flush=True)
                if time.time() - t0 > budget:
                    print(f"[M={M}] BUDGET exceeded; reached={reached}/{P}",
                          flush=True)
                    break
    else:
        print(f"[M={M}] resume_i={resume_i} >= P={P}: scan already "
              f"complete, verifying and writing the witness file",
              flush=True)

    # ---- Final verification against the recorded complete census ----
    ok = True

    def check(name, got, want):
        nonlocal ok
        if got != want:
            ok = False
            print(f"[FAIL] {name}: got {got}, expected {want}", flush=True)

    check("outer index covered", reached, exp["index"])
    check("pairs checked", total_pairs, exp["pairs"])
    check("minus total", total_minus, exp["minus"])
    check("plus total", total_plus, exp["plus"])
    check("both total", total_both, exp["both"])
    check("minus entries in witness list", len(
        [w for w in witnesses if w["kind"] == "minus"]), total_minus)
    check("plus entries in witness list", len(
        [w for w in witnesses if w["kind"] == "plus"]), total_plus)

    # Per-entry re-verification: reduced, q1>q2, q1+q2<1, kind matches test.
    bad = 0
    for w in witnesses:
        A1, B1 = w["q1"]
        A2, B2 = w["q2"]
        num = A1 * B2 + A2 * B1
        den = B1 * B2
        if (gcd(A1, B1) != 1 or gcd(A2, B2) != 1
                or A1 * B2 <= A2 * B1 or num >= den):
            bad += 1
            print(f"[FAIL] witness invariant violated: {w}", flush=True)
        okm = rat_square(den - num, den)
        okp = rat_square(den + num, den)
        if w["kind"] == "minus" and not okm:
            bad += 1
            print(f"[FAIL] minus witness fails its own test: {w}", flush=True)
        if w["kind"] == "plus" and not okp:
            bad += 1
            print(f"[FAIL] plus witness fails its own test: {w}", flush=True)
    check("witness self-verification failures", bad, 0)

    if ok:
        with open(wfile, "w") as fh:
            json.dump(witnesses, fh)
        print(f"[M={M}] COMPLETE: covered outer-index [0,{reached}) of {P}",
              flush=True)
        print(f"  pairs checked (q1>q2, q1+q2<1): {total_pairs}", flush=True)
        print(f"  1-(q1+q2) rational square: {total_minus}", flush=True)
        print(f"  1+(q1+q2) rational square: {total_plus}", flush=True)
        print(f"  BOTH: {total_both}", flush=True)
        print(f"  witness file: {wfile} "
              f"({len(witnesses)} entries)", flush=True)
        print(f"RESULT workers={nproc} coverage={reached}/{P} "
              f"pairs={total_pairs} minus={total_minus} plus={total_plus} "
              f"both={total_both} witnesses={wfile}", flush=True)
    else:
        print("[FAIL] totals disagree with the recorded complete census "
              "(side_census_M800_complete.captured.txt); witness file NOT "
              "written (stale checkpoint data would corrupt it). "
              "Delete the checkpoint and re-run for a cold scan.",
              flush=True)
        sys.exit(1)


if __name__ == "__main__":
    main()