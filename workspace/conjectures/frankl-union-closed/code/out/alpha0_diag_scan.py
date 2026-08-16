#!/usr/bin/env python3
"""alpha0_diag_scan.py

Verify the diagonal subfamily a1=a2=a, b1=b2=1 (the achiever shape): the
alpha=0 iid-OR ratio R(a) = (1-beta) with beta given, and confirm it equals
phi/2 exactly at a=(3-sqrt5)/2 and exceeds phi/2 elsewhere in (0,0.5].

R(a): marginal has p=a with weight (1-beta) and p=1 with weight beta (h(1)=0),
beta=(t-a)/(1-a) with t=1/2, so (1-beta)=(0.5)/(1-a).  Since 2a-a^2=1-a at the
barrier root, the OR of two a's has entropy h(a), and the a,1 and 1,1 terms
vanish, so ratio = w1^2 h(a)/(w1 h(a)) = w1 = (1-beta) = 0.5/(1-a).
Check: at a=(3-sqrt5)/2, 0.5/(1-a) = phi/2 exactly.
"""
import math
from mpmath import mp, mpf, log
mp.dps = 60

def h(x):
    x=float(x)
    if x<=0 or x>=1: return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def R(a):
    t=0.5
    w1=(1-t)/(1-a)   # (1-beta)
    eor=w1*w1*h(2*a-a*a)
    eh=w1*h(a)
    return eor/eh

a0=(3-math.sqrt(5))/2
phi2=(1+math.sqrt(5))/4
print("a0=(3-sqrt5)/2 =", a0, "  phi/2 =", phi2)
print("R(a0) =", R(a0), "  w1=0.5/(1-a0) =", 0.5/(1-a0))
print()
print("scan R(a) over (0,0.5]:")
lo=1e9; lo_a=None
import numpy as np
for a in np.linspace(0.01,0.499,500):
    v=R(a)
    if v<lo: lo=v; lo_a=a
print("min R on grid:", lo, "at a=", lo_a)
print("phi/2 =", phi2)
print()
# exact ratio at a0 via mpmath h
def hm(x):
    x=mpf(x)
    if x<=0 or x>=1: return mpf(0)
    return -x*log(x)/log(2)-(1-x)*log(1-x)/log(2)
def Rm(a):
    a=mpf(a); t=mpf("0.5"); one=mpf(1)
    w1=(one-t)/(one-a)
    return w1*w1*hm(2*a-a*a)/(w1*hm(a))
print("mpmath R(a0) =", Rm(a0))
print("a0^2-3a0+1 =", a0*a0-3*a0+1)
print("0.5/(1-a0) - phi/2 =", 0.5/(1-a0)-phi2)
print("2a0-a0^2 vs 1-a0:", 2*a0-a0*a0, 1-a0)
