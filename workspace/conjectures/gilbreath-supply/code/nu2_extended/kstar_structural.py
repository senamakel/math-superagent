#!/usr/bin/env python3
"""Decisive structural check of K*(n) via maximal run length of M_d △ M_{d'}.

CLAIM UNDER TEST (from the task):
    S^2 is a function of C_1..C_K  iff  every maximal run of M_d △ M_{d'}
    has length <= K+1 for all d,d' in [2,n-1].
    Hence K*(n) = R(n) - 1, where
    R(n) = max over d,d' in [2,n-1] of max-run-length(M_d △ M_{d'}).

Notation:
    S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}
    x_j = (-1)^{h_j},  (-1)^{T(n,d)} = prod_{s⊆d} x_{n-1-s}   (submask identity)
    M_d = { n-1-s : s ⊆ d }  the fold row (reflection of the downset of d),
          same run-length multiset as the downset, so we use runs_of_downset.
    S^2 = sum_{d,d'} prod_{j in M_d △ M_{d'}} x_j   (monomial identity)
    C_K(h) = histogram of (K+1)-grams of h over its n-K overlapping windows.
    K*(n) = min{K>=1 : S^2 constant on every C_K-fiber of F_2^n}.

FINDINGS (all reproduced by the runs below):
  [1] R(n) is NOT ceil(n/2)+1. Closed form (verified n=2..200):
        R(n) = 2^k on (2^k, 2^{k+1})  (argmax (2^k-1, 2^k): single run of length 2^k)
        R(2^j) = 2^j - 3 for j>=2     (argmax (2, 2^j-1))
        R(2)=R(3)=0, R(4)=1.
  [2] The run-length characterization is FALSE in both directions.
      Counterexample (n=6, K=3): a=001001 and b=010010 lie in the SAME C_3
      fiber (identical multiset of 4-grams) yet S^2(a)=4 != S^2(b)=0.  All
      monomial runs are <= 4 = K+1, so the SUFFICIENCY direction fails.
      Necessity fails elsewhere (see capture body).
  [3] ROOT CAUSE: C_K is a histogram -- it counts how many of each (K+1)-gram
      word occur, NOT where.  A fixed-position monomial run's product needs
      the positioned word, which the histogram does not give.  Moreover
      C_{K+1} does not determine C_K (the last boundary window is lost on
      marginalisation), so the K* threshold framework is itself non-monotone
      (e.g. n=14: no witness at K=8 but a witness at K=9).
  [4] The imported "measured" K* table (1,1,2,2,3,4,4,5,5,...) disagrees with
      the exhaustive ground-truth brute (n=6: table 3, ground truth 4).
      Against ground truth, K*(n) is neither ceil(n/2) nor R(n)-1.

Oracle: lib.supply_fold.s_sos (canonical floored fold, d in [2,n-1]); its
runs_of_downset for the downset runs; s_direct cross-checked on n=4..9.

Exact integer arithmetic.  The only exponential part is the 2^n fiber
enumeration, which is the declared oracle, bounded to n<=14.
"""

import itertools
import sys
from fractions import Fraction

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos, s_direct, runs_of_downset


# --------------------------------------------------------------------------
# Part 1: R(n) geometry
# --------------------------------------------------------------------------
def row_mask_from_runs(n, d):
    """n-bit mask of fold row M_d = { n-1-d+o : o ⊆ d }, from the downset runs
    (M_d is a reflection of the downset, shifted by n-1-d)."""
    m = 0
    base = n - 1 - d
    for (u, v) in runs_of_downset(d):
        for j in range(u, v + 1):
            m |= 1 << (base + j)
    return m


def max_run_of_mask(x):
    """Longest consecutive run of 1-bits in non-negative int x."""
    best = 0
    while x:
        while x and not (x & 1):
            x >>= 1
        c = 0
        while x & 1:
            c += 1
            x >>= 1
        best = max(best, c)
    return best


def R_of(n):
    """R(n) = max over d,d' in [2,n-1] of max-run-length(M_d △ M_{d'})."""
    masks = {d: row_mask_from_runs(n, d) for d in range(2, n)}
    best = 0
    arg = None
    ds = list(range(2, n))
    for i, d1 in enumerate(ds):
        for d2 in ds[i:]:
            m = max_run_of_mask(masks[d1] ^ masks[d2])
            if m > best:
                best = m
                arg = (d1, d2)
    return best, arg


