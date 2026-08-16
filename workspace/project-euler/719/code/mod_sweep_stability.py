#!/usr/bin/env python3
"""Does the mod-filter sweep's 'stronger' residue set reflect a provable rule
or an overfit to the 406 observed roots?

The mod-9 rule (m in {0,1} mod 9) is provable (digit-sum invariant). For a
general modulus q, 10^k != 1 mod q, so there is no such invariant. A residue
set observed on 406 roots is weak evidence; the question is whether the
'small residue count' for composite q is stable under splitting the sample.
If it is a genuine forced filter, two disjoint halves should give the SAME
allowed residue set; if it is overfit noise, they will differ."""
import re, random

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
R = [r for r in roots if 2 <= r <= 10**6]
assert len(R) == 406, len(R)
S = set(R)

def residue_count(seq, q):
    return len({r % q for r in seq})

# Theoretical mod-9-consistent count at modulus q: residues r with r%9 in {0,1}
def mod9_consistent_count(q):
    return sum(1 for r in range(q) if r % 9 in (0, 1))

random.seed(12345)
half = random.sample(R, len(R)//2)
half2 = [r for r in R if r not in set(half)]
print(f"Samples: full={len(R)}, halfA={len(half)}, halfB={len(half2)}")
print(f"{'q':>6} {'full#':>5} {'consist(mod9)':>14} {'halfA#':>6} {'halfB#':>6} {'A∩B':>5}")
for q in [18, 27, 36, 81, 99, 180, 720, 990, 1620, 1980, 1998]:
    f = residue_count(R, q)
    a = residue_count(half, q)
    b = residue_count(half2, q)
    inter = len({r % q for r in half} & {r % q for r in half2})
    consist = mod9_consistent_count(q)
    print(f"{q:>6} {f:>5} {consist:>14} {a:>6} {b:>6} {inter:>5}")

print()
print("Interpretation: a forced filter => halfA and halfB agree on allowed")
print("residue classes (A∩B == full count, and == a == b). If they disagree,")
print("the reduced residue set is a finite-sample artifact, not a rule.")
