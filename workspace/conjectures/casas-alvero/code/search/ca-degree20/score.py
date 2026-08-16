"""Scorer for the degree-20 Casas-Alvero candidate search.

Usage
-----
    python score.py <path/to/candidate/module.py>

The candidate module is imported *by literal path* via importlib (never by
adding it to PYTHONPATH) and is expected to expose a monic degree-20
polynomial over Q in the symbol x — conventionally the attribute ``f``, but
any module attribute that sympy recognises as a polynomial in x is accepted.

It prints EXACTLY ONE line and exits 0:
    SCORE: k          k = #{ j in 1..19 : deg(gcd(f, f^(j))) > 0 over Q[x] }
    INVALID: <reason> the candidate is rejected (see rules below).

Exactness
---------
Every decision is a sympy exact computation over QQ: Polynomial gcd,
.degree(), monic(), coefficient lookup. No floating point anywhere.

Rules (reasons are passed through in the INVALID line)
-------------------------------------------------------
(a) f is (x-a)^20 for some a  ->  INVALID: ...(x-a)^20...  (the trivial
    family the conjecture allows — the exploit; it would trivially score 19).
(b) f not monic / not degree exactly 20 / has non-rational coefficients  ->
    INVALID with the specific reason.
(c) the module fails to import / does not expose a polynomial in x  ->
    INVALID with the import/no-such-polynomial reason.

The (a) check is made *first* on a valid (monic, degree 20, rational)
polynomial, so it has priority over the plain SCORE computation.

Return value: 0 when a SCORE is printed or a candidate is rejected as INVALID
(error in *our* machinery — a missing argv, an unreadable path — exits 2).
"""

import importlib.util
import sys

import sympy
from sympy import Poly, symbols, QQ, SympifyError


DEGREE = 20
NUMBER_OF_DERIVATIVES = DEGREE - 1  # 19


def _is_trivial_family(f):
    """True iff f = (x-a)^DEGREE for some a over Q (pure power of a linear)."""
    if DEGREE <= 0:
        return False
    mono = f.monic()
    _content, factors = mono.factor_list()
    if len(factors) != 1:
        return False
    base, mult = factors[0]
    return mult == DEGREE and base.degree() == 1


def _load_polynomial(path):
    """Import the module at ``path`` and return a sympy Poly in x, or None.

    Returns ``(poly, error_reason)``. On any failure the reason is a
    human-readable string explaining *why* (import failed / no polynomial in x
    / not a polynomial), so it can be passed straight into the INVALID line.
    """
    spec = importlib.util.spec_from_file_location("_candidate", path)
    if spec is None or spec.loader is None:
        return None, "could not build import spec from path"
    try:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
    except Exception as exc:  # noqa: BLE001 - report the exact import failure
        return None, "import failed: %s" % (exc,)

    x = symbols("x")
    found = None
    for name in dir(module):
        if name.startswith("_"):
            continue
        attr = getattr(module, name)
        # Only genuine symbolic expressions / numbers qualify. A callable
        # (function/module), a string, or a singleton would otherwise be
        # sympified by string-fallback into a junk degree-0 polynomial, which
        # would wrongly mask the "no polynomial here" case.
        if callable(attr) or isinstance(attr, (str, bytes, type(None))):
            continue
        try:
            poly = Poly(attr, x)
        except (SympifyError, TypeError, ValueError, AttributeError,
                sympy.polys.polyerrors.PolynomialError):
            continue
        # Univariate polynomial in x with at least one term.
        if poly.gens == (x,) and poly.degree() is not None and poly.degree() >= 1:
            found = poly
            break
    if found is None:
        return None, "no polynomial in x exposed by module"
    return found, None


def score(poly):
    """Return how many of f',..,f^(19) share a non-constant factor with f.

    Exact over QQ: ``k = #{ j in 1..19 : deg(gcd(f, f^(j))) > 0 }``.
    """
    n = poly.degree()
    k = 0
    d = poly
    for _j in range(1, n):
        d = d.diff()
        if poly.gcd(d).degree() > 0:
            k += 1
    return k


def _validate(poly):
    """Return None if valid, else (DEGREE_OK, reason) --- reason if ``invalid``.

    Checks, in order: domain is rational (QQ), monic leading coeff == 1,
    degree exactly 20. Returns the reason string on the first failure, or
    None if the polynomial passes all three.
    """
    # non-rational coefficients: every coefficient must be an exact rational.
    # (Tested per-coefficient because a Gaussian/algebraic domain would crash
    # a domain=QQ rebuild rather than reject cleanly.)
    if not all(c.is_rational for c in poly.all_coeffs()):
        return "non-rational coefficients (domain %s)" % poly.get_domain()
    lc = poly.LC()
    if lc != 1:
        return "not monic (leading coefficient %s)" % lc
    if poly.degree() != DEGREE:
        return "degree %s != %s" % (poly.degree(), DEGREE)
    return None


def main(argv):
    if len(argv) != 2:
        sys.stderr.write(
            "usage: python score.py <path/to/candidate/module.py>\n"
        )
        return 2

    path = argv[1]
    poly, err = _load_polynomial(path)
    if poly is None:
        print("INVALID: %s" % err)
        return 0

    # Bring the polynomial over an explicit rational domain once we know it is
    # rational, so scoring and the factor-based trivial-family check run over QQ.
    if all(c.is_rational for c in poly.all_coeffs()):
        poly = poly.set_domain(QQ)

    invalid = _validate(poly)
    if invalid is not None:
        print("INVALID: %s" % invalid)
        return 0

    if _is_trivial_family(poly):
        print("INVALID: f is (x-a)^%d (the trivial family the conjecture allows)"
              % DEGREE)
        return 0

    k = score(poly)
    print("SCORE: %d" % k)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
