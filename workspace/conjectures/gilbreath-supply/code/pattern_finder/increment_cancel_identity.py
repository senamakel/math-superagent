#!/usr/bin/env python3
"""Decisive structural check: is the near-cancellation of successive S
increments (ACF1(D) ~ -1/2, keeping var(S) = O(n) despite var(D) ~ 4000)
a FOLD IDENTITY independent of input, or does it depend on the input?

Test on purely adversarial inputs too: h = single 1 (near kernel), and a
'sawtooth' pattern. If ACF1(D) and the std ratio are invariant, then
var(S(n)) = O(n) is a fold-generic FACT and the only remaining open arithmetic
input is bounded 1-density (which the primes satisfy: ~0.585).

Also: what is the exact relation? For a process with increments D and
ACF1(D) = r, var(S across k steps) = k*var(D)*(1+2*rho_1+...) roughly.
If r ~ -1/2 exactly, var(S) ~ var(D)/2 per step NOT k*var(D). Measure.
"""
import sys, math, random, time
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def S_of_h(N, h):
    return {n: s_sos(n, h)[0] for n in range(2, N + 1)}


def full_metrics(S, N):
    ns = list(range(50, N + 1))
    stdS = math.sqrt(sum(S[n] ** 2 for n in ns) / len(ns))
    D = [S[n + 1] - S[n] for n in range(2, N)]
    m = sum(D) / len(D)
    varD = sum((d - m) ** 2 for d in D) / len(D)
    stdD = math.sqrt(varD)
    den = sum((D[i] - m) ** 2 for i in range(len(D)))
    acf1 = (sum((D[i] - m) * (D[i + 1] - m) for i in range(len(D) - 1))
            / den) if den else 0
    return stdS, stdD, acf1


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    assert_supply_guard(4000)
    print(f"{'input':<26s}  stdS    stdD   ACF1(D)  stdS/stdD  (random-walk pred stdD*sqrtN)")
    rows = []

    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    sS, sD, a1 = full_metrics(SP, N)
    rows.append(("PRIMES", sS, sD, a1))

    random.seed(3)
    h = [1 if random.random() < 0.5 else 0 for _ in range(N + 1)]
    S = S_of_h(N, h)
    sS, sD, a1 = full_metrics(S, N)
    rows.append(("iid p=0.5", sS, sD, a1))

    # single-1 (near kernel) - should this still be mean-reverting?
    h = [0] * (N + 1)
    h[N // 2] = 1
    S = S_of_h(N, h)
    sS, sD, a1 = full_metrics(S, N)
    rows.append(("single-1 (near kernel)", sS, sD, a1))

    # alternating sawtooth h: 1,0,1,0,...
    h = [1 if j % 2 == 0 else 0 for j in range(N + 1)]
    S = S_of_h(N, h)
    sS, sD, a1 = full_metrics(S, N)
    rows.append(("alternating 1010", sS, sD, a1))

    # delta: h = [1,0,0,...]
    h = [0] * (N + 1)
    h[0] = 1
    S = S_of_h(N, h)
    sS, sD, a1 = full_metrics(S, N)
    rows.append(("delta h0=1", sS, sD, a1))

    rw_pred = math.sqrt(N)
    for label, sS, sD, a1 in rows:
        print(f"{label:<26s} {sS:7.1f} {sD:7.1f} {a1:+7.3f}  "
              f"{sS/sD:9.3f}   ({sD*rw_pred:.0f})")


if __name__ == "__main__":
    main()
