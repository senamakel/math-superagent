#!/usr/bin/env python3
"""Sharpen the Parseval identity: for the PRIMES and iid-balanced input,
   var(S over [range]) = varD * k * (1 + 2*sum_{i>=1} r_i)
Check multiple ranges (k = window length) and whether sum r_i -> -1/2 (so the
bracket -> 0) as the window/range grows. Also check it for the primes at a
longer range N=6000 to see if it stabilises near 0.

The most important falsifier: if sum r_i were really -1/2 over ALL lags, the
bracket would be identically 0 and var(S)=O(1) over any span (not O(n)). The
measured var(S)~0.8n says the bracket is ~ var(S)/(k*varD) ~ 0.8/(4000) =
0.0002 — positive tiny, i.e. the anti-correlation is ~ -1/2 + O(1/n). This
would be EXACTLY the statement that S is a 'balanced' path (variance grows
linearly but with constant 0.8, not 4000) — i.e. the increments form a
near-deterministic-zero-sum sequence. Determine the constant honestly.
"""
import sys, math, random, time
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def S_of_h(N, h):
    return {n: s_sos(n, h)[0] for n in range(2, N + 1)}


def bracket(S, N, k, offset=2):
    """var(S over a window of length k) / (k * varD), measuring (1+2 sum r_i)
    via the exact variance of the running partial sums over the window.
    Uses windows ending at various tops to average out finite-N noise."""
    D = [S[n + 1] - S[n] for n in range(2, N)]
    mD = sum(D) / len(D)
    varD = sum((d - mD) ** 2 for d in D) / len(D)
    # multiple windows of length k
    vals = []
    for end in range(k + offset, N, max(1, k // 2)):
        # running sums S over this window directly (S is bounded, exact)
        w = [S[end - k + 1 + j] for j in range(k)]  # approx; use real S
        # variance of S across this window: var over positions
        mw = sum(w) / len(w)
        vw = sum((x - mw) ** 2 for x in w) / len(w)
        vals.append(vw)
    # average window variance
    avg = sum(vals) / len(vals) if vals else 0
    return avg / (k * varD) if varD else 0, avg


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    assert_supply_guard(4000)
    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    D = [SP[n + 1] - SP[n] for n in range(2, N)]
    mD = sum(D) / len(D)
    varD = sum((d - mD) ** 2 for d in D) / len(D)
    print(f"PRIMES N={N}: varD={varD:.1f}")
    for k in [256, 512, 1024, 1500, 2000]:
        b, avg = bracket(SP, N, k)
        print(f"  window k={k:5d}: avg window var(S)={avg:7.1f}  "
              f"bracket = var(S)/(k varD) = {b:.6f}   "
              f"bracket^1/2*(k varD) ~ sqrt(avg)={math.sqrt(avg):7.2f}")
    # cumulative var-growth rate: var(S across [50,n])/n should stabilize ~0.8
    print("\nvar(S(n)) as function of n (prefix):")
    for top in [1000, 2000, 4000, 6000]:
        if top <= N:
            ns = list(range(50, top + 1))
            v = sum(SP[n] ** 2 for n in ns) / len(ns)
            print(f"  n<={top}: var(S)={v:.1f}  var/S/n~{v/top:.4f}")

    # ---- the same for random balanced ----
    random.seed(3)
    h = [1 if random.random() < 0.5 else 0 for _ in range(N + 1)]
    SR = S_of_h(N, h)
    D = [SR[n + 1] - SR[n] for n in range(2, N)]
    mD = sum(D) / len(D)
    varD = sum((d - mD) ** 2 for d in D) / len(D)
    print(f"\niid p=0.5 N={N}: varD={varD:.1f}")
    for k in [256, 512, 1024, 1500, 2000]:
        b, avg = bracket(SR, N, k)
        print(f"  window k={k:5d}: avg window var(S)={avg:7.1f}  "
              f"bracket={b:.6f}  sqrt(avg)={math.sqrt(avg):7.2f}")


if __name__ == "__main__":
    main()
