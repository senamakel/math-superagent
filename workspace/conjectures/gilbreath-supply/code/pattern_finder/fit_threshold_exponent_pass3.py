"""Fit the exponent of the exact-mean linear-supply threshold weight (pass 3).

Data: exact-mean threshold weight w*(n) = min w with mean_n(w) >= 0.40 over
weight-w binary strings in F2^n. Every per-n w* is an EXACT value from the
verified threshold formula (see code/out/threshold_limit_exact.txt PART A,
code/out/threshold_exact_mean_independent.txt PART 3; small-n 10/12/14/16
from code/out/linear_supply_by_weight.txt PART 1 exhaustive).

    n  :  8  10  12  14  16  32  64  128 256 512 1024 2048 4096 8192 16384 32768
    w* :  3   3   3   4   3   5   7  11  16  24   35   52   77  112   164   239

Task: (1) OLS fit of log2(w*) vs log2(n) over the tail n>=256, with a standard
error on the slope; report per-doubling slope log2(w(2n)/w(n)) for each
consecutive power-of-two pair. (2) Test the fitted exponent E against the
candidates log_4(3)=0.7925 and 1/2; report |E - each|. (3) State plainly that E
is a FITTED value, not a closed form. (4) File the claim block. (5) Post it.

Exact integer/Fraction data; only the log/regression arithmetic is float.
This is a measurement (numerical fit), NOT a proof: the LIMIT of theta=w*/n
and the exponent are fitted; the per-n values are exact.
"""
import math

# (n, w*) — every value exact from the verified formula.
NS = [8, 10, 12, 14, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
WS = [3, 3, 3, 4, 3, 5, 7, 11, 16, 24, 35, 52, 77, 112, 164, 239]


def ols_fit(xs, ys):
    """OLS slope + intercept of y = a + b*x. Returns (b, se_b, a, sse)."""
    k = len(xs)
    mx = sum(xs) / k
    my = sum(ys) / k
    sxx = sum((x - mx) ** 2 for x in xs)
    sxy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    b = sxy / sxx
    a = my - b * mx
    sse = sum((y - (a + b * x)) ** 2 for x, y in zip(xs, ys))
    se_b = math.sqrt(sse / sxx / (k - 2)) if k > 2 else float('nan')
    return b, se_b, a, sse


lines = []
lines.append("sequence = exact-mean threshold weight w*(n) over weight-w strings in F2^n")
lines.append("oracle   = verified threshold formula P_d(w) (cross-checked vs s_sos brute);")
lines.append("           per-n w* EXACT, see threshold_limit_exact.txt / threshold_exact_mean_independent.txt")
lines.append("range    = n in {8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768}")
lines.append("=" * 78)
lines.append(f"n-list: {NS}")
lines.append(f"w*    : {WS}")
lines.append("")

# ---- per-doubling slopes (consecutive power-of-two pairs) ----
lines.append("per-doubling slope  s = log2(w*(2n)/w*(n)) = d log2 w / d log2 n  (doubling pairs only):")
for (pn, pw), (n, w) in zip(zip(NS, WS), zip(NS[1:], WS[1:])):
    if n == 2 * pn:
        s = (math.log2(w) - math.log2(pw)) / (math.log2(n) - math.log2(pn))
        lines.append(f"  n={pn:6d} -> {n:6d}:  slope={s:.4f}")
lines.append("")

# ---- OLS fits over various tails ----
lines.append("OLS fit  log2(w*) = a + E*log2(n)   (E = exponent, se = standard error):")
for lo, label in [
    (256, "n>=256  (task tail)"),
    (128, "n>=128"),
    (64, "n>=64"),
    (512, "n>=512"),
    (16, "all n>=16"),
]:
    pts = [(n, w) for n, w in zip(NS, WS) if n >= lo]
    xs = [math.log2(n) for n, _ in pts]
    ys = [math.log2(w) for _, w in pts]
    b, se, a, sse = ols_fit(xs, ys)
    lines.append(f"  {label:16s}  E={b:.5f}  se={se:.5f}  a={a:.4f}  sse={sse:.4f}  npts={len(pts)}")
lines.append("")

# ---- task tail n>=256 ----
tail = [(n, w) for n, w in zip(NS, WS) if n >= 256]
xs = [math.log2(n) for n, _ in tail]
ys = [math.log2(w) for _, w in tail]
E, se, a, sse = ols_fit(xs, ys)
lines.append(f"TASK TAIL n>=256:  E = {E:.5f} +/- {se:.5f}   (log2 w* = {a:.4f} + {E:.5f} * log2 n)")
lines.append("")

# ---- test against candidates ----
lines.append("candidate closed forms:")
for name, v in [("1/2", 0.5), ("log_4(3)=0.7925", math.log(3) / math.log(4)), ("2/3", 2 / 3)]:
    lines.append(f"  {name:18s}   |E - {v:.4f}| = {abs(E - v):.4f}")
lines.append("")
lines.append("PLAIN STATEMENT: E is a FITTED value (numerical regression over the sampled")
lines.append("n-list), NOT a closed form.  It sits between n^1/2 and n^log_4(3) and is not")
lines.append("equal to either:  E ~ %.4f is sublinear (~n^%.2f), so linear supply is typical"
                % (E, E))
lines.append("once the switch weight exceeds ~n^%.2f — strictly weaker than a positive fraction" % E)
lines.append("(n^1) of on-bits, and the arithmetic demand on the primes is sublinear.")
lines.append("")
lines.append("theta = w*/n at each n (exact per-n; the LIMIT is fitted, not proved):")
for n, w in zip(NS, WS):
    lines.append(f"  n={n:6d}  w*={w:4d}  theta={w / n:.6f}")
lines.append("")
lines.append("MEASURED, NOT PROVED: per-n w* are exact; the sublinear exponent and the")
lines.append("tend-to-zero limit are fitted from the data, not a theorem.")

txt = "\n".join(lines) + "\n"
print(txt)
