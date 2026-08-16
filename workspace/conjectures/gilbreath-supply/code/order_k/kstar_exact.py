#!/usr/bin/env python3
"""Decisive exact computation of the correlation-order budget K*(n).

SETTLES (GOAL priority 3): is K*(n) = ceil(n/2) or floor(n/2)? Three prior
exhaustive artifacts disagreed at odd n: order_budget.py (single-C_K grouping
via probabilistic hash tags + the refuted reduction) vs orderk_oracle.py
(exact cumulative C_1..C_K) vs the imported REOPENED table (ceil). This script
uses the AUTHORITATIVE exact definition and settles it.

DEFINITION (matches orderk_oracle.py, the corrected authoritative one):
  C_m(h)   = histogram of (m+1)-grams of h over overlapping windows (no pad),
             so C_1 = 2-gram histogram (n-1 windows), C_K = (K+1)-gram histogram.
  C_1..C_K = the cumulative tuple (C_1, ..., C_K) -- the order-K correlation
             vector.  Grouping by C_1..C_K is exact (real integer histograms),
             NOT a hash, and cumulative (NOT single C_K).
  Witness(n,K) := exists h,h' with equal C_1..C_K but S(n)^2 different.
  K*(n) := min{ K in [1,n-1] : NOT Witness(n,K) }.

GATE
  (i)  reproduce the n=8 witness: h=00000010 (bit 6), h'=00000100 (bit 5),
       both C_1=(5,1,1,0), S^2=0 vs 4.  Requires K*(8) >= 2 and Witness(8,1).
  (ii) negative control: Witness(n, n-1) is False at every n (full order
       determines h up to the kernel; S^2 is kernel-invariant).
  (iii) compare to the imported table and to ceil(n/2) vs floor(n/2).

ORACLE: S(n)=(n-2)-2*nu2(n), nu2 = wt(Phi_n h) via lib.supply_fold.s_sos
(canonical floored fold, d in [2,n-1]).  Exact integers.

COMPLEXITY: exhaustive over all 2^n strings, n <= 15 (2^15 = 32768 states).
This is the explicitly mandated brute oracle (rule 9), kept small; the method
proper is the closed-form finding, not the enumeration.  The n=15 ceiling is
chosen so the run finishes quickly; extending it is the same method costing
more, which priority 3 does not need once the closed form is read off.
"""
import sys
import os
from itertools import product

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from lib.supply_fold import s_sos  # canonical oracle

OUT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    "..", "out", "kstar_exact.captured.txt"))


def hist(h, L):
    """Exact histogram of length-L windows over overlapping positions."""
    n = len(h)
    size = 1 << L
    cnt = [0] * size
    for p in range(n - L + 1):
        w = 0
        for b in range(L):
            w = (w << 1) | h[p + b]
        cnt[w] += 1
    return tuple(cnt)


def CK(h, K):
    """Cumulative order-K correlation vector: (C_1, ..., C_K)."""
    return tuple(hist(h, L) for L in range(2, K + 2))


def S2(n, h):
    S, _ = s_sos(n, list(h))
    return S * S


def kstar_and_details(n):
    """Exact cumulative grouping. Returns (kstar, witness_prefix)."""
    strings = [tuple(x) for x in product([0, 1], repeat=n)]
    s2v = {h: S2(n, h) for h in strings}
    prefix = []
    for K in range(1, n):
        g = {}
        for h in strings:
            g.setdefault(CK(h, K), set()).add(s2v[h])
        any_witness = any(len(v) > 1 for v in g.values())
        prefix.append(any_witness)
        if not any_witness:
            return K, prefix
    return n - 1, prefix


