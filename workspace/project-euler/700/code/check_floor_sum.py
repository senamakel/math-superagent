"""Independent verification of Project Euler 700 that does NOT use the
record-low index recurrence n_{k+2} = ceil(...)*n_{k+1} - n_k.

Problem data:
    A = 1504170715041707
    M = 4503599627370517
    sequence c_n = (A * n) mod M  (n = 1, 2, 3, ...)
    An Eulercoin is a term strictly smaller than every earlier term (the
    running prefix minimum / record low).

The gold answer lives in /workspace/code/out/solution.txt (produced by the
index recurrence). This script re-derives the Eulercoin VALUE set and their
sum through two routes that share nothing with that recurrence:

Route A -- Euclidean/continued-fraction quotient descent on VALUES ONLY.
    The record lows (coins) v_1 > v_2 > ... > 0 of c_n come from the
    quotient structure of the map n -> A*n mod M. Their VALUES satisfy
        v_1 = A,  v_2 = (A * 3) mod M   (seed, statement's first two coins)
        v_{k+2} = (ceil(v_k / v_{k+1}) * v_{k+1} - v_k) mod m,  v_{k+1} > 0
    Reason: the index recurrence n_{k+2} = ceil(v_k/v_{k+1})*n_{k+1} - n_k
    gives c_{n_{k+2}} = (ceil(v_k/v_{k+1})*v_{k+1} - v_k) mod M, i.e. the
    next value is computable from the previous two values alone, with no
    reference to any index n. Iterating to a 0 value reproduces the complete
    Eulercoin value set. Index bookkeeping is deliberately absent.
    (Note: ceil(v_k/v_{k+1})*v_{k+1} - v_k is NOT always v_{k+1}-(v_k mod
    v_{k+1}): they differ at exact division, so the mod-free form is wrong and
    fails to terminate. We use the ceil form with a final mod m.)

Route B -- AtCoder floor_sum (exercised as a supporting arithmetic cross-check).
    floor_sum(n,m,a,b) = sum_{i=0}^{n-1} floor((a*i+b)/m) via the Euclidean
    recursion. On the real pair it is validated against closed forms:
        sum_{i=0}^{M-1} floor(A*i/M) = (A-1)*(M-1)/2          (full period)
        sum_{i=0}^{M-1} (A*i mod M)  = M*(M-1)/2   [via floor_sum above]
    This exercises exact big-integer recursion at full size on the same A, M.

All arithmetic is exact integer (Python ints, no floats).

Captured to /workspace/code/out/check_floor_sum.txt
"""
import os
import sys
from math import gcd

A = 1504170715041707
M = 4503599627370517


