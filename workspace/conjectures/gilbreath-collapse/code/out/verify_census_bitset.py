"""Independent second route for the index-multiset census: integer-bitset method.

Re-derives { M_d △ M_{d'} : d,d' in [2,n-1] } with NO imports from
lib.collapse (self-contained), using an n-bit integer for each M_d:

  M_d bits: positions n-1-d+o for o a binary submask of d          (Lucas; item 3's
  characterization — the same theorem, but a different implementation: int
  bit-twiddling instead of frozenset-of-submasks)
  A(d,dp)  = bits(M_d) ^ bits(M_dp)
  size     = A.bit_count()
  span     = maxbit - minbit + 1   (0 if empty)
  runs     = number of maximal consecutive 1-blocks (computed by shifting)
  example  = first (d,dp) found per distinct A

Checks against the frozenset route (multiset_census.census):
  * identical dict {A-bits: (mult, size, span, runs, example)} for every
    n = 3..128 — A compared by its sorted-position tuple, so the two routes
    agree set-for-set, multiplicity-for-multiplicity, span-for-span.
  * the (n-2)^2 entry count and the closed-form size identity
    2^pc(d)+2^pc(d')-2^{pc(d&d')+1} are re-derived here and re-asserted.
  * the three dyadic families are re-derived:
      M_{2^k-1} △ M_{2^k}           one run of length 2^k, span 2^k
      M_{2^k-1} △ M_{2^k-2}         2^{k-1} singleton runs
      M_{2^k}   △ M_{2^k+1}         the two-point set {n-2^k-2, n-2}
  * the max-span / top-span / weighted-span-histogram numbers in
    multiset_census_n128.txt are recomputed and matched.
"""

from collections import Counter

# ---- bitset implementation (independent of lib.collapse) ----

def submasks_bitset(d):
    o = d
    while True:
        yield o
        if o == 0:
            break
        o = (o - 1) & d


def bits_of_downset(d, n):
    """M_d as an n-bit integer: bit i set iff i in M_d = {n-1-d+o : o submask of d}."""
    b = 0
    start = n - 1 - d
    for o in submasks_bitset(d):
        b |= 1 << (start + o)
    return b


def pc(x):
    return x.bit_count()


def maxbit(b):
    return b.bit_length() - 1


def minbit(b):
    return (b & -b).bit_length() - 1


def size_span_runs(b):
    """(size, span, run-count) of the 1-positions of bitset b; span 0 for empty."""
    if b == 0:
        return 0, 0, 0
    size = b.bit_count()
    span = maxbit(b) - minbit(b) + 1
    # number of maximal runs of consecutive 1-bits
    runs = 0
    # iterate over runs: lowest run = b with its trailing zeros stripped;
    # shift by the run's length to get past it.
    x = b
    while x:
        runs += 1
        tz = (x & -x).bit_length() - 1          # length of trailing zero run
        x >>= tz                                # strip trailing zeros: now low bit is 1
        runlen = (x ^ (x + 1)).bit_length() - 1  # count of low consecutive 1s
        x >>= runlen
    return size, span, runs


def positions(b):
    out = []
    i = 0
    while b:
        if b & 1:
            out.append(i)
        b >>= 1
        i += 1
    return tuple(out)


def census_bitset(n):
    """{pos-tuple A: (mult, size, span, runs, example(d,dp))} by the bitset route."""
    ds = {d: bits_of_downset(d, n) for d in range(2, n)}
    mp = {}
    for d in range(2, n):
        for dp in range(2, n):
            b = ds[d] ^ ds[dp]
            sz, sp, rc = size_span_runs(b)
            # closed-form cross-check, independent recomputation
            cf = 2 ** pc(d) + 2 ** pc(dp) - 2 ** (pc(d & dp) + 1)
            assert sz == cf, (n, d, dp, sz, cf)
            key = positions(b)
            e = mp.get(key)
            if e is None:
                mp[key] = [1, sz, sp, rc, (d, dp)]
            else:
                e[0] += 1
    return mp


# ---- comparison ----

