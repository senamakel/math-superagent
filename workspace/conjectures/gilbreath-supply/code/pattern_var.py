#!/usr/bin/env python3
"""Test G-var-vanishing for the prime h: does sigma^2_N of nu2(n)/n -> 0?

nu2(n) from the endpoint character sum S(n) via nu2 = (n-2-S)/2, read from the
already-computed supply_endpoint_density.txt (n=2..4000, primes only).
sigma^2_N = (1/N) sum_{n<=N} (nu2(n)/n - mu_N)^2, mu_N = mean of nu2(n)/n.

Also report: min over the tail, and the empirical lower envelope. If sigma^2
does NOT decay, G-var-vanishing is refuted as stated (but, per the adversarial
note, averaged SUPPLY could still hold).
"""
S = []
for l in open('code/out/supply_endpoint_density.txt'):
    parts = l.split()
    if len(parts) < 4:
        continue
    n, lbl, Sv = parts[0], parts[1], parts[2].split('=')[1]
    if lbl == 'primes':
        S.append(int(Sv))
# nu2(n) for n=2..4001 : index i-2
nu2 = [((n) - 2 - S[n - 2]) // 2 for n in range(2, len(S) + 2)]
# sanity: cross-check a few nu2(n) against the gap-parity fold (independent
# subroutine) -- these agree up to the +-1 h[0] convention edge.
import sys
sys.path.insert(0, 'code')
from lib.supply_fold import s_sos
from lib.primes import h_string
def nu2_sos(n, h):
    tau = [1 - 2 * h[j] for j in range(n)]
    barray = [tau[n - 1 - t] for t in range(n)]
    size = 1
    while size < n: size <<= 1
    g = [1] * size
    for t in range(n): g[t] = barray[t]
    bit = 1
    while bit < size:
        for x in range(size):
            if x & bit: g[x] *= g[x ^ bit]
        bit <<= 1
    return sum(1 for d in range(2, n) if g[d] == -1)
h = h_string(4002)
for n in [100, 500, 1000, 2000, 4000]:
    v = nu2_sos(n, h[:n])
    print(f"  cross n={n}: from-S={nu2[n-2]} from-h-sos={v} diff={nu2[n-2]-v}")
print("cross-check note: +-1 convention edge expected")

ratios = [nu2[n - 2] / n for n in range(2, len(S) + 2)]
print("\nN      mean     sigma^2    sigma      min_tail")
for N in [100, 250, 500, 750, 1000, 1500, 2000, 3000, 4000]:
    xs = ratios[:N]
    mu = sum(xs) / N
    var = sum((x - mu) ** 2 for x in xs) / N
    print(f"{N:5d}  {mu:.4f}  {var:.2e}  {var**0.5:.4f}  {min(xs):.4f}")
# also variance restricted to tail n in [N/2, N] to see decay without small-n effect
print("\nTail-only sigma^2 over last half (should decay to 0 if G-var holds):")
for N in [500, 1000, 2000, 4000]:
    xs = ratios[N // 2:N]
    mu = sum(xs) / len(xs)
    var = sum((x - mu) ** 2 for x in xs) / len(xs)
    print(f"  N={N:5d} window[{N//2},{N}): sigma^2={var:.2e}")
