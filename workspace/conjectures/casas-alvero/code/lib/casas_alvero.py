"""Canonical exact oracle for the Casas-Alvero (CA) conjecture.

This is the single decision procedure for the derivative-sharing hypothesis
used across the whole run. No other implementation decides it inline.

The conjecture (over a field K, f monic, deg f = n >= 1):

    If gcd(f, f^(i)) != 1 for every i = 1 .. n-1   (f shares a root with each
    of its first n-1 derivatives)  then  f = (x - a)^n  for some a in K-bar.

This module decides the *hypothesis* exactly and the *pure-power* conclusion
exactly, over a base field that remembers its characteristic.

Exactness rules
---------------
- The base field is given explicitly by ``char``:
    char == 0  ->  domain=QQ   (exact rational arithmetic)
    char == p  ->  domain=GF(p) (exact arithmetic over F_p)
- Every decision goes through sympy's exact Poly gcd / factor / diff over the
  correct domain. No floating point anywhere: approximate root-finding may
  only *search*, never *decide*.
- Characteristic matters in a specific way: for char p, a derivative can be
  **identically zero** (e.g. (x^n)' = n x^{n-1} = 0 mod p when p | n). Then
  gcd(f, 0) = f, which is non-constant, so the hypothesis still holds — this
  is exactly the degeneration that makes CA *false* in char p. We handle it by
  taking the derivative in the base field and using sympy's gcd, which knows
  gcd(f, 0) = f.

Functions
---------
- is_ca(poly, char)               True iff the hypothesis holds (exact).
- is_pure_power(poly, char)       True iff f = c*(x-a)^deg over K-bar (exact).
- is_counterexample(poly, char)   is_ca and not is_pure_power.
- is_ca_hasse(poly, char)         CA hypothesis with Hasse derivatives H_i(f)
                                  (the formulation of the published char-p
                                  bad-prime lists); agrees with is_ca in
                                  characteristic 0 and for p >= n.
- charp_witness(p)                x^{p+1} - x^p over GF(p): the char-p
                                  counterexample family (hypothesis holds,
                                  not a pure power).
- run_guards(verbose=True)        Runs the full guard set; returns (ok, lines).
"""

import random
import os
from math import comb

from sympy import Poly, symbols, QQ, GF


def _coerce(poly, char):
    """Return ``poly`` as a sympy Poly over the domain specified by ``char``.

    Accepts either a Poly (rebuilt over the requested domain) or a sympy
    expression / number. char==0 -> QQ; char==p -> GF(p).
    """
    x = symbols("x")
    if char == 0:
        dom = QQ
    else:
        dom = GF(char)
    if isinstance(poly, Poly):
        poly = poly.as_expr()
    return Poly(poly, x, domain=dom)


def is_ca(poly, char):
    """Exact decision of the CA hypothesis.

    True iff deg(f) = n >= 1 and gcd(f, f^(i)) is non-constant for every
    i = 1 .. n-1 over the base field of characteristic ``char``. For n = 1 the
    quantified range is empty, so it returns True vacuously.

    Handles the char-p case where a derivative is identically zero: gcd(f, 0)
    = f, which is non-constant, so the hypothesis still holds there.
    """
    f = _coerce(poly, char)
    n = f.degree()
    if n is None or n < 1:
        return False
    if n == 1:
        return True
    d = f
    for _i in range(1, n):
        d = d.diff()
        g = f.gcd(d)
        if g.degree() < 1:
            return False
    return True


def is_pure_power(poly, char):
    """Exact decision that f is a pure power of a linear polynomial.

    True iff over K-bar, f has exactly one distinct root, of multiplicity
    equal to its degree — i.e. f = c*(x-a)^n for some c, a in K-bar. Because
    the property is insensitive to base change, it is decided over the given
    base field by factoring the monic part: f is a pure power iff its monic
    reduction factors as a single linear irreducible factor with multiplicity
    n.
    """
    f = _coerce(poly, char)
    n = f.degree()
    if n is None or n < 0:
        return False
    if n == 0:
        # constant polynomial; convention: not a pure power of a linear factor
        return False
    mono = f.monic()
    _content, factors = mono.factor_list()
    if len(factors) != 1:
        return False
    base, mult = factors[0]
    if mult != n:
        return False
    return base.degree() == 1


def is_counterexample(poly, char):
    """True iff the CA hypothesis holds AND f is not a pure power."""
    return is_ca(poly, char) and not is_pure_power(poly, char)


