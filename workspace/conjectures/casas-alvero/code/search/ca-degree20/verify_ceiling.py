"""Independent exact re-check of the degree-20 search's two structural claims.

The search (`SEARCH.md`, scorer `score.py`) reports that the top score over its
construction space is 18, never 19, and that the binding constraint is the
*linear* highest derivative f^(19). This script independently re-derives the
per-derivative gcd data for the two families the task names, using exact sympy
`Poly.gcd` over QQ (no floats anywhere).

Two claims to verify:

(1) f(x) = x^20 - x.  Per-j deg(gcd(f, f^(j))) for j = 1..19, and the identity
    of the failing derivative(s). The smoke test says f = x^20 - x shares root
    0 with f''..f^(19) but NOT with f'; the task asks us to check whether
    j=19 (f^(19) = 20!·x, root 0, and f(0) = 0) actually fails. It should NOT
    fail: it shares root 0 exactly. So the unique failing derivative must be
    j = 1 (f' = 20x^19 - 1), and the score must be 18.

(2) f(x) = x^19·(x - c) for c in {1, 2, 3} (mult-19 root at 0, one genuine
    second root at c). The question: does aligning f^(19)'s single linear root
    with a genuine second root of f push the score to 19, or stay at 18?
    f^(19) = 19!·(20x - c) has root c/20; c/20 coincides with a root of f
    (0 or c) only when c = 0 (pure power, rejected) — so it must stay at 18
    with j = 19 the binding failure. Also verified: the general shifted family
    (x - a)^19·(x - b), where aligning f^(19)'s root with a or b forces a = b
    (the pure-power family the scorer rejects).

Every number below is a deg(gcd(...)) over QQ[x], computed by sympy Poly.gcd.
"""

import sympy
from sympy import Poly, QQ, symbols, factorial


def per_j_degrees(f, jmax):
    """Return list of (j, deg(gcd(f, f^(j)))) for j = 1..jmax, exact over QQ.

    f is a sympy Poly over QQ. f^(j) is the ordinary j-th derivative,
    accumulated by repeated .diff(). No floats anywhere.
    """
    out = []
    d = f
    for j in range(1, jmax + 1):
        d = d.diff()
        g = sympy.gcd(f.as_expr(), d.as_expr())
        out.append((j, Poly(g, x, domain=QQ).degree()))
    return out


def report(title, f, jmax=19):
    rows = per_j_degrees(f, jmax)
    failing = [j for (j, deg) in rows if deg == 0]
    print("=" * 72)
    print(title)
    print("  f = %s" % f.as_expr())
    for (j, deg) in rows:
        marker = "PASS" if deg > 0 else "FAIL"
        print("  j=%2d  deg(gcd(f, f^(%2d))) = %d   [%s]" % (j, j, deg, marker))
    print("  -> score k = %d (out of %d)" % (len(rows) - len(failing), jmax))
    print("  -> failing j = %s" % (failing if failing else "none"))
    return rows, failing


x = symbols("x")

results = {}

# --------------------------------------------------------------------------
# Part (1): f = x^20 - x.  The critical check on the searcher's central claim.
# --------------------------------------------------------------------------
f1 = Poly(x**20 - x, x, domain=QQ)
rows1, fail1 = report("PART (1):  f = x^20 - x", f1)
results["x20_minus_x"] = (rows1, fail1)
assert len(fail1) == 1 and fail1[0] == 1, (
    "x^20 - x should fail ONLY at j=1 (f' = 20x^19 - 1); got failing %s" % fail1
)
assert len(rows1) - len(fail1) == 18, "x^20 - x should score exactly 18"

# --------------------------------------------------------------------------
# Part (2): f = x^19 (x - c) for c in {1,2,3}.  Alignment question.
# --------------------------------------------------------------------------
for c in (1, 2, 3):
    fc = Poly(x**19 * (x - c), x, domain=QQ)
    rows, fail = report("PART (2):  f = x^19 (x - %d)" % c, fc)
    results["x19_xminus_%d" % c] = (rows, fail)
    assert fail == [19], (c, fail)
    assert len(rows) - len(fail) == 18, c

# --------------------------------------------------------------------------
# PART (2b): the general shifted family (x-a)^19 (x-b), incl. the search's
# "root-alignment" attempts (c0068..c0070).  Answer the push-to-19 question
# for a nonzero base root, where alignment with a or b is not obviously empty.
# --------------------------------------------------------------------------
print("=" * 72)
print("PART (2b): general family f = (x-a)^19 (x-b):"
      " can aligning f^(19)'s root with a root of f give 19?")
# Closed form: f^(19) = 19! * (20x - (19a + b)), a linear poly with the single
# root r19 = (19a + b)/20.  Aligning r19 with a root of f:
#   with a: (19a+b)/20 = a  <=>  b = a   (pure power, rejected)
#   with b: (19a+b)/20 = b  <=>  a = b   (pure power, rejected)
# So alignment forces a = b, the trivial family.  Verify numerically over QQ:
for (a, b) in [(2, 18), (2, 1), (4, 16), (3, 17), (0, 5)]:
    fa = Poly((x - a) ** 19 * (x - b), x, domain=QQ)
    f19 = fa
    for _ in range(19):
        f19 = f19.diff()
    r19 = -sympy.Rational(f19.coeff_monomial(x ** 0),
                          f19.coeff_monomial(x))  # -const/coeff of x
    in_root = r19 in (a, b)
    print("  a=%2d b=%2d | r19=(19a+b)/20 = %3s | in {a,b}? %s" % (
        a, b, sympy.nsimplify(r19) if hasattr(r19, "is_Rational") else r19,
        in_root))
    # score for this family: 1..18 always pass (mult-19 root), j=19 iff in_root
    rows, fail = report("   (x-%d)^19 (x-%d)" % (a, b), fa)
    assert fail == [19] or (fail == [] and a == b)

# --------------------------------------------------------------------------
print("=" * 72)
print("VERDICT")
print("  x^20 - x          : score 18, failing derivative = %s" % fail1)
print("  x^19 (x-1)        : score 18, failing = j=19 (f^(19) linear, root 1/20 "
      "not a root of f)")
print("  x^19 (x-2)        : score 18, failing = j=19 (root 1/10)")
print("  x^19 (x-3)        : score 18, failing = j=19 (root 3/20)")
print("  Verdict: 18 is the real ceiling for these families; for x^20 - x the")
print("  UNIQUE failing derivative is j = 1 (f' = 20x^19 - 1) — NOT j = 19.")
print("  f^(19) = 20!·x shares root 0 with f, so j = 19 PASSES for x^20-x.")
print("  For the mult-19-root family, j = 19 (the LINEAR f^(19)) is the binding")
print("  failure and cannot be aligned to a genuine second root in Q: that would")
print("  force a = b (pure power, rejected).  ALL EXACT CHECKS PASSED.")
