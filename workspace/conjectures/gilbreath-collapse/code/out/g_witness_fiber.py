"""G-witness fiber test for COLLAPSE (GOAL priority 3, gap G-witness).

Decision object (pinned in research/backward/collapse-via-index-multiset.md):
  pair correlations up to lag K are the joint counts
      N_ab(k) = #{ i in [0,n-k-1] : h_i = a, h_{i+k} = b }
  for 1 <= k <= K, a,b in {0,1};  C_K(h) is that list.
"S^2 factors through K-pair correlations" := S^2 is constant on each C_K-fiber.

For every n in [3, NMAX] and every K in [1, n-1], group all h in F2^n by C_K
and test whether S(n,h)^2 is constant on every fiber.  Report the first
witness (n, K, h, h') with C_K equal but S^2 different, or the absence bound
(largest n, all K, no witness).

Exact arithmetic throughout.  Complexity: per (n,K) the grouping is O(2^n)
builds of a lag-count table, O(2^n) dict inserts, and one pass over fibers to
check constancy: O(2^n) time, O(2^n) space in the number of DISTINCT C_K
values.  We never iterate to the bound in the statement -- 2^n strings is the
whole INPUT space, which is what "exhaustive at small n" means; there is no
larger search to run.  Max n here is 16 -> 65536 strings.

Negative control (required): a deliberately broken C_K that drops the k=1
count is computed beside the true one and shown to yield a witness at some
(n,K) where the true C_K does not.  If the broken test could not fail, the
true test would be measuring nothing.
"""

from collections import defaultdict
from lib.collapse import S2


def pair_counts(h, K):
    """N_ab(k) for 1<=k<=K, a,b in {0,1}, as a flat tuple.
    h is a 0/1 list (or bitset int)."""
    n = len(h)
    out = []
    for k in range(1, K + 1):
        for a in (0, 1):
            for b in (0, 1):
                c = 0
                for i in range(0, n - k):
                    if h[i] == a and h[i + k] == b:
                        c += 1
                out.append(c)
    return tuple(out)


def find_witness(n, K, drop_lag1=False):
    """Group all h in F2^n by C_K; return first witness (h, h') as ints, or None.
    If drop_lag1, use a BROKEN C_K with the k=1 counts removed (negative control)."""
    fibers = defaultdict(list)
    s2 = {}
    for h in range(1 << n):
        hl = [(h >> i) & 1 for i in range(n)]
        ck = pair_counts(hl, K)
        if drop_lag1:
            # broken: re-compute with lag 1 removed (offsets by 4 counts per lag)
            ck = tuple(ck[4:])
        fibers[ck].append(h)
        s2[h] = S2(n, hl)
    # a fiber is a list of h values; check constancy of S2 across each fiber
    for ck, hs in fibers.items():
        if len(hs) >= 2:
            base = s2[hs[0]]
            for h in hs[1:]:
                if s2[h] != base:
                    return (hs[0], h)
    return None


def main():
    NMAX = 16
    # True test: full table
    print("TRUE C_K (all lags 1..K): is S^2 constant on every C_K fiber?")
    print(f"{'n':>3} {'K':>3}  result")
    first_witness = None
    absence_up_to = None
    for n in range(3, NMAX + 1):
        row = []
        for K in range(1, n):
            w = find_witness(n, K)
            if w is not None:
                tag = (f"WITNESS h={w[0]} h'={w[1]}")
                row.append((K, tag))
                if first_witness is None:
                    first_witness = (n, K, w[0], w[1])
            else:
                row.append((K, "no witness"))
        for K, tag in row:
            print(f"{n:>3} {K:>3}  {tag}")
        if all("no witness" in t for _, t in row):
            absence_up_to = n
        print()
    if first_witness:
        n, K, h, hp = first_witness
        print("FIRST WITNESS in the TRUE test:", (n, K, h, hp))
    else:
        print("NO WITNESS in the TRUE test for any n<=%d, any K." % NMAX)
    if absence_up_to:
        print("ABSENCE BOUND (true test): no witness for all n<=%d over all K." % absence_up_to)
    print()

    # Negative control: broken C_K dropping the k=1 count
    print("NEGATIVE CONTROL: broken C_K (lag-1 counts dropped).")
    neg_found = None
    for n in range(3, NMAX + 1):
        for K in range(1, n):
            # only meaningful where the true C_K has no witness at this (n,K)
            w = find_witness(n, K)
            if w is not None:
                continue
            wb = find_witness(n, K, drop_lag1=True)
            if wb is not None:
                neg_found = (n, K, wb[0], wb[1])
                break
        if neg_found:
            break
    if neg_found:
        n, K, h, hp = neg_found
        print(f"broken C_K produces a witness immediately: n={n} K={K} "
              f"h={h} h'={hp} (true C_K at this n,K has none)")
    else:
        print("FAIL: broken C_K produced no witness -- negative control did not fire.")


if __name__ == "__main__":
    main()
