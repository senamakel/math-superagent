#!/usr/bin/env python3
"""verify_mrstt_witnesses.py

Reproduce the Singmaster/MRSTT witness set in exact integer arithmetic.
Every binomial value is computed with math.comb (exact integers); no floats
are used for any binomial.

Convention (identical to code/out/witnesses.json): N(a) counts BOTH
mirrored pairs C(n,k) and C(n,n-k) as two distinct pairs, and includes the
trivial pair C(a,1) = C(a,a-1).

Parts
-----
1.  C(3003,1) = C(78,2) = C(15,5) = C(14,6) = 3003, and exactly 8 pairs
    (n,k), n <= 3003, with C(n,k) = 3003, by direct triangle enumeration.
2.  The six known N(a)=6 witnesses 120, 210, 1540, 7140, 11628, 24310
    from code/out/witnesses.json (plus 3003 with N=8), each confirmed by
    direct enumeration of the rows n <= a.
3.  The infinite Fibonacci (Lind/Tovey) family: for j = 1..12,
    n = F(2j+2)*F(2j+3) - 1,  m = F(2j)*F(2j+3) - 1,  check
    C(n+1,m+1) == C(n,m+2) exactly. Direct math.comb where k is small
    enough; everywhere via the algebraically equivalent integer identity
    (n+1)*(m+2) == (n-m)*(n-m-1), derived from the ratio of the two
    binomials (the ratio is exactly
    C(n+1,m+1)/C(n,m+2) = (n+1)(m+2) / ((n-m)(n-m-1)), so the identity
    holds iff the binomials are equal).
4.  The k <= log2(a) bound: for a <= 10^12 only k = 1..39 are candidates,
    so inverting C(n,k) = a costs about 39 binary searches (~1560 comb
    evaluations) per a instead of scanning a^2/2 triangle entries.

Run:  timeout 300 python3 /workspace/code/verify_mrstt_witnesses.py
"""

import json
import math
import sys
import time
sys.set_int_max_str_digits(0)  # exact binoms have thousands of digits; no limit
from pathlib import Path

# math.comb is O(k) big-int operations; above this k, compute the gigantic
# binomials only through the exact equivalent identity (see part 3).
MAX_DIRECT_COMB_K = 200_000

WITNESSES_PATH = Path("/workspace/code/out/witnesses.json")


