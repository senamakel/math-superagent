#!/usr/bin/env python3
"""Price the 'bounded autocorrelation of h' candidate (GOAL priority 2).

The open arithmetic step is E[S(n)^2] = O(n) for the prime h. To tell whether
*generic* bounded-autocorrelation input has this property (i.e. whether it is
a real hypothesis to prove, or vacuous software on the fold), measure the
fold second-moment ratio E[S(n)^2]/(n-2) for several inputs:

  primes        — the target
  iid(0.5)      — independent, (nearly) zero centered autocorrelation
  iid(0.569)    — independent at measured prime switch density
  thue-morse    — balanced, small (but non-decaying) autocorrelation
  alternating   — maximally anti-correlated (period 2 => kernel-adjacent)

If iid and iid-at-p give ratio -> 1 (good) while thue-morse gives a growing
ratio, then 'bounded autocorrelation' as a bare hypothesis is NOT sufficient
by itself — what separates good from bad is the submask-window correlation,
and the primes sit at the good (uniform) level.
"""
import sys, random
sys.path.insert(0, "/workspace/code")
from lib.primes import h_string
from lib.supply_fold import s_sos


def thue_morse(j):
    return bin(j).count('1') % 2


def make_input(label, N, seed=1):
    if label == "primes":
        return h_string(N + 3)
    if label == "iid05":
        random.seed(seed)
        return [random.randint(0, 1) for _ in range(N + 2)]
    if label == "iidp":
        random.seed(seed)
        p = 0.569
        return [1 if random.random() < p else 0 for _ in range(N + 2)]
    if label == "thue":
        return [thue_morse(j) for j in range(N + 2)]
    if label == "alt":
        return [j % 2 for j in range(N + 2)]
    raise ValueError(label)


def second_moment_ratio(h, n):
    S, _ = s_sos(n, h[:n])
    return S * S / (n - 2)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 32768
    labels = ["primes", "iid05", "iidp", "thue", "alt"]
    hcache = {lab: make_input(lab, N) for lab in labels}
    # sample n at dyadic points
    pts = [1 << k for k in range(6, 16)]
    pts = [p for p in pts if p <= N]
    print(f"N={N}")
    hdr = "n".rjust(8) + "".join(lab.rjust(12) for lab in labels)
    print(hdr)
    for n in pts:
        row = f"{n:8d}"
        for lab in labels:
            r = second_moment_ratio(hcache[lab], n)
            row += f"{r:12.3f}"
        print(row)


if __name__ == "__main__":
    main()
