#!/usr/bin/env python3
"""Confirm the pricing: is 'bounded lag-k autocorrelation of h' discriminated
by the fold? Compares the fold second moment E[S(n)^2]/(n-2) (its prefix mean
over a full dyadic range, freshly computed, exact SOS) for primes vs iid vs
Thue-Morse vs alternating.

If primes ~ iid ~ 1 (good) while Thue-Morse/alternating grow ~ n, then a bare
autocorrelation hypothesis is NOT the right weaker input: iid passes with ~0
autocorrelation too. The thing that separates good from bad is the *submask-
window* correlation structure, which is exactly what E[S^2]=O(n) measures.
"""
import sys, random
sys.path.insert(0, "/workspace/code")
from lib.primes import h_string
from lib.supply_fold import s_sos


def thue(j):
    return bin(j).count('1') % 2


def mk(lab, N):
    if lab == "primes":
        return h_string(N + 3)
    if lab == "iid05":
        random.seed(11)
        return [random.randint(0, 1) for _ in range(N + 2)]
    if lab == "thue":
        return [thue(j) for j in range(N + 2)]
    if lab == "alt":
        return [j % 2 for j in range(N + 2)]
    raise ValueError(lab)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 16384
    labels = ["primes", "iid05", "thue", "alt"]
    hc = {l: mk(l, N) for l in labels}
    # prefix mean of S^2/(n-2) over n in [M, N], sampled every sp
    M, sp = 512, 128
    print(f"prefix-mean of fold second-moment ratio E[S(n)^2]/(n-2), n in [{M},{N}]")
    print("label".ljust(10) + "mean_ratio".rjust(12) + "  max_ratio".rjust(12) + "  n_sample".rjust(10))
    for l in labels:
        s = 0.0
        mx = 0.0
        c = 0
        for n in range(M, N + 1, sp):
            S, _ = s_sos(n, hc[l][:n])
            r = S * S / (n - 2)
            s += r
            mx = max(mx, r)
            c += 1
        print(f"{l:10s}{s/c:12.3f}{mx:12.3f}{c:10d}")


if __name__ == "__main__":
    main()
