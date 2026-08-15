"""Hypercube combinatorial helpers: adjacency, internal degrees.

Vertices are integers 0..2^n-1 (their bit strings). Two vertices u, v are
adjacent iff they differ in exactly one coordinate, i.e. (u ^ v) is a power
of two. All arithmetic is exact integer.
"""


def popcount(x):
    """Exact integer popcount."""
    return bin(x).count("1")


def is_edge(u, v):
    """True iff u and v are distinct and differ in exactly one bit."""
    if u == v:
        return False
    d = u ^ v
    return d & (d - 1) == 0


def internal_degree_distribution(n, S):
    """{degree: #vertices of S with that many neighbours inside S}.

    S is an iterable of ints in 0..2^n-1. Exact integers throughout.
    """
    S = sorted(set(S))
    N = 1 << n
    assert all(0 <= v < N for v in S)
    spos = set(S)
    counts = {}
    for v in S:
        d = 0
        for k in range(n):
            if (v ^ (1 << k)) in spos:
                d += 1
        counts[d] = counts.get(d, 0) + 1
    return counts


def max_internal_degree(n, S):
    """Maximum internal degree of vertices of S in Q_n[S]; -1 if S empty."""
    dist = internal_degree_distribution(n, S)
    return max(dist.keys()) if dist else -1
