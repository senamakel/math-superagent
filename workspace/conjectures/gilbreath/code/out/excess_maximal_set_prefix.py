#!/usr/bin/env python3
"""Exact synthesis of the maximal safe set S_K of the halved |a-b| operator at
M=3 (raw w coordinates, no excess projection which collapses w=0/1). Goal:
find whether S_K is determined by a FIXED-LENGTH prefix (property that would
yield a width-uniform invariant), and extract the minimal defining description.

Queries:
  1. prefix-determinism: is membership of w in S_K decided by its first j
     coordinates for all K >= j (i.e. w in S_K iff prefix_j(w) in P_j for some
     fixed P_j independent of K)?
  2. minimal prefix length J that decides S_K for all K;
  3. the exact prefix set P_J and its irredundant condition;
  4. report S_K sizes (K=1..10).
"""
from itertools import product

M = 3
KMAX = 10


def H(w):
    return tuple(abs(w[i] - w[i + 1]) for i in range(len(w) - 1))


def backward_S(M, KMAX):
    S = {0: {()}}
    for k in range(1, KMAX + 1):
        prev = S[k - 1]
        S[k] = {w for w in product(range(M + 1), repeat=k)
                if w[0] <= 1 and H(w) in prev}
    return S


def prefix_project(S, k, j):
    """The set of j-prefixes that occur among width-k safe windows."""
    return {w[:j] for w in S[k]}


def main():
    S = backward_S(M, KMAX)
    print("M =", M)
    for k in range(1, KMAX + 1):
        print(f"  |S_{k}| = {len(S[k])}")
    print()

    # prefix-determinism test: find smallest j such that for all K in range the
    # set of j-prefixes of S_K is the same set AND is sufficient (a window is
    # safe iff its j-prefix is in that set). We use the LARGEST K as witness for
    # sufficiency on the far coordinates.
    Kref = KMAX
    print("Prefix-determinism analysis (is S_K decided by a fixed prefix?):")
    found = None
    for j in range(1, KMAX):  # J = j
        # the set of safe j-prefixes at the largest K
        Pj = {w[:j] for w in S[Kref]}
        # is every window whose j-prefix is in Pj safe at EVERY K from j..KMAX?
        ok = True
        for K in range(j, KMAX + 1):
            for w in product(range(M + 1), repeat=K):
                if w[:j] in Pj:
                    if w not in S[K]:
                        ok = False
                        break
            if not ok:
                break
        # and does S_K depend only on prefix for all K (no window with prefix in
        # Pj is unsafe, which we checked; also need: no safe window whose prefix
        # NOT in Pj -- but prefix in Pj is by construction, so sufficiency holds
        # iff every K>=j window with safe-j-prefix is safe).
        allK_prefix_set_same = all(prefix_project(S, K, j) == Pj
                                   for K in range(max(j, 2), KMAX + 1))
        print(f"  J={j}: |safe prefixes|={len(Pj)}  decides-all-K={ok}  "
              f"prefix-set-constant-over-K={allK_prefix_set_same}")
        if ok and allK_prefix_set_same:
            found = j
            break
    print()
    if found is None:
        print("NO fixed prefix decides S_K over K=1..%d: the constraint family "
              "does not stabilise to a prefix property within this range." % KMAX)
    else:
        J = found
        Pj = {w[:J] for w in S[Kref]}
        print(f"MINIMAL deciding prefix length J = {J}")
        print(f"  defining set P_{J} (safe {J}-prefixes): size {len(Pj)}")
        print(f"  S_K = {{ w : w[0..{J}-1] in P_{J} }}  for all K >= {J}  (within tested range)")
        # list P_J complement (forbidden prefixes) - the irredundant constraints
        comp = [p for p in product(range(M + 1), repeat=J) if p not in Pj]
        print(f"  forbidden {J}-prefixes: {sorted(comp)}")
        # the minimal description: check if it's a threshold/simple
        print("  Wording: a width-K window is safe for K rows iff its first",
              J, "entries avoid the listed forbidden prefixes.")


if __name__ == "__main__":
    main()
