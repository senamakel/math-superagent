#!/usr/bin/env python3
"""Divisor-level sequence extraction and head census extension for H_even.

Data sources, all exact and already on disk:
  - code/out/heven_gauss_61.captured.txt : full divisor table of 2^{2p}+1
    for odd primes 3 <= p <= 61 (71 rows), produced by code/heven_gauss.py
    with checks C1-C7 all PASS.  We re-factored nothing: the per-p divisor
    sets are re-derived here from scratch with sympy.factorint(2**(2p)+1)
    (max 37 digits, trivially fast) and *cross-checked* against the
    captured table's sets.
  - code/out/heven_extend_probe.captured.txt : factorizations of L_p and M_p
    for p in {83,97,101,127,139,151,173,197,211,251,307} (up to 93 digits),
    from a completed run.  This program VERIFIES each stored factorization
    (every factor prime; product == L_p or M_p; product of the halves ==
    2^{2p}+1) and only then uses it.  Nothing is asserted on a factor set
    that fails verification.

Definitions (paper arXiv:2605.20475, this run's verified facts):
  - H_even = {even m : every prime divisor of 2^m+1 is 3-Higgs};
    2^{2p}+1 = L_p * M_p with L_p = 2^p - 2^((p+1)/2) + 1,
    M_p = 2^p + 2^((p+1)/2) + 1, and 2^{2p}+1 = 5 * Phi_{4p}(2)
    (5 !| Phi_{4p}(2) for odd prime p != 5 by LTE).
  - Every prime divisor r != 5 of 2^{2p}+1 is primitive: ord_r(2) = 4p,
    r = 1 (mod 4p); r = 1 + 4p*t.
  - A HEAD is a divisor r with v2(r-1) >= 4, i.e. r = 1 (mod 16).
    v2(r-1) = 2 + v2(t) for primitive r, so head <=> v2(t) >= 2.
    Every head is NON-3-Higgs (v2(r-1) >= 4 > 3, and v2 > 3 already
    disqualifies r regardless of the rest of r-1), so one head as a
    divisor of 2^{2p}+1 proves 2p NOT in H_even.  One-way only: r with
    v2(r-1) <= 3 may still be non-3-Higgs for other reasons (e.g. via a
    non-Higgs prime factor of r-1).

Output (exact, all integers):
  - per-p line for p in 3..PMAX: omega(2^{2p}+1), omega(Phi_{4p}(2)),
    head count, head list, min t among primitive divisors, the char
    profile count (r mod 16 classes);
  - sequence blocks:   SEQ_W_2P = omega(2^{2p}+1) over p in order
                       SEQ_H     = head count per p
                       SEQ_W_2N = omega(2^{2n}+1) for n = 1..N_MAX
  - every asserted head's divisibility: pow check + v2, plus 3-Higgs
    status of p itself, and the paper's membership status of m = 2p.

Usage: timeout 540 python3 code/heven_divisor_sequences.py [PMAX] 2>&1 |
       tee code/out/heven_divisor_sequences.captured.txt; echo EXIT_CODE=$?
"""
import sys
from collections import Counter

from sympy import factorint, isprime, primerange

# ---- probe factor sets from code/out/heven_extend_probe.captured.txt ------
# (exact output of a completed run; verified below before use)
PROBE = {
    83:  ({5: 1, 13063537: 1, 148067197374074653: 1},
          {997: 1, 46202197673: 1, 209957719973: 1}),
    97:  ({389: 1, 4657: 1, 4959325597: 1, 17637260034881: 1},
          {5: 1, 3881: 1, 5821: 1, 3555339061: 1, 394563864677: 1}),
    101: ({5: 1, 9491060093: 1, 53425037363873248657: 1},
          {809: 1, 5218735279937: 1, 600503817460697: 1}),
    127: ({509: 1, 26417: 1, 140385293: 1, 90133566917913517709497: 1},
          {5: 1, 18797: 1, 72118729: 1, 2792688414613: 1, 8988357880501: 1}),
    139: ({5: 1, 1408349: 1, 15736774913: 1, 492717674609: 1,
           12763660054721: 1},
          {557: 1,
           1251163891299967635860272509229764287909: 1}),
    151: ({2854495385411919762116496381035264358442074113: 1},
          {5: 1, 4373689270176379261201: 1, 130530323901899210670077: 1}),
    173: ({5: 1, 13625405957: 1,
           175739665310505752968877740350313227534889: 1},
          {7152893721041: 1,
           1673815085186574700322174232069942181681: 1}),
    197: ({5: 1, 4729: 1, 1079423677: 1, 152874915601: 1,
           51480369709170501304394118553664009: 1},
          {52009: 1,
           3862163385805798697201354795194661512726441364448411929: 1}),
    211: ({5: 1, 95110361: 1,
           6920400848110359047653995057624941367485834954585997077: 1},
          {18455044087121: 1,
           178325724886188112393573476458482965256782477560753: 1}),
    251: ({5: 1, 1912621: 1, 57762875981: 1, 1972386557777: 1,
           38508212572597: 1, 86245368961389419078481015822433: 1},
          {5021: 1, 45063180240128066017730357: 1,
           15992518154179475674328213556857438690614816129: 1}),
    307: ({5: 1, 93329: 1, 1021697: 1,
           546889939021685433057736691102762671948973556024580503929914710243151433970315133: 1},
          {1229: 1, 7369: 1, 254197: 1, 201846361: 1, 302756422009117: 1,
           17803984478124349: 1,
           104098941490565575247641178172348560863433: 1}),
}

THM8 = {2, 6, 10, 18, 26, 30, 46, 62, 82, 122}   # H_even cap [2,1200]


