#!/usr/bin/env python3
"""Attack the second-moment plateau E[S(n)^2] ~ (n-2) at larger n.

The density-1 form of SUPPLY needs E[S^2] = O(n). The risk is that rare
spikes of S(n)^2/(n-2) (max ~14.5 at n=27624 among n<=40000; xo bound 16)
grow with n. Push the exact SOS fold to larger n and watch:
  - max S^2/(n-2) and the number exceeding thresholds 9 and 16,
  - pointwise S/sqrt(n) (the |S|<=C sqrt(n) uniform bound),
  - prefix mean of S^2/(n-2).
"""
import sys
import numpy as np
sys.path.insert(0, '/workspace/code')
from lib.supply_fold import s_sos
from lib.nu2_guard import assert_supply_guard, prime_h

N = int(sys.argv[1]) if len(sys.argv) > 1 else 131072
assert_supply_guard(4000)
h = prime_h(N + 2)

# build S once for all needed n by feeding the SOS fold directly per n,
# but reuse the O(n log n) per n. For N=131072 sampling every 256 is ~512
# SOS calls each O(n log n) -> heavy. Instead step densely near powers.
step = 64
print(f"N={N}, step={step}")
mx = 0.0; mxn = 0
over9 = 0; over16 = 0
acc = 0.0; cnt = 0
for n in range(N // 2, N + 1, step):
    S, _ = s_sos(n, h)
    r = S * S / (n - 2)
    if r > mx:
        mx = r; mxn = n
    if r > 9: over9 += 1
    if r > 16: over16 += 1
    acc += r; cnt += 1
print(f"window [{N//2},{N}]: max S^2/(n-2)={mx:.3f} at n={mxn}")
print(f"  frac over9={over9/cnt:.5f}  over16={over16/cnt:.5f}")
print(f"  mean S^2/(n-2) over window={acc/cnt:.4f}")

# max |S|/sqrt(n) over window
mxr = 0; mxrn = 0
for n in range(N // 2, N + 1, step):
    S, _ = s_sos(n, h)
    r = abs(S) / np.sqrt(n)
    if r > mxr:
        mxr = r; mxrn = n
print(f"  max |S|/sqrt n={mxr:.3f} at n={mxrn}")
