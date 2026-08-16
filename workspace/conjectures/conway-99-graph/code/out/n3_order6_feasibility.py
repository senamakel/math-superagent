#!/usr/bin/env python3
"""
n3_order6_feasibility.py

For each family member srg(n,k,1,2) with (n,k) in
{(9,4),(99,14),(243,22),(6273,112),(494019,994)},
determine which values of n3 (number of pairs of triangles joined by
exactly 2 edges = the one free order-6 subgraph count) are arithmetically
admissible: every one of the 62 Reimbayev order-6 induced-subgraph counts
n_i must be a NONNEGATIVE INTEGER.

All 62 formulas n_i = (n,k)-term +/- c*n3 are transcribed verbatim from
research/sources/reimbayev-subgraphs-order-six-body.full.md (the "summary"
section, n1..n62), using exact Fraction arithmetic.  No hand-simplification.

Output: per (n,k) minimal admissible n3, whether n3=0 is feasible, the
residue class of admissible n3 (from the 1/3,2/3,4/3 fractional
coefficients), and the k=14 verdict.
"""

from fractions import Fraction

# ---------------------------------------------------------------------------
# The 62 exact formulas.  Each returns Fraction n_i(n, k, n3).
# Structure: a coefficient polynomial in k (sometimes also n), a denominator D,
# the common factor n*k*(k-2)*(k-4) (NOT always present), and a signed n3
# coefficient.  Transcribed verbatim; nothing simplified by hand.
# ---------------------------------------------------------------------------

def n1(n, k, n3):
    return Fraction(1, 12) * n * k * (k - 2) - Fraction(n3, 3)

def n2(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2)

def n3(n, k, n3):
    return n3

def n4(n, k, n3):
    return 2 * n3

def n5(n, k, n3):
    return Fraction(1, 8) * n * k * (k - 2) * (k - 4) - n3

def n6(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 3) - 2 * n3

def n7(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4)

def n8(n, k, n3):
    return n * k * (k - 2) * (k - 4) - 2 * n3

def n9(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) - n3

def n10(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) - 2 * n3

def n11(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k - 6) + 4 * n3

def n12(n, k, n3):
    return Fraction(1, 12) * n * k * (k - 2) * (2 * k**2 - 21 * k + 53) + n3

def n13(n, k, n3):
    return Fraction(1, 32) * n * k * (k - 2) * (k - 4) * (k**2 - 12 * k + 42) - n3

def n14(n, k, n3):
    return Fraction(1, 144) * n * k * (k - 2) * (k - 4) * (k - 12) + Fraction(n3, 3)

def n15(n, k, n3):
    return Fraction(1, 8) * n * k * (k - 2) * (k - 4)

def n16(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4)

def n17(n, k, n3):
    return n * k * (k - 2) * (k - 4)

def n18(n, k, n3):
    return n * k * (k - 2) * (k - 4) - 4 * n3

def n19(n, k, n3):
    return Fraction(1, 12) * n * k * (k - 2) * (k - 4) * (k - 6)

def n20(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4)**2

def n21(n, k, n3):
    return Fraction(1, 6) * n * k * (k - 2) * (k - 3) * (k - 4) + Fraction(2, 3) * n3

def n22(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k - 5)

def n23(n, k, n3):
    return n * k * (k - 2) * (k - 4) * (k - 5) + 4 * n3

def n24(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k - 6) + 2 * n3

def n25(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k - 7) + 4 * n3

def n26(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k - 6)

def n27(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k - 5) + 2 * n3

def n28(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k - 6) + 2 * n3

def n29(n, k, n3):
    return n * k * (k - 2) * (k - 4) * (k - 6) + 6 * n3

def n30(n, k, n3):
    return Fraction(1, 120) * n * k * (k - 2) * (k - 4) * (k - 6) * (k - 8)

def n31(n, k, n3):
    return Fraction(1, 6) * n * k * (k - 2) * (k - 4) * (k - 5) * (k - 6)

