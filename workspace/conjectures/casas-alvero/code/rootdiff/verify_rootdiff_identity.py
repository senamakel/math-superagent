"""First step of the adopted root-difference-coloring approach.

Verifies, symbolically and exactly, the Abel-Gontcharoff / root-difference
identity the whole approach rests on, over QQ and over F_p:

    f(x) = prod_{j=1..n} (x - beta_j)   (monic)

    (Identity 1, Hasse = elementary symmetric)
        H_i(f)(x) = e_{n-i}(x - beta_1, ..., x - beta_n)
    where H_i(f) = [t^i] f(x+t) is the i-th Hasse derivative (no i! factor),
    and e_k is the elementary symmetric polynomial of degree k.  Because
    f(x+t) = prod_j ((x - beta_j) + t) = sum_i e_{n-i}(x-beta_1,..) t^i.

    (Identity 2, resultant = product over roots)
        R_i := Res_x(f, H_i(f)) = prod_{j=1..n} H_i(f)(beta_j)
    with leading constant 1 for monic f (the resultant-norm identity).

Checks run:
    A. Identity 1 over QQ, n = 4, 5, 6, symbolic roots (exact polynomial
       equality of the t^i coefficient of f(x+t) and e_{n-i}(x-beta_*)).
    B. Identity 2 over QQ, n = 4, 5, 6, symbolic resultant vs. the product
       over roots (exact equality as symmetric polynomials), and the
       leading-constant value c_n is reported (expected 1).
    C. Both identities over F_p for n = p+1, p = 2, 3, 5: the symbolic
       identity reduced mod p, and the concrete witness x^{p+1}-x^p.
    D. Char-p test: run the witness through the oracle (lib.casas_alvero,
       Hasse formulation) and record exactly where the char-0 collapse
       argument stops holding -- which H_i degenerate, and that a consistent
       coloring with two distinct roots survives.

Guard discipline: this script does not decide the CA hypothesis inline; every
hypothesis decision in section D goes through lib.casas_alvero.is_ca_hasse /
is_pure_power.
"""
import sys
from math import comb

import sympy as sp
from sympy import Poly, symbols, prod, expand, resultant, GF, QQ

from lib.casas_alvero import is_ca_hasse, is_pure_power, charp_witness

x, t, y = symbols("x t y")

PASS = []
FAIL = []


def rec(label, ok, detail=""):
    (PASS if ok else FAIL).append(f"[{'PASS' if ok else 'FAIL'}] {label}"
                                  + (f"  ({detail})" if detail else ""))


def hasse_coeff(fexpr, x, t, i):
    """The i-th Hasse derivative H_i(f)(x) = coefficient of t^i in f(x+t)."""
    ft = expand(fexpr.subs(x, x + t))
    return Poly(ft, t).nth(i)


def esym_from_diffs(betas, x, y, k):
    """e_k(x - beta_1, ..., x - beta_n) as a polynomial in x."""
    e = expand(prod((x - b) + y for b in betas))
    return Poly(e, y).nth(k)


def elemsym_of_x_minus_betas(betas, k):
    """e_k(x - beta_1, ..., x - beta_n), expanded in x."""
    return expand(esym_from_diffs(betas, x, y, k))


def integer_coeffs_mod_p_zero(expr, p):
    """True iff every integer coefficient of expr (a poly in x with integer
    coefficients in the betas) reduces to 0 mod p."""
    pexpr = expand(expr)
    for m in Poly(pexpr, x).all_coeffs():
        if sp.simplify(sp.expand(m) % p) != 0:
            return False
    return True


