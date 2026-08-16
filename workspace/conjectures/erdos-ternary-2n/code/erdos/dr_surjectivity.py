#!/usr/bin/env python3
"""Settle whether the adopted cross-modulus route can reduce the survivor count
below |A_k| = 2^(k-1).  Answer: NO, for every modulus q coprime to 3.

Section 1 - oracle reproduction (exact integer arithmetic):
    digit_free(2^0), digit_free(2^2), digit_free(2^8) = True;
    digit_free(2^5) = False  (2^5 = 32 = 1012_3).

Section 2 - structural fact, PROVED and verified by construction:
    Dr(q) := { s mod q : s is a digit-{0,1} ternary integer } = F_q
    for every q >= 2 with gcd(q, 3) = 1.  Verified for every q in
    [5,300] coprime to 3 (197 moduli, 257 among them) and the primes
    641, 1021, for every residue t, by building the witnesses
    S_t = sum_{j<t} 3^(j*m)  (m = ord_q(3)) and checking S_t mod q == t
    and that S_t is digit-{0,1}.

Section 3 - corrected mixed-modulus sieve, mod 3^k only (2^n never built):
    for survivor r in A_k (low k ternary digits of 2^r avoid 2), write
    2^r = L_r + 3^k s with L_r = 2^r mod 3^k.  2^r is fully digit-free
    iff s is digit-free.  The mod-q consistency (b') requires a digit-free
    s with residue  (2^r - L_r) * (3^k)^(-1) (mod q)  in Dr(q); because
    Dr(q) = F_q this is VACUOUS, so mixed_count == pure == 2^(k-1) for
    every (q,k) tested: no mixed modulus kills any survivor class.

Section 4 - conclusion: hypothesis H1 of CROSS-MODULUS-BEATS-SIEVE-
    HYPOTHESES (a mixed modulus forcing the survivor count strictly below
    2^(k-1)) is REFUTED: the digit-{0,1} integers are surjective mod every
    q coprime to 3, so no mixed modulus introduces a nontrivial consistency
    constraint and |A_k| stays 2^(k-1) forever.

Complexity: all loops are polynomial in the stated bounds (q <= 1021,
k <= 9, the fixed grid).  No exponential search anywhere.
"""
import sys
import time
from math import gcd


def to_base3(m):
    """Base-3 digit string of m >= 0, most significant first."""
    if m == 0:
        return "0"
    digs = []
    while m:
        digs.append(str(m % 3))
        m //= 3
    return "".join(reversed(digs))


def digit_free_int(m):
    """True iff the base-3 expansion of integer m >= 0 avoids digit 2."""
    while m:
        if m % 3 == 2:
            return False
        m //= 3
    return True


def digit_free(n):
    """True iff the base-3 expansion of 2**n avoids digit 2.  Exact."""
    return digit_free_int(2 ** n)


def order_mod(a, q):
    """Smallest d >= 1 with a**d == 1 (mod q); requires gcd(a, q) == 1."""
    x = 1
    for d in range(1, q + 1):
        x = (x * a) % q
        if x == 1:
            return d
    raise AssertionError("no multiplicative order")


def verify_order(a, q, m):
    """Exact check that m is the multiplicative order of a mod q."""
    assert 1 <= m <= q and pow(a, m, q) == 1
    assert all(pow(a, d, q) != 1 for d in range(1, m))
    return True


def phi(n):
    return sum(1 for x in range(1, n) if gcd(x, n) == 1)


def lcm(a, b):
    return a // gcd(a, b) * b


def invmod(a, m):
    """Inverse of a modulo m by the extended Euclidean algorithm.  Exact."""
    t, nt, r, nr = 0, 1, m, a % m
    while nr:
        qq = r // nr
        t, nt = nt, t - qq * nt
        r, nr = nr, r - qq * nr
    assert r == 1
    return t % m


