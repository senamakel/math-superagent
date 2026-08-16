#!/usr/bin/env python3
"""Recheck of the 'f(X^p) without constant term' clause of claim
charp-witness-xpp1-xp under the HASSE derivative formulation.

Claim under test (research/summaries/grafvonbothmer2007_infinitely_many.md,
id charp-witness-xpp1-xp): "In characteristic p, f(x) = x^{p+1} - x^p (and
relatives) is a CA-polynomial ... f(X^p) without constant term also works
since all derivatives vanish."

The first part (x^{p+1} - x^p is CA, not a pure power) is checked already.
The second clause is ORDINARY-derivative vacuity: over F_p, d/dx f(X^p) =
p X^{p-1} f'(X^p) = 0, so every ordinary derivative vanishes and
gcd(f, f^(i)) = f is trivially non-constant. Under the HASSE formulation
H_i(f) = sum_j C(j,i) c_j X^{j-i} does NOT vanish in general. This program
decides, per prime, whether the clause survives: whether g = f(X^p) with
f(0) = 0 is Hasse-CA, and whether "all Hasse derivatives vanish" is true
at all (in particular H_2).

Method
------
All decisions are exact over GF(p) through the canonical oracle in
lib.casas_alvero (is_ca ordinary, is_ca_hasse Hasse, is_pure_power) and
lib.casasalvero (hasse_derivative). No floating point anywhere.

Fact the analysis rests on (worked by hand, verified here by the program):
for g = X^{mp}, H_i(g) = C(mp, i) X^{mp-i}, and Lucas' theorem gives
C(mp, i) = 0 mod p unless p | i, with C(mp, pi') = C(m, i') mod p. So all
Hasse derivatives vanish iff C(m, i') = 0 mod p for every 1 <= i' <= m-1,
which fails in general (e.g. p=2, m=3: H_2(X^6) = C(6,2) X^4 = X^4 != 0).
For g = c_1 X^p + c_2 X^{2p}, H_{pi'}(g) = H_{i'}(c_1 Y + c_2 Y^2)(X^p), so
Hasse-CA holds iff c_1 = 0.

Complexity
----------
n = deg g <= 21 here; per polynomial O(n) Hasse derivatives, each an
O(n)-term exact sum, each gcd an exact Poly gcd over GF(p): polynomial in n,
trivial at these sizes. No exponential time or space anywhere.
"""

import os

from sympy import symbols, Poly, GF, QQ

from lib.casas_alvero import is_ca, is_ca_hasse, is_pure_power
from lib.casasalvero import hasse_derivative

x = symbols("x")


# ---------------------------------------------------------------------------
# Guards (the run dies here if any fails)
# ---------------------------------------------------------------------------
def run_guards():
    """Entry guard set from the task: (x-1)^3 is CA over QQ, x^3-x is not,
    and the char-p witness x^{p+1}-x^p is Hasse-CA for p = 2, 3, 5."""
    lines = []
    assert is_ca((x - 1) ** 3, 0) is True, "guard: (x-1)^3 over QQ must be CA"
    lines.append("GUARD PASS: is_ca((x-1)^3, 0) == True")
    assert is_ca(x ** 3 - x, 0) is False, "guard: x^3-x over QQ must NOT be CA"
    lines.append("GUARD PASS: is_ca(x^3-x, 0) == False")
    for p in (2, 3, 5):
        assert is_ca_hasse(x ** (p + 1) - x ** p, p) is True, \
            f"guard: x^{p+1}-x^p must be Hasse-CA over F_{p}"
        lines.append(f"GUARD PASS: is_ca_hasse(x^{{{p+1}}}-x^{p}, {p}) == True")
    return lines


# ---------------------------------------------------------------------------
# Hasse-derivative helpers (exact)
# ---------------------------------------------------------------------------
def H_poly(f, i):
    """H_i(f) as a Poly over the same domain as f; exact, reduced mod p."""
    return Poly(hasse_derivative(f.as_expr(), x, i), x, domain=f.get_domain())


def nonzero_hasse_indices(f):
    """All i in 1..deg(f)-1 with H_i(f) not identically zero (exact)."""
    return [i for i in range(1, f.degree()) if not H_poly(f, i).is_zero]


def first_failing_index(f):
    """First i in 1..deg(f)-1 with gcd(f, H_i(f)) constant; None if none.

    Convention gcd(f, 0) = f (non-constant, hypothesis holds there), matching
    the oracle's docstring and is_ca_hasse behaviour."""
    n = f.degree()
    for i in range(1, n):
        H = H_poly(f, i)
        if H.is_zero:
            continue  # gcd(f, 0) = f, non-constant
        if f.gcd(H).degree() < 1:
            return i
    return None


def describe_H(f, i):
    """Explicit H_i(f) as a string, or 'out of range' / '≡ 0'."""
    if i >= f.degree():
        return "out of range (deg < i+1)"
    H = H_poly(f, i)
    return "≡ 0" if H.is_zero else str(H)


