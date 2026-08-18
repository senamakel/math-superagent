"""Verify the directive-6 anchors by the independent sliding-window residue route.

Route (this task):
    M = 101001001.  S = infinite Fibonacci word (limit of S_0='0', S_1='01',
    S_n = S_{n-1}S_{n-2}); S = 0100101001001...

    Build a prefix W of S of length
        L = k + NextFib(k) - 1 + k
    where NextFib(k) = least Fibonacci strictly greater than k (lib.fibword
    next_fib, bisect_right => STRICT).  For each start r in [0, L-k] the
    window value w_r = (decimal value of W[r..r+k-1]) mod M, computed by the
    sliding recurrence
        w_{r+1} = (10*w_r - y_r * pow(10,k,M) + y_{r+k}) mod M,   y_i = digit at i
    starting from w_0 = value of the first k digits.  Distinct windows are
    de-duplicated by residue pairs under TWO moduli (M and a second M2), and
    the distinct count asserted equal to k+1 (Sturmian factor count).  Sum of
    squares of the distinct window residues mod M = Psi(k) mod M.

    A single-modulus set is NOT sufficient: distinct length-k factors can be
    congruent mod M (k=10 gives both M=101001001 and 10*M as factors, so both
    are residue 0), so a single-modulus count can drop below k+1.  The two-
    modulus pair is exact: when the pair-count equals k+1, each pair
    corresponds to exactly one distinct factor, and r^2 = (v mod M)^2 = v^2
    (mod M), so summing r^2 over the distinct pairs equals the true Psi mod M.

Reported checks:
    k=3    -> 20302, factor set {1,10,100,101}
    k=10   -> 10699667
    k=10^4 -> 34432237, distinct 10001
    k=10^6 -> 20938836, distinct 1000001
plus a cross-check of k=1..60 against the string oracle code/brute.py psi_of.

O(1) per window (sliding recurrence), so k=10^6 (~3.35M-digit prefix, ~2.35M
windows) runs in seconds.
"""

import sys
import time

from lib.fibword import fib_prefix, next_fib
from brute import psi_of, fib_word

M = 101001001
# second modulus for exact-pair de-duplication of distinct window values
M2 = 1000000007


def next_fib_pair(k):
    """(nf, L) with nf = strict next fibonacci > k, L = window-prefix length."""
    nf = next_fib(k)
    return nf, k + nf - 1 + k


def window_residues(k, W):
    """Return (psi, pair_count, single_count) for distinct length-k windows of W.

    psi   = sum of squares of distinct window decimal values mod M (dedup by
            the two-modulus residue pair).
    pair_count     = number of distinct (value mod M, value mod M2) pairs
            (== k+1 expected), exact when it equals k+1.
    single_count   = number of distinct residues mod M alone (diagnostic; can
            be < k+1 when distinct factors are congruent mod M).

    Two independent sliding residues must be kept: taking the mod-M residue
    and folding it mod M2 does NOT give the true value mod M2 (e.g. the
    factors 10*M and M are both 0 mod M but differ mod M2), so the M2 residue
    is evolved by its own copy of the sliding recurrence.
    """
    L = len(W)
    p10k = pow(10, k, M)          # 10^k mod M
    p10k2 = pow(10, k, M2)        # 10^k mod M2
    digits = [ord(c) - 48 for c in W]
    w1 = 0  # value mod M
    w2 = 0  # value mod M2
    for i in range(k):
        w1 = (w1 * 10 + digits[i]) % M
        w2 = (w2 * 10 + digits[i]) % M2
    pairs = set()
    sing = set()
    ps = 0
    for r in range(L - k + 1):
        key = (w1, w2)
        if key not in pairs:
            pairs.add(key)
            ps = (ps + w1 * w1) % M
        sing.add(w1)
        if r + k < L:
            w1 = (10 * w1 - digits[r] * p10k + digits[r + k]) % M
            w2 = (10 * w2 - digits[r] * p10k2 + digits[r + k]) % M2
    return ps, len(pairs), len(sing)


def run(k):
    nf, L = next_fib_pair(k)
    W = fib_prefix(L)
    t0 = time.time()
    ps, pc, sc = window_residues(k, W)
    dt = time.time() - t0
    return ps, pc, sc, L, nf, dt


def main():
    out = sys.stdout

    def line(s=""):
        print(s, file=out)
        out.flush()

    line("Sliding-window residue route — directive-6 anchor verification")
    line(f"M = {M}  (second modulus M2 = {M2})")
    line("=" * 60)

    # ---- k=3 : factor set and value
    _, _, _, L3, nf3, _ = run(3)
    # reconstruct the factor set explicitly for the report
    W3 = fib_prefix(L3)
    set3 = sorted({int(W3[r:r + 3]) for r in range(len(W3) - 3 + 1)})
    line(f"k=3    prefix L={L3} NextFib={nf3}")
    line(f"       factor set = {set3}")
    line(f"       Psi(3) = {sum(x * x for x in set3)}  (want 20302), "
         f"count={len(set3)} (want 4)")
    line(f"       match = {set3 == [1, 10, 100, 101] and len(set3) == 4}")

    # ---- k=10
    ps10, pc10, sc10, L10, nf10, _ = run(10)
    line(f"k=10   prefix L={L10} NextFib={nf10}")
    line(f"       Psi(10) mod M = {ps10}  (want 10699667), "
         f"pair-count={pc10} (want 11), single-count={sc10}")
    line(f"       match = {ps10 == 10699667 and pc10 == 11}")

    # ---- k=10^4
    ps4, pc4, sc4, L4, nf4, dt4 = run(10 ** 4)
    line(f"k=10^4 prefix L={L4} NextFib={nf4}  ({dt4:.1f}s)")
    line(f"       Psi(10^4) mod M = {ps4}  (want 34432237), "
         f"distinct={pc4} (want 10001), single-count={sc4}")
    line(f"       match = {ps4 == 34432237 and pc4 == 10001}")

    # ---- k=10^6
    t0 = time.time()
    ps6, pc6, sc6, L6, nf6, _ = run(10 ** 6)
    dt6 = time.time() - t0
    line(f"k=10^6 prefix L={L6} NextFib={nf6}  ({dt6:.1f}s wall)")
    line(f"       Psi(10^6) mod M = {ps6}  (want 20938836), "
         f"distinct={pc6} (want 1000001), single-count={sc6}")
    line(f"       match = {ps6 == 20938836 and pc6 == 1000001}")

    # ---- cross-check k=1..60 vs string oracle
    line("=" * 60)
    line("Cross-check k=1..60 against code/brute.py psi_of")
    bad = []
    for k in range(1, 61):
        ps, pc, sc, _, _, _ = run(k)
        exact, _ = psi_of(fib_word(3 * k), k)
        ex = exact % M
        if ps != ex or pc != k + 1:
            bad.append((k, ps, ex, pc, sc, k + 1))
    line(f"       mismatches: {bad if bad else 'none'}")
    line(f"       all agree with oracle on value and count = {not bad}")

    # ---- summary
    line("=" * 60)
    allok = (set3 == [1, 10, 100, 101] and len(set3) == 4
             and ps10 == 10699667 and pc10 == 11
             and ps4 == 34432237 and pc4 == 10001
             and ps6 == 20938836 and pc6 == 1000001
             and not bad)
    line(f"ALL CHECKS PASS = {allok}")
    line(f"Wall time for k=10^6: {dt6:.1f}s")


if __name__ == "__main__":
    main()
