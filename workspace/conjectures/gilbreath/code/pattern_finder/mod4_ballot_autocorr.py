#!/usr/bin/env python3
"""Fresh, self-contained structural analysis of the mod-4 switch counts.

Everything is recomputed from the primes with EXPLICIT definitions; the only
external input is the sieve (lib.gilbreath.primes_up_to) and the stored
nu2_dense.txt (for the transfer bound), both previously verified by the run.

Definitions (1-indexed primes p_1=2, p_2=3, ...):
  gap_j     = p_{j+1} - p_j                       (even for j >= 2)
  h_j       = (gap_j // 2) % 2                    (j >= 2): h_j = 1 iff gap_j = 2 mod 4
  W(n)      = sum_{j=2}^{n-1} h_j                 (n >= 2), W(2) = 0
  E(n)      = 2*W(n) - (n-2)                      excess of switches over non-switches
  r_j       = p_j mod 4  in {1,3}  (j >= 2)
  u_j       = +1 if r_j = 1 else -1
  identity  h_j = (1 - u_j u_{j+1})/2   =>   E(n) = -sum_{j=2}^{n-1} u_j u_{j+1}
             (checked EXACTLY at every step in this program)

The pointwise majority statement is E(n) >= 0 for all n (ballot-path form:
E is a +1/-1 step walk that never goes below 0).  Verified to N=10^6 here.

Also: residue run structure (maximal strings of equal r_j), the E-walk step
runs, dyadic values of E and of the adjacent-product sum A(x) = -E(x), and
the transfer composition  nu2(n) >= W(n)/2  (n>=17) with  W(n) >= (n-2)/2
giving  nu2(n) >= (n-2)/4  on [17, 30000].

Exact integer arithmetic; O(N) memory; sieve 1e8 ~ 2s.
"""
import sys, time
from lib.gilbreath import primes_up_to

N = 1_000_000          # analyze W,E up to n = N
SIEVE = 100_000_000    # primes needed: index up to N+1

t0 = time.time()
P = primes_up_to(SIEVE)
print("sieve to %d : %d primes (%.1fs)" % (SIEVE, len(P), time.time() - t0))
assert len(P) >= N + 1, "need %d primes" % (N + 1)

# --- residues and signs of odd primes ---
r = [P[i] % 4 for i in range(1, N + 1)]        # r[0] = p_2 % 4, ..., r[N-1] = p_{N} % 4
u = [1 if v == 1 else -1 for v in r]           # u[0] corresponds to p_2
assert all(v in (1, 3) for v in r)

