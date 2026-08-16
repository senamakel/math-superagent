"""Small brute-force boundary checks for the bad-prime-minors criterion.

Verification of the *inputs* to Thm 3.1, not the theorem itself:
  1. The canonical CA oracle (lib.casas_alvero) reports the known char-p
     counterexamples correctly: for p in {2,3,5,7} the polynomial
     f = x^{p+1} - x^p over GF(p) satisfies the derivative-sharing
     hypothesis and is NOT a pure power, while (x-1)^n over QQ is a CA
     polynomial and a pure power.
  2. The char-p CA-polynomial family really gives counterexamples in
     degrees n that the criterion's G_{T,i} regular-sequence reformulation
     is about: x^{p+1}-x^p has degree p+1, so p is a bad prime for n = p+1.
     (Printed for the record; the exact classification of bad primes for
     n=4 is done by the minor criterion in verify_badprimes_n4.py.)
  3. A generic random integer matrix has gcd of minors = 1 (sanity control
     that J_T = 1 is the generic case and J_T > 1 is structurally special).

Exit 0 iff all checks pass.
"""

import random

import sympy as sp

from lib.casas_alvero import is_ca, is_pure_power, is_counterexample
from lib.badprimes import jt_from_matrix


def main():
    x = sp.symbols("x")
    ok = True
    lines = []

    def rec(label, passed, detail=""):
        nonlocal ok
        ok = ok and passed
        lines.append("[%s] %s%s" % ("PASS" if passed else "FAIL", label,
                                    ("  (%s)" % detail) if detail else ""))

    # --- Guard A: char-p witnesses (negative control of the oracle) -------
    lines.append("-- Guard A: oracle char-p witness x^{p+1}-x^p over GF(p), "
                 "p = 2,3,5,7")
    for p_ in (2, 3, 5, 7):
        f = sp.Poly(x ** (p_ + 1) - x ** p_, x, domain=sp.GF(p_))
        ca = is_ca(f, p_)
        pp = is_pure_power(f, p_)
        ce = is_counterexample(f, p_)
        rec("p=%d: is_ca=%s is_pure_power=%s counterexample=%s"
            % (p_, ca, pp, ce), ca and not pp and ce)

    # --- Guard B: pure powers over QQ (positive control of the oracle) ----
    lines.append("-- Guard B: (x-1)^n over QQ, n = 2..7")
    for n_ in range(2, 8):
        f = sp.Poly((x - 1) ** n_, x, domain=sp.QQ)
        ca = is_ca(f, 0)
        pp = is_pure_power(f, 0)
        rec("n=%d: is_ca=%s is_pure_power=%s" % (n_, ca, pp), ca and pp)

    # --- Guard C: generic random matrices have gcd of minors = 1 ----------
    lines.append("-- Guard C: random integer 19x15 matrices have J = 1 "
                 "(generic case; used for several seeds)")
    for seed in (1, 2, 3, 4, 5):
        random.seed(seed)
        M = sp.Matrix(19, 15, lambda i, j: random.randint(-5, 5))
        J = jt_from_matrix(M)
        rec("seed=%d: J=%d" % (seed, J), J == 1)

    lines.append("ALL GUARDS %s" % ("PASSED" if ok else "FAILED"))
    for line in lines:
        print(line)
    raise SystemExit(0 if ok else 1)


if __name__ == "__main__":
    main()
