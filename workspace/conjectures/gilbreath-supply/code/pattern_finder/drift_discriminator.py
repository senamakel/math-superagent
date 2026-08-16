#!/usr/bin/env python3
"""Confirm the discriminator for collapse vs good inputs is the DRIFT mean(D),
not the fluctuation: for collapsing inputs (single-1, Thue-Morse) mean(D)~1
(=S(N)/(N-2)~1, i.e. S~N), while for balanced inputs mean(D)~0 (S~o(N)).
The telescoping identity ties them exactly, so 'no collapse' == 'S(N)=o(N)'.
"""
import sys, math, random
from lib.supply_fold import s_sos


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    cases = {}
    # single 1 near middle: collapse
    h = [0] * (N + 1)
    h[N // 2] = 1
    cases["single-1 (collapse)"] = h
    cases["Thue-Morse (collapse)"] = [bin(j).count('1') % 2 for j in range(N + 1)]
    random.seed(5)
    cases["iid p=0.5 (good)"] = [1 if random.random() < 0.5 else 0
                                 for _ in range(N + 1)]
    # sparse low density
    random.seed(6)
    cases["Bern p=0.10 (collapse)"] = [1 if random.random() < 0.10 else 0
                                       for _ in range(N + 1)]
    print(f"{'input':<24s}  mean(D)  S(N)/(N-2)  max|S|/N   ACF1(D)")
    for label, h in cases.items():
        S = {n: s_sos(n, h)[0] for n in range(2, N + 1)}
        D = [S[n + 1] - S[n] for n in range(2, N)]
        m = sum(D) / len(D)
        tel = (S[N] - S[2]) / (N - 2)
        mx = max(abs(S[n]) for n in range(2, N + 1)) / N
        den = sum((d - m) ** 2 for d in D)
        a1 = (sum((D[i] - m) * (D[i + 1] - m) for i in range(len(D) - 1))
              / den) if den else 0
        print(f"{label:<24s}  {m:+.4f}  {tel:+.4f}       "
              f"{mx:.3f}     {a1:+.3f}")


if __name__ == "__main__":
    main()
