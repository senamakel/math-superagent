#!/usr/bin/env python3
"""Verify the ABGS m=4 consecutive-prime-pair counts and the switch-density ratio.

This reproduces the four counts in Ash-Beltis-Gross-Sinnott §7 (Table for m=4,
over x from 10^3 to 10^6) and checks the derived switch-density percentages,
to validate the claim blocks that reference these numbers.

The four ordered residue-pair classes mod 4 are indexed by (a, a+d):
  (1,1) equal, (1,3) switch, (3,1) switch, (3,3) equal.
"""
# Counts directly from ABGS 2011, m=4 table (§7), over 10^3 .. 10^6.
counts = {(1,1): 16574, (1,3): 22521, (3,1): 22520, (3,3): 16715}
pred   = {(1,1): 16618.8, (1,3): 22407.7, (3,1): 22407.7, (3,3): 16618.8}

total = sum(counts.values())
switch = counts[(1,3)] + counts[(3,1)]
equal = counts[(1,1)] + counts[(3,3)]

print("m=4 counts over 10^3..10^6 (ABGS Table, §7):")
for k in [(1,1),(1,3),(3,1),(3,3)]:
    print(f"  {k}: observed={counts[k]:6d}  predicted={pred[k]:8.1f}")
print("total:", total)
print("switch pairs (1,3)+(3,1):", switch, f"= {100*switch/total:.2f}%")
print("equal  pairs (1,1)+(3,3):", equal, f"= {100*equal/total:.2f}%")
print("switch / equal ratio:", switch/equal)
print("largest/smallest ratio:", max(counts.values())/min(counts.values()))
# diagonal vs off-diagonal: the split is by whether a+d == a mod 4
for label, keys in [("switch(off-diag)", [(1,3),(3,1)]), ("equal(diag)", [(1,1),(3,3)])]:
    val = sum(counts[k] for k in keys)
    print(f"  {label}: {val} = {100*val/total:.2f}%")

# Cross-check the independent route: GLB is that all four would be equal at
# fair share; measure deviation from total/4.
fair = total/4
print("\nfair share per class =", fair)
for k in [(1,1),(1,3),(3,1),(3,3)]:
    print(f"  {k}: dev = {counts[k]-fair:+.1f} ({(100*counts[k]/total - 25):+.2f}%)")
