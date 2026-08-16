"""Naive, obviously-correct oracle for the Casas-Alvero derivative-sharing
hypothesis.

For a monic polynomial f of degree n over a field K (char 0 = Q, or F_p),
the hypothesis is:

    gcd(f, f^(i)) != 1   for every i = 1, ..., n-1

where f^(i) is the i-th formal derivative and gcd is taken in K[x].

This module decides that hypothesis EXACTLY, using Euclid's algorithm over an
exact coefficient ring, and separately decides whether f is a pure power
f = (x - a)^n.  No floating-point root finding anywhere: over Q we use
rational (Fraction) arithmetic; over F_p we use integers mod p.

It is deliberately naive -- a direct implementation of the definition -- and
is meant to be the oracle other (faster) methods are checked against.

Public API
----------
satisfies_hypothesis(f, p=None) -> bool
    f : list of coefficients in ASCENDING order (f[k] = coeff of x^k),
        assumed monic (highest coeff == 1).
    p : None => arithmetic over Q (Fractions); an int prime => over F_p.
    Returns True iff gcd(f, f^(i)) is non-constant for every i=1..n-1.

is_pure_power(f, p=None) -> bool
    Returns True iff f equals (x - a)^n for some a in the coefficient field.

ca_verdict(f, p=None) -> (hypothesis_holds, is_pure_power)
    Pair returned together so a caller can read off the CA conclusion and,
    crucially, the negative-control case (hypothesis holds but NOT a pure
    power = a char-p counterexample) unambiguously.
"""

from fractions import Fraction


def _ring(p):
    """Return an exact scalar field as a dict of operations.

    p is None  -> Q via fractions.Fraction
    p is prime -> Z/pZ via integers (inverses by Fermat).
    """
    if p is None:
        return {
            "zero": Fraction(0),
            "one": Fraction(1),
            "add": lambda x, y: x + y,
            "neg": lambda x: -x,
            "mul": lambda x, y: x * y,
            "inv": lambda x: 1 / x,
            "is_zero": lambda x: x == 0,
        }
    else:
        return {
            "zero": 0,
            "one": 1,
            "add": lambda x, y: (x + y) % p,
            "neg": lambda x: (-x) % p,
            "mul": lambda x, y: (x * y) % p,
            "inv": lambda x: pow(x, p - 2, p),  # Fermat: valid for x != 0
            "is_zero": lambda x: x % p == 0,
        }


def _strip(poly, ring):
    """Remove trailing (highest-degree) zero coefficients."""
    out = list(poly)
    while out and ring["is_zero"](out[-1]):
        out.pop()
    return out


def _deg(poly):
    return len(poly) - 1 if poly else -1


def _monic(poly, ring):
    """Make leading coefficient 1 (field: multiply by inverse of lead)."""
    poly = _strip(poly, ring)
    if not poly:
        return []
    lead = poly[-1]
    if ring["is_zero"](lead - ring["one"]):
        return poly
    inv = ring["inv"](lead)
    return [ring["mul"](c, inv) for c in poly]


def _mod(a, b, ring):
    """a mod b over the field, both as ascending coeff lists, b nonzero."""
    a = _strip(a, ring)
    b = _strip(b, ring)
    db = _deg(b)
    assert db >= 0
    lead_inv = ring["inv"](b[-1])
    # copy a, reduce degree by subtracting multiples of b
    r = list(a)
    while len(r) - 1 >= db and not (len(r) == 0):
        r = _strip(r, ring)
        if not r:
            break
        dr = _deg(r)
        if dr < db:
            break
        # factor to kill leading term of r
        factor = ring["mul"](r[-1], lead_inv)
        shift = dr - db  # b shifted up by `shift`; leading terms align
        # subtract factor * b * x^shift
        for k in range(db + 1):
            r[k + shift] = ring["add"](r[k + shift], ring["neg"](ring["mul"](factor, b[k])))
        # r[-1] is now zero; loop strips it
    return _strip(r, ring)


def _gcd(a, b, ring):
    a = _strip(a, ring)
    b = _strip(b, ring)
    while b and not (len(b) == 1 and ring["is_zero"](b[-1])):
        a, b = b, _mod(a, b, ring)
    # b == 0 (empty); gcd is monic(a)
    return _monic(a, ring)


