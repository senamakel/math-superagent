#!/usr/bin/env python3
"""Confirm pure-bump parity depends on MAGNITUDES even at n=3, by scanning many
magnitude vectors for a FIXED strict ordering and showing parity varies.
Same ordering v0>v1>v2, many different concrete speed values -> does parity flip?
This settles whether the ordering-count model can ever be right."""
import sys, os
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_purebump_magnitude import pure_bump_parity

def main():
    # ordering (0,1,2): v0>v1>v2, fixed.  Scan magnitudes.
    # choose v0>v1>v2 with varied spread; record parity.
    found = {}
    for v0 in range(4, 8):
        for v1 in range(1, v0):
            for v2 in range(0, v1):
                p = pure_bump_parity(3, [F(v0), F(v1), F(v2)])
                found.setdefault(p, []).append((v0, v1, v2))
    for p, lst in sorted(found.items()):
        print(f"parity {p}: {len(lst)} vectors, e.g. {lst[:4]}")
    print("n=3 pure-bump parity DOES vary within fixed ordering (0>1>2):",
          len(found) > 1)
    # integral weight check: does 2/6 orderings mislead?  Compute exact measure
    # of even parity by integrating over the wedge v0>v1>v2>0 under Exp(1)?
    # Simpler: uniform density on this wedge is what the simplex model uses.
    # The true p(3,inf)=7/18 while order-count gives 1/3: so parity genuinely
    # varies within an ordering with non-zero probability.
    print("\nOrder-count model claims p(3,inf)=1/3; true limit from closed form 7/18=0.3889")
    print("=> parity varies within a single ordering (the two are incompatible)")

if __name__ == '__main__':
    main()