def is_ca_hasse(poly, char):
    """Exact decision of the CA hypothesis in the HASSE-derivative
    formulation: gcd(f, H_i(f)) non-constant for every i = 1 .. n-1, where
    H_i(f) = sum_j C(j, i) c_j x^(j-i) is the i-th Hasse derivative
    (binomial-coefficient derivative, computed here over the exact domain).

    Char-p subtlety (why this is a separate function from is_ca):
    the ordinary i-th derivative vanishes identically over F_p for i >= p
    (i! = 0 in F_p), so gcd(f, f^(i)) = f holds trivially there.  The Hasse
    derivative H_i is generally NONZERO in that range, so the two hypotheses
    agree in characteristic 0 and for p >= n, but DIFFER when p < n.

    The published bad-prime lists (Castryck et al. 2012, Thm 4; Draisma-de
    Jong for degree 4; Schaub-Spivakovsky) are for the HASSE formulation:
    e.g. p = 2 is GOOD for n = 4 there (x^4 + x^2 over F_2 has H_2 = 1, a
    nonzero constant, so gcd(f, H_2) = 1 and the hypothesis fails), while
    the ordinary formulation makes x^4 + x^2 a counterexample (all ordinary
    derivatives vanish).  The standard char-p witness x^{p+1} - x^p is
    Hasse-CA for every prime p.
    """
    f = _coerce(poly, char)
    n = f.degree()
    if n is None or n < 1:
        return False
    if n == 1:
        return True
    x = symbols("x")
    coeffs = [f.coeff_monomial(x ** j) for j in range(n + 1)]
    for i in range(1, n):
        H_expr = sum(comb(j, i) * coeffs[j] * x ** (j - i)
                     for j in range(i, n + 1))
        H = Poly(H_expr, x, domain=f.get_domain())
        g = f.gcd(H)
        if g.degree() < 1:
            return False
    return True


def charp_witness(p):
    """The characteristic-p counterexample family f = x^{p+1} - x^p over GF(p).

    CA is false in char p: with f = x^p*(x - 1) over F_p the hypothesis
    gcd(f, f^(i)) != 1 holds for every i = 1 .. p (indeed f is divisible by
    gcd(x^p, x - 1)-free powers in a way that satisfies every gcd test), yet
    f has two distinct roots 0 and 1, so it is NOT a pure power. This is the
    negative control every argument in the run must survive: the checker
    reports it as a counterexample, which is exactly what it should not be
    able to do if CA were true in char p.

    Returns a sympy Poly over GF(p).  p must be prime.
    """
    x = symbols("x")
    return Poly(x ** (p + 1) - x ** p, x, domain=GF(p))


# ---------------------------------------------------------------------------
# Guard set
# ---------------------------------------------------------------------------

def _f_pure_power(x, a, n, char):
    if char == 0:
        return Poly((x - a) ** n, x, domain=QQ)
    return Poly((x - a) ** n, x, domain=GF(char))


