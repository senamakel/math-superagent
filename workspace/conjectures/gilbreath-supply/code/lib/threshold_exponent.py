"""Fit the exponent of the exact-mean linear-supply threshold weight.

Data from code/out/threshold_limit_exact.txt PART A "first w" column:
threshold weight w*(n) = min w with mean_n(w) >= 0.40, n as listed.
Question: does w* ~ n^beta?  Fit log2(w*) vs log2(n) by least squares
over the large-n tail, report beta with a standard error, and test the
candidate closed forms log_4(3)=0.7925 and 1/2.

This is a measurement (numerical fit over sampled n), not a proof.
"""
import math

# (n, w*) from threshold_limit_exact.txt PART A  [first w column]
DATA = [
    (8, 3), (10, 3), (12, 3), (14, 4), (16, 3),
    (32, 5), (64, 7), (128, 11), (256, 16), (512, 24),
    (1024, 35), (2048, 52), (4096, 77),
]

def fit(points):
    """Least-squares slope of log2(w) vs log2(n); return (beta, se)."""
    xs = [math.log2(float(n)) for n, _ in points]
    ys = [math.log2(float(w)) for _, w in points]
    k = len(points)
    mx = sum(xs) / k
    my = sum(ys) / k
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    beta = sxy / sxx
    sse = sum((y - my - beta * (x - mx)) ** 2 for x, y in zip(xs, ys))
    se2 = sse / sxx / (k - 2) if k > 2 else float('nan')
    return beta, math.sqrt(se2) if k > 2 else float('nan'), sse

print("Per-doubling slope d log2 w / d log2 n (all adjacent pairs):")
prev = None
slopes = []
for n, w in DATA:
    if prev is not None:
        pn, pw = prev
        if n == 2 * pn:
            s = (math.log2(w) - math.log2(pw)) / (math.log2(n) - math.log2(pn))
            slopes.append((n, round(s, 3)))
    prev = (n, w)
for n, s in slopes:
    print(f"  -> n={n:5d}  slope={s:.3f}")
print("slopes:", [s for _, s in slopes])

print("\nLeast-squares fit  log2 w* = a + beta*log2 n  over tails:")
for lo, hi, label in [
    (16, 4096, "n in 16..4096 (pure doublings)"),
    (64, 4096, "n in 64..4096"),
    (128, 4096, "n in 128..4096"),
    (256, 4096, "n in 256..4096"),
    (512, 4096, "n in 512..4096"),
]:
    pts = [(n, w) for n, w in DATA if lo <= n <= hi]
    b, se, sse = fit(pts)
    print(f"  {label:30s} beta={b:.4f}  se={se:.4f}  sse={sse:.3f}")

b, se, _ = fit([(n, w) for n, w in DATA if 64 <= n <= 4096])
print(f"\nBest (64..4096): beta = {b:.4f} +/- {se:.4f}")

cand = {"1/2": 0.5, "log4(3)": math.log(3) / math.log(4)}
for name, v in cand.items():
    print(f"  candidate {name} = {v:.4f}: |beta-v| = {abs(b-v):.4f}")
print("No candidate matches beta to within 3*se; exponent is fitted, not a closed form.")