def fib(n):
    """F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2). Exact integers."""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def scan_triangle_for(a, n_max=None):
    """Directly enumerate the triangle rows n=1..n_max (default n_max=a).

    Exhaustive for finding C(n,k)=a with n <= n_max: any solution has
    k <= n//2 up to mirror symmetry, and C(n,k) strictly increases with k
    for k <= n//2, so the inner loop breaks as soon as C(n,k) > a.
    Returns the sorted list of upper-half representatives (n,k) with
    k <= n-k and C(n,k) == a, each binomial computed exactly.
    """
    if n_max is None:
        n_max = a
    found = []
    for n in range(1, n_max + 1):
        for k in range(1, n // 2 + 1):
            c = math.comb(n, k)
            if c == a:
                found.append((n, k))
            elif c > a:
                break
    return found


def with_mirrors(reps):
    """Expand upper-half reps (k <= n//2) to the full pair set. (n,k) and
    (n,n-k) count as two distinct pairs unless k == n-k (n even, k=n/2)."""
    pairs = []
    for n, k in reps:
        if 2 * k == n:
            pairs.append((n, k))
        else:
            pairs.extend(((n, k), (n, n - k)))
    return sorted(pairs)


def fmt_pairs(pairs):
    return ", ".join(f"C({n},{k})" for (n, k) in pairs)


def main():
    t0 = time.perf_counter()

    # ---------------------------------------------------------------- part 1
    print("=" * 78)
    print("Part 1: the 3003 witness -- four pairs, one value, N(3003)=8")
    print("  convention: (n,k) and (n,n-k) are two distinct pairs; C(a,1), C(a,a-1) counted")
    witness_pairs = [(3003, 1), (78, 2), (15, 5), (14, 6)]
    vals = [math.comb(n, k) for (n, k) in witness_pairs]
    for (n, k), c in zip(witness_pairs, vals):
        print(f"    C({n:>4},{k:<2}) = {c}")
    assert all(c == 3003 for c in vals), "witness pairs must all equal 3003"
    print("  -> all four pairs give exactly 3003")

    reps = scan_triangle_for(3003, n_max=3003)  # direct enumeration, n <= 3003
    all_pairs = with_mirrors(reps)
    expected = sorted(
        [(14, 6), (14, 8), (15, 5), (15, 10), (78, 2), (78, 76),
         (3003, 1), (3003, 3002)]
    )
    print(f"  direct triangle scan, n<=3003, k<=n//2 with early-exit "
          f"(exhaustive: C(n,k)>3003 cannot be 3003):")
    print(f"    upper-half hits: {reps}")
    print(f"    all pairs counting mirrors: {fmt_pairs(all_pairs)}")
    assert all_pairs == expected, f"expected 8 pairs, got {all_pairs}"
    assert len(all_pairs) == 8
    print("  -> exactly 8 pairs (n,k) in the triangle with C(n,k)=3003: N(3003) = 8")
    print(f"     (matches code/out/witnesses.json: N=8)")

    # ---------------------------------------------------------------- part 2
    print("=" * 78)
    print("Part 2: direct-enumeration check of code/out/witnesses.json")
    with open(WITNESSES_PATH) as f:
        data = json.load(f)
    expected = {int(k): v for k, v in data["witnesses"].items()}
    for a in sorted(expected):
        exp_N = expected[a]["N"]
        exp_nontriv = [tuple(p) for p in expected[a]["nontrivial"]]
        reps = scan_triangle_for(a, n_max=a)
        nontriv = [p for p in reps if p[0] != a]          # drop trivial (a,1)
        all_pairs = with_mirrors(reps)
        for (n, k) in reps:
            assert math.comb(n, k) == a, f"C({n},{k}) != {a}"
        assert nontriv == exp_nontriv, (
            f"a={a}: nontrivial reps {nontriv} != JSON {exp_nontriv}")
        assert len(all_pairs) == exp_N, (
            f"a={a}: N={len(all_pairs)} != JSON N={exp_N}")
        print(f"  a={a}: {fmt_pairs(all_pairs)}")
        print(f"      nontrivial pairs {nontriv} match JSON; "
              f"N={len(all_pairs)} = 2 + 2*{len(nontriv)} matches JSON N={exp_N}")
    print("  -> all witnesses.json entries reproduced by direct enumeration")

    # ---------------------------------------------------------------- part 3
    print("=" * 78)
    print("Part 3: infinite Fibonacci family  C(n+1,m+1) == C(n,m+2)")
    print("  n = F(2j+2)*F(2j+3)-1,  m = F(2j)*F(2j+3)-1,  j = 1..12")
    print("  [for the huge members the binomial equality is checked through the")
    print("   exactly equivalent identity (n+1)(m+2) == (n-m)(n-m-1), since")
    print("   C(n+1,m+1)/C(n,m+2) = (n+1)(m+2)/((n-m)(n-m-1)) is exact;")
    print("   direct math.comb of both sides is used when k = m+2 is small]")
    all_hold = True
    for j in range(1, 13):
        n = fib(2 * j + 2) * fib(2 * j + 3) - 1
        m = fib(2 * j) * fib(2 * j + 3) - 1
        # exact check 1: cheap integer identity, equivalent to the binomial
        # equality (ratio of the two binomials equals 1 iff this holds)
        ident = (n + 1) * (m + 2) == (n - m) * (n - m - 1)
        k2 = m + 2
        if k2 <= MAX_DIRECT_COMB_K:
            lhs = math.comb(n + 1, m + 1)
            rhs = math.comb(n, m + 2)
            direct = lhs == rhs
            digits = (lhs.bit_length() * 30103) // 100000 + 1  # ~log10(lhs)
            common = str(lhs) if digits <= 40 else f"<{digits} digits>"
            tag = f"direct comb: OK ({common})"
        else:
            direct = None
            tag = "direct comb skipped (k too large); exact identity used"
        ok = ident and (direct is not False)
        all_hold = all_hold and ok
        print(f"  j={j:>2}: n={n}, m={m} | (n+1)(m+2)={(n+1)*(m+2)}, "
              f"(n-m)(n-m-1)={(n-m)*(n-m-1)} | holds={bool(ok)} | {tag}")
    assert all_hold, "a Fibonacci family member failed"
    assert math.comb(fib(4) * fib(5), fib(2) * fib(5)) == 3003  # j=1 ties to part 1
    print("  -> all 12 members hold: C(n+1,m+1) == C(n,m+2) exactly")
    print("     (j=1 is n=14,m=4, the 3003 witness: C(15,5) = C(14,6) = 3003)")

    # ---------------------------------------------------------------- part 4
    print("=" * 78)
    print("Part 4: candidate k values for a <= 10^12 (the k <= log2(a) bound)")
    A = 10 ** 12
    # C(n,k) >= C(2k,k) >= 2^k for n >= 2k  (each factor (k+i)/i >= 2),
    # so C(n,k) = a forces 2^k <= a, i.e. k <= log2(a).
    exact_floor = A.bit_length() - 1          # floor(log2(A)), exact integer
    print(f"  C(n,k) >= C(2k,k) >= 2^k  ==>  C(n,k)=a implies k <= log2(a)")
    print(f"  log2(10^12) = {math.log2(A):.6f}  -> floor = {exact_floor}")
    print(f"  candidate k per a: 1..{exact_floor}  -> {exact_floor} values")
    steps = exact_floor * A.bit_length()      # ~39 binary searches x ~40 evals
    print(f"  per-a inversion cost: {exact_floor} candidate k x "
          f"~{A.bit_length()} binary-search steps ~= {steps} comb evaluations")
    print(f"  vs naive triangle scan: ~a^2/2 = {A*A//2} pairs for a=10^12")
    print("  -> the inversion count is ~1560 exact comb() calls per a, not a^2/2")

    # ---------------------------------------------------------------- summary
    print("=" * 78)
    print(f"ALL CHECKS PASSED in {time.perf_counter() - t0:.2f} s "
          f"(exact integer arithmetic throughout)")


if __name__ == "__main__":
    main()