# ---------------------------------------------------------------------------
# A. Identity 1 over QQ, n = 4, 5, 6 (symbolic)
# ---------------------------------------------------------------------------
print("-- A. Identity 1 over QQ: H_i(f) = e_{n-i}(x-beta_*) for n=4,5,6")
identity1_ok = True
for n in (4, 5, 6):
    betas = symbols("b1:%d" % (n + 1))
    fexpr = prod(x - b for b in betas)
    all_ok = True
    for i in range(n + 1):
        hi = hasse_coeff(fexpr, x, t, i)
        esym = elemsym_of_x_minus_betas(betas, n - i)
        ok = sp.simplify(expand(hi - esym)) == 0
        all_ok = all_ok and ok
        if not ok:
            print(f"   n={n} i={i}: MISMATCH")
    rec(f"n={n} all i=0..n: H_i(f) == e_{{n-i}}", all_ok)
    identity1_ok = identity1_ok and all_ok
rec("Identity 1 holds over QQ for n=4,5,6", identity1_ok)

# ---------------------------------------------------------------------------
# B. Identity 2 over QQ: R_i = prod_j H_i(beta_j), c_n reported
# ---------------------------------------------------------------------------
print("-- B. Identity 2 over QQ: Res_x(f,H_i) = prod_j H_i(beta_j), n=4,5,6")
identity2_ok = True
for n in (4, 5, 6):
    betas = symbols("b1:%d" % (n + 1))
    fexpr = prod(x - b for b in betas)
    all_ok = True
    for i in range(1, n):
        hi = hasse_coeff(fexpr, x, t, i)
        res = resultant(fexpr, hi, x)
        prod_side = prod(hi.subs(x, b) for b in betas)
        # both sides are symmetric polynomials in beta_1..beta_n
        diff = sp.simplify(expand(res - prod_side))
        ok = diff == 0
        all_ok = all_ok and ok
        if not ok:
            print(f"   n={n} i={i}: MISMATCH (diff has {len(diff.args)} terms "
                  f"if nonzero)")
    rec(f"n={n} all i=1..n-1: Res_x(f,H_i) == prod_j H_i(beta_j)", all_ok)
    identity2_ok = identity2_ok and all_ok
rec("Identity 2 holds over QQ for n=4,5,6; leading constant c_n = 1 (monic f)",
    identity2_ok,
    "Res_x(monic f, g) = prod_{f(b)=0} g(b), no extra constant")

# ---------------------------------------------------------------------------
# C. Identities over F_p for n = p+1, p = 2, 3, 5
# ---------------------------------------------------------------------------
print("-- C. Identities over F_p, n = p+1, p = 2, 3, 5")
for p in (2, 3, 5):
    n = p + 1
    betas = symbols("b1:%d" % (n + 1))
    fexpr = prod(x - b for b in betas)

    # C1: symbolic identity reduced mod p (identity 1 is integer-coefficient,
    # so reduction mod p is the F_p statement).
    c1_ok = True
    for i in range(n + 1):
        hi = hasse_coeff(fexpr, x, t, i)
        esym = elemsym_of_x_minus_betas(betas, n - i)
        if not integer_coeffs_mod_p_zero(hi - esym, p):
            c1_ok = False
            print(f"   p={p} i={i}: identity 1 fails mod p")
    rec(f"p={p} (n={n}): identity 1 holds mod p", c1_ok)

    # C2: symbolic identity 2 reduced mod p.
    c2_ok = True
    for i in range(1, n):
        hi = hasse_coeff(fexpr, x, t, i)
        res = resultant(fexpr, hi, x)
        prod_side = prod(hi.subs(x, b) for b in betas)
        if not integer_coeffs_mod_p_zero(res - prod_side, p):
            c2_ok = False
            print(f"   p={p} i={i}: identity 2 fails mod p")
    rec(f"p={p} (n={n}): identity 2 holds mod p", c2_ok)

    # C3: concrete witness x^{p+1}-x^p over F_p.  Roots are 0 (mult p) and
    # 1 (mult 1).  Check H_i(f)(x) == e_{n-i}(x,...,x,x-1) (p copies of x,
    # one copy of x-1) over GF(p) for every i.
    fp = charp_witness(p)
    # Hasse derivatives of the concrete witness over GF(p)
    coeffs = [fp.coeff_monomial(x ** j) for j in range(n + 1)]
    c3_ok = True
    for i in range(n + 1):
        Hi = Poly(sum(comb(j, i) * coeffs[j] * x ** (j - i)
                      for j in range(i, n + 1)), x, domain=GF(p))
        args = [x] * p + [x - 1]
        esym_side = Poly(expand(elemsym_of_x_minus_betas(args, n - i)),
                         x, domain=GF(p))
        if Hi != esym_side:
            c3_ok = False
            print(f"   p={p} i={i}: witness H_i != e_{{n-i}}(x,...,x,x-1)")
    rec(f"p={p} (n={n}): witness H_i(f) == e_{{n-i}}(x,...,x,x-1) over F_p",
        c3_ok)

    # C4: resultant factorization on the concrete witness: Res_x(f, H_i) =
    # H_i(0)^p * H_i(1) over F_p.
    c4_ok = True
    for i in range(1, n):
        Hi = Poly(sum(comb(j, i) * coeffs[j] * x ** (j - i)
                      for j in range(i, n + 1)), x, domain=GF(p))
        res = Poly(resultant(fp.as_expr(), Hi.as_expr(), x), x, domain=GF(p))
        rhs = Hi.eval(0) ** p * Hi.eval(1)
        if res.as_expr() != rhs:
            c4_ok = False
            print(f"   p={p} i={i}: witness resultant != H_i(0)^p * H_i(1)")
    rec(f"p={p} (n={n}): Res_x(f,H_i) == H_i(0)^p * H_i(1) over F_p", c4_ok)

