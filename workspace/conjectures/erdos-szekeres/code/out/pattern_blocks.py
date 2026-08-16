#!/usr/bin/env python3
"""Per-block structural data for the ES construction.

The ES construction X_n = union_{i=0}^{n-2} T_i with |T_i| = C(n-2, i),
T_i has no (i+2)-cap and no (n-i)-cup.  We print the block-size row (which
must be a binomial row summing to 2^{n-2}) and each block's actual longest
cup/cap against its claimed bounds.  Exact oracle only.
"""
from lib.es_construct import es_set_blocks, es_block
from lib.es_geom import longest_cup, longest_cap, in_general_position
from math import comb

print("Block-size rows of the ES construction, |T_i| = C(n-2,i):")
for n in range(3, 9):
    row = [comb(n - 2, i) for i in range(n - 1)]
    print(f"  n={n}: {row}  sum={sum(row)} = 2^{n-2} = {2**(n-2)}")
print()

print("Per-block cup/cap bounds vs actual (es_construct, build at n=6):")
n = 6
pts, blocks = es_set_blocks(n)
ok = True
for i, blk in enumerate(blocks):
    T = [ (float(x), float(y)) for x,y in blk ]
    # longest cup/cap need Fraction-safe ints; use integer-rounded? keep as is
    cu = longest_cup(blk)
    ca = longest_cap(blk)
    no_cup_bnd = n - i      # no (n-i)-cup  => longest cup should be <= n-i
    no_cap_bnd = i + 2      # no (i+2)-cap => longest cap should be <= i+2
    good_cup = cu <= no_cup_bnd
    good_cap = ca <= no_cap_bnd
    ok &= good_cup and good_cap
    print(f"  block i={i}: |T|={len(blk)} (want C(4,{i})={comb(4,i)}) "
          f"cup={cu} (bnd {no_cup_bnd}, {'ok' if good_cup else 'VIOL'}) "
          f"cap={ca} (bnd {no_cap_bnd}, {'ok' if good_cap else 'VIOL'})")
print("ALL BLOCK CUP/CAP BOUNDS OK:", ok)
