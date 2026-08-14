"""Naive oracle for f(n) on the hypercube Q_n.

f(n) = min { D(S) : S subset of {0,1}^n, |S| = 2^{n-1} + 1 }

where D(S) is the maximum internal degree of Q_n[S] (largest number of
neighbours any vertex of S has *inside* S).

This file is the deliberately-naive, obviously-correct checker (oracle). It
enumerates subsets of {0,1}^n of the required size and measures each one
directly. It is exact integer arithmetic throughout; it is NOT fast and is
intended only to pin down the definition at small n and to validate the
fast/solver methods built against it. The search space is doubly exponential,
so this is strictly a small-n tool.

Functions
---------
internal_degree_distribution(n, S)
    Given a subset S (iterable of ints, each 0..2^n-1), return a dict mapping
    each internal-degree value to the number of vertices of S having it.
    Also asserts |S| <= 2^n and that every element is a valid vertex.
max_internal_degree(n, S)
    max over vertices of S of internal degree; -1 if S empty.
f_exact(n)
    exact value of f(n) by exhaustive enumeration over all subsets of size
    2^{n-1}+1.
even_weight_set(n)
    the set of all even-weight vertices of Q_n (size 2^{n-1}), which is
    independent, i.e. has D = 0. Used to reproduce the statement's example.

Every returned value is a plain Python int (exact). No floating point.
"""

from itertools import combinations


def _popcount(x):
    """Exact integer popcount."""
    return bin(x).count("1")


def internal_degree_distribution(n, S):
    """Return {degree: count} of internal degrees over vertices v in S.

    Two vertices u, v of Q_n are adjacent iff they differ in exactly one bit,
    i.e. (u ^ v) is a power of two.
    """
    S = sorted(set(S))
    N = 1 << n
    assert all(0 <= v < N for v in S), "vertex index out of range"
    assert len(S) == len(set(S)), "S contains duplicates"
    # Build adjacency within S: vertex -> set of neighbours inside S.
    adj = {v: set() for v in S}
    spos = set(S)
    for v in S:
        for k in range(n):
            w = v ^ (1 << k)
            if w in spos:
                adj[v].add(w)
    counts = {}
    for v in S:
        d = len(adj[v])
        counts[d] = counts.get(d, 0) + 1
    return counts


def max_internal_degree(n, S):
    """Maximum internal degree of vertices of S in Q_n[S]; -1 if S empty."""
    if not S:
        return -1
    return max(internal_degree_distribution(n, S).keys())


def f_exact(n, progress=False):
    """Exact f(n) by exhaustive enumeration (oracle). Small n only."""
    N = 1 << n
    m = (1 << (n - 1)) + 1
    assert m <= N, f"need 2^{n-1}+1 <= 2^n, i.e. n>=1"
    best = None
    best_set = None
    for S in combinations(range(N), m):
        M = set(S)
        d = max_internal_degree(n, M)
        if best is None or d < best:
            best = d
            best_set = M
            if progress:
                print(f"  n={n}: new best D={d} on S={sorted(M)}")
    return best, best_set


def even_weight_set(n):
    """The |S| = 2^{n-1} independent set from the statement (all even weight)."""
    return set(v for v in range(1 << n) if _popcount(v) % 2 == 0)


def main():
    print("=== Worked example 1: even-weight set is independent, D=0, size 2^{n-1} ===")
    for n in range(1, 5):
        S = even_weight_set(n)
        dist = internal_degree_distribution(n, S)
        dmax = max(dist.keys())
        print(f"n={n}: |S|={len(S)} (want {2**(n-1)}), D(S)={dmax}, "
              f"degree profile={dict(sorted(dist.items()))}")

    print()
    print("=== f_exact(n) by exhaustive enumeration ===")
    for n in range(1, 5):
        f, S = f_exact(n, progress=False)
        dist = internal_degree_distribution(n, S)
        print(f"f({n}) = {f}  |S|={len(S)}  achieved by S={sorted(S)}  "
              f"profile={dict(sorted(dist.items()))}")


if __name__ == "__main__":
    main()