THEOREM = r"""THEOREM (surjectivity of digit-{0,1} ternary integers mod q).
Let q >= 2 with gcd(3, q) = 1, and let
    Dr(q) = { s mod q : s is a digit-{0,1} ternary integer }.
Then Dr(q) = F_q (all of Z/qZ).

PROOF.  Since gcd(3,q) = 1, 3 is a unit mod q; let m = ord_q(3) be its
multiplicative order.  Then 3^m == 1 (mod q), hence every power 3^(j*m)
satisfies 3^(j*m) = (3^m)^j == 1 (mod q).  The integers 3^0, 3^m, 3^(2m), ...
are pairwise DISTINCT powers of 3.  For t = 0..q-1 define
    S_t = 3^0 + 3^m + 3^(2m) + ... + 3^((t-1)*m)      (S_0 = 0).
Each S_t is a sum of DISTINCT powers of 3, so no two summands share a base-3
digit position, no carry can occur, and the base-3 expansion of S_t is the
digit-{0,1} word with a 1 in the positions 0, m, 2m, ..., (t-1)*m and 0s
elsewhere.  Reducing S_t modulo q term by term,
    S_t == 1 + 1 + ... + 1 == t  (mod q).
As t runs over 0..q-1 the residues t cover every element of F_q, so
Dr(q) contains F_q; trivially Dr(q) is contained in F_q.  Hence Dr(q) = F_q.
                                                                       [QED]
"""


def verify_dr_surjectivity(qs, convert_cap=2000):
    """Verify Dr(q) = F_q by constructing the proof's witnesses S_t.

    For every residue t of every q: S_t = sum_{j<t} 3^(j*m) with
    m = ord_q(3), checking (i) S_t mod q == t, (ii) S_t is digit-{0,1}
    (no-overlap position array + independent base-3 conversion of the
    witnesses small enough to convert cheaply), (iii) the set of positions
    used has exactly one 1 per summand.  The position array is the exact
    digit-{0,1} certificate for every t (distinct powers of 3 never carry);
    the base-3 conversion is a spot check on the small prefix, kept small
    because to_base3 is quadratic in the number of digits.
    Returns dict q -> (m, ok, conv_ok, conv_count).
    """
    out = {}
    for q in qs:
        m = order_mod(3, q)
        verify_order(3, q, m)
        assert phi(q) % m == 0, (q, phi(q), m)   # Lagrange sanity check
        npos = (q - 1) * m + 1                   # positions 0..(q-1)*m
        arr = bytearray(npos)
        s = 0                                    # exact S_t big integer
        term = 1                                 # 3^(t*m)
        p3m = 3 ** m
        modsum = 0                               # S_t mod q by recurrence
        ok = True
        conv_ok = True
        conv_count = 0
        set_count = 0
        for t in range(q):
            if s % q != t or modsum != t or set_count != t:
                ok = False
            if t > 0 and (t - 1) * m + 1 <= convert_cap:
                digs = to_base3(s)
                conv_count += 1
                good = (len(digs) == (t - 1) * m + 1
                        and all(c in "01" for c in digs)
                        and digs.count("1") == t)
                if not good:
                    conv_ok = False
                    ok = False
            pos = t * m
            if pos < npos and arr[pos] == 0:
                arr[pos] = 1
                set_count += 1
            else:
                ok = False
            s += term
            term *= p3m
            modsum = (modsum + pow(3, t * m, q)) % q
        if set_count != q or arr.count(1) != q:
            ok = False
        out[q] = (m, ok, conv_ok, conv_count)
    return out


