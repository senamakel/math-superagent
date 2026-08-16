"""Candidate 0003: Yu's published certified witness, invoking the scorer in-process.

Rule: alpha=0.035, a1=a2=b1=0.3300622, b2=1.0 -- the exact point Yu's paper
uses to certify density t=0.38234 with Gamma_hat >= 1.00000889. We import the
scorer module (already on disk as score.py) and call its main() with argv set
to this candidate's five parameters, so the certified SCORE line is emitted.
"""
import os
import sys

# the five parameters of this candidate: (alpha, a1, a2, b1, b2)
alpha = 0.035
a1 = 0.3300622
a2 = 0.3300622
b1 = 0.3300622
b2 = 1.0

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
import score  # the unmodified scorer

for _f in list(sys.modules):
    if _f == "score" or _f.startswith("score."):
        pass
# point the scorer's argv at this candidate's parameters
sys.argv = ["score.py", str(alpha), str(a1), str(a2), str(b1), str(b2),
            "20000", "0.38234"]
score.main()
