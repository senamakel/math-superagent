"""INDEPENDENT ROUTE: semantic bad-prime check for degree n=5 on small primes.

The bad-prime-minors criterion (arXiv:2411.13967 Thm 3.1) says p is bad for
degree 5 iff rank_{F_p}(M_T) < 120 for some tuple T. That is a *criterion*;
this program checks the *semantics* it stands for: p is bad iff a monic
degree-5 polynomial f over F_p satisfies the Hasse-derivative CA hypothesis
(gcd(f, H_i(f)) != 1 for i = 1..4) and is not a pure power — i.e. iff a
genuine counterexample exists over F_p. This is exactly the definition of
"bad prime" (Castryck-Laterveer-Ounaies 2012, Def 1).

Method: enumerate ALL p^5 monic degree-5 polynomials over F_p and decide
each one with the canonical oracle lib.casas_alvero.is_ca_hasse /
is_pure_power (exact arithmetic over GF(p), no floating point). p is bad
iff the count of counterexamples is > 0.

Feasible only for small p (space p^5): p in {2,3,5,7,11,13} =
32+243+3125+16807+161051+371293 = 552551 polynomials total. This covers the
published bad primes 2,3,7,11 and the good primes 5,13 (which the rank route
certified GOOD). The large bad primes 131,193,599,3541,8009 are out of reach
for enumeration (e.g. 131^5 ~ 3.9e10) — exactly why the minors criterion
exists; they are covered by the rank route only.

Agreement asserted: for each p in the set, (counterexample exists) ==
(p in {2,3,7,11}). Also reports the count of counterexamples and a sample
witness for each bad p.

Exit 0 iff every assert passes.
"""

from __future__ import annotations

import os
import time
from concurrent.futures import ProcessPoolExecutor
from itertools import product

from sympy import Poly, GF, symbols

from lib.casas_alvero import is_ca_hasse, is_pure_power

N = 5
PRIMES = [2, 3, 5, 7, 11, 13]
PUBLISHED_BAD = {2, 3, 7, 11}
WORKERS = 28
x = symbols("x")


def _check_chunk(chunk):
    """chunk: list of (p, coeff tuple (c4,c3,c2,c1,c0)) -> (p, coeffs, ce)
    where ce is True iff f = x^5 + c4 x^4 + ... + c0 is a counterexample
    (is_ca_hasse and not is_pure_power) over GF(p)."""
    out = []
    for p, coeffs in chunk:
        f = Poly(x ** N + sum(c * x ** (N - 1 - k)
                              for k, c in enumerate(coeffs)),
                 x, domain=GF(p))
        ce = is_ca_hasse(f, p) and not is_pure_power(f, p)
        out.append((p, coeffs, ce))
    return out


def main():
    lines = []

    def rec(label):
        lines.append(label)

    # ---- build the full search space -------------------------------------
    all_polys = []  # (p, coeffs)
    for p in PRIMES:
        all_polys.extend((p, c) for c in product(range(p), repeat=N))
    rec("search space: %d monic degree-5 polynomials over F_p, "
        "p in %s (p^5 each: %s)"
        % (len(all_polys), PRIMES,
           {p: p ** N for p in PRIMES}))
    rec("worker count: %d" % WORKERS)

    chunks = [all_polys[i::WORKERS] for i in range(WORKERS)]
    chunks = [c for c in chunks if c]

    t0 = time.time()
    results = []
    with ProcessPoolExecutor(max_workers=len(chunks)) as ex:
        for r in ex.map(_check_chunk, chunks):
            results.extend(r)
    wall = time.time() - t0
    assert len(results) == len(all_polys)
    rec("wall time over %d workers: %.1f s" % (len(chunks), wall))

    # ---- aggregate ---------------------------------------------------------
    counts = {p: 0 for p in PRIMES}
    witnesses = {}
    for p, coeffs, ce in results:
        if ce:
            counts[p] += 1
            witnesses.setdefault(p, coeffs)

    rec("")
    rec("counterexample counts (Hasse-CA degree-5 polys over F_p, "
        "not pure powers):")
    for p in PRIMES:
        rec("  p=%2d : %6d counterexamples  bad=%s"
            % (p, counts[p], p in PUBLISHED_BAD))
    rec("")
    for p in sorted(witnesses):
        c = witnesses[p]
        rec("  witness over F_%d: f = x^5 %s"
            % (p, " + ".join("%d x^%d" % (c[k], N - 1 - k)
                             for k in range(N) if c[k]) or "(monomial x^5)"))

    # ---- assertions: semantics == published list on these primes -----------
    for p in PRIMES:
        ce_exists = counts[p] > 0
        assert ce_exists == (p in PUBLISHED_BAD), (
            "p=%d: counterexamples=%d but published bad=%s"
            % (p, counts[p], p in PUBLISHED_BAD))
    rec("")
    rec("agreement: (counterexample over F_p exists) == (p in {%s}) "
        "for every p in %s" % (", ".join(map(str, sorted(PUBLISHED_BAD))),
                               PRIMES))
    rec("RESULT: semantic route (literal definition via canonical oracle) "
        "agrees with the published bad-prime list on all small primes; "
        "matches the rank-over-F_p criterion route "
        "(code/out/badprimes_n5.captured.txt) on 2,3,7,11 bad and 5,13 good.")
    rec("ALL CHECKS PASSED")
    return "\n".join(lines)


if __name__ == "__main__":
    text = main()
    print(text)
    out_dir = "/workspace/code/out"
    os.makedirs(out_dir, exist_ok=True)
    header = [
        "DEGREE n=5 BAD PRIMES, INDEPENDENT SEMANTIC ROUTE "
        "(literal definition, canonical oracle)",
        "program: code/badprimes_criterion/semantic_n5_smallprimes.py",
        "oracle: lib.casas_alvero.is_ca_hasse / is_pure_power (exact over "
        "GF(p), no floating point); counterexample = is_ca_hasse and not "
        "is_pure_power",
        "base ring: GF(p), p in {2,3,5,7,11,13}; term order: not used "
        "(oracle decisions, no Groebner basis)",
        "ground truth: Castryck-Laterveer-Ounaies 2012 Thm 4 (bad primes of "
        "degree 5 = {2,3,7,11,131,193,599,3541,8009}); this route covers the "
        "small primes by exhaustive enumeration of all p^5 monic degree-5 "
        "polynomials",
        "scope: 552551 polynomials total; large bad primes (>=131) are out of "
        "enumeration reach (131^5 ~ 3.9e10) and covered only by the rank "
        "route; agreement asserted on all six primes in scope",
        "",
    ]
    with open(os.path.join(out_dir,
                           "badprimes_n5_semantic.captured.txt"), "w") as fh:
        fh.write("\n".join(header) + text + "\n")
    raise SystemExit(0)
