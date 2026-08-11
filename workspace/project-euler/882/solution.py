#!/usr/bin/env python3
"""Project Euler 882 — dyadic CGT solution.

Structural hypothesis (research/CONTEXT.md, code/dyadic.py): each single number
k in the bit-deletion game is a canonical dyadic "Number" g(k):
    g(0) = 0
    g(k) = { g(j) for j a 1-deletion of k  |  g(j) for j a 0-deletion of k }
           = simplest dyadic strictly between max(Left) and min(Right)
where deleting a bit from bin(k) drops leading zeros (empty -> 0).
Board value G(n) = sum_{k=1..n} k*g(k), and S(n) = ceil(G(n)).

Steps (per the task):
  1. simplest_between validated (toolkits module + birthday oracle).
  2. compute g(k) for all k=1..100000; for every k assert Number-ness:
        max(Left g values) < min(Right g values)   for a Number.
     Report first violating k (critical).
  3. G(n)=sum k*g(k), S_ceil=ceil(G(n)) for n=1..20; cross-check against
     real-game oracle on disk S(1,2,3,4,5,10)=1,2,8,9,17,64.
  4. Compute G(100000) exactly, print S_answer = ceil(G(100000)).

Complexity: g(k) needs bit-length ~17 enumerations, all children < k so the
forward sweep is O(N * log N).  Exact Fraction arithmetic throughout.
"""
import sys
from fractions import Fraction
from math import ceil, floor

# improved sys path so direct run can import the toolkit
from toolkits.simplest_dyadic import simplest_between


def one_deletions(x):
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '1':
            t = s[:i] + s[i + 1:]
            out.add(0 if t == '' else int(t, 2))
    return out


def zero_deletions(x):
    if x == 0:
        return []
    s = bin(x)[2:]
    out = set()
    for i, ch in enumerate(s):
        if ch == '0':
            t = s[:i] + s[i + 1:]
            out.add(0 if t == '' else int(t, 2))
    return out


def eval_g(maxk):
    """g = dict k -> Fraction for k=0..maxk.  Returns (g, first_violation)
    where first_violation is the first k that is NOT a Number (max(L) >= min(R)
    or a degenerate hand side), or None if all are Numbers."""
    g = {0: Fraction(0)}
    first_viol = None
    for k in range(1, maxk + 1):
        Lvals = [g[j] for j in one_deletions(k)]
        Rvals = [g[j] for j in zero_deletions(k)]
        lo = max(Lvals) if Lvals else None   # None == -inf
        hi = min(Rvals) if Rvals else None   # None == +inf
        # Number-ness: must have at least meaning... a Number requires the
        # game to be numeric; single-sided games are still Numbers (option set
        # empty on one side treated as no constraint), but we need lo<hi when
        # both sides present.
        if Lvals and Rvals and not (lo < hi):
            first_viol = first_viol if first_viol is not None else k
        g[k] = simplest_between(lo, hi)
    return g, first_viol


def main():
    N = 100000
    g, first_viol = eval_g(N)

    # ---- step 2: Number-ness report ----
    print("g(k) Number-ness check for k=1..100000 ...")
    if first_viol is None:
        print(f"ALL k in 1..{N} are Numbers: max(Left) < min(Right) for every k.")
        viol_str = "none"
    else:
        print(f"FIRST violating k = {first_viol} (max(Left) >= min(Right)).")
        viol_str = str(first_viol)

    # ---- step 3: S_ceil(n) n=1..20 vs real oracle ----
    real = {1: 1, 2: 2, 3: 8, 4: 9, 5: 17, 10: 64}
    print("\n n    G(n)              S_ceil   real-oracle  match")
    G = Fraction(0)
    matches = []
    for n in range(1, 21):
        G += n * g[n]
        Sc = ceil(G)
        m = "  --" if n not in real else ("  OK" if Sc == real[n] else "MISMATCH")
        if n in real:
            matches.append(Sc == real[n])
        print(f"{n:2d}  {str(G):>18s}  {Sc:8d}   {real.get(n, '-'):>5}   {m}")
    oracle_ok = all(matches)
    print(f"\nOracle cross-check (against S(1,2,3,4,5,10)=1,2,8,9,17,64): "
          f"{'ALL MATCH' if oracle_ok else 'SOME MISMATCH'}")

    # ---- step 4: final answer ----
    # note: G already accumulated to n=20; keep a separate exact value for N
    G_full = sum(k * g[k] for k in range(1, N + 1))
    S_answer = ceil(G_full)
    print(f"\nG(100000) = {G_full}")
    print(f"G(100000) as decimal ~ {float(G_full):.10g}")
    print(f"S(100000) = ceil(G(100000)) = {S_answer}")

    return viol_str, G_full, S_answer, oracle_ok


if __name__ == "__main__":
    sys.setrecursionlimit(10 ** 7)
    viol, Gf, Sa, ok = main()
    # two-line output for dyadic_answer.txt
    with open("/workspace/dyadic_answer.txt", "w") as f:
        f.write(f"g-Number-ness: first_violating_k={viol} "
                f"(checked k=1..100000)\n")
        f.write(f"S(100000)=ceil(G(100000))= {Sa}\n")
    print("\nwritten /workspace/dyadic_answer.txt")
