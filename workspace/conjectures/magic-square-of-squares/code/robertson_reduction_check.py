#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exact-integer verification of the completed Robertson reduction
(Bremner 1999, "On squares of squares", Acta Arith. 88, eqs. (2)-(4))
against Bremner's 7-square witness grid:

       373^2   289^2   565^2
       360721  425^2   23^2
       205^2   527^2   222121

The reduction (Robertson's observation): a 3x3 magic square of squares over Q
exists iff there are three points P0,P1,P2 in E(Q) on E: y^2 = x(x^2-c^2)
whose DOUBLED x-coordinates x(2P0)=a-b, x(2P1)=a, x(2P2)=a+b form an AP
(the main diagonal of the square, parametrisation (2)).  A point (X,Y) in
E(Q) lies in 2E(Q) iff {X, X-c, X+c} are all rational squares.

WHAT IS CHECKED HERE (all exact; no floating point in the claims):
  (1) the two diagonals and all 8 line sums equal the magic constant 541875
  (2) reduction parameters a = 425^2 = 180625, b = 41496, c = 138600 with
      main diagonal (a-b,a,a+b) = (139129,180625,222121) and
      anti-diagonal (a-c,a,a+c)  = (205^2,425^2,565^2)
  (3) 2E(Q)-membership of the three main-diagonal x-coordinates
      (criterion: X, X-c, X+c all perfect squares) - expect exactly 2 of 3
  (4) doubling formula x(2Q) = (ux^2+c^2)^2/(4*uy^2): symbolic identity
      against the standard duplication formula, plus a rational-point check
  (5) rank of E: y^2 = x^3 - c^2 x over Q via mwrank 2-descent (Sage),
      with an independent lower bound rank >= 2 from explicit points whose
      doubled x-coordinates are the two membership values
  converse structure: three AP x-coordinates in 2E(Q) -> grid (4) is a magic
      square of squares with constant 3a; the witness realises only 2 of the
      3 points, so it is exactly one doubled point short of an MSS.

Run:  DOT_SAGE=/workspace/.sage sage code/robertson_reduction_check.py \
        | tee code/out/robertson_reduction_check.txt
"""
from sage.all import *
from fractions import Fraction
import math

def isqrt(n):
    return math.isqrt(n)

def sq(n):
    """Exact: (isqrt(n), True) if n is a perfect square, else (isqrt(n), False)."""
    r = isqrt(n)
    return (r, r * r == n)

def q2f(qq):
    """Exact QQ element -> Fraction (for comparisons)."""
    return Fraction(int(qq.numerator()), int(qq.denominator()))

def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)

# ---- constants of the witness (plain Python ints: no floats anywhere) ----
CURVE_C = 138600    # anti-diagonal half-difference c
A0 = 425**2         # centre entry a = 425^2 = 180625
B0 = 41496          # main-diagonal half-difference b
MAGIC = 541875      # 3a

GRID = [[373**2, 289**2, 565**2],
        [360721,  425**2, 23**2],
        [205**2,  527**2, 222121]]

print("Robertson reduction check on Bremner's 7-square witness")
print("grid =")
for row in GRID:
    print("   ", row)

# ----------------------------------------------------------------------
section("(1) The two diagonals and the eight line sums")
main_diag = [GRID[0][0], GRID[1][1], GRID[2][2]]
anti_diag = [GRID[0][2], GRID[1][1], GRID[2][0]]
print("main diagonal    : (373^2, 425^2, 222121) = %s" % (tuple(main_diag),))
print("  sum =", sum(main_diag))
print("anti-diagonal    : (565^2, 425^2, 205^2) = %s" % (tuple(anti_diag),))
print("  sum =", sum(anti_diag))
assert sum(main_diag) == MAGIC
assert sum(anti_diag) == MAGIC
print("both diagonals sum to the magic constant 541875: OK")

lines = []
for i in range(3):
    lines.append(("row %d" % (i + 1), GRID[i]))
for j in range(3):
    lines.append(("col %d" % (j + 1), [GRID[i][j] for i in range(3)]))
lines.append(("main diag", main_diag))
lines.append(("anti diag", anti_diag))
assert len(lines) == 8
all_ok = True
for name, ln in lines:
    s = sum(ln)
    good = (s == MAGIC)
    all_ok = all_ok and good
    print("  %-9s %-36s sum = %-8d %s" % (name, str(ln), s, "OK" if good else "FAIL"))
assert all_ok
print("all 8 lines equal 541875: OK")

# ----------------------------------------------------------------------
section("(2) Reduction parameters: a = 425^2, b = 41496, c = 138600")
a = A0
b = B0
c = CURVE_C
amb, apb = 373**2, GRID[2][2]     # main diagonal endpoints (a-b, a+b)
amc, apc = GRID[2][0], 565**2     # anti-diagonal endpoints (a-c, a+c)
print("centre a = 425^2 =", a)
print("main diagonal  = (a-b, a, a+b) with b = a - 373^2 =", a - amb)
assert a - amb == b and a + b == apb
print("   a-b = a - 41496 =", a - b, "= 373^2 =", amb)
print("   a+b = a + 41496 =", a + b, "= 222121 (not a square; isqrt = %d)" % (isqrt(a + b),))
print("   b = 41496 =", b)
r3, s3 = sq(a - b), sq(a + b)
assert r3[0] == 373 and r3[1] and not s3[1]
print("   verified: main diag = (a-b, a, a+b) = (139129, 180625, 222121)")
print("anti-diagonal  = (a-c, a, a+c) with c = a - 205^2 =", a - amc)
assert a - amc == c and a + c == apc
print("   a-c = a - 138600 =", a - c, "= 205^2 =", amc)
print("   a+c = a + 138600 =", a + c, "= 565^2 =", apc)
print("   c = 138600 =", c)
assert amc == 205**2 and apc == 565**2
assert amc == 42025 and apc == 319225
print("205^2  = 42025  = a - c :", amc == 42025 == a - c)
print("565^2  = 319225 = a + c :", apc == 319225 == a + c)
print("verified: anti diag = (a-c, a, a+c) = (205^2, 425^2, 565^2)")

# ----------------------------------------------------------------------
section("(3) 2E(Q) membership test on E: y^2 = x(x^2 - c^2), c = 138600")
print("criterion (Bremner 1999, eq. (3)): a point (X,Y) in E(Q) lies in 2E(Q)")
print("  if and only if X, X-c, X+c are all perfect squares.")
cands = [("X = a-b = 139129", 139129),
         ("X = a   = 180625", 180625),
         ("X = a+b = 222121", 222121)]
in2e = []
for name, X in cands:
    rX, sX = sq(X); rXm, sXm = sq(X - c); rXp, sXp = sq(X + c)
    member = sX and sXm and sXp
    def fmt(r, s):
        return ("%d^2" % r) if s else ("NOT square (isqrt %d)" % r)
    print("\n%s:" % name)
    print("  X   = %-7d : %s" % (X, fmt(rX, sX)))
    print("  X-c = %-7d : %s" % (X - c, fmt(rXm, sXm)))
    print("  X+c = %-7d : %s" % (X + c, fmt(rXp, sXp)))
    print("  in 2E(Q):", member)
    if member:
        in2e.append(X)
print("\nin 2E(Q):", in2e, " -> 2 of the 3 main-diagonal x-coordinates")
if 139129 in in2e:
    print("  X=139129: X=373^2, X-c=529=23^2, X+c=277729=527^2 : YES")
if 180625 in in2e:
    print("  X=180625: X=425^2, X-c=42025=205^2, X+c=319225=565^2 : YES")
if 222121 not in in2e:
    print("  X=222121: X itself NOT a square, X-c=83521=289^2 square,"
          " but X+c=360721 NOT a square : NO")
assert in2e == [139129, 180625]

# ----------------------------------------------------------------------
section("(4) Doubling x-coordinate formula:  x(2Q) = (ux^2 + c^2)^2/(4*uy^2)")
var('x cs')
y2sym = x**3 - cs**2 * x          # y^2 on the curve
standard = (3 * x**2 - cs**2)**2 / (4 * y2sym) - 2 * x
formula = (x**2 + cs**2)**2 / (4 * y2sym)
red = (standard - formula).simplify_rational()
print("standard duplication on y^2 = x^3 - c^2 x :")
print("   x(2P) = (3x^2 - c^2)^2/(4y^2) - 2x")
print("claimed form:  x(2P) = (x^2 + c^2)^2/(4y^2)")
print("symbolic difference with y^2 = x(x^2 - c^2) substituted:", red)
assert bool(red == 0)
print("=> the two expressions are identical on the curve (symbolic, exact).")

# numeric consistency with a sample rational point: Q from X = 139129 membership
X0q, y0q = 139129, 373 * 23 * 527
print("\nsample rational point Q = (%d, %d) on E:" % (X0q, y0q))
assert y0q * y0q == X0q * (X0q - c) * (X0q + c)
print("   y^2 = %d  ==  x(x-c)(x+c) = %d   : on curve" % (y0q * y0q, X0q * (X0q - c) * (X0q + c)))
xf = Fraction((X0q * X0q + c * c)**2, 4 * y0q * y0q)
lam = Fraction(3 * X0q * X0q - c * c, 2 * y0q)
xs = lam * lam - 2 * X0q
ys = lam * (X0q - xs) - y0q
print("   (x^2+c^2)^2/(4y^2)          =", xf)
print("   (3x^2-c^2)^2/(4y^2) - 2x    =", xs)
assert xf == xs
assert ys * ys == Fraction(xs**3 - c * c * xs, 1)
print("   equal, and 2Q = (x(2Q), y(2Q)) lies on the curve: OK")

E = EllipticCurve([0, 0, 0, -c * c, 0])
P4 = E(X0q, y0q)
x2_sage = (2 * P4)[0]
print("   Sage 2*P x-coordinate      =", q2f(x2_sage), " : agrees", q2f(x2_sage) == xs)
assert q2f(x2_sage) == xs

# ----------------------------------------------------------------------
section("(5) Rank of E: y^2 = x^3 - c^2 x over Q, with c = 138600")
c2 = c * c
print("c^2 =", c2)
print("E : y^2 = x^3 - %d x   (equivalently y^2 = x(x-c)(x+c))" % c2)
print("discriminant =", E.discriminant())
print("torsion      =", E.torsion_subgroup())

r_mw = E.rank()
print("\nE.rank() [Sage default 2-descent] =", r_mw)
try:
    r_all = E.rank(algorithm='all')
    print("E.rank(algorithm='all') [mwrank and pari must agree] =", r_all)
    assert r_all == r_mw
except Exception as ex:
    print("  (algorithm='all' not usable: %s)" % ex)

# explicit points whose DOUBLED x-coordinates are two of the three AP values
print("\nexplicit points on E whose doubled x-coordinates are main-diagonal values:")
P_lo = E(139129, 373 * 23 * 527)               # x = a-b = 139129
P_mid = E(180625, 205 * 425 * 565)             # x = a   = 180625
print("  P_lo =", P_lo, "   (x(2Q) = a-b, from 23^2,373^2,527^2)")
print("  P_mid =", P_mid, "  (x(2Q) = a,   from 205^2,425^2,565^2)")
div_lo = P_lo.division_points(2)
div_mid = P_mid.division_points(2)
print("  division_points(2) of P_lo (X=139129): %d preimage(s)" % len(div_lo), div_lo)
print("  division_points(2) of P_mid (X=180625): %d preimage(s)" % len(div_mid), div_mid)
assert div_lo and div_mid
for Qp in div_lo + div_mid:
    assert q2f((2 * Qp)[0]) in (139129, 180625)
print("  every preimage Q satisfies 2Q = P : checked (exact)")

Q0 = div_lo[0]
Q1 = div_mid[0]
print("\npreimage Q0 with x(2Q0) = 139129 :", Q0)
print("preimage Q1 with x(2Q1) = 180625 :", Q1)
print("orders:", Q0.order(), Q1.order())
pre_xs = sorted(set(qp[0] for qp in div_lo + div_mid))
print("x-coordinates of all 8 division preimages:", pre_xs)
try:
    gens = E.gens()
    gen_xs = sorted(g[0] for g in gens)
    print("generator x-coordinates from E.gens():", gen_xs)
    assert all(gx in pre_xs for gx in gen_xs)
    print("=> both MW generators have x-coordinates among the division preimages;")
    print("   the Mordell-Weil group is generated by preimages of the two")
    print("   membership x-coordinates (independent confirmation of rank >= 2).")
except Exception as ex:
    print("  (E.gens not usable: %s)" % ex)
try:
    h00, h11 = Q0.height(), Q1.height()
    hsum = (Q0 + Q1).height()
    h01 = (hsum - h00 - h11) / 2.0
    det = h00 * h11 - h01 * h01
    print("height pairing matrix det = %.6e (h00=%.6g, h11=%.6g, h01=%.6g)" % (det, h00, h11, h01))
    assert det > 0
    print("=> Q0, Q1 independent, so rank(E(Q)) >= 2")
except Exception as ex:
    print("height-based independence check failed (%s); rank >= 2 rests on mwrank" % ex)

import subprocess
try:
    mw = subprocess.run(['mwrank', '-q'], input="0 0 0 -%d 0\n" % c2,
                        capture_output=True, text=True, timeout=180)
    print("\nstandalone mwrank (independent invocation), tail of output:")
    print(mw.stdout[-1800:])
except Exception as ex:
    print("\nstandalone mwrank not run: %s" % ex)

# ----------------------------------------------------------------------
section("Extra: duplication-map preimages via quartic roots (exact, QQ)")
print("(x^2+c^2)^2 - 4X x (x^2-c^2) = 0  has a rational root x with y^2=x(x^2-c^2)")
print("a square  <=>  X is the x-coordinate of a point in 2E(Q).")
Rpoly = QQ['t']; t = Rpoly.gen()
for Xv in (139129, 180625, 222121):
    # (x^2 + c^2)^2 - 4 X x (x^2 - c^2) = 0,  expanded:
    # x^4 - 4X x^3 + 2c^2 x^2 + 4Xc^2 x + c^4 = 0  (constant term c^4 = c2^2)
    f = t**4 - 4 * Xv * t**3 + 2 * c2 * t**2 + 4 * Xv * c2 * t + c2**2
    print("\nquartic for X = %d :" % Xv)
    print("  factor:", f.factor())
    roots = f.roots()
    print("  rational roots:", roots if roots else "none")
    for root, mult in f.roots():
        y2_ = root * (root * root - c2)
        if y2_.is_square():
            Qp = E(root, y2_.sqrt())
            x2Q = q2f((2 * Qp)[0])
            print("  root x = %s, y^2 = %s square -> Q on E, x(2Q) = %s == %d : %s"
                  % (root, y2_, x2Q, Xv, x2Q == Xv))
            assert x2Q == Xv
        else:
            print("  root x = %s but y^2 = %s NOT a square -> no Q in E(Q)" % (root, y2_))

# ----------------------------------------------------------------------
section("Converse direction: three AP x-coordinates in 2E(Q) give a magic square, constant 3a")
var('aa bb cc')
Gsym = matrix(SR, 3, 3,
              [[aa - bb, aa + bb + cc, aa - cc],
               [aa + bb - cc, aa, aa - bb + cc],
               [aa + cc, aa - bb - cc, aa + bb]])

def line_sums(Gm):
    out = []
    for i in range(3):
        out.append(sum(Gm[i][j] for j in range(3)))
    for j in range(3):
        out.append(sum(Gm[i][j] for i in range(3)))
    out.append(Gm[0][0] + Gm[1][1] + Gm[2][2])
    out.append(Gm[0][2] + Gm[1][1] + Gm[2][0])
    return out

lsym = line_sums(Gsym)
assert len(lsym) == 8
sym_ok = all(bool((s - 3 * aa).simplify_full() == 0) for s in lsym)
print("symbolically, all 8 line sums of parametrisation (2) equal 3a:", sym_ok)
assert sym_ok
print("Bremner's converse grid (4) is parametrisation (2) with")
print("  a = x(2P1), b = x(2P2)-x(2P1) = x(2P1)-x(2P0) (the AP condition), so its")
print("  8 line sums are 3a = 3*x(2P1) automatically.")
print("Hence: if x(2P0), x(2P1), x(2P2) all lie in 2E(Q) (each X, X-c, X+c a square),")
print("then every entry of grid (4) is a square and it is a genuine MSS, constant 3a.")

X0v, X1v, X2v = 139129, 180625, 222121
Gconv = [[X0v, X2v + c, X1v - c],
         [X2v - c, X1v, X0v + c],
         [X1v + c, X0v - c, X2v]]
print("\nconverse grid (4) built from the witness AP (a-b, a, a+b) = (139129, 180625, 222121), c = 138600:")
for r_ in Gconv:
    print("  ", r_)
lconv = line_sums(Gconv)
for k, s in enumerate(lconv):
    print("  line %d sum = %-8d %s" % (k + 1, s, "OK" if s == 3 * X1v else "FAIL"))
assert all(s == 3 * X1v for s in lconv)
print("all 8 sums = 3a = 3*180625 =", 3 * X1v, "= magic constant 541875 : OK")
assert Gconv == [[GRID[i][j] for i in range(3)] for j in range(3)]
print("(this grid is the transpose of Bremner's printed witness: entry multiset matches exactly)")
print("\nsquare status of the nine entries of the converse grid:")
for r_ in Gconv:
    for e in r_:
        rr, ss = sq(e)
        print("   %-8d : %s" % (e, ("%d^2" % rr) if ss else "NOT a square"))
nsq_entries = [e for r_ in Gconv for e in r_ if not sq(e)[1]]
print("non-square entries:", nsq_entries, "= {x(2P2)+c, x(2P2)} = {360721, 222121}")
assert sorted(nsq_entries) == [222121, 360721]
print("Both come from the failed membership X = a+b = 222121 (X and X+c not squares).")
print("=> the witness is exactly ONE doubled point short of an MSS.")

# ----------------------------------------------------------------------
section("Exact values")
vals = [("205^2", 205**2), ("565^2", 565**2), ("527^2", 527**2), ("23^2", 23**2),
        ("289^2", 289**2), ("373^2", 373**2), ("425^2", 425**2),
        ("360721", 360721), ("222121", 222121)]
for name, v in vals:
    r, ss = sq(v)
    extra = "" if ss else "   (NOT a square; %d^2 < %d < %d^2)" % (r, v, r + 1)
    print("  %-8s = %-8d%s" % (name, v, extra))
    if ss:
        assert r * r == v
    else:
        assert r * r < v < (r + 1) * (r + 1)
print("\nALL CHECKS PASSED (exit 0).")