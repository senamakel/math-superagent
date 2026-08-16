"""Candidate 0005: expose a callable returning the parameter tuple.

Rule: Yu's published certified witness alpha=0.035, a1=a2=b1=0.3300622, b2=1.
This candidate exposes a function that returns the five parameters, so the
harness can feed them to the unmodified score.py.
"""
def candidate():
    return (0.035, 0.3300622, 0.3300622, 0.3300622, 1.0)
