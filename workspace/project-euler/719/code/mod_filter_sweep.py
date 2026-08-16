#!/usr/bin/env python3
"""Attack the one untested structural angle: is there a *cheap modular filter*
stronger than the known mod-9 rule (m == 0 or 1 mod 9)?

The mod-9 rule comes from the digit-sum invariant: 10^k == 1 (mod 9), so any
block's value == its digit sum (mod 9), hence m = sum of blocks == sum of
digit-sums == m^2 (mod 9). That is EXHAUSTIVE only for q | 9, but a different
kind of invariant might hold for other q. We sweep small moduli q and ask:
what is the minimal residue set that contains all 406 S-roots m in [2,10^6],
and does any q cut below the 2/9 allowed by mod-9 (after CRT with mod-9)?
"""
import re
from math import gcd

B_FILE = "research/sources/oeis_a038206_b.full.md"
def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots

roots = load_roots(B_FILE)
R = [r for r in roots if 2 <= r <= 10**6]   # the 406 roots for T(10^12)
assert len(R) == 406, len(R)

def minimal_residues(seq, q):
    """sorted residue classes (mod q) present among seq"""
    return sorted({r % q for r in seq})

# Baseline: mod-9 -> residues {0,1}, i.e. 2 allowed classes out of 9.
base = minimal_residues(R, 9)
print("mod-9 residues among 406 roots:", base, f"-> {len(base)}/9 classes")

print("\nSweep small moduli q, report allowed classes vs q, and the CRT fraction")
print("relative to the mod-9 baseline (fraction of [2,1e6] surviving IF the")
print("set were actually the true filter — NOT a claim, just the reduction):")
print(f"{'q':>6} {'#cls':>5} {'frac':>10} {'residues'}")
order = []
for q in range(2, 2000):
    res = minimal_residues(R, q)
    frac = len(res) / q
    order.append((frac, len(res), q, res))
    # print anything that, combined with mod-9, is strictly stronger than mod-9
order.sort()
print("\nStrongest small-modulus restrictions (smallest allowed fraction):")
for frac, ncls, q, res in order[:25]:
    print(f"q={q:>5} allowed {ncls:>3}/{q:<5} frac={frac:.5f} residues={res[:12]}{'...' if len(res)>12 else ''}")
