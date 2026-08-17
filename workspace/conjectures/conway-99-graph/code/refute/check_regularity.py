"""Attack problem.md's load-bearing restatement: C1 & C2 force regularity.

C1: every ADJACENT pair has exactly one common neighbour (every edge lies in
    exactly one triangle / unique triangle).
C2: every NON-ADJACENT distinct pair has exactly two common neighbours
    (unique 4-cycle through each non-adjacent pair).

The restatement claims: any finite graph satisfying C1 and C2 is REGULAR
(hence strongly regular with lambda=1, mu=2), with v forced to 99 by counting.

Brute force over ALL graphs up to n vertices (this is the oracle/counterexample
hunt for the claim, not the method). If a non-regular C1&C2 graph exists, the
restatement is false and the whole problem framing collapses.

complexity_class: exponential (2^C(n,2) graphs)
oracle_bound: n = 7 (2^21 = 2M labelled graphs, tractable)
"""
import itertools
import sys


def satisfies(E):
    n = len(E)
    for x in range(n):
        for y in range(x + 1, n):
            cn = sum(1 for z in range(n)
                     if z != x and z != y and E[x][z] and E[y][z])
            if E[x][y]:  # adjacent -> exactly 1 common neighbour (C1)
                if cn != 1:
                    return False
            else:        # non-adjacent -> exactly 2 common neighbours (C2)
                if cn != 2:
                    return False
    return True


def main():
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 7
    for n in range(0, nmax + 1):
        pairs = list(itertools.combinations(range(n), 2))
        count_c12 = 0
        nonregular = []
        for mask in range(1 << len(pairs)):
            E = [[0] * n for _ in range(n)]
            for t, (i, j) in enumerate(pairs):
                if mask & (1 << t):
                    E[i][j] = E[j][i] = 1
            if not satisfies(E):
                continue
            count_c12 += 1
            degs = [sum(row) for row in E]
            if len(set(degs)) > 1:
                nonregular.append((degs, E))
        print(f"n={n}: {count_c12} graphs satisfy C1&C2, "
              f"{len(nonregular)} non-regular", flush=True)
        if nonregular:
            for degs, E in nonregular:
                print("  NON-REGULAR C1&C2 GRAPH: degrees", degs)
                for r in E:
                    print("   ", r)
            print("*** RESTATEMENT IS FALSE: C1&C2 does NOT force regularity ***")
            return
    print("No non-regular C1&C2 graph up to n =", nmax,
          "-> restatement holds on this oracle range")


if __name__ == "__main__":
    main()