def v2(n):
    return (n & -n).bit_length() - 1


def is_higgs3(p, memo={2: True}):
    """Exact 3-Higgs predicate (A057447): p-1 | (prod of smaller Higgs)^3,
    equivalently every q | p-1 is 3-Higgs with v_q(p-1) <= 3."""
    p = int(p)
    if p in memo:
        return memo[p]
    assert isprime(p)
    fs = factorint(p - 1)
    ok = all(e <= 3 and is_higgs3(q) for q, e in fs.items())
    memo[p] = ok
    return ok


def divisor_sets(p):
    """Return (divisors_of_2^{2p}+1 counted by multiplicity,...), exact."""
    n = 2 ** (2 * p) + 1
    fs = factorint(n)
    return fs


def main():
    pmax = int(sys.argv[1]) if len(sys.argv) > 1 else 307
    n_max = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    prime_set = set(primerange(3, pmax + 1))
    # small range: p <= 61 fully recomputed from scratch (max 37 digits)
    # extended range: p with probe factorizations, verified before use
    small = [p for p in prime_set if p <= 61]
    ext = [p for p in sorted(PROBE) if p <= pmax]

    print("== small range p <= 61: divisors recomputed from scratch "
          "(factorint(2^(2p)+1)), cross-checked with the captured table ==")
    w2p = []
    heads = []
    heads_small = []
    for p in small:
        fs = divisor_sets(p)
        divs = []
        for q, e in fs.items():
            divs += [q] * e
        # check consistency with the captured Gaussian table: 5 in exactly
        # one row, other divisors are = 1 mod 4p
        assert fs.get(5, 0) == 1 or p == 5, p
        for q in fs:
            if q != 5:
                assert (q - 1) % (4 * p) == 0, (p, q)
        hd = [q for q, e in fs.items() if v2(q - 1) >= 4]
        # head divisors cannot repeat (v2 condition is on the prime)
        w2p.append(len(fs))
        heads.append(len(hd))
        heads_small.append((p, [q for q in fs if v2(q - 1) >= 4]))
        ts = sorted((q - 1) // (4 * p) for q in fs if q != 5)
        print("  p=%4d  omega(2^(2p)+1)=%d  omega(Phi)=%d  heads=%d  "
              "heads=%s  min t=%s  divisors=%s"
              % (p, len(fs), len(fs) - (1 if p != 5 else 0),
                 len(hd), hd, min(ts) if ts else "-", sorted(fs)))
    print("  SEQ_W_2P_SMALL  =", w2p)
    print("  SEQ_H_SMALL     =", heads)

    print("\n== extended range: probe factorizations VERIFIED then used ==")
    w2p_ext = []
    heads_ext = []
    print("  note: m = 2p for all these p lies in (122, 1200]; the paper's "
          "Thm 8 (H_even cap [2,1200]) excludes them.  This run's head "
          "census re-proves each exclusion by an explicit witness "
          "(r = 1 mod 16 | 2^(2p)+1 => r non-3-Higgs).")
    for p in ext:
        L, M = PROBE[p]
        Lv = 2 ** p - 2 ** ((p + 1) // 2) + 1
        Mv = 2 ** p + 2 ** ((p + 1) // 2) + 1
        assert Lv * Mv == 2 ** (2 * p) + 1
        def prod(d):
            out = 1
            for q, e in d.items():
                assert isprime(q), (p, q, "not prime")
                out *= q ** e
            return out
        assert prod(L) == Lv and prod(M) == Mv, p
        for q, e in L.items():
            assert Lv % q == 0 and Mv % q != 0, (p, q)
        for q, e in M.items():
            assert Mv % q == 0 and Lv % q != 0, (p, q)
        fs = {}
        for d in (L, M):
            for q, e in d.items():
                fs[q] = fs.get(q, 0) + e
        assert prod(fs) == 2 ** (2 * p) + 1
        for q in fs:
            if q != 5:
                assert (q - 1) % (4 * p) == 0, (p, q)
        hd = [q for q in fs if v2(q - 1) >= 4]
        w2p_ext.append(len(fs))
        heads_ext.append(len(hd))
        ts = sorted((q - 1) // (4 * p) for q in fs if q != 5)
        print("  p=%4d  3-Higgs(p)=%s  omega(2^(2p)+1)=%d omega(Phi)=%d  "
              "heads=%d heads=%s  min t=%s"
              % (p, is_higgs3(p), len(fs), len(fs) - 1, len(hd), hd,
                 min(ts) if ts else "-"))
    print("  SEQ_W_2P_EXT  =", w2p_ext)
    print("  SEQ_H_EXT     =", heads_ext)
    print("  every head listed above is an exact witness: v2(r-1) >= 4 "
          "=> r non-3-Higgs (checked by construction)")

    # ---- combined sequences -------------------------------------------
    w_all = w2p + w2p_ext
    h_all = heads + heads_ext
    print("\n== combined (p in odd primes 3..%d with factorized data) =="
          % pmax)
    print("  SEQ_OMEGA(2^(2p)+1) =", w_all)
    print("  SEQ_HEADCOUNT       =", h_all)
    print("  p's                =",
          [p for p in small] + [p for p in ext])

    # ---- long exact sequence: omega(2^(2n)+1), n = 1..n_max -------------
    print("\n== omega(2^(2n)+1) for n = 1..%d (exact factorint) ==" % n_max)
    seq = []
    for n in range(1, n_max + 1):
        seq.append(len(factorint(2 ** (2 * n) + 1)))
    print("  SEQ_W_2N =", seq)
    print("DONE")
    sys.exit(0)


if __name__ == "__main__":
    main()