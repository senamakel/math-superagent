#!/usr/bin/env python3
"""Exploratory: determine which indexing makes the regeneration lemma true.

Tests, for each k 1..999, two index conventions for (edge, intruder, q):
  A) literal task (b_k-1):  e=A_k[b_k-1], c=A_k[b_k+1], q=A_{k+1}[b_k-1]
  B) true block end (b_k):  e=A_k[b_k],   c=A_k[b_k+1], q=A_{k+1}[b_k]
For both: q==|e-c| ?  and  lemma: q in {0,2} iff (e==2 and c==4);
and regen: b_{k+1}>=b_k iff (e==2 and c==4).
Skips k where the intruder index is out of the row's width (block runs to
the array end) -- these are the null intruder entries in the witness.
"""
import numpy as np
from lib.gilbreath import primes_up_to

SIEVE = 20_000_000
DEPTH = 1000
primes = np.array(primes_up_to(SIEVE), dtype=np.int64)

def block_profile(row):
    n = 0
    for x in row[1:]:
        if x in (0, 2):
            n += 1
        else:
            break
    return n

r0 = primes.copy()
r1 = np.abs(np.diff(r0))          # A_1

def eval_var(label, off):
    global r0, r1
    iff_fail = 0
    regen_fail = 0
    id_mismatch = 0
    skipped = 0
    checked = 0
    held_t = 0    # both true
    for k in range(1, 1000):
        r2 = np.abs(np.diff(r1))  # A_{k+1}
        b = block_profile(r1)
        bi = b - 1 if off == 0 else b       # edge index
        if b + 1 >= len(r1):
            skipped += 1
            r0, r1 = r1, r2
            continue
        e = int(r1[bi])
        c = int(r1[b + 1])
        q = int(r2[bi])
        if q != abs(e - c):
            id_mismatch += 1
        lhs = (q in (0, 2))
        rhs = (e == 2 and c == 4)
        if lhs != rhs:
            iff_fail += 1
        bnext = block_profile(r2)
        if (bnext >= b) != rhs:
            regen_fail += 1
        checked += 1
        if lhs and rhs:
            held_t += 1
        r0, r1 = r1, r2
    print(f"[{label}] checked={checked} skipped(row-end, no intruder)={skipped}")
    print(f"[{label}] q==|e-c| mismatches = {id_mismatch}")
    print(f"[{label}] IFF failures (q in {{0,2}} iff e==2&c==4) = {iff_fail}")
    print(f"[{label}] REGEN failures (b_next>=b iff e==2&c==4) = {regen_fail}")
    print(f"[{label}] k where both q in {{0,2}} AND e==2&c==4 = {held_t}")
    return iff_fail, regen_fail

# must recompute rows per variant since we consumed r1/r2; rerun fresh
def reset():
    global r0, r1
    r0 = primes.copy()
    r1 = np.abs(np.diff(r0))

reset(); eval_var("A) literal b_k-1", 0)
reset(); eval_var("B) true end b_k ", 1)
