"""Verify Lmin(k) = k + NextFib(k) - 1 for all k = 1..6764, on a prefix
of the infinite Fibonacci word of length >= 24000.

This extends verify_lmin_formula.py (which covered k = 1..2583 on a 6765-char
prefix) to the whole block k <= 6764 using the same exact-integer bit-mask
factor extraction (gen_sequences.py style).  It is a fresh, independent
recomputation: new prefix, new driver, helpers imported from code/lib/fibword.py
rather than copied.

A prefix-bug note recorded in the run: an insufficient prefix (4181 chars for
k up to 2583, where Lmin(2583)=2583+2584-1=5166) made the scan return None --
an early-stop scan cannot falsely pass, it can only fail by None.  So a
"zero mismatches" verdict on a prefix >= 24000 is an honest verification for
every k in range.  The largest Lmin over the whole range is at k=6764:
with the run's Fibonacci indexing (F_2=1, F_3=2, ..., F_19=6765, F_20=10946),
NextFib(6764)=6765, so Lmin(6764)=13528 << 24000, and in every block
F_m <= k < F_{m+1} the value Lmin = k + F_{m+1} - 1 <= F_{m+1} + F_{m+1} - 2
= 2*F_{m+1} - 2 stays well under the prefix once F_{m+1} <= 6765 (this range
is F_19 = 6765).  Every Lmin measured is < 24000, so no None can appear; the
script asserts that anyway.

Report (a) zero mismatches or the first failing k, and (b) Lmin and the
formula value at k = 1596, 1597, 2583, 2584, 4180, 4181, 6764.
"""

from lib.fibword import fibs_upto, next_fib, fib_prefix, lmin_seq, lmin_formula

KMAX = 6764
L = 24000


def main():
    # Prefix length >= 24000, landing on a Fibonacci length: 3.7*6764+100
    # = 25126.8, and the first Fibonacci length above that is F_22 = 28657
    # (the doubling 6765 -> 10946 -> 17711 -> 28657); the doubling loop
    # below stops at the first fib length >= 24000.
    L = 24000
    W = fib_prefix(L)
    assert len(W) >= 24000
    print(f"prefix length {len(W)} (Fibonacci number F_22 = 28657, >= 24000)")

    lm = lmin_seq(W, KMAX)
    assert all(v is not None for v in lm), "prefix too short: an Lmin came back None"

    fibs = fibs_upto(KMAX + 1)
    mism = []
    for k in range(1, KMAX + 1):
        want = lmin_formula(k)
        if lm[k - 1] != want:
            mism.append((k, lm[k - 1], want))
    print(f"mismatches of Lmin(k) = k + NextFib(k) - 1 for k=1..{KMAX}: {len(mism)}")
    print("first mismatches:", mism[:10])
    if mism:
        print(f"FIRST FAILING k: {mism[0][0]}  (Lmin={mism[0][1]} formula={mism[0][2]})")
    else:
        print("first failing k: none -- zero mismatches")

    print("\nRequested values (k, Lmin(k), k + NextFib(k) - 1):")
    for k in [1596, 1597, 2583, 2584, 4180, 4181, 6764]:
        print(f"  k={k:5d}  Lmin={lm[k - 1]:6d}  formula={lmin_formula(k):6d}"
              f"  NextFib(k)={next_fib(k, fibs)}")

    # Fibonacci-block summary around the requested points: the block
    # F_m <= k < F_{m+1} has the constant NextFib = F_{m+1}, so Lmin is
    # linear in k inside each block -- the boundary k's are where a wrong
    # block constant would show up.
    print("\nBlock boundaries in the requested range (k, NextFib(k)):")
    for Fm in fibs:
        if Fm >= 6764:
            break
        # k = F_m - 1 (block below) and k = F_m (block at F_m)
        for k in (Fm - 1, Fm):
            if 1 <= k <= KMAX:
                print(f"  k={k:5d}  NextFib={next_fib(k, fibs):6d}")


if __name__ == '__main__':
    main()