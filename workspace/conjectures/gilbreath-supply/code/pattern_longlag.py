#!/usr/bin/env python3
"""Long-lag autocorrelation of the nu2/n residual. Determines whether the
wandering is finite-correlation-length noise (rho(k) dies after some lag) or
long-range dependence (rho(k) ~ k^-alpha, 1/f-like). This decides how many
effective independent blocks the tail/Cesaro estimate has, hence the strength
of the averaged-form Chebyshev argument.
"""
import sys
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    ps = primes_upto_index(N + 2)
    h = [((ps[j+1]-ps[j])//2) % 2 for j in range(N+1)]
    nu = [0]*(N+1)
    for n in range(2, N+1):
        _, ones = s_sos(n, h[:n])
        nu[n] = ones
    r = [nu[n]/n for n in range(2, N+1)]
    m = sum(r)/len(r)
    dev = [x-m for x in r]
    var = sum(x*x for x in dev)/len(dev)
    L = len(dev)
    print(f"N={N} L={L} var={var:.5e}")
    print("lag    rho(k)    cumulative sum of rho (correlation length proxy)")
    cum=0.0
    for k in range(1, 61):
        num = sum(dev[i]*dev[i+k] for i in range(L-k))
        rk = num/var/L   # /L: (L-k)/L ~ 1
        cum += rk
        if k in [1,2,3,5,8,13,21,34,55,60] or k%10==0:
            print(f"  {k:4d}  {rk:+.4f}   {cum:8.3f}")
    print(f"\ncorrelation time tau ~ 1 + 2*sum_{k>=1} rho(k)  (sum to 60 here, tail-ignored)")
    print(f"  tau(60) = {1+2*cum:.2f}")

if __name__ == "__main__":
    main()
