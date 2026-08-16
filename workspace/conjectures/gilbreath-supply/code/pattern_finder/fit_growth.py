#!/usr/bin/env python3
"""Fit the growth exponent of max|S| and std(S) vs n for the primes, and test
the density-1 tail shape that SUPPLY's averaged form needs.

S(n) = (n-2) - 2*nu2(n). If |S|=O(n^a), then nu2/n = (1-2a-S/n)/2 -> 1/2 and
SUPPLY holds for any c<1/2 on a density-1 set when a<1. The empirical claim is
a~1/2 (CLT). This fits the exponent from octave block maxima and from
log-log regression, exactly.
"""
import sys, math, time
from lib.nu2 import fold_nu2
from lib.nu2_guard import prime_h, assert_supply_guard


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    assert_supply_guard(4000)
    h = prime_h(N + 1)
    t0 = time.time()
    S = {}
    for n in range(2, N + 1):
        S[n] = (n - 2) - 2 * fold_nu2(n, h)
    print(f"S(n) for n=2..{N} in {time.time()-t0:.1f}s")

    # octave block max |S| and std(S)
    print("\noctave     n-range          max|S|  std(S)   std/sqrt(hi)")
    pts = []
    j = 6
    while (1 << j) <= N:
        lo, hi = 1 << j, min(N, (1 << (j + 1)) - 1)
        blk = [S[n] for n in range(lo, hi + 1)]
        mx = max(abs(v) for v in blk)
        stdd = math.sqrt(sum(v * v for v in blk) / len(blk))
        pts.append((hi, mx, stdd))
        print(f"  [2^{j},2^{j+1})  {lo:6d}..{hi:6d}   {mx:6d}  {stdd:8.1f}  "
              f"{stdd/math.sqrt(hi):.3f}")
        j += 1

    # log-log regression of max|S| (and std) vs hi over octaves
    import statistics
    def fit(pairs):
        xs = [math.log(p[0]) for p in pairs]
        ys = [math.log(p[1]) for p in pairs]
        n = len(xs)
        mx, my = sum(xs)/n, sum(ys)/n
        num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
        den = sum((xs[i]-mx)**2 for i in range(n))
        return num/den
    emax = fit([(p[0], p[1]) for p in pts])
    estd = fit([(p[0], p[2]) for p in pts])
    print(f"\nlog-log slope: max|S| exponent ~ {emax:.3f},  "
          f"std(S) exponent ~ {estd:.3f}  (1/2 = CLT, 1 = drift)")

    # density-1 tail: fraction of n in [1000,N] with nu2/n below various c
    print("\ndensity-1 tail over [1000, N]:  # {n: nu2/n < c} / width")
    for c in [0.40, 0.42, 0.45, 0.48, 0.30]:
        cnt = sum(1 for n in range(1000, N + 1)
                  if (S[n] if True else 0) and (((n-2)-S[n])/2)/n < c)
        width = N - 1000 + 1
        print(f"  c={c:.2f}: {cnt} / {width} = {cnt/width:.6f}")
    # equivalently via S: nu2/n < c  <=>  (n-2)/n - S/n < 2c  <=>
    #   S/n > (n-2)/n - 2c  ~  1 - 2c
    print("\nvia S/n > 1-2c (upper tail of |S|/n):")
    for c in [0.40, 0.42, 0.45, 0.48]:
        thr = 1 - 2 * c
        cnt = sum(1 for n in range(1000, N + 1)
                  if abs(S[n]) / n > thr)
        print(f"  c={c:.2f} (threshold S/n>{thr:.3f}): count={cnt} "
              f"density={cnt/(N-1000+1):.6f}")

    # The exact quantity SUPPLY needs: min over c of the density-1 holding.
    # Report the biggest c for which the count is 0 over [1000,N] and [N/2,N].
    for lo, tag in [(1000, "abs"), (N//2, "last-half")]:
        # largest c in 0.25..0.49 step 0.005 with zero violations
        best = None
        for k in range(50, 99):
            c = k / 200.0        # 0.25 .. 0.49 step 0.005
            thr = 1 - 2 * c
            cnt = sum(1 for n in range(lo, N + 1) if abs(S[n]) / n > thr)
            if cnt == 0:
                best = c
        print(f"largest c with ZERO violations on [{lo},{N}]: "
              f"{('%.3f' % best) if best is not None else 'none'}")


if __name__ == "__main__":
    main()
