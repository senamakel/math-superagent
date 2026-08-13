"""
Verification of the count-doubles theorem for the Erdős ternary conjecture.

The theorem (proved in code/out/lifting_theorem.md): for
    A_k = { r mod 2*3^(k-1) : the low k ternary digits of 2^r mod 3^k lie in {0,1} }
we have |A_k| = 2^(k-1).  The 3-adic sieve therefore never empties, so no
finite congruence can prove the conjecture.

This program checks the six computational pillars of that theorem.  Exact
integers only; 2^n is never materialised for large n — only pow(2, x, 3**k).
"""
import sys


# ---------------------------------------------------------------- section 1
def digit_free(m):
    """True iff the ternary expansion of m avoids the digit 2."""
    if m == 0:
        return True
    while m > 0:
        if m % 3 == 2:
            return False
        m //= 3
    return True


def ternary(m):
    if m == 0:
        return "0"
    digs = []
    while m > 0:
        digs.append(str(m % 3))
        m //= 3
    return "".join(reversed(digs))


def section1_digit_free():
    print("=" * 60)
    print("1. digit_free on given values")
    ok = True
    for m in (1, 4, 256):
        v = digit_free(m)
        print(f"   digit_free({m}) = {v}   ({m} = {ternary(m)}_3)")
        if not v:
            ok = False
    # values that must contain a 2
    for m in (32, 64):  # 2^5=32, 2^6=64
        v = digit_free(m)
        print(f"   digit_free({m}) = {v}   ({m} = {ternary(m)}_3)  [must be False]")
        if v:
            ok = False
    print(f"   -> {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- section 2
def order_of_2_mod_3k(k):
    """Order of 2 mod 3^k by order reduction over primes {2,3}."""
    m = 3 ** k
    if k == 1:
        # order of 2 mod 3 = 2 (phi=2)
        return 2
    order = 2 * (3 ** (k - 1))  # phi(3^k)
    # candidate = phi; divide out primes while the power order stays 1
    cand = order
    for p in (2, 3):
        while cand % p == 0 and pow(2, cand // p, m) == 1:
            cand //= p
    return cand


def section2_primitive_root():
    print("=" * 60)
    print("2. order of 2 mod 3^k == 2*3^(k-1) for k=1..40")
    ok = True
    for k in range(1, 41):
        o = order_of_2_mod_3k(k)
        want = 2 * (3 ** (k - 1))
        good = (o == want)
        if not good:
            ok = False
        print(f"   k={k:2d}  order={o}  expected={want}  {'ok' if good else 'MISMATCH'}")
    print(f"   -> {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- section 3
def low_digits_good(x, k):
    for _ in range(k):
        d = x % 3
        if d == 2:
            return False
        x //= 3
    return True


def sieve_direct(k):
    """Direct sieve: enumerate r in 0..2*3^(k-1)-1."""
    mod_n = 2 * (3 ** (k - 1))
    return [r for r in range(mod_n) if low_digits_good(pow(2, r, 3 ** k), k)]


def section3_direct_count():
    print("=" * 60)
    print("3. |A_k| by DIRECT sieve == 2^(k-1) for k=1..12")
    ok = True
    for k in range(1, 13):
        A = sieve_direct(k)
        want = 2 ** (k - 1)
        good = (len(A) == want)
        if not good:
            ok = False
        print(f"   k={k:2d}  |A_k|={len(A):5d}  expected={want:5d}  {'ok' if good else 'MISMATCH'}")
    print(f"   -> {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- section 4
def lifting(k):
    """Lift A_k to k+1; return total survivors."""
    A_prev = sieve_direct(k) if k > 0 else [0]
    if k == 0:
        # A_0 degenerate: single residue 0 modulo 1 -> base for building A_1
        return []
    M_k = 2 * (3 ** (k - 1))
    surv = 0
    for r in A_prev:
        survs = 0
        for j in (0, 1, 2):
            if low_digits_good(pow(2, r + j * M_k, 3 ** (k + 1)), k + 1):
                survs += 1
        assert survs == 2, f"k={k}: class r={r} did not have exactly 2 survivors (got {survs})"
        surv += survs
    return surv


def section4_lifting():
    print("=" * 60)
    print("4. LIFTING: exactly two of three lifts survive, total = 2^k, k=1..11")
    ok = True
    for k in range(1, 12):  # lift A_k to level k+1
        surv = lifting(k)
        want = 2 ** k  # |A_{k+1}| = 2*|A_k| = 2^(k-1)*2 = 2^k
        good = (surv == want)
        if not good:
            ok = False
        print(f"   k={k:2d}: survivors at level {k+1} = {surv:5d}  expected(2^k)={want:5d}  {'ok' if good else 'MISMATCH'}")
    print(f"   -> {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- section 5
def section5_lte():
    print("=" * 60)
    print("5. LTE: v_3(2^(2*3^(k-2)) - 1) = k-1 exactly, c in {1,2}, k=2..40")
    ok = True
    for k in range(2, 41):
        mod = 3 ** k
        # 2^(2*3^(k-2)) mod 3^k  == 1 + c*3^(k-1) with c in {1,2}
        val = pow(2, 2 * (3 ** (k - 2)), mod)
        c = (val - 1) // (3 ** (k - 1))
        good = (val % (3 ** (k - 1)) == 1) and (c in (1, 2))
        if not good:
            ok = False
        print(f"   k={k:2d}: c={c}  {'ok' if good else 'BAD'}")
    print(f"   -> {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- section 6
def section6_witnesses():
    print("=" * 60)
    print("6. Witnesses n=0,2,8: 2^n digit-free at every level k=1..40")
    ok = True
    for n in (0, 2, 8):
        for k in range(1, 41):
            g = low_digits_good(pow(2, n, 3 ** k), k)
            if not g:
                ok = False
                print(f"   FAIL: n={n} not digit-free at k={k}")
        print(f"   n={n}: digit-free for all k=1..40 {'ok' if True else ''}")
    print(f"   -> {'PASS' if ok else 'FAIL'}")
    return ok


if __name__ == "__main__":
    results = {}
    results["1_digit_free"] = section1_digit_free()
    results["2_primitive_root"] = section2_primitive_root()
    results["3_direct_count"] = section3_direct_count()
    results["4_lifting"] = section4_lifting()
    results["5_lte"] = section5_lte()
    results["6_witnesses"] = section6_witnesses()

    print("=" * 60)
    print("SUMMARY")
    all_ok = True
    for name, r in results.items():
        print(f"   {name}: {'PASS' if r else 'FAIL'}")
        all_ok = all_ok and r
    print(f"OVERALL: {'PASS' if all_ok else 'FAIL'}")
    sys.exit(0 if all_ok else 1)
