"""PE1006 pattern hunt: count of length-k factors by weight (# of 1s).

For a Sturmian word the set of length-k factors has a well-studied weight
distribution: among the k+1 factors the weights take exactly two values,
floor(k*r) and ceil(k*r) (there are b-1 factors of weight a and ... , by
balance: the distinct factors differ by at most one 1).  Specifically for
slope r = 1/phi (fibonacci word), number of 1s in any length-k factor is
either floor(k/phi) or ceil(k/phi), and the counts are governed by the
leading-position offset.

This program enumerates the exact factor set for small k and tabulates:
  weight w -> #factors with weight w.
Conjecture from balance: weights are floor(k/phi^2) and ceil(k/phi^2)? No --
the density of 1s in the Fibonacci word is 1/phi^2 ~ 0.382, so a length-k
factor has ~ k/phi^2 ones; by Sturmian balance each length-k factor has
either floor(k/phi^2) or ceil(k/phi^2) ones.  Let's verify.
"""

from collections import Counter


def fib_prefix(L):
    a, b = '0', '01'
    while len(b) < L:
        a, b = b, b + a
    return b


def main():
    KMAX = 30
    W = fib_prefix(3 * KMAX + 10)
    from decimal import Decimal, getcontext
    getcontext().prec = 40
    PHI2 = (Decimal(3) - Decimal(5).sqrt()) / 2
    print("k : weight_count ; floor(k/phi^2),ceil(k/phi^2)")
    for k in range(1, KMAX + 1):
        facs = {W[i:i + k] for i in range(len(W) - k + 1)}
        assert len(facs) == k + 1
        wc = Counter(f.count('1') for f in facs)
        lo = int(Decimal(k) * PHI2)
        hi = lo + 1
        weights = sorted(wc)
        plausible = weights == [lo, hi] or weights == [lo] or weights == [hi]
        print(f"k={k:2d} {dict(wc)}  expect {lo},{hi}  fit={plausible}")


if __name__ == '__main__':
    main()