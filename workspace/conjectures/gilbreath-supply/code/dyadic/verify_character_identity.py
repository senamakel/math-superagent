#!/usr/bin/env python3
"""TASK B — Independent full verification of the corrected character identity.

For the real prime residue string r (q mod 4, via lib.primes.mod4_string),
for every n in a sweep (n=20..120) and every d in [2, n-1]:

    (-1)^{T(n,d)} == prod over runs R=[u,v] of downset(d) of
                     chi(r[a_R]) * chi(r[b_R])

where a_R = n-1-d+u, b_R = n-1-d+v+1, and chi(x) = -1 if x%4==3 else +1.

The oracle for T is lib.supply_fold.t_direct: the brute submask XOR over the
bitwise submasks of d (the literal definition). Runs come from
lib.supply_fold.runs_of_downset(d).

NEGATIVE CONTROL that must FAIL: include a spurious factor (-1)^{#runs(d)}
(i.e. multiply the product by -1 when the run count is odd) and show that it
fails on some d (e.g. d=3) — proving the no-extra-sign form is the true one.

Report the (n,d) pair count checked, the corrected-form pass count (must equal
the checked count), and the negative-control failure count (must be > 0).
Everything measured, not proved.
"""

from lib.primes import mod4_string
from lib.supply_fold import h_from_r, t_direct, runs_of_downset


def chi(x):
    return -1 if x % 4 == 3 else 1


def char_product(n, d, r):
    """prod over runs R=[u,v] of downset(d) of chi(r[a])*chi(r[b]),
    a = n-1-d+u, b = n-1-d+v+1. Corrected form (no extra sign)."""
    prod = 1
    for (u, v) in runs_of_downset(d):
        a = n - 1 - d + u
        b = n - 1 - d + v + 1
        prod *= chi(r[a]) * chi(r[b])
    return prod


def char_product_spurious(n, d, r):
    """Same but with the spurious (-1)^{#runs(d)} factor: multiply by -1 when
    the run count is odd."""
    prod = 1
    nruns = 0
    for (u, v) in runs_of_downset(d):
        nruns += 1
        a = n - 1 - d + u
        b = n - 1 - d + v + 1
        prod *= chi(r[a]) * chi(r[b])
    if nruns % 2 == 1:
        prod *= -1
    return prod


def main():
    n_lo, n_hi = 20, 120
    r = mod4_string(n_hi + 1)   # r[j]=q_j mod 4, j=0..n_hi (need index up to n-1)
    h = h_from_r(r)             # h[j] = [r[j+1] != r[j]], length len(r)-1

    checked = 0
    corrected_passes = 0
    spurious_fails = 0
    corrected_fails = []        # should stay empty
    spurious_fail_examples = [] # d where the spurious form flips

    for n in range(n_lo, n_hi + 1):
        for d in range(2, n):
            # oracle: literal submask XOR over h (the switch string), NOT r
            t = t_direct(n, d, h)
            true_sign = -1 if t else 1
            cp = char_product(n, d, r)
            cps = char_product_spurious(n, d, r)
            checked += 1
            if cp == true_sign:
                corrected_passes += 1
            else:
                corrected_fails.append((n, d, true_sign, cp))
            if cps != true_sign:
                spurious_fails += 1
                if len(spurious_fail_examples) < 8:
                    spurious_fail_examples.append((n, d, true_sign, cps))

    print(f"n sweep: {n_lo}..{n_hi}")
    print(f"(n,d) pairs checked           : {checked}")
    print(f"corrected form passes         : {corrected_passes} "
          f"({corrected_passes}/{checked})")
    print(f"corrected form FAILS          : {len(corrected_fails)}")
    for f in corrected_fails:
        print("   FAIL (corrected):", f)
    print(f"spurious (-1)^{{#runs}} FAILS  : {spurious_fails} "
          f"({spurious_fails}/{checked})  [negative control, MUST be > 0]")
    print("spurious-form failure examples (n,d,true_sign,spurious_sign):")
    for ex in spurious_fail_examples:
        print("  ", ex)

    assert not corrected_fails, f"corrected identity failed: {corrected_fails}"
    assert spurious_fails > 0, \
        "negative control did NOT fail — the corrected form is not distinguished"
    print(f"\nRESULT: corrected identity holds on all {checked} pairs; "
          f"spurious form fails on {spurious_fails} pairs "
          f"(incl. d=3, see examples).")


if __name__ == "__main__":
    main()
