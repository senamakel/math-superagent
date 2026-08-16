#!/usr/bin/env python3
"""Extend the exact nu2(n) computation for the prime input beyond n=4000.

nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }, T the depth-d submask-XOR fold cell
over F2 of h. Computed per n by the O(n log n) submask-product SOS transform
(lib.supply_fold.s_sos), NOT the O(n^2) row-triangle DP. Streamed per n: one
nu2 value held at a time, never a full row triangle in memory.

h comes from lib.primes.h_string (prime gap mod-4 switch bits); h length >= n
for every n (we build h_string(20002) once and reuse h[0..n-1]).

Outputs, exact:
  (1) every n in [50, 20000] with nu2(n)/n < 0.42, plus count and largest such n;
  (2) mean of nu2/n over n in [50,N] at N = 1000, 5000, 10000, 20000;
  (3) last-half-window variance sigma^2 of nu2/n over window [N/2, N) at those N.

s_sos is cross-checked against the direct oracle s_direct on n=4..200 (primes)
at the top; failure aborts. All arithmetic exact; only ratios are float.
"""
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_sos, s_direct
from lib.primes import h_string


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 20000

    # ---- oracle cross-check: s_sos vs s_direct on primes, small n ----
    h_check = h_string(N + 2)
    for n in range(4, 201):
        Sd, od = s_direct(n, h_check)
        Ss, os_ = s_sos(n, h_check)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    print(f"oracle cross-check: s_sos == s_direct on n=4..200 (primes): OK")

    # ---- build prime h once; h has length >= N (indexed 0..N-1) ----
    h = h_string(N + 2)
    assert len(h) >= N, len(h)

    # streamed: only the current nu2 value is held; no full triangle
    nu2 = [0] * (N + 1)          # full sequence kept only because reporting needs it
    dips = []                     # n with nu2/n < 0.42, n in [50,N]
    t0 = time.time()
    for n in range(2, N + 1):
        _, ones = s_sos(n, h)
        nu2[n] = ones
        if 50 <= n and ones / n < 0.42:
            dips.append((n, ones, ones / n))
    elapsed = time.time() - t0
    print(f"computed nu2(n) for n=2..{N} streamed (per-n s_sos) in {elapsed:.1f}s; "
          f"reached n={N}")

    # ---- (1) dips below 0.42 ----
    lines = [f"nu2_extended: primes, per-n submask-product SOS (s_sos), d in [2,n-1]",
             f"N={N}"]
    lines.append(f"(1) n in [50,{N}] with nu2(n)/n < 0.42:")
    for (n, ones, r) in dips:
        lines.append(f"    n={n}  nu2={ones}  nu2/n={r:.6f}")
    lines.append(f"    count of such n = {len(dips)}")
    lines.append(f"    largest such n = {dips[-1][0] if dips else None}")

    # ---- (2) mean of nu2/n over [50,N] at sample N ----
    samples = [1000, 5000, 10000, 20000]
    lines.append("(2) mean of nu2/n over n in [50,N]:")
    for S in samples:
        if S > N:
            continue
        tot = 0.0
        for n in range(50, S + 1):
            tot += nu2[n] / n
        mean = tot / (S - 50 + 1)
        lines.append(f"    N={S}: mean = {mean:.8f}")

    # ---- (3) last-half-window variance of nu2/n over [N/2, N) ----
    lines.append("(3) last-half-window variance sigma^2 of nu2/n over [N/2, N):")
    for S in samples:
        if S > N:
            continue
        lo = S // 2
        hi = S - 1                # window [N/2, N) -> n in [S//2, S-1]
        vals = [nu2[n] / n for n in range(lo, hi + 1)]
        m = sum(vals) / len(vals)
        var = sum((v - m) ** 2 for v in vals) / len(vals)
        lines.append(f"    N={S}: window n in [{lo},{hi}] (count {len(vals)}): "
                     f"sigma^2 = {var:.8f}  (mean={m:.8f})")

    text = "\n".join(lines) + "\n"
    print(text)

    outdir = os.path.join(os.path.dirname(__file__), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "nu2_extended.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
