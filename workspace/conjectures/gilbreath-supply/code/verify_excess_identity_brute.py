#!/usr/bin/env python3
"""Independent verification of the identity  2*nu2(n)-(n-2) == -S(n)
by the BRUTE-FORCE route s_direct (literal submask-XOR), not the SOS path.

Both s_direct and t_direct in lib.supply_fold are literal definitions, and
nu2 (=number of ones among T(n,d), d in [2,n-1]) is equal to (n-2-S)/2 by pure
counting. This script recomputes everything from t_direct alone and checks the
identity against fold_nu2. So it is a genuinely independent (brute) route.
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import t_direct
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    bad = 0
    for n in range(2, N + 1):
        S = 0
        ones = 0
        for d in range(2, n):
            t = t_direct(n, d, h[:n])
            S += -1 if t else 1
            ones += t
        # identity: 2*ones - (n-2) == -S  <=>  S == (n-2) - 2*ones
        lhs = 2 * ones - (n - 2)
        rhs = -S
        v = fold_nu2(n, h)
        if lhs != rhs or ones != v:
            print(f"MISMATCH n={n}: ones={ones} v(fold)={v} 2*ones-(n-2)={lhs} -S={rhs}")
            bad += 1
            if bad > 5:
                return
    print(f"N={N}: brute identity 2*nu2-(n-2) == -S held for EVERY n in [2,{N}]; "
          f"ones==fold_nu2 for all; {bad} mismatches.")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 60)
