"""Candidate 0006: expose PARAMS as a list via a function attribute probe.

Rule: Yu's published certified witness alpha=0.035, a1=a2=b1=0.3300622, b2=1.
This candidate exposes a function `solve` returning param dict and a module-level
`params` dict, covering multiple plausible import contracts at once.
"""
def solve():
    return dict(alpha=0.035, a1=0.3300622, a2=0.3300622, b1=0.3300622, b2=1.0)

params = dict(alpha=0.035, a1=0.3300622, a2=0.3300622, b1=0.3300622, b2=1.0)
values = [0.035, 0.3300622, 0.3300622, 0.3300622, 1.0]
