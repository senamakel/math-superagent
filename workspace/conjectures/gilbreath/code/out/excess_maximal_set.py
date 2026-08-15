#!/usr/bin/env python3
"""Exact maximal safe set of the halved absolute-difference operator in excess
coordinates (approach excess-maximal-invariant-set, first-step).

Exact integer backtracking induction S_1={w:w_1<=1}, S_K={w in [0..M]^K:
w_1<=1 and H(w) in S_{K-1}}, H(w)_i=|w_i-w_{i+1}|, for M=3, K=1..8.

Deliverables:
  1. load real halved first row h_1 = A_1(i)/2 for i>=1 from witnesses.json,
     verify against problem.md's A_1.
  2. the exact S_K sets.
  3. membership of the real window h_1(1..K) in S_K for each K.
  4. shape extraction in excess coords t_i=max(0,w_i-1): irredundant defining
     constraints, and whether the family stabilises with K.
  5. sanity: forward-oracle cross-check of the recursion, and reproduction of
     A_2 from h_1 by H.
"""
import json
from itertools import product

M = 3
KMAX = 8


def H(w):
    """H(w)_i = |w_i - w_{i+1}|; width drops by one."""
    return tuple(abs(w[i] - w[i + 1]) for i in range(len(w) - 1))


def build_S(M, KMAX):
    """S[k] (1-indexed) = S_k as set of tuples over [0..M]^k."""
    S = {0: {()}}
    for k in range(1, KMAX + 1):
        prev = S[k - 1]
        cur = set()
        for w in product(range(M + 1), repeat=k):
            if w[0] <= 1 and H(w) in prev:
                cur.add(w)
        S[k] = cur
    return S


def real_h1():
    """h_1(i) = A_1(i)/2 for i>=1 from witnesses.json."""
    d = json.load(open("code/out/witnesses.json"))
    A1 = d["A_1_first_12"]
    assert A1[0] == 1, A1
    h = tuple(a // 2 for a in A1[1:])
    return h


def forward_safe(h1, K):
    """Forward oracle: does the triangle from window h1(1..K) have h_k(1)<=1 for all k=1..K?"""
    row = list(h1[:K])  # halved row 1, positions 1..K
    ok = True
    for k in range(1, K + 1):
        if row[0] > 1:
            ok = False
        w = row[0]
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    return ok


def excess(w):
    return tuple(max(0, x - 1) for x in w)


def main():
    print("=" * 70)
    print("M =", M, " K up to", KMAX, " box size (M+1)^K")
    h1 = real_h1()
    print("real h_1 (halved A_1, i>=1):", h1)
    # verify against problem.md A_1 - check the first 9 halved values
    prob_A1 = [1, 2, 2, 4, 2, 4, 2, 4, 6, 2]
    prob_h = tuple(a // 2 for a in prob_A1[1:])
    print("problem.md halved A_1(1..9):", prob_h)
    print("match first 9:", h1[:9] == prob_h)
    # A_2 reproduction by H
    A2 = json.load(open("code/out/witnesses.json"))["A_2_first_12"]
    Hh = H(real_h1())  # H of h_1 (note: h_1 has finite first 12 entries; H drops one)
    print("H(h_1)(1..10) (expect A_2(i)/2 for i=1..10):", tuple(H(real_h1())[i] if i < len(H(real_h1())) else None for i in range(10)))
    # A_2(1..10) halved:
    A2h = tuple(a // 2 for a in A2[1:])
    print("A_2(1..10)/2:", A2h)
    print("H reproduces halved A_2(1..10)?", Hh[:min(len(Hh),10)] == A2h[:min(len(Hh),10)])

    S = build_S(M, KMAX)
    print()
    print("=" * 70)
    print("S_K sizes:")
    for k in range(1, KMAX + 1):
        print(f"  |S_{k}| = {len(S[k])}")
    print()
    print("=" * 70)
    print("Membership of real window h_1(1..K) in S_K:")
    all_true = True
    for k in range(1, KMAX + 1):
        win = h1[:k]
        mem = win in S[k]
        all_true &= mem
        fs = forward_safe(h1, k)
        agree = (mem == fs)
        print(f"  K={k}: window {win}  in S_{k}={mem}  forwardOracle={fs}  agree={agree}")
    print("all membership True:", all_true)

    # window max check for M adequacy
    wmax = max(h1[:KMAX])
    print(f"\nmax halved value in window 1..{KMAX} = {wmax} (<= M={M}? {wmax<=M})")

    print()
    print("=" * 70)
    print("Shape extraction in excess coordinates t_i=max(0,w_i-1):")
    # For each K report the S_K set in excess coords, and attempt to describe constraints.
    # Represent S_K in excess coords.
    for k in range(1, KMAX + 1):
        eset = {excess(w) for w in S[k]}
        print(f"\nS_{k} (excess coords), size {len(eset)}:")
        # first entry: t_1 : since w_1<=1 -> t_1=0 always. verify
        t1s = {t[0] for t in eset}
        print(f"   t_1 values: {sorted(t1s)}")
        # describe: print sorted (limited)
        sl = sorted(eset)
        shown = ", ".join(str(x) for x in sl)
        if len(shown) > 2000:
            shown = shown[:2000] + "..."
        print(f"   {shown}")

    print()
    print("=" * 70)
    print("Irredundant constraints attempt (threshold inequalities in excess coords):")
    # Hypothesis: constraints are of the form: sum_i c_i t_i <= b or t_i <= threshold
    # We look at the maximal allowed 'profiles'. Instead, we extract defining
    # half-spaces by checking which coordinate-threshold / pair constraints are tight.
    # We'll attempt parametric-family stabilization by comparing constraint sets.
    # Represent S_K (in excess) as all points satisfying a family of threshold
    # inequalities of the form  t_j <= b  or  t_i + t_j <= b  or  t_i <= t_j + b.
    # We test candidate template families and detect at which K a new type appears.
    report_constraints(KMAX, S)
    print()
    print("=" * 70)
    print("DONE")


def report_constraints(KMAX, S):
    """Detect which simple constraint types are active at each K and whether
    the family stabilises."""
    # candidate types: for pairs (i,j) in window: t_i <= b  (b=0,1,2), t_i + t_j <= b,
    # t_i - t_j <= b (i.e. t_i <= t_j + b).
    # We infer, for each S_K, the set of forbidden/required constraints and compare
    # across K by re-indexing from the LEFT (position 1 fixed).
    def constraints_of(k):
        eset = {excess(w) for w in S[k]}
        active = set()
        # singleton bounds
        for i in range(k):
            # smallest bound b such that all t_i <= b : since max t <= M-1=2
            pass
        return eset

    # Fresh approach: for each K, list, in excess coords, the "maximal" points
    # (Pareto frontier). The frontier shape is the invariant signature.
    for k in range(1, KMAX + 1):
        eset = {excess(w) for w in S[k]}
        # Pareto maximal: point p with no other q in eset with q_i>=p_i all i, q!=p
        par = []
        for p in eset:
            dominated = False
            for q in eset:
                if q != p and all(q[i] >= p[i] for i in range(k)):
                    dominated = True
                    break
            if not dominated:
                par.append(p)
        par.sort()
        print(f"  K={k} Pareto frontier (excess coords): {par}")


if __name__ == "__main__":
    main()