# --- switch bits h_j for j=2..N-1 (j is the GAP index; h_j = bit of gap_j) ---
# store h[j] in array indexed by j directly: h[j] for j in 2..N-1
h = {}
for j in range(2, N):                          # gap_j = p_{j+1} - p_j
    g = P[j + 1] - P[j]                        # P is 0-indexed: P[j+1] = p_{j+2}?? see below
    h[j] = (g // 2) % 2
# NOTE: P[k] = p_{k+1} (0-indexed list).  gap_j = p_{j+1} - p_j = P[j] - P[j-1].
# Correct that: recompute with P indices.
h = {}
for j in range(2, N):
    g = P[j] - P[j - 1]                        # p_{j+1} - p_j  (since P[j-1]=p_j, P[j]=p_{j+1})
    h[j] = (g // 2) % 2

# u_j for j>=2: u[j] with same j-indexing = sign of r_{p_j}. u_seq[j] = sign of p_j mod 4.
usign = {}
for j in range(2, N + 1):
    v = P[j - 1] % 4
    usign[j] = 1 if v == 1 else -1

# --- verify identity h_j = (1 - u_j u_{j+1})/2 for every j ---
bad = 0
for j in range(2, N):
    lhs = h[j]
    rhs = (1 - usign[j] * usign[j + 1]) // 2
    if lhs != rhs:
        bad += 1
        if bad < 5:
            print("IDENTITY FAIL j=%d gap=%d h=%d u=%d,%d rhs=%d" %
                  (j, P[j] - P[j - 1], lhs, usign[j], usign[j + 1], rhs))
print("identity h_j = (1 - u_j u_{j+1})/2 over j=2..%d: %s (bad=%d)" % (N - 1, "OK" if bad == 0 else "FAIL", bad))

# --- W, E with exact running computation and identity check ---
W = [0] * (N + 1)   # W[n]
E = [0] * (N + 1)   # E[n]
sumUU = [0] * (N + 1)  # sum_{j=2}^{n-1} u_j u_{j+1}
e = 0
s = 0
W[2] = 0
E[2] = 0
for n in range(2, N + 1):
    if n > 2:
        s += usign[n - 1] * usign[n]
        e += 2 * h[n - 1] - 1
    W[n] = (n - 2 + e) // 2   # from e = 2W - (n-2)
    E[n] = e
    sumUU[n] = s
    if n >= 2 and E[n] != -sumUU[n]:
        print("E!= -sumUU at n=%d: %d vs %d" % (n, E[n], -sumUU[n]))
        break
else:
    print("E(n) = -sum_{j=2}^{n-1} u_j u_{j+1} for all n in [2,%d]: OK" % N)

# --- pointwise majority check ---
viol = [n for n in range(2, N + 1) if E[n] < 0]
print("\n== pointwise switch majority E(n) >= 0 for n in [2,%d]: %s (violations=%d, first=%s)" %
      (N, "YES" if not viol else "NO", len(viol), viol[:5]))
z = [n for n in range(2, N + 1) if E[n] == 0]
print("   E(n)=0 exactly at n: %s (count=%d)" % (z[:10], len(z)))
for T in (17, 100, 1000, 10000, 100000):
    m = min(E[n] for n in range(T, N + 1))
    mn = min((E[n], n) for n in range(T, N + 1))[1]
    print("   min E over n in [%6d, %d] = %d at n=%d" % (T, N, m, mn))

# --- dyadic table: W(n), E(n), E(n)*log(n*log n)/n (LOS-type bias shape probe) ---
import math
print("\n== dyadic table ==")
print("   n         W(n)      E(n)    W/n     E/(n/log(n*log n))")
for k in range(2, 7):
    n = 10 ** k
    ln = math.log(n * math.log(n))
    print("   %7d %9d %9d  %.4f  %.3f" % (n, W[n], E[n], W[n] / n, E[n] * ln / n))

# --- residue run structure over p_2..p_{N+1} (N primes, indices j=2..N+1) ---
runs = []
cur_len = 1
cur_val = P[2 - 1] % 4   # p_2 % 4
for j in range(3, N + 2):
    v = P[j - 1] % 4
    if v == cur_val:
        cur_len += 1
    else:
        runs.append((cur_len, cur_val))
        cur_len = 1
        cur_val = v
runs.append((cur_len, cur_val))
L = sorted((l for l, v in runs), reverse=True)
from collections import Counter
cnt = Counter(l for l, v in runs)
print("\n== equal-residue run structure, residues of p_2..p_%d ==" % (N + 1))
print("   number of runs: %d (over %d primes)" % (len(runs), N))
print("   longest run: %d   top-10 lengths: %s" % (L[0], L[:10]))
print("   run-length histogram (top 8 by length): %s" % dict(sorted(cnt.items(), reverse=True)[:8]))
print("   runs of length 1: %d (%.1f%%)" % (cnt.get(1, 0), 100.0 * cnt.get(1, 0) / len(runs)))

# --- E-walk step structure: up step (h_j=1) / down step (h_j=0) ---
down_runs = []
up_runs = []
cur = 1
for j in range(3, N):
    if h[j] == 0:
        if j - 1 >= 2 and h[j - 1] == 0:
            cur += 1
        else:
            cur = 1
    # run tracking done properly below
down = []
curd = 0
curu = 0
for j in range(2, N):
    if h[j] == 0:
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
print("\n== E-walk steps (j=2..%d): +1 = switch (h=1), -1 = non-switch (h=0) ==" % (N - 1))
print("   up steps: %d   down steps: %d" % (sum(up_runs), sum(down_runs)))
print("   longest up-run (consecutive switches): %d" % max(up_runs))
print("   longest down-run (consecutive non-switches): %d" % max(down_runs))
print("   count of down-runs: %d, mean down-run: %.3f" % (len(down_runs), sum(down_runs) / len(down_runs)))

# --- Chebyshev-type sign balance for context ---
bal = sum(usign[j] for j in range(2, N + 1))
c1 = sum(1 for j in range(2, N + 1) if usign[j] == 1)
print("\n== context ==")
print("   # {p_j = 1 mod 4, j in [2,%d]} = %d   # {3 mod 4} = %d   sum u_j = %d" %
      (N, c1, N - c1, bal))

# --- transfer composition with stored nu2 ---
print("\n== transfer composition (nu2 from code/out/nu2_dense.txt, W computed here) ==")
nu2 = {}
with open("code/out/nu2_dense.txt") as f:
    for line in f:
        n, v = map(int, line.split())
        nu2[n] = v
assert W[17] * 1 == W[17]
viol_a = [n for n in range(17, 30001) if nu2[n] < W[n] // 2 + (W[n] % 2)]
# exact condition: nu2[n] >= W[n]/2  i.e. 2*nu2[n] >= W[n]
viol_a = [n for n in range(17, 30001) if 2 * nu2[n] < W[n]]
print("   leg (a) nu2(n) >= W(n)/2 for n in [17,30000]: violations=%d first=%s" %
      (len(viol_a), viol_a[:5]))
viol_b = [n for n in range(2, 30001) if 2 * W[n] < n - 2]
print("   leg (b) W(n) >= (n-2)/2 for n in [2,30000]: violations=%d first=%s" %
      (len(viol_b), viol_b[:5]))
viol_c = [n for n in range(17, 30001) if 4 * nu2[n] < n - 2]
print("   composed nu2(n) >= (n-2)/4 for n in [17,30000]: violations=%d first=%s" %
      (len(viol_c), viol_c[:5]))
# crossover where (n-2)/4 > n^0.525
crossover = None
for n in range(2, 100):
    if (n - 2) > 4 * n ** 0.525:
        crossover = n
        break
print("   first n with (n-2)/4 > n^0.525: %d" % crossover)
if crossover:
    m = min(4.0 * nu2[n] / (n - 2) for n in range(max(crossover, 17), 30001))
    mn = min(((4 * nu2[n]) / (n - 2), n) for n in range(max(crossover, 17), 30001))[1]
    print("   min 4*nu2/(n-2) over n in [%d,30000] = %.4f at n=%d (margin over 1)" %
          (max(crossover, 17), m, mn))
    mm = min((nu2[n] / n ** 0.525, n) for n in range(max(crossover, 17), 30001))
    print("   min nu2/n^0.525 over n in [%d,30000] = %.3f at n=%d" %
          (max(crossover, 17), mm[0], mm[1]))

# --- write sequences for the tools ---
with open("code/out/pattern_finder_outputs/E_ballot_first512.txt", "w") as f:
    f.write(" ".join(str(E[n]) for n in range(2, 514)))
with open("code/out/pattern_finder_outputs/W_switch_prefix_first512.txt", "w") as f:
    f.write(" ".join(str(W[n]) for n in range(2, 514)))
with open("code/out/pattern_finder_outputs/hbits_j2_first512.txt", "w") as f:
    f.write(" ".join(str(h[j]) for j in range(2, 514)))
print("\nwrote E_ballot_first512.txt, W_switch_prefix_first512.txt, hbits_j2_first512.txt (512 terms each)")
print("total time %.1fs" % (time.time() - t0))