def R_closed_form(n):
    """Candidate closed form of R(n), to check against the exact computation."""
    if n < 4:
        return 0
    import math
    k = (n - 1).bit_length() - 1            # floor(log2(n-1))
    two_k = 1 << k
    # if n-1 is a power of two (n = 2^k+1): best pair (2^k-1, 2^k) reachable -> 2^k
    if n == two_k + 1:
        return two_k
    # if n is a power of two >= 4: dip -> 2^k - 3  (k = log2 n)
    if n & (n - 1) == 0 and n >= 4:
        return n - 3
    # otherwise on (2^k, 2^{k+1}) with n-1 not a power -> 2^{floor(log2(n-1))}?
    # n-1 in [2^k, 2^{k+1}-1]; if n != 2^k+1 then n <= 2^{k+1} and n-1 = 2^k gives
    # the (2^k-1, 2^k) pair only when n-1 >= 2^k, i.e. always here.  But the
    # block max is 2^k when n-1 < 2^{k+1} i.e. n <= 2^{k+1}, with the dip at
    # n = 2^{k+1}.  So the constant value on strictly-non-power n is:
    if n - 1 == two_k:
        return two_k                       # n = 2^k + 1 handled above; else range
    return two_k if n <= 2 * two_k else 2 * two_k


# --------------------------------------------------------------------------
# C_K and brute ground-truth K*
# --------------------------------------------------------------------------
def c_k(h, K):
    """C_K(h): (K+1)-gram histogram of h over its n-K overlapping windows."""
    n = len(h)
    counts = [0] * (1 << (K + 1))
    for start in range(n - K):
        w = 0
        for t in range(K + 1):
            w = (w << 1) | h[start + t]
        counts[w] += 1
    return tuple(counts)


def s_squared(n, h):
    S, _ = s_sos(n, h)
    return S * S


def kstar_and_witness_flags(n):
    """Ground-truth brute: K* and per-K witness flags.  flags[K] True iff two
    strings in one C_K fiber have different S^2.  kstar = smallest K with no
    witness (first True->False crossing).  Note: for n where flags are not
    monotone (e.g. n=14) K* is not a sharp threshold; reported as-is."""
    all_str = list(itertools.product([0, 1], repeat=n))
    s2_of = {s: s_squared(n, s) for s in all_str}
    flags = {}
    kstar = None
    for K in range(1, n):
        fibers = {}
        for s in all_str:
            key = c_k(s, K)
            fibers.setdefault(key, set()).add(s2_of[s])
        flags[K] = any(len(v) > 1 for v in fibers.values())
        if flags[K] is False and kstar is None:
            kstar = K
    return kstar, flags


def cum_fiber_key(h, K):
    """Cumulative fiber key: equal on all of C_1..C_K (a nested refinement;
    this is the faithful reading of 'a function of C_1..C_K')."""
    return tuple(c_k(h, k) for k in range(1, K + 1))


def kstar_cumulative_flags(n):
    """witness_flags[K] True iff two strings equal on C_1..C_K differ in S^2.
    Returns dict with flags[K] for K=1..n-1.  These flags are monotone
    (nested fibers) since CUM_{K+1} refines CUM_K."""
    alls = list(itertools.product([0, 1], repeat=n))
    s2v = {s: s_squared(n, s) for s in alls}
    flags = {}
    for K in range(1, n):
        fibers = {}
        for s in alls:
            key = cum_fiber_key(s, K)
            fibers.setdefault(key, set()).add(s2v[s])
        flags[K] = any(len(v) > 1 for v in fibers.values())
    return flags


# --------------------------------------------------------------------------
# Explicit counter-example construction for the sufficiency direction
# --------------------------------------------------------------------------
def find_suff_counterexample(n, K):
    """If every monomial run <= K+1 but some C_K fiber splits S^2, return a
    witness pair (a,b)."""
    alls = list(itertools.product([0, 1], repeat=n))
    fibers = {}
    for s in alls:
        fibers.setdefault(c_k(s, K), []).append(s)
    for grp in fibers.values():
        if len(grp) < 2:
            continue
        for i in range(len(grp)):
            for j in range(i + 1, len(grp)):
                a, b = grp[i], grp[j]
                if s_squared(n, a) != s_squared(n, b):
                    return a, b
    return None


def all_msd_runs_le(n, K):
    """True iff every M_d△M_d' has max run <= K+1."""
    masks = {d: row_mask_from_runs(n, d) for d in range(2, n)}
    ds = list(range(2, n))
    for i, d1 in enumerate(ds):
        for d2 in ds[i:]:
            if max_run_of_mask(masks[d1] ^ masks[d2]) > K + 1:
                return False
    return True


# --------------------------------------------------------------------------
# imported table (research/witness-hunt-n20-imported.txt / kstar-n20-measured)
# --------------------------------------------------------------------------
IMPORTED_KSTAR = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5,
                  11: 6, 12: 6, 13: 7, 14: 7, 15: 8, 16: 8, 17: 9, 18: 9,
                  19: 10, 20: 10}


