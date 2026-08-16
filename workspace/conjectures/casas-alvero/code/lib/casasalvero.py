"""Casas-Alvero exact machinery for the S_n scheme: elimination, Groebner
bases and radical-membership tests used to verify CA for small degrees.

One-canonical-oracle rule
-------------------------
The derivative-sharing hypothesis and the pure-power conclusion are decided
ONLY by ``lib.casas_alvero`` (is_ca / is_pure_power / is_counterexample).
This module does NOT re-implement them. It builds and eliminates the S_n
scheme, which is a different object: the *equations* f(r_i)=0, f^(i)(r_i)=0
in (a_1..a_n, r_1..r_{n-1})-space, not the univariate hypothesis test.

All arithmetic here is exact (rationals over QQ, or modular arithmetic over
GF(p)). No floating point anywhere. A root computed by this module is an exact
symbolic object or a residue class, never a float.

What the S_n scheme proves
--------------------------
CA in degree n over Qbar is equivalent to: every point satisfying the S_n
equations has all r_i equal and f = (x - r_1)^n. Both directions of that
equivalence are reduced here to exact ideal computations over QQ:

  * direction V(I) subset V(P): every generator of the pure-power ideal P is
    in rad(I), tested by the Rabinowitsch trick
        p in rad(J)  <=>  1 in (J, 1 - t p),
    checked by an exact Groebner basis (unit ideal). Correct over an
    algebraically closed field by the Nullstellensatz; the GB test is
    independent of term order (reduced GB = [1] iff unit ideal).
  * direction V(P) subset V(I): every generator of I vanishes identically on
    the pure-power locus by explicit exact substitution.

Both directions passing => the S_n scheme is set-theoretically the
pure-power locus => CA in degree n, proved by exact elimination over QQ.

Validation performed on this module
-----------------------------------
- ca_oracle-equivalent guard set: same cases run through lib.casas_alvero
  (pure powers pass, generic random fails, char-p witnesses x^(p+1)-x^p over
  GF(2), GF(3), GF(5) pass the hypothesis and are NOT pure powers).
- Rabinowitsch control cases through both sympy and Singular:
    a1 in rad(a1^2)      -> True   (Nullstellensatz: V(a1^2)=V(a1))
    a1+1 in rad(a1^2)    -> False
    a1 in rad(a1, r1)    -> True   (radical ideal)
  Both engines agree on all three.
- S_n equations vanish identically on the pure-power locus for n = 2..6.
- Hasse scheme cross-check: hasse_sn_equations(4) over F_2 marks p=2 GOOD
  (rad(I)=rad(P) holds), matching the published d=4 bad-prime list {3,5,7};
  the ordinary scheme marks p=2 bad because f^(i) vanishes identically for
  i >= 2 there (ordinary-vs-Hasse divergence, see sn_equations warning).
"""
from __future__ import annotations

import subprocess
import time
from math import comb

import sympy as sp

# the canonical oracle (hypothesis + pure-power) lives in lib.casas_alvero
from lib.casas_alvero import is_ca, is_pure_power, is_counterexample  # noqa: F401

# ---------------------------------------------------------------------------
# S_n scheme
# ---------------------------------------------------------------------------

def sn_equations(n, a, r, K=None):
    """Defining equations of the S_n scheme:
       f(r_i) = 0,  f^(i)(r_i) = 0   (i = 1..n-1)
    with f = x^n + a_1 x^{n-1} + ... + a_n monic.
    a  : list of n symbols a_1..a_n
    r  : list of n-1 symbols r_1..r_{n-1}
    K  : coefficient field (None -> QQ; GF(p) via modulus elsewhere)
    Returns list of 2(n-1) polynomials in QQ[a,r].

    CHARACTERISTIC-p WARNING: this is the ORDINARY-derivative scheme.  Over
    F_p the ordinary i-th derivative vanishes identically for i >= p, so the
    equations f^(i)(r_i) = 0 become 0 = 0 and the scheme is NOT the CA
    hypothesis of the published char-p literature (which uses Hasse
    derivatives).  The ordinary and Hasse schemes agree in characteristic 0
    and for p >= n; they differ for p < n.  Use hasse_sn_equations for the
    formulation the published bad-prime lists are computed with.
    """
    x = sp.symbols("x")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    eqs = []
    for i in range(1, n):
        eqs.append(f.subs(x, r[i - 1]))
        eqs.append(f.diff(x, i).subs(x, r[i - 1]))
    return eqs


