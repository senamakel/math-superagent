#!/usr/bin/env python3
"""Structure of d(n) = K(n) - floor(3n/7).

Hypothesis (from data up to n=600): d(n) in {0,1} for n <= N0 (N0 ~ 1150),
and within that range, {n : d(n)=1} = union over residue classes r mod 7 of
  { n : n ≡ r (mod 7), n >= T_r }
with thresholds in the sweep order r = 2,4,6,1,3,5,0.

Verify exactly up to n=600 (sympy exact), and also find the FIRST n where
d(n) = 2 (the falsifier of the {0,1} claim) using high-precision root
finding of tan(x*pi/n) = (x+n)*tan(pi/n), cross-checked against the exact
definition on a sample.
"""
import sympy as sp
import mpmath as mp

# ---------------- exact K(n) via sympy (small n) ----------------
def K_of_n_exact(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    best = 0
    for k in range(0, n):
        if sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th) < 0:
            best = k
    return best

# ---------------- high-precision K(n) via root bisection ----------------
def K_of_n_mp(n, dps=40):
    mp.mp.dps = dps
    th = mp.pi / n
    t = mp.tan(th)
    def f(x):
        return mp.tan(x*th) - (x+n)*t
    lo, hi = mp.mpf(1), mp.mpf(n)/2 - mp.mpf('1e-30')
    # f is increasing on [1, n/2) (tan increasing, -(x+n)t decreasing linear)
    assert f(lo) < 0 and f(hi) > 0
    for _ in range(200):
        mid = (lo+hi)/2
        if f(mid) > 0:
            hi = mid
        else:
            lo = mid
    r = (lo+hi)/2
    return int(mp.floor(r))

def d_of_n(n, K):
    return K - 3*n//7

# ---------- verify hypothesis exactly up to 600 ----------
N_EXACT = 600
Ks = [K_of_n_exact(n) for n in range(3, N_EXACT+1)]
ds = [d_of_n(n, K) for n, K in zip(range(3, N_EXACT+1), Ks)]
max_d = max(ds)
print("exact sympy: n=3..%d, max d = %d, d in {0,1}: %s" % (N_EXACT, max_d, set(ds) <= {0,1}))

# residue thresholds: for each r in 0..6, first n in [3,600] with n≡r and d=1
first_dev = {}
for r in range(7):
    for n in range(3, N_EXACT+1):
        if n % 7 == r and ds[n-3] == 1:
            first_dev[r] = n
            break
    else:
        first_dev[r] = None
print("first deviating n per residue mod 7:", first_dev)

# verify: for every n<=600, d(n)==1 iff n>=T_{n mod 7} (when T defined)
ok = True
for n in range(3, N_EXACT+1):
    r = n % 7
    T = first_dev[r]
    if T is None:
        if ds[n-3] != 0:
            ok = False; print("FAIL: no threshold for r=%d but d(%d)=%d" % (r, n, ds[n-3]))
    else:
        if (ds[n-3] == 1) != (n >= T):
            ok = False; print("FAIL at n=%d r=%d T=%d d=%d" % (n, r, T, ds[n-3]))
print("threshold structure holds exactly for n in [3,%d]: %s" % (N_EXACT, ok))

# ---------- find first n with d(n)=2 (falsifier of {0,1}) ----------
# cross-check mpmath K against exact sympy on n in 3..80 first
cks = [(n, K_of_n_exact(n), K_of_n_mp(n)) for n in range(3, 81)]
assert all(e == m for _, e, m in cks), [c for c in cks if c[1] != c[2]]
print("mpmath root K matches exact sympy K for n=3..80: True")

first2 = None
for n in range(3, 1600):
    if d_of_n(n, K_of_n_mp(n)) >= 2:
        first2 = n
        break
print("first n with d(n) >= 2:", first2)
if first2:
    for n in [first2-3, first2-1, first2, first2+1]:
        print("  n=%d K=%d floor(3n/7)=%d d=%d" % (n, K_of_n_mp(n), 3*n//7, d_of_n(n, K_of_n_mp(n))))