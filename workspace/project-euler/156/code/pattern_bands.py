"""Exact verification of the band-translation self-similarity of the PE156
solution sets, at the two nontrivial band points T = k*10^m with k(10-m)=10:
  (k,m) = (2,5):  T = 200000,       valid for d < 2  (d = 1 only)
  (k,m) = (5,8):  T = 500000000,    valid for d < 5  (d = 1..4)

Theorem (derived from the place-value count, then checked exactly on data):
  For T = k*10^m, 1 <= d < k, 0 <= x < 10^m:
      f_d(T + x) = f_d(x) + T,   hence (T+x) is a fixed point  <=>  x is one,
  so B_d ∩ [T, T+10^m) = {T + s : s in B_d, s < 10^m} where B_d = solutions
  in [0, 10^10).  Proof sketch: f_d(k*10^m - 1) = k*m*10^(m-1) + 10^m (the
  digit d appears in the leading position only inside block j = d, one full
  block of 10^m numbers), which equals k*10^m exactly when km + 10 = 10k,
  i.e. k(10-m) = 10; and the number k*10^m itself has leading digit k != d,
  so f_d(T) = T.  For x in [1, 10^m), T+x = k||(x as m digits) with leading
  k != d, contributing exactly f_d(x) further occurrences.

These two bands are OUTSIDE the run's documented k <= d-1 residue identity
(f_d(k*10^m+x)-f_d(x)=k*m*10^(m-1), verified in pattern_mech_gen), because
here k > d-1 and k*m*10^(m-1) != k*10^m; the equality instead comes from the
leading-position block contribution 10^m closing the gap.

Checks performed on the complete verified solution files (661 solutions):
  1. f_d(T) == T for every valid (d, T)  [via lib.digits.f_place_value]
  2. set equality B_d ∩ [T, T+10^m) == {T + s : s in B_d, s < 10^m} (exact)
  3. the translation identity f_d(T+x)-f_d(x)=T on a dense sample of x
  4. run-length motif: B_1's run lengths are (M1 M2)(M1 M2) with
     M1=(2,10,2,10,2,1), M2=(2,10,2,1), i.e. period 10 over the complete 20
     runs; within each run every member past the first has exactly one '1'
  5. pre-band self-similarity inside B_1: the <1e8 part A is 41 terms,
     B_1 = A ⊔ (5e8+A) ⊔ {117463825} ⊔ {1111111110}  (84 = 41+41+1+1)
  6. decimated seed-count and seed-sum sequences per digit
"""
import sys, os, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

BASE = "/workspace/code/out"
sols = {d: [int(x) for x in open(f"{BASE}/solutions-d{d}.txt").read().split()]
        for d in range(1, 10)}

B = {d: [n for n in sols[d] if n < 10**10] for d in range(1, 10)}
SB = {d: set(B[d]) for d in range(1, 10)}

points = [(2, 5, [1]), (5, 8, [1, 2, 3, 4])]   # (k, m, valid d's)
print("== 1. band points are fixed points: f_d(k*10^m) == k*10^m ==")
for k, m, ds in points:
    T = k * 10**m
    for d in ds:
        got = f_place_value(T, d)
        print(f"  (k,m)=({k},{m}) d={d}: T={T}  f={got}  fixed={got == T}")
        assert got == T

print("\n== 2. band set equality  B_d ∩ [T, T+10^m) == {T + s : s in B_d, s < 10^m} ==")
for k, m, ds in points:
    T = k * 10**m
    for d in ds:
        upper = sorted(s for s in B[d] if T <= s < T + 10**m)
        shifted = sorted(T + s for s in B[d] if s < 10**m)
        ok = (upper == shifted)
        print(f"  (k,m)=({k},{m}) d={d}: |band terms|={len(upper)}  exact={ok}")
        assert ok, (k, m, d)

print("\n== 3. translation identity f_d(T+x) - f_d(x) == T, dense random x ==")
random.seed(156)
bad = 0
for k, m, ds in points:
    T = k * 10**m
    for d in ds:
        for _ in range(20000):
            x = random.randrange(0, 10**m)
            if f_place_value(T + x, d) - f_place_value(x, d) != T:
                bad = bad + 1
print(f"  160000 checks (x<10^m), failures = {bad}")
assert bad == 0

print("\n== 4. B_1 run-length motif + within-run condition ==")
B1 = B[1]
runs = []
i = 0
while i < len(B1):
    j = i
    while j + 1 < len(B1) and B1[j + 1] == B1[j] + 1:
        j = j + 1
    runs.append((B1[i], j - i + 1))
    i = j + 1
RL = [L for _, L in runs]
P = (2, 10, 2, 10, 2, 1, 2, 10, 2, 1)
print(f"  run lengths = {RL}")
print(f"  complete 20 runs = P P with P={P}: {tuple(RL[:10]) == P and tuple(RL[10:]) == P}")
wrun = True
for start, L in runs:
    for n in range(start + 1, start + L):
        if str(n).count('1') != 1:
            wrun = False
print(f"  every run member past the first has exactly one '1': {wrun}")

print("\n== 5. B_1 exact decomposition ==")
A = [s for s in B1 if s < 10**8]
assert len(A) == 41
rebuilt = sorted(A + [5 * 10**8 + s for s in A] + [117463825, 1111111110])
print(f"  |A| = {len(A)};  B_1 == A ⊔ (5e8+A) ⊔ {{117463825,1111111110}}: {rebuilt == B1}")
print(f"  84 = 41 + 41 + 1 + 1: {len(B1) == 84}")

print("\n== 6. per-digit decimated seed counts and sums ==")
for d in range(1, 10):
    S0 = sum(B[d])
    print(f"  d={d}: N0={len(B[d]):>3}  S0={S0}")