#!/usr/bin/env python3
"""Corrected structural analysis of the mod-4 switch counts.

WINDOW FIX: the transfer quantity is w(n) = # { k in [3, n] : gap_k = 2 mod 4 }
= sum of switch bits over gaps g_3..g_n, matching the run's established
ancestor window (nu2_vs_gap_parity.py / nu2_structure_check.py: w(n) =
pref[n]-pref[2] with hbits[i] = bit of gap_{i+1}).  My first version used
gaps 2..n-1 (off by one on both ends); this version is corrected and its
E sequence is cross-checked byte-for-byte against the pre-existing
code/out/pattern_finder_outputs/excess_e_first512.txt (same window, written
by mod4_switch_majority_big.py).

Definitions (1-indexed primes p_1=2, p_2=3, ...):
  gap_k     = p_{k+1} - p_k
  h_k       = (gap_k // 2) % 2                  k >= 2
  w(n)      = sum_{k=3}^{n} h_k                 (n >= 2), w(2)=0
  e(n)      = 2*w(n) - (n-2)                    excess of switches over non-switches
  u_k       = +1 if p_k = 1 mod 4, else -1      (u_k = chi_4(p_k))
  identity  h_k = (1 - u_k u_{k+1})/2,  e(n) = -sum_{k=3}^{n} u_k u_{k+1}
  run form  e(n) = 2*R(n) - n  with R(n) = # maximal equal-residue runs
            among primes p_3..p_{n+1}           (both checked exactly)
"""
import time
from lib.gilbreath import primes_up_to

N = 1_000_000
SIEVE = 100_000_000

t0 = time.time()
P = primes_up_to(SIEVE)
print("sieve to %d : %d primes (%.1fs)" % (SIEVE, len(P), time.time() - t0))
assert len(P) >= N + 1

# u_k for k = 2..N+1
usign = {k: (1 if P[k - 1] % 4 == 1 else -1) for k in range(2, N + 2)}
assert all(v in (-1, 1) for v in usign.values())

