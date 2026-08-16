"""Candidate 0009: Yu's published certified witness (module-path contract).

Rule: alpha=0.035, a1=a2=b1=0.3300622, b2=1.0 -- the exact point Yu's paper
uses to certify density t=0.38234 with Gamma_hat >= 1.00000889. The scorer
(score.py) reads these five module-level constants, verifies every constraint
with rigorous interval arithmetic, and prints the certified SCORE line.
"""
alpha = 0.035
a1 = 0.3300622
a2 = 0.3300622
b1 = 0.3300622
b2 = 1.0
