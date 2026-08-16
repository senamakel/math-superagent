#!/usr/bin/env python3
"""Probe the two RIVAL structural claims whose shared first move is the
sparse-image question:

  G-weak-input-strictness : EXISTS fixed h with switch density 0 (density of
    1-positions -> 0) yet nu2(n) = wt(Phi_n h) >= c.n  (fold does work the
    frequency form cannot see).
  G-eq-sparse-fold-is-sublinear : max over k-sparse h (k = o(n)) of wt(Phi_n h)
    is o(n); no sparse h reaches linear fold weight.

These are contrapositive-ish rivals.  We test concrete sparse families against
the EXACT fold oracle and report nu2(n)/n:
  - single fixed 1 at j (known: bounded by j+1, so sublinear) -- control
  - powers of two (density 0)
  - squares (density 0)
  - 2^floor(log2) boundaries?  plus a hand-constructed "every 2^m" family.

We first VALIDATE the oracle on the real prime h by reproducing
nu2(53)=18, nu2(64)=27, nu2(4000)=1975 (problem.md convention).

Operative definition (problem.md): nu2(n) = #{ d in [2, n-1] :
T(n,d)=1 }, T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o].
Exact, via lib.supply_fold.s_sos (verified vs the literal oracle on
n=8..60).
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_sos
from lib.primes import h_string


def prime_h(n):
    return h_string(n + 2)[:n]


def nu2(n, h):
    S, ones = s_sos(n, h)
    return ones


def validate():
    got = {n: nu2(n, prime_h(n)) for n in (4000, 53, 64, 100)}
    print("validation (real prime h):", got)
    assert got[53] == 18, got[53]
    assert got[64] == 27, got[64]
    assert got[4000] == 1975, got[4000]
    # empirical mean sanity ~ 0.5
    tot = 0.0
    for n in range(2, 2001):
        tot += nu2(n, prime_h(n)) / n
    print("M(2000) prime = %.4f (literature ~0.495)" % (tot / 2000))
    return "oracle OK"


def sparse_set_indicator(n, positions):
    """Length-n h with 1s exactly at positions < n in the set `positions`."""
    h = [0] * n
    for j in positions:
        if j < n:
            h[j] = 1
    return h


def min_and_tail_ratio(n_min, n_max, family_fn, family_name):
    """Report mean and min of nu2(n)/n over n in [n_min, n_max] for the
    family h defined by family_fn(n) (a length-n string)."""
    ratios = []
    for n in range(n_min, n_max + 1):
        h = family_fn(n)
        ratios.append(nu2(n, h) / n)
    mean = sum(ratios) / len(ratios)
    mn = min(ratios)
    tail = min(ratios[len(ratios) // 2:]) if len(ratios) > 1 else mn
    print(f"{family_name:28s} n in [{n_min},{n_max}]  mean={mean:.4f} "
          f"min={mn:.4f}  min tail={tail:.4f}")
    return mean, mn, tail


def powers_of_two(n):
    return sparse_set_indicator(n, [1 << k for k in range(64)])


def squares(n):
    import math
    return sparse_set_indicator(n, [k * k for k in range(1, int(math.isqrt(n)) + 2)])


def single_fixed_one(n):
    return sparse_set_indicator(n, [7])


def twin_powers(n):
    # 1s at 2^k and 2^k+1 : a "long" run structure, density 0
    return sparse_set_indicator(n, [ (1 << k) + i for k in range(64) for i in range(1 << min(k, 3)) ])


def main():
    validate()
    print()
    print("=== nu2(n)/n for sparse families (fixed h, switch density 0) ===")
    print("NOTE: linear here (bounded below by c>0) SUPPORTS G-weak-input-")
    print("strictness and REFUTES G-eq-sparse-fold-is-sublinear; sublinear")
    print("supports the rival.")
    print()
    H = head = lambda: None
    min_and_tail_ratio(50, 3000, powers_of_two, "powers of two")
    min_and_tail_ratio(50, 3000, squares, "squares")
    min_and_tail_ratio(50, 3000, single_fixed_one, "single fixed 1 @7 (control)")
    # twin_powers is expensive (dense in small ranges) -- restrict
    print()


if __name__ == "__main__":
    main()