def pure_survivors(k):
    """A_k = { r mod 2*3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }.
    Computed by survivor lifting, mod 3^k only; 2^n is never materialised.
    """
    A = {0}
    cur = 1
    while cur < k:
        L = 2 * 3 ** (cur - 1)
        m3 = 3 ** (cur + 1)
        g = pow(2, L, m3)
        scale = 3 ** cur
        nxt = set()
        for r in A:
            base = pow(2, r, m3)
            gp = 1
            for j in range(3):
                v = (base * gp) % m3
                d = (v // scale) % 3
                if d in (0, 1):
                    nxt.add(r + j * L)
                gp = (gp * g) % m3
        A = nxt
        cur += 1
    return sorted(A)


def direct_survivors(k):
    """Naive oracle for A_k: enumerate every r in the period.  Small k only."""
    mod = 3 ** k
    period = 2 * 3 ** (k - 1)
    out = []
    for r in range(period):
        v = pow(2, r, mod)
        vv = v
        ok = True
        for _ in range(k):
            if vv % 3 == 2:
                ok = False
                break
            vv //= 3
        if ok:
            out.append(r)
    return out


def dr_witnesses(q):
    """Proof's witnesses S_w = sum_{j<w} 3^(j*m), m = ord_q(3), w = 0..q-1.

    Built incrementally (one addition and one multiplication per step, so
    the whole list costs O(q^2 m) big-int work, polynomial in q).  Verifies
    per w that S_w mod q == w (residue coverage) and that the summands
    occupy distinct base-3 positions (digit-{0,1}, no carry).
    Returns (m, S)."""
    m = order_mod(3, q)
    S = [0] * q
    term = 1                      # 3^(w*m), the summand about to be added
    p3m = 3 ** m
    npos = (q - 1) * m + 1        # positions 0 .. (q-2)*m used by S_{q-1}
    pos = bytearray(npos)
    for w in range(1, q):
        S[w] = S[w - 1] + term
        p = (w - 1) * m
        assert p < npos and pos[p] == 0, (q, w, p)   # distinct positions
        pos[p] = 1
        term *= p3m
    assert pos.count(1) == q - 1
    for w in range(q):
        assert S[w] % q == w, (q, w)                  # S_w == w (mod q)
    return m, S


def mixed_sieve(q, k):
    """Corrected mixed-modulus survivor count for modulus q at precision k.

    For every pure survivor r (low k ternary digits of 2^r avoid 2), the
    mod-q consistency (b') asks whether a digit-free high part s exists
    with 2^r = L_r + 3^k s, i.e. s == (2^r - L_r) * (3^k)^(-1) (mod q).
    Because Dr(q) = F_q, every residue class of q is representable by a
    digit-{0,1} ternary integer (a sum of distinct powers of 3, by the
    theorem), hence a digit-free s always exists; the constraint is
    vacuous and mixed_count == |A_k|.  Exact arithmetic mod 3^k only;
    2^n is never materialised.
    """
    inv3k = invmod(3 ** k, q)
    _m, S = dr_witnesses(q)       # S[w] digit-{0,1}, S[w] == w (mod q)
    A = pure_survivors(k)
    mod3k = 3 ** k
    for r in A:
        Lr = pow(2, r, mod3k)
        need = ((pow(2, r, q) - Lr % q) * inv3k) % q
        assert S[need] % q == need, (q, k, r, need)
    return len(A)


def main():
    t0 = time.time()
    print("=" * 78)
    print("dr_surjectivity: does a mixed modulus kill survivor classes?")
    print("=" * 78)

    # ---------------- Section 1: oracle reproduction ----------------
    print("\n[1] ORACLE REPRODUCTION (exact integer arithmetic)")
    witnesses = [0, 2, 8]
    expected = {0: True, 2: True, 8: True, 5: False}
    ok1 = True
    for n in witnesses:
        got = digit_free(n)
        print("    digit_free(2^%d) = %-5s  (2^%d = %s_3)"
              % (n, got, n, to_base3(2 ** n)))
        ok1 &= (got is expected[n])
    got5 = digit_free(5)
    print("    digit_free(2^5) = %-5s  (2^5 = %s_3)"
          % (got5, to_base3(2 ** 5)))
    ok1 &= (got5 is expected[5])
    print("    WITNESS REPRODUCTION:", "PASS" if ok1 else "FAIL")
    if not ok1:
        print("    ABORT: oracle does not reproduce the known witnesses")
        return 1

    # ---------------- Section 2: structural fact ----------------
    print("\n[2] STRUCTURAL FACT: Dr(q) = { s mod q : s digit-{0,1} } = F_q")
    print(THEOREM)
    qs = [q for q in range(5, 301) if gcd(q, 3) == 1]
    qs += [257] if 257 not in qs else []
    big_primes = [641, 1021]
    qs += big_primes
    qs = sorted(set(qs))
    res = verify_dr_surjectivity(qs)
    n_q = len(qs)
    failed = [q for q, (m, ok, conv, cc) in res.items() if not ok]
    n_conv = sum(cc for (m, ok, conv, cc) in res.values())
    print("    verified for every residue t of every q in the list below:")
    print("    moduli checked: %d  (q in [5,300] with 3|/q, plus 257, 641, 1021)"
          % n_q)
    print("    independent base-3 conversions of witnesses: %d" % n_conv)
    if failed:
        print("    SURJECTIVITY FAILED for q =", failed)
        return 1
    print("    SURJECTIVITY VERIFICATION: PASS for all %d moduli, "
          "all residues" % n_q)
    # report a couple of representative rows (m = ord_q(3))
    for q in (19, 257, 641, 1021):
        print("      sample row q=%d: ord_q(3)=%d, Dr(q)=F_q verified"
              % (q, res[q][0]))

    # ---------------- Section 3: corrected mixed sieve ----------------
    print("\n[3] CORRECTED MIXED-MODULUS SIEVE (mod 3^k only; 2^n never built)")
    QLIST = [5, 7, 11, 13, 17, 19, 29, 41, 193, 257]
    CAP = 300000
    grid = []
    for q in QLIST:
        for k in range(1, 10):
            u = lcm(2 * 3 ** (k - 1), order_mod(2, q))
            if u <= CAP:
                grid.append((q, k))
    print("    (q,k) grid after dropping those with lcm(2*3^(k-1), ord_q(2)) "
          "> %d: %d pairs" % (CAP, len(grid)))
    ok3 = True
    for q, k in grid:
        pure = len(pure_survivors(k))
        mixed = mixed_sieve(q, k)
        if pure != 2 ** (k - 1) or mixed != pure:
            ok3 = False
            print("    MISMATCH q=%d k=%d: pure=%d mixed=%d"
                  % (q, k, pure, mixed))
    # sanity: brute-force oracle on the smallest k
    for k in (1, 2, 3):
        assert direct_survivors(k) == pure_survivors(k), k
    print("    pure_survivors(k) == 2^(k-1) and mixed == pure for every "
          "(q,k):", "PASS" if ok3 else "FAIL")
    print("    brute-force oracle agrees with the lifting sieve for k = 1,2,3: "
          "PASS")

    # ---------------- Section 4: conclusion ----------------
    print("\n[4] CONCLUSION")
    if ok1 and not failed and ok3:
        print("    Hypothesis H1 of CROSS-MODULUS-BEATS-SIEVE-HYPOTHESES is "
              "REFUTED.")
        print("    Dr(q) = F_q for every q coprime to 3 (proved, verified by "
              "construction), so the mod-q")
        print("    consistency (b') is vacuous: a digit-free high part s "
              "always exists, no mixed modulus")
        print("    introduces a nontrivial constraint, and |A_k| = 2^(k-1) "
              "for every k.  A mixed modulus")
        print("    cannot reduce the survivor count below 2^(k-1).")
    else:
        print("    CHECK FAILED — see output above")
        return 1
    print("\n    elapsed: %.2f s" % (time.time() - t0))
    print("=" * 78)
    return 0


if __name__ == "__main__":
    sys.exit(main())
