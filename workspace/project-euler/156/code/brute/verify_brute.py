"""Independent verification of code/brute.py's scan results.

Second route (rule: verify independently): instead of counting digits by
string-scanning every integer to 300000, evaluate the closed-form place-value
digit count f_place_value(n, 1) at each n the oracle reported as a solution,
and also probe the oracle's two negative claims:
  * f(n,1) == 3 over 0..200000  ->  assert none, and none in 0..300000
  * 199981 really is the third solution  ->  assert f(199981,1) == 199981
      and f(n,1) != n for every 2 <= n < 199981 (checked by direct count).
Additionally, by way of cross-checking the counter-program itself, evaluate
f_place_value(n, 1) for every n in 0..20000 and compare with the brute-force
running-total f; they must agree everywhere.
"""
from lib.digits import f_place_value

ORACLE_SOLS = [0, 1, 199981, 199982, 199983, 199984, 199985, 199986,
               199987, 199988, 199989, 199990, 200000, 200001]


def f_running(limit, d):
    """Brute-force running total (same method as brute.py), for cross-check."""
    total = 0
    vals = []
    ds = str(d)
    for i in range(limit + 1):
        total += str(i).count(ds)
        vals.append(total)
    return vals


def main():
    sols = []
    for n in ORACLE_SOLS:
        f = f_place_value(n, 1)
        assert f == n, f"closed-form f({n},1)={f} != {n}"
        sols.append(n)
    print("place-value counter confirms every oracle solution n with f(n,1)=n:")
    print(sols)

    # Cross-check the counter-program against brute force on the whole small
    # range first (this also proves f(981,1) etc. along the way).
    vals = f_running(20000, 1)
    for n in range(20001):
        got = f_place_value(n, 1)
        assert got == vals[n], f"mismatch at n={n}: {got} vs {vals[n]}"
    print("place-value counter agrees with brute-force running total for all n in 0..20000.")

    # 199981 is the third solution: f(n,1) != n for all 2 <= n < 199981.
    bad = [n for n in range(2, 199981) if f_place_value(n, 1) == n]
    assert not bad, f"unexpected early solutions: {bad}"
    print("no solution of f(n,1)=n between 2 and 199980, so 199981 is the third:", end=" ")
    print(f_place_value(199981, 1) == 199981)

    # f(n,1) == 3 never occurs in 0..300000.
    hits = [n for n in range(300001) if f_place_value(n, 1) == 3]
    assert not hits, f"f(n,1)=3 at {hits}"
    print("f(n,1)=3 never occurs for any n in 0..300000: confirmed")

    # No solution strictly between 200001 and 300000 (oracle found 14 total).
    between = [n for n in range(200002, 300001) if f_place_value(n, 1) == n]
    assert not between, f"unexpected solutions 200002..300000: {between}"
    print("no solution of f(n,1)=n with 200002 <= n <= 300000: confirmed")


if __name__ == "__main__":
    main()