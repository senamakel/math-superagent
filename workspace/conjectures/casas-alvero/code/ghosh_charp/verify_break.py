"""Verify, computationally and exactly, the char-p break in the Ghosh proof.

Verifies the objects and claims of the held source
research/sources/ghosh2025_proof_html.full.md section 2, exactly over QQ and
GF(p), using the canonical oracle lib.casas_alvero for the counterexample
part.  No floating point anywhere.

Checks
------
A. HD^i_n(x_1...x_n) == e_{n-i}(x_1,...,x_n) (elementary symmetric), from the
   definition (2.1), for n = 2..10, i = 0..n-1, over QQ and over GF(p),
   p in {2,3,5,7}.  Spot-checks e_1 = x_1+...+x_n and e_2.

B. Phi^#_{d,j} of eq (2.2) really is an algebra automorphism: linearity,
   multiplicativity, inverse (x_l -> x_l + x_j for l != j, x_j -> -x_j), and
   Phi^#_{d,d+1} = identity, for d = 2..6, j = 1..d+1, over QQ and GF(p).

1. For all n in 2..10 and all j in 1..n+1, the leading coefficient
   f(n,j,n) (from F(n,j,n) = x_n*f + g) equals 1 when j != n and -n when
   j == n, over QQ and over GF(p) for p in {2,3,5,7}.  This is the exact
   divisibility Eq (4.18) of the proof depends on.

2. Over QQ: f(n,n,n) = -n != 0 for n = 2..10.  Over GF(p) with p | n:
   f(n,n,n) = -n = 0 (the unit dies).  Concretely,
   Phi^#_{n,n}(e_1) = (x_1+...+x_{n-1}) - n*x_n  and
   Phi^#_{n,j}(e_1) = e_1 - (n+1)*x_j for j != n, for several n, over QQ and
   GF(p).

3. Over GF(p), f = x^{p+1} - x^p (degree n = p+1): oracle
   lib.casas_alvero.is_counterexample reports hypothesis holds and not a pure
   power, for p = 2,3,5,7.  The downward induction would need the step d = p
   where char | p fails (f(p,p,p) = -p = 0), which is exactly why the proof's
   char-0-only step cannot rule this family out.

Exit code 0 iff every check passes.  Output captured to
code/out/ghosh_break.captured.txt (first three lines name the program, the
oracle functions, and the n,p ranges).
"""

import os
import sys

from sympy import Integer, Poly, expand, symbols, QQ, GF

from lib.ghosh2025 import (
    F_ij,
    e_symmetric,
    f_ij,
    hd_monomial_image,
    phi,
)
from lib.casas_alvero import (
    is_ca,
    is_counterexample,
    is_pure_power,
    charp_witness,
)

N_MAX = 10
PRIMES = [2, 3, 5, 7]
CHARS = [0] + PRIMES          # 0 = Q, otherwise F_p

X = symbols("x1:11")          # x1 .. x10 (index 0 unused; 1-based names)
X0 = tuple([symbols("x0")])   # never used; kept for clarity of indexing


def char_label(char):
    return "QQ" if char == 0 else f"GF({char})"


def value_in_char(k, char):
    """Integer k reduced to the coefficient field of characteristic ``char``."""
    return Integer(k) if char == 0 else Integer(k % char)


def poly_diff_zero(e1, e2, gens, char):
    """True iff e1 - e2 is zero in the coefficient field of ``char``.

    GF(p) polynomials store coefficients as symmetric representatives
    (e.g. -2 for 3 mod 5), so a bare expression comparison is wrong: the
    difference must be rebuilt over the field, which reduces every
    coefficient mod p.  char == 0 -> QQ.
    """
    diff = expand(e1 - e2)
    if char == 0:
        return Poly(diff, *gens, domain=QQ).is_zero
    return Poly(diff, *gens, modulus=char).is_zero


