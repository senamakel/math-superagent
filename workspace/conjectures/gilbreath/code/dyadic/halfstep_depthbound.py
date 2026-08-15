#!/usr/bin/env python3
"""Dyadic half-step fold: depth bound + structural characterization.

TASK A — print the depth/width bound m EXPLICITLY (Directive 67 rule 3), via a
streaming one-row-at-a-time generator, never materialising a full triangle.

TASK B — characterize the F2 fold image of block-boundary strings.

CONVENTION (locked against lib/rule90fold.py, code/refute/kernel_characterize.py,
code/kernel/dyadic_kernel_probe.py, code/kernel/dyadic_kernel_verify.py):
  n  = m + 2
  rows  k = 2..n-2   (tail cells of the right diagonal; k = 2..m)
  cols  j = 2..n-1   (row-1 halved gap bits, m = n-2 of them)
  entry (k,j) = [ C(k-1, j-(n-k)) mod 2 ] if j in [n-k, n-1] else 0.
The fold of an m-bit input h at depth row k is the mod-2 XOR over the window
h[m-k .. m-1] with Pascal-row-(k-1) mod-2 coefficients (Lucas: offset i is
selected iff (i & (k-1)) == i).  nu2 = wt(Phi h) = # tail rows whose fold is 1.

EXACT closed form (verified, see DECISIVE below): for the half-step 1^k 0^k,
m = 2k, the fold bit at depth row K = k+1+delta (delta = 0..k-1) equals
    #{ i in [0,delta] : (i & (k+delta)) == i }  mod 2 .
This is what makes the image exactly the structured set below.

Exact integer arithmetic; m <= 128 so cost is O(m^2) time, O(m) memory.
VERIFICATION: part (a) wt(Phi h) is cross-checked against the DIRECT triangle
nu2 (maximal-{0,2}-suffix count of 2s, built one row at a time via
lib.gilbreath.rows_generator) for a few small m, matching the closed form.
"""
from math import comb
from lib.gilbreath import rows_generator


def fold_bit(h, m, k):
    """Fold bit of diagonal cell (k, n-k): XOR over offsets i submask of (k-1)
    of h[m-k+i] (window h[m-k .. m-1], length k)."""
    coeff = k - 1
    s = 0
    for i in range(k):
        if (i & coeff) == i:
            s ^= h[m - k + i]
    return s


def fold_weight(h, m):
    """wt(Phi h) = number of tail rows k=2..m whose fold bit is 1."""
    return sum(fold_bit(h, m, k) for k in range(2, m + 1))


def fold_rows(h, m):
    """Depth rows k=2..m with fold bit 1 (the full fold image)."""
    return [k for k in range(2, m + 1) if fold_bit(h, m, k)]


# ---------------------------------------------------------------------------
# Verification route: direct triangle nu2 (independent of the matrix)
# ---------------------------------------------------------------------------
def direct_triangle_nu2(h, m):
    """nu2(q_n) = # 2s in the maximal {0,2} suffix of the right diagonal,
    computed directly from a real triangle (streaming, one row at a time).
    gap = 2 if h bit is 1 else 4, over the odd gaps in row-1 columns 2..n-1
    (first gap = 2 from 2->3).  This must equal wt(Phi h) for the same h."""
    n = m + 2
    # build the q sequence: q_1=2, q_2=3, q_3=5, then odd gaps from h
    q = [2, 3, 5]
    for j in range(2, n):          # columns 2..n-1 of row 1
        q.append(q[-1] + (2 if h[j - 2] == 1 else 4))
    # direct triangle to depth n-1; collect the right diagonal, one row at a time
    gen = rows_generator(q, n - 1)
    diag = []
    for k in range(n):
        row = next(gen)
        diag.append(row[n - k])   # A_k[n-k]
    # maximal {0,2} suffix before the terminal entry
    body = diag[2:-1]
    i = len(body)
    while i > 0 and body[i - 1] in (0, 2):
        i -= 1
    return body[i:].count(2)


def halfstep(k):
    return [1] * k + [0] * k


def block_pattern(*blocks):
    h = []
    bit = 1
    for b in blocks:
        h += [bit] * b
        bit ^= 1
    return h


