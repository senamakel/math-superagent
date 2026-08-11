import math
from fractions import Fraction

pi = math.pi

def best_a_b(d, n):
    """Among b in [0,n], find (b, a) minimizing |pi - a - b*sqrt(d)|; return (b,a,err)."""
    sd = math.sqrt(d)
    best_b, best_a, best_err = 0, round(pi), abs(pi - round(pi))
    for b in range(0, n+1):
        a = round(pi - b*sd)
        err = abs(pi - a - b*sd)
        if err < best_err:
            best_err, best_b, best_a = err, b, a
    return best_b, best_a, best_err

def convergents_of(x, limit):
    """Return list of (a,b) numerators... of continued fraction convergents p/q < limit."""
    cf = []
    # CF of x
    t = x
    res = []
    for _ in range(limit):
        ai = int(t)
        res.append(ai)
        t = t - ai
        if t < 1e-15: break
        t = 1.0/t
    # convergents
    p_2,q_2 = 0,1
    p_1,q_1 = 1,0
    out=[]
    for ai in res:
        p = ai*p_1 + p_2
        q = ai*q_1 + q_2
        p_2,q_2 = p_1,q_1
        p_1,q_1 = p,q
        out.append((p,q))
    return out

# Check the big oracle for d=2: does scanning find b=4375636191520, a=-6188084046055?
# We can't scan to 1e13. Instead verify the GIVEN b gives the claimed I, and check it's a convergent.
sd2 = math.sqrt(2)
b_given = 4375636191520
a_given = -6188084046055
print("d=2: verify given b,a:", a_given + b_given*sd2, "vs pi", pi)

# Test convergent hypothesis for d=2: is b_given a convergent denominator of pi*sqrt(2)?
print("\nConvergents of pi*sqrt(2):")
for p,q in convergents_of(pi*sd2, 50):
    if q > 4.5e11 and q < 4.6e12:
        print("  near p,q=",p,q)
    if q == b_given:
        pass
# print all convergent denominators up to 1e13
print("convergent q's of pi*sqrt2 up to ~1e13:")
for p,q in convergents_of(pi*sd2, 60):
    if q > 1e8:
        print(q, end=", ")
print()

# Check convergents of pi/sqrt(2) too
print("\nconvergent q's of pi/sqrt2:")
for p,q in convergents_of(pi/sd2, 60):
    if q > 1e8:
        print(q, end=", ")
print()

# Also record-b sequence for d=2 at small scale
print("\nRecord b's for d=2 within n=2e6 (new minima of |pi-a-b*sqrt2|):")
sd=sd2
best_err=1e9
recs=[]
for b in range(0, 2_000_000):
    a=round(pi-b*sd)
    err=abs(pi-a-b*sd)
    if err<best_err:
        best_err=err; recs.append(b)
print(recs[:40], "... count=",len(recs))
