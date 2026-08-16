"""Independent verification of the small-degree bad-prime lists over GF(p)
via the S_n scheme (radical-equality route): a second route distinct from the
minors-criterion computation.

Route (exact; all ideal work over GF(p)):
    CA_{n,p} holds  <=>  rad(I_n) = rad(P_n) in GF(p)[a_1..a_n, r_1..r_{n-1}]
        I_n = < f(r_i), H_i(f)(r_i) : i = 1..n-1 >     (S_n scheme equations,
                                        HASSE formulation: H_i is the i-th
                                        Hasse derivative, sum_j C(j,i) c_j
                                        x^(j-i) -- the formulation the
                                        published bad-prime lists are
                                        computed with; the ordinary
                                        derivative f^(i) vanishes
                                        identically over F_p for i >= p, so
                                        the ordinary scheme diverges there)
        P_n = < r_j - r_1, a_j - (-1)^j C(n,j) r_1^j > (pure-power locus)
  Direction 1 (the deciding test): every generator of P_n lies in rad(I_n),
      by the Rabinowitsch trick  g in rad(J) <=> 1 in (J, 1 - t g), decided
      by an exact Groebner basis over GF(p) (sympy groebner, modulus=p).
      Valid over any field (localization argument), no Nullstellensatz needed.
  Direction 2 (automatic, kept as a check): every generator of I_n vanishes
      identically on the pure-power locus, exact symbolic substitution
      (characteristic-independent: f = (x-r_1)^n there, so f(r_1) = 0 and
      f^(i)(r_1) = 0 for every i < n, in every characteristic).
  CA_{n,p} HOLDS iff both directions pass over GF(p); a failing radical
  membership => CA FAILS (p is a bad prime for n).

Expected (published; Castryck-Laterveer-Ounaies 2012, Theorem 4; d=4 case
from De Jong-Draisma):  n=3 bad primes {2};  n=4 bad primes {3,5,7}.
(In the Hasse formulation p=2 is GOOD for n=4: over F_2 every degree-4
polynomial has H_2 nonzero, so x^4 + x^2 -- a counterexample to the ordinary
formulation -- fails the Hasse hypothesis.)  This program computes the Hasse
list; the ordinary list {2,3,5,7} is included as a documented contrast.

Second, independent route (bounded oracle, exact, via lib.casas_alvero):
enumerate ALL monic degree-n polynomials over F_p for p in {2,3,5,7}
(<= 7^4 = 2401 polynomials) and count CA counterexamples (is_ca and not
is_pure_power).  Confirms each bad prime in the published list has an
explicit counterexample and the small good primes have none.

Entry guards (lib.casas_alvero, exact): (x-1)^n is_ca & pure power over QQ
and GF(2); x^3-x over QQ fails is_ca; random generic monics fail is_ca; the
char-p witnesses x^{p+1}-x^p are is_counterexample for p = 2,3,5.

Exit 0 iff all checks pass.  Capture to code/out/badprimes_sn.captured.txt.
"""
from __future__ import annotations

import random
import sys
import time
from itertools import product
from math import comb

import sympy as sp

from lib.casas_alvero import (
    is_ca,
    is_ca_hasse,
    is_pure_power,
    is_counterexample,
    charp_witness,
)
from lib.casasalvero import (
    sn_equations,
    hasse_sn_equations,
    pure_power_generators,
    rabinowitsch_membership,
)

CAPTURE = "/workspace/code/out/badprimes_sn.captured.txt"
PRIMES_BELOW_60 = [q for q in range(2, 60)
                   if all(q % d for d in range(2, int(q ** 0.5) + 1))]
EXPECTED_BAD = {3: {2}, 4: {3, 5, 7}}


