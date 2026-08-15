"""Independent exact checker for f(n) with a spectral (Huang) cross-check.

f(n) = min { D(S) : S subset of {0,1}^n, |S| = 2^{n-1}+1 }, D(S) = maximum
internal degree of the induced subgraph Q_n[S].

This program does three things, all independently (it re-derives the oracle
rather than importing brute.py, so a disagreement between the two would be
caught rather than hidden):

  1. Brute-force every S of size 2^{n-1}+1 for n = 1..4 (exhaustive, exact
     integer arithmetic), compute the full internal degree distribution and
     D(S), and report f(1)..f(4) with one achieving set each.

  2. For each admissible S (and hence for each achieving/hitting set), build
     Huang's signed adjacency A_n on {0,1}^n (the recursion
        A_1 = [[0,1],[1,0]],  A_n = [[A_{n-1}, I],[I, -A_{n-1}]],
     which satisfies A_n^2 = n·I and so has eigenvalues ±sqrt(n), each with
     multiplicity 2^{n-1}), take the principal submatrix B = A_n[S,S], and
     compute its largest eigenvalue numerically:
        * λ_max(B) >= sqrt(n)   (interlacing: a >2^{n-1}-row principal
          submatrix of a matrix whose (2^{n-1})-th largest eigenvalue is
          sqrt(n) must have top eigenvalue at least sqrt(n));
        * λ_max(B) <= D(S)      (perron/quadratic-form bound: spectral radius
          of a signed adjacency supported on edges of a graph is at most the
          graph's maximum degree).
     These are exactly the two legs of Huang's lower-bound theorem, checked
     against the true exact minimum. Also count, over ALL admissible S, how
     often each inequality holds.

  3. Reproduce the statement's worked example: the even-weight vertex set has
     size 2^{n-1} and is independent (D = 0).

Complexity: exhaustive enumeration of C(2^n, 2^{n-1}+1) subsets, feasible only
for n <= 4 (n=4 is C(16,9) = 11440). Super-exponential in n by design; it is
the oracle, used strictly at small n as the evidence policy allows. Spectral
part: one small eigendecomposition per set.

All exact arithmetic for degrees; the eigenvalue check is floating point, so it
is reported with a tolerance and flagged only when it fails by more than it.
"""

import numpy as np
from itertools import combinations


def popcount(x):
    return bin(x).count("1")


def internal_degree_distribution(n, S):
    """{degree: count} of internal degrees over vertices v in S (exact ints)."""
    S = sorted(set(S))
    N = 1 << n
    assert all(0 <= v < N for v in S)
    spos = set(S)
    counts = {}
    for v in S:
        d = sum(1 for k in range(n) if (v ^ (1 << k)) in spos)
        counts[d] = counts.get(d, 0) + 1
    return counts


def max_internal_degree(n, S):
    dist = internal_degree_distribution(n, S)
    return max(dist.keys())


def f_exact(n):
    """Exact f(n) and one achieving set, by exhaustive enumeration."""
    N = 1 << n
    m = (1 << (n - 1)) + 1
    best = None
    best_set = None
    for comb in combinations(range(N), m):
        d = max_internal_degree(n, set(comb))
        if best is None or d < best:
            best = d
            best_set = set(comb)
    return best, best_set


def signed_adjacency(n):
    """Huang signed adjacency A_n (exact int matrix): A_n^2 = n·I.

    A_1 = [[0,1],[1,0]];  A_n = [[A_{n-1}, I_{2^{n-1}}],
                                   [I_{2^{n-1}}, -A_{n-1}]].
    Symmetric, zero diagonal, entry +-1 on each cube edge, A_n^2 = n I, so
    spectrum {+sqrt(n)^(2^{n-1}), -sqrt(n)^(2^{n-1})}.
    """
    A = np.array([[0, 1], [1, 0]], dtype=float)
    for _ in range(1, n):
        k = A.shape[0]
        I = np.eye(k)
        A = np.block([[A, I], [I, -A]])
    return A


def lambda_max_principal(A, S):
    """Largest eigenvalue of principal submatrix A[S,S] (float)."""
    S = sorted(S)
    B = A[np.ix_(S, S)]
    return float(np.linalg.eigvalsh(B)[-1])


def even_weight_set(n):
    return set(v for v in range(1 << n) if popcount(v) % 2 == 0)


def main():
    print("=== Part 3 first: WORKED EXAMPLE — even-weight set is independent ===")
    for n in range(1, 5):
        S = even_weight_set(n)
        dist = internal_degree_distribution(n, S)
        dmax = max(dist.keys())
        ok = (len(S) == 2 ** (n - 1)) and (dmax == 0)
        print(f"  n={n}: |S|={len(S)} (want {2**(n-1)}), D(S)={dmax}, "
              f"independent={ok}, profile={dict(sorted(dist.items()))}")

    print()
    print("=== Parts 1 & 2: exhaustive f(n) with spectral cross-check ===")
    tol = 1e-8
    for n in range(1, 5):
        A = signed_adjacency(n)
        N = 1 << n
        m = (1 << (n - 1)) + 1
        sq = np.sqrt(n)
        f, fset = f_exact(n)

        # spectral scan over ALL admissible sets
        inter_ok = deg_ok = both_ok = n_sets = 0
        worst_lam = None
        for comb in combinations(range(N), m):
            S = set(comb)
            n_sets += 1
            d = max_internal_degree(n, S)
            lam = lambda_max_principal(A, S)
            i_ok = lam >= sq - tol
            d_ok = lam <= d + tol
            inter_ok += i_ok
            deg_ok += d_ok
            both_ok += (i_ok and d_ok)
            if worst_lam is None or lam > worst_lam[0]:
                worst_lam = (lam, S, d)

        # explicit report on one achieving (hitting) set
        S = fset
        d = max_internal_degree(n, S)
        lam = lambda_max_principal(A, S)
        dist = internal_degree_distribution(n, S)
        print(f"  n={n}: f(n)={f}, |S|={m}, achieving S={sorted(S)}")
        print(f"      degree profile={dict(sorted(dist.items()))}")
        print(f"      D(S)={d}; λ_max(A_n[S,S])={lam:.6f}; "
              f"sqrt(n)={sq:.6f}")
        print(f"      λ_max <= D(S)? {lam <= d + tol};  "
              f"λ_max >= sqrt(n)? {lam >= sq - tol}")
        print(f"      (over all {n_sets} admissible sets of size {m}: "
              f"interlacing holds in {inter_ok}/{n_sets}, "
              f"degree bound holds in {deg_ok}/{n_sets}, "
              f"both in {both_ok}/{n_sets}; "
              f"worst λ_max seen = {worst_lam[0]:.6f} on |S|={len(worst_lam[1])}, D={worst_lam[2]})")


if __name__ == "__main__":
    main()
