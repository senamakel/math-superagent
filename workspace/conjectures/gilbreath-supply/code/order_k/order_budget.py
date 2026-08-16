#!/usr/bin/env python3
"""Reconstruct and extend the correlation-order budget K*(n) of the SUPPLY fold.

DEFINITION (reconstructed from research/witness-hunt-n20-imported.txt and its
claim block research/notes/kstar_n20_table.md):

  C_K(h) := the empirical (K+1)-gram count vector of h in F2^n -- the histogram
            of the n-K overlapping windows h[i..i+K], i = 0..n-K-1,
            |window| = K+1.  No padding.  So C_1 is the 2-gram histogram
            (n-1 windows).  Because each (K+1)-gram contains a left and a right
            K-gram, C_K determines C_{K'} for every K' < K, hence "identical
            C_1..C_K" is equivalent to "identical C_K".

  Witness(n,K) := exists h, h' in F2^n with C_K(h) == C_K(h') but
                  S(n)^2(h) != S(n)^2(h'), where
                  S(n) = (n-2) - 2*nu2(n)   (signed fold excess).

  K*(n) := min{ K in [1, n-1] : NOT Witness(n,K) }
           -- the first correlation order at which S^2 is constant on every
           C_K-fiber.  The imported table (n=2..20) gives
           1,1,2,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10.

  GATE: reproduce (i) the n = 8 witness h=00000010 (bit 6), h'=00000100 (bit 5),
  both C_1 = (5,1,1,0), S^2 = 0 vs 4; and (ii) the FULL K* table n = 2..20
  including the n = 5 exception (K*(5) = 2 != ceil(5/2) = 3).  Negative control:
  Witness(n, n-1) is False at every n (full-order correlations determine h up to
  the kernel, and S^2 is kernel-invariant).

METHOD (exhaustive verification oracle, the explicit mandated bound):
Enumerate all 2^n strings, n <= 28 (~2.7e8; cap at n <= 26 if too slow).
S(n,h) for ALL h at once via the Walsh (Hadamard) transform: with
    A_d = { n-1-s : s bitwise submask of d } (positions the depth-d fold cell
reads) and x_j = (-1)^{h_j},
    S(n,h) = sum_{d=2}^{n-1} (-1)^{T(n,d)} = sum_d prod_{j in A_d} x_j
            = sum_v g[v] (-1)^{<h, v>},   g[v] = #{d : A_d = v},
which is the WHT of g.  O(n 2^n) time, O(2^n) space, exact integers.

Fiber detection: key(h) = sum over windows w of tag[w] (two independent 64-bit
tag families, so collisions are negligible); key is a function of the (K+1)-gram
histogram.  Group all h by key and check whether S^2 varies within any group.
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.supply_fold import s_sos  # canonical oracle, only for cross-checks


def fold_s_direct(n, h):
    """Signed excess S(n) = (n-2) - 2*nu2(n) for a single h (h as int/bitstring),
    using the canonical lib oracle for cross-checking."""
    bits = [(h >> j) & 1 for j in range(n)]
    _, ones = s_sos(n, bits)
    return (n - 2) - 2 * ones


def _rowmask(n, d):
    """A_d as an n-bit mask: bit j set iff j in {n-1-s : s submask of d}."""
    mask = 0
    for s in range(d + 1):
        if (s & d) == s:
            mask |= 1 << (n - 1 - s)
    return mask


def s_walsh(n):
    """S(n,h) for every h in [0, 2^n) as a numpy array indexed by h.

    g[v] = #{d in [2,n-1] : A_d = v}; S = WHT(g).  Exact int64.
    """
    size = 1 << n
    g = np.zeros(size, dtype=np.int64)
    seen = {}
    for d in range(2, n):
        m = _rowmask(n, d)
        g[m] += 1
        seen[m] = seen.get(m, 0) + 1
    a = g
    h = 1
    while h < size:
        a = a.reshape(-1, 2, h)
        x = a[:, 0, :].copy()
        y = a[:, 1, :].copy()
        a[:, 0, :] = x + y
        a[:, 1, :] = x - y
        a = a.reshape(-1)
        h *= 2
    return a  # S(h) at index h


def gram_key(n, h, K, tags0, tags1):
    """Commutative fiber key for h at order K: sum over (K+1)-grams of two
    independent tag values.  Two strings have equal (K+1)-gram histogram iff
    (with overwhelming probability) equal keys."""
    mask = (1 << (K + 1)) - 1
    k0 = 0
    k1 = 0
    for i in range(n - K):
        w = (h >> (i)) & mask
        k0 += tags0[w]
        k1 += tags1[w]
    return (k0, k1)


def witness(n, K, S, tags0, tags1):
    """Returns True and an example pair if Witness(n,K) holds.

    S is the full S array (index h).  Group h by fiber key; if any fiber has
    two distinct S^2 values, a witness exists.
    """
    size = 1 << n
    groups = {}
    for h in range(size):
        k = gram_key(n, h, K, tags0, tags1)
        s2 = int(S[h]) * int(S[h])
        if k in groups:
            prev = groups[k]
            if prev[0] != s2:
                return True, (prev[1], h, prev[0], s2)
        else:
            groups[k] = (s2, h)
    return False, None


def K_star(n, S, tags0, tags1, verbose=True):
    """Compute K*(n) = min K with no witness, and record witness truth per K."""
    kstar = None
    perK = []
    for K in range(1, n):  # K in [1, n-1]
        w, pair = witness(n, K, S, tags0, tags1)
        perK.append(w)
        if not w:
            kstar = K
            break
    if kstar is None:
        kstar = n - 1
    return kstar, perK


def tags_for(n):
    rng0 = np.random.default_rng(12345)
    rng1 = np.random.default_rng(67890)
    tags0 = [int(rng0.integers(0, 2**63)) for _ in range(1 << n)]
    tags1 = [int(rng1.integers(0, 2**63)) for _ in range(1 << n)]
    return tags0, tags1


def main():
    out = []
    out.append("order_budget: correlation-order budget K*(n) of the SUPPLY fold")
    out.append("sequence: n = 2..N over all 2^n strings (exhaustive oracle)")
    out.append("oracle: S(n)=(n-2)-2*nu2(n), nu2 via lib.supply_fold.s_sos (canonical floored fold, d in [2,n-1])")
    out.append("definition C_K(h) = empirical (K+1)-gram count vector of h; K*(n)=min{K: no witness}")

    N = 20  # gate: reproduce n=2..20
    print("=== GATE: reproduce K* n=2..20 (incl n=5 exception) and the n=8 witness ===")
    seq = {}
    for n in range(2, N + 1):
        S = s_walsh(n)
        tags0, tags1 = tags_for(n)
        # cross-check Walsh S against canonical oracle on a few h
        for h in [0, 1, (1 << (n - 1)), (1 << (n - 2)), (1 << (n - 1)) - 1]:
            sd = fold_s_direct(n, h)
            sw = int(S[h])
            assert sd == sw, (n, h, sd, sw)
        kstar, perK = K_star(n, S, tags0, tags1, verbose=False)
        seq[n] = kstar
        out.append(f"n={n:<3d} K*={kstar:<3d} witness-per-K={perK}")
        print(f"n={n:<3d} K*={kstar} witness-per-K={perK}")

    # Gate 1: the n=8 witness
    n8 = 8
    S8 = s_walsh(n8)
    t0, t1 = tags_for(n8)
    ok, pair = witness(n8, 1, S8, t0, t1)
    assert ok, "n=8 K=1 witness not found!"
    # find the specific pair
    h8a, h8b = None, None
    for h in range(1 << n8):
        for hp in range(h + 1, 1 << n8):
            if gram_key(n8, h, 1, t0, t1) == gram_key(n8, hp, 1, t0, t1):
                if int(S8[h]) ** 2 != int(S8[hp]) ** 2:
                    h8a, h8b = h, hp
                    break
        if h8a is not None:
            break
    cri = None  # to also report C1
    k0a = gram_key(h8a, 1, t0, t1)
    def c1counts(h):
        c = {0: 0, 1: 0, 2: 0, 3: 0}
        for i in range(n8 - 1):
            w = (h >> i) & 3
            c[w] += 1
        return (c[0], c[1], c[2], c[3])
    print(f"n=8 witness pair: h={bin(h8a)[2:].zfill(8)} (int {h8a}, bit {h8a.bit_length()-1}) "
          f"S2={int(S8[h8a])**2}; h'={bin(h8b)[2:].zfill(8)} (int {h8b}, bit {h8b.bit_length()-1}) S2={int(S8[h8b])**2}")
    print(f"  C1(h)={c1counts(h8a)}  C1(h')={c1counts(h8b)}  (expected (5,1,1,0) both)")
    assert c1counts(h8a) == (5, 1, 1, 0) and c1counts(h8b) == (5, 1, 1, 0)
    assert (int(S8[h8a]) ** 2, int(S8[h8b]) ** 2) == (0, 4), (int(S8[h8a]) ** 2, int(S8[h8b]) ** 2)
    # and that the specific bit-6/bit-5 pair is it
    # h=64 (bit6), h'=32 (bit5)
    hx, hy = 64, 32
    assert c1counts(hx) == (5, 1, 1, 0) and c1counts(hy) == (5, 1, 1, 0)
    assert int(S8[hx]) ** 2 == 0 and int(S8[hy]) ** 2 == 4
    print(f"  confirmed the stated pair h=00000010 (int 64, S2=0), h'=00000100 (int 32, S2=4)")

    # Gate 2: full sequence check
    expected = {2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 4, 8: 4, 9: 5, 10: 5, 11: 6,
                12: 6, 13: 7, 14: 7, 15: 8, 16: 8, 17: 9, 18: 9, 19: 10, 20: 10}
    print("Gate sequence check (n=2..20):")
    allok = True
    for n, k in expected.items():
        got = seq[n]
        ok = (got == k)
        print(f"  n={n:<3d} got K*={got} expected {k}  {'OK' if ok else 'MISMATCH'}")
        if not ok:
            allok = False
    assert allok, "K* sequence n=2..20 does NOT reproduce!"
    # n=5 exception check
    assert seq[5] == 2 and (5 + 1) // 2 == 3, "n=5 exception not reproduced"
    print(f"  n=5 exception reproduced: K*(5)=2 != ceil(5/2)=3")

    # Negative control: witness@K=n-1 False at every n
    print("Negative control (Witness(n, n-1) must be False at every n):")
    for n in range(2, N + 1):
        S = s_walsh(n)
        t0, t1 = tags_for(n)
        w, _ = witness(n, n - 1, S, t0, t1)
        assert not w, f"Witness(n={n}, K=n-1) was True!"
        print(f"  n={n:<3d} witness@K=n-1 = False  OK")

    print("=== GATE PASSED ===")

    with open(os.path.join(os.path.dirname(__file__), "..", "out", "order_budget_capture.txt"), "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
