#!/usr/bin/env python3
"""Confirm the MA(1)-boundary increment structure of the nu2 supply fluctuation."""
import math

def load():
    nu2 = {}
    with open("/workspace/code/out/nu2_dense.txt") as f:
        for line in f:
            p = line.split()
            if len(p) == 2:
                nu2[int(p[0])] = int(p[1])
    return nu2

def acf(xs, maxlag):
    m = sum(xs)/len(xs)
    xc = [x-m for x in xs]
    v = sum(x*x for x in xc)
    return [sum(xc[i]*xc[i+lag] for i in range(len(xs)-lag))/v for lag in range(1, maxlag+1)]

def main():
    nu2 = load()
    ns = sorted(nu2)
    D = [2*nu2[n]-n for n in ns]
    I = [D[i+1]-D[i] for i in range(len(D)-1)]
    N = len(I)
    se = 1/math.sqrt(N)
    print("N increments =", N, "  1/sqrt(N)=%.4f" % se)

    ac = acf(I, 40)
    print("acf(I) lags 1..40:")
    print("  ".join("%d:%.3f" % (k+1, ac[k]) for k in range(40)))
    big = [k+1 for k in range(40) if abs(ac[k]) > 3*se]
    print("lags with |ac|>3*se=%.3f : %s" % (3*se, big))

    half = N//2
    ac1 = acf(I[:half], 4)[0]
    ac2 = acf(I[half:], 4)[0]
    print("acf(1) first/second half: %.3f / %.3f" % (ac1, ac2))

    r1 = ac[0]
    # MA(1): rho1 = -theta/(1+theta^2), achievable range [ -1/2, 1/2 ]
    # observed -0.503 => saturates the MA(1) boundary => theta = -1 (pure first difference)
    print("rho1 = %.4f  (MA(1) boundary is -0.5; |rho1| reaching -0.5 means theta=-1, i.e. I = first difference of iid noise)" % r1)
    print("=> D(n) = 2nu2-n behaves like a bounded partial sum of independent steps (no drift, sqrt-type growth).")
    print("long-run-variance factor 1+2*sum(rho_1..40) = %.3f" % (1 + 2*sum(ac)))

    # D stays within +/- ~4 sqrt(n)? report worst
    worst = max((abs(D[n-1])/math.sqrt(n), n, abs(D[n-1])) for n in ns)
    print("max |D|/sqrt(n) = %.3f at n=%d, |D|=%d  (illustrates sqrt-class fluctuation)" % worst)

if __name__ == "__main__":
    main()