def _deriv(poly, ring):
    """Formal derivative of ascending coeff list."""
    if not poly:
        return []
    return [ring["mul"](k, poly[k]) for k in range(1, len(poly))]


def satisfies_hypothesis(f, p=None):
    """True iff gcd(f, f^(i)) is non-constant for every i = 1..n-1."""
    ring = _ring(p)
    f = _strip(list(f), ring)
    n = _deg(f)
    if n < 1:
        return False  # degree-0 has no derivatives to check; degenerate
    # current derivative; iterate
    d = _deriv(f, ring)   # f^(1)
    for i in range(1, n):  # i = 1 .. n-1
        if _deg(d) < 0:
            return False  # derivative identically zero -> gcd would be f, non-trivial
        g = _gcd(f, d, ring)
        if _deg(g) < 1:   # gcd is a non-zero constant
            return False
        d = _deriv(d, ring)  # next derivative
    return True


def is_pure_power(f, p=None):
    """True iff monic f of degree n equals (x - a)^n, a in an algebraic closure.

    Uses the char-safe characterization: f is a pure power of a linear
    polynomial exactly when it has a single distinct root, i.e. when the
    degree of its squarefree radical is 1.  The radical is computed by a
    recursion that is correct in every characteristic, including p | n where
    the elementary "a = -c_{n-1}/n" read-off fails and where
    deg(gcd(f,f')) == n-1 is NOT equivalent to pure power (multiplicities
    divisible by p survive in the gcd).
    """
    ring = _ring(p)
    f = _strip(list(f), ring)
    n = _deg(f)
    if n < 1:
        return False
    rad = _radical(f, ring, p)
    return _deg(rad) == 1


def _polydiv(a, b, ring):
    """a / b as exact division (b monic or leading inverted), returns quotient.
    Assumes b divides a.  Ascending coeff lists."""
    a = _strip(a, ring)
    b = _strip(b, ring)
    db = _deg(b)
    assert db >= 0
    lead_inv = ring["inv"](b[-1])
    # normalize: q is built in descending-power steps; we work on a copy
    r = list(a)
    q = [ring["zero"]] * (len(a) - db)
    while len(r) - 1 >= db and len(r) > 0:
        r = _strip(r, ring)
        if not r:
            break
        dr = _deg(r)
        if dr < db:
            break
        factor = ring["mul"](r[-1], lead_inv)
        shift = dr - db
        q[shift] = factor
        for k in range(db + 1):
            r[k + shift] = ring["add"](r[k + shift],
                                       ring["neg"](ring["mul"](factor, b[k])))
    assert _deg(_strip(r, ring)) < 0, "exact division failed"
    return q


def _pth_root(f, ring, p):
    """If f is a perfect p-th power (char = p), return g with f = g(x^p).
    Over F_p every coefficient is its own p-th root, so this just keeps the
    coefficients whose monomial degree is divisible by p and rewrites x^(pk)
    as t^k."""
    assert p is not None
    out = []
    for k in range(0, len(f), p):
        out.append(f[k])
    # any nonzero coefficients in positions not divisible by p would make f
    # not a p-th power; caller ensures f'==0 which forces them absent
    return out


def _radical(f, ring, p):
    """Squarefree radical of f: product of its distinct irreducible factors,
    each with multiplicity 1.  Correct in every characteristic (including
    p | multiplicities), via the recursion:
      R(f) = R(c) * R(g) / gcd(R(c), R(g)),  c = f/g, g = gcd(f, f') (f'!=0)
      R(f) = R(pth_root(f))                                   (f' == 0)
    Returned as an ascending coefficient list."""
    f = _strip(f, ring)
    if _deg(f) < 1:
        return [ring["one"]]  # constant: only the empty (trivial) radical 1
    d = _deriv(f, ring)
    if _deg(_strip(d, ring)) < 0:          # derivative identically zero
        rootpoly = _pth_root(f, ring, p)    # f = g(x^p): same roots as g
        return _radical(_strip(rootpoly, ring), ring, p)
    g = _gcd(f, d, ring)
    if _deg(g) < 1:                        # gcd constant -> f squarefree
        return _monic(f, ring)
    c = _polydiv(f, g, ring)
    Rc = _radical(c, ring, p)
    Rg = _radical(g, ring, p)
    h = _gcd(Rc, Rg, ring)
    return _monic(_polydiv(_mul(Rc, Rg, ring), h, ring), ring)


