"""Naive oracle for Project Euler 156.

f(n, d) = total number of occurrences of digit d in all integers from 0 to n
inclusive, written in base 10.  This program computes f by literal digit
counting -- deliberately slow and obviously correct -- so it can pin down what
the statement means.  It is NOT the efficient method; it is the oracle the
fast method will later be checked against.
"""


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
    """Return (listed_table, solutions) using one running total pass.

    solutions  = [n in 0..limit with f(n,d) == n]
    The running total makes a full scan of `limit` feasible; a per-n call to
    f_naive up to a large limit would be O(limit^2), so this is the pass used
    for the "find the next solutions" check.
    """
    total = 0
    solutions = []
    ds = str(d)
    for i in range(limit + 1):
        total += str(i).count(ds)
        if total == i:
            solutions.append(i)
    return solutions


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

    # Note: f(11,1)=4, f(12,1)=5 confirmed above; the statement's claim that
    # f(n,1) never equals 3 is checked inside the solution scan below.

    # --- Worked example 2: first solutions of f(n,1)=n are 0, 1, then 199981
    # Run the scan only far enough past 199981 to confirm it is the third
    # solution and no other solution appears between 2 and 199981.
    LIMIT = 200000
    sols = f_incremental(LIMIT, 1)
    print(f"\nSolutions of f(n,1)=n in 0..{LIMIT}: {sols}")
    print("  first three are 0, 1, 199981:", sols[:3] == [0, 1, 199981])
    # value 3 never attained by f(n,1) for n in this range:
    attained = set()
    total = 0
    for i in range(LIMIT + 1):
        total += str(i).count("1")
        attained.add(total)
    print("  f(n,1)=3 ever occurs in 0..%d: %s" % (LIMIT, 3 in attained))

    print("\nNOTE: reproducing s(1) = 22786974071 by enumeration would need a")
    print("scan to ~2e10, which is exactly the size the brute-force bound is")
    print("chosen to defeat -- not attempted here.  That is the efficient")
    print("method's job.")


if __name__ == "__main__":
    main()
