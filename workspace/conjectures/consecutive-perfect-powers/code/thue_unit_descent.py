#!/usr/bin/env python3
"""Explore whether the units of Q(cuberoot(2)) give a complete in-workspace
resolution of the Thue equations  c^3 - 2 d^3 = +-1  via unit descent.

Setup.  omega^3 = 2.  Element 1 - omega has norm -1 and is the fundamental
unit of Z[omega]; the field has class number 1 and unit rank 1, so every unit
is +-(1-omega)^n for n in Z.  A number c - d*omega has coefficients
(c, -d, 0) in the basis {1, omega, omega^2}: zero omega^2 coefficient.  Hence
the integer solutions (c, d) of c^3 - 2 d^3 = +-1 are exactly the n for which
(1-omega)^n has zero omega^2 coefficient, with c = a_n and d = -b_n where
(1-omega)^n = a_n + b_n omega + c_n omega^2.

The open question (the reason this is exploration, not a proof) is whether the
omega^2-coefficient c_n vanishes only for n in {0, 1}, or vanishes again at
some larger |n|.  This program scans n in [-N, N] by EXACT integer recurrence
and reports every zero.  N = 2000 per the task.  It also characterises the
growth of c_n (sign changes, magnitude) to show why a recorded window is not
itself a proof for all n.

Recurrences (exact integers):
  Forward (multiply by 1-omega):
    a_{n+1} = a_n - 2 c_n
    b_{n+1} = b_n - a_n
    c_{n+1} = c_n - b_n
    base (a_0, b_0, c_0) = (1, 0, 0)      [ (1-omega)^0 = 1 ]
  Backward (multiply by (1-omega)^-1 = -(1+omega+omega^2) = (-1,-1,-1);
            omega^4 = 2 omega):
    a' = -a - 2 b - 2 c
    b' = -a - b - 2 c
    c' = -a - b - c
  Verified: forward n=1 -> (1,-1,0) = 1-omega (c_1 = 0);
            backward maps n=1 -> (1,0,0) [*], n=0 -> (-1,-1,-1) [*].

All arithmetic arbitrary-precision integers; no floats.
"""
import sys

N = 2000


def forward_step(abc):
    """Multiply coefficients a + b*w + c*w^2 by (1 - w)."""
    a, b, c = abc
    return (a - 2 * c, b - a, c - b)


def backward_step(abc):
    """Multiply coefficients a + b*w + c*w^2 by (1-w)^-1 = -(1+w+w^2)."""
    a, b, c = abc
    return (-a - 2 * b - 2 * c, -a - b - 2 * c, -a - b - c)


def collect_zeros(N):
    """Return {n: (a, b)} for each n in [-N, N] whose omega^2 coeff is 0."""
    zeros = {}

    # ---- forward from n=0 up to N ----
    a, b, c = 1, 0, 0
    for n in range(0, N + 1):
        if c == 0:
            zeros[n] = (a, b)
        a, b, c = forward_step((a, b, c))

    # ---- backward from n=0 down to -N ----
    a, b, c = 1, 0, 0
    for m in range(0, N + 1):          # m = |n| steps of inverse
        n = -m
        if c == 0:
            zeros[n] = (a, b)
        a, b, c = backward_step((a, b, c))

    return zeros