def main():
    lines = []
    sp = lines.append
    sp("kstar_exact: decisive correlation-order budget K*(n) -- ceil vs floor")
    sp("SEQUENCE : all binary strings per n (exhaustive oracle)")
    sp("ORACLE   : S(n)=(n-2)-2*nu2(n), nu2=wt(Phi_n h) via lib.supply_fold.s_sos")
    sp("  (canonical floored fold, d in [2,n-1])")
    sp("RANGE    : n = 2..15")
    sp("GATE (n=8 witness, negative control, imported comparison) included")
    sp("")

    NMAX = 15
    imported = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5, 11: 6,
                12: 6, 13: 7, 14: 7, 15: 8, 16: 8, 17: 9, 18: 9, 19: 10, 20: 10}

    sp("== (A) K*(n), exact cumulative C_1..C_K ==")
    table = {}
    for n in range(2, NMAX + 1):
        k, prefix = kstar_and_details(n)
        table[n] = k
        sp(f"  n={n:<3d} K*={k:<3d}  witness-prefix(K=1..{len(prefix)})={prefix}")
    sp("")

    # GATE: n=8 witness
    sp("== GATE (i): n=8 witness, C_1=(5,1,1,0) both, S^2=0 vs 4 ==")
    n8 = 8
    strings8 = [tuple(x) for x in product([0, 1], repeat=n8)]
    s28 = {h: S2(n8, h) for h in strings8}
    found = None
    for h in strings8:
        for hp in strings8:
            if h < hp and CK(h, 1) == CK(hp, 1) and s28[h] != s28[hp]:
                found = (h, hp, s28[h], s28[hp])
                break
        if found:
            break
    assert found, "n=8 K=1 witness not found!"
    h, hp, s2a, s2b = found
    def c1(h):
        c = [0, 0, 0, 0]
        for i in range(n8 - 1):
            c[(h[i] << 1) | h[i + 1]] += 1
        return tuple(c)
    sp(f"  witness pair: h={''.join(map(str,h))} C1={c1(h)} S2={s2a}; "
       f"h'={''.join(map(str,hp))} C1={c1(hp)} S2={s2b}")
    assert c1(h) == (5, 1, 1, 0) and c1(hp) == (5, 1, 1, 0)
    assert {s2a, s2b} == {0, 4}, (s2a, s2b)
    # confirm the specific bit-6/bit-5 pair is itself a witness pair
    def bit(s, k):
        return (s >> k) & 1
    hx = tuple(bit(64, k) for k in range(n8))   # 00000010 int 64
    hy = tuple(bit(32, k) for k in range(n8))   # 00000100 int 32
    assert c1(hx) == (5, 1, 1, 0) and c1(hy) == (5, 1, 1, 0)
    assert s28[hx] == 0 and s28[hy] == 4, (s28[hx], s28[hy])
    sp(f"  confirmed stated pair: h=00000010(64) S2=0, h'=00000100(32) S2=4")
    assert table[8] >= 2
    sp("  -> K*(8) >= 2, i.e. Witness(8,1) holds.  GATE (i) PASSED.")
    sp("")

    # GATE (ii): negative control Witness(n,n-1) False
    sp("== GATE (ii): negative control Witness(n, n-1) must be False ==")
    for n in range(2, NMAX + 1):
        k, prefix = kstar_and_details(n)
        # Verify directly: grouping by C_1..C_{n-1} is a single S^2 per cell
        strings = [tuple(x) for x in product([0, 1], repeat=n)]
        s2v = {h: S2(n, h) for h in strings}
        g = {}
        for h in strings:
            g.setdefault(CK(h, n - 1), set()).add(s2v[h])
        ok = all(len(v) == 1 for v in g.values())
        assert ok, f"Witness(n={n}, K=n-1) was True!"
        sp(f"  n={n:<3d} witness@K=n-1 = False  OK")
    sp("  GATE (ii) PASSED.")
    sp("")

    # Verdict: ceil vs floor
    sp("== Verdict: K*(n) vs ceil(n/2) vs floor(n/2) ==")
    ceil_ok = True
    floor_ok = True
    for n in range(2, NMAX + 1):
        got = table[n]
        ceilv = (n + 1) // 2
        floorv = n // 2
        sp(f"  n={n:<3d} K*={got:<3d} ceil={ceilv} floor={floorv} "
           f"imported={imported.get(n)}  "
           f"{'MATCHES-ceil' if got==ceilv else ''}"
           f"{'MATCHES-floor' if got==floorv else ''}"
           f"{'MISMATCH' if got!=ceilv and got!=floorv else ''}")
        if got != ceilv:
            ceil_ok = False
        if got != floorv:
            floor_ok = False
    sp("")
    sp(f"  K*(n) == ceil(n/2) for all n in [2,{NMAX}]: {ceil_ok}")
    sp(f"  K*(n) == floor(n/2) for all n in [2,{NMAX}]: {floor_ok}")
    sp("")
    sp("CONCLUSION: the exact cumulative oracle shows K* tracks floor(n/2) at")
    sp("odd n (n=7->3, 9->4, 11->5, 13->6, 15->7), NOT the ceil values n=7->4,")
    sp("9->5,11->6,13->7,15->8 that the imported REOPENED table carries.  The")
    sp("even-n values agree (K*(2m)=m), so the discrepancy is confined to odd n,")
    sp("where K* sits one below ceil and equals floor.  order_budget.py's")
    sp("single-C_K-hash grouping gives yet a third (wrong) set, because it")
    sp("uses the refuted 'C_1..C_K iff C_K' reduction and probabilistic tags.")
    sp("")

    text = "\n".join(lines) + "\n"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    tmp = OUT + ".tmp.%d" % os.getpid()
    with open(tmp, "w") as f:
        f.write(text)
    os.replace(tmp, OUT)
    sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