def run_entry_guards():
    """Entry guard set through the canonical oracle. Returns (label, ok)."""
    x = sp.symbols("x")
    checks = []

    def rec(label, cond):
        checks.append((label, bool(cond)))
        return bool(cond)

    for n in (3, 4):
        rec(f"(x-1)^{n} over QQ: is_ca and pure power",
            is_ca((x - 1) ** n, 0) and is_pure_power((x - 1) ** n, 0))
    for p in (2, 3, 5):
        rec(f"(x-1)^3 over GF({p}): is_ca and is_ca_hasse and pure power",
            is_ca((x - 1) ** 3, p)
            and is_ca_hasse((x - 1) ** 3, p)
            and is_pure_power((x - 1) ** 3, p))
    rec("x^3 - x over QQ: is_ca False",
        not is_ca(x ** 3 - x, 0))
    for p in (2, 3, 5):
        rec(f"charp witness x^{p+1}-x^{p} over GF({p}): is_counterexample",
            is_counterexample(charp_witness(p), p))
    # Hasse-vs-ordinary divergence control: x^4 + x^2 over F_2 is an ordinary
    # counterexample but NOT Hasse-CA (H_2 = 1, nonzero constant).  This is
    # the exact mechanism by which p=2 is bad in the ordinary formulation and
    # good in the published (Hasse) one.
    x = sp.symbols("x")
    fdiv = sp.Poly(x ** 4 + x ** 2, x, domain=sp.GF(2))
    rec("x^4+x^2 over GF(2): is_ca True (ordinary) but is_ca_hasse False",
        is_ca(fdiv, 2) and not is_ca_hasse(fdiv, 2))
    for n in (3, 4, 5):
        for seed in (7, 19):
            random.seed(seed)
            coeffs = [random.randint(-9, 9) for _ in range(n)]
            g = sp.Poly(x ** n + sum(coeffs[i] * x ** (n - 1 - i)
                                     for i in range(n)), x, domain=sp.QQ)
            rec(f"random deg-{n} seed={seed} over QQ: is_ca False",
                not is_ca(g, 0))
    return checks


def direction1(n, a, r, eqs, p):
    """P_n subset rad(I_n) over GF(p): Rabinowitsch per P-generator.
    Returns list of (generator, ok, elapsed)."""
    syms = list(a) + list(r)
    out = []
    for g in pure_power_generators(n, a, r):
        ok, engine, order, dt = rabinowitsch_membership(
            g, eqs, syms, order="grevlex", modulus=p, engine="sympy")
        out.append((g, ok, dt))
    return out


def direction2(n, a, r, eqs):
    """I_n vanishes on the pure-power locus: exact symbolic substitution.
    Returns list of substituted values (each must be exactly 0)."""
    subs = {r[j]: r[0] for j in range(1, n - 1)}
    for j in range(1, n + 1):
        subs[a[j - 1]] = (-1) ** j * comb(n, j) * r[0] ** j
    return [sp.expand(g.subs(subs)) for g in eqs]


def enumerate_counterexamples(n, p, hasse=False):
    """Bounded oracle: all p^n monic degree-n polys over F_p.
    Returns (n_total, n_ca, counterexamples) via lib.casas_alvero
    (is_ca ordinary, or is_ca_hasse when hasse=True)."""
    x = sp.symbols("x")
    cex = []
    n_ca = 0
    n_total = 0
    for coeffs in product(range(p), repeat=n):
        expr = x ** n + sum(coeffs[i] * x ** (n - 1 - i) for i in range(n))
        n_total += 1
        hyp = is_ca_hasse(expr, p) if hasse else is_ca(expr, p)
        if hyp:
            n_ca += 1
            if not is_pure_power(expr, p):
                cex.append(expr)
    return n_total, n_ca, cex


