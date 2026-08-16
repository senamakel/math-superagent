#!/usr/bin/env python3
"""Control: is the mean-reverting sqrt(n) S-structure prime-specific or
fold-generic? Run the same S/D analysis on (a) random iid h (balanced p=0.5),
(b) a balanced Bernoulli(p=0.5855) surrogate matching the prime 1-density.

If random input shows the same |S|=O(sqrt n) and the same lag-1 anti-correlation
in D, then this is a fold-generic fact and NOT an arithmetic input to SUPPLY
(consistent with the pattern-finder final report). If it differs, that is a
genuine arithmetic signal.

Uses the canonical fold oracle (s_sos) — no new nu2 implementation.
"""
import sys, math, time, random
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def S_of_h(N, h):
    S = {}
    for n in range(2, N + 1):
        ns, ones = s_sos(n, h)
        S[n] = ns
    return S


def stats(S, N):
    ns = list(range(50, N + 1))
    maxratio = max(abs(S[n]) / math.sqrt(n) for n in ns)
    maxn = max(abs(S[n]) / n for n in ns)
    D = {n: S[n + 1] - S[n] for n in range(2, N)}
    ds = list(D.values())
    mean = sum(ds) / len(ds)
    var = sum((d - mean) ** 2 for d in ds) / len(ds)
    std = math.sqrt(var)
    m = mean
    den = sum((D[n] - m) ** 2 for n in range(2, N))
    acf1 = sum((D[n] - m) * (D[n + 1] - m) for n in range(2, N - 1)) / den
    return maxratio, maxn, std, acf1


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    assert_supply_guard(4000)
    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    mr, mn, ds, a1 = stats(SP, N)
    print(f"PRIMES N={N}: max|S|/sqrt n={mr:.3f} max|S|/n={mn:.4f} "
          f"std(D)={ds:.2f} ACF1(D)={a1:+.3f}")

    random.seed(seed)
    for label, p in [("iid p=0.5", 0.5)]:
        h = [1 if random.random() < p else 0 for _ in range(N + 1)]
        S = S_of_h(N, h)
        mr, mn, ds, a1 = stats(S, N)
        print(f"{label} N={N}: max|S|/sqrt n={mr:.3f} max|S|/n={mn:.4f} "
              f"std(D)={ds:.2f} ACF1(D)={a1:+.3f}")


if __name__ == "__main__":
    main()