def _mul(a, b, ring):
    """Polynomial product, ascending coeff lists."""
    if not a or not b:
        return []
    out = [ring["zero"]] * (len(a) + len(b) - 1)
    for i, ca in enumerate(a):
        for j, cb in enumerate(b):
            out[i + j] = ring["add"](out[i + j], ring["mul"](ca, cb))
    return _strip(out, ring)


def ca_verdict(f, p=None):
    """(hypothesis_holds, is_pure_power) for monic f."""
    return (satisfies_hypothesis(f, p), is_pure_power(f, p))


# ----------------------------------------------------------------------
# Checks against the worked examples of the statement
# ----------------------------------------------------------------------

def _run_checks():
    print("== Oracle checks against the statement's worked examples ==")
    ok = True

    # 1. Pure powers (x - a)^n over Q: converse, must satisfy hypothesis
    #    AND be pure powers.
    for n in range(1, 7):
        for a in (Fraction(0), Fraction(1), Fraction(3, 2)):
            # (x - a)^n coefficients ascending
            poly = [Fraction(0)] * (n + 1)
            poly[0] = Fraction(-a) ** n
            for k in range(n):
                poly[k] = Fraction(poly[k])
            # build via multiply
            lin = [-a, Fraction(1)]
            poly = [Fraction(1)]
            for _ in range(n):
                newlen = len(poly) + 1
                out = [Fraction(0)] * newlen
                for kk, c in enumerate(poly):
                    out[kk] += c * (-a)
                    out[kk + 1] += c * 1
                poly = out
            hyp = satisfies_hypothesis(poly, None)
            pp = is_pure_power(poly, None)
            match = (hyp is True) and (pp is True)
            ok &= match
            print(f"  (x-{a})^{n} over Q : hypothesis={hyp} "
                  f"pure_power={pp}  {'OK' if match else 'FAIL'}")

    # 2. Generic random f over Q: hypothesis must FAIL.
    from random import Random
    rng = Random(12345)
    generic_pass = True
    for _ in range(8):
        n = rng.randint(3, 8)
        poly = [Fraction(0)] * (n + 1)
        poly[n] = Fraction(1)
        for k in range(n):
            poly[k] = Fraction(rng.randint(-9, 9))
        # ensure not trivially a pure power
        hyp = satisfies_hypothesis(poly, None)
        if hyp:
            generic_pass = False
            print(f"  WARNING: generic f {poly} satisfied hypothesis")
    ok &= generic_pass
    print(f"  generic random monic f over Q (8 samples): "
          f"all fail hypothesis  {'OK' if generic_pass else 'FAIL'}")

    # 3. Char-p witnesses x^{p+1} - x^p: hypothesis TRUE, NOT pure power.
    for p in (2, 3, 5, 7):
        n = p + 1
        poly = [0] * (n + 1)
        poly[p] = (-1) % p   # -x^p
        poly[n] = 1          # + x^{p+1}
        hyp = satisfies_hypothesis(poly, p)
        pp = is_pure_power(poly, p)
        match = (hyp is True) and (pp is False)
        ok &= match
        print(f"  x^{p+1} - x^p in F_{p} : hypothesis={hyp} "
              f"pure_power={pp}  {'OK (char-p counterexample)' if match else 'FAIL'}")

    # 4. Pure powers over F_p: still satisfy hypothesis (trivially).
    for p in (3, 5):
        a = 1
        n = p
        poly = [1]  # (x - a)^p : coefficients
        # build
        lin = [(-a) % p, 1]
        poly = [1]
        for _ in range(n):
            newlen = len(poly) + 1
            out = [0] * newlen
            for kk, c in enumerate(poly):
                out[kk] = (out[kk] + c * (-a)) % p
                out[kk + 1] = (out[kk + 1] + c) % p
            poly = out
        hyp = satisfies_hypothesis(poly, p)
        pp = is_pure_power(poly, p)
        match = (hyp is True) and (pp is True)
        ok &= match
        print(f"  (x-1)^{p} in F_{p} : hypothesis={hyp} pure_power={pp} "
              f"{'OK' if match else 'FAIL'}")

    print("=" * 30)
    print("ALL WORKED-EXAMPLE CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    return ok


if __name__ == "__main__":
    _run_checks()