def main():
    only_n = [int(s) for s in sys.argv[1:] if s.isdigit()] or [3, 4]
    lines = []
    ok_all = True

    guards = run_entry_guards()
    guards_ok = all(c for _, c in guards)
    ok_all &= guards_ok
    lines.append("== Entry guards (lib.casas_alvero, exact) ==")
    for label, c in guards:
        lines.append(f"    [{'PASS' if c else 'FAIL'}] {label}")
    lines.append(f"    => guards {'PASSED' if guards_ok else 'FAILED'}")
    lines.append("")

    computed = {}
    for n in only_n:
        a = sp.symbols("a_1:%d" % (n + 1))
        r = sp.symbols("r_1:%d" % n)
        eqs = hasse_sn_equations(n, a, r)   # published (Hasse) formulation
        eqs_ord = sn_equations(n, a, r)      # ordinary: contrast only
        bad = set()
        bad_ord = set()
        lines.append(f"== n = {n}: Hasse-CA_{{n,p}} over GF(p), all primes "
                     f"p < 60 (published formulation) ==")
        for p in PRIMES_BELOW_60:
            t0 = time.monotonic()
            d1 = direction1(n, a, r, eqs, p)
            d2_ok = all(v == 0 for v in direction2(n, a, r, eqs))
            d1_ok = all(ok for _, ok, _ in d1)
            holds = d1_ok and d2_ok
            dt = time.monotonic() - t0
            if not holds:
                bad.add(p)
            # contrast: ordinary scheme (only informative, not asserted)
            d1o = direction1(n, a, r, eqs_ord, p)
            if not all(ok for _, ok, _ in d1o):
                bad_ord.add(p)
            flags = " ".join("Y" if ok else "N" for _, ok, _ in d1)
            lines.append(
                f"    p={p:2d}: dir1(P⊆rad(I))=[{flags}] "
                f"dir2(I⊆rad(P))={'Y' if d2_ok else 'N'}  "
                f"{'CA HOLDS' if holds else 'CA FAILS (bad)'}  [{dt:7.2f}s]")
            print(f"n={n} p={p}: {'CA HOLDS' if holds else 'CA FAILS (bad)'} "
                  f"({dt:.2f}s)", flush=True)
        ok_all &= (bad == EXPECTED_BAD[n])
        computed[n] = bad
        lines.append(f"    => bad primes computed for n={n}: {sorted(bad)}")
        lines.append(f"    => ordinary-derivative scheme for n={n}: "
                     f"{sorted(bad_ord)}  (contrast only; NOT the published "
                     f"list -- differs when p < n because f^(i) vanishes "
                     f"identically for i >= p)")
        lines.append(f"    => published list for n={n}:   {sorted(EXPECTED_BAD[n])}")
        lines.append(f"    => match: {'YES' if bad == EXPECTED_BAD[n] else 'NO'}")
        lines.append("")

    lines.append("== Second route (bounded oracle): enumerate monic polys over "
                 "F_p, p in {2,3,5,7} (<= 2401 polys), HASSE hypothesis ==")
    for n in only_n:
        for p in (2, 3, 5, 7):
            t0 = time.monotonic()
            n_total, n_ca, cex = enumerate_counterexamples(n, p, hasse=True)
            dt = time.monotonic() - t0
            expected_bad = p in EXPECTED_BAD[n]
            found_cex = len(cex) > 0
            match = (found_cex == expected_bad)
            ok_all &= match
            lines.append(
                f"    n={n} p={p}: {n_total} polys, {n_ca} satisfy hypothesis, "
                f"{len(cex)} counterexamples -> "
                f"{'matches' if match else 'MISMATCH'} "
                f"(published: {'bad' if expected_bad else 'good'})  [{dt:5.2f}s]")
            if cex:
                lines.append(f"        witness: {cex[0]}")
    lines.append("")

    lines.append("== VERDICT ==")
    lines.append(f"    bad primes computed  n=3: {sorted(computed.get(3, set()))}"
                 f"  (published {{2}})")
    lines.append(f"    bad primes computed  n=4: {sorted(computed.get(4, set()))}"
                 f"  (published {{3,5,7}})")
    lines.append(f"    ALL CHECKS {'PASSED' if ok_all else 'FAILED'}")

    header = [
        "PROGRAM: code/badprimes/verify_badprimes_sn.py",
        "ROUTE: S_n-scheme radical equality over GF(p), HASSE formulation "
        "(published bad-prime lists) -- direction1: P_n subset rad(I_n) via "
        "Rabinowitsch (sympy groebner, modulus=p); direction2: I_n vanishes on "
        "the pure-power locus (exact substitution); plus bounded F_p "
        "enumeration through lib.casas_alvero.is_ca_hasse as an independent "
        "second route.  Ordinary-derivative scheme reported as contrast.",
        "RANGE: n in {3,4}; all 17 primes p < 60; enumeration p in {2,3,5,7}",
    ]
    text = "\n".join(header + [""] + lines) + "\n"
    with open(CAPTURE, "w") as fh:
        fh.write(text)
    print(text)
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
