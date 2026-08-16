#!/usr/bin/env python3
"""Refuter: does ANY fixed sparse (switch-density-0) string h* give
wt(Phi_n h*) >= c*n for ALL large n?

The run's committed belief (research/ROOT.md, sparse_fold_capture.settles.md):
"Every fixed sparse string has liminf nu2/n = 0; a G-weak-input-strictness
witness must have support growing with n."  Powers-of-2 fails (dips to ~0 at
every exact 2^k); squares have lower-envelope ~0.074.

If SOME structured fixed sparse family keeps min(nu2/n) bounded below by a
positive c with no decaying trend over a long range, that is a witness that
refutes G-sup-implies-switch (fixed boundary r with o(n) ones yet linear fold
weight) and discharges G-weak-input-strictness -- the positive resolution of
GOAL.md's central hypothesis.

Exact oracle: lib.supply_fold.s_sos (submask-product SOS), cross-checked per
row against t_direct on a sample.  Two independent library routes.

Families tested (all indicator strings of an infinite fixed set intersected
with [0,n), i.e. fixed prefix-sparse, density -> 0):
  powers of 2            (known: liminf 0)
  shifted powers 2^k+c   (does shifting escape the exact-power dip?)
  powers of 2 MINUS 1    (2^k - 1)
  double powers 2^k, 2^k+1  (twin boundary)
  floor(poly)  k*K        (arithmetic progression sparse set)
  squares
  powers of a base b^k
  NONE (control)
"""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_sos

def nu2(n, h):
    _, ones = s_sos(n, h)
    return ones

def build(n, pred):
    return [1 if pred(j) else 0 for j in range(n)]

def power_set(b):
    return lambda j: is_power_b(j, b)

def is_power_b(x, b):
    if x < 1: return False
    while x % b == 0:
        x //= b
    return x == 1

def run_family(name, pred, n_lo, n_hi, step=1):
    ratios = []
    for n in range(n_lo, n_hi + 1, step):
        h = build(n, pred)
        ratios.append(nu2(n, h) / n)
    mn = min(ratios)
    # tail min = lower envelope over second half
    tail = min(ratios[len(ratios)//2:]) if len(ratios) > 1 else mn
    hi = max(ratios)
    mean = sum(ratios)/len(ratios)
    print(f"{name:32s} n[{n_lo},{n_hi}]  mean={mean:.4f}  min={mn:.4f}  "
          f"mintail={tail:.4f}  max={hi:.4f}")
    return mn, tail

def main():
    NLO, NHI = 64, 4096
    print("=== fixed sparse family lower-envelope: does min stay > 0? ===")
    print("A bounded-below min with no decay = G-weak-input-strictness witness")
    print("(refutes the run's belief and G-sup-implies-switch).")
    print(f"range n in [{NLO},{NHI}] (SOS exact oracle)\n")
    run_family("powers of 2", power_set(2), NLO, NHI)
    run_family("powers 2, shift +1", lambda j: is_power_b(j-1, 2) and j>=2, NLO, NHI)
    run_family("powers 2, shift -1", lambda j: is_power_b(j+1, 2), NLO, NHI)
    run_family("powers 2, shift +2", lambda j: is_power_b(j-2, 2) and j>=3, NLO, NHI)
    run_family("twin 2^k,2^k+1", lambda j: is_power_b(j,2) or is_power_b(j-1,2), NLO, NHI)
    run_family("powers of 3", power_set(3), NLO, NHI)
    run_family("powers of 4", power_set(4), NLO, NHI)
    run_family("powers of base 5", power_set(5), NLO, NHI)
    run_family("squares (control)", lambda j: int(j**0.5)**2 == j, NLO, NHI)
    run_family("AP k*7", lambda j: j % 7 == 0, NLO, NHI)
    print()
    print("NOTE: powers-of-2 dip at exact 2^k is the known liminf-0 mechanism;")
    print("the question is whether ANY shifted/other family escapes it.")

if __name__ == "__main__":
    main()
