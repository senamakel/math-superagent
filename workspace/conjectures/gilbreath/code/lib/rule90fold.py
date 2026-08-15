#!/usr/bin/env python3
"""The Rule-90 (Pascal mod 2) fold of the halved row-1 gap-parity bits onto the
right diagonal.

For an even row-1 entry A_1[j] (all j>=1 in the prime triangle), write
h[c] = (A_1[c]//2) % 2  ( = 1  iff the gap ending at prime index c is == 2 mod 4 ).
In the even interior, halved entries are integer and evolve by XOR:
    A'_{k+1}(j) = A'_k(j) XOR A'_k(j+1)      (|a-b|/2 = (a/2) XOR (b/2) mod 2)
so the halved diagonal cell at depth k, column n-k satisfies
    (delta_k(q_n)/2) mod 2 =  XOR_{i: (i & (k-1)) == i}  h[n-k+i]
i.e. a Pascal-row-(k-1) mod-2 weighted XOR over the fixed ancestor window
[n-k, n-1] of row-1 (the k = n-2 cell alone reaches column 2, and the union
over the {0,2}-tail cells k = 2..n-2 is the whole interval [2, n-1]).

Exports:
  halved_gap_bits(primes)      -> h indexed by prime index c (h[c] for c>=1)
  fold_cell_bit(hcol, k, n)    -> fold bit of diagonal cell (k, n-k)
  fold_bits(hcol, n)           -> [fold bit for k = 2..n-2]
  fold_weight(hcol, n)         -> number of 1-bits among fold_bits
  fold_weight_h(h, m)          -> weight of fold of an abstract m-bit h
                                   (h[0..m-1] = columns 2..n-1, m = n-2)

All integer. The fold identity is checked against the direct integer diagonal
in code/gap_analysis/random_analogue_fold_anchor.py.
"""


def halved_gap_bits(primes):
    """h[c] = ((gap to prime with index c)//2) % 2, for c >= 1.
    primes[0]=2; A_1[c] = primes[c+1]-primes[c] is the gap ending at index c."""
    return [((primes[c + 1] - primes[c]) // 2) % 2
            for c in range(len(primes) - 1)]


def fold_cell_bit(hcol, k, n):
    """Mod-2 fold bit of the right-diagonal cell (k, n-k).
    XOR over i in 0..k-1 with C(k-1,i) odd (i.e. (i & (k-1)) == i) of
    hcol[n-k+i] (row-1 halved bits over the ancestor window [n-k, n-1])."""
    # n - k + i with i = 0..k-1 covers columns [n-k, n-1]; hcol is indexed by column.
    coeff = k - 1
    s = 0
    for i in range(k):
        if (i & coeff) == i:
            s ^= hcol[n - k + i]
    return s


def fold_bits(hcol, n):
    """Fold bits of diagonal cells k = 2..n-1 (n-2 values), matching the range
    over which cycle_and_nu2 scans the maximal {0,2} suffix (body = indices
    2..n-1 of the length-n+1 diagonal delta_0..delta_n)."""
    return [fold_cell_bit(hcol, k, n) for k in range(2, n)]


def fold_weight(hcol, n):
    """Number of 1-bits among the diagonal fold cells k = 2..n-1."""
    return sum(fold_bits(hcol, n))


def fold_weight_h(h, m):
    """Weight of the fold of an abstract m-bit input h (h[0..m-1] = columns
    2..n-1 with m = n-2).  Output cells k = 2..n-1 (k = 2..m+1 in the shifted
    index), each an XOR of the k-1 lower input bits with Pascal-row-(k-2)
    mod-2 coefficients, ending at input index m-1."""
    w = 0
    for k in range(2, m + 1):
        coeff = k - 1
        s = 0
        for i in range(k):
            if (i & coeff) == i:
                s ^= h[m - k + i]
        w += s
    return w