def hasse_derivative(f, x, i):
    """i-th Hasse derivative H_i(f) = sum_j C(j,i) c_j x^(j-i), as an exact
    expression with integer binomial coefficients (valid in every
    characteristic; over F_p the coefficients are reduced mod p at use).
    f must be a polynomial expression in x with symbolic coefficients."""
    p = sp.Poly(sp.expand(f), x)
    coeffs = {j: p.coeff_monomial(x ** j) for j in range(p.degree() + 1)}
    return sum(sp.binomial(j, i) * c * x ** (j - i)
               for j, c in coeffs.items() if j >= i and c != 0)


def hasse_sn_equations(n, a, r):
    """S_n scheme equations in the HASSE formulation:
       f(r_i) = 0,  H_i(f)(r_i) = 0   (i = 1..n-1),
    where H_i is the i-th Hasse derivative.  This is the formulation the
    published char-p bad-prime lists are defined with (Castryck et al. 2012;
    Schaub-Spivakovsky).  In characteristic p >= n it coincides with the
    ordinary scheme sn_equations; for p < n it does not (ordinary i-th
    derivatives vanish for i >= p).  Equality rad(I) = rad(P) of this scheme
    is exactly Hasse-CA in degree n over the field of characteristic p."""
    x = sp.symbols("x")
    f = x ** n + sum(a[i] * x ** (n - 1 - i) for i in range(n))
    eqs = []
    for i in range(1, n):
        eqs.append(f.subs(x, r[i - 1]))
        eqs.append(hasse_derivative(f, x, i).subs(x, r[i - 1]))
    return eqs


def pure_power_generators(n, a, r, K=None):
    """Generators of the ideal P_n of the pure-power locus:
       r_j - r_1 (j=2..n-1),   a_j - (-1)^j C(n,j) r_1^j  (j=1..n).
    On this locus f = (x - r_1)^n.  Returns a list of 2n-2 polynomials."""
    gens = []
    for j in range(2, n):
        gens.append(r[j - 1] - r[0])
    for j in range(1, n + 1):
        gens.append(a[j - 1] - (-1) ** j * comb(n, j) * r[0] ** j)
    return gens


# ---------------------------------------------------------------------------
# Exact radical membership: Rabinowitsch trick
# ---------------------------------------------------------------------------

def rabinowitsch_membership(p, ideal_gens, syms, order="grevlex", modulus=None,
                            engine="sympy", n=None):
    """p in rad(J)  <=>  1 in (J, 1 - t p), checked by exact Groebner basis.
    engine: 'sympy' or 'singular'. Terms orders: grevlex (degrevlex, dp),
    lex (lp), grlex (deglex, Dp). n = number of a-coefficients (degree), only
    needed by the singular engine to declare the ring.
    Returns (bool, engine, order, elapsed_seconds)."""
    t = sp.symbols("t")
    aug = list(ideal_gens) + [1 - t * p]
    if engine == "sympy":
        start = time.monotonic()
        gb = sp.groebner(aug, *(list(syms) + [t]), order=order,
                         modulus=modulus)
        # unit ideal  <=>  reduced Groebner basis contains a nonzero constant
        is_one = any(g.total_degree() == 0 and g != 0 for g in gb.polys)
        elapsed = time.monotonic() - start
        return is_one, "sympy", order, elapsed
    elif engine == "singular":
        if n is None:
            raise ValueError("singular engine requires n (degree)")
        script = _singular_membership_script(p, ideal_gens, n, order)
        start = time.monotonic()
        res = _run_singular(script)
        elapsed = time.monotonic() - start
        ok = "MEMBERSHIP_YES" in res["stdout"]
        return ok, "singular", order, elapsed
    raise ValueError(engine)


def _run_singular(script: str, timeout=1800):
    """Run a Singular script through `Singular -q`, return dict with stdout,
    stderr, returncode."""
    import tempfile, os
    fd, path = tempfile.mkstemp(suffix=".sing", dir="/workspace/code/out")
    with os.fdopen(fd, "w") as fh:
        fh.write(script)
    try:
        proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                              text=True, timeout=timeout)
        return {"stdout": proc.stdout, "stderr": proc.stderr,
                "returncode": proc.returncode, "script": script}
    finally:
        os.unlink(path)


def _singular_membership_script(p, ideal_gens, n, order):
    """Singular script for the Rabinowitsch test 1 in (J, 1 - t p)."""
    ordmap = {"grevlex": "dp", "lex": "lp", "grlex": "Dp"}
    ringvars = ", ".join(["a(%d)" % i for i in range(1, n + 1)]
                         + ["r(%d)" % i for i in range(1, n)] + ["t"])
    body = ["ring S = 0, (%s), %s;" % (ringvars, ordmap[order]),
            "poly p = %s;" % _to_singular(p),
            "ideal J = %s;" % ", ".join(_to_singular(g) for g in ideal_gens),
            "ideal K = J, 1 - t*p;",
            "ideal G = std(K);",
            "if (deg(lead(G[1])) == 0) { \"MEMBERSHIP_YES\"; } "
            "else { \"MEMBERSHIP_NO\"; }",
            ]
    return "\n".join(body) + "\n"


