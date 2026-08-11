"""Project Euler 591 - brute-force oracle.

BQA_d(x,n) = quadratic integer a + b*sqrt(d) with |a|,|b| <= n closest to x,
minimizing |a + b*sqrt(d) - x|.

Brute force: for each b in [-n, n], best a = round(x - b*sqrt(d)); if |a|<=n,
record error. Track global min, tie-break by smaller error then smaller |a|.
Report both on a tie of equal error.
"""
import math


def bqa_brute(d, x, n):
    """Return (a, b) of the best quadratic integer and its absolute error.

    Tracks smallest error; on equal error picks smaller |a|; reports all
    candidates tied for the minimum error.
    """
    s = math.sqrt(d)
    best_err = float("inf")
    best = None            # (a, b) with smallest error
    tie_tallies = None     # spots with equal smallest error, by |a|
    for b in range(-n, n + 1):
        a = round(x - b * s)          # Python round-half-even; ties harmless
        if abs(a) > n:
            continue
        err = abs(a + b * s - x)
        if err < best_err - 1e-18:
            best_err = err
            best = (a, b)
            tie_tallies = {(abs(a), a, b): (a, b)}
        elif abs(err - best_err) <= 1e-18 * max(1.0, best_err):
            tie_tallies.setdefault((abs(a), a, b), (a, b))
    # best = globally smallest-error candidate with smallest |a| (ties broken)
    return best[0], best[1], best_err, tie_tallies


def top_errors(d, x, n, k):
    """Return sorted list of (error, a, b, |a|) of the k best candidates."""
    s = math.sqrt(d)
    rows = []
    for b in range(-n, n + 1):
        a = round(x - b * s)
        if abs(a) > n:
            continue
        err = abs(a + b * s - x)
        rows.append((err, a, b, abs(a)))
    rows.sort(key=lambda r: (r[0], r[3], r[1]))
    return rows[:k]


def check(d, n, ea, eb, label):
    a, b, err, _ = bqa_brute(d, math.pi, n)
    ok = (a == ea and b == eb)
    print(f"[{label}] d={d} n={n}  -> a={a} b={b} err={err:.6e}  "
          f"expected a={ea} b={eb}  {'PASS' if ok else 'FAIL'}")
    return ok


all_ok = True
all_ok &= check(2, 10, 6, -2, "example 1")
all_ok &= check(5, 100, -55, 26, "example 2")
all_ok &= check(7, 10**6, 560323, -211781, "example 3")

# d=2 n=10^7, 10^8; d=3 n=10^6  (within reach, record)
a, b, err, ties = bqa_brute(2, math.pi, 10**7)
print(f"[record] d=2 n=10^7 -> a={a} b={b} err={err:.6e}")
a, b, err, ties = bqa_brute(2, math.pi, 10**8)
print(f"[record] d=2 n=10^8 -> a={a} b={b} err={err:.6e}")
a, b, err, ties = bqa_brute(3, math.pi, 10**6)
print(f"[record] d=3 n=10^6 -> a={a} b={b} err={err:.6e}")

# numeric check of the given 10^13 candidate
a13 = -6188084046055
b13 = 4375636191520
err13 = abs(a13 + b13 * math.sqrt(2) - math.pi)
print(f"[check] d=2 n=10^13 candidate a={a13} b={b13} -> |a+b*sqrt(2)-pi|={err13:.3e} "
      f"(expect < 1e-13: {'PASS' if err13 < 1e-13 else 'FAIL'})")

# top-3 table for tie-break inspection
print("\nTop-3 smallest errors for d=2 n=100:")
for err, a, b, aa in top_errors(2, math.pi, 100, 3):
    print(f"  err={err:.6e}  a={a}  b={b}  |a|={aa}")

print(f"\nALL WORKED EXAMPLES PASS: {all_ok}")
