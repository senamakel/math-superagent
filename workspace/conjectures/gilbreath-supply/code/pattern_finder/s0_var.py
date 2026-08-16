#!/usr/bin/env python3
"""Is E[S_0^2]/n bounded for the primes (condition (A) at the dominant scale)?

S_0(n) = sum over d with trailing_ones(d)=0 of (-1)^{T(n,d)}  (adjacent-pair scale).
If E[S_0^2]/n is bounded like the total E[S^2]/n, condition (A) holds at the
dominant scale.  Measure mean S_0^2/n and max S_0^2/n over a wide n-range.
"""
import json
from lib.primes import h_string


def trailing_ones(d):
    k = 0
    while d & 1:
        k += 1
        d >>= 1
    return k


def main():
    N = 9000
    h = h_string(N + 1)
    # windows
    means0 = 0.0
    maxs0 = 0.0
    argmax = 0
    ncnt = 0
    wmin, wmax = 800, N
    for n in range(wmin, wmax, 200):
        S0 = 0
        Stot = 0
        for d in range(2, n):
            g = trailing_ones(d)
            x = 0
            o = d
            base = n - 1 - d
            while True:
                x ^= h[base + o]
                if o == 0:
                    break
                o = (o - 1) & d
            s = 1 if x == 0 else -1
            if g == 0:
                S0 += s
            Stot += s
        r0 = S0 * S0 / n
        rtot = Stot * Stot / n
        means0 += r0
        if r0 > maxs0:
            maxs0 = r0
            argmax = n
        ncnt += 1
    print(f"n={wmin}..{wmax} step200: {ncnt} windows")
    print(f"mean S_0^2/n = {means0/ncnt:.4f}")
    print(f"max  S_0^2/n = {maxs0:.4f} at n={argmax}")
    print(f"(total E[S^2]/n was ~0.9-1.3; g=0 holds ~half of it)")


if __name__ == "__main__":
    main()