def _to_singular(expr):
    """Render a sympy expression (QQ coefficients, symbols a_i, r_i) as a
    Singular polynomial string with exact rational coefficients, using
    Singular's indexed names a(1), r(1)."""
    def name_of(sy):
        s = str(sy)
        if s.startswith("a_"):
            return "a(%s)" % s[2:]
        if s.startswith("r_"):
            return "r(%s)" % s[2:]
        return s

    def rec(e):
        if e.is_Integer:
            return str(e)
        if e.is_Rational:
            return "%s/%s" % (e.p, e.q)
        if e.is_Symbol:
            return name_of(e)
        if e.is_Add:
            return "(" + "+".join(rec(a) for a in e.args) + ")"
        if e.is_Mul:
            return "*".join("(%s)" % rec(a) if a.is_Add else rec(a)
                            for a in e.args)
        if e.is_Pow:
            return "(%s)^%d" % (rec(e.base), e.exp)
        if e.is_Number:
            return str(e)
        return sp.sstr(e)

    return rec(sp.sympify(expr))


# ---------------------------------------------------------------------------
# Elimination / radical-membership proof of CA for a fixed degree
# ---------------------------------------------------------------------------

def prove_ca_elimination(n, engine="sympy", order="grevlex",
                         timeouts=(120, 600, 1800)):
    """Verify rad(I_n) = rad(P_n) by exact elimination, i.e. CA in degree n:
      direction 1 (V(I) subset V(P)): every generator of P_n lies in
          rad(I_n) -- Rabinowitsch test per generator;
      direction 2 (V(P) subset V(I)): every generator of I_n vanishes on the
          pure-power locus -- exact symbolic substitution.
    Returns a report dict with per-test results and timings. If every test
    passes, all solutions of the S_n equations over Qbar have all r_i equal
    and f = (x - r_1)^n:  exactly CA in degree n, proved by exact elimination
    over QQ (a Groebner basis computation)."""
    a = sp.symbols("a_1:%d" % (n + 1))
    r = sp.symbols("r_1:%d" % n)
    syms = list(a) + list(r)
    eqs = sn_equations(n, a, r)
    P = pure_power_generators(n, a, r)
    report = {"n": n, "engine": engine, "order": order,
              "ring": "QQ[a_1..a_n, r_1..r_{n-1}]",
              "num_eqs": len(eqs), "num_P_gens": len(P), "tests": []}
    # direction 1: radical membership of each P generator
    allpass = True
    for g in P:
        kw = {"order": order}
        if engine == "singular":
            kw["n"] = n
        ok, eng, ord_, dt = rabinowitsch_membership(g, eqs, syms,
                                                    engine=engine, **kw)
        allpass = allpass and ok
        report["tests"].append({"type": "radical_membership",
                                "poly": str(g), "passed": ok,
                                "engine": eng, "order": ord_,
                                "elapsed": dt})
    # direction 2: substitute the pure-power locus into the I_n generators
    for i, g in enumerate(eqs):
        subs = {r[j]: r[0] for j in range(1, n - 1)}
        for j in range(1, n + 1):
            subs[a[j - 1]] = (-1) ** j * comb(n, j) * r[0] ** j
        val = sp.simplify(g.subs(subs) - 0)
        ok = val == 0
        allpass = allpass and ok
        report["tests"].append({"type": "vanishes_on_pure_power",
                                "poly": str(g), "passed": ok,
                                "engine": "symbolic", "order": "-",
                                "elapsed": 0.0})
    report["passed"] = allpass
    report["tests_passed"] = sum(1 for t_ in report["tests"] if t_["passed"])
    report["tests_total"] = len(report["tests"])
    return report


def sn_ideal_groebner(n, order="grevlex", engine="sympy", modulus=None):
    """Compute the Groebner basis of the S_n ideal I_n over QQ (or GF(p) via
    modulus). Returns dict with n, order, engines, syms, eqs, elapsed, gb."""
    a = sp.symbols("a_1:%d" % (n + 1))
    r = sp.symbols("r_1:%d" % n)
    eqs = sn_equations(n, a, r)
    syms = list(a) + list(r)
    if engine == "sympy":
        start = time.monotonic()
        kwargs = {}
        if modulus is not None:
            kwargs["modulus"] = modulus
        gb = sp.groebner(eqs, *syms, order=order, **kwargs)
        elapsed = time.monotonic() - start
        return {"n": n, "order": order, "engine": "sympy", "syms": syms,
                "eqs": eqs, "gb": gb, "elapsed": elapsed}
    else:
        raise NotImplementedError("gb via singular handled in elim script")