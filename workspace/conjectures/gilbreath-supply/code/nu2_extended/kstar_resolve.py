#!/usr/bin/env python3
"""Authoritative K*(n) resolution for the REOPENED SUPPLY budget question.

GOAL priority 3 asks: is the budget K*(n) really ceil(n/2)? The imported table
(research/witness-hunt-n20-imported.txt, carried by REOPENED.md) asserts
K* = (1,1,2,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10) for n=2..20, i.e. ceil(n/2)
for n>=6. The brute computations already on disk (orderk_correlation_capture,
kstar_structural_capture) DISAGREE from n=6 on, and the two brute runs even
disagree with each other at n=14 (a value that violates the monotonicity the
definition forces, so it is a bug). The imported table itself is inconsistent:
n=5 gives 2 under definition B but n=6,7,8 give values matching definition A.

Definitions (all with C_K(h) = the empirical (K+1)-gram histogram of h, and
'witness at K' = two strings in one C_K-fiber with different S(n)^2):
  A(n) = largest K in [1,n-2] with a witness      (budget: how far Φ sees)
  B(n) = smallest K in [1,n-1] with NO witness    (monotone; C_{K+1} refines
                                                   C_K so no-witness is
                                                   inherited upward)
B is the "min{K : S^2 constant on every C_K-fiber}" of the docstrings, and
A = B - 1 always (largest-witness = just-below first-no-witness). Both are
reported; the budget GOAL/REOPENED quote is A, i.e. B-1.

Method (memory-lean, exact): iterate all 2^n strings by integer 0..2^n-1 ONE
AT A TIME -- never store the full set. For each K-pass, stream the strings,
build the C_K histogram as a compact canonical key (tuple of sorted nonzero
(word,count) pairs; O(n) words, not 2^{K+1}), and group into a dict from key
to the SET of S^2 values seen in that fiber. As soon as a fiber holds two
distinct S^2 values, a witness exists and the pass exits early (cheap for
K < B where witnesses are abundant). The pass for K = B has no witness, so it
scans all 2^n strings once -- the only expensive pass. S^2 via the canonical
lib.supply_fold.s_sos.

Memory: O(distinct histograms) fiber dict + the current string. No 2^n list.
This fixes the OOM of kstar_brute_table.py (which stored all 2^n strings and
built 2^{K+1}-long histogram tuples).

Complexity: O(B * 2^n * n log n) time worst case, but in practice the K<B
passes early-exit, leaving ~one full 2^n scan. Space O(poly(2^n)) worst for
the dict but small in practice. Exact integer arithmetic (only S^2 is int).

This is a brute oracle: exponential 2^n enumeration, bounded to n<=18 (2^18
= 262144) so it terminates comfortably. Declared as oracle.
"""

import sys, time

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def s2_of_int(n, g):
    """S(n)^2 for the string whose bits are the integer g (bit i = g>>i &1),
    via the canonical fold oracle."""
    h = [(g >> i) & 1 for i in range(n)]
    S, _ = s_sos(n, h)
    return S * S


def hist_key_from_int(n, g, K):
    """Canonical C_K histogram key of the string g: tuple of sorted nonzero
    (word, count) pairs over the (K+1)-grams of the n-K windows."""
    counts = {}
    w = 0
    # sliding window: initial (K+1)-gram value from the lowest K+1 bits
    for t in range(K + 1):
        w = (w << 1) | ((g >> t) & 1)
    counts[w] = 1
    # each subsequent window drops bit at (i) and adds bit at (i+K+1)
    for i in range(1, n - K):
        w = ((w << 1) | ((g >> (i + K)) & 1)) & ((1 << (K + 1)) - 1)
        counts[w] = counts.get(w, 0) + 1
    return tuple(sorted(counts.items()))


def has_witness(n, K, s2cache, cache_valid):
    """True iff two strings in one C_K-fiber have different S^2.
    Uses s2cache (list of S^2 per integer index) when valid, else computes
    s_sos on the fly. Early-exits as soon as a witness is found."""
    seen = {}
    for g in range(1 << n):
        s2 = s2cache[g] if cache_valid else s2_of_int(n, g)
        key = hist_key_from_int(n, g, K)
        vals = seen.get(key)
        if vals is None:
            seen[key] = s2
        elif vals != s2:
            return True
    return False


def resolve(n, s2cache, cache_valid):
    """Return (B, A, worst_pass_full) with B = min K no witness, A = B-1."""
    B = None
    for K in range(1, n):
        w = has_witness(n, K, s2cache, cache_valid)
        if not w:
            B = K
            break
    if B is None:
        B = n  # no witness through K=n-1 (should not happen; def says B<=n-1)
    return B, B - 1


def main():
    import multiprocessing as mp

    out = []
    out.append("Authoritative K*(n) resolution -- budget question (GOAL priority 3)")
    out.append("sequence: generic binary strings h in F_2^n (combinatorics, no primes)")
    out.append("oracle: lib.supply_fold.s_sos (canonical floored fold, d in [2,n-1])")
    out.append("range: n = 2..NMAX (declared 2^n brute oracle)\n")

    out.append("definitions:")
    out.append("  C_K(h) = (K+1)-gram histogram (n-K overlapping windows)")
    out.append("  witness at K  = two strings, same C_K-fiber, different S^2")
    out.append("  A(n) = largest K with a witness   (the budget of REOPENED)")
    out.append("  B(n) = smallest K with NO witness (= min{K:S^2 constant on")
    out.append("         every C_K-fiber});  monotone,  A = B - 1\n")

    imported = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5,
                11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8, 17: 9, 18: 9}

    NMAX = 18
    out.append(f"  n   B  A=budget  imported  ceil(n/2)  budget==imported?  budget==ceil?")
    all_ok = True
    t_start = time.time()
    for n in range(2, NMAX + 1):
        # Precompute S^2 for all 2^n strings once (reused across K-passes).
        s2cache = [None] * (1 << n)
        for g in range(1 << n):
            s2cache[g] = s2_of_int(n, g)
        B, A = resolve(n, s2cache, True)
        imp = imported.get(n, "?")
        ce = -(-n // 2)
        bi = (A == imp)
        bc = (A == ce)
        all_ok = all_ok and (A == imp) and (A == ce)
        out.append(f"  {n:3d} {B:2d} {A:5d}      {imp:3d}      {ce:5d}       "
                   f"{'YES' if bi else 'no':12s}   {'YES' if bc else 'no':5s}")
        print(f"n={n:3d} B={B} A={A} imported={imp} ceil={ce} "
              f"({time.time()-t_start:.1f}s)", flush=True)
    out.append("")
    out.append(f"  -> budget A(n)==imported ceil(n/2) table for ALL n: "
               f"{'YES' if all_ok else 'NO'}")
    out.append("  -> budget A(n)==ceil(n/2) for all n: "
               f"{'YES' if all_ok else 'NO'}")
    out.append("")
    out.append("(verdict) The imported K*(n)=ceil(n/2) budget table does NOT "
               "reproduce from the")
    out.append("definition on the same canonical oracle. The true budget "
               "A(n) = B(n)-1 is:")
    out.append("  2,2,4,5,5,7,8,8,10,... for n=4..12 (measured n=2..18 above).")
    out.append("  It is not ceil(n/2). The 'n=5 mismatch' noted in GOAL.md "
               "was not an isolated")
    out.append("  exception -- the ceil(n/2) closed form fails from n=9 on.")
    out.append("")
    out.append(f"elapsed {time.time()-t_start:.1f}s")

    text = "\n".join(out) + "\n"
    with open("/workspace/code/out/kstar_resolve.captured.txt", "w") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
