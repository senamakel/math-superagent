#!/usr/bin/env python3
"""Corrected effective-sample test: actual variance of sliding-window means of
the nu2/n residual sequence vs naive var/M. If consecutive residuals were
independent, var(mean of window size M) = var/M. If they are positively
autocorrelated over lags ~ L, the effective count is M/(2L-ish) and the ratio
var(mean)*M/var exceeds 1 by that factor. This ratio is a direct probe of
whether the Chebyshev lower-tail estimate of the averaged form (GOAL priority
1) has real teeth at these finite sizes.
"""
import sys
from lib.primes import primes_upto_index
from lib.supply_fold import s_sos

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
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
    print(f"N={N}  mean={m:.5f}  var={var:.6e}")
    print("actual variance of sliding-window means (independence inflator):")
    for M in [200, 500, 1000]:
        # sliding windows over dev
        wins = [sum(dev[i:i+M])/M for i in range(0, len(dev)-M, M//2)]
        # variance of these window means
        wm = sum(wins)/len(wins)
        wvar = sum((w-wm)**2 for w in wins)/len(wins)
        infl = wvar*M/var
        print(f"  M={M:5d}: nwindows={len(wins):5d}  var(mean)={wvar:.3e}  inflator*var/M = {infl:.3f}x")
        # inferred effective sample ~ M/infl
        print(f"          effective sample ~ {M/infl:7.1f}")

if __name__ == "__main__":
    main()
