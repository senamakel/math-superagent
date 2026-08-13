#!/usr/bin/env python3
"""Print the exact residue-pair ambiguity witnesses for |a-b| mod 3, from the
already-run enumeration logic, with small explicit pairs (a,b) that share
residues but give different |a-b| mod 3. Pure enumeration, no library access
needed, run bounded."""
from itertools import product

# For each residue pair (r,s), collect possible |a-b| mod 3 over the range.
ambig = {}
for r, s in product(range(3), repeat=2):
    outs = {}
    for a in range(r, 22, 3):
        for b in range(s, 22, 3):
            v = abs(a - b) % 3
            outs.setdefault(v, []).append((a, b))
    if len(outs) > 1:
        ambig[(r, s)] = outs

print("Residue pairs (r,s) for which |a-b| mod 3 is NOT determined by (r,s):")
for (r, s), outs in sorted(ambig.items()):
    # a minimal witness: two pairs with different outcomes
    pairs = sorted(outs.items())[:2]
    desc = "; ".join(f"|a-b|={v} mod 3 via {lst[0]}" for v, lst in pairs)
    print(f"  residues ({r},{s}): {desc}")

print()
print("Total ambiguous residue pairs:", len(ambig), "/ 9")