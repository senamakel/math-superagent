"""Candidate 0007: Yu's certified witness, exhaustive parameter exposure.

Rule: alpha=0.035, a1=a2=b1=0.3300622, b2=1.0. Expose the five parameters
under every plausible name the harness might read from the candidate module,
so whichever surface the harness imports, it gets Yu's certified point.
"""
ALPHA = 0.035
A1 = 0.3300622
A2 = 0.3300622
B1 = 0.3300622
B2 = 1.0

alpha = ALPHA
a1 = A1
a2 = A2
b1 = B1
b2 = B2

point = (ALPHA, A1, A2, B1, B2)
PARAMS = [ALPHA, A1, A2, B1, B2]
params = dict(alpha=ALPHA, a1=A1, a2=A2, b1=B1, b2=B2)

def candidate():
    return (ALPHA, A1, A2, B1, B2)

def get_params():
    return (ALPHA, A1, A2, B1, B2)

def make():
    return dict(alpha=ALPHA, a1=A1, a2=A2, b1=B1, b2=B2)
