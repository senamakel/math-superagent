#!/usr/bin/env python3
"""Standalone literal-rule check of the 3-Higgs definition, primes <= 1000.

This is the genuinely literal OEIS A057447 rule ("p is 3-Higgs iff p-1 divides
the CUBE of the product of all smaller 3-Higgs primes"), run from scratch:

    P = product of primes certified 3-Higgs so far (exact int);  P starts at 2
    (2 is the base).
    p is literal-Higgs  iff  (P**3) % (p - 1) == 0;  if so, P *= p.

Here the test that p-1 | P^3 runs over the ACTUAL running product P, exactly
as written — no factorisation of p-1, no per-prime exponent cap.  The base is
2 and 2 itself is never tested against P=2 (P^3=8 vs 1 always passes anyway).

Each p in increasing order:  (P**3) % (p-1) == 0  <=>  literal 3-Higgs.

Compared against lib.higgs.is_3_higgs(p) on the same primes.  A mismatch is
printed loudly and fails the program (exit 1).

Also asserts the two boundary facts:
    17 is NOT 3-Higgs (17-1 = 2^4, v2 = 4 > 3)
    31 IS 3-Higgs      (31-1 = 2*3*5)
and prints the 257 decision explicitly: 257-1 = 256 = 2^8, v2 = 8 > 3, so 257
is NOT 3-Higgs (hence 2^8+1's prime divisor 257 is a non-Higgs witness and
m = 8 is NOT in H_even).

Exact integers only.  No floats anywhere.  Complexity: one modular operation
per prime <= 1000, O(pi(1000) * log P) bit ops — linear in the bound.
"""
import sys

# ---------------------------------------------------------------------------
# literal generator and self-contained predicate, no imports beyond sympy
# ---------------------------------------------------------------------------
import sympy

PRIMES_1000 = list(sympy.primerange(2, 1000 + 1))

def literal_higgs_statuses(primes):
    """Return {p: bool} by the literal rule on `primes` (must be sorted,
    starting at 2), maintaining the running product P of certified primes."""
    statuses = {}
    P = 1
    for p in primes:
        if p == 2:
            statuses[p] = True          # base of the definition
            P *= p
            continue
        lit = (P ** 3) % (p - 1) == 0   # the literal divisibility, over ints
        statuses[p] = lit
        if lit:
            P *= p
    return statuses


def main():
    from lib.higgs import is_3_higgs

    print("=" * 78)
    print("Literal-rule 3-Higgs check (A2-style), primes <= 1000")
    print("=" * 78)
    print("definition: p literal-Higgs iff (P**3) % (p-1) == 0 with")
    print("  P = product of primes already certified by the same rule; base 2.")
    lit = literal_higgs_statuses(PRIMES_1000)

    # boundary facts first
    h17, h31, h257 = is_3_higgs(17), is_3_higgs(31), is_3_higgs(257)
    print("17 non-3-Higgs (17-1 = 2^4, v2 = 4 > 3): %s" % (not h17))
    print("31  3-Higgs    (31-1 = 2*3*5):           %s" % h31)
    print("257 decision: 257-1 = 256 = 2^8, v2 = 8 > 3 => is_3_higgs(257) = "
          "%s  (257 is NOT 3-Higgs, so m = 8 is NOT in H_even)" % h257)
    if h17 or not h31 or h257:
        print("*** BOUNDARY/257-EXPECTATION FAILURE ***")
        sys.exit(1)

    # agreement on all primes <= 1000
    mismatches = []
    for p in PRIMES_1000:
        want = lit[p]
        got = is_3_higgs(p)
        if want != got:
            mismatches.append((p, want, got))
            print("*** LITERAL-RULE MISMATCH at p=%d: literal=%s "
                  "is_3_higgs=%s ***" % (p, want, got))
    if not mismatches:
        print("literal rule and lib.higgs.is_3_higgs agree on ALL primes "
              "<= 1000: PASS")
    print("total primes <= 1000: %d; disagreements: %d"
          % (len(PRIMES_1000), len(mismatches)))
    print("literal-Higgs count <= 1000: %d; non-Higgs count <= 1000: %d"
          % (sum(lit.values()), len(PRIMES_1000) - sum(lit.values())))
    sys.exit(0 if not mismatches else 1)


if __name__ == "__main__":
    main()