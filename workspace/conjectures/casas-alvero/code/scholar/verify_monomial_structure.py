"""Independently verify the load-bearing `resultant-monomials` claim from
Schaub-Spivakovsky arXiv:2307.05997 (Thm 6, Thm 9), peer-reviewed
Res. Math. Sci. 11 (2024), facts first proved by R. de Frutos (PhD thesis
Prop 2.2.1).

Claim under test, with f = x^d + a_1 x^{d-1} + ... + a_{d-1} x (a_d set to 0),
H_i(f) the Hasse derivative, R_i = Res_x(f, H_i(f)) in Z[a_1,...,a_{d-1}]:
  (A) (-1)^{d-i} (binomial(d,i)-1)^{d-i} a_{d-i}^d appears in R_i, and
      a_{d-i}^d is the ONLY pure power (a single a-variable to the d-th
      power) appearing in any R_i;
  (B) for i>=2, (-1)^{(d-1)(d-i)} binomial(d,i)^{d-1} a_{d-1}^{d-i} a_{d-i}
      is the unique monomial of degree d-i+1 in R_i, all others higher.

We compute R_i symbolically over Z[a_1,...,a_{d-1}] (Hasse derivatives, exact
sympy resultant), expand, and check (A) and (B) term by term for d=3,4.
d=5 is recorded-infeasible (one symbolic resultant exceeds the cap).

Pure power = a monomial c * prod_j a_j^{e_j} with exactly one e_j = d, the
rest 0. We check both that the named pure power is present and that no OTHER
monomial is a pure power of a single a-variable-^d.
"""

import os
import sympy as sp


def hasse_derivative(coeffs, x, i):
    """H_i(f) = sum_k binomial(k,i) c_k x^{k-i}, f = sum_k c_k x^k."""
    terms = 0
    for k, ck in enumerate(coeffs):
        if k >= i:
            terms += sp.binomial(k, i) * ck * x ** (k - i)
    return sp.expand(terms)


def poly_monomials(P, gens):
    """Return list of (exponent_tuple_over_gens, coeff) for Poly P."""
    poly = sp.Poly(P.as_expr(), gens)
    out = []
    gens_list = list(poly.gens)
    for (expkey, coeff) in poly.terms():
        exptup = tuple(int(expkey[g]) for g in gens_list)
        out.append((exptup, coeff))
    return out


def verify_degree(d):
    a = {j: sp.symbols("a%d" % j) for j in range(1, d)}
    symbols = [a[j] for j in range(1, d)]  # order a_1,...,a_{d-1}
    x = sp.symbols("x")
    f = x**d + sum(a[j] * x ** (d - j) for j in range(1, d))
    # coeffs c_k of x^k
    coeffs = [f.coeff(x, k) for k in range(d + 1)]

    lines = ["Degree d = %d" % d]
    for i in range(1, d):
        Hi = hasse_derivative(coeffs, x, i)
        R = sp.resultant(f, Hi, x)
        P = sp.Poly(sp.expand(R), symbols)
        monoms = poly_monomials(P, symbols)
        exp_to_c = {tuple(e): c for (e, c) in monoms}
        total = len(monoms)
        lines.append("  i=%d: R_i has %d monomials" % (i, total))

        # (A) named pure power at position a_{d-i}
        posA = (d - i) - 1  # index in symbols list (a_{d-i})
        targetA = [0] * (d - 1)
        targetA[posA] = d
        tA = tuple(targetA)
        expectedA = (-1) ** (d - i) * (sp.binomial(d, i) - 1) ** (d - i)
        presentA = tA in exp_to_c
        lines.append("    (A) a_{%d}^%d present=%s coeff=%s (expected %s)"
                     % (d - i, d, presentA,
                        exp_to_c.get(tA), expectedA))
        # unique pure power: any single-var-^d monomial other than tA?
        others_pp = [ (e, c) for (e, c) in monoms
                      if e != tA and sum(1 for z in e if z != 0) == 1
                      and max(e) == d ]
        lines.append("    (A) other single-var-^d pure powers in R_i: %s"
                     % others_pp)

        if i >= 2:
            # (B) a_{d-1}^{d-i} * a_{d-i}: a_{d-1}=index d-2, a_{d-i}=index (d-i)-1
            targetB = [0] * (d - 1)
            targetB[d - 2] = d - i
            targetB[(d - i) - 1] = 1
            tB = tuple(targetB)
            expectedB = (-1) ** ((d - 1) * (d - i)) * sp.binomial(d, i) ** (d - 1)
            presentB = tB in exp_to_c
            lines.append("    (B) a_{%d}^{%d} a_{%d} present=%s coeff=%s (expected %s)"
                         % (d - 1, d - i, d - i, presentB,
                            exp_to_c.get(tB), expectedB))
            degs = [sum(e) for (e, c) in monoms]
            mindeg = min(degs)
            min_ms = [(e, c) for (e, c) in monoms if sum(e) == mindeg]
            lines.append("    (B) monomials of minimal degree %d: %s"
                         % (mindeg, min_ms))
            lines.append("    (B) minimal degree == d-i+1 = %d ? %s"
                         % (d - i + 1, mindeg == d - i + 1))
    return lines


def main():
    lines = ["VERIFY resultant-monomials structure "
             "(Schaub-Spivakovsky arXiv:2307.05997 Thm 6/9; de Frutos "
             "PhD Prop 2.2.1)",
             "method: exact symbolic resultants R_i=Res_x(f,H_i(f)) over "
             "Z[a_1..a_{d-1}], Hasse derivatives, sympy; d=3,4 "
             "(d=5 infeasible boundary)",
             "exact arithmetic, no floats; sign convention = sympy resultant"]
    for d in [3, 4]:
        lines.append("")
        lines += verify_degree(d)
    lines.append("")
    lines.append("CAPTURE COMPLETE -- see asserted structure above")
    return "\n".join(lines)


if __name__ == "__main__":
    text = main()
    print(text)
    out_dir = "/workspace/code/out"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "verify_monomial_structure.captured.txt")
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        fh.write(text + "\n")
    os.replace(tmp, path)
    raise SystemExit(0)
