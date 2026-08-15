#!/usr/bin/env python3
"""Falsification oracle for the dyadic ODD-FACTOR CONVERSE.

NOT EXECUTED in the scholar session (no shell tool): this file is a self-
contained oracle drafted for the tool_builder to run. It is NOT evidence.

Claim under attack (the open half of the dyadic dichotomy, currently only
'conjectured'):
    For h periodic of period P whose minimal period has an odd part o > 1,
    and h non-constant, the supply density nu2(q_n)/n is bounded below by a
    positive constant c(P) > 0.  ("non-constant odd-factor period --> nu2 >= c*n")

Mechanism (this run's proved fold): tail cell at encoder index d is
    a_d = (sigma^d h)_0,   sigma = I + S on the cyclic F2-vector of length P.

Test: for every NON-CONSTANT word h of length P (P in {3,5,7,9,15}, plus
powers-of-two {2,4,8} as the collapsing control), compute the asymptotic
density of a_d=1 over d=1..m for large m, and record the MINIMUM over h.
If that minimum tends to 0 for some P with an odd factor, the converse dies.

Exact integer / F2 arithmetic only.  O(2^P * m) — for P<=15, 32768 words.



def word_is_nonconstant(h):
    return any(b == 1 for b in h) and any(b == 0 for b in h)


def sigma_step(v, P):
    """(I+S)v[c] = v[c] ^ v[(c+1) mod P]."""
    return [v[c] ^ v[(c + 1) % P] for c in range(P)]


def densities_for_period(P, m):
    """Return (min_density_nonconstant, list_of_worst_words) over all
    non-constant words of length P, using the fold formula a_d=(sigma^d h)_0."""
    min_dens = None
    worst = []
    for bits in range(1, (1 << P) - 1):  # skip all-0 (0) and all-1 (2^P-1) as constant
        h = [(bits >> c) & 1 for c in range(P)]
        # iterate sigma^d h, count v[0]==1 for d=1..m
        v = h[:]
        cnt = 0
        for d in range(1, m + 1):
            v = sigma_step(v, P)
            cnt += v[0]
        dens = cnt / m
        if min_dens is None or dens < min_dens:
            min_dens = dens
            worst = [(bits, dens, cnt)]
        elif abs(dens - min_dens) < 1e-12:
            worst.append((bits, dens, cnt))
    return min_dens, worst


def main():
    print("Odd-factor converse falsifier: min over non-constant words of period P")
    print("of density(a_d==1, d=1..m).  If min -> 0, converse dead; if positive, holds here.")
    print("=" * 74)
    m = 20000
    print("m =", m)
    for P in [2, 3, 4, 5, 7, 8, 9, 15]:
        md, worst = densities_for_period(P, m)
        label = "POWER OF 2 (control, collapse expected)" if P in (2, 4, 8) else "odd factor"
        print(f"  P={P:2d} [{label:38s}] min density = {md:.6f}  "
              f"worst word bits={worst[0][0]} (of 2^{P}-2)  count={worst[0][2]}")
    print("=" * 74)


if __name__ == "__main__":
    main()
