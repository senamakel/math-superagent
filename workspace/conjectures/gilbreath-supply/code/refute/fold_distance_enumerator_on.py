#!/usr/bin/env python3
"""Adversarial check of the adopted approach's geometry crux.

Claim fold-distance-enumerator-On (research/ROOT.md): for the row code
C_n = { M_d : d in [2,n-1] }, M_d = { n-1-d+o : o subseteq d },
    F_n(z) = sum_{d,d'} z^{|M_d XOR M_{d'}|}  = O(n)   as n -> oo,
uniformly for every fixed |z| < 1.  Its own stated falsifier (in
fold-second-moment-krawtchouk.md) is A_2 = Theta(n^2), which would make
F_n(z) carry a z^2 n^2 term and kill (C).

We compute, EXACTLY, the distance distribution A_k of the row code and the
enumerator F_n(z) at several |z|<1, for n up to a few thousand, and report
F_n(z)/n and A_2 as functions of n.

dist(d,d') = |M_d XOR M_{d'}| = 2^pc(d) + 2^pc(d') - 2^{pc(d&d')+1}  (Lucas:
one element per submask; the intersection of the translated down-sets has
size 2^{pc(d&d')}, claim downset-row-intersection-meet-formula).

Exact integer arithmetic.  Declared cost: O(n^2) pair enumeration, kept to
n <= 4000 so this stays small (it is the oracle for the O(n) claim).
complexity_class: quadratic (oracle for an O(n) claim), oracle_bound: n<=4000
"""

from fractions import Fraction


def pc(x):
    return x.bit_count()


def dist(d, a):
    return (1 << pc(d)) + (1 << pc(a)) - (1 << (pc(d & a) + 1))


def F_n(n):
    """Return A_2 count, F_n(1/2), F_n(3/4), F_n(1/8), and ratio to n.
    F_n/half = n-2 + sum_{d<a} 2 z^{dist} .  z in {1/2, 3/4, 1/8}."""
    from fractions import Fraction
    zs = {Fraction(1, 2): Fraction(0), Fraction(3, 4): Fraction(0),
          Fraction(1, 8): Fraction(0)}
    A2 = 0
    pairs = 0
    rows = list(range(2, n))
    for i in range(len(rows)):
        d = rows[i]
        for j in range(i + 1, len(rows)):
            a = rows[j]
            dd = dist(d, a)
            if dd == 2:
                A2 += 1
            for z in zs:
                zs[z] += 2 * (z ** dd)
            pairs += 1
    diag = len(rows)  # n-2 diagonal terms of z^0
    out = {}
    for z in zs:
        out[z] = diag + zs[z]
    return A2, out, pairs


def main():
    print(f"{'n':>6} {'A_2':>8} {'A2/n':>8} {'F(1/2)/n':>10} "
          f"{'F(3/4)/n':>10} {'F(1/8)/n':>10}")
    for n in [16, 32, 64, 128, 256, 512, 1024, 2048, 4096]:
        A2, out, pairs = F_n(n)
        print(f"{n:>6} {A2:>8} {A2/n:>8.3f} "
              f"{float(out[Fraction(1,2)]/n):>10.3f} "
              f"{float(out[Fraction(3,4)]/n):>10.3f} "
              f"{float(out[Fraction(1,8)]/n):>10.3f}")
    # also the theoretically predicted bound rows with distinct popcounts
    print("\n(pairs enumerated exactly; n=4096 is ~8.4M pairs, fine)")


if __name__ == "__main__":
    main()
