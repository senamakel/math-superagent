"""Verify the 2-adic digit-position constraint family exactly and oracle-lean.

THEOREM under test (2-adic digit-position constraint family).  Write 2^n and
let A = { a : the position-a base-3 digit of 2^n is 1 } (LSB-first, so
2^n = sum_a a_digit*3^a).  For r >= 3 let ord = 2^(r-2) and define
N_c = #{ a in A : a ≡ c (mod ord) }.  The claimed congruence is

    sum_{c=0}^{ord-1} N_c * 3^c  ≡  2^n  (mod 2^r).          (*)

For n >= r this would say the LHS vanishes mod 2^r.

Why (*) must be treated with care

The sum over c is a *partition of the same sum* that defines 2^n restricted to
the digit-1 positions:

    sum_c N_c * 3^c  =  sum_{a in A} 3^a.

For a DIGIT-FREE n (all ternary digits in {0,1}) this equals 2^n exactly, so
(*) is exactly "2^n ≡ 2^n (mod 2^r)" — always true, a tautology.  For an n
whose expansion contains a digit 2, A omits those positions and
sum_{a in A} 3^a < 2^n, so (*) generally FAILS.  The task's claim that it
holds "for ALL n, not specific to counterexamples" is therefore false; it is a
genuine necessary condition on a counterexample (which is digit-free) but says
nothing else.  This program checks all of it and reports honestly.

Oracle-lean: the checks reconstruct digit positions from modular base-3 digits
(lib.digits3) rather than from the erdos oracle, so they cannot be polluted by
the very function under test.
"""

from lib.digits3 import base3_digits_lsb, digit_free_lsb


def order_of_3_mod_2r(r):
    """Multiplicative order of 3 modulo 2^r, by repeated squaring. r >= 3.

    The group (Z/2^r)^x for r>=3 is C_2 x C_{2^(r-2)}, so every element's
    order is a power of 2, 2^m with m <= r-2.  We square 3 repeatedly:
    3^(2^i) for i = 0,1,...,r-2.  The first i with 3^(2^i) ≡ 1 mod 2^r is the
    exponent m of the order, so order = 2^m.  This is O(r) modular squares
    (polynomial in r), never looping over the 2^(r-2) elements.
    """
    if r < 3:
        raise ValueError("r must be >= 3")
    mod = 2 ** r
    val = 3 % mod
    for i in range(0, r - 1):      # i = 0 .. r-2
        if val == 1:
            return 2 ** i
        val = val * val % mod
    # 3^(2^(r-1)) ≡ 1 mod 2^r must hold; if we exit without finding 1, order
    # is the top of the range.  (Exponent of the group is 2^(r-2).)
    return 2 ** (r - 1)


def residue_class_counts(positions, ord_):
    """N_c = #{ a in positions : a ≡ c mod ord_ }, c = 0..ord_-1."""
    n = [0] * ord_
    for a in positions:
        n[a % ord_] += 1
    return n


def verify_identity_for_n(n, r):
    """Return (lhs_mod, rhs_mod, is_digit_free, sum_over_A_exact, two_n).

    lhs = sum_{a in A} 3^a, which EQUALS sum_c N_c*3^c (the c-index is just a
    regrouped relabelling of position a by its residue mod ord).  rhs = 2^n.
    Both reduced mod 2^r; also returns the exact sum over A and 2^n.

    The batched direct sum is used (not the per-class loop over ord=2^(r-2)
    classes) because looping over ord classes is exponential in r; this is
    fine because the two forms are the identical reindexed sum.
    """
    two_n = 2 ** n
    digs = base3_digits_lsb(two_n)
    free = digit_free_lsb(digs)
    A = [a for a, d in enumerate(digs) if d == 1]
    lhs = sum(3 ** a for a in A)           # exactly sum_c N_c * 3^c
    lhs_mod = lhs % (2 ** r)
    rhs_mod = two_n % (2 ** r)
    sum_over_A = sum(3 ** a for a in A)
    return lhs_mod, rhs_mod, free, sum_over_A, two_n


def grouped_Nc_form(n, r):
    """Grouped form sum_c N_c*3^c mod 2^r, plus the direct sum mod 2^r.

    Only usable for small r (ord = 2^(r-2) materialisable).  Confirms the
    regrouping: N_c over c == direct sum over positions.  Returns
    (grouped_mod, direct_mod, agree).
    """
    two_n = 2 ** n
    digs = base3_digits_lsb(two_n)
    A = [a for a, d in enumerate(digs) if d == 1]
    ord_ = 2 ** (r - 2)
    N = residue_class_counts(A, ord_)
    grouped = sum(N[c] * (3 ** c) for c in range(ord_)) % (2 ** r)
    direct = sum(3 ** a for a in A) % (2 ** r)
    return grouped, direct, (grouped == direct)