def main():
    print("=" * 74)
    print(f"Thue unit descent in Q(cuberoot(2)), omega^3 = 2")
    print(f"(1-omega)^n = a_n + b_n omega + c_n omega^2 for n in [-{N}, {N}]")
    print(f"Exact integer recurrence; no floats.  Scan bound N = {N}.")
    print("=" * 74)

    # Sanity checks of the recurrence on the tiny cases.
    print("\nSanity: (1-omega)^small cases by the recurrence")
    a, b, c = 1, 0, 0
    for n in range(0, 5):
        print(f"  n={n}: a={a}, b={b}, c={c}   meaning {a} + {b}*w + {c}*w^2")
        a, b, c = forward_step((a, b, c))
    # inverse check
    print("  inverse of (1-w) by backward_step on (1,-1,0):",
          backward_step((1, -1, 0)), " (expect (1,0,0))")
    print("  (1-w)^-1 backward from (1,0,0):", backward_step((1, 0, 0)),
          " (expect (-1,-1,-1))")

    zeros = collect_zeros(N)

    print("\n" + "=" * 74)
    print(f"n in [-{N}, {N}] with omega^2-coefficient c_n == 0")
    print("=" * 74)
    if not zeros:
        print("  NONE")
    for n in sorted(zeros):
        a, b = zeros[n]
        c, d = a, -b
        print(f"  n={n:5d}: (1-w)^n = a + b*w (c_n=0)  ->  (c,d)=({c},{d})"
              f"  c^3-2d^3 = {c**3 - 2*d**3}")

    # Complete solution set of the two Thue equations from the found n.
    # c_n == 0 means BOTH (1-w)^n and -(1-w)^n have zero w^2 coefficient, so
    # each zero index yields two units -> two (c,d) pairs (the +/- partners).
    print("\nComplete (c,d) for c^3 - 2 d^3 = +-1 from zero-c_n units")
    print("  (both sign partners; each zero c_n gives (a,-b) and (-a,b)):")
    sols = sorted({(zz[0], -zz[1]) for zz in zeros.values()} |
                  {(-zz[0], zz[1]) for zz in zeros.values()})
    for (c, d) in sols:
        print(f"  (c,d)=({c},{d})   c^3-2d^3 = {c**3 - 2*d**3}")

    print("\n" + "=" * 74)
    print("Growth behaviour of the omega^2 coefficient c_n")
    print("=" * 74)
    vals = []
    a, b, c = 1, 0, 0
    for n in range(0, N + 1):
        vals.append((n, c))
        a, b, c = forward_step((a, b, c))
    a, b, c2 = 1, 0, 0
    for m in range(1, N + 1):
        n = -m
        vals.append((n, c2))
        a, b, c2 = backward_step((a, b, c2))
    vals.sort()

    signs = set()
    for (n, cnow) in vals:
        if cnow > 0:
            signs.add('pos')
        elif cnow < 0:
            signs.add('neg')
        else:
            signs.add('zero')
    print("  signs taken by c_n over |n|<=N:", sorted(signs))
    # count sign changes between consecutive n
    changes = 0
    ordered = [c for (_, c) in vals]
    sign_of = lambda v: (v > 0) - (v < 0)
    for i in range(1, len(ordered)):
        if sign_of(ordered[i]) != 0 and sign_of(ordered[i-1]) != 0 \
           and sign_of(ordered[i]) != sign_of(ordered[i-1]):
            changes += 1
    print(f"  sign changes among nonzero c_n over |n|<=N: {changes}")
    mags = [abs(c) for (_, c) in vals]
    print(f"  max |c_n| over |n|<=N: {max(mags)}")
    print(f"  min |c_n| over NONZERO c_n, |n|<=N: {min(m for m in mags if m>0)}")
    # how big are the largest few indices' coefficients (magnitude growth)?
    tail = sorted(vals)[-6:]
    print("  tail behaviour (n -> c_n):")
    for (n, cnow) in tail:
        print(f"    n={n:5d}: c_n = {cnow}   (|c_n|={abs(cnow)})")

    print("\n" + "=" * 74)
    zeros_list = sorted(zeros)
    if zeros_list == [0, 1]:
        verdict = ("EXACTLY n in {0, 1} within |n| <= %d.  The omega^2 "
                   "coefficient never vanishes again inside this window."
                   % N)
    else:
        verdict = ("omega^2 vanishes at extra index/indices "
                   "beyond {0,1}: %s" % zeros_list)
    print("Verdict over |n| <= %d: %s" % (N, verdict))
    if zeros_list == [0, 1]:
        print("  Within the scanned window the only Thue solutions are")
        print("  (c,d) = (1,0) [=1] and (1,1) [=1-w], giving c^3-2d^3 = 1 and -1.")
    print("=" * 74)


if __name__ == "__main__":
    main()
