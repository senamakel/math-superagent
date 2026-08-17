"""Task C (rigorous): structural facts of the factor matrix.

1. Verify each column i is a circular interval (contiguous run of ones mod k+1).
2. Verify N(i;k) is constant across the few levels {floor((k+1)a), ceil((k+1)a)},
   a = (3-sqrt5)/2 = 1/phi^2, and FIT N(i;k) = floor((k-i)*a + const).
3. Verify pair correlation C(i,i+d) is constant in i for fixed d.
4. Build the exact Psi(k) from the (k+1)xk matrix to validate the formula.

Exact/very-high-precision rational arithmetic for fitting.
"""
import json
import os

MOD = 101001001
DATA = os.path.join(os.path.dirname(__file__), "..", "out", "factors_k40.json")

# exact alpha = (3-sqrt5)/2 as a high-precision decimal for fitting
from mpmath import mp, mpf, sqrt
mp.dps = 60
ALPHA = mpf(3) / 2 - sqrt(5) / 2  # (3-sqrt5)/2 = 1/phi^2


def load_factors():
    return json.load(open(DATA))


def is_circular_interval(bits):
    """bits: list of 0/1. Return True if the 1s form a contiguous circular run."""
    ones = [i for i, b in enumerate(bits) if b == 1]
    if not ones:
        return True
    L = len(bits)
    if len(ones) == L:
        return True
    # sort; check consecutive circular gaps all 1 except one, or contiguity linear
    # Approach: the set of ones is a circular interval iff its complement is a
    # single contiguous circular interval (or empty).
    zeros = [i for i, b in enumerate(bits) if b == 0]
    # zeros contiguous circular run?
    n = len(zeros)
    if n == 0:
        return True
    s = sorted(zeros)
    gaps = [s[(j + 1) % n] - s[j] for j in range(n)]
    # circular: wrap
    gaps = [(s[(j + 1) % n] - s[j]) % L for j in range(n)]
    return gaps.count(1) == n - 1


def main():
    data = load_factors()

    print("=" * 70)
    print("TASK C structural analysis")
    print(f"alpha = (3-sqrt5)/2 = 1/phi^2 = {mp.nstr(ALPHA, 40)}")
    print("=" * 70)

    # ---- 1. columns are circular intervals ----
    print("\n[1] Each column a circular interval of ones (mod k+1 rows)?")
    for k in range(1, 41):
        facs = data[str(k)]
        good = True
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            if not is_circular_interval(bits):
                good = False
                break
        if not good:
            print(f"   k={k}: FAIL (column not circular interval)")
        if k <= 40 and k % 10 == 0:
            print(f"   ... checked k={k}: columns-all-circular = {good}")

    alln = True
    for k in range(1, 41):
        facs = data[str(k)]
        for i in range(k):
            bits = [1 if f[i] == '1' else 0 for f in facs]
            if not is_circular_interval(bits):
                alln = False
                print(f"   first non-circular column at k={k}, i={i}")
                break
        if not alln:
            break
    print("   ALL columns circular for k=1..40:", alln)

    # ---- 2. N(i;k) closed form: values in {floor((k+1)a), ceil((k+1)a)} ----
    print("\n[2] N(i;k) = #factors with 1 at position i. Values vs floor/ceil((k+1)a):")
    s_floor = lambda k: int((mpf(k + 1) * ALPHA))
    s_ceil = lambda k: int(mpf(k + 1) * ALPHA) + 1
    ok_all = True
    for k in range(1, 41):
        facs = data[str(k)]
        lo, hi = s_floor(k), s_ceil(k)
        for i in range(k):
            n = sum(1 for f in facs if f[i] == '1')
            if n != lo and n != hi:
                ok_all = False
                print(f"   k={k} i={i}: N={n} outside [{lo},{hi}]  (k+1)*a={mp.nstr((k+1)*ALPHA,12)})")
    print("   N(i;k) in {floor((k+1)a), floor((k+1)a)+1} for all k<=40:", ok_all)

    # FIT: N(i;k) = floor((k+1)*a + c_i) or floor((k+1-i)*a + c)? Try several.
    print("\n   Fit attempt: is N(i;k) = floor((k+1-i)*A + B) for some A?")
    # We'll test A=1-ALPHA? Actually try to find A,B (real) that reproduce all N.
    # Because N(i;k) is ~ (k+1)a regardless of i, a fit to (k+1)*a is natural.
    # Check: does N(i;k) = floor((k+1)*a) or +1, and the +1 pattern?
    print("   Print N(i;k) - floor((k+1)*a) for each k to see the +1 pattern:")
    for k in range(1, 26):
        facs = data[str(k)]
        base = s_floor(k)
        pat = []
        for i in range(k):
            n = sum(1 for f in facs if f[i] == '1')
            pat.append(n - base)
        print(f"   k={k:2d}: (k+1)*a={mp.nstr((k+1)*ALPHA,8):>10} floor={base}, pattern(N - floor) = {pat}")

    # ---- 3. pair-correlation constant in i for fixed gap ----
    print("\n[3] Pair-correlation C(i,i+d) constant in i for fixed d (k up to 40):")
    pair_ok = True
    for k in range(4, 41):
        facs = data[str(k)]
        for d in range(1, min(k, 8)):
            vals = []
            for i in range(k - d):
                c = sum(1 for f in facs if f[i] == '1' and f[i + d] == '1')
                vals.append(c)
            if len(set(vals)) > 1:
                pair_ok = False
                print(f"   k={k} d={d}: C varies: {vals}")
                break
        if not pair_ok:
            break
    print("   C(i,i+d) constant in i for all k<=40 (d up to 7):", pair_ok)


if __name__ == "__main__":
    main()
