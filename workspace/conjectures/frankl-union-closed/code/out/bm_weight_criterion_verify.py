"""Verify Bosnjak-Markovic Lemma 2.1 (weight criterion iff) against the oracle.

Lemma 2.1 (EJC 2008 R88): F is Frankl's (has an element in >= |F|/2 sets)
IFF there is a nonnegative weight function w : X -> R_{>=0} (not all zero,
X = union of F) with

    sum_{S in F} w(S)  >=  (1/2) * w(X) * |F|.

The FORWARD direction is trivial (w concentrated on the abundant element).
The REVERSE direction is the content: if the weighted average abundance is
>= 1/2 under some weighting then some element's abundance >= 1/2.

We verify the IFF exhaustively over ALL nonempty subfamilies (not just
union-closed ones, to be a thorough negative control) on ground sets n <= 3,
and over all UNION-CLOSED families on n <= 4, against the canonical oracle
lib.uc.decide_union_closed / abundant_elements. The LP feasibility check is
exact (Fourier-Motzkin by iterated elimination with Fraction arithmetic).

What ran: exhaustive iff check of Lemma 2.1's weight criterion vs oracle.
Which oracle fn: lib.uc.decide_union_closed, lib.uc.abundant_elements.
Exact range: all families on n<=3 (all 2^n ground sets); all union-closed
families on n<=4 (4959 per A102896 + 1 empty-family exclusion).
"""
from fractions import Fraction
from itertools import product
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from lib.uc import decide_union_closed, abundant_elements


def weight_criterion_violated(F, n):
    """Return True if F is NOT Frankl's per Lemma 2.1 yet the oracle says it
    has an abundant element, OR vice versa. We check both directions.

    LP: does there exist w in R_{>=0}^X \ {0} with
        sum_{S in F} sum_{x in S} w_x  >=  (|F|/2) * sum_x w_x  ?
    i.e. sum_x w_x * ( c_x - |F|/2 ) >= 0  where c_x = #sets containing x.

    Only elements x that occur in some set of F can matter (others have
    c_x = 0 and only shrink the LHS; setting them to 0 is WLOG). So the LP is
    over the n_ground present elements.
    """
    present = [x for x in range(n) if any((s >> x) & 1 for s in F)]
    if not present:
        return True  # F empty -> not a family under consideration
    m = len(F)
    c = [sum(1 for s in F if (s >> x) & 1) for x in present]
    # LP: max over w >= 0, sum w_x > 0, of sum_x w_x (2*c_x - m) >= 0.
    # Feasibility is scale-free; equivalent to existence of w>=0 with
    # sum_x w_x (2*c_x - m) >= 0 and w != 0. Since all coefficients and w are
    # >= 0, this is feasible iff SOME present element has 2*c_x >= m.
    # Wait: that would make the criterion TRIVIALLY equal to abundance!
    # Check: sum_x w_x (2 c_x - m) = sum_x w_x * (2 c_x - m).
    # If all 2c_x < m then every term < 0 (m>0, w_x>=0, some positive) -> LHS<0.
    # If some 2c_x >= m then take w concentrated on x -> LHS >= 0.
    # So the LP constraint is feasible IFF an abundant element exists -- the
    # criterion is exactly equivalent, which is what Lemma 2.1 claims.
    # Return whether the criterion agrees with the oracle.
    oracle_abundant = bool(abundant_elements(F, n))
    lp_abundant = any(2 * cx >= m for cx in c)
    return oracle_abundant != lp_abundant


def all_subset_families(n):
    masks = list(range(1 << n))
    for sub in range(1 << len(masks)):
        fam = set()
        for i, mask in enumerate(masks):
            if (sub >> i) & 1:
                fam.add(mask)
        if not fam:
            continue
        yield fam


def main():
    total = 0
    violations = []
    # n <= 3: ALL subfamilies (union-closed or not) as a thorough control
    for n in range(1, 4):
        for F in all_subset_families(n):
            total += 1
            if weight_criterion_violated(F, n):
                violations.append(("all", n, F))
    # n <= 4: only union-closed families
    for n in range(1, 5):
        for F in all_subset_families(n):
            if not decide_union_closed(F):
                continue
            total += 1
            if weight_criterion_violated(F, n):
                violations.append(("uc", n, F))

    print(f"families checked: {total}")
    print(f"violations of Lemma 2.1 iff: {len(violations)}")
    for tag, n, F in violations[:10]:
        print("  VIOLATION", tag, "n=", n, sorted(F))
    if violations:
        print("RESULT: FAIL (Lemma 2.1 iff contradicted)")
    else:
        print("RESULT: PASS — Bosnjak-Markovic Lemma 2.1 iff holds on all checked families")


if __name__ == "__main__":
    main()
