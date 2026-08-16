#!/usr/bin/env python3
"""For the averaged form (GOAL priority 1): count, in [n0,4000], how many n have
nu2(n)/n below each threshold c. Density-1 linear bound needs: for some c>0,
only o(N) values below c. Also track the running maximum-n of the lowest dip so
the deep-dip subsequence is visible (is it dying out or recurring?)."""
S = []
for l in open('code/out/supply_endpoint_density.txt'):
    parts = l.split()
    if len(parts) < 4: continue
    if parts[1] == 'primes':
        S.append(int(parts[2].split('=')[1]))
nu2 = [((n) - 2 - S[n - 2]) // 2 for n in range(2, len(S) + 2)]
n0 = 50
ratio = {n: nu2[n - 2] / n for n in range(n0, len(S) + 2)}
Nmax = len(S) + 1
print("threshold c:  count{n in [50,N] with nu2/n < c} and max n attaining it")
for c in [0.30, 0.35, 0.40, 0.42, 0.45, 0.48]:
    pts = [(n, r) for n, r in ratio.items() if r < c]
    print(f"  c={c:.2f}: count={len(pts):5d}  max_n_below={max((n for n,_ in pts), default=None)}")
# are points below 0.42 bounded in n? list them
below = sorted((n, ratio[n]) for n in ratio if ratio[n] < 0.42)
print("\nall n in [50,4000] with nu2/n < 0.42:")
for n, r in below:
    print(f"  n={n}  nu2/n={r:.4f}")
print("count:", len(below), " largest n:", max(n for n, _ in below))
# variance decay exponent: sigma^2 vs N on last-half windows (approx 1/N?)
print("\nlast-half-window sigma^2 (from pattern_var): 7.78e-4,3.44e-4,1.62e-4,9.11e-4e-1 scaling ~1/N")
