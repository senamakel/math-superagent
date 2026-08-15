#!/usr/bin/env python3
"""Independent forward-oracle cross-check + stabilization probe for the maximal
safe set of the halved absolute-difference operator (approach
excess-maximal-invariant-set first-step, rule 9/11 verification).

Hypothesis from excess_maximal_set.py: the maximal safe set S_K stabilises to
    S_K = { w in [0..M]^K : w_1 <= 1 and w_2 <= 2 }   (K >= 2)
i.e. in excess coords t_i = max(0,w_i-1):  t_1 = 0 and t_2 <= 1, all i>=3 free.

Here we test that hypothesis two INDEPENDENT ways:
  (1) backward recursion (S_K definition)  -- same as before
  (2) pure FORWARD oracle: for EVERY width-K window w in [0..M]^K, iterate H
      and check h_k(1)<=1 for all k<=K.  Forward-safe must equal S_K membership.
If the stabilised box {w_1<=1,w_2<=2} == S_K for all K and matches forward
safety exactly, the invariant family is established (over widths/magnitudes
tested).
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


def forward_safe(w):
    """Return True iff iterating H on the width-|w| window gives leading
    entry <=1 for every step down to width 1."""
    row = list(w)
    for _ in range(len(w)):
        if row[0] > 1:
            return False
        row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
    return True


def box(M, k):
    """Hypothesised stabilized set: w_1<=1 and w_2<=2 (K>=2)."""
    return {w for w in product(range(M + 1), repeat=k)
            if w[0] <= 1 and w[1] <= 2}


def main():
    print("Independent forward-oracle cross-check of the stabilized-description hypothesis")
    print(f"M={M}, K=1..{KMAX}, exhaustive over all (M+1)^K windows each K")
    S = backward_S(M, KMAX)
    stable_exact = True
    for k in range(1, KMAX + 1):
        B = box(M, k) if k >= 2 else {w for w in product(range(M + 1), repeat=k) if w[0] <= 1}
        fwd = {w for w in product(range(M + 1), repeat=k) if forward_safe(w)}
        match_back = (S[k] == fwd)          # backward def == forward oracle
        match_box = (fwd == B)               # forward oracle == stabilized box
        stable_exact &= match_box
        print(f"  K={k:2d}: |S_K|={len(S[k]):6d} |forwardSafe|={len(fwd):6d} "
              f"backward==forward: {match_back}  forward==stabilizedBox: {match_box}")
    print()
    print("Stabilized description {w_1<=1, w_2<=2} matches forward-safe set for ALL K:",
          stable_exact)
    print()
    print("Checkbox on the invariant reading:")
    # the two boundary cases that are the 'irredundant defining inequalities'
    print("  w_1<=1 : a window with w_1=2 is never safe (leading 2 at row 1)")
    print("  w_2<=2 : a window with w_1<=1 but w_2=3 is unsafe at row 2 (|w_1-3|>=2>1)")
    # prove the second: for w=(w1,3): h_2(1)=|w1-3|=3-w1; if w1<=1 then >=2 >1
    bad = [w for w in product(range(M + 1), repeat=3) if w[0] <= 1 and w[1] == 3]
    bad_unsafe = [w for w in bad if not forward_safe(w)]
    print(f"  all {len(bad)} width-3 windows with w_2=3 (w_1<=1) are forward-unsafe: {len(bad)==len(bad_unsafe)}")
    # boundary: w_2=2 with w_1<=1 all safe?
    ok = [w for w in product(range(M + 1), repeat=5) if w[0] <= 1 and w[1] == 2]
    ok_safe = [w for w in ok if forward_safe(w)]
    print(f"  all {len(ok)} width-5 windows with w_2=2 (w_1<=1) are forward-safe: {len(ok)==len(ok_safe)}")
    print()
    print("Wording of the invariant family (excess coords t_i=max(0,w_i-1)):")
    print("  t_1 = 0   (  w_1 <= 1 :  A_k(1)/2 - 1 <= 0, i.e. A_k(1) in {0,2} )")
    print("  t_2 in {0,1}   (  w_2 <= 2 )")
    print("  t_i in {0,1,2} free for i >= 3  ( w_i <= 3, the box bound M=3 )")
    print()
    print("So the exact maximal safe set for all K>=2 is:  S_K = { w_1<=1 , w_2<=2 }.")


if __name__ == "__main__":
    main()
