#!/usr/bin/env python3
"""Independent confirmation of the union density by direct counting over an
increasing range of K (n=840K+1), for the three family sets:
  A: 7 families from the original capture (M in {11,13,17})   -> earlier found 0.526
  B: all 603 (M up to 37)
Reports the observed fraction at several N to confirm convergence to the
claimed values (A: 0.5261, B: 0.9453)."""
import re
from math import gcd
from collections import defaultdict

txt = open('code/out/extended_subprogression.full.txt').read()
lines = txt.splitlines()
per_all = defaultdict(set)      # modulus -> set of K-residues
for ln in lines:
    m = re.match(r'FOUND a=(\d+) b=(\d+)\s+x=', ln)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        per_all[a//840].add((b-1)//840)

def fraction(N, per):
    covered = 0
    for K in range(N):
        if any(K % m in s for m, s in per.items()):
            covered += 1
    return covered / N

# Set A: original 7 (M in 11,13,17)
per_A = defaultdict(set)
for (a, b, *_ ) in [(9240,4201),(9240,5881),(9240,8401),
                    (10920,5881),(10920,7561),(10920,9241),(10920,10081),
                    (14280,3361)]:
    per_A[a//840].add((b-1)//840)

print("Set A (original 7 families), fraction covered among n=840K+1, K<N:")
for N in [1000, 10000, 100000, 1000000]:
    print(f"  N={N}: {fraction(N, per_A):.5f}   (claim 0.5261)")

print("\nSet B (all 603 families), fraction covered:")
for N in [1000, 10000, 100000, 1000000, 3000000]:
    print(f"  N={N}: {fraction(N, per_all):.5f}   (claim 0.9453)")
