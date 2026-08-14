"""Explore the interval geometry behind C(j,l;k).

Prior work established each column i (position i of length-k factors) is a
circular interval of ones on the (k+1)-circle: a contiguous run of N(i) rows.
C(j,l;k) = #factors with a 1 at both positions j and l = |interval_j ∩ interval_l|.

Here we recover (s(i), N(i)) for every column, then test whether C(j,l) is
determined by the circular distance between interval starts:
    C(j,l) ?= max(0, N(j)+N(l) - n - something) or a piecewise form.

Precise goals:
  - does C(j,l) depend only on the circular gap between s(j) and s(l)?
  - find the function f(d) with C = f(circular_distance(start_j, start_l)).
Exact integers. The circle has size n = k+1.
"""
import json, os
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
STRUCT = os.path.join(HERE, "..", "out", "structure.json")


def load():
    return json.load(open(STRUCT))


def circ_interval(bits):
    """Return (start, length) of the circular interval of ones on an n-cycle."""
    n = len(bits)
    ones = [j for j, b in enumerate(bits) if b == 1]
    if not ones:
        return None, 0
    if len(ones) == n:
        return 0, n
    z0 = next(j for j, b in enumerate(bits) if b == 0)
    start = None
    L = 0
    j = (z0 + 1) % n
    seen = 0
    while seen < n:
        if bits[j] == 1:
            if start is None:
                start = j
            L += 1
        else:
            if start is not None:
                break
        seen += 1
        j = (j + 1) % n
    return start, L


def circle_dist(a, b, n):
    return min((a - b) % n, (b - a) % n)


def main():
    data = load()
    for k in [6, 8, 10, 14, 20, 34, 55]:
        d = data[str(k)]
        facs = d["factors"]
        n = k + 1
        cmat = d["C"]
        # recover column bits
        cols = []
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            cols.append(bits)
            # sanity: reconstruct C(j,l) from columns
        ok = True
        for j in range(k):
            for l in range(j, k):
                val = sum(1 for f in facs if f[j] == '1' and f[l] == '1')
                if val != int(cmat[f"{j},{l}"]):
                    ok = False
        print(f"k={k}: C reconstructed from columns: {ok}")

        starts = []
        Ns = []
        for i in range(k):
            s, L = circ_interval(cols[i])
            starts.append(s)
            Ns.append(L)

        # Test: does C(j,l) depend only on circular distance between s(j),s(l)?
        print(f"  N(i) values: {sorted(set(Ns))}")
        bins = defaultdict(set)   # (gap) -> set of C values observed
        for j in range(k):
            for l in range(j, k):
                gap = circle_dist(starts[j], starts[l], n)
                c = int(cmat[f"{j},{l}"])
                bins[gap].add(c)
        multi = {g: v for g, v in bins.items() if len(v) > 1}
        print(f"  distinct C vs circular-gap(interval-start): gaps with >1 C value = {len(multi)}")
        if multi:
            sample = list(multi.items())[:3]
            for g, v in sample:
                print(f"     gap={g}: C values {sorted(v)}")
        # show the function C(gap) if single-valued
        if not multi:
            fn = {g: sorted(v)[0] for g, v in sorted(bins.items())}
            print(f"  C as function of circular gap (start-to-start): {fn}")


if __name__ == "__main__":
    main()
