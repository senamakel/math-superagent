#!/usr/bin/env python3
"""Test self-similar families over ALL 408 roots (complete to 10^12)."""
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"

def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots

R = load_roots(B_FILE)
S = set(R)
print("total roots (complete to 10^12):", len(R))
print("max root:", max(R), "= sqrt(10^12):", max(R)**2 == 10**12)

# families present in full range
def present(v):
    return v in S

# A) powers of 10
p10 = [10**p for p in range(1, 8)]
print("\nA powers of 10:", [(p, present(p)) for p in p10])

# B) 9-repunits
rep9 = [10**p - 1 for p in range(1, 8)]
print("B 9-repunits:", [(p, present(p)) for p in rep9])

# C) 45-family 5*10^k*(10^{k+1}-1): 45, 4950, 499500, 49995000
famC = [5*(10**k)*(10**(k+1)-1) for k in range(6)]
print("C 45-family:", [(v, present(v)) for v in famC])

# D) 55-family? 55=1^2+... check 55, 5050, 500500 typical Kaprekar via 5*10^k+5
#    standard Kaprekar family: 55=55? let's check A037838-style: 55, 5050, 500500, 50005000
famD = [5*(10**(2*k)+10**k) for k in range(5)]  # (10^k)*(5*10^k+5)? compute
print("D attempt 5*(10^{2k}+10^k):", [(v, present(v)) for v in famD])
# 55 = 5*10+5; 5050=5*1000+50? 5050 = 5*10^3+5*10, 500500=5*10^5+5*10^2
famD2 = [5*(10**(2*k+1)+10**k) for k in range(5)]
print("D2 5*(10^{2k+1}+10^k):", [(v, present(v)) for v in famD2])

# E) 82-family: 82, 8200? classic 82^2=6724 (A|B). Extension 82, 820...?
#    kaprekar family for 82: 82^2=6724, 8+72+4... Let's instead find all
#    roots whose square-char matches. Hard; skip.

# F) Count how many roots are "structurally trivial" closed families:
#    10^p, 10^p-1, and the 45/4950/499500 family, vs total
trivial = set(p10) | set(rep9) | set(famC)
# subtract those > max
trivial = {v for v in trivial if v <= max(R)}
print("\nF trivial closed-family roots count:", len(trivial), "of", len(R))
print("   fraction:", len(trivial)/len(R))

# G) digit-count growth: count roots with each digit-count
import collections
byd = collections.Counter(len(str(r)) for r in R)
print("G roots by digit-count:", dict(sorted(byd.items())))
bydval = collections.Counter(len(str(r*r)) for r in R)
print("   roots by digit-count of m^2:", dict(sorted(bydval.items())))