# h_k for k = 2..N
h = {k: ((P[k] - P[k - 1]) // 2) % 2 for k in range(2, N + 1)}

# --- identity check 1: h_k = (1 - u_k u_{k+1})/2 ---
bad = 0
for k in range(2, N + 1):
    if h[k] != (1 - usign[k] * usign[k + 1]) // 2:
        bad += 1
        if bad < 5:
            print("ID FAIL k=%d gap=%d h=%d u=%d,%d" % (k, P[k] - P[k - 1], h[k], usign[k], usign[k + 1]))
print("identity h_k = (1 - u_k u_{k+1})/2 over k=2..%d: %s (bad=%d)" % (N, "OK" if bad == 0 else "FAIL", bad))

# --- w(n), e(n) over the CORRECT window k=3..n, with identity checks ---
w = [0] * (N + 1)
e = [0] * (N + 1)
runR = [0] * (N + 1)   # run count among p_3..p_{n+1}
sumUU = [0] * (N + 1)  # sum_{k=3}^{n} u_k u_{k+1}

sw = 0
se = 0
# runs among p_3..p_{n+1}: compute incrementally
def runcount_prefix(start, end_plus):  # primes p_start..p_end (indices start..end inclusive)
    pass

# incremental run count over primes p_3..p_{n+1}: track whether we're extending a run
# Simple approach: build run counts for prefixes of the u sequence starting at index 3.
us = [usign[k] for k in range(3, N + 2)]   # u_3..u_{N+1}
runs_pref = [0] * (len(us) + 1)            # runs_pref[m] = #runs in us[0..m-1]
runs_pref[1] = 1
for m in range(2, len(us) + 1):
    runs_pref[m] = runs_pref[m - 1] + (1 if us[m - 1] != us[m - 2] else 0)
# e(n) = 2*R(n) - n with R(n) = runs among p_3..p_{n+1} = us[0..n-2] -> runs_pref[n-1]

for n in range(2, N + 1):
    if n >= 3:
        sw += h[n]
        se += 2 * h[n] - 1
        sumUU[n] = sumUU[n - 1] + usign[n] * usign[n + 1]
    w[n] = sw
    e[n] = se
    runR[n] = runs_pref[n - 1] if n - 1 >= 1 else 0

badE = [n for n in range(2, N + 1) if e[n] != -sumUU[n]]
badR = [n for n in range(3, N + 1) if e[n] != 2 * runR[n] - n]
print("e(n) = -sum_{k=3}^{n} u_k u_{k+1} for n in [2,%d]: %s (bad=%s)" % (N, "OK" if not badE else "FAIL", badE[:3]))
print("e(n) = 2*R(n) - n (R = residue runs among p_3..p_{n+1}) for n in [3,%d]: %s (bad=%s)" % (N, "OK" if not badR else "FAIL", badR[:3]))

# --- cross-check against the pre-existing file (same window) ---
with open("code/out/pattern_finder_outputs/excess_e_first512.txt") as f:
    old = list(map(int, f.read().split()))
newE = [e[n] for n in range(2, 514)]
match = (old == newE)
print("cross-check vs excess_e_first512.txt (512 terms): %s" % ("IDENTICAL" if match else "DIFFER"))

# --- pointwise majority ---
viol = [n for n in range(2, N + 1) if e[n] < 0]
print("\n== pointwise switch majority e(n) >= 0 for n in [2,%d]: %s (violations=%d, first=%s)" %
      (N, "YES" if not viol else "NO", len(viol), viol[:5]))
zeros = [n for n in range(2, N + 1) if e[n] == 0]
print("   e(n)=0 at: %s (count=%d)" % (zeros[:10], len(zeros)))
for T in (17, 100, 1000, 10000, 100000):
    mn = min((e[n], n) for n in range(T, N + 1))
    print("   min e over n in [%6d, %d] = %d at n=%d" % (T, N, mn[0], mn[1]))

# --- dyadic table ---
import math
print("\n== dyadic table (w(n), e(n)) ==")
print("   n         w(n)      e(n)    w/n    e/(n/log(n*log n))")
for k in range(2, 7):
    n = 10 ** k
    ln = math.log(n * math.log(n))
    print("   %7d %9d %9d  %.4f  %.3f" % (n, w[n], e[n], w[n] / n, e[n] * ln / n))

# --- residue-run structure over p_3..p_{N+1} ---
from collections import Counter
runs = []
cur_len = 1
cur_val = P[3 - 1] % 4
for k in range(4, N + 2):
    v = P[k - 1] % 4
    if v == cur_val:
        cur_len += 1
    else:
        runs.append(cur_len)
        cur_len = 1
        cur_val = v
runs.append(cur_len)
cnt = Counter(runs)
L = sorted(runs, reverse=True)
print("\n== equal-residue run structure, residues of p_3..p_%d (n=%d) ==" % (N + 1, N))
print("   number of runs R(%d) = %d,  e(%d)=2R-n = %d (check vs above: e=%d)" %
      (N, len(runs), N, 2 * len(runs) - N, e[N]))
print("   longest run: %d   top-10: %s" % (L[0], L[:10]))
print("   run-length histogram top 8: %s" % dict(sorted(cnt.items(), reverse=True)[:8]))
print("   runs of length 1: %d (%.1f%%)" % (cnt.get(1, 0), 100.0 * cnt.get(1, 0) / len(runs)))
print("   mean run length: %.4f" % (N / len(runs)))

# --- E-walk step runs ---
down_runs = []
up_runs = []
curd = 0
curu = 0
for k in range(3, N + 1):
    if h[k] == 0:
        curd += 1
        if curu > 0:
            up_runs.append(curu)
            curu = 0
    else:
        curu += 1
        if curd > 0:
            down_runs.append(curd)
            curd = 0
if curd > 0:
    down_runs.append(curd)
if curu > 0:
    up_runs.append(curu)
print("\n== e-walk steps (gaps k=3..%d): +1 switch / -1 non-switch ==" % N)
print("   up steps %d, down steps %d, longest up-run %d, longest down-run %d" %
      (sum(up_runs), sum(down_runs), max(up_runs), max(down_runs)))
print("   down-run count %d, mean down-run %.3f" % (len(down_runs), sum(down_runs) / len(down_runs)))

# --- context: chi_4 balance ---
c1 = sum(1 for k in range(2, N + 2) if usign[k] == 1)
print("\n== context ==")
print("   p_k = 1 mod 4 among k in [2,%d]: %d ;  3 mod 4: %d ;  sum u = %d" %
      (N + 1, c1, N, c1 - N))

# --- transfer composition with stored nu2 (correct window) ---
print("\n== transfer composition (nu2 from code/out/nu2_dense.txt, w here = correct window) ==")
nu2 = {}
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        n, v = map(int, line.split())
        nu2[n] = v
viol_a = [n for n in range(17, 30001) if 2 * nu2[n] < w[n]]
print("   leg (a) nu2(n) >= w(n)/2 for n in [17,30000]: violations=%d first=%s" %
      (len(viol_a), viol_a[:5]))
if viol_a:
    print("   first violation ratio nu2/w = %.4f" % (nu2[viol_a[0]] / w[viol_a[0]]))
else:
    mn = min((nu2[n] / w[n], n) for n in range(17, 30001) if w[n] > 0)
    print("   min nu2/w over [17,30000] = %.4f at n=%d" % (mn[0], mn[1]))
viol_b = [n for n in range(2, 30001) if 2 * w[n] < n - 2]
print("   leg (b) w(n) >= (n-2)/2 for n in [2,30000]: violations=%d first=%s" % (len(viol_b), viol_b[:5]))
viol_c = [n for n in range(17, 30001) if 4 * nu2[n] < n - 2]
print("   composed nu2(n) >= (n-2)/4 for n in [17,30000]: violations=%d first=%s" % (len(viol_c), viol_c[:5]))
crossover = None
for n in range(2, 100):
    if (n - 2) > 4 * n ** 0.525:
        crossover = n
        break
print("   first n with (n-2)/4 > n^0.525: %d" % crossover)
if crossover:
    mm = min((nu2[n] / n ** 0.525, n) for n in range(max(crossover, 17), 30001))
    print("   min nu2/n^0.525 over n in [%d,30000] = %.3f at n=%d" % (max(crossover, 17), mm[0], mm[1]))
    margin = min((4.0 * nu2[n] / (n - 2), n) for n in range(max(crossover, 17), 30001))
    print("   min 4*nu2/(n-2) over n in [%d,30000] = %.4f at n=%d" % (max(crossover, 17), margin[0], margin[1]))

# --- write corrected sequences ---
with open("code/out/pattern_finder_outputs/e_ballot_corrected_first512.txt", "w") as f:
    f.write(" ".join(str(e[n]) for n in range(2, 514)))
with open("code/out/pattern_finder_outputs/w_switch_corrected_first512.txt", "w") as f:
    f.write(" ".join(str(w[n]) for n in range(2, 514)))
with open("code/out/pattern_finder_outputs/runs_residue_first512.txt", "w") as f:
    f.write(" ".join(str(runR[n]) for n in range(3, 515)))
print("\nwrote e_ballot_corrected_first512.txt, w_switch_corrected_first512.txt, runs_residue_first512.txt")
print("total time %.1fs" % (time.time() - t0))