def records():
    """Yield (passed, text) for every check; runs the whole suite."""
    ok = True
    total = 0
    failed = 0
    lines = []

    def rec(passed, text):
        nonlocal ok, total, failed
        total += 1
        ok = ok and passed
        if not passed:
            failed += 1
        lines.append(f"[{'PASS' if passed else 'FAIL'}] {text}")

    # ------------------------------------------------------------------ A --
    lines.append("-- A. HD^i_n(x_1..x_n) == e_{n-i} over QQ and GF(p), "
                 "n=2..10, i=0..n-1")
    for n in range(2, N_MAX + 1):
        for i in range(0, n):
            for char in CHARS:
                hd = hd_monomial_image((1,) * n, i, X[:n], char)
                e = e_symmetric(n - i, X[:n], char)
                rec((hd - e).is_zero,
                    f"HD^{i}_{n}(x_1..x_{n}) == e_{n - i} over {char_label(char)}")
    # spot checks of the closed forms named in the source
    for char in CHARS:
        for n in (4, 7, 10):
            hd1 = hd_monomial_image((1,) * n, n - 1, X[:n], char)
            expect1 = sum(X[:n])
            hd2 = hd_monomial_image((1,) * n, n - 2, X[:n], char)
            expect2 = e_symmetric(2, X[:n], char)
            rec((hd1 - expect1).is_zero,
                f"HD^{n-1}_{n} x_n == e_1 = x_1+...+x_{n} over {char_label(char)}")
            rec((hd2 - expect2).is_zero,
                f"HD^{n-2}_{n} x_n == e_2 over {char_label(char)}")

    # ------------------------------------------------------------------ B --
    lines.append("-- B. Phi^#_{d,j} is an algebra automorphism "
                 "(linearity, multiplicativity, inverse, d+1 = identity)")

    for d in range(2, 7):
        for j in range(1, d + 2):
            for char in CHARS:
                # sample polynomials as expressions; phi() rebuilds them over
                # the field, and every comparison is reduced over the field
                p1_expr = expand(sum(X[:d]) ** 2)
                p2_expr = X[0] * X[1] + X[d - 1]
                a, b = Integer(2), Integer(-3)
                # linearity: phi(a p1 + b p2) == a phi(p1) + b phi(p2)
                lhs = phi(a * p1_expr + b * p2_expr, d, j, X[:d], char)
                rhs_e = (a * phi(p1_expr, d, j, X[:d], char).as_expr()
                         + b * phi(p2_expr, d, j, X[:d], char).as_expr())
                rec(poly_diff_zero(lhs.as_expr(), rhs_e, X[:d], char),
                    f"linearity Phi^#_{{{d},{j}}} over {char_label(char)}")
                # multiplicativity: phi(p1 p2) == phi(p1) phi(p2)
                lhs = phi(p1_expr * p2_expr, d, j, X[:d], char)
                rhs_e = expand(phi(p1_expr, d, j, X[:d], char).as_expr()
                               * phi(p2_expr, d, j, X[:d], char).as_expr())
                rec(poly_diff_zero(lhs.as_expr(), rhs_e, X[:d], char),
                    f"multiplicativity Phi^#_{{{d},{j}}} over {char_label(char)}")
                # inverse: Phi^# is an involution (x_l - x_j then -x_j twice
                # returns x_l / x_j), so phi(phi(p)) == p
                img = phi(p1_expr, d, j, X[:d], char)
                back = phi(img, d, j, X[:d], char)
                rec(poly_diff_zero(back.as_expr(), p1_expr, X[:d], char),
                    f"inverse Phi^#_{{{d},{j}}} over {char_label(char)}")
        # identity at j = d+1
        for char in CHARS:
            p_expr = expand(sum(X[:d]) ** 3) + X[0]
            img = phi(p_expr, d, d + 1, X[:d], char)
            rec(poly_diff_zero(img.as_expr(), p_expr, X[:d], char),
                f"Phi^#_{{{d},{d + 1}}} = identity over {char_label(char)}")

    # ------------------------------------------------------------------ 1 --
    lines.append("-- 1. f(n,j,n) == 1 (j != n), == -n (j == n), "
                 "n=2..10, j=1..n+1, over QQ and GF(p)")
    for n in range(2, N_MAX + 1):
        for j in range(1, n + 2):
            for char in CHARS:
                coeff = f_ij(n, j, n, X[:n], char)
                expected = Integer(1) if j != n else value_in_char(-n, char)
                rec(poly_diff_zero(coeff, expected, X[:n - 1], char),
                    f"f({n},{j},{n}) = {coeff} over {char_label(char)} "
                    f"(expected {expected})")
    # independent route for the same claim: Poly.coeff_monomial on F directly
    lines.append("-- 1'. independent route: x_n-coefficient of F(n,j,n) via "
                 "Poly.coeff_monomial, n=3..10 (QQ) and spot GF(p), must agree "
                 "with f_ij")
    for n in range(3, N_MAX + 1):
        for j in range(1, n + 2):
            for char in (0, PRIMES[0], PRIMES[2]):  # QQ, GF(2), GF(5)
                F = F_ij(n, j, n, X[:n], char)
                coeff_mon = F.coeff_monomial(X[n - 1])
                coeff = f_ij(n, j, n, X[:n], char)
                rec(poly_diff_zero(coeff_mon, coeff, X[:n - 1], char),
                    f"coeff_monomial agrees with f_ij for f({n},{j},{n}) "
                    f"over {char_label(char)}")

    # ------------------------------------------------------------------ 2 --
    lines.append("-- 2. char-0 unit vs char-p death: f(n,n,n) = -n, "
                 "nonzero in QQ, zero in GF(p) iff p | n; concrete e_1 images")
    for n in range(2, N_MAX + 1):
        coeff = f_ij(n, n, n, X[:n], 0)
        rec(expand(coeff - Integer(-n)) == 0 and int(coeff) != 0,
            f"over QQ: f({n},{n},{n}) = {coeff} != 0")
        for p in PRIMES:
            if n % p == 0:
                coeff_p = f_ij(n, n, n, X[:n], p)
                rec(expand(coeff_p) == 0,
                    f"over GF({p}): f({n},{n},{n}) = {coeff_p} == 0 "
                    f"because {p} | {n}  (the unit dies at step d={n})")
    # concrete images of e_1 under Phi^#_{n,j}
    for char in CHARS:
        for n in (2, 3, 5, 6, 10):
            e1 = sum(X[:n])
            img_nn = phi(e1, n, n, X[:n], char)
            expect_nn = sum(X[:n - 1]) + value_in_char(-n, char) * X[n - 1]
            rec(poly_diff_zero(img_nn.as_expr(), expect_nn, X[:n], char),
                f"Phi^#_{{{n},{n}}}(e_1) = {img_nn.as_expr()} over {char_label(char)}")
            for j in dict.fromkeys((1, 2, n - 1 if n > 2 else 1)):
                if not (1 <= j <= n):
                    continue
                img = phi(e1, n, j, X[:n], char)
                expect = e1 - value_in_char(n + 1, char) * X[j - 1]
                rec(poly_diff_zero(img.as_expr(), expect, X[:n], char),
                    f"Phi^#_{{{n},{j}}}(e_1) = {img.as_expr()} over {char_label(char)}")

    # ------------------------------------------------------------------ 3 --
    lines.append("-- 3. char-p counterexample family x^{p+1}-x^p over GF(p), "
                 "p = 2,3,5,7, decided by the canonical oracle")
    for p in PRIMES:
        f = charp_witness(p)
        ca = is_ca(f, p)
        pp = is_pure_power(f, p)
        ce = is_counterexample(f, p)
        n = p + 1
        rec(ca and not pp and ce,
            f"x^{p + 1}-x^{p} over GF({p}): is_ca={ca}, is_pure_power={pp}, "
            f"is_counterexample={ce}  (degree n={n}; the downward induction "
            f"would need step d={p} where char | p fails)")
        # the exact divisibility the proof's Eq (4.18) needs at step d = p:
        # f(p,p,p) = -p must be a unit there, and it is 0 in GF(p)
        coeff_step = f_ij(p, p, p, X[:p], p)
        rec(coeff_step == 0,
            f"step d={p}: f({p},{p},{p}) = {coeff_step} in GF({p}) "
            f"(-{p} = 0), the unit Eq (4.18) needs has died -- this is "
            f"exactly the step the degree-{n} witness escapes through")

    lines.append("")
    lines.append(f"TOTAL: {total} checks, {failed} failed.")
    return ok, lines


def main():
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..", "out")
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, "ghosh_break.captured.txt.tmp")
    final_path = os.path.join(out_dir, "ghosh_break.captured.txt")

    ok, lines = records()

    header = [
        "CHAR-P BREAK VERIFICATION, Ghosh proof of Casas-Alvero "
        "(code/ghosh_charp/verify_break.py)",
        "oracle functions: lib.casas_alvero.is_ca / is_pure_power / "
        "is_counterexample / charp_witness; lib.ghosh2025 HD/Phi/F objects",
        "range: n = 2..10, j = 1..n+1, chars QQ and GF(p), p = 2,3,5,7 "
        "(witnesses x^{p+1}-x^p); exact arithmetic only",
    ]
    body = header + [""] + lines + [""]
    body.append(f"ALL CHECKS {'PASSED' if ok else 'FAILED'}")

    with open(tmp_path, "w") as fh:
        fh.write("\n".join(body) + "\n")
    if ok:
        os.replace(tmp_path, final_path)
        print(f"capture saved to {final_path}")
    else:
        print(f"FAILED - capture left at {tmp_path} (not moved on failure)")
    for line in body:
        print(line)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
