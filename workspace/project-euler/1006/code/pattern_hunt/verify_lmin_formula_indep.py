"""Independent cross-check of Lmin(k) = k + NextFib(k) - 1.

Second, deliberately different route: plain Python str substrings (no bit-mask
integer factor extraction like verify_lmin_formula_f20.py).  Checks a sampled
set of k spanning the whole range 1..6764 plus every Fibonacci boundary, on a
prefix of length >= 24000, and reports any disagreement with the formula.
Used to confirm the bit-mask result is not an artifact of that extraction
method.
"""

from lib.fibword import fib_prefix, next_fib, lmin_formula


def lmin_plain(W, ks):
    """Lmin(k) for each k in ks, by plain substring scanning.  Each k stops
    as soon as its (k+1)-th distinct factor is seen."""
    L = len(W)
    out = {}
    for k in ks:
        s = set()
        for i in range(L - k + 1):
            s.add(W[i:i + k])
            if len(s) == k + 1:
                out[k] = i + k
                break
    return out


def main():
    L = 24000
    W = fib_prefix(L)
    print(f"prefix length {len(W)} (>= 24000)")

    ks = set([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
              1596, 1597, 2583, 2584, 4180, 4181, 6764])
    # every Fibonacci boundary in range: k = F_m - 1, F_m, F_m + 1
    a, b = 1, 2
    while b <= 6764:
        for k in (b - 1, b, b + 1):
            if 1 <= k <= 6764:
                ks.add(k)
        a, b = b, a + b

    kmax = max(ks)
    lm = lmin_plain(W, sorted(ks))
    assert all(v is not None for v in lm.values()), "prefix too short"

    mism = []
    for k in sorted(ks):
        if lm[k] != lmin_formula(k):
            mism.append((k, lm[k], lmin_formula(k)))
    print(f"independent plain-substring check on {len(ks)} sampled k-values: "
          f"{len(mism)} mismatches")
    if mism:
        print("first mismatches:", mism[:10])
    else:
        print("no mismatches (agrees with bit-mask run and with the formula)")

    print("\nRequested values via plain substrings:")
    for k in [1596, 1597, 2583, 2584, 4180, 4181, 6764]:
        print(f"  k={k:5d}  Lmin={lm[k]:6d}  formula={lmin_formula(k):6d}")


if __name__ == '__main__':
    main()