#!/usr/bin/env python3
"""Test structural conjectures on the S-number roots (A038206) <= 10^6 (408 terms)."""
import re, collections

B_FILE = "research/sources/oeis_a038206_b.full.md"

def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots

R = [r for r in load_roots(B_FILE) if r <= 10**6]
S = set(R)
print("num roots <= 10^6:", len(R))

# 1) mod-9 necessity: every term congruent to 0 or 1 mod 9
bad = [r for r in R if r % 9 not in (0, 1)]
print("mod9 outside {0,1}:", bad[:10], "count", len(bad))

# 2) every Kaprekar number (2-block split) is an S-root: check a known set.
#    We test cheaply: a Kaprekar split is A|B with A+B=m (two halves).
def is_kaprekar(m):
    s = str(m*m)
    for cut in range(1, len(s)):
        a = int(s[:cut]); b = int(s[cut:])
        if a + b == m:
            return True
    return False
KAP = [r for r in R if is_kaprekar(r)]
print("Kaprekar (2-block) among roots:", len(KAP))
print("  examples:", KAP[:25])

# 3) self-similar families present
p10 = [10**p for p in range(1, 8)]
print("powers of 10 present:", [p for p in p10 if p in S])
rep9 = [10**p - 1 for p in range(1, 8)]
print("9-repunits present:", [p for p in rep9 if p in S])
# family 5*10^k*(10^{k+1}-1): 45, 4950, 499500, ...
famA = [5*(10**k)*(10**(k+1)-1) for k in range(0, 4)]
print("45-family (5*10^k*(10^{k+1}-1)):", [(v, v in S) for v in famA])
# family 1*10^k*(10^{k+1}-1) i.e. repunit-ish? 9,99,999 are (10^{k+1}-1)/... skip

# Count roots that are NOT Kaprekar but >= 2-block S-roots
print("non-2-block S-roots:", len(R) - len(KAP))

# 4) Count how many roots are powers of 10 or 9-repunits (trivial closed families)
trivial = sum(1 for r in R if r == 10**int(round(__import__('math').log10(r+1)))-1 or
              (10**int(__import__('math').log10(r)) == r))
print("trivial family count (powers of 10 / close):", trivial)

# 5) check suffix/prefix self-similarity: does 45 appear as suffix of 4950, 499500?
def suffix_family(m):
    s = str(m)
    # look for other roots whose decimal string begins with some prefix and ends with m's string
    out = []
    for r in R:
        sr = str(r)
        if sr.endswith(s):
            out.append(r)
    return out
for base in [45, 9, 10]:
    print(f"roots ending with '{base}':", suffix_family(base))
