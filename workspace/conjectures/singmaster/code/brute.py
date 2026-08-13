"""Naive oracle for Singmaster's conjecture.

Counts N(a) = #{ (n,k) : 0 <= k <= n, C(n,k) = a } by direct enumeration.

Convention (matches code/out/witnesses.json): counts BOTH mirrored occurrences
(C(n,k) and C(n,n-k) are two distinct pairs) and includes the trivial pair
C(a,1)=C(a,a-1).  So an `a` that appears once nontrivially reports N(a)=4.

Obviously correct rather than fast: it builds no triangle and inverts nothing,
it just evaluates C(n,k) exactly for every (n,k) with n <= n_max and counts.
Exact integer arithmetic throughout (math.comb).

The only wrinkle is choosing n_max.  For a full N(a) you need n up to a (the
trivial pair C(a,1) sits at n = a).  This routine also returns the matching
occurrences so the statement's worked examples can be compared directly.
"""

from math import comb


def occurrences(a, n_max):
    """Return the list [(n,k)] of all pairs with 0<=k<=n<=n_max and C(n,k)==a."""
    hits = []
    for n in range(0, n_max + 1):
        for k in range(0, n + 1):
            if comb(n, k) == a:
                hits.append((n, k))
    return hits


def multiplicity(a, n_max):
    """N(a) counted over all 0<=k<=n<=n_max."""
    return len(occurrences(a, n_max))


if __name__ == "__main__":
    # Split each nontrivial (n,k) pair into its two mirrored occurrences, and
    # add the trivial pair C(a,1)=C(a,a-1).  Matches the witness JSON record.
    witness_a = [3003, 120, 210, 1540, 7140, 11628, 24310]

    for a in witness_a:
        occ = occurrences(a, n_max=a)
        nontriv = sorted({(min(n, k), max(n, k)) for (n, k) in occ
                          if (n, k) not in ((a, 1), (a, a - 1))})
        N = multiplicity(a, n_max=a)
        print(f"a={a}: N(a)={N}")
        print(f"   occurrences={sorted(occ)}")
        print(f"   nontrivial (n,k) pairs k<=n/2 = {nontriv}")
        print()

    # The specific record-breaking identity from the statement.
    print("Statement identity 3003 = C(3003,1) = C(78,2) = C(15,5) = C(14,6):")
    for (n, k) in [(3003, 1), (78, 2), (15, 5), (14, 6), (3003, 3002),
                   (78, 76), (15, 10), (14, 8)]:
        print(f"   C({n},{k}) = {comb(n, k)}")
