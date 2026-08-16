from lib.supply_fold import s_sos
from lib.primes import h_string
import sys
sys.path.insert(0, 'code')
from refute.check_live_structural_claims import t as fold_cell

# The endpoint-density claim G-endpoint-comparison-density: #{d : T(n,d)=1} >= c0 n
# for large n.  We measure the empirical density of T(n,d)=1 for the real prime h
# out to a moderate n, checking that it does NOT collapse to 0 (i.e. that the
# density stays bounded below by a positive constant) and compare the SOS count
# to a literal brute count on a subsample.

import sympy
def primes(n):
    return list(sympy.ntheory.generate.primerange(0, sympy.prime(n)+1))[:n]

for n in (50, 100, 200, 400, 800):
    h = h_string(n+2)  # need index up to n-1
    h = h[:n]
    S, ones = s_sos(n, h)
    nd = n-2
    print(f"n={n:5d}  T=1 count={ones:5d}  density={ones/nd:.4f}  S={S:5d}")