# --------------------------------------------------------------------------
# Route A: Euclidean quotient descent on values only.
# --------------------------------------------------------------------------
def record_lows_value_descent(a, m, seed_n1=1, seed_n2=3):
    """Eulercoin VALUES by a quotient descent (no index recurrence).

    Seeded with the first two record-low values v1 = (a*seed_n1) mod m and
    v2 = (a*seed_n2) mod m (on the real pair the statement's first two coins
    A at n=1 and 8912517754604 at n=3), then iterates values only:
        v_{k+2} = (ceil(v_k/v_{k+1}) * v_{k+1} - v_k) mod m   for v_{k+1} > 0
    until a 0 value appears. No indices are computed after the seed.
    Returns the full list [v_1, v_2, ..., 0] of Eulercoin values.
    For consistency the seed values must be actual record lows (second strictly
    below first); callers that do not know the indices pass
    seed_n2=None to have it found by a forward scan.
    """
    v1 = (a * seed_n1) % m
    if seed_n2 is None:
        v2 = None
        n = 2
        while True:
            c = (a * n) % m
            if c < v1:
                v2 = c
                break
            n += 1
    else:
        v2 = (a * seed_n2) % m
    vals = [v1, v2]
    while vals[-1] != 0:
        vk, vk1 = vals[-2], vals[-1]
        q = -(-vk // vk1)              # ceil(vk / vk1), exact ints
        nxt = (q * vk1 - vk) % m
        vals.append(nxt)
    return vals


def record_lows_brute(a, m):
    """Naive oracle: forward scan of c_n = a*n mod m, n = 1.., returning the
    record-low VALUES in order of occurrence (terminated at value 0, n = m)."""
    vals = []
    running_min = None
    for n in range(1, m + 1):
        c = (a * n) % m
        if running_min is None or c < running_min:
            vals.append(c)
            running_min = c
            if c == 0:
                break
    return vals


# --------------------------------------------------------------------------
# Route B: AtCoder floor_sum recursion.
# --------------------------------------------------------------------------
def floor_sum(n, m, a, b):
    """sum_{i=0}^{n-1} floor((a*i + b)/m), Euclidean recursion, O(log m).

    Convention as in the AtCoder Library floor_sum: reduces a, b mod m each
    step and swaps roles like the Euclidean algorithm. Exact integers.
    """
    ans = 0
    while True:
        if a >= m:
            ans += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            ans += n * (b // m)
            b %= m
        y_max = a * n + b
        if y_max < m:
            break
        n = y_max // m
        b = y_max % m
        m, a = a, m
    return ans


def main():
    out = []

    def p(s=""):
        out.append(s)
        print(s)

    p("=" * 78)
    p("Independent verification of Project Euler 700 (no index recurrence)")
    p("A = %d, M = %d, gcd(A,M) = %d" % (A, M, gcd(A, M)))
    p("=" * 78)

    assert 0 < A < M and gcd(A, M) == 1
    p("\nPASS: 0 < A < M and gcd(A,M) = 1")

    # ------------------------------------------------------------------
    # Route B: validate floor_sum at full size.
    # ------------------------------------------------------------------
    p("\n---- Route B: floor_sum on the real pair ----")
    F = floor_sum(M, M, A, 0)
    F_closed = (A - 1) * (M - 1) // 2
    p("floor_sum(M,M,A,0)       = %d" % F)
    p("closed form (A-1)(M-1)/2 = %d" % F_closed)
    okF = F == F_closed
    p(("PASS" if okF else "FAIL") + ": floor_sum matches closed form")

    S_res = A * M * (M - 1) // 2 - M * F
    okRes = S_res == M * (M - 1) // 2
    p("sum of residues over full period (via floor_sum) = %d" % S_res)
    p("expected M*(M-1)/2                              = %d" % (M * (M - 1) // 2))
    p(("PASS" if okRes else "FAIL") + ": residue-sum identity holds")

    def floor_sum_brute(n, m, a, b):
        return sum((a * i + b) // m for i in range(n))
    small_ok = all(floor_sum(n, m, a, b) == floor_sum_brute(n, m, a, b)
                   for (n, m, a, b) in [(10, 7, 5, 3), (17, 17, 7, 0),
                                        (23, 3, 1, 1), (100, 1000, 123, 45)])
    p("floor_sum vs direct summation on 4 small cases: " +
      ("PASS" if small_ok else "FAIL"))
    assert small_ok and okF and okRes

    # ------------------------------------------------------------------
    # Route A: certify the value descent against brute oracle on small pairs,
    # then run it on the real pair.
    # ------------------------------------------------------------------
    p("\n---- Route A - certify against brute force on small pairs ----")
    small_pairs = [(7, 17), (3, 23), (5, 13), (11, 29), (6, 35),
                   (9, 41), (13, 47)]
    small_ok = True
    for sa, sm in small_pairs:
        dvals = record_lows_value_descent(sa, sm, seed_n2=None)
        bvals = record_lows_brute(sa, sm)
        ok = dvals == bvals
        small_ok = small_ok and ok
        p("  A=%d, M=%d: descent %s == brute %s : %s" %
          (sa, sm, dvals, bvals, "PASS" if ok else "FAIL"))
    p("value descent matches brute-force oracle on %d small pairs: %s" %
      (len(small_pairs), "PASS" if small_ok else "FAIL"))
    assert small_ok

    p("\n---- Route A: Euclidean quotient descent on VALUES ONLY (real pair) ----")
    # Seed with the statement's first two Eulercoin values: A at n=1, and
    # 8912517754604 at n=3 (the smallest index whose value < A).
    vals = record_lows_value_descent(A, M, seed_n1=1, seed_n2=3)
    V = sum(vals)                                  # final 0 adds nothing
    ncoins = len(vals)
    p("Eulercoin value count (incl. final 0): %d" % ncoins)
    p("non-zero Eulercoin count:              %d" % sum(1 for v in vals if v))
    p("values strictly decreasing to 0:       %s" %
      ("PASS" if all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
       else "FAIL"))
    p("sum of all Eulercoin values V =        %d" % V)

    # ------------------------------------------------------------------
    # Compare against the gold in code/out/solution.txt.
    # ------------------------------------------------------------------
    p("\n---- Comparison against /workspace/code/out/solution.txt ----")
    sol_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "out", "solution.txt")
    gold_vals = []
    gold_V = None
    with open(sol_path) as fh:
        for line in fh:
            tl = line.strip()
            low = tl.lower()
            if low.startswith("final sum") or "sum v" in low:
                gold_V = int(tl.split()[-1])
            if "c_n =" in tl:
                gold_vals.append(int(tl.split("c_n =")[1].strip()))

    match_set = sorted(vals) == sorted(gold_vals)
    match_sum = (V == gold_V)
    match_count = (len(vals) == len(gold_vals))
    p("gold coin values read from solution.txt: %d" % len(gold_vals))
    p("gold sum V (solution.txt)              = %d" % gold_V)
    p("descent sum V                          = %d" % V)
    p("descent value set == gold value set    : " +
      ("PASS" if match_set else "FAIL"))
    p("descent value count == gold count      : " +
      ("PASS" if match_count else "FAIL"))
    p("descent sum == gold sum                : " +
      ("PASS" if match_sum else "FAIL"))

    if match_set:
        expect = [1504170715041707, 8912517754604, 2044785486369,
                  1311409677241, 578033868113, 422691927098, 267349986083,
                  112008045068, 68674149121, 25340253174]
        p("first 10 descent values: %s" %
          ", ".join(str(v) for v in vals[:10]))
        p("matches statement first 10: " +
          ("PASS" if vals[:10] == expect else "FAIL"))

    overall = okF and okRes and small_ok and match_set and match_count and \
        match_sum
    p("\n" + "=" * 78)
    p("OVERALL: %s" % ("PASS" if overall else "FAIL"))
    p("Final Eulercoin sum V (independent value descent): %d" % V)
    p("=" * 78)

    cap = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "out", "check_floor_sum.txt")
    with open(cap, "w") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n[captured to %s]" % cap)
    return 0 if overall else 1


if __name__ == "__main__":
    sys.exit(main())