def run_guards(*, verbose=True):
    """Run the complete guard set. Returns (ok: bool, lines: list[str]).

    Guards (each printed explicitly with its value):
      1. (x-a)^n passes is_ca AND is_pure_power over QQ for n = 1..8 and
         a in {-2, 0, 1, 5}.
      2. generic random monic polynomials of degrees 2..7 over QQ FAIL is_ca.
      3. THE CHAR-p NEGATIVE CONTROL: over GF(p), f = x^{p+1} - x^p must give
         is_ca True and is_pure_power False for p = 2,3,5,7. This is what
         proves the checker measures the right thing: it *is* a CA polynomial
         but is NOT a pure power.
      4. f = x^n (pure power of x) over GF(p) gives is_pure_power True.
      5. CHAR-0 AGREEMENT GUARD: is_ca(f, 0) == is_ca_hasse(f, 0) on every
         char-0 guard polynomial of guards 1-2 plus a set of structured
         polynomials (repeated-root non-pure-powers, distinct-root, mixed).
         In characteristic 0 the ordinary i-th derivative differs from the
         Hasse i-th derivative by the nonzero factor i!, so the two
         formulations must decide the hypothesis identically. This guard
         exists so the Hasse formulation (used for the published char-p
         bad-prime lists) can never silently drift from the canonical
         ordinary-derivative oracle in char 0.
    """
    x = symbols("x")
    lines = []
    ok = True

    def rec(label, passed, detail=""):
        nonlocal ok
        ok = ok and passed
        lines.append(
            f"[{'PASS' if passed else 'FAIL'}] {label}"
            + (f"  ({detail})" if detail else "")
        )

    # --- Guard 1: (x-a)^n over QQ -----------------------------------------
    lines.append("-- Guard 1: (x-a)^n over QQ, n=1..8, a in {-2,0,1,5} "
                 "(should be is_ca & pure power)")
    for n in range(1, 9):
        for a in (-2, 0, 1, 5):
            f = _f_pure_power(x, a, n, 0)
            ca = is_ca(f, 0)
            pp = is_pure_power(f, 0)
            rec(f"(x-{a})^{n}: is_ca={ca}, is_pure_power={pp}",
                ca and pp,
                f"n={n}, a={a}")

    # --- Guard 2: generic random monic degrees 2..7 over QQ fail ----------
    lines.append("-- Guard 2: generic random monic deg 2..7 over QQ "
                 "(should FAIL is_ca)")
    for n in range(2, 8):
        for seed in (3, 11, 29, 53):
            random.seed(seed)
            coeffs = [random.randint(-9, 9) for _ in range(n)]
            g = Poly(x ** n + sum(coeffs[i] * x ** (n - 1 - i)
                                  for i in range(n)), x, domain=QQ)
            ca_n = is_ca(g, 0)
            rec(f"deg-{n} seed={seed} coeffs={coeffs}: is_ca={ca_n}",
                not ca_n,
                f"expected FAIL, got is_ca={ca_n}")

    # --- Guard 3: char-p negative control ----------------------------------
    lines.append("-- Guard 3: char-p witness x^{p+1}-x^p over GF(p) "
                 "(should be is_ca=True, is_pure_power=False, i.e. counterexample)")
    for p_ in [2, 3, 5, 7]:
        f = charp_witness(p_)
        ca = is_ca(f, p_)
        pp = is_pure_power(f, p_)
        ce = is_counterexample(f, p_)
        rec(f"x^{p_+1}-x^{p_} over GF({p_}): is_ca={ca}, is_pure_power={pp}, "
            f"counterexample={ce}",
            ca and not pp and ce,
            f"p={p_}")

    # --- Guard 4: f = x^n over GF(p) is a pure power -----------------------
    lines.append("-- Guard 4: f = x^n over GF(p) (should be is_pure_power=True)")
    for p_ in [2, 3, 5, 7]:
        f = Poly(x ** p_, x, domain=GF(p_))
        pp = is_pure_power(f, p_)
        ca = is_ca(f, p_)
        rec(f"x^{p_} over GF({p_}): is_pure_power={pp}, is_ca={ca}",
            pp,
            f"p={p_}")

    # --- Guard 5: char-0 agreement is_ca == is_ca_hasse --------------------
    lines.append("-- Guard 5: is_ca(f, 0) == is_ca_hasse(f, 0) over QQ "
                 "(ordinary and Hasse formulations must agree in char 0)")
    guard5_polys = []
    # all guard-1 pure powers
    for n in range(1, 9):
        for a in (-2, 0, 1, 5):
            guard5_polys.append(("(x-a)^n", _f_pure_power(x, a, n, 0)))
    # all guard-2 random monics (rebuilt identically)
    for n in range(2, 8):
        for seed in (3, 11, 29, 53):
            random.seed(seed)
            coeffs = [random.randint(-9, 9) for _ in range(n)]
            g = Poly(x ** n + sum(coeffs[i] * x ** (n - 1 - i)
                                  for i in range(n)), x, domain=QQ)
            guard5_polys.append(("random deg-%d" % n, g))
    # structured char-0 polynomials: repeated roots, distinct roots, mixed
    structured = [
        ("(x-1)^2 (x-2)", (x - 1) ** 2 * (x - 2)),       # not CA: gcd with f'' is 1
        ("(x-1)(x-2)(x-3)", (x - 1) * (x - 2) * (x - 3)),  # not CA: distinct roots
        ("(x-1)^2 (x-2)^2", (x - 1) ** 2 * (x - 2) ** 2),
        ("(x+2)^3 (x-1)", (x + 2) ** 3 * (x - 1)),
        ("x^4 + x^2 + 1", x ** 4 + x ** 2 + 1),
        ("(x^2+x+1)^2", (x ** 2 + x + 1) ** 2),
        ("(x-1)^3", (x - 1) ** 3),                        # CA pure power
        ("x^5 + 2 x^3 - x + 7", x ** 5 + 2 * x ** 3 - x + 7),
    ]
    for label, expr in structured:
        guard5_polys.append((label, Poly(expr, x, domain=QQ)))
    n_agree = 0
    for label, poly in guard5_polys:
        ca = is_ca(poly, 0)
        hasse = is_ca_hasse(poly, 0)
        agree = ca == hasse
        n_agree += agree
        rec(f"{label}: is_ca={ca}, is_ca_hasse={hasse}",
            agree,
            f"n={poly.degree()}")
    rec(f"agreement count {n_agree}/{len(guard5_polys)}", n_agree == len(guard5_polys))

    return ok, lines


def main():
    """Command line entry: run guards, capture output, exit 0 iff all pass."""
    out_dir = os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "out")
    os.makedirs(out_dir, exist_ok=True)
    capture_path = os.path.join(out_dir, "oracle_guard.captured.txt")

    ok, lines = run_guards(verbose=True)

    header = [
        "CANONICAL ORACLE GUARD RUN (code/lib/casas_alvero.py)",
        "oracle functions: is_ca / is_pure_power / is_counterexample / is_ca_hasse from lib.casas_alvero",
        "range: (x-a)^n n=1..8 a in {-2,0,1,5} over QQ; random monic deg 2..7 over QQ; "
        "char-p witnesses x^{p+1}-x^p for p=2,3,5,7; x^n over GF(p); "
        "char-0 is_ca==is_ca_hasse agreement guard on 64+8 polynomials over QQ",
    ]
    body = header + [""] + lines + [""]
    body.append(f"ALL GUARDS {'PASSED' if ok else 'FAILED'}")
    text = "\n".join(body)
    with open(capture_path, "w") as fh:
        fh.write(text + "\n")

    for line in body:
        print(line)
    print(f"\ncapture saved to {capture_path}")
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