def main():
    print("=== (4) order of 3 mod 2^r for r=3..40 ===")
    order_ok = True
    for r in range(3, 41):
        o = order_of_3_mod_2r(r)
        want = 2 ** (r - 2)
        ok = (o == want)
        order_ok &= ok
        print(f"r={r:3d}  order(3 mod 2^r)={o:>9d}  expected 2^(r-2)={want:<9d}  {'OK' if ok else 'FAIL'}")
    print(f"ORDER CLAIM ALL-PASS: {order_ok}\n")

    print("=== (3) grouped N_c form agrees with direct sum (small r only) ===")
    agree_all = True
    for n in range(0, 61):
        for r in range(3, 17):     # ord <= 2^14 = 16384, cheap
            g, d, agree = grouped_Nc_form(n, r)
            agree_all &= agree
            if not agree:
                print(f"   MISMATCH n={n} r={r}: grouped={g} direct={d}")
    print(f"grouped-vs-direct agreement on n in [0,60], r in [3,16]: "
          f"{'PASS' if agree_all else 'FAIL'}")
    print("(mathematically the same reindexed sum; this confirms the code)\n")

    print("=== (1) congruence (*) for n in [0,300], digit-free n (must PASS) ===")
    nfree_pass = 0
    nfree_fail = []
    nonfree_fail = 0
    for n in range(0, 301):
        for r in range(3, n + 6):     # r <= n+5
            lhs, rhs, free, _, _ = verify_identity_for_n(n, r)
            eq = (lhs == rhs)
            if free:
                nfree_pass += 1
                if not eq:
                    nfree_fail.append((n, r))
            else:
                if not eq:
                    nonfree_fail += 1
    print(f"digit-free congruence pairs checked: {nfree_pass}")
    print(f"digit-free congruence failures: {nfree_fail[:10] if nfree_fail else 'NONE (all pass)'}")
    print(f"non-digit-free congruence pairs that FAIL (*): {nonfree_fail} "
          f"(expected > 0 — (*) is not an identity off the digit-free set)")

    # exact identity sum_{a in A} 3^a == 2^n, on digit-free n
    exact_ok = True
    bad = []
    for n in range(0, 301):
        _, _, free, sA, two_n = verify_identity_for_n(n, 3)
        if free and sA != two_n:
            exact_ok = False
            bad.append(n)
    print("exact 2^n == sum_{a in A} 3^a on digit-free n in [0,300]: "
          f"{'PASS' if exact_ok else 'FAIL '+str(bad)}")

    print("\n=== (1b) NON-digit-free n: (*) is NOT an identity (correction to task) ===")
    nf_fail = 0
    nf_hold = 0
    first_fail = None
    for n in range(0, 301):
        _, _, free, sA, two_n = verify_identity_for_n(n, 3)
        if not free:
            exacts = (sA == two_n)
            if not exacts:
                nf_fail += 1
                if first_fail is None:
                    first_fail = n
            else:
                nf_hold += 1
    print("non-digit-free n in [0,300] where sum_{a in A}3^a != 2^n exactly: "
          f"{nf_fail}")
    print(f"non-digit-free n where it coincidentally equals: {nf_hold}")
    if first_fail is not None:
        _, _, _, sA, two_n = verify_identity_for_n(first_fail, 3)
        print(f"first such n = {first_fail}: sum over A = {sA}, 2^n = {two_n}, "
              f"digits = {''.join(reversed([str(d) for d in base3_digits_lsb(two_n)]))}")

    print("\n=== (2) digit-free n in [0,400]: every (*) congruence holds ===")
    free_list = [n for n in range(0, 401)
                 if digit_free_lsb(base3_digits_lsb(2 ** n))]
    print("digit-free n in [0,400]:", free_list)
    fail2 = []
    for n in free_list:
        for r in range(3, min(n, 40) + 1):
            lhs, rhs, _, _, _ = verify_identity_for_n(n, r)
            if lhs != rhs:
                fail2.append((n, r))
    # also the identity LHS == 2^n exactly on all free n
    exact_free = all(verify_identity_for_n(n, 3)[3] == 2 ** n for n in free_list)
    print(f"digit-free (2)/(4)-style congruence failures: {fail2 if fail2 else 'NONE'}")
    print(f"exact LHS(sum N_c 3^c) == 2^n on every digit-free n in [0,400]: {exact_free}")
    print("\nNote: for digit-free n, sum_c N_c 3^c = sum_{a in A} 3^a = 2^n EXACTLY, "
          "so (*) is the tautology 2^n ≡ 2^n (mod 2^r).  It is always satisfiable.")


if __name__ == "__main__":
    main()