def n32(n, k, n3):
    return Fraction(1, 8) * n * k * (k - 2) * (k - 4) * (k**2 - 10 * k + 26) - n3

def n33(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k**2 - 10 * k + 28) - 6 * n3

def n34(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k**2 - 11 * k + 34) - 8 * n3

def n35(n, k, n3):
    return Fraction(1, 2) * n * k * (k - 2) * (k - 4) * (k**2 - 11 * k + 36) - 10 * n3

def n36(n, k, n3):
    poly = (k**7 - 24 * k**6 + 248 * k**5 - 1520 * k**4 + 6436 * k**3
            - 19520 * k**2 + 38896 * k - 40704)
    return Fraction(1, 23040) * n * k * (k - 2) * (k - 4) * poly + Fraction(n3, 3)

def n37(n, k, n3):
    poly = (k**6 - 22 * k**5 + 212 * k**4 - 1208 * k**3 + 4484 * k**2
            - 10456 * k + 12288)
    return Fraction(1, 768) * n * k * (k - 2) * (k - 4) * poly - 3 * n3

def n38(n, k, n3):
    poly = (k**5 - 20 * k**4 + 172 * k**3 - 828 * k**2 + 2300 * k - 3048)
    return Fraction(1, 96) * n * k * (k - 2) * (k - 4) * poly + 6 * n3

def n39(n, k, n3):
    poly = (k**5 - 20 * k**4 + 176 * k**3 - 884 * k**2 + 2588 * k - 3624)
    return Fraction(1, 128) * n * k * (k - 2) * (k - 4) * poly + 6 * n3

def n40(n, k, n3):
    poly = (k**4 - 18 * k**3 + 130 * k**2 - 460 * k + 696)
    return Fraction(1, 48) * n * k * (k - 2) * (k - 4) * poly - 2 * n3

def n41(n, k, n3):
    poly = (k**4 - 18 * k**3 + 136 * k**2 - 524 * k + 892)
    return Fraction(1, 16) * n * k * (k - 2) * (k - 4) * poly - 14 * n3

def n42(n, k, n3):
    poly = (k**4 - 17 * k**3 + 120 * k**2 - 430 * k + 684)
    return Fraction(1, 16) * n * k * (k - 2) * (k - 4) * poly - 10 * n3

def n43(n, k, n3):
    poly = (k**4 - 18 * k**3 + 130 * k**2 - 460 * k + 720)
    return Fraction(1, 288) * n * k * (k - 2) * (k - 4) * poly - Fraction(2, 3) * n3

def n44(n, k, n3):
    return Fraction(1, 24) * n * k * (k - 2) * (k - 4) * (k - 6) * (n - 5 * k + 13)

def n45(n, k, n3):
    return Fraction(1, 64) * n * k * (k - 2) * (k - 4) * (k - 6) * (k**2 - 8 * k + 26) + n3

def n46(n, k, n3):
    poly = (k**3 - 14 * k**2 + 72 * k - 140)
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * poly + 8 * n3

def n47(n, k, n3):
    return Fraction(1, 16) * n * k * (k - 2) * (k - 4) * (k - 6) * (k**2 - 8 * k + 22) + 2 * n3

def n48(n, k, n3):
    poly = (k**3 - 14 * k**2 + 75 * k - 160)
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * poly + 14 * n3

def n49(n, k, n3):
    poly = (k**3 - 16 * k**2 + 94 * k - 216)
    return Fraction(1, 48) * n * k * (k - 2) * (k - 4) * poly + 2 * n3

def n50(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k**2 - 10 * k + 30) - 4 * n3

def n51(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k**2 - 9 * k + 22) - 2 * n3

