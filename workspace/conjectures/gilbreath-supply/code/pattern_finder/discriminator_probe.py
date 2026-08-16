#!/usr/bin/env python3
"""Discriminator probe: which statistic separates GOOD inputs (S=O(sqrt n))
from BAD/collapsing inputs (Thue-Morse, all-ones, low-density Bernoulli)?

Candidates: lag-1 ACF of increments D(n)=S(n+1)-S(n); ratio std(D)/sqrt-var(S);
max|S|/n. If "good" inputs share a signature (e.g. ACF1(D)~-1/2, mean-reverting)
that "bad" collapse inputs lack, then a provable ACF1 bound would be a real
arithmetic->SUPPLY route (a weaker input than switch density).
"""
import sys, math, random, time
from lib.supply_fold import s_sos
from lib.nu2_guard import prime_h, assert_supply_guard


def S_of_h(N, h):
    return {n: s_sos(n, h)[0] for n in range(2, N + 1)}


def metrics(S, N):
    ns = list(range(50, N + 1))
    maxratio = max(abs(S[n]) / math.sqrt(n) for n in ns)
    max_over_n = max(abs(S[n]) / n for n in ns)
    D = [S[n + 1] - S[n] for n in range(2, N)]
    mean = sum(D) / len(D)
    varD = sum((d - mean) ** 2 for d in D) / len(D)
    stdD = math.sqrt(varD)
    den = sum((D[i] - mean) ** 2 for i in range(len(D)))
    acf1 = (sum((D[i] - mean) * (D[i + 1] - mean) for i in range(len(D) - 1))
            / den) if den else 0
    varS = sum(S[n] ** 2 for n in ns) / len(ns)
    # std(S)/sqrt(n) at the top of range
    s_ratio = math.sqrt(varS) / math.sqrt(N)
    return maxratio, max_over_n, stdD, acf1, s_ratio


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    assert_supply_guard(4000)
    rows = []

    hP = prime_h(N + 1)
    SP = S_of_h(N, hP)
    v = metrics(SP, N)
    rows.append(("PRIMES (balanced, good?)", v))
    print(f"{'input':<28s} max|S|/s N  max|S|/n  std(D)  ACF1(D)  std(S)/sN")

    tm = [bin(j).count('1') % 2 for j in range(N + 1)]
    ST = S_of_h(N, tm)
    v = metrics(ST, N)
    rows.append(("THUE-MORSE (collapses)", v))

    ones = [1] * (N + 1)
    SO = S_of_h(N, ones)
    v = metrics(SO, N)
    rows.append(("ALL-ONES (kernel, S=n)", v))

    random.seed(7)
    for p, label in [(0.5855, "Bernoulli p=0.5855 (density-matched)"),
                     (0.10, "Bernoulli p=0.10 (low density)")]:
        h = [1 if random.random() < p else 0 for _ in range(N + 1)]
        S = S_of_h(N, h)
        v = metrics(S, N)
        rows.append((label, v))

    for label, v in rows:
        print(f"{label:<28s} {v[0]:9.3f} {v[1]:9.4f} {v[2]:7.2f} "
              f"{v[3]:+8.3f} {v[4]:9.3f}")


if __name__ == "__main__":
    main()