# ---------------------------------------------------------------------------
# D. Char-p test: where does the char-0 collapse argument stop holding?
# ---------------------------------------------------------------------------
print("-- D. Char-p test on the witness x^{p+1}-x^p: locate the break")
for p in (2, 3, 5):
    n = p + 1
    fp = charp_witness(p)
    ca = is_ca_hasse(fp, p)
    pp = is_pure_power(fp, p)
    rec(f"p={p} witness is Hasse-CA and NOT pure power (oracle)",
        ca and not pp,
        f"is_ca_hasse={ca}, is_pure_power={pp}")

    coeffs = [fp.coeff_monomial(x ** j) for j in range(n + 1)]
    degenerate = []
    for i in range(1, n):
        Hi = Poly(sum(comb(j, i) * coeffs[j] * x ** (j - i)
                      for j in range(i, n + 1)), x, domain=GF(p))
        if Hi == Poly(0, x, domain=GF(p)):
            degenerate.append(i)
    # Which derivative i is witnessed by which root
    witnesses = {}
    for i in range(1, n):
        Hi = Poly(sum(comb(j, i) * coeffs[j] * x ** (j - i)
                      for j in range(i, n + 1)), x, domain=GF(p))
        roots = [b for b in (0, 1) if Hi.eval(b) == 0]
        witnesses[i] = roots
    print(f"   p={p}: H_i == 0 for i in {degenerate}")
    print(f"   p={p}: derivative i witnessed by roots: {witnesses}")
    # A consistent two-root coloring exists exactly because the conditions do
    # not force a single root to satisfy all of them; the char-0 convex-hull /
    # Gauss-Lucas ordering that would force collapse has no F_p analogue.
    rec(f"p={p}: coloring with distinct roots 0,1 survives (break located)",
        (0 in witnesses.get(1, [])) and (1 in witnesses.get(p, [])))

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
lines = ["ROOT-DIFFERENCE IDENTITY VERIFICATION (code/rootdiff/verify_rootdiff_identity.py)",
         "oracle: lib.casas_alvero.is_ca_hasse / is_pure_power (section D only)",
         "range: n=4,5,6 over QQ (identities 1,2); n=p+1 over F_p for p=2,3,5; "
         "witness x^{p+1}-x^p"]
body = lines + [""] + PASS + FAIL + [""]
body.append("ALL CHECKS %s (%d passed, %d failed)"
            % ("PASSED" if not FAIL else "FAILED", len(PASS), len(FAIL)))
text = "\n".join(body)
print("\n".join(PASS))
for line in FAIL:
    print(line)
print()
print(text)
sys.exit(0 if not FAIL else 1)
