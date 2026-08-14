"""Naive oracle for Project Euler 156.

f(n, d) = total number of occurrences of digit d in all integers from 0 to n
inclusive, written in base 10.  This program computes f by literal digit
counting -- deliberately slow and obviously correct -- so it can pin down what
the statement means.  It is NOT the efficient method; it is the oracle the
fast method will later be checked against.
"""


import time


def f_naive(n, d):
    """Total occurrences of digit d in the decimal strings of 0..n inclusive.

    O(n * digits) per call, exact integer arithmetic.  Obviously correct.
    """
    ds = str(d)
    total = 0
    for i in range(n + 1):
        total += str(i).count(ds)
    return total


def f_incremental(limit, d):
    """Scan n = 0..limit once, maintaining one running total.

    Returns (solutions, hit_three):
      solutions  = [n in 0..limit with f(n,d) == n]
      hit_three  = True if the running f ever equalled 3 (verifies the
                   statement's "the value 3 never occurs" claim over the whole
                   scanned range, not just the 13-row printed table).
    The running total makes a full scan of `limit` feasible; a per-n call to
    f_naive up to a large limit would be O(limit^2), so this is the pass used
    for the "find the next solutions" check.
    """
    total = 0
    solutions = []
    hit_three = False
    ds = str(d)
    for i in range(limit + 1):
        total += str(i).count(ds)
        if total == i:
            solutions.append(i)
        if total == 3:
            hit_three = True
    return solutions, hit_three


def main():
    # --- Worked example 1: the f(n,1) table for n = 0..12 -----------------
    expected = {
        0: 0, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1,
        8: 1, 9: 1, 10: 2, 11: 4, 12: 5,
    }
    print("Table check  f(n,1), n=0..12:")
    all_ok = True
    for n in range(13):
        got = f_naive(n, 1)
        ok = got == expected[n]
        all_ok = all_ok and ok
        print(f"  n={n:2d}  f={got:2d}  expected={expected[n]:2d}  {'OK' if ok else 'MISMATCH'}")
    print(f"  table all match: {all_ok}")
    print(f"  value 3 never occurs in that table: {all(v != 3 for v in expected.values())}")

    # --- Worked example 2 (statement): f(22,2) = 6 ------------------------
    got22 = f_naive(22, 2)   # independent per-n counting, not the scan
    print(f"\nf(22,2) = {got22}   expected 6: {got22 == 6}")

    # --- Worked example 3 (statement): first solutions of f(n,1) = n are
    # 0, 1, then 199981.  One running-total pass to 300000 confirms 199981 is
    # a solution, reports every solution up to 300000, and keeps the "3 never
    # occurs" check over the whole scanned range.
    LIMIT = 300000
    t0 = time.perf_counter()
    sols, hit_three = f_incremental(LIMIT, 1)
    elapsed = time.perf_counter() - t0
    print(f"\nSolutions of f(n,1)=n in 0..{LIMIT}:")
    print(sols)
    print("  first three are 0, 1, 199981:", sols[:3] == [0, 1, 199981])
    print("  199981 is among the solutions:", 199981 in sols)
    print(f"  number of solutions up to {LIMIT}: {len(sols)}")
    print("  solutions after 200000:", [n for n in sols if n > 200000])
    print(f"  f(n,1)=3 ever occurs in the entire scanned range: {hit_three}")
    print(f"  timing for the 0..{LIMIT} scan: {elapsed:.3f} s")

    print("\nNOTE: reproducing s(1) = 22786974071 by enumeration would need a")
    print("scan to ~2e10, which is exactly the size the brute-force bound is")
    print("chosen to defeat -- not attempted here.  That is the efficient")
    print("method's job.")


if __name__ == "__main__":
    main()
