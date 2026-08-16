"""Candidate 0001: Yu's published certified witness (module-path contract).

Rule: alpha=0.035, a1=a2=b1=0.3300622, b2=1.0. This is the exact point Yu's
paper uses to certify density t=0.38234 with Gamma_hat >= 1.00000889.

The scorer (score.py) reads the five parameters FROM THIS MODULE via its
module-path contract (module-level lowercase alpha/a1/a2/b1/b2, plus the
PARAMS list as a fallback), verifies every constraint with rigorous interval
arithmetic, and prints the certified SCORE line. The harness invokes exactly
`python3 score.py candidates/c0001.py`, so the candidate must be a passive
data module, NOT a program that spawns the scorer.

Fixed: this module used to run score.py as a subprocess with five positional
floats (the OLD contract), which printed "INVALID: candidate module not
found: 0.035" and never surfaced a SCORE: line to the harness. Now it simply
exposes the parameters the scorer's module-path contract reads.
"""
alpha = 0.035
a1 = 0.3300622
a2 = 0.3300622
b1 = 0.3300622
b2 = 1.0

PARAMS = [alpha, a1, a2, b1, b2]

def params():
    return (alpha, a1, a2, b1, b2)
