#!/usr/bin/env python3
"""Independent, decisive recomputation of the correlation-order budget K*(n).

Settles GOAL priority 3: is K*(n) = floor(n/2), ceil(n/2), or something else?

DEFINITION (authoritative, per REOPENED.md):
  C_m(h)   = histogram of (m+1)-grams over overlapping windows of h.
             So C_1 = 2-gram histogram (n-1 windows), C_K = (K+1)-gram histogram.
  C_1..C_K = cumulative tuple of histograms for word-lengths 2..K+1.
  Witness(n,K) := exists h,h' with equal C_1..C_K but S(n)^2(h) != S(n)^2(h').
  K*(n) := min{ K in [1,n-1] : NOT Witness(n,K) }.

S(n) = (n-2) - 2*nu2(n); nu2 = wt(Phi_n h) = number of 2s in the {0,2}-suffix.
Used here via the canonical lib.supply_fold.s_sos, AND S^2 cross-checked by a
fully independent direct submask-XOR brute on a sample, so the oracle and the
definition are both grounded independently.

Independent implementation choices (differing from the prior artifacts):
  - cumulative key built as a tree / incremental refinement: we group strings
    by C_1..C_K incrementally as K grows, never recomputing lower histograms.
  - S2 computed once per string, stored.

Range: n = 2..NMAX. Exponential oracle (2^n states); oracle_bound n <= 20.
"""
import sys, os, time
from itertools import product

sys.path.insert(0, "/workspace/code")
from lib.supply_fold import s_sos


def hist(h, L):
    """histogram of length-L words over overlapping windows."""
    n = len(h)
    size = 1 << L
    cnt = [0] * size
    for p in range(n - L + 1):
        w = 0
        for b in range(L):
            w = (w << 1) | h[p + b]
        cnt[w] += 1
    return tuple(cnt)


def S2(n, h):
    S, _ = s_sos(n, list(h))
    return S * S


def kstar_sequence(n):
    """Return (K*, witness_prefix) with witness_prefix[K]=True iff witness at K.

    Incremental: partition strings by C_1..C_K key; refine as K grows.
    Even the first K with no witness is returned (min K).
    """
    strings = [tuple(x) for x in product([0, 1], repeat=n)]
    s2v = {h: S2(n, h) for h in strings}
    # incremental fiber refinement: cells dict key -> set of strings (or S2 set)
    # We instead track per-cell S2-value-set by cumulative key.
    keymap = {h: () for h in strings}          # current cumulative key
    prefix = []
    for K in range(1, n):
        newkeymap = {}
        for h in strings:
            key = (hist(h, K + 1),)
            newkeymap[h] = keymap[h] + key
        keymap = newkeymap
        # group by cumulative key, collect S2 sets
        cells = {}
        for h in strings:
            cells.setdefault(keymap[h], set()).add(s2v[h])
        any_witness = any(len(v) > 1 for v in cells.values())
        prefix.append(any_witness)
        if not any_witness:
            return K, prefix
    return n - 1, prefix


def direct_s2(n, h):
    """Independent direct submask-XOR brute of the fold (no s_sos)."""
    # T(n,d) = XOR over submasks o of d of h[n-1-d+o], d in [2,n-1]
    S = 0
    for d in range(2, n):
        val = 0
        o = d
        # iterate submasks of d
        sub = d
        while True:
            val ^= h[n - 1 - d + sub]
            if sub == 0:
                break
            sub = (sub - 1) & d
        S += -1 if val else 1
    return S, val


def main():
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--nmax", type=int, default=16)
    p.add_argument("--probe", action="store_true", help="cross-check s_sos vs direct")
    args = p.parse_args()
    NMAX = args.nmax

    out = []
    sp = out.append
    sp("kstar_settle: independent K*(n) -- floor vs ceil (GOAL priority 3)")
    sp("SEQUENCE: all binary strings per n (exhaustive oracle)")
    sp("ORACLE  : S=(n-2)-2*nu2 via lib.supply_fold.s_sos; direct-submask cross-check")
    sp("RANGE   : n = 2..%d (exponential 2^n, oracle_bound=%d)" % (NMAX, NMAX))
    sp("")

    # Cross-check s_sos against independent direct submask oracle on a sample
    import random
    random.seed(1)
    if args.probe:
        bad = 0
        for trial in range(200):
            n = random.randint(3, 40)
            h = [random.randint(0, 1) for _ in range(n)]
            S1, _ = s_sos(n, h)
            S2d, _ = direct_s2(n, h)
            if S1 != S2d:
                bad += 1
                sp("  MISMATCH s_sos vs direct n=%d S_sos=%d S_direct=%d" % (n, S1, S2d))
        sp("  probe: 200 random (n,h) s_sos vs independent direct submask-XOR: %s"
           % ("ALL AGREE" if bad == 0 else "%d MISMATCH" % bad))
        sp("")

    sp("== (A) K*(n), cumulative C_1..C_K, independent implementation ==")
    table = {}
    for n in range(2, NMAX + 1):
        t0 = time.time()
        k, prefix = kstar_sequence(n)
        table[n] = k
        sp("  n=%-3d K*=%-3d witness-prefix(K=1..%d)=%s  (%.1fs)"
           % (n, k, len(prefix), prefix, time.time() - t0))
    sp("")

    sp("== (B) Verdict vs floor / ceil ==")
    floor_ok = True; ceil_ok = True
    seq = []
    for n in range(2, NMAX + 1):
        got = table[n]
        floorv = n // 2
        ceilv = (n + 1) // 2
        seq.append(got)
        fl = got == floorv
        ce = got == ceilv
        floor_ok &= fl
        ceil_ok &= ce
        tag = ("floor" if fl and not ce else
               "ceil" if ce and not fl else
               "both" if fl and ce else "NEITHER")
        sp("  n=%-3d K*=%-3d  floor(n/2)=%-3d ceil(n/2)=%-3d -> %s"
           % (n, got, floorv, ceilv, tag))
    sp("")
    sp("  K*(n) == floor(n/2) for all n in [2,%d]: %s" % (NMAX, floor_ok))
    sp("  K*(n) == ceil(n/2)  for all n in [2,%d]: %s" % (NMAX, ceil_ok))
    sp("  sequence K*(n) = %s" % seq)
    sp("")

    text = "\n".join(out) + "\n"
    capture = "/workspace/code/out/kstar_settle.captured.txt"
    tmp = capture + ".tmp.%d" % os.getpid()
    with open(tmp, "w") as f:
        f.write(text)
    os.replace(tmp, capture)
    sys.stdout.write(text)


if __name__ == "__main__":
    main()
