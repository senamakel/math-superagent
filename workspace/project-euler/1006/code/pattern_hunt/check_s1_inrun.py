"""PE1006: within-run structure of S1(k) and V(R_k) corrections.

The k-step recurrence is Psi(k+1) = 100 Psi(k) + 100 V(R_k)^2 + 20 S1(k) + J(k),
with J(k)=1+floor((k+1)/phi^2).  Prior work established V(R_k) is constant on
Wythoff runs [floor(j phi^2), ...] (length 2 or 3).  We probe S1(k) inside each
run to see whether it has a clean closed form per run (toward a summable
O(log) correction).

All exact integer arithmetic.  Loads s1_exact.txt and vR_exact.txt
(k = 1..KMAX) which were produced by verify_R_runs_wythoff.py.
"""
import sys

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

# build V-runs
runs = []
start, v0 = 1, V[1]
for k in range(2, KMAX + 1):
    if V[k] != v0:
        runs.append((start, k - 1, v0))
        start, v0 = k, V[k]
runs.append((start, KMAX, v0))

# For each run, print S1 values and their successive ratios/differences pattern.
print("V-runs: (start, end, len, V) and the S1(k) values on the run")
print("Check: does S1(k+1) == 10*S1(k)+something within a run? does V relate?")
all_len2, all_len3 = 0, 0
len2_ok = len3_ok = 0
len2_bad = len3_bad = 0
# within-run affine probe: S1(k) - 10^... no, just record raw pattern
for (a, b, v) in runs[1:]:   # skip the singleton k=1 run
    L = b - a + 1
    vals = [S1[k] for k in range(a, b + 1)]
    if L == 2:
        all_len2 += 1
        # S1(a) and S1(a+1): is S1(a+1) == 100*?  decimal value S1(a) shifted?
        # base word has length a-?  Probe: relation of S1(k+1) to S1(k)
        # For a length-2 run, print when first few runs.
        if a <= 30:
            print(f"  len2 run s={a} V={v}: S1={vals}")
    else:
        all_len3 += 1
        if a <= 30:
            print(f"  len3 run s={a} V={v}: S1={vals}")

# Global probe: on runs, is S1(k) of the form (decimal) left-append of S1(a)?
# i.e. S1 within run = S1(a) * 10^{k-a} + correction?
print()
print("within-run probe A: for each run, S1(k) vs 10^{k-a}*S1(a)")
nz = 0
for (a, b, v) in runs[1:]:
    base = S1[a]
    for k in range(a + 1, b + 1):
        pred = base * (10 ** (k - a))
        if S1[k] != pred:
            # diff must be < 10^{k-a} then; measure "below-leading" structure
            nz += 1
print("  runs with S1(k) != 10^{k-a} S1(a) somewhere:", nz)

# probe B: growth ratio S1(k+1)/S1(k) within runs (decimal shift works only if S1(a) has no trailing issue)
print()
print("check: within a run, does S1(k+1) == 10*S1(k) exactly?")
count_10 = 0
count_not = 0
ex10 = []
for (a, b, v) in runs[1:]:
    for k in range(a, b):
        if S1[k + 1] == 10 * S1[k]:
            count_10 += 1
        else:
            count_not += 1
            if len(ex10) < 12:
                ex10.append((a, k, S1[k], S1[k + 1]))
print(f"  S1(k+1)==10*S1(k): {count_10},  not: {count_not}")
print("  first few non-10 pairs (runstart,k,S1k,S1k1):", ex10)
