"""PE1006: S1 within-run left-append conjecture.

Conjecture: on each constant-V run [a, b] (b-a+1 in {2,3}):
  S1(a+1) == d * 10^{len(S1(a))} + S1(a)   for some single digit d (0..9),
  and S1(k) == S1(a+1) for all k in [a+1, b].
I.e. S1(k) has the constant suffix S1(a) after a left-append of one digit,
then is flat for the rest of the run.

We also test: d == the leading letter / first bit that distinguishes
consecutive right-special factors, and record d's value per run for
run-pattern analysis.

All exact integer arithmetic; loads s1_exact.txt / vR_exact.txt (KMAX=3000).
"""
KMAX = 3000

S1 = [0] * (KMAX + 1)
V = [0] * (KMAX + 1)
with open('code/out/s1_exact.txt') as fh:
    for line in fh:
        k, v = line.split()
        S1[int(k)] = int(v)
with open('code/out/vR_exact.txt') as fh:
    for line in fh:
        k, v = line.split()
        V[int(k)] = int(v)

runs = []
start, v0 = 1, V[1]
for k in range(2, KMAX + 1):
    if V[k] != v0:
        runs.append((start, k - 1, v0))
        start, v0 = k, V[k]
runs.append((start, KMAX, v0))

n_ok = 0
n_bad = 0
n_flatlen2 = n_flatlen3 = 0
first_bad = None
d_vals = {}      # d -> count
for (a, b, v) in runs[1:]:
    L = b - a + 1
    if L == 1:
        continue   # artificial truncation singleton at KMAX
    if L == 2:
        # S1(a), S1(a+1): check left-append then nothing to be flat
        x = S1[a]
        y = S1[a + 1]
        lens = len(str(x))
        for d in range(10):
            if y == d * (10 ** lens) + x:
                d_vals[d] = d_vals.get(d, 0) + 1
                n_ok += 1
                break
        else:
            n_bad += 1
            if first_bad is None:
                first_bad = (a, L, x, y)
        n_flatlen2 += 1
    else:
        x = S1[a]
        y = S1[a + 1]
        z = S1[a + 2]
        lens = len(str(x))
        for d in range(10):
            if y == d * (10 ** lens) + x:
                d_vals[d] = d_vals.get(d, 0) + 1
                n_ok += 1
                break
        else:
            n_bad += 1
            if first_bad is None:
                first_bad = (a, L, x, y)
        if z != y:
            n_flatlen3 += 1
        n_flatlen3 += 0
        if z != y:
            n_bad += 1
            if first_bad is None:
                first_bad = (a, L, y, z)

print("runs tested (excl k=1 singleton):", len(runs) - 1)
print("left-append holds (y = d*10^len + x):", n_ok)
print("left-append fails:", n_bad)
print("length-3 runs with S1 not flat on 3rd position:", n_flatlen3)
print("first_bad:", first_bad)
print("d distribution (left-appended leading digit), counts:", dict(sorted(d_vals.items())))

# cross correlation: d vs V (right-special value at run start) - is d the first
# bit of V's overflowing prefix? try: d == floor(V / 10^(len(V)-1))? no.
# Try correlating d with run length and with membership of a in Fibonacci-ish.
# Just report d sequence for the first 40 runs.
print()
print("first 40 runs: (j, s=V-run start, V, S1(a), d):")
runs2 = runs[1:]
for j in range(1, min(len(runs2), 40) + 1):
    a, b, v = runs2[j - 1]
    x = S1[a]
    y = S1[a + 1]
    lens = len(str(x))
    d = -1
    for dd in range(10):
        if y == dd * (10 ** lens) + x:
            d = dd
            break
    print(f"  j={j:4d} s={a:5d} V={v} S1a={x} d={d}")
