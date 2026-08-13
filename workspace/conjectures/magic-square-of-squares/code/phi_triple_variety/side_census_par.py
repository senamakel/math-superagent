#!/usr/bin/env python3
"""Parallel, checkpointed side census — COMPLETE M=800 run of the two side
conditions.  Mirrors prefilter_census_par.py (exact sort, chunked outer
index, process pool); the serial side_census.py was budget-killed at 18% of
the outer index at M=800, so the 6/11/both=0 figures it printed covered only
the smallest Phi-values.

Census problem, exactly as in side_census.py:
  for pairs q1 > q2 in Phi(M) (primitive m <= M), values sorted ASCENDING by
  exact cross-multiplication, with q1 + q2 < 1:
      n      = number of pairs checked
      nminus = pairs where 1-(q1+q2) is a rational square
      nplus  = pairs where 1+(q1+q2) is a rational square
      nboth  = pairs where BOTH are rational squares
  A both-witness is a NECESSARY-condition survivor for q1+q2 in Phi (every
  q in Phi has 1-q and 1+q rational squares) and would be printed
  IMMEDIATELY.  The claim under test (phi-pair-sides-never-both-square,
  status: checked at M=400) is extended to the full M=800 index.

Rational-square test is exact: reduce num/den by gcd, then both reduced
parts must be perfect squares.  No floats anywhere.

Usage:
  side_census_par.py M [budget_s] [resume_i] [nproc] [checkpoint]
  M        primitive bound, default 800
  budget   wall-clock budget per invocation, default 560 (tool ceiling 600)
  resume_i outer index to resume from (default 0); chunks beyond the
           checkpoint's max completed lo are the resume range.
  nproc    pool size, default 28 (the box has 28 CPUs; two reserved)
  checkpoint JSONL path, default code/out/side_census_stages_M{M}.jsonl

Prints one line per chunk plus a final RESULT with worker count and the
covered index range.  Exit code 0.
"""
import sys
import time
import json
import os
from math import gcd, isqrt
from functools import cmp_to_key
from multiprocessing import Pool

from lib.phi import phi_pairs


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
    (lo, hi, n, nminus, nplus, nboth, minus_examples, plus_examples)
    with examples limited to the first 5 of each kind per chunk."""
    lo, hi = chunk
    P = PAIRS
    n = nminus = nplus = nboth = 0
    minus_ex = []
    plus_ex = []
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
                if len(minus_ex) < 5:
                    minus_ex.append(((A1, B1), (A2, B2)))
            if ok_plus:
                nplus += 1
                if len(plus_ex) < 5:
                    plus_ex.append(((A1, B1), (A2, B2)))
            if ok_minus and ok_plus:
                nboth += 1
    return lo, hi, n, nminus, nplus, nboth, minus_ex, plus_ex


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 800
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 560.0
    resume_i = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    nproc = int(sys.argv[4]) if len(sys.argv) > 4 else 28
    ckpt = sys.argv[5] if len(sys.argv) > 5 else f"out/side_census_stages_M{M}.jsonl"

    t0 = time.time()
    Phi = phi_pairs(M)
    pairs = sorted(Phi, key=cmp_to_key(frac_cmp))
    P = len(pairs)
    global PAIRS
    PAIRS = pairs
    del Phi

    # resume past the furthest completed chunk recorded in the checkpoint
    if resume_i == 0 and os.path.exists(ckpt):
        for line in open(ckpt):
            try:
                rec = json.loads(line)
                resume_i = max(resume_i, rec["hi"])
            except (ValueError, KeyError):
                pass

    print(f"[M={M}] |Phi|={P}  exact-sorted index  resume_i={resume_i}  "
          f"nproc={nproc}  budget={budget}s", flush=True)

    nchunk = 4 * nproc
    chunks = []
    stride = max(1, (P - resume_i) // nchunk)
    lo = resume_i
    while lo < P:
        hi = min(P, lo + stride)
        chunks.append((lo, hi))
        lo = hi

    os.makedirs(os.path.dirname(ckpt) or ".", exist_ok=True)
    total_pairs = total_minus = total_plus = total_both = 0
    reached = resume_i
    if not chunks:
        print(f"[M={M}] resume_i={resume_i} >= P={P}: nothing to do")
        print(f"RESULT workers={nproc} reached={reached}/{P} "
              f"pairs={total_pairs} minus={total_minus} plus={total_plus} "
              f"both={total_both}")
        return

    with Pool(nproc) as pool:
        for (clo, chi, cn, cnmin, cnplus, cnboth, minex, pluex) in \
                pool.imap(chunk_work, chunks):
            rec = {"M": M, "lo": clo, "hi": chi, "pairs": cn,
                   "minus": cnmin, "plus": cnplus, "both": cnboth}
            with open(ckpt, "a") as fh:
                fh.write(json.dumps(rec) + "\n")
            total_pairs += cn
            total_minus += cnmin
            total_plus += cnplus
            total_both += cnboth
            reached = max(reached, chi)
            for q1, q2 in minex:
                print(f"  MINUS q1={q1[0]}/{q1[1]} q2={q2[0]}/{q2[1]} "
                      f"(chunk {clo}-{chi})", flush=True)
            for q1, q2 in pluex:
                print(f"  PLUS  q1={q1[0]}/{q1[1]} q2={q2[0]}/{q2[1]} "
                      f"(chunk {clo}-{chi})", flush=True)
            if cnboth:
                print(f"  *** BOTH-WITNESS count {cnboth} in chunk "
                      f"{clo}-{chi} *** (needs immediate exact "
                      f"re-verification)", flush=True)
            print(f"[M={M}] chunk {clo}-{chi}: pairs {cn} minus {cnmin} "
                  f"plus {cnplus} both {cnboth} | cumulative pairs "
                  f"{total_pairs} minus {total_minus} plus {total_plus} "
                  f"both {total_both} | {time.time()-t0:.0f}s", flush=True)
            if time.time() - t0 > budget:
                print(f"[M={M}] BUDGET exceeded; reached={reached}/{P}", flush=True)
                break
    print(f"[M={M}] COMPLETE: covered outer-index [0,{reached}) of {P}",
          flush=True)
    print(f"  pairs checked (q1>q2, q1+q2<1): {total_pairs}", flush=True)
    print(f"  1-(q1+q2) rational square: {total_minus}", flush=True)
    print(f"  1+(q1+q2) rational square: {total_plus}", flush=True)
    print(f"  BOTH: {total_both}", flush=True)
    print(f"RESULT workers={nproc} reached={reached}/{P} pairs={total_pairs} "
          f"minus={total_minus} plus={total_plus} both={total_both}")


if __name__ == "__main__":
    main()