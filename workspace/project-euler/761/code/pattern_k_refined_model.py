#!/usr/bin/env python3
"""Test K(n) = floor(c*n + k/n) model, k = 1/(3*(1+c)), c = root of tan(c*pi)=pi*(c+1).

Derivation (first-order asymptotics of the root r(n) of
tan(r*pi/n) = (r+n)*tan(pi/n)):
  With r = c*n + delta, tan(c*pi + delta*pi/n) = T + (delta*pi/n)(1+T^2) + ...,
  (c*n+delta+n)*tan(pi/n) = T + delta*pi/n + pi^3*(1+c)/(3*n^2) + ...
  => delta*pi*T^2/n = pi^3*(1+c)/(3n^2)  =>  delta = 1/(3*n*(1+c)).
So K(n) = floor(r(n)) is conjectured == floor(c*n + k/n), k = 1/(3*(1+c)).

This corrects the two known failures of the plain floor(c*n) model
(at n=165 and n=3809 the +k/n term pushes r just over an integer).
Checks:
 1. exact k vs numerical limit of n*(r-cn).
 2. K(n) == floor(cn+k/n) over n in [3, 120000], first failure.
 3. exact sympy cross-check at failure candidates and a sample.
"""
import mpmath as mp
mp.mp.dps = 50

def root_n(n):
    th = mp.pi / n
    t = mp.tan(th)
    def f(x): return mp.tan(x*th) - (x+n)*t
    lo, hi = mp.mpf(1), mp.mpf(n)/2 - mp.mpf('1e-30')
    for _ in range(300):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    return (lo+hi)/2

def K_mp(n):
    return int(mp.floor(root_n(n)))

c = mp.findroot(lambda x: mp.tan(x*mp.pi) - mp.pi*(x+1), 0.43)
k = 1/(3*(1+c))
print("c =", mp.nstr(c, 25))
print("k = 1/(3(1+c)) =", mp.nstr(k, 25))

# 1. numeric limit
print("\nn*(r-cn) ->")
for n in [1000, 10000, 100000, 500000]:
    print("  n=%6d: %.10f" % (n, (root_n(n) - c*n)*n))

# 2. model test
fails = []
worst = 0
NMAX = 120000
for n in range(3, NMAX+1):
    K = K_mp(n)
    model = int(mp.floor(c*n + k/n))
    if K != model:
        fails.append((n, K, model))
        if len(fails) >= 20:
            break
print("\nK(n) vs floor(cn+k/n), n in [3,%d]:" % NMAX)
print("  first failures:", fails if fails else "NONE")

# extra check: what about floor(cn + k/n + 0.5)? and the old model's failure count for comparison
old_fails = 0
for n in range(3, min(NMAX, 20000)+1):
    if K_mp(n) != int(mp.floor(c*n)):
        old_fails += 1
print("  floor(cn) model failures in [3,20000]:", old_fails)

# 3. exact sympy cross-check at the old boundary cases and near misses
import sympy as sp
def K_exact(n):
    th = sp.pi / n
    tan_th = sp.tan(th)
    best = 0
    for k in range(0, n):
        if sp.sin(k*th) - (k+n)*tan_th*sp.cos(k*th) < 0:
            best = k
    return best

print("\nexact sympy cross-check:")
for n in [86, 165, 667, 1248, 3809, 9000]:
    e, m = K_exact(n), K_mp(n)
    print("  n=%5d exact=%3d mpmath=%3d %s" % (n, e, m, "OK" if e == m else "MISMATCH"))