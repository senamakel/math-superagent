"""Scholar verification of the three new library sources' central checkable claims.

1. Liu-Zhou 2022: plain adjacency spectrum of Q_d is {d-2i : i=0..d} with mult C(d,i).
2. Barber 2012: the maximum independent sets of Q_n are exactly the two parity classes
   (even/odd weight), each of size 2^{n-1}; a brute-force confirmation over all
   independent sets for small n.
3. Ellis 2011 edge-isoperimetric extremal: among subsets of {0,1}^n of a given size,
   edge boundary is minimised by subcubes -- spot-checked against other shapes for
   small n (this confirms the extremal-family claim, not the quantitative stability).

Kept to small n so the independent-set search stays polynomial-subset-size feasible.
"""
import itertools, math
import numpy as np

def plain_spectrum_ok(n):
    N = 2**n
    # adjacency of Q_n
    A = np.zeros((N, N))
    for x in range(N):
        for i in range(n):
            y = x ^ (1 << i)
            A[x, y] = 1.0
    vals = np.linalg.eigvalsh(A)
    # sort, group by distinct integer value
    from collections import Counter
    c = Counter(round(v, 6) for v in vals)
    # expected: value d-2i with multiplicity C(d,i)
    expected = {}
    for i in range(n + 1):
        expected[n - 2*i] = math.comb(n, i)
    got = {}
    for k in c:
        got[k] = c[k]
    return got == {float(k): v for k, v in expected.items()}, got, expected

def max_independent_sets_are_parity(n):
    N = 2**n
    edges = []
    for x in range(N):
        for i in range(n):
            y = x ^ (1 << i)
            if y > x:
                edges.append((x, y))
    adj = {x: set() for x in range(N)}
    for a, b in edges:
        adj[a].add(b); adj[b].add(a)
    # brute force all independent sets (small n only)
    best_size = 0
    nonparity_maximal = []
    for r in range(N + 1):
        for S in itertools.combinations(range(N), r):
            S = set(S)
            ind = all(b not in adj[a] for a in S for b in S if b != a)
            if ind:
                # parity check
                ev = {x for x in S if bin(x).count('1') % 2 == 0}
                od = S - ev
                if len(S) > best_size:
                    best_size = len(S)
                    nonparity_maximal = [] if (len(ev) == len(S) or len(od) == len(S)) else [S]
                elif len(S) == best_size and not (len(ev) == len(S) or len(od) == len(S)):
                    nonparity_maximal.append(S)
    return best_size, 2**(n-1), nonparity_maximal

def subcube_minimizes_edge_boundary(n, m):
    """Check whether a subcube of size m minimises the edge boundary among all
    size-m subsets (Ellis: edge-isoperimetric extremal families are subcubes).
    """
    N = 2**n
    def boundary(S):
        S = set(S)
        b = 0
        for x in S:
            for i in range(n):
                y = x ^ (1 << i)
                if y not in S:
                    b += 1
        return b
    # find a subcube of size m: fix n - log2(m) coordinates
    k = n - int(round(math.log2(m)))
    if 2**k != m:
        return None
    best = None
    for S in itertools.combinations(range(N), m):
        b = boundary(S)
        if best is None or b < best:
            best = b
    # build one subcube: all vertices with last k bits free, first n-k fixed to 0
    subcube = set()
    for free in range(2**k):
        subcube.add(free)  # fixed bits = 0 (first n-k), free = last k
    bsub = boundary(subcube)
    return best, bsub, best == bsub

print("=== Liu-Zhou plain adjacency spectrum of Q_d ===")
for n in range(2, 8):
    ok, got, exp = plain_spectrum_ok(n)
    print(f"  n={n}: spectrum == {{d-2i mult C(d,i)}} : {ok}")
    if not ok:
        print("     got", got, "exp", {int(k): v for k, v in exp.items()})

print("\n=== Barber: max independent sets of Q_n are the parity classes ===")
for n in range(2, 5):
    best, expected, nonparity = max_independent_sets_are_parity(n)
    print(f"  n={n}: best independent size={best} (expect {expected}), "
          f"non-parity maximum sets found: {len(nonparity)}")

print("\n=== Ellis: subcube minimises edge boundary among size-m subsets ===")
for n, m in [(3, 4), (3, 2), (4, 4), (4, 8)]:
    res = subcube_minimizes_edge_boundary(n, m)
    if res is None:
        print(f"  n={n} m={m}: not a subcube-size, skip")
    else:
        best, bsub, equal = res
        print(f"  n={n} m={m}: global-min-boundary={best}, subcube-boundary={bsub}, subcube-is-extremal={equal}")
