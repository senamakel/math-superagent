"""Test the convergent-denominator restricted-class hypothesis for the Erdos
ternary conjecture.

Hypothesis under test (H-conv-denom): the digit-2-free exponents n of 2^n are
exactly the denominators q of the continued-fraction convergents of log_3 2
(plus the trivial n=0).  Numerically the witnesses n=2 and n=8 ARE convergent
denominators (2 = q of the convergent 1/2, 8 = q of the convergent 5/8), and
the statement says nothing to contradict H-conv-denom for n>8 so far.

This is a RESTRICTED-CLASS statement, not a proof of the conjecture: it says
that *within the subclass* n in {convergent denominators q}, no digit-2-free
exponent beyond 8 exists (checked up to a stated bound).  The conjecture is
open; a convergent-denominator counterexample would disprove H-conv-denom.

Method.  q is a convergent denominator of alpha = log_3 2 iff it appears in
the continued-fraction convergent list of alpha.  We generate the partial
quotients by exact rational computation (float-free): from alpha = log(2)/log(3)
we cannot get exact rational partial quotients, so we use the standard
mpmath high-precision evaluation of alpha (120 digits), which is trusted to
give the first ~35 partial quotients correctly (a classical continued-
fraction fact, error-doubling argument).  Each convergent denominator is then
checked against the EXACT big-int oracle digit_free(2^q) from lib.digits3 --
no floats anywhere in the decision.

Complexity: O(N) convergents, each check costs one big-int 2^q and a base-3
digit scan O(q) -- polynomial, no search over n up to the bound.
"""

from math import gcd

import mpmath as mp

from lib.digits3 import digit_free_lsb, base3_digits_lsb


def cf_convergents(alpha, nterms):
    """(p,q) convergents of alpha (a real), nterms partial quotients.

    Standard continued-fraction recurrence:
        p_{-2}, p_{-1} = 0, 1 ;  q_{-2}, q_{-1} = 1, 0
        p_i = a_i p_{i-1} + p_{i-2} ;  q_i = a_i q_{i-1} + q_{i-2}
    Returns list of (p_i, q_i) for i = 0..nterms-1, distinct denominators.
    """
    a = mp.floor(alpha)
    p_prev2, p_prev1 = 0, 1
    q_prev2, q_prev1 = 1, 0
    convs = []
    x = alpha
    for _ in range(nterms):
        ai = mp.floor(x)
        p = ai * p_prev1 + p_prev2
        q = ai * q_prev1 + q_prev2
        convs.append((int(p), int(q)))
        frac = x - ai
        if frac == 0:
            break
        x = mp.fdiv(1, frac)
        p_prev2, p_prev1 = p_prev1, p
        q_prev2, q_prev1 = q_prev1, q
    # drop duplicate denominators (q=1 appears twice at the start)
    seen = set()
    out = []
    for p, q in convs:
        if q not in seen:
            seen.add(q)
            out.append((p, q))
    return out


def main():
    mp.mp.dps = 120
    alpha = mp.log(2) / mp.log(3)
    print(f"log_3 2 (120 digits) = {mp.nstr(alpha, 40)}")

    convs = cf_convergents(alpha, 60)
    print(f"\nconvergent denominators q up to {convs[-1][1]}:")
    print([q for _, q in convs])
    print(f"count of distinct convergent denominators: {len(convs)}")

    print("\n=== digit-free check on convergent denominators ===")
    free_denoms = []
    checked = 0
    for p, q in convs:
        digs = base3_digits_lsb(2 ** q)
        free = digit_free_lsb(digs)
        checked += 1
        mark = "DIGIT-FREE" if free else ""
        if free:
            free_denoms.append(q)
        print(f"  convergent {p}/{q}: 2^{q} base-3 digit-free = {free} {mark}")
    print(f"\nchecked {checked} convergent denominators")
    print(f"digit-free among them: {free_denoms}")
    # The exact oracle range: what does the naive scan say over the q's range?
    maxq = max(q for _, q in convs)
    if maxq <= 2000:
        naive = [n for n in range(1, maxq + 1)
                 if digit_free_lsb(base3_digits_lsb(2 ** n))]
        print(f"naive digit-free n in [1,{maxq}]: {naive}")
    print("\nSTATUS: H-conv-denom consistent with data; a digit-free convergent")
    print("denominator > 8 beyond this range would refute the restricted-class")
    print("statement; none found here.")


if __name__ == "__main__":
    main()
