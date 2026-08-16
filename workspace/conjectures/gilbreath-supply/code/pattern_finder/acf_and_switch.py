#!/usr/bin/env python3
"""Two decisive questions:

(1) Is ACF1(D) ~ -1/2 an EXACT identity of the fold as N grows, or an
    asymptotic that drifts?  Track ACF1(D) over growing N for the primes.
    (If it settles at exactly -1/2 = 0.5000, it's a candidate identity; if it
    varies, it's noise.)

(2) THE central question: what is the increment mean mean(D) as a function of
    the switch density?  mean(D) = E[S(n+1)-S(n)].  If mean(D)~0 is
    EXACTLY equivalent to balanced switch density, then the fold extracts
    nothing new and SUPPLY stays equivalent to switch density (the negative
    theorem, goal 5).  Measure mean(D) and the local switch density of h.

Connects to: research/backward/switch-equivalence.md, thread switch-side-gap.
"""
import sys, math, random, time
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard
from lib.primes import h_string


def S_of_h(N, h):
    return {n: s_sos(n, h)[0] for n in range(2, N + 1)}


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    assert_supply_guard(4000)
    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)

    # (1) ACF1(D) vs N
    print("ACF1(D) as N grows (primes):")
    for top in [1000, 2000, 4000, 8000, 12000, 16000, N]:
        if top > N: continue
        D = [SP[n + 1] - SP[n] for n in range(2, top)]
        m = sum(D) / len(D)
        den = sum((d - m) ** 2 for d in D)
        a1 = (sum((D[i] - m) * (D[i + 1] - m) for i in range(len(D) - 1))
              / den) if den else 0
        print(f"  N={top:6d}: ACF1(D)={a1:+.4f}")

    # (1b) increment std vs N
    print("\nincrement mean and std vs N (primes):")
    for top in [1000, 2000, 4000, 8000, 12000, 16000, N]:
        if top > N: continue
        D = [SP[n + 1] - SP[n] for n in range(2, top)]
        m = sum(D) / len(D)
        std = math.sqrt(sum((d - m) ** 2 for d in D) / len(D))
        print(f"  N={top:6d}: mean(D)={m:+.4f}  std(D)={std:7.2f}  "
              f"std(D)/sqrt(N)={std/math.sqrt(top):.3f}")

    # (2) switch density of h vs mean(D)
    h = prime_h(N + 1)
    sw = sum(1 for j in range(len(h) - 1) if h[j] != h[j + 1]) / (len(h) - 1)
    ones = sum(h) / len(h)
    print(f"\nprime h: 1-density={ones:.4f}  switch density={sw:.4f}")
    # mean(D) over full range:
    D = [SP[n + 1] - SP[n] for n in range(2, N)]
    print(f"mean(D) over [2,{N}) = {sum(D)/len(D):.4f}")

    # compare: for a RANDOM balanced-1 h (ones ~0.585, which is what primes
    # have), is mean(D)~0 the SAME? Yes per earlier runs. So test: does mean(D)
    # track ones-density - 1/2, or switch density - 1/2?
    print("\nmean(D) vs ones-density: test by scaling against Bernoulli(p):")
    for p in [0.5, 0.4, 0.5855, 0.7]:
        random.seed(p * 100)
        h = [1 if random.random() < p else 0 for _ in range(N + 1)]
        S = S_of_h(N, h)
        D = [S[n + 1] - S[n] for n in range(2, N)]
        print(f"  Bernoulli p={p}: ones~{sum(h)/(N+1):.3f}  "
              f"mean(D)={sum(D)/len(D):+.4f}  std(D)={math.sqrt(sum((d-sum(D)/len(D))**2 for d in D)/len(D)):.2f}")


if __name__ == "__main__":
    main()
