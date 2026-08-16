#!/usr/bin/env python3
"""Test whether S(n) is mean-reverting as a multiplicative AR(1):
    S(n+1) ~ c * S(n) + noise, c < 1
which would explain the large increment variance yet sqrt(n)-scale S.

If S is AR(1) with coefficient c, then Var(S) ~ Var(noise)/(1-c^2) and the
steady state is bounded (mean-reverting), not a random walk. A random walk has
c = 1. Measure c by least squares over the whole range, and also whether c
depends on n (blocked fit). Compare across inputs (primes, random, Thue-Morse).

Also measure the variance reduction explicitly: std(S_top) vs std(D)*sqrt(span)
what a random walk would predict.
"""
import sys, math, random, time
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def S_of_h(N, h):
    return {n: s_sos(n, h)[0] for n in range(2, N + 1)}


def ar1_fit(S, N, lo=100):
    """Fit S(n+1) = c*S(n) + b; return c, b, and r2."""
    xs, ys = [], []
    for n in range(lo, N):
        xs.append(S[n])
        ys.append(S[n + 1])
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    num = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    den = sum((xs[i] - mx) ** 2 for i in range(n))
    c = num / den if den else 0
    b = my - c * mx
    # r2
    sst = sum((ys[i] - my) ** 2 for i in range(n))
    sse = sum((ys[i] - (c * xs[i] + b)) ** 2 for i in range(n))
    r2 = 1 - sse / sst if sst else 0
    return c, b, r2, n


def stats(S, N):
    ns = list(range(50, N + 1))
    stdS = math.sqrt(sum(S[n] ** 2 for n in ns) / len(ns))
    D = [S[n + 1] - S[n] for n in range(2, N)]
    m = sum(D) / len(D)
    stdD = math.sqrt(sum((d - m) ** 2 for d in D) / len(D))
    # random walk prediction for std(S) at top
    rw_pred = stdD * math.sqrt(N)
    return stdS, stdD, rw_pred


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    assert_supply_guard(4000)
    print(f"AR(1) fit of S(n+1) ~ c*S(n):  input  c     b     r2    n="
          f"   |  stdS  stdDW  rwPred/act")
    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    c, b, r2, n = ar1_fit(SP, N)
    sS, sD, rw = stats(SP, N)
    print(f"{'PRIMES':<24s} {c:+.4f} {b:+.2f} {r2:.4f} {n:6d} | "
          f"{sS:6.1f} {sD:6.1f} {rw/sS:9.1f}")

    for label, hgen in [
            ("iid p=0.5", lambda: [1 if random.random() < 0.5 else 0
                                   for _ in range(N + 1)]),
            ("Bern p=0.5855", lambda: [1 if random.random() < 0.5855 else 0
                                       for _ in range(N + 1)]),
            ("Thue-Morse", lambda: [bin(j).count('1') % 2 for j in range(N + 1)])]:
        random.seed(11)
        h = hgen()
        S = S_of_h(N, h)
        c, b, r2, n = ar1_fit(S, N)
        sS, sD, rw = stats(S, N)
        print(f"{label:<24s} {c:+.4f} {b:+.2f} {r2:.4f} {n:6d} | "
              f"{sS:6.1f} {sD:6.1f} {rw/sS:9.1f}")

    # does c depend on n (blocked)?
    print("\nblocked AR(1) c for PRIMES:")
    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    j = 9
    while (1 << j) <= N:
        lo, hi = 1 << j, min(N, (1 << (j + 1)) - 1)
        c, b, r2, n = ar1_fit(SP, hi, lo=lo)
        print(f"  S over [{lo},{hi}]:  c={c:+.4f}  r2={r2:.4f}")
        j += 1


if __name__ == "__main__":
    main()