def n52(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (n - 5 * k + 12)

def n53(n, k, n3):
    return Fraction(1, 5) * n * k * (k - 2) * (k - 4) * (n - 5 * k + 15) - 2 * n3

def n54(n, k, n3):
    return Fraction(1, 16) * n * k * (k - 2) * (k - 4) * (k - 6)

def n55(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k - 6) + 2 * n3

def n56(n, k, n3):
    return Fraction(1, 4) * n * k * (k - 2) * (k - 4) * (k**2 - 10 * k + 30) - 4 * n3

def n57(n, k, n3):
    poly = (k**4 - 18 * k**3 + 140 * k**2 - 564 * k + 996)
    return Fraction(1, 192) * n * k * (k - 2) * (k - 4) * poly - Fraction(4, 3) * n3

def n58(n, k, n3):
    poly = (k**3 - 15 * k**2 + 86 * k - 190)
    return Fraction(1, 8) * n * k * (k - 2) * (k - 4) * poly + 8 * n3

def n59(n, k, n3):
    return Fraction(1, 24) * n * k * (k - 2) * (k - 4) * (k - 6) * (k**2 - 10 * k + 34) + 2 * n3

def n60(n, k, n3):
    return Fraction(1, 8) * n * k * (k - 2) * (k - 4) * (k**2 - 12 * k + 38) - 2 * n3

def n61(n, k, n3):
    poly = (k**3 - 16 * k**2 + 96 * k - 220)
    return Fraction(1, 16) * n * k * (k - 2) * (k - 4) * poly + 5 * n3

def n62(n, k, n3):
    return Fraction(1, 24) * n * k * (k - 2) * (k - 4) * (k**2 - 14 * k + 54) - 2 * n3


ALL_N = [
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16,
    n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30,
    n31, n32, n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44,
    n45, n46, n47, n48, n49, n50, n51, n52, n53, n54, n55, n56, n57, n58,
    n59, n60, n61, n62,
]

FAMILY = [(9, 4), (99, 14), (243, 22), (6273, 112), (494019, 994)]


def n3_upper_cap(n, k):
    """
    Tightest arithmetic upper bound on n3 coming from the nonnegativity
    constraints n_i = B_i + c_i*n3 >= 0 with c_i < 0, i.e. n3 <= B_i/(-c_i).
    Iterating the finite cap is exact for a nonneg-integer search.
    """
    cap = None
    argmin = None
    for fi, f in enumerate(ALL_N, 1):
        b = f(n, k, 0)              # base value (rational)
        c = f(n, k, 1) - b          # signed n3 coefficient (rational)
        if c < 0:
            lim = b / (-c)          # n3 <= lim
            lim_floor = int(lim)    # floor (lim is nonneg; could be huge)
            if cap is None or lim_floor < cap:
                cap = lim_floor
                argmin = fi
    return cap, argmin


def linear_bounds(n, k):
    """
    Admissible n3 set = { n3 integer : L <= n3 <= U AND all 62 n_i integer }.
    Returns (L, U) as Fractions (rational) plus the base-integerity check.
    Each n_i = base + c*n3 is linear in n3, so nonnegativity is an interval.
    """
    L = Fraction(0)          # nonnegativity lower (n_i>=0 for c>0)
    U = None                 # upper (n_i>=0 for c<0)
    fixed_ok = True          # formulas with c==0 must be nonneg-integer on their own
    for f in ALL_N:
        base = f(n, k, 0)
        c = f(n, k, 1) - base
        if c == 0:
            if base < 0 or base.denominator != 1:
                fixed_ok = False
        elif c > 0:
            # base + c*n3 >= 0  =>  n3 >= -base/c
            lb = -base / c
            if lb > L:
                L = lb
        else:
            # base + c*n3 >= 0  =>  n3 <= base/(-c)
            ub = base / (-c)
            if U is None or ub < U:
                U = ub
    return L, U, fixed_ok


def integer_residue_classes(n, k):
    """
    Which residues r (mod P) make every n_i an integer.  Each n_i = base+c*n3
    with c=p/q in lowest terms has period q in n3 (mod 1), so overall period
    P = lcm of denominators of the fractional c's.
    """
    from math import gcd
    P = 1
    for f in ALL_N:
        base = f(n, k, 0)
        c = f(n, k, 1) - base
        P = P * c.denominator // gcd(P, c.denominator)
    good_r = []
    for r in range(P):
        if all((f(n, k, r)).denominator == 1 for f in ALL_N):
            good_r.append(r)
    return P, good_r


def main():
    lines = []
    lines.append("n3_order6_feasibility.py -- Reimbayev 62 order-6 subgraph-count "
                 "formulas, exact Fraction arithmetic")
    lines.append("method: n_i = (n,k)-term +/- c*n3 ; require every n_i a nonnegative "
                 "integer; N_cap = tightest nonneg upper bound on n3")
    lines.append("inputs: family {(9,4),(99,14),(243,22),(6273,112),(494019,994)}; "
                 "all 62 formulas transcribed verbatim from source summary")
    lines.append("")
    lines.append(f"{'family':<18}{'0-adm':<6}{'min-adm':<9}{'bounds':<20}{'residue-class'}")
    lines.append(f"{'':-<60}")
    verdict = None
    for (n, k) in FAMILY:
        cap, argmin = n3_upper_cap(n, k)
        L, U, fixed_ok = linear_bounds(n, k)
        P, good_r = integer_residue_classes(n, k)

        # smallest integer n3 >= max(L,0) lying in an admissible residue class
        if not fixed_ok or U is None or int(Fraction(L)) > U:
            min_adm = None
            zero_ok = False
        else:
            lo = max(Fraction(0), L)
            lo_int = lo.numerator // lo.denominator
            if lo_int < lo:
                lo_int += 1
            cand = None
            for r in good_r:
                x = lo_int + ((r - lo_int) % P)
                if x > U:
                    continue
                if cand is None or x < cand:
                    cand = x
            min_adm = cand
            zero_ok = (0 >= L and 0 <= U and 0 % P in good_r and fixed_ok)

        if good_r and len(good_r) < P:
            res_str = "n3≡" + " or ".join(str(r) for r in good_r) + f" (mod {P})"
        elif good_r:
            res_str = "all residues"
        else:
            res_str = "none"

        # brute-force cross-check where cap is small enough
        bf = None
        if cap <= 30000:
            bf = [x for x in range(0, cap + 1)
                  if all(f(n, k, x).denominator == 1 and f(n, k, x) >= 0
                         for f in ALL_N)]
            bf_min = bf[0] if bf else None
            bf_zero = (0 in bf)

        lines.append(f"({n:>6},{k:>3})  {str(zero_ok):<6}{str(min_adm):<9}"
                     f"L={float(L):.3g} U={float(U):.3g}  {res_str}"
                     + (f"  [brute cf {bf_min}]" if bf is not None else ""))
        if (n, k) == (99, 14):
            if zero_ok:
                verdict = ("k=14 (n=99): n3=0 IS arithmetically admissible -- "
                           "order-6 integrality alone does NOT force n3>=1")
            else:
                verdict = ("k=14 (n=99): n3=0 is NOT admissible -- order-6 "
                           "integrality alone forces n3>=%s" % (min_adm,))
    lines.append("")
    lines.append("VALIDATION (controllers): k=4 (n=9, rook exists) and k=22 "
                 "(n=243, BvLS exists) MUST admit n3=0.")
    lines.append("Brute-force cross-check (all formulas nonneg-int) run for "
                 "every (n,k) with cap<=30000, against analytic interval+residue.")
    lines.append("VERDICT k=14: " + verdict)
    txt = "\n".join(lines) + "\n"
    print(txt)
    with open("code/out/n3_order6_feasibility.captured.txt", "w") as fh:
        fh.write(txt)
    return verdict


if __name__ == "__main__":
    v = main()
    print("\n[returned verdict]")
    print(v)