def main():
    lines = []

    def emit(text):
        lines.append(text)
        print(text)

    emit("RECHECK of claim charp-witness-xpp1-xp clause 'f(X^p) without "
         "constant term also works since all derivatives vanish'")
    emit("oracle functions: is_ca / is_ca_hasse / is_pure_power from "
         "lib.casas_alvero; hasse_derivative from lib.casasalvero")
    emit("range: primes p in {2,3,5,7}; (A) g = x^{p+1}-x^p; "
         "(B) g = x^{mp} for m = 1..3 and g = x^p + x^{2p} over GF(p)")
    emit("exact sympy arithmetic over GF(p); no floats")
    emit("")

    emit("-- GUARDS --")
    for line in run_guards():
        emit(line)
    emit("")

    # --- (A) genuine Hasse witness -----------------------------------------
    emit("== (A) g = x^{p+1} - x^p over GF(p): the genuine Hasse witness ==")
    for p in (2, 3, 5, 7):
        f = Poly(x ** (p + 1) - x ** p, x, domain=GF(p))
        ca = is_ca(f, p)
        hasse = is_ca_hasse(f, p)
        pp = is_pure_power(f, p)
        nz = nonzero_hasse_indices(f)
        emit(f"p={p}: deg={f.degree()} is_ca={ca} is_ca_hasse={hasse} "
             f"is_pure_power={pp} "
             f"(hypothesis holds && not pure power: {ca and hasse and not pp})")
        emit(f"       nonzero H_i indices: {nz}")
    emit("")

    # --- (B) f(X^p) without constant term ----------------------------------
    emit("== (B) g = f(X^p) with f(0) = 0: is the 'all derivatives vanish' "
         "clause ordinary-only? ==")
    emit("")
    emit("-- (B1) g = x^{mp}, m = 1..3 (f(Y) = Y^m) --")
    for p in (2, 3, 5, 7):
        for m in (1, 2, 3):
            g = Poly(x ** (m * p), x, domain=GF(p))
            ca = is_ca(g, p)
            hasse = is_ca_hasse(g, p)
            pp = is_pure_power(g, p)
            nz = nonzero_hasse_indices(g)
            H1 = describe_H(g, 1)
            H2 = describe_H(g, 2)
            Hp = describe_H(g, p)
            emit(f"p={p} m={m}: g=x^{m*p} deg={g.degree()} "
                 f"is_ca={ca} is_ca_hasse={hasse} is_pure_power={pp}")
            emit(f"        H_1 = {H1}; H_2 = {H2}; H_{p} = {Hp}")
            emit(f"        nonzero H_i indices in 1..deg-1: "
                 f"{nz if nz else 'NONE (all Hasse derivatives vanish)'}")
    emit("")
    emit("-- (B2) g = c_1 x^p + c_2 x^{2p}, (c_1, c_2) = (1, 1) "
         "(f(Y) = Y + Y^2) --")
    for p in (2, 3, 5, 7):
        g = Poly(x ** p + x ** (2 * p), x, domain=GF(p))
        ca = is_ca(g, p)
        hasse = is_ca_hasse(g, p)
        pp = is_pure_power(g, p)
        nz = nonzero_hasse_indices(g)
        fail = first_failing_index(g)
        H1 = describe_H(g, 1)
        Hp = describe_H(g, p)
        emit(f"p={p}: g=x^{p}+x^{2*p} deg={g.degree()} "
             f"is_ca={ca} is_ca_hasse={hasse} is_pure_power={pp}")
        emit(f"        H_1 = {H1}; H_{p} = {Hp}")
        emit(f"        nonzero H_i indices in 1..deg-1: "
             f"{nz if nz else 'NONE'}")
        emit(f"        first i with gcd(g, H_i) constant: "
             f"{fail if fail is not None else 'none (Hasse-CA)'}")
    emit("")
    emit("-- (B2b) boundary: g = c_1 x^p + c_2 x^{2p} with c_1 = 0 "
         "(reduces to x^{2p} = (B1) m=2) vs c_1 != 0 --")
    for p in (2, 3, 5, 7):
        g0 = Poly(x ** (2 * p), x, domain=GF(p))
        g1 = Poly(2 * x ** p + x ** (2 * p), x, domain=GF(p))
        emit(f"p={p}: (c1=0,c2=1): is_ca_hasse={is_ca_hasse(g0, p)}; "
             f"(c1=2,c2=1): is_ca_hasse={is_ca_hasse(g1, p)} "
             f"(expect True iff c1 == 0 mod p)")
    emit("")
    emit("VERDICT: for g = x^{mp}, Hasse-CA hypothesis holds (as monomial gcd) "
         "for all tested (p, m), but 'all Hasse derivatives vanish' is FALSE "
         "whenever some i = p*i' has C(m, i') != 0 mod p (see nonzero lists; "
         "in particular p=2, m=3 gives H_2 != 0). For g = x^p + x^{2p} with "
         "c_1 != 0 the Hasse hypothesis FAILS (first failing index = p); the "
         "clause is ordinary-only there.")

    # capture
    out_dir = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "out")
    os.makedirs(out_dir, exist_ok=True)
    capture_path = os.path.join(out_dir, "ordinary-vs-hasse-charp-witness.captured.txt")
    with open(capture_path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"\ncapture saved to {capture_path}")


if __name__ == "__main__":
    main()
