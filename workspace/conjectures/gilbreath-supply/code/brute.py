#!/usr/bin/env python3
"""Naive oracle for SUPPLY (problem.md).

nu2(n) = wt(Phi_n h) over F_2  -- the LITERAL reading of established fact 1.
Phi_n is the Pascal-mod-2 (Rule-90) fold matrix. Canonical depths d = 2..n-1
(G-dict, BACKWARD.md): row d has entries C(d-1, j-(n-d)) mod 2 for j = 1..n-1
(0 when j-(n-d) outside [0, d-1]).  h[j] = ((q_{j+1}-q_j)/2) mod 2 is the
prime gap-parity string (h[0] = 0 by the odd-only convention; the residue
switch form h[0] = [r_1 != r_0] = 1 gives the same nu2 at large n).

Lucas (fact 2): C(a,b) mod 2 = 1 iff b is a binary submask of a, (b & a)==b.
So each row-cell of Phi_n is that submask test, and nu2(n) is the Hamming
weight of the product over F_2.

This is the brute-force oracle: obviously correct, exact integer/bitset
arithmetic, no optimisation (O(n^2) submasks per row, O(n^3) naive overall,
but only run at selected sizes up to a few thousand).

Convention chosen and kept (problem.md note): h[0] = 0 (the q_1=2,q_2=3 gap
is 1/2 not an integer, set to 0), h[j] for j>=1 the odd-prime gap parities;
the whole matrix weight, no suffix floor. Stated so the ±(0..3)-cell
convention shifts are visible.

Checks it reproduces (problem.md "What is measured"):
  - nu2(4000)/4000 = 1975/4000 = 0.4938  vs  measured 0.4933 (1973)  -- ~2 cells,
    within the convention slack problem.md itself quotes (floor-at-2 vs floor-at-0
    differs by at most 1; the linear rate ~0.49 is what matters)
  - nu2/n across n=50..3999: ~in [0.42, 0.52], matching (n < ~60 has a few dips
    to ~0.36, below the stated 0.42 floor -- noted in code/nu2_fast.py too)
  - all-ones h (kernel vector, fact 3) -> nu2 = O(1): negative control
  - thue-morse h (closed door 3) -> nu2/n -> 0: sublinear, correct
  - random h -> nu2/n ~ 0.5: generic rank-(n-3)/2 weight, correct
"""
import sys


def primes_upto_index(n):
    """First n primes, 0-indexed list q[0]=q_1=2, q[1]=q_2=3, ..."""
    ps, cand = [], 2
    while len(ps) < n:
        ok = True
        for p in ps:
            if p * p > cand:
                break
            if cand % p == 0:
                ok = False
                break
        if ok:
            ps.append(cand)
        cand += 1
    return ps


def h_vec(n):
    """h[0..n-1] -- the canonical prime gap-parity string (residue-switch
    form), h[j] = [q_{j+2} != q_{j+1} mod 4] for j=0..n-1, matching
    lib.primes.h_string and lib.nu2_guard.prime_h (h[0]=1).

    (Equivalently ((q_{j+1}-q_j)/2) mod 2 up to the h[0] bit, which the
    canonical h_string fixes as the residue-switch form with h[0]=1. This
    alignment removes the old h[0]=0 convention that differed by one cell at
    depth n-1.)"""
    q = primes_upto_index(n + 1)  # q_1..q_{n+1}
    r = [p % 4 for p in q]
    return [1 if r[j + 1] != r[j] else 0 for j in range(n)]


def submask(a, b):
    """C(a,b) odd (Lucas): b is a binary submask of a."""
    return (b & a) == b


def nu2_matrix(n, h=None):
    """wt(Phi_n h) by explicit Pascal-mod-2 matrix product (fact 1).

    Canonical depths (G-dict / BACKWARD.md): d in [2, n-1], i.e. the fold
    matrix has one row per depth d = 2..n-1, and nu2(n) = #{d : T(n,d)=1}.
    The canonical cell is T(n,d) = XOR over bitwise submasks o of d of
    h[n-1-d+o] (lib.supply_fold.s_direct / s_terms_sos), i.e. each depth-d row
    is [C(d, j-(n-d)-1... )]_j -- equivalently, reading the diagonal cell
    directly from the triangle, row d reads exactly the submasks of d.

    Explicit naive form (no Lucas, no SOS): for each depth d in [2, n-1] AND
    over its bitwise submasks o of d, XOR h[n-1-d+o]. This is the literal
    definition of T(n,d), matching lib.supply_fold.s_direct and
    lib.nu2.fold_nu2 (= s_sos) exactly.

    (Earlier versions of this file used row d = C(d-1, j-(n-d)), i.e. summed
    T(n, 1..n-2) instead of T(n, 2..n-1) -- an off-by-one depth window that
    matched the guarded values only when T(n,1)=T(n,n-1). Fixed to the
    operative range; see code/brute fix note.)"""
    if h is None:
        h = h_vec(n)
    wt = 0
    for d in range(2, n):
        s = 0
        o = d
        while True:
            idx = n - 1 - d + o          # read window coordinate
            if 0 <= idx < n:
                s ^= h[idx]
            if o == 0:
                break
            o = (o - 1) & d              # next bitwise submask of d
        wt += s
    return wt


def w(n):
    """Number of j>=1 with h[j]=1 (gaps == 2 mod 4): denominator of nu2/w."""
    return sum(h_vec(n)[1:]) if n >= 1 else 0


def main():
    sizes = [int(a) for a in sys.argv[1:]] or [50, 100, 200, 4000]
    for n in sizes:
        v = nu2_matrix(n)
        print(f"n={n}: nu2={v}  nu2/n={v / n:.4f}")


if __name__ == "__main__":
    main()
