#!/usr/bin/env python3
"""Extend the per-index second-moment plateau E[S(n)^2] ~ (n-2) for the real
prime h beyond the N=40000 data on disk, using the exact O(n log n) SOS fold.

Also reports sign bias of S(n) (Chebyshev-type residue bias) which would break
the centered-at-zero assumption behind the Markov/Chebyshev tail argument.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.supply_fold import s_sos
from lib.nu2_guard import assert_supply_guard
import numpy as np

N = int(sys.argv[1]) if len(sys.argv) > 1 else 65536
assert_supply_guard(4000)

# Build the prime h once (length N)
from lib.nu2_guard import prime_h
h = prime_h(N + 1)

# Sample the plateau at target n
targets = list(range(40000, N + 1, 512)) + [32768, 40000, 49152, 65536]
targets = sorted(set(t for t in targets if 3 <= t <= N))

print(f"per-index S, E[S], S^2/(n-2), S/n for prime h, sampled n up to {N}")
vals_S2rn = []
for n in targets:
    S, ones = s_sos(n, h)
    r = S * S / (n - 2)
    vals_S2rn.append(r)
    print(f"  n={n:6d}  S={S:+7d}  S/sqrt n={S/np.sqrt(n):+.3f}  "
          f"S^2/(n-2)={r:.4f}  S/n={S/n:+.5f}")

print(f"\nsample mean of S^2/(n-2) over {len(targets)} targets: "
      f"{np.mean(vals_S2rn):.4f}")
print(f"max S^2/(n-2) among samples: {max(vals_S2rn):.3f}")

# sign bias: fraction of S>0, and mean sign
Slist = []
for n in targets:
    S, _ = s_sos(n, h)
    Slist.append(S)
Snp = np.array(Slist)
print(f"fraction S>0: {(Snp>0).mean():.3f}, mean S^3/(n^{1.5}) (skew proxy): "
      f"{np.mean(Snp**3)/np.mean(targets)**1.5:.3f}")
