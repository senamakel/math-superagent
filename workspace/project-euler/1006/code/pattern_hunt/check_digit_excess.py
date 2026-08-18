"""Compute C(k) = len(Psi(k)) - (2k-1), the digit-excess staircase, exactly up to
KMAX via the fast in-run-pipeline route for small k (from recorded exact values)
plus the sliding-window residue? No -- we need the exact decimal length, not a
residue. Use the right-extension recurrence pipeline to get exact Psi(k) for
moderate k quickly: Psi(k+1)=100Psi(k)+100V(R_k)^2+20S1(k)+c1(k+1), with V(R_k)
and S1(k) from recorded vR_exact.txt / s1_exact.txt.  True exact digits.

Then report the transition points where C(k) steps up, and test whether the
transition points t_c = min{k : C(k)>=c} are close to floor(some_j * phi^2 / 10^p)
or follow a pattern.  We only have V/S1 recorded up to k=3000, so this gives
exact C(k) up to ~3000 -- enough to see the transitions at 23, 256, 2568 and the
next at ~25684? No, 25684 > 3000.  Use the mechanical/file route would be slow.
Instead: compute C(k) up to 3000 and extrapolate the transition-sequence:
t1=23 (0->1), t2=256, t3=2568, ... test whether t_c ~ floor(e^? ) or ~ 10^c * const.

Observation to test: t_c approx (1/1.618)^c * 10^{c} ?  Let's look at ratios:
23, 256, 2568: each ~10x the previous.  If t_c ~ alpha * 10^c, then log10(t_c/c)... 
Check whether the mantissa of t_c has a limit.  t1=23 ~ 2.3*10^1, t2=256~2.56*10^2,
t3=2568~2.568*10^3.  Mantissa ~ 2.3, 2.56, 2.568 ... looks like it approaches
something. Compute the first-digit behavior.
"""
import sys
sys.set_int_max_str_digits(20000)
import mpmath as mp
mp.mp.dps = 60

def load_pairs(path):
    out = {}
    for line in open(path):
        p = line.split()
        if len(p) >= 2:
            out[int(p[0])] = int(p[1])
    return out

vR = load_pairs("code/out/vR_exact.txt")
s1 = load_pairs("code/out/s1_exact.txt")
PHI2_INV = mp.mpf(1) / ((1 + mp.sqrt(5)) / 2) ** 2
def c1(k):
    return 1 + int(mp.floor(k * PHI2_INV))

KMAX = 3000
Psi = {1: 1}
for k in range(1, KMAX):
    Psi[k+1] = 100*Psi[k] + 100*vR[k]**2 + 20*s1[k] + c1(k+1)

C = {}
for k in range(1, KMAX+1):
    C[k] = len(str(Psi[k])) - (2*k-1)

# transitions: first k where C(k) >= c
trans = []
cprev = C[1]
for k in range(2, KMAX+1):
    if C[k] > cprev:
        trans.append((k, C[k], C[k-1], Psi[k]))
        cprev = C[k]
print("transitions (k, newC, oldC) up to KMAX=%d:" % KMAX)
for t in trans:
    print("  ", t[0], t[1], t[2])
print("number of transitions found:", len(trans))
# Mantissa analysis: express transition k as mantissa * 10^(digits-1)
print("\nmantissa of each transition:", [f"{t[0]/10**(len(str(t[0]))-1):.9f}" for t in trans])