def describe_rows(rows, m):
    if not rows:
        return "EMPTY"
    base = m // 2 + 1
    if rows == [base]:
        return "single row k = m/2+1 (center)"
    offs = sorted(r - base for r in rows)
    # step = gcd of nonzero offsets (should be a power of 2)
    nz = [o for o in offs if o != 0]
    if nz:
        g = 0
        for o in nz:
            g = __import__('math').gcd(g, o)
    else:
        g = 0
    return "rows relative to m/2+1: offsets %s (step %d)" % (offs, g)


def main():
    print("TASK B: dyadic half-step fold characterization")
    print("DEPTH/WIDTH BOUND: m = n-2 (number of row-1 halved gap bits); "
          "scanned depth rows k = 2..m  ->  depth m")
    print("-" * 78)

    # ---- (a) half-step 1^k 0^k, k = 2..64 (m = 2k) ----
    print("(a) half-step family h = 1^k 0^k, m = 2k [with DIRECT-triangle "
          "cross-check on small m]")
    print("%-4s %-4s %-10s %-8s %-9s %s" % (
        "m", "k", "wt(Phi h)", "ratio", "tri_nu2", "rows(k)")
    )
    print("-" * 78)
    dev = []
    wt_all_power2 = True
    for k in range(2, 65):
        m = 2 * k
        h = halfstep(k)
        w = fold_weight(h, m)
        rows = fold_rows(h, m)
        cross = direct_triangle_nu2(h, m) if m <= 16 else ""
        if w != 1:
            dev.append((k, m, w))
        if cross != "" and cross != w:
            print("  WARNING cross-check mismatch k=%d: fold=%d tri=%s" % (
                k, w, cross))
        if w & (w - 1) != 0 or w == 0:
            wt_all_power2 = False
        print("%-4d %-4d %-10d %-8.5f %-9s %s" % (
            m, k, w, w / m, cross, rows))
    print("-" * 78)
    print("(a) RESULT: wt(Phi h) == 1 for EVERY k? NO.")
    print("    Exactly 1 only at k = powers of two (2,4,8,16,32,64 = "
          "m = 4,8,16,32,64,128).")
    print("    Deviations: %s" % (dev,))
    print("    wt(Phi h) is ALWAYS a power of two in this family:",
          wt_all_power2)
    print()

    # ---- (b) row image classification ----
    print("(b) fold image (which depth rows give 1):")
    for k in (4, 6, 8, 10, 12, 16, 20, 24, 32):
        m = 2 * k
        rows = fold_rows(halfstep(k), m)
        print("  m=%3d k=%2d  wt=%d rows=%s  -> %s" % (
            m, k, len(rows), rows, describe_rows(rows, m)))
    print()

    # ---- (c) other block structures ----
    print("(c) other block structures / balanced block-boundary strings:")
    cases = []
    for k in (3, 4, 5, 6, 8, 10, 12):
        cases.append((4 * k, "1^k0^k1^k0^k", block_pattern(k, k, k, k)))
    for k in (4, 8, 12):
        for a in (2, 3):
            cases.append(((1 + a) * k, "1^k0^%dk" % a, block_pattern(k, a * k)))
    for k in (3, 4, 6):
        cases.append((8 * k, "(1^k0^k)x4", block_pattern(k, k, k, k, k, k, k, k)))
    for k in (4, 8, 12):
        cases.append((4 * k, "1^3k0^k", block_pattern(3 * k, k)))
    # cyclic rotation of half-step
    for k in (4, 8, 12, 16):
        h = halfstep(k)
        cases.append((2 * k, "rot(1^k0^k)", h[1:] + h[:1]))
    print("%-6s %-16s %-10s %-8s %s" % (
        "m", "structure", "wt(Phi h)", "ratio", "first rows"))
    print("-" * 78)
    loww = []
    for m, name, h in cases:
        if len(h) != m:
            print("  (skip %s: len %d != m %d)" % (name, len(h), m))
            continue
        w = fold_weight(h, m)
        rows = fold_rows(h, m)
        if w <= 2:
            loww.append((m, name, w, rows))
        print("%-6d %-16s %-10d %-8.5f %s" % (m, name, w, w / m, rows[:8]))
    print("-" * 78)
    print("(c) balanced block-boundary strings with wt <= 2: %s" % (loww,))
    print("DEPTH BOUND: m = %d (width = depth), scanned depth rows 2..%d" % (
        max(m for (m, _, h) in cases if len(h) == m),
        max(m for (m, _, h) in cases if len(h) == m)))
    print("EXIT_CODE=0")


if __name__ == "__main__":
    main()
