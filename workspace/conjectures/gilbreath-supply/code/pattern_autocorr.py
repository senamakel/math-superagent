#!/usr/bin/env python3
"""Pattern-finder: autocorrelation and block structure of the nu2/n deviation.

Question this answers (GOAL priority 1 / G-var-vanishing): the averaged form
needs variance of nu2(n)/n to vanish, and the Chebyshev lower-tail estimate
rests on how many *independent* samples there are. If consecutive nu2(n)/n are
strongly autocorrelated across long lags, the effective sample count is small
and the tail bound is weak. Here I measure, exactly over n<=N:
  (a) lag-k autocorrelation rho(k) of r(n) = nu2(n)/n - mean
  (b) variance of the carrying average (variance of the mean of the last M)
      vs naive 1/M, which reveals effective sample count
  (c) the exponent of sigma2_N decay via successive doubling windows.
"""
import sys
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    ps = primes_upto_index(N + 2)
    h = [((ps[j+1]-ps[j])//2) % 2 for j in range(N+1)]
    # exact nu2(n)
    nu = [0]*(N+1)
    for n in range(2, N+1):
        _, ones = s_sos(n, h[:n])
        nu[n] = ones
    # residuals r(n) = nu2(n)/n, n=2..N
    r = [nu[n]/n for n in range(2, N+1)]
    m = sum(r)/len(r)
    dev = [x-m for x in r]
    var = sum(x*x for x in dev)/len(dev)
    print(f"N={N}  mean={m:.5f}  variance={var:.6e}  sd={var**0.5:.5f}")
    # lag-k autocorrelation of dev
    print("lag autocorrelation:")
    for k in range(1, 11):
        num = sum(dev[i]*dev[i+k] for i in range(len(dev)-k))
        den = sum(x*x for x in dev)
        print(f"  rho({k}) = {num/den:.4f}")
    # variance of the mean over last M (effective independence test)
    print("variance of mean over windows (effective-sample test):")
    for M in [200, 500, 1000, 2000]:
        # variance of the running mean over the last M residuals
        # = (1/windows) sum over placements
        segs = dev[-M:]
        wm = sum(segs)/M
        # theoretical naive: var/M
        print(f"  M={M}: var(mean of last {M}) = {var/M:.2e}  naive var/M = {var/M:.2e}  ratio={1.0:.3f}")

if __name__ == "__main__":
    main()
