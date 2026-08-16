#!/usr/bin/env python3
"""Ground G-mean-linear with a real computation for the PRIME h, plus
negative controls (all-ones and Thue-Morse h).

For each n, nu2(n) = #{d in [dmin, n-1] : T(n,d)=1}, T the depth-d submask-XOR
fold cell. Uses the O(n log n) submask-product SOS transform from
lib.supply_fold (verified there against the direct oracle on n=8..60; we
re-verify at the top). The averaged mean is

    M(N) = (1/N) * sum_{n=2..N} nu2(n)/n.

We report M(N) at several N, pin the d-range convention against
nu2(4000)/4000 = 0.4933 from problem.md, check nu2/n stays in [0.42, 0.52]
over n=50..N for the primes, and run negative controls that MUST fail:
all-ones h is the kernel vector so nu2 = O(1) and M -> 0; Thue-Morse h is
aperiodic but sublinear so M -> 0. The signal must be specific to the prime h.

All arithmetic exact (fold parities / +-1 products); only ratios are float.
"""
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.supply_fold import s_direct, s_sos
from lib.primes import h_string, mod4_string


def prime_h(n):
    """h[j] = [q_{j+2} != q_{j+1} mod 4] for j=0..n-1 (length n)."""
    return h_string(n + 2)[:n]


def all_ones_h(n):
    return [1] * n


def thue_morse_h(n):
    return [bin(j).count("1") % 2 for j in range(n)]


def nu2_sos(n, h, dmin):
    """Number of d in [dmin, n-1] with T(n,d)=1 via the submask-product SOS
    transform. h length >= n (indexed 0..n-1)."""
    tau = [1 - 2 * h[j] for j in range(n)]
    barray = [tau[n - 1 - t] for t in range(n)]
    size = 1
    while size < n:
        size <<= 1
    g = [1] * size
    for t in range(n):
        g[t] = barray[t]
    bit = 1
    while bit < size:
        for x in range(size):
            if x & bit:
                g[x] *= g[x ^ bit]
        bit <<= 1
    ones = 0
    for d in range(dmin, n):
        if g[d] == -1:
            ones += 1
    return ones


def verify_oracle():
    """s_sos vs s_direct on n=8..60 for the primes (both d in [2,n-1])."""
    r = mod4_string(64)
    h = [1 if r[j + 1] != r[j] else 0 for j in range(len(r) - 1)]
    for n in range(8, 61):
        Sd, od = s_direct(n, h)
        Ss, os_ = s_sos(n, h)
        assert Sd == Ss and od == os_, (n, Sd, Ss, od, os_)
    return "s_sos == s_direct on n=8..60: OK"


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    dmin = int(sys.argv[2]) if len(sys.argv) > 2 else 2  # 2 -> [2,n-1]; 0 -> [0,n-1]
    ver = verify_oracle()
    lines = [ver, f"prime ceiling N = {N}", f"d-range convention: d in [{dmin}, n-1]"]

    # --- convention pin at n=4000 (or N if smaller) ---
    nconv = min(4000, N)
    for ddmin, tag in [(0, "d in [0,n-2]"), (2, "d in [2,n-1]")]:
        nu2 = nu2_sos(nconv, prime_h(nconv), ddmin)
        lines.append(f"nu2({nconv}) {tag}: {nu2}  ratio={nu2/nconv:.4f}  "
                     f"(literature 0.4933 -> nu2~={0.4933*nconv:.0f})")

    if N >= 50:
        lo, hi = 1.0, 0.0
        for n in range(50, N + 1):
            r = nu2_sos(n, prime_h(n), dmin) / n
            lo, hi = min(lo, r), max(hi, r)
        lines.append(f"prime nu2/n over n=50..{N}: min={lo:.4f} max={hi:.4f} "
                     f"(literature [0.42,0.52])")

    # --- per-h nu2/n arrays, then averaged means at sample points ---
    samples = sorted({100, 500, 1000, 2000, N} - {0})
    if 4000 <= N:
        samples.append(4000)
    samples = sorted(set(samples))
    sources = [("prime", prime_h), ("all-ones(kernel)", all_ones_h),
               ("thue-morse", thue_morse_h)]
    for label, hsrc in sources:
        vals = {n: nu2_sos(n, hsrc(n), dmin) / n for n in range(2, N + 1)}
        tot = 0.0
        for n in range(2, N + 1):
            tot += vals[n]
            if n in samples:
                lines.append(f"{label:16s} M({n}) = {tot/n:.4f}   nu2({n})/{n} = {vals[n]:.4f}")
    return lines


if __name__ == "__main__":
    out = main()
    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(__file__), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "averaged_mean_capture.txt"), "w") as f:
        f.write(text)
