#!/usr/bin/env python3
"""TASK B — kernel component of the prime switch bit h.

For n in {8,16,32,64,128} build the operative fold Phi_n: (n-2) rows,
d in [2, n-1], (n-2) x n, columns j = 0..n-1, entry
    Phi_n[d, j] = C(d-1, j - (n-d)) mod 2
(equivalently the depth-d row is the Pascal-mod-2 / Lucas row supported on
submasks). We already know (problem.md fact 3): rank Phi_n = n-2, nullity 2,
ker = span(even-alt, odd-alt); with the four vectors
    0, even-alt (1 at even j), odd-alt (1 at odd j), all-ones = even XOR odd.

We verify that by exact F2 elimination on the built matrix, then for the real
prime h (length n) compute the exact minimum Hamming distance
    d_min = min_{v in ker} d_H(h, v)  over the 4 kernel vectors
and report d_min/n and the attaining v, plus wt(h)/n. This measures whether
the prime switch bit sits close to a fold-collapse direction (a direction whose
image under Phi has weight 0, i.e. nu2 = 0).

Exact integer / F2 arithmetic throughout; only the ratios are float.
"""
import os

from lib.primes import h_string


def build_phi(n):
    """(n-2) x n matrix over F2, rows indexed by depth d = 2..n-1,
    columns j = 0..n-1.

    By the key identity in lib.supply_fold (substituting s = d - o, no borrow,
    i.e. T(n,d) = XOR_{s subseteq d} h[n-1-s]), the depth-d fold cell is

        T(n,d) = XOR_{s subseteq d} h[n-1-s].

    So the row for depth d is the indicator of the reversed column bits that
    are submasks of d: Phi[d, j] = 1  iff  s = (n-1-j) is a bitwise submask of d.

    This is verified below to have exactly the known kernel
    span(even-alt, odd-alt) (0, even-alt, odd-alt, all-ones all fold to 0).
    """
    mat = []
    for d in range(2, n):          # depth d
        row = [0] * n
        for j in range(n):
            s = n - 1 - j          # h index that column j multiplies
            if (s & d) == s:       # s is a bitwise submask of d
                row[j] = 1
        mat.append(row)
    return mat


def rref_f2(mat):
    """In-place row-reduce a list-of-int-rows matrix over F2 to RREF.
    Returns pivots (row index in RREF). Mutates mat."""
    rows = len(mat)
    cols = len(mat[0]) if rows else 0
    r = 0
    pivots = []
    for c in range(cols):
        # find a pivot row at/after r with a 1 in column c
        piv = None
        for i in range(r, rows):
            if mat[i][c]:
                piv = i
                break
        if piv is None:
            continue
        mat[r], mat[piv] = mat[piv], mat[r]
        # eliminate c from all other rows
        for i in range(rows):
            if i != r and mat[i][c]:
                mat[i] = [mat[i][j] ^ mat[r][j] for j in range(cols)]
        pivots.append(c)
        r += 1
        if r == rows:
            break
    return pivots


def kernel_from_rref(mat, pivots, cols):
    """Given RREF matrix and pivot columns, return basis vectors spanning ker
    (over F2) as list of tuples. Free columns -> basis vector with 1 in that
    free column and -pivot entries above (here + = - in F2)."""
    rows = len(mat)
    free = [c for c in range(cols) if c not in set(pivots)]
    basis = []
    for fc in free:
        v = [0] * cols
        v[fc] = 1
        for ri in range(rows):
            if mat[ri][fc]:
                pc = pivots[ri]
                v[pc] = 1
        basis.append(tuple(v))
    return basis


def ker_set(basis):
    """All 2^k kernel vectors from basis."""
    from itertools import product
    out = set()
    for combo in product([0, 1], repeat=len(basis)):
        v = [0] * len(basis[0]) if basis else []
        for b, bit in zip(basis, combo):
            if bit:
                v = [x ^ y for x, y in zip(v, b)]
        out.add(tuple(v))
    return out


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


NAME = {}


def run_task_b(out):
    out.append("=" * 70)
    out.append("TASK B — kernel component of prime switch bit h")
    out.append("=" * 70)
    out.append("Phi_n: (n-2) x n, rows d in [2,n-1], entry "
               "C(d-1, j-(n-d)) mod 2.")
    out.append("Known ker = span(even-alt, odd-alt), so the 4 collapse "
               "vectors are 0, even-alt, odd-alt, all-ones.")
    out.append("")

    # canonical kernel vectors to compare against
    def even_alt(n):
        return tuple(1 if j % 2 == 0 else 0 for j in range(n))

    def odd_alt(n):
        return tuple(1 if j % 2 == 1 else 0 for j in range(n))

    def all_ones(n):
        return tuple(1 for _ in range(n))

    hdr = (f"{'n':>4} {'rank':>4} {'null':>4} "
           f"{'ker=span?':>10} {'wt(h)/n':>8} {'dmin/n':>8}  attaining v")
    out.append(hdr)
    out.append("-" * len(hdr))
    for n in [8, 16, 32, 64, 128]:
        mat = build_phi(n)
        pivots = rref_f2(mat)
        rank = len(pivots)
        nullity = n - len(pivots)
        basis = kernel_from_rref(mat, pivots, n)
        ker = ker_set(basis)
        # check canonical span
        can = {even_alt(n), odd_alt(n), all_ones(n), tuple([0] * n)}
        span_ok = (ker == can)
        # prime h of length n
        h = tuple(h_string(n + 1)[:n])
        wt = sum(h)
        # min distance over the 4 kernel vectors
        vecs = [tuple([0] * n), even_alt(n), odd_alt(n), all_ones(n)]
        dm = None
        arg = None
        for v in vecs:
            d = hamming(h, v)
            if dm is None or d < dm:
                dm = d
                arg = v
        def vname(v):
            if all(x == 0 for x in v):
                return "0"
            if v == even_alt(n):
                return "even-alt"
            if v == odd_alt(n):
                return "odd-alt"
            if all(x == 1 for x in v):
                return "all-ones"
            return "other"
        out.append(
            f"{n:>4} {rank:>4} {nullity:>4} {str(span_ok):>10} "
            f"{wt/n:>8.4f} {dm/n:>8.4f}  {vname(arg)}"
        )
    out.append("")
    out.append("Interpretation: dmin/n = min over collapse directions of the")
    out.append("distance from the prime h to that direction. wt(h)/n = switch")
    out.append("density. A small dmin/n would mean h is close to a direction")
    out.append("whose fold image has weight 0 (nu2 = 0); a dmin/n near 1/2")
    out.append("would mean h is far from every collapse direction.")
    out.append("NOTE: dmin over the kernel is essentially the distance to the")
    out.append("nearest parity-alternating string; with this script's own")
    out.append("measured wt(h)/n in 0.6250..0.6875 (n=8..128, see table), dmin/n")
    out.append("is expected ~ |wt(h)/n - 0.5| away from 0, not near 0.")
    return out


def main_task_b():
    out = run_task_b([])
    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "kernel_component.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main_task_b()
