"""COLLAPSE core objects: the fold matrix Phi_n and its row down-sets M_d.

Single canonical implementation of the objects GOAL.md names:
  M_d       -- the set { n-1-d+o : o binary submask of d }  (a principal down-set)
  downset_d -- M_d as a frozenset of absolute positions in [0, n-1]
  fold_row  -- indicator row d of Phi_n
  S(n,h)    -- signed excess (n-2) - 2*w(h)
  S2        -- S(n,h)**2 as a sum over d,d' of (-1)^{XOR over M_d △ M_d' of h}

Everything uses exact integers / bitsets. The canonical S(n,h) is
cross-checked against a brute-force submask enumeration in the runner.
"""

from functools import lru_cache


def submasks(d):
    """All binary submasks o of nonnegative integer d (o & d == o)."""
    o = d
    while True:
        yield o
        if o == 0:
            break
        o = (o - 1) & d


def downset(d, n):
    """M_d = { n-1-d+o : o submask of d }, as a frozenset of positions in [0,n-1]."""
    return frozenset(n - 1 - d + o for o in submasks(d))


def fold_row(d, n):
    """Indicator vector of M_d: list over positions j in 0..n-1 (bit j = membership)."""
    s = downset(d, n)
    return [1 if j in s else 0 for j in range(n)]


def fold_row_brute(d, n):
    """Independent derivation via C(d, j-(n-1-d)) mod 2 (imported result / Lucas)."""
    from math import comb
    return [comb(d, j - (n - 1 - d)) % 2 if 0 <= j - (n - 1 - d) <= d else 0
            for j in range(n)]


def T(n, d, h):
    """Fold cell: XOR over i in M_d of h[i]. h is a bitset (int) or 0/1 list."""
    if isinstance(h, int):
        return sum(((h >> i) & 1) for i in downset(d, n)) % 2
    return sum(h[i] for i in downset(d, n)) % 2


def S(n, h):
    """Signed excess S(n,h) = (n-2) - 2*w(h). h is 0/1 list (length n)."""
    w = sum(T(n, d, h) for d in range(2, n))
    return (n - 2) - 2 * w


def S2(n, h):
    """S(n,h)^2, the second-moment functional whose collapse is in question."""
    s = S(n, h)
    return s * s


def S2_char(n):
    """The S(n,h)^2 index multiset: dict {frozenset A : multiplicity} over
    A = M_d △ M_{d'}, d,d' in [2, n-1].  A is stored as a frozenset of absolute
    positions. This is GOAL priority 1's object."""
    from collections import Counter
    ms = {d: downset(d, n) for d in range(2, n)}
    c = Counter()
    for d in range(2, n):
        for dp in range(2, n):
            c[frozenset(ms[d] ^ ms[dp])] += 1
    return c


def run_count(A):
    """Number of maximal runs of consecutive integers in frozenset A (positions are ints)."""
    if not A:
        return 0
    s = sorted(A)
    runs = 1
    for a, b in zip(s, s[1:]):
        if b != a + 1:
            runs += 1
    return runs
