#!/usr/bin/env python3
"""Direct, exhaustive verification of the endpoint-sign identity in
G-endpoint-comparison-density, using the literal fold (t_direct) as oracle
and two candidate closed forms:

  committed:  (-1)^{T(n,d)} =? (-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})
  corrected:  (-1)^{T(n,d)} =? prod_R chi(r_{a_R}) chi(r_{b_R})

The down-set {submasks of d} decomposes into consecutive runs; XOR over a run
of h telescopes to a single endpoint comparison [r_{b+1} != r_a] (h[j] =
[r_{j+1}!=r_j]). Each such indicator contributes (-1)^{[...]} = chi(r_a)chi(r_b)
since [x!=y]=1 <=> chi(x)chi(y)=-1. XOR of run indicators => product of signs.
There is NO (-1)^{#runs} factor.
"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.submasks import boundary_from_h, downset_runs
from lib.supply_fold import t_direct


def chi(x):
    return -1 if x % 4 == 3 else 1


def run_terms(n, d, r):
    """(u,v) and the endpoint indices a=n-1-d+u, b=n-1-d+v+1 for each run."""
    out = []
    for (u, v) in downset_runs(d):
        out.append((n - 1 - d + u, n - 1 - d + v + 1))
    return out


def corrected(n, d, r):
    p = 1
    for (a, b) in run_terms(n, d, r):
        p *= chi(r[a]) * chi(r[b])
    return p


def committed(n, d, r):
    runs = run_terms(n, d, r)
    p = 1
    for (a, b) in runs:
        p *= chi(r[a]) * chi(r[b])
    return (-1) ** len(runs) * p


random.seed(11)
N, DMAX = 12, 11
bad_c = bad_m = 0
max_n_primes = 0
# exhaustive over ALL h of length 12 is 2^12 = 4096; do that for certainty
for mask in range(1 << N):
    h = [(mask >> j) & 1 for j in range(N)]
    r = boundary_from_h(h)
    for d in range(2, min(DMAX, N)):
        T = t_direct(N, d, h)
        true = -1 if T else 1
        if corrected(N, d, r) != true:
            bad_c += 1
            print("CORRECTED MISMATCH", "h", mask, "d", d, corrected(N, d, r), true)
        if committed(N, d, r) != true:
            bad_m += 1
            if bad_m < 6:
                print("COMMITTED MISMATCH h=%d d=%d committed=%d true=%d"
                      % (mask, d, committed(N, d, r), true))
print(f"exhaustive h in {{0,1}}^{N}: checked {N*DMAX} cells")
print(f"  corrected formula mismatch count = {bad_c}")
print(f"  committed formula mismatch count = {bad_m}")

# Also run on the actual prime residues r
from lib.primes import mod4_string
big = mod4_string(40)
r = [big[j] for j in range(40)]
h = [1 if r[j + 1] != r[j] else 0 for j in range(len(r) - 1)]
badm = badc = 0
for n in range(3, 15):
    for d in range(2, n):
        T = t_direct(n, d, h)
        true = -1 if T else 1
        if corrected(n, d, r) != true:
            badc += 1
            print("PRIME corrected mismatch", n, d, corrected(n, d, r), true)
        if committed(n, d, r) != true:
            badm += 1
            if badm < 8:
                print(f"PRIME committed mismatch n={n} d={d}: committed={committed(n,d,r)} true={true}")
print(f"primes' own r: corrected mismatch={badc}, committed mismatch={badm}")
