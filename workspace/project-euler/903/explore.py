#!/usr/bin/env python3
"""Exploratory script: M_j and N(j,m) for n = 2..7.

Definitions (0-indexed one-line permutation of {0..n-1}):
  a_j(tau) = #{ m>j : tau[m] < tau[j] }   (Lehmer code coefficient at position j)
  M_j      = sum over all pi of sum_{i=0}^{n!-1} a_j(pi^i)
  N(j,m)   = #{ (pi,i) : 0<=i<n!, (pi^i)[m] < (pi^i)[j] }

Note  M_j = sum_{m>j} N(j,m)  by linearity.  We print both and check that
identity.  Exact integers only.
"""
import itertools
from math import factorial


def apply_power(pi, k):
    """Return pi^k (0-indexed one-line); pi^0 = identity."""
    n = len(pi)
    cur = list(range(n))
    for _ in range(k):
        cur = [pi[v] for v in cur]
    return tuple(cur)


def a_j(tau, j):
    """a_j(tau) = #{m>j : tau[m] < tau[j]}."""
    n = len(tau)
    return sum(1 for m in range(j + 1, n) if tau[m] < tau[j])


def explore(n):
    nf = factorial(n)
    perms = [tuple(p) for p in itertools.permutations(range(n))]
    M = [0] * n                       # M[j]
    N = [[0] * n for _ in range(n)]   # N[j][m]

    for pi in perms:
        # orbit of distinct powers pi^0, pi^1, ...
        orbit = []
        seen = {}
        cur = tuple(range(n))         # pi^0 = identity
        while cur not in seen:
            seen[cur] = len(orbit)
            orbit.append(cur)
            if len(orbit) > len(perms):
                raise RuntimeError("orbit longer than n! -- bug")
            cur = tuple(pi[v] for v in cur)
        d = len(orbit)               # order of pi
        assert nf % d == 0
        mult = nf // d               # each distinct power appears `mult` times in i=0..n!-1

        for tau in orbit:
            for j in range(n):
                M[j] += mult * a_j(tau, j)
                for m in range(j + 1, n):
                    if tau[m] < tau[j]:
                        N[j][m] += mult

    # sanity: M_j == sum_{m>j} N[j][m]
    ok = all(M[j] == sum(N[j][m] for m in range(j + 1, n)) for j in range(n))
    return M, N, ok


def main():
    print("=== M_j and N(j,m), exact integers, n = 2..7 ===")
    for n in range(2, 8):
        M, N, ok = explore(n)
        print(f"\n----- n = {n} -----")
        print(f"M_j (j=0..{n-1}) = {M}")
        # constant check
        const = (len(set(M)) == 1)
        print(f"  M_j constant in j?  {const}"
              + (f"  (value {M[0]})" if const else ""))
        # differences between consecutive j
        if not const:
            print("  differences M[j]-M[j-1] = "
                  f"{[M[j] - M[j - 1] for j in range(1, n)]}")
        print("  N(j,m) matrix (row j, col m):")
        print("   ", "  ".join(str(m) for m in range(n)))
        for j in range(n):
            row = "  ".join(str(N[j][m]) if m > j else " ." for m in range(n))
            print(f"  {j}: {row}")
        print(f"  [check] M_j == sum_{'{m>j}'} N[j][m] for all j: {ok}")


if __name__ == "__main__":
    main()
