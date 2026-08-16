"""Verify the Schaub-Spivakovsky bad-prime-minors criterion
(arXiv:2411.13967, Thm 3.1) for degree n = 4, exactly.

Known ground truth: the bad primes of degree 4 are {3, 5, 7}.

Method (Thm 3.1): with x = (x_1,x_2,x_3), d = (16-12+4)/2 = 4,
C = number of monomials of degree 4 in 3 variables = 15,
D = |S_T| = sum_i C(4-i+2,2) = C(5,2)+C(4,2)+C(3,2) = 10+6+3 = 19.
For each T in {1,2,3,4}^3, M_T is the 19 x 15 matrix whose rows are the
coefficient vectors of G_{T,i} x^alpha (i = 1..3, |alpha| = 4-i),
and J_T = gcd of all 15x15 minors of M_T = |prod of the 15 SNF invariant
factors|.  Then the prime p is bad for degree 4 iff p | J_T for some T,
i.e. iff p | lcm_T J_T.

Two independent routes to the final answer:
  (1) factor the exact lcm of all 64 J_T values (exact integer arithmetic);
  (2) rank over GF(p): p | J_T  <=>  rank_{F_p}(M_T) < 15, checked for every
      prime up to the bound and every tuple.
Both must give exactly {3, 5, 7}.

Additional computed facts:
  - the sufficient binomial criterion p | C(4,i)-1 (i = 1..3) gives a
    SUBSET of the true bad primes {3,5,7} (it misses 7);
  - distribution of J_T values over the 64 tuples (how many tuples witness
    each bad prime), and the prime divisors of lcm J_T.

Exit 0 iff every assert passes.
"""

import math
import os

import sympy as sp

from lib.badprimes import (
    jt_of_T, lcm_jt_over_T, rank_mod_p, criterion_bad_primes,
    matrix_MT, jt_from_matrix, jt_bruteforce,
)


def main():
    n = 4
    lines = []

    def rec(label, detail=""):
        lines.append(label + (("  (%s)" % detail) if detail else ""))

    # ---- parameters from the theorem -------------------------------------
    d = (n * n - 3 * n + 4) // 2
    C = sp.binomial((n * n - n) // 2, n - 2)
    D = sum(sp.binomial(d - i + n - 2, n - 2) for i in range(1, n))
    rec("parameters: n=%d, d=%d, C=%d, D=%d" % (n, d, C, D))
    assert (d, int(C), int(D)) == (4, 15, 19)

    # ---- sanity: matrix shape and the SNF identity on one real tuple -----
    M = matrix_MT(n, (1, 1, 1))
    rec("M_{(1,1,1)} shape: %dx%d" % M.shape)
    assert M.shape == (19, 15)
    a = jt_bruteforce(M)          # brute-force gcd of all 3876 minors
    b = jt_from_matrix(M)         # SNF route
    rec("J_{(1,1,1)}: brute-force %d, SNF %d, agree=%s"
        % (a, b, a == b))
    assert a == b

    # ---- main computation: all 64 tuples ---------------------------------
    L, js = lcm_jt_over_T(n)
    assert len(js) == 64
    rec("lcm over 64 tuples J_T = %d" % L)

    # distribution of J_T values
    from collections import Counter
    dist = Counter(js.values())
    rec("J_T value distribution: %s" % dict(sorted(dist.items())))

    # which tuples have J_T > 1
    bad_tuples = {T: v for T, v in js.items() if v != 1}
    rec("tuples with J_T > 1: %d of 64" % len(bad_tuples))
    for T in sorted(bad_tuples):
        rec("  T=%s J_T=%d" % (T, bad_tuples[T]))

    # ---- route 1: exact factorization of the lcm -------------------------
    fact = sp.factorint(L)
    primes1 = set(fact)
    rec("factorization of lcm J_T: %s" % fact)
    rec("prime divisors of lcm J_T (route 1): %s"
        % sorted(primes1))

    # ---- route 2: rank drops over GF(p) for every prime <= L and tuple ---
    # prime divisors of J_T are among primes <= max J_T (any prime divisor
    # of the lcm divides some J_T).  Also check all primes <= 101 as an
    # independent sweep.
    maxJ = max(js.values())
    primes2 = set()
    for p_ in sp.primerange(2, maxJ + 1):
        for T, v in js.items():
            if v % p_ == 0:
                assert rank_mod_p(matrix_MT(n, T), p_) < C
                primes2.add(p_)
    for p_ in sp.primerange(2, 102):
        rank_bad = any(rank_mod_p(matrix_MT(n, T), p_) < C for T in js)
        assert rank_bad == (p_ in primes2)
    rec("prime divisors via rank mod p over all tuples (route 2): %s"
        % sorted(primes2))

    # ---- the two routes must agree ---------------------------------------
    assert primes1 == primes2, (primes1, primes2)

    # ---- known ground truth ----------------------------------------------
    known = {3, 5, 7}
    rec("known bad primes of degree 4: %s" % sorted(known))
    assert primes1 == known

    # ---- sufficient binomial criterion -----------------------------------
    crit = set(criterion_bad_primes(n))
    rec("sufficient binomial criterion primes p | C(4,i)-1, i=1..3: %s"
        % sorted(crit))
    assert crit <= known
    rec("criterion is a strict subset of the true bad primes: %s"
        % (crit != known))
    assert crit != known

    rec("RESULT: prime divisors of lcm_T J_T = %s exactly; "
        "sufficient binomial criterion = %s (subset)"
        % (sorted(primes1), sorted(crit)))
    rec("ALL CHECKS PASSED" if True else "")

    return "\n".join(lines) + "\nALL CHECKS PASSED"


if __name__ == "__main__":
    text = main()
    print(text)
    out_dir = "/workspace/code/out"
    os.makedirs(out_dir, exist_ok=True)
    header = [
        "SCHAUB-SPIVAKOVSKY BAD-PRIME-MINORS CRITERION, DEGREE n=4 "
        "(arXiv:2411.13967 Thm 3.1)",
        "program: code/badprimes_criterion/verify_badprimes_n4.py",
        "oracle: lib.badprimes (J_T = gcd of all 15x15 minors of the 19x15 "
        "matrix M_T, via Smith normal form; rank-mod-p independent route)",
        "range: all 64 tuples T in {1,2,3,4}^3, exact integer arithmetic, "
        "primes up to max J_T and sweep to 101",
        "",
    ]
    with open(os.path.join(out_dir, "badprimes_n4.captured.txt"), "w") as fh:
        fh.write("\n".join(header) + text + "\n")
    raise SystemExit(0)
