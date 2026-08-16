"""Independent computational verification of the char-p break table for
x^{p+1} - x^p, the live question of the adopted root-difference-coloring
approach (directive 10: the identity is char-free, the break is downstream in
the coloring collapse step).

The proof note research/notes/root-difference-identity-verified.md asserts by
hand via Lucas's theorem that for f = x^{p+1} - x^p over F_p the Hasse
derivatives are exactly

    H_1(f) = x^p              (nontrivial; witnessed by root 0)
    H_i(f) = 0  for 2 <= i <= p-1   (vacuously witnessed: gcd(f,0)=f)
    H_p(f) = x - 1            (nontrivial; witnessed by root 1)

so the witness carries a consistent 2-root coloring (root 0 witnesses i=1..p-1,
root 1 witnesses i=p) and nothing forces 0 = 1 — the char-0 collapse/convex-hull
step has no F_p analogue. This script checks that table exactly over GF(p) for
p=2,3,5,7,11,13, with every CA-hypothesis decision routed through the canonical
oracle lib.casas_alvero.is_ca_hasse / is_pure_power.

Failure criterion (what would falsify the named break): a nontrivial H_i at an
index where the proof says H_i == 0, or a root failing to witness a derivative
the proof says it witnesses.
"""
import sys
from math import comb
import sympy as sp
from sympy import Poly, GF

from lib.casas_alvero import is_ca_hasse, is_pure_power, charp_witness

x = sp.symbols("x")

PASS, FAIL = [], []


def rec(label, ok, detail=""):
    (PASS if ok else FAIL).append(f"[{'PASS' if ok else 'FAIL'}] {label}"
                                  + (f"  ({detail})" if detail else ""))


for p in (2, 3, 5, 7, 11, 13):
    n = p + 1
    fp = charp_witness(p)
    coeffs = [fp.coeff_monomial(x ** j) for j in range(n + 1)]
    Hi = {}
    for i in range(1, n):
        Hi[i] = Poly(sum(comb(j, i) * coeffs[j] * x ** (j - i)
                         for j in range(i, n + 1)), x, domain=GF(p))

    # (a) degeneracy profile: which indices have H_i == 0?
    zero_idx = sorted(i for i in range(1, n) if Hi[i] == Poly(0, x, domain=GF(p)))
    expect_zero = list(range(2, p))  # 2 .. p-1
    rec(f"p={p}: H_i == 0 exactly for i in 2..p-1 = {expect_zero}",
        zero_idx == expect_zero, f"got {zero_idx}")

    # (b) H_1 == x^p, H_p == x-1 (the two nontrivial/non-vacuous witnesses)
    rec(f"p={p}: H_1 == x^p", Hi[1] == Poly(x ** p, x, domain=GF(p)),
        f"got {Hi[1].as_expr()}")
    rec(f"p={p}: H_p == x-1", Hi[p] == Poly(x - 1, x, domain=GF(p)),
        f"got {Hi[p].as_expr()}")

    # (c) NONTRIVIAL root witnesses. A nontrivial H_i (not identically zero)
    # is witnessed by a root b with H_i(b)=0. The degenerate H_i == 0 are
    # vacuous (every point a witness) so they carry no root information.
    # The proof asserts: root 0 nontrivially witnesses i=1 (H_1=x^p has root 0)
    # and root 1 nontrivially witnesses i=p (H_p=x-1 has root 1).
    def nontriv_witnesses(b):
        return [i for i in range(1, n)
                if Hi[i] != Poly(0, x, domain=GF(p)) and Hi[i].eval(b) == 0]
    ntw0 = nontriv_witnesses(0)
    ntw1 = nontriv_witnesses(1)
    rec(f"p={p}: root 0 nontrivially witnesses exactly i=1", ntw0 == [1],
        f"got {ntw0}  (H_1=x^{p} has root 0)")
    rec(f"p={p}: root 1 nontrivially witnesses exactly i=p", ntw1 == [p],
        f"got {ntw1}  (H_p=x-1 has root 1)")

    # (d) every derivative shares a root (f is Hasse-CA) but not a pure power
    ca = is_ca_hasse(fp, p)
    pp = is_pure_power(fp, p)
    rec(f"p={p}: witness is Hasse-CA and NOT pure power (canonical oracle)",
        ca and not pp, f"is_ca_hasse={ca}, is_pure_power={pp}")

    # (e) the two actual roots {0,1} admit a valid coloring and neither alone
    #     suffices. Degenerate H_i == 0 are vacuous (witnessed by every point),
    #     so they cannot be evidence for "a root". "Root b witnesses i" means
    #     H_i has b as a root and H_i is NONZERO (nontrivial sharing); a purely
    #     vacuous H_i == 0 would make every point a witness and trivialize.
    def nontriv_roots(i):
        # roots of H_i that genuinely witness i (nontrivial polys only)
        if Hi[i] == Poly(0, x, domain=GF(p)):
            return "vacuous"
        return [b for b in (0, 1) if Hi[i].eval(b) == 0]

    # root 0 nontrivially witnesses every i=1..p-1 (H_1=x^p and the rest are
    # vacuous or zero at 0); root 1 nontrivially witnesses i=p via H_p=x-1.
    r0 = [i for i in range(1, n) if (Hi[i] == Poly(0, x, domain=GF(p)))
          or (Hi[i].eval(0) == 0 and Hi[i] != Poly(0, x, domain=GF(p)))]
    r1 = [i for i in range(1, n) if (Hi[i] == Poly(0, x, domain=GF(p)))
          or (Hi[i].eval(1) == 0 and Hi[i] != Poly(0, x, domain=GF(p)))]
    # the 2-coloring: root 0 handles 1..p-1, root 1 handles p; every i is
    # covered, and neither root alone covers all i.
    r0_covers = set(range(1, p)) <= set(r0)
    r1_covers_p = p in r1
    root0_alone = set(range(1, n)) <= set(r0)
    root1_alone = set(range(1, n)) <= set(r1)
    coloring_ok = r0_covers and r1_covers_p and not root0_alone and not root1_alone
    rec(f"p={p}: 2-root coloring {0,1} covers all i, neither root alone suffices",
        coloring_ok,
        f"r0 covers 1..{p-1}={r0_covers}, r1 covers p={r1_covers_p}, "
        f"r0-alone={root0_alone}, r1-alone={root1_alone}")

header = [
    "CHAR-P BREAK TABLE, x^{p+1}-x^p (live question after directive 10)",
    "oracle: lib.casas_alvero.is_ca_hasse / is_pure_power (all hypothesis decisions)",
    "range: p=2,3,5,7,11,13 (n=p+1); exact over GF(p)",
]
body = header + [""] + PASS + FAIL + [""]
body.append("ALL CHECKS %s (%d passed, %d failed)"
            % ("PASSED" if not FAIL else "FAILED", len(PASS), len(FAIL)))
text = "\n".join(body)
print(text)
sys.exit(0 if not FAIL else 1)
