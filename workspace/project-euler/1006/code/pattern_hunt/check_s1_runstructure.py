"""PE1006: exact S1(k) within-run structure — final verification.

Facts to establish exactly for k = 1..3000 (KMAX of the recorded data):

  (F1) S1 is constant on [s_j, s_j] (trivially) AND on [s_j + 1, s_{j+1} - 1]:
       i.e. within each V-run, S1 changes at most once, right after the start.
  (F2) hence exactly two maximal constant-S1 sub-runs per V-run:
       [s_j, s_j] and [s_j + 1, s_{j+1} - 1] (the second may be empty when
       run length is 1, which only happens at the truncation singleton).
  (F3) decimal length of S1(s_j) == s_j for every run start s_j.
  (F4) decimal length of S1(s_j + 1) == s_j + 1 when run length >= 2.
  (F5) delta_j := S1(s_j + 1) - S1(s_j) written out; report mod M, and
       attempt exact linear-recurrence detection on delta_j mod M later.

All exact integer arithmetic.  V-runs are computed from vR_exact.txt;
Wythoff starts s_j = floor(j*phi^2) are recomputed independently with
Decimal (500 digits) and cross-checked with the Beatty identity
s_j = j + floor(j*phi).
"""
from decimal import Decimal, getcontext

KMAX = 3000
S1 = [0] * (KMAX + 1)
V = [0] * (KMAX + 1)
for line in open('code/out/s1_exact.txt'):
    k, v = line.split()
    S1[int(k)] = int(v)
for line in open('code/out/vR_exact.txt'):
    k, v = line.split()
    V[int(k)] = int(v)

# V-runs
runs = []
start, v0 = 1, V[1]
for k in range(2, KMAX + 1):
    if V[k] != v0:
        runs.append((start, k - 1, v0))
        start, v0 = k, V[k]
runs.append((start, KMAX, v0))

# Wythoff starts, independent recomputation
getcontext().prec = 500
phi2 = (Decimal(3) + Decimal(5).sqrt()) / 2
phi = (Decimal(1) + Decimal(5).sqrt()) / 2
s = [0] + [int(Decimal(j) * phi2) for j in range(1, len(runs) + 1)]
# sanity: recompute once more via Beatty identity
s2 = [0] + [j + int(Decimal(j) * phi) for j in range(1, len(runs) + 1)]
assert s == s2, "Beatty identity check failed"

n_vruns = len(runs) - 1          # excluding the k=1 singleton
f1_ok = True
f3_ok = True
f4_ok = True
f3_bad = f4_bad = None
lens_s1a = []
for j in range(1, len(runs)):
    a, b, v = runs[j]
    assert a == s[j], (j, a, s[j])
    # (F1) constant on [a+1, b]
    if b >= a + 1:
        val = S1[a + 1]
        for k in range(a + 2, b + 1):
            if S1[k] != val:
                f1_ok = False
                break
    # (F3)
    if len(str(S1[a])) != a:
        f3_ok = False
        f3_bad = (j, a, len(str(S1[a])))
    # (F4)
    if b >= a + 1 and len(str(S1[a + 1])) != a + 1:
        f4_ok = False
        f4_bad = (j, a, len(str(S1[a + 1])))
    lens_s1a.append(len(str(S1[a])))

# count S1 maximal runs and their positions
s1runs = []
st, v0 = 1, S1[1]
for k in range(2, KMAX + 1):
    if S1[k] != v0:
        s1runs.append((st, k - 1))
        st, v0 = k, S1[k]
s1runs.append((st, KMAX))

print(f"V-runs (excl singleton): {n_vruns}, S1 maximal runs: {len(s1runs)}")
print(f"(F1) S1 constant on [s_j+1, s_{'{j+1}'}-1] of every run: {f1_ok}")
print(f"(F3) len(S1(s_j)) == s_j for all runs: {f3_ok}" + ("" if f3_ok else f" bad={f3_bad}"))
print(f"(F4) len(S1(s_j+1)) == s_j+1 (runs of len>=2): {f4_ok}" + ("" if f4_ok else f" bad={f4_bad}"))

# print S1-run structure for the first 15 runs to show the split at first position
print("\nfirst 12 runs: (s_j, s_{{j+1}}-1, S1 at start, S1 elsewhere)")
for j in range(1, 13):
    a, b, v = runs[j]
    print(f"  j={j:3d} [{a},{b}] S1(a)={S1[a]} S1(a+1..b)={S1[a + 1] if b >= a + 1 else '-'}")

# delta_j = S1(s_j+1) - S1(s_j), mod M, for linear-recurrence probing
M = 101001001
deltas = []
for j in range(1, len(runs)):
    a, b, v = runs[j]
    if b >= a + 1:
        deltas.append((S1[a + 1] - S1[a]) % M)
    else:
        deltas.append(None)
print("\ndelta_j mod M, j=1..40:")
print([d for d in deltas[:40]])
print("\nfirst 20 delta_j raw (not mod):")
raw = []
for j in range(1, len(runs)):
    a, b, v = runs[j]
    if b >= a + 1:
        raw.append(S1[a + 1] - S1[a])
for j in range(20):
    print(f"  j={j+1:3d} s={s[j+1]:4d} delta={raw[j]}")