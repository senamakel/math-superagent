#!/usr/bin/env python3
"""Light refined K(n) model test over a smaller range + key boundary points."""
import mpmath as mp
mp.mp.dps = 40

def root_and_K(n):
    th = mp.pi / n; t = mp.tan(th)
    lo = mp.mpf(1); hi = mp.mpf(n)/2 - mp.mpf('1e-20')
    def f(x): return mp.tan(x*th) - (x+n)*t
    if f(lo) > 0: return None, 0
    for _ in range(260):
        mid = (lo+hi)/2
        if f(mid) > 0: hi = mid
        else: lo = mid
    r = (lo+hi)/2
    return r, int(mp.floor(r))

c = mp.findroot(lambda x: mp.tan(x*mp.pi) - mp.pi*(x+1), 0.43)
k = 1/(3*(1+c))
print("c=%.15f k=1/(3(1+c))=%.10f" % (float(c), float(k)))

# first failure over [3,8000]
fails = []
for n in range(3, 8001):
    r, K = root_and_K(n)
    model = int(mp.floor(c*n + k/n))
    if K != model:
        fails.append((n, K, model))
        if len(fails) >= 12:
            break
print("first failures in [3,8000]:")
for f in fails:
    print("   n=%d K=%d model=%d" % f)

# check the two old plain-floor(cn) failures are fixed by +k/n
print("\nboundary points (old floor(cn) failures 165, 3809):")
for n in [165, 3809, 667, 1248]:
    r, K = root_and_K(n)
    m_ref = int(mp.floor(c*n + k/n))
    m_plain = int(mp.floor(c*n))
    print(f"   n={n}: K={K}  refined={m_ref}  plain={m_plain}")
