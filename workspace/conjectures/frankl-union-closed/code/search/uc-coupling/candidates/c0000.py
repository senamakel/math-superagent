"""Candidate 0000: probe the harness contract (module-path contract).

This module encodes Yu's published certified witness parameters
(alpha=0.035, a1=a2=b1=0.3300622, b2=1.0) as the candidate point.

The scorer (score.py) reads the five parameters FROM THIS MODULE via its
module-path contract. Fixed: this module originally exposed only UPPERCASE
ALPHA/A1/A2/B1/B2, which the scorer does not read (it reads lowercase
alpha/a1/a2/b1/b2, or a params()/PARAMS/point). So the scorer found no
readable parameters and printed "INVALID: candidate exposes no readable
parameters". Now lowercase scalars + PARAMS + params() are exposed, matching
the contract the harness actually calls.
"""
alpha = 0.035
a1 = 0.3300622
a2 = 0.3300622
b1 = 0.3300622
b2 = 1.0

PARAMS = [alpha, a1, a2, b1, b2]

def params():
    return (alpha, a1, a2, b1, b2)
