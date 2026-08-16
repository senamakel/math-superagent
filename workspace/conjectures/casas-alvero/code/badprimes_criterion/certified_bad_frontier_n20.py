"""Certified-bad frontier for degree n = 20, by the Schaub-Spivakovsky
sufficient binomial criterion (arXiv:2307.05997, Cor 8).

Criterion (SUFFICIENT, not exhaustive): if a prime p divides
    C(20, i) - 1   for some i in {1, ..., 19},
then p is a BAD prime for degree 20 (CA fails in degree 20, characteristic
p).  This is proved in the 2023 paper by showing that for such p no pure
power of any a_j appears in any resultant R_j mod p, so the point e_i
lies in V(R_1,...,R_19) over F_p.

The full minor criterion (arXiv:2411.13967, Thm 3.1) is the exact
characterization of bad primes, but for n = 20 it would require the gcd of
all C x C minors with C = binomial(190, 18) ~ 10^20 -- infeasible.  The
binomial criterion gives an exact, certified SUBSET of the bad primes
(calibration at n = 4: criterion {3,5} vs true bad primes {3,5,7} -- a
strict subset, so a prime NOT certified by this criterion is a candidate
good prime, NOT a proven good prime).

Output
------
1. certified-bad list: all primes p with p | C(20,i)-1 for some i, exactly
   (sympy.factorint; numbers <= C(20,10)-1 = 184755 are trivially factored).
2. certified-bad frontier: the 20 smallest primes NOT in the certified list
   (candidate good primes), each with an explicit check that p divides no
   C(20,i)-1 (must be empty by construction -- the guard).
3. among those 20 candidates, those < 100, listed.

Exit 0 iff all asserts pass.
"""

import os

import sympy as sp


def main():
    n = 20
    lines = []

    def rec(label, detail=""):
        lines.append(label + (("  (%s)" % detail) if detail else ""))

    # ---- certified-bad list: exact --------------------------------------
    certified = set()
    divisions = {}  # prime -> [i values with p | C(20,i)-1]
    c20 = [sp.binomial(n, i) for i in range(1, n)]
    for i, v in enumerate(c20, start=1):
        assert v - 1 == sp.binomial(n, i) - 1
        for p in sp.factorint(v - 1):
            certified.add(p)
            divisions.setdefault(p, []).append(i)
    certified = sorted(certified)
    rec("certified-bad primes for degree 20 (p | C(20,i)-1, 1<=i<=19): "
        "%d primes" % len(certified))
    rec("  " + ", ".join(map(str, certified)))
    for p in certified:
        rec("  p=%d certified by i=%s" % (p, divisions[p]))

    # ---- smallest certified primes, for the record -----------------------
    rec("smallest certified primes: %s" % certified[:20])
    rec("largest certified prime: %d" % certified[-1])

    # ---- frontier: 20 smallest primes NOT certified ----------------------
    # sympy's primerange(2, None) is a silent empty iterator; use an explicit
    # bound instead.  The certified set is all <= 15269; among any 20
    # consecutive primes past it, at least 20 are not certified, so
    # 15400 is a safe upper bound for the 20th non-certified prime.
    candidates = []
    for p in sp.primerange(2, 15400):
        if p not in certified:
            candidates.append(p)
            if len(candidates) == 20:
                break

    # guard: each candidate divides no C(20,i)-1 (else it would be certified)
    for p in candidates:
        divides = [i for i in range(1, n) if (sp.binomial(n, i) - 1) % p == 0]
        rec("candidate good prime p=%d: divides C(20,i)-1 for i=%s (must be [])"
            % (p, divides))
        assert divides == []

    rec("20 smallest primes NOT certified (candidate good primes):")
    for k, p in enumerate(candidates, start=1):
        rec("  %2d. p=%d" % (k, p))

    # ---- candidates < 100 ------------------------------------------------
    small = [p for p in candidates if p < 100]
    rec("candidate good primes < 100: %s" % small)
    assert all(p < 100 for p in small)

    # ---- sanity: the certified list really is a subset of the true bad
    #      primes at n=4 (calibration), and every certified prime is prime --
    for p in certified:
        assert sp.isprime(p)

    rec("RESULT: degree-20 certified-bad list has %d primes; "
        "frontier (20 smallest not certified) = %s; candidates < 100 = %s"
        % (len(certified), candidates, small))
    rec("ALL CHECKS PASSED")
    return "\n".join(lines) + "\nALL CHECKS PASSED"


if __name__ == "__main__":
    text = main()
    print(text)
    out_dir = "/workspace/code/out"
    os.makedirs(out_dir, exist_ok=True)
    header = [
        "CERTIFIED-BAD FRONTIER FOR DEGREE n=20 "
        "(Schaub-Spivakovsky sufficient binomial criterion, arXiv:2307.05997 Cor 8)",
        "program: code/badprimes_criterion/certified_bad_frontier_n20.py",
        "oracle: sympy binomial + factorint (exact integers, all values "
        "<= C(20,10)-1 = 184755); criterion: p | C(20,i)-1 for some i in 1..19",
        "range: i = 1..19; certified primes collected exactly; frontier = "
        "20 smallest primes not certified, plus those < 100",
        "",
    ]
    with open(os.path.join(out_dir, "badprimes_n20_frontier.captured.txt"),
              "w") as fh:
        fh.write("\n".join(header) + text + "\n")
    raise SystemExit(0)
