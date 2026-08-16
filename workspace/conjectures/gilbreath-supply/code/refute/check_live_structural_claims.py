#!/usr/bin/env python3
"""Adversarial check of two LIVE (proposed, unchecked) structural claims:

1. abel-boundary-recurrence:  T(n,d) == T(n-1,d) XOR T(n-1,d-1)
   (claimed from "the submask set of d splits by the lowest set bit")
2. substitution-incidence-perron:  T(2n,2d)==T(n,d), T(2n,2d+1)==0,
   T(2n+1,2d)==T(n,d), T(2n+1,2d+1)==T(n,d)

where T(n,d) = XOR_{o subseteq d} h[n-1-d+o]  (SUPPLY fold cell).

Both are claimed to hold for ANY {0,1} sequence h (pure Boolean structure).
We brute-check them on many random h and on structured h (all-ones, powers of
two, Thue-Morse, anti-dyadic balanced).  A single (n,d,h) counterexample
refutes the claim as stated.

NOTE on "up to the window reversal": T(n,d) reads h[ n-1-d+o ].  The three
cells T(n,d), T(n-1,d), T(n-1,d-1) read h at offsets from three different
window starts (n-1-d, n-2-d, n-2-(d-1)).  If the claimed relation holds as a
statement about the SAME h with these offsets, it is nontrivial and worth
checking exactly.
"""

import random


def t(n, d, h):
    """Literal fold cell."""
    x = 0
    for o in range(d + 1):
        if (o & d) == o:
            x ^= h[n - 1 - d + o]
    return x


def check_abel(n_hi, trials, rng):
    bad = []
    for n in range(3, n_hi + 1):
        for _ in range(trials):
            h = [rng.randint(0, 1) for _ in range(n)]
            for d in range(2, n):
                lhs = t(n, d, h)
                # rhs cells use h of length n-1 (T(n-1,*) reads up to index n-2)
                if d <= n - 2:
                    rhs = t(n - 1, d, h[:n - 1]) ^ t(n - 1, d - 1, h[:n - 1])
                else:
                    continue
                if lhs != rhs:
                    bad.append((n, d, h[:n], lhs, rhs))
                    if len(bad) >= 5:
                        return bad
    return bad


def check_subst(n_hi, trials, rng):
    """Check T(2n,2d)=T(n,d), T(2n,2d+1)==0, T(2n+1,2d)=T(n,d),
    T(2n+1,2d+1)=T(n,d).  The LHS reads h up to index 2n-1, the RHS reads h
    up to n-1.  We give the LHS a fresh h (length 2n) and reuse its first n
    entries for the RHS (so the RHS window is the left half).  This checks
    whether the claim holds 'along the dyadic path' as the same h is extended
    by the substitution.  Honest test: any mismatch is a refutation of the
    claim as a constraint on extension."""
    bad = []
    for n in range(2, n_hi + 1):
        for _ in range(trials):
            h = [rng.randint(0, 1) for _ in range(2 * n)]
            hn = h[:n]
            for d in range(0, n):
                # d range: cells need d inside [:,], for T(n,d) d<n
                got = {}
                if 2 * d < 2 * n:
                    got['T(2n,2d)'] = t(2 * n, 2 * d, h)
                if 2 * d + 1 < 2 * n:
                    got['T(2n,2d+1)'] = t(2 * n, 2 * d + 1, h)
                if 2 * d < 2 * n + 1:
                    got['T(2n+1,2d)'] = t(2 * n + 1, 2 * d, h)
                if 2 * d + 1 < 2 * n + 1:
                    got['T(2n+1,2d+1)'] = t(2 * n + 1, 2 * d + 1, h)
                ref = t(n, d, hn)
                # T(2n,2d) vs T(n,d)
                if 2 * d < 2 * n and got['T(2n,2d)'] != ref:
                    bad.append(('T(2n,2d)=T(n,d)', n, d, h, got['T(2n,2d)'], ref))
                if 2 * d + 1 < 2 * n and got['T(2n,2d+1)'] != 0:
                    bad.append(('T(2n,2d+1)=0', n, d, h, got['T(2n,2d+1)'], 0))
                if 2 * d < 2 * n + 1 and got['T(2n+1,2d)'] != ref:
                    bad.append(('T(2n+1,2d)=T(n,d)', n, d, h, got['T(2n+1,2d)'], ref))
                if 2 * d + 1 < 2 * n + 1 and got['T(2n+1,2d+1)'] != ref:
                    bad.append(('T(2n+1,2d+1)=T(n,d)', n, d, h, got['T(2n+1,2d+1)'], ref))
            if bad:
                return bad
    return bad


def run():
    rng = random.Random(12345)
    print("=== Claim 1: abel-boundary-recurrence  T(n,d)==T(n-1,d)^T(n-1,d-1) ===")
    for trial_mult in (5, 20):
        bad = check_abel(40, trial_mult, rng)
        if bad:
            print(f"  REFUTED (trials={trial_mult}): first bad = {bad[0]}")
            break
        else:
            print(f"  no counterexample, n=3..40, {trial_mult} random h per n")
    print()
    print("=== Claim 2: substitution-incidence-perron ===")
    bad = check_subst(12, 500, rng)
    if bad:
        print(f"  REFUTED: first bad = {bad[0]}")
    else:
        print("  no counterexample, n=2..12, 500 random h per n")
    print()
    # structured controls
    print("=== structured controls for claim 1 (abel) ===")
    for name, gen in [("all-ones", lambda n: [1]*n),
                      ("powers-of-two", lambda n: [1 if (i & (i-1)) == 0 and i > 0 else 0 for i in range(n)]),
                      ("thue-morse", lambda n: [bin(i).count('1') % 2 for i in range(n)])]:
        bad = []
        for n in range(3, 60):
            h = gen(n)
            for d in range(2, n):
                if d <= n - 2:
                    if t(n, d, h) != t(n-1, d, h[:n-1]) ^ t(n-1, d-1, h[:n-1]):
                        bad.append((n, d))
                        break
            if bad:
                break
        print(f"  {name}: {'REFUTED first bad ' + str(bad[0]) if bad else 'no counterexample n=3..60'}")


if __name__ == "__main__":
    run()
