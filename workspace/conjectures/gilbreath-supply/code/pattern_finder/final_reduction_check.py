#!/usr/bin/env python3
"""Final decisive measurements for the pattern-finder report:

(1) Confirm var(D) ~ O(N)  while  var(S) ~ O(N):  i.e. D has variance growing
    like N (std like sqrt(N)) but S's variance stays linear with small
    constant ~0.5.  This is the 'anti-correlated increments' engine.

(2) Verify the density-1 reduction:  given |S(n)| <= C*sqrt(n) for all n
    (a pointwise variance bound, fold-generic), the sample variance
    s2_N = var_{n<=N}( nu2(n)/n )  satisfies  s2_N = O(log N / N) -> 0.
    Check the analytic bound against the measured s2_N, and check the
    explicit inequality  sum (S(n)/(2n))^2 <= (C^2/4) * sum 1/n ~ (C^2/4)logN.
    This is what makes density-1 SUPPLY follow from the pointwise sqrt-n bound.

(3) Disentangle: does the prime mean(D) (drift) being ~0 track switch density
    or 1-density? (for the report's equivalence/weaker-input discussion)
"""
import sys, math, random
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    assert_supply_guard(4000)
    h = prime_h(N + 1)
    S = {n: s_sos(n, h)[0] for n in range(2, N + 1)}

    # (1) var(D) vs N and var(S) vs N scale
    print("var(D) and var(S) as N grows (primes):")
    for top in [2000, 4000, 8000, 12000, 16000, N]:
        if top > N: continue
        D = [S[n + 1] - S[n] for n in range(2, top)]
        varD = sum(d * d for d in D) / len(D)   # ~O(N): mean~0
        ns = range(50, top + 1)
        varS = sum(S[n] ** 2 for n in ns) / (len(list(ns)))
        print(f"  N={top:6d}: var(D)={varD:9.1f}   var(S)={varS:9.1f}   "
              f"var(D)/N={varD/top:.3f}   var(S)/N={varS/top:.4f}")

    # (2) density-1 reduction: s2_N = var of nu2/n over n<=N, and the
    #     analytic bound sum_{n<=N} (S(n)/(2n))^2  vs (C^2/4)*H_N
    print("\ndensity-1 reduction check (primes):")
    C = 3.8  # measured max |S|/sqrt(n) uniform bound
    for top in [2000, 4000, 8000, N]:
        if top > N: continue
        rs = [S[n] / (2 * n) for n in range(2, top + 1)]
        term_sum = sum(r * r for r in rs)
        harm = sum(1.0 / n for n in range(2, top + 1))
        bound = (C * C / 4.0) * harm
        # s2_N of nu2/n
        r2 = [ ( (n-2) - S[n] ) / (2 * n) for n in range(2, top + 1)]
        mu = sum(r2) / len(r2)
        s2 = sum((x - mu) ** 2 for x in r2) / len(r2)
        print(f"  N={top:6d}: sum(S/(2n))^2={term_sum:.4f}  "
              f"<= (C^2/4)H_N={bound:.4f}  |  s2_N(nu2/n)={s2:.3e}  "
              f"s2_N <= 2*sum/N ~ {2*term_sum/top:.3e}")

    # (3) drift vs densities
    h = prime_h(N + 1)
    ones = sum(h) / len(h)
    sw = sum(1 for j in range(len(h) - 1) if h[j] != h[j + 1]) / (len(h) - 1)
    D = [S[n + 1] - S[n] for n in range(2, N)]
    meanD = sum(D) / len(D)
    print(f"\nprimes: 1-dens={ones:.4f} switch-dens={sw:.4f} "
          f"mean(D)={meanD:+.4f} = S(N)/(N-2) check {S[N]/(N-2):+.4f}")


if __name__ == "__main__":
    main()
