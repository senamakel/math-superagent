#!/usr/bin/env python3
"""Analyze the increments D(n)=S(n+1)-S(n) and S-var growth structure.

The SUPPLY target (density-1 averaged form) reduces to |S(n)|=o(n), and the
empirical claim is that |S(n)|=O(sqrt(n)) — i.e. Var(S(n))=O(n) — with
std(S)/sqrt(n) ~ 1. The interesting structural question: what makes S stay
sqrt(n) while its increments D(n) are large? If Var(D) is large but S stays
bounded, the increments must be strongly negatively autocorrelated. Here I
measure that correlation exactly, since an anti-correlation bound on D(n)
would be a provable route to Var(S(n))=O(n) (G-var-vanishing).

Uses the canonical oracle fold_nu2 / prime_h from lib.
"""
import sys, math, time
from lib.nu2 import fold_nu2
from lib.nu2_guard import prime_h, assert_supply_guard


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    assert_supply_guard(max(N, 4000))
    h = prime_h(max(N + 1, 4001))
    t0 = time.time()
    S = {}
    for n in range(2, N + 1):
        S[n] = (n - 2) - 2 * fold_nu2(n, h)
    print(f"S(n) for n=2..{N} in {time.time()-t0:.1f}s")

    # increments D(n) = S(n+1)-S(n), n=2..N-1
    D = {n: S[n + 1] - S[n] for n in range(2, N)}
    ds = list(D.values())
    mean = sum(ds) / len(ds)
    var = sum((d - mean) ** 2 for d in ds) / len(ds)
    std = math.sqrt(var)
    print(f"D(n) n=2..{N-1}: mean={mean:.4f} std={std:.3f}")

    # S std and range
    ns = list(range(50, N + 1))
    sstd = math.sqrt(sum(S[n] ** 2 for n in ns) / len(ns))
    maxratio = max(abs(S[n]) / math.sqrt(n) for n in ns)
    print(f"std(S) over [50,{N}]: {sstd:.3f};  max|S|/sqrt(n)={maxratio:.3f}")

    # autocorrelation of D at lags 1..20 (exact floats from ints)
    def acf(lag):
        m = mean
        num = sum((D[n] - m) * (D[n + lag] - m) for n in range(2, N - lag))
        den = sum((D[n] - m) ** 2 for n in range(2, N))
        return num / den if den else 0.0

    print("ACF of increments D at lags 1..15:")
    for L in range(1, 16):
        print(f"  lag {L:2d}: {acf(L):+.4f}")

    # Var(S(n+1)-S(n)) vs Var(S): energy budget. If Var(D)~k but Var(S)~1,
    # the sum of D is much smaller than sqrt(sum Var(D)) -> anti-correlation.
    # Also measure Var(S blocks).
    print("\nVar(S) over dyadic blocks [2^j,2^{j+1}):")
    j = 5
    while (1 << j) <= N:
        lo, hi = 1 << j, min(N, (1 << (j + 1)) - 1)
        blk = [S[n] for n in range(max(lo, 50), hi + 1)]
        v = sum(x * x for x in blk) / len(blk)
        print(f"  [2^{j},2^{j+1}): n={max(lo,50)}..{hi}  var(S)={v:.2f}  "
              f"std/sqrt(n)~{math.sqrt(v)/math.sqrt(hi):.3f}")
        j += 1

    # Does S satisfy a block identity? Var multiplicative across dyadic blocks?
    print("\nMax |S| in each octave:")
    j = 5
    while (1 << j) <= N:
        lo, hi = 1 << j, min(N, (1 << (j + 1)) - 1)
        m = max(abs(S[n]) for n in range(max(lo, 50), hi + 1))
        print(f"  [2^{j},2^{j+1}): max|S|={m}")
        j += 1


if __name__ == "__main__":
    main()
