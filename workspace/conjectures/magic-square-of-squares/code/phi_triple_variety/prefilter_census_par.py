#!/usr/bin/env python3
"""Parallel, checkpointed prefilter-survivor census — same semantics as the
serial prefilter_census.py, but chunked by outer index over a process pool.

Census: for pairs q1 > q2 in Phi (primitive m <= M), values sorted
ascending, with q1+q2 < 1, count those where BOTH 1-(q1+q2) and
1+(q1+q2) are rational squares — a NECESSARY condition for q1+q2 to lie
in the universal set Phi = { 4mn(m^2-n^2)/(m^2+n^2)^2 } (every q in Phi
has 1-q and 1+q rational squares).  A survivor is a CANDIDATE additive
triple (q1, q2, q1+q2 in Phi), not a proof: report it immediately.

Differences from the serial program, all checked:
  * sort key is EXACT cross-multiplication (cmp_to_key), not float division
    — denominators reach ~2e13 at M=1500, below float's 53-bit separation,
    so the float sort used by the serial program can misorder close values
    and would make the sum<1 break invalid at large M.
  * outer range [resume_i, P) is split into ~4*nproc contiguous chunks;
    each chunk is one pool task with the identical inner loop and the
    identical survivor predicate (exact integer arithmetic throughout).
  * every completed chunk is appended as one JSON line to the checkpoint
    file, so progress survives a stage timeout; the next stage resumes by
    outer index = max completed hi.

Usage:
  prefilter_census_par.py M [budget_s] [resume_i] [nproc] [checkpoint]

  M          primitive bound (outer pairs use Phi(M), i.e. m <= M)
  budget_s   wall-clock budget per INVOCATION (checked per chunk), default 500
  resume_i   restart outer index (pairs[i] for i < resume_i already counted;
             survivors among them already recorded in earlier stages) default 0
  nproc      pool size, default 28
  checkpoint path for JSONL stage records, default
             code/out/prefilter_census_stages_M.jsonl

Prints one line per chunk and a stage summary with the reached index.
Exit code 0.  Survivors print IMMEDIATELY with their (A,B) value triples.
"""
import sys, time, json, os
from math import gcd, isqrt
from functools import cmp_to_key
from multiprocessing import Pool


def rat_square(num, den):
    """Exact: is reduced fraction num/den a rational square? (num,den > 0)"""
    g = gcd(num, den)
    num //= g
    den //= g
    return (num > 0 and den > 0
            and isqrt(num) ** 2 == num and isqrt(den) ** 2 == den)


def frac_cmp(a, b):
    """Exact comparator: a.A/a.B vs b.A/b.B (both (A,B), B>0)."""
    lhs = a[0] * b[1]
    rhs = b[0] * a[1]
    return (lhs > rhs) - (lhs < rhs)


def phi_pairs_exact(M):
    """Reduced value set of Phi for primitive m in [2, M], n in [1, m-1].
    Exact integer arithmetic only."""
    out = set()
    for m in range(2, M + 1):
        m2 = m * m
        for n in range(1, m):
            num = 4 * m * n * (m2 - n * n)
            den = (m2 + n * n) ** 2
            g = gcd(num, den)
            out.add((num // g, den // g))
    return out


PAIRS = None  # set in main; fork inherits (read-only, copy-on-write)


def chunk_work(chunk):
    """Run the serial inner loop over outer indices [lo, hi).
    Returns (lo, hi, pairs_checked, survivors) where packages are not yet
    reduced sums: each survivor is ((A1,B1),(A2,B2),(num,den)) with
    S = num/den (reduced at report time)."""
    lo, hi = chunk
    P = PAIRS
    n = 0
    surv = []
    for i in range(lo, hi):
        A1, B1 = P[i]
        for j in range(i):
            A2, B2 = P[j]
            num = A1 * B2 + A2 * B1
            den = B1 * B2
            if num >= den:          # q1+q2 >= 1 -> cannot be in Phi; j grows
                break
            n += 1
            if rat_square(den - num, den) and rat_square(den + num, den):
                surv.append(((A1, B1), (A2, B2), (num, den)))
    return lo, hi, n, surv


def reduce_nd(num, den):
    g = gcd(num, den)
    return (num // g, den // g)


def main():
    M = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 500.0
    resume_i = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    nproc = int(sys.argv[4]) if len(sys.argv) > 4 else 28
    ckpt = sys.argv[5] if len(sys.argv) > 5 else (
        f"out/prefilter_census_stages_M{M}.jsonl")

    t0 = time.time()
    Phi = phi_pairs_exact(M)
    pairs = sorted(Phi, key=cmp_to_key(frac_cmp))
    P = len(pairs)
    global PAIRS
    PAIRS = pairs
    del Phi

    nchunk = 4 * nproc
    chunks = []
    stride = max(1, (P - resume_i) // nchunk)
    lo = resume_i
    while lo < P:
        hi = min(P, lo + stride)
        chunks.append((lo, hi))
        lo = hi

    os.makedirs(os.path.dirname(ckpt) or ".", exist_ok=True)
    total_pairs = 0
    total_surv = 0
    reached = resume_i
    if not chunks:
        print(f"[M={M}] resume_i={resume_i} >= P={P}: nothing to do")
        print("RESULT reached=" + str(reached) + " pairs=" + str(total_pairs)
              + " survivors=" + str(total_surv))
        return

    with Pool(nproc) as pool:
        for (clo, chi, cn, csv) in pool.imap(chunk_work, chunks):
            rec = {
                "M": M, "lo": clo, "hi": chi, "pairs": cn,
                "survivors": [
                    {"q1": list(map(int, q1)), "q2": list(map(int, q2)),
                     "S": list(map(int, reduce_nd(*s)))}
                    for q1, q2, s in csv
                ],
            }
            with open(ckpt, "a") as fh:
                fh.write(json.dumps(rec) + "\n")
            total_pairs += cn
            reached = max(reached, chi)
            if csv:
                total_surv += len(csv)
                for q1, q2, s in csv:
                    s_red = reduce_nd(*s)
                    print(f"  SURVIVOR q1={q1[0]}/{q1[1]} q2={q2[0]}/{q2[1]} "
                          f"S={s_red[0]}/{s_red[1]}  (M={M} chunk {clo}-{chi})",
                          flush=True)
            print(f"[M={M}] chunk {clo}-{chi}: pairs {cn} survivors {len(csv)} "
                  f"| cumulative {total_pairs} | {time.time()-t0:.0f}s",
                  flush=True)
            if time.time() - t0 > budget:
                print(f"[M={M}] BUDGET exceeded; reached={reached}/{P}; "
                      f"pairs this invocation: {total_pairs}; "
                      f"survivors this invocation: {total_surv}",
                      flush=True)
                print("RESULT reached=" + str(reached) + " pairs="
                      + str(total_pairs) + " survivors=" + str(total_surv))
                return
    print(f"[M={M}] COMPLETE: |Phi|={P}; pairs q1>q2 sum<1 checked "
          f"this invocation: {total_pairs}; survivors: {total_surv}; "
          f"{time.time()-t0:.0f}s", flush=True)
    print("RESULT reached=" + str(reached) + " pairs=" + str(total_pairs)
          + " survivors=" + str(total_surv))


if __name__ == "__main__":
    main()