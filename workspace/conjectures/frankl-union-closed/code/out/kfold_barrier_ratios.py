"""Verify the k-fold iid-OR crossover and barrier facts numerically.

R_k(p) = h(1-(1-p)^k)/h(p).  h(a)=h(b) <=> a=b or a=1-b, so the nontrivial
crossover of R_k=1 is at c_k solving (1-p)^k = p, i.e. 1-(1-p)^k = 1-p.

We check numerically:
  (A) R_k(c_k) = 1 exactly (crossover).
  (B) R_k(p) >= 1 on [0, c_k] for a fine grid (supporting evidence per k).
  (C) c_k strictly decreasing in k (already proved; independent numeric check).
All numerical (high precision); no exact claims beyond the k=2 algebraic value.
"""
import mpmath as mp
mp.mp.dps = 40


def h(x):
    if x <= 0 or x >= 1:
        return mp.mpf(0)
    return -x*mp.log(x) - (1-x)*mp.log(1-x)


def c_k(k):
    f = lambda x: (1-x)**k - x
    return mp.findroot(f, (mp.mpf(0), mp.mpf(1)))


for k in [2, 3, 4, 5, 10, 20]:
    c = c_k(k)
    R = h(1 - (1-c)**k)/h(c)
    # grid check of R(p)-1 on [0,c]
    N = 4000
    worst = mp.mpf(10)
    for i in range(1, N):
        p = c*i/N
        r = h(1-(1-p)**k) - h(p)     # sign of (R-1); compare entropies
        if r < worst:
            worst = r
    print(f"k={k:3}: c_k={mp.nstr(c,12)}  R(c_k)={mp.nstr(R,10)}  "
          f"min[R(p)-1]*sign on grid = {mp.nstr(worst,8)}")
