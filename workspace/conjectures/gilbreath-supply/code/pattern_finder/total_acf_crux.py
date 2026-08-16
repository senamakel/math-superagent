#!/usr/bin/env python3
"""The crux: for the primes, var(S(n))/n ~ 0.8 while var(D) ~ 4000.  A
random 'independent increments' walk would give var(S)/n = var(D) ~ 4000.
The 5000x collapse is governed by the TOTAL autocorrelation of the increments:
    var(S(k))/k  ~  var(D) * (1 + 2 sum_{i=1}^{infty} r_i)
where r_i are the lag-i autocorrelations of D(n) = S(n+1)-S(n).

Measure (1 + 2*sum_{i>=1} r_i) = var(S)/ (k * var(D)) directly, and check
whether it is a stable small constant ~ 0.0002 (sum r_i ~ -1/2) — a Parseval
identity that would say the increments are 'almost exactly' anti-correlated
across all lags. Compare primes vs random vs Thue-Morse (which should NOT
have sum r_i ~ -1/2, since it diffuses).

CRUCIAL: collapse inputs have increments with a large MEAN (drift). For them
var(D) is computed about the mean, so mean-drift is hidden. Report the
increment mean separately.
"""
import sys, math, random, time
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def S_of_h(N, h):
    return {n: s_sos(n, h)[0] for n in range(2, N + 1)}


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    assert_supply_guard(4000)
    print(f"{'input':<22s} mean(D)  var(S)/var(D)  (1+2 sum r_i)  ACF1(D)  300-lag sum r_i")
    runs = []

    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    runs.append(("PRIMES", SP))

    random.seed(3)
    h = [1 if random.random() < 0.5 else 0 for _ in range(N + 1)]
    runs.append(("iid p=0.5", S_of_h(N, h)))

    # sparse single-1 (collapses: drift)
    h = [0] * (N + 1)
    h[N // 2] = 1
    runs.append(("single-1", S_of_h(N, h)))

    # thue-morse
    h = [bin(j).count('1') % 2 for j in range(N + 1)]
    runs.append(("Thue-Morse", S_of_h(N, h)))

    for label, S in runs:
        D = [S[n + 1] - S[n] for n in range(2, N)]
        mD = sum(D) / len(D)
        varD = sum((d - mD) ** 2 for d in D) / len(D)
        ns = list(range(50, N + 1))
        varS = sum(S[n] ** 2 for n in ns) / len(ns)
        nk = len(ns)          # ~N
        ratio = varS / nk / varD if varD else 0
        # lag-i autocorrelation of D (about mean)
        ac = []
        for i in range(1, 301):
            num = sum((D[j] - mD) * (D[j + i] - mD) for j in range(len(D) - i))
            den = sum((d - mD) ** 2 for d in D)
            ac.append(num / den if den else 0)
        acf1 = ac[0]
        sum300 = sum(ac)
        print(f"{label:<22s} {mD:8.3f}  {ratio:9.5f}   "
              f"{(1+2*sum300):9.5f}  {acf1:+8.3f}   {sum300:9.3f}")


if __name__ == "__main__":
    main()