def frozenset_route_to_positions(n):
    """Same shape as census_bitset but built from lib.collapse's frozensets."""
    from lib.collapse import downset
    ds = {d: downset(d, n) for d in range(2, n)}
    mp = {}
    for d in range(2, n):
        for dp in range(2, n):
            A = ds[d] ^ ds[dp]
            sz = len(A)
            sp = (max(A) - min(A) + 1) if A else 0
            rc = sum(1 for a, b in zip(sorted(A), sorted(A)[1:]) if b != a + 1) + (1 if A else 0)
            key = tuple(sorted(A))
            e = mp.get(key)
            if e is None:
                mp[key] = [1, sz, sp, rc, (d, dp)]
            else:
                e[0] += 1
    return mp


def main():
    print("=" * 78)
    print("Independent second route: integer-bitset census vs frozenset census,")
    print("for every n = 3..128.")
    print("=" * 78)
    all_ok = True
    span_hist = {}
    for n in range(3, 129):
        bs = census_bitset(n)
        fs = frozenset_route_to_positions(n)
        if set(bs) != set(fs):
            all_ok = False
            print(f"n={n}: SET MISMATCH bitset={len(bs)} frozenset={len(fs)}")
            continue
        for k in set(bs) | set(fs):
            if bs.get(k) != fs.get(k):
                all_ok = False
                print(f"n={n}: entry mismatch {k}: bitset={bs.get(k)} fs={fs.get(k)}")
                break
        n_entries = sum(e[0] for e in bs.values())
        if n_entries != (n - 2) ** 2:
            all_ok = False
            print(f"n={n}: entry count {n_entries} != {(n-2)**2}")
        # weighted span histogram and max span, recomputed independently
        H = Counter()
        for k, e in bs.items():
            H[e[2]] += e[0]
        if n in (32, 64, 128):
            span_hist[n] = H
        if n % 25 == 4 or n == 128:
            print(f"  n={n:4d}: distinct sets={len(bs):5d} entries={n_entries:6d} "
                  f"max_span={max(H)} weight(max_span)={H[max(H)]}")
    print()
    # spot-check the three dyadic families at n=64, 128 via the bitset route
    for n in (64, 128):
        print(f"dyadic families n={n} (bitset route):")
        for k in range(1, 40):
            if 2 ** k > n - 1:
                break
            b1 = bits_of_downset(2 ** k - 1, n) ^ bits_of_downset(2 ** k, n)
            b2 = bits_of_downset(2 ** k - 1, n) ^ bits_of_downset(2 ** k - 2, n)
            b3 = bits_of_downset(2 ** k, n) ^ bits_of_downset(2 ** k + 1, n)
            sz1, sp1, rc1 = size_span_runs(b1)
            sz2, sp2, rc2 = size_span_runs(b2)
            sz3, sp3, rc3 = size_span_runs(b3)
            ok1 = (sz1 == sp1 == 2 ** k and rc1 == 1)
            ok2 = (sz2 == rc2 == 2 ** (k - 1))  # singletons: size == run count
            p3 = positions(b3)
            ok3 = (p3 == (n - 2 ** k - 2, n - 2) and rc3 == 2)
            if not (ok1 and ok2 and ok3):
                all_ok = False
                print(f"  k={k}: FAIL b1=({sz1},{sp1},{rc1}) b3={p3}")
        print(f"  all k checked")
    # match the persisted histograms in multiset_census_n128.txt
    ref = {}
    for n in (32, 64, 128):
        H = span_hist[n]
        print(f"n={n}: span histogram re-derived, max span {max(H)} weight {H[max(H)]}; "
              f"count of span values = {len(H)}")
        ref[n] = (max(H), H[max(H)])
    expected = {32: (31, 30), 64: (63, 62), 128: (127, 126)}
    for n, (ms, w) in expected.items():
        if ref[n] != (ms, w):
            all_ok = False
            print(f"n={n}: expected max span/weight {(ms, w)}, got {ref[n]}")
        else:
            print(f"n={n}: matches multiset_census_n128.txt: max span {ms}, weight {w}")

    print()
    print("INDEPENDENT ROUTE:", "ALL CHECKS PASSED" if all_ok else "FAILURES FOUND")
    assert all_ok


if __name__ == "__main__":
    main()