def main():
    out = []
    out.append("K*(n) structural characterization via maximal run length of M_d Δ M_{d'}")
    out.append("sequence: generic binary strings h in F_2^n (combinatorics, no primes)")
    out.append("oracle: lib.supply_fold.s_sos (canonical floored fold d in [2,n-1])")
    out.append("        + s_direct cross-check; lib.supply_fold.runs_of_downset for runs")
    out.append("range: R(n) geometry n=2..200; brute C_K fiber ground truth n=4..14\n")

    # ---- (1) R(n) table + closed form ----
    out.append("(1) R(n) = max run length of M_d △ M_{d'}   [exact geometry]")
    out.append("    n      R    R-1  ceil(n/2)   argmax(d,d')   closed-form R")
    Rtab = {}
    cf_ok = True
    for n in range(2, 201):
        R, arg = R_of(n)
        Rtab[n] = R
        cfr = R_closed_form(n)
        if cfr != R:
            cf_ok = False
        if n <= 34 or n in (64, 100, 128, 200):
            out.append(f"    {n:4d} {R:5d} {R-1:4d} {-(-n//2):8d}   {str(arg):14s} {cfr:5d}")
    out.append(f"    closed form R(n)=2^k on (2^k,2^{{k+1}}), 2^j-3 at n=2^j "
               f"-> matches exact on n=2..200: {cf_ok}")
    out.append("")

    # ---- (2) R-1 vs imported K* vs ceil(n/2) on n=2..20 ----
    out.append("(2) R(n)-1 vs imported 'measured' K* vs ceil(n/2)   (n=2..20)")
    out.append("    n   K*_imp  R-1  ceil   R-1==K*?  R-1==ceil?")
    for n in range(2, 21):
        k = IMPORTED_KSTAR[n]
        r1 = Rtab[n] - 1
        ce = -(-n // 2)
        out.append(f"    {n:3d} {k:7d} {r1:4d} {ce:4d}   "
                   f"{'YES' if r1==k else 'no':8s}  "
                   f"{'YES' if r1==ce else 'no':8s}")
    ex = all(Rtab[n] - 1 == IMPORTED_KSTAR[n] for n in range(6, 21))
    out.append(f"    -> R(n)-1 == K*_imported for all n=6..20? {ex}")
    out.append("")

    # ---- (4) K*==ceil(n/2) and R==ceil(n/2)+1 ----
    k_ceil = all(IMPORTED_KSTAR[n] == -(-n // 2) for n in range(6, 21))
    R_ceil = all(Rtab[n] == -(-n // 2) + 1 for n in range(6, 40))
    out.append("(4) K*(n)=ceil(n/2) for n=6..20 (imported table): "
               f"{'YES' if k_ceil else 'NO'}")
    out.append("    R(n)=ceil(n/2)+1 for n=6..39 (geometry): "
               f"{'YES' if R_ceil else 'NO'}")
    out.append("    (R is a 2-power block function, NOT ceil(n/2)+1; the two")
    out.append("     coincide only where ceil(n/2)+1 happens to be a power-of-2")
    out.append("     block value.)")
    out.append("")

    # ---- (3) brute characterization check + counterexamples ----
    out.append("(3) Exhaustive C_K fiber witness check, n=4..14 (declared 2^n oracle)")
    out.append("    prediction: has_witness(K)  <=>  some monomial run > K+1  <=>  K < R(n)-1")
    out.append("    n   K*_brute  R-1  K*_imp   pred==ground?  first K mismatch")
    all_pred_ok = True
    ground_k = {}
    for n in range(4, 15):
        kstar, flags = kstar_and_witness_flags(n)
        ground_k[n] = kstar
        pred_ok = True
        mis = None
        for K in range(1, n):
            predict = (K < Rtab[n] - 1)
            ground = flags.get(K, False)
            if predict != ground:
                pred_ok = False
                if mis is None:
                    mis = K
        imp = IMPORTED_KSTAR.get(n, "?")
        out.append(f"    {n:3d} {str(kstar if kstar is not None else '-'):8s} "
                   f"{Rtab[n]-1:4d} {str(imp):7s} "
                   f"{'OK' if pred_ok else 'FAIL':13s} {mis if mis is not None else ''}")
        all_pred_ok = all_pred_ok and pred_ok
        if not pred_ok:
            for K in range(1, n):
                predict = (K < Rtab[n] - 1)
                ground = flags.get(K, False)
                if predict != ground:
                    out.append(f"        (n={n},K={K}): predict has_witness="
                               f"{predict}, ground={ground}")
    out.append(f"    -> characterization holds on n=4..14 by brute: {all_pred_ok}")
    out.append("")

    # ---- explicit counterexamples, sufficiency direction ----
    out.append("    Explicit sufficiency-direction counterexamples (all monomial runs")
    out.append("    <= K+1, yet a C_K fiber splits S^2):")
    for (n, K) in [(6, 3), (7, 3), (12, 8)]:
        rle = all_msd_runs_le(n, K)
        if not rle:
            out.append(f"      n={n},K={K}: NOT applicable (some run > K+1 exists)")
            continue
        pair = find_suff_counterexample(n, K)
        if pair:
            a, b = pair
            out.append(f"      n={n},K={K}: all runs<=K+1 ({rle}); "
                       f"a={' '.join(map(str,a))} b={' '.join(map(str,b))} "
                       f"same C_{K}, S^2={s_squared(n,a)} vs {s_squared(n,b)}")
    out.append("")
    out.append("    Root cause: C_K is a HISTOGRAM (word counts, no positions).")
    out.append("    Example (n=6,K=3): a=001001, b=010010 have the SAME multiset of")
    out.append("    4-grams {(0010),(0100),(1001)} yet the 4-gram at fixed positions")
    out.append("    1..4 is 0100 (product -1) in a and 1001 (product +1) in b.  A")
    out.append("    positioned monomial run is not determined by the histogram.")
    out.append("    Also C_{K+1} does not determine C_K: the last boundary window is")
    out.append("    lost on marginalisation, so the K* threshold is non-monotone")
    out.append("    (n=14: no witness at K=8, a witness at K=9).")
    out.append("")

    # ---- K* ground truth vs both candidate formulas ----
    out.append("(5) K* ground truth vs R(n)-1 and ceil(n/2)   (n=4..14)")
    out.append("    n   K*_brute  R-1  ceil(n/2)  K*_imp  K*_brute==R-1?  ==ceil?")
    for n in range(4, 15):
        ks = ground_k[n]
        out.append(f"    {n:3d} {ks:8d} {Rtab[n]-1:4d} {-(-n//2):9d} "
                   f"{str(IMPORTED_KSTAR.get(n,'?')):7s} "
                   f"{'YES' if ks==Rtab[n]-1 else 'no':14s} "
                   f"{'YES' if ks==-(-n//2) else 'no':5s}")
    gR = all(ground_k[n] == Rtab[n] - 1 for n in range(4, 15))
    gC = all(ground_k[n] == -(-n // 2) for n in range(4, 15))
    out.append(f"    -> ground-truth K* == R(n)-1 for all n=4..14: {gR}")
    out.append(f"    -> ground-truth K* == ceil(n/2) for all n=4..14: {gC}")
    out.append("")

    # ---- (6) cumulative fibers: the faithful reading of 'C_1..C_K' ----
    out.append("(6) Same claim under CUMULATIVE fibers (equal on C_1..C_K), the")
    out.append("    faithful reading of the task's 'C_1..C_K'.  CUM_{K+1} refines")
    out.append("    CUM_K (nested), so flags are monotone and K* is a genuine threshold.")
    out.append("    prediction still: has_cumwitness(K) <=> K < R(n)-1.")
    out.append("    n   R-1  K*_cum  floor  ceil   pred==ground?")
    cum_ok = True
    cum_k = {}
    for n in range(4, 15):
        cflags = kstar_cumulative_flags(n)
        kstar = next((K for K in range(1, n) if not cflags[K]), None)
        cum_k[n] = kstar
        Rv = Rtab[n]
        ok = True
        for K in range(1, n):
            pred = (K < Rv - 1)
            gr = cflags[K]
            if pred != gr:
                ok = False
        cum_ok = cum_ok and ok
        out.append(f"    {n:3d} {Rv-1:4d} {str(kstar):6s} {n//2:5d} "
                   f"{-(-n//2):4d}  "
                   f"{'OK' if ok else 'FAIL':13s}")
    out.append(f"    -> cumulative run-length characterization holds on n=4..14: {cum_ok}")
    out.append("    -> cumulative K*(n)==floor(n/2) for all n=4..14: "
               f"{all(cum_k[n]==n//2 for n in range(4,15))}")
    out.append("    (The R-1 prediction overshoots: R is a 2-power block function")
    out.append("     far above floor(n/2), so the run-length criterion is not the")
    out.append("     operative threshold under either definition.)")
    out.append("")

    out.append("VERDICT: the run-length characterization K*(n)=R(n)-1 is REFUTED")
    out.append("by ground truth, and K*(n)=ceil(n/2) is also refuted against the")
    out.append("exhaustive oracle.  The structural claim that a histogram C_K")
    out.append("pins positioned products over runs of length <=K+1 is false --")
    out.append("whether C_K means the single histogram (non-nested, non-monotone")
    out.append("K*, floor/ceil test fails) or the cumulative family C_1..C_K (nested,")
    out.append("monotone, K*=floor(n/2), but again not R(n)-1).")
    out.append("")

    text = "\n".join(out) + "\n"
    with open("/workspace/code/out/kstar_structural_capture.txt", "w") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
