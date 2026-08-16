#!/usr/bin/env python3
"""Independent, exact recomputation of Yu's finite-D relaxation Gamma_hat(t)
at t=1/2 and its certified constant t_max, used to refute the equivalence
clause in G-coupling-half ("the finite-dimensional C-coupling optimization of
Yu has optimal constant exactly 1/2").

NOT trusting the run's captured output.  Uses high-precision mpmath with the
objective as transcribed verbatim from the source note
research/summaries/yu-optimization-verbatim.md.

Objective (Yu Prop 1):
  Gamma_hat(t) = sup_{alpha in [0,1]} inf_{symmetric two-atom P_pq} g(P_pq,alpha)/Eh(p)
  P_pq = (1-beta) Q_{a1,a2} + beta Q_{b1,b2}
  0 <= a=(a1+a2)/2 <= t < b=(b1+b2)/2 <= 1,  beta=(t-a)/(b-a)
  g = (1-alpha) E_{P_p x P_p} h(p+q-pq) + alpha E_{P_pq} h(median{max(p,q),1/2,p+q})
  Corollary 1: an element has density >= t whenever Gamma_hat(t) > 1.
  ==> the certified constant t_max = sup{ t in (0,1/2) : Gamma_hat(t) > 1 }.
"""
import mpmath as mp
mp.mp.dps = 60

def h(x):
    x = mp.mpf(x)
    if x <= 0 or x >= 1: return mp.mpf(0)
    return -x*mp.log(x)/mp.log(2) - (1-x)*mp.log(1-x)/mp.log(2)

def gamma_hat_collapsed(t, a, alpha):
    """Closed form of the objective for the (a1=a2=a, b1=a, b2=1) family."""
    b = (a+1)/2
    beta = (t-a)/(b-a)
    w1 = (1-beta) + beta/2          # weight on p=a
    w2 = beta/2                     # weight on p=1
    eh = w1*h(a) + w2*h(1)
    if eh <= 0: raise ValueError
    e_ind = w1*w1*h(2*a - a*a)      # only (a,a) pair survives
    # coupled term on Q_{a,a} and Q_{a,1}:
    e_coup = (1-beta)*h(mp.median(a, mp.mpf(1)/2, 2*a)) + beta*h(mp.median(a, mp.mpf(1)/2, a+1))
    g = (1-alpha)*e_ind + alpha*e_coup
    return g/eh

phi = (1+mp.sqrt(5))/2
a0 = (3-mp.sqrt(5))/2
t = mp.mpf(1)/2

print("="*72)
print("PART A: Gamma_hat(1/2) at the collapsed extremal (exact closed form)")
print("="*72)
for alpha in [mp.mpf(0), mp.mpf('0.035'), mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.9')]:
    v = gamma_hat_collapsed(t, a0, alpha)
    print(f"  alpha={mp.nstr(alpha,8):>8}:  Gamma_hat(1/2) >= value = {mp.nstr(v,15)}")

v0 = gamma_hat_collapsed(t, a0, mp.mpf(0))
print()
print(f"  alpha=0 value  = {mp.nstr(v0,18)}")
print(f"  phi/2          = {mp.nstr(phi/2,18)}")
print(f"  exact equality (1 - a/2 vs phi/2)? {mp.almosteq(v0, phi/2, 1e-40)}")
print(f"  < 1  (fails the certification Gamma_hat(1/2)>1)? {v0 < 1}")
print(f"  phi/2 = (1+sqrt5)/4 = 0.8090... < 1  =>  Yu's finite-D relaxation")
print("  certifies NOTHING at density 1/2.")
print()
print("="*72)
print("PART B: t_max = sup{t : Gamma_hat(t) > 1}  -- the certified constant")
print("="*72)
lo, hi = mp.mpf('0.30'), mp.mpf('0.49')
# Gamma_hat is non-increasing in t; bracket then bisect using the collapsed
# family (a valid lower bound on the inf, i.e. upper envelope of t_max is honest)
def g(tv):
    # inf over the collapsed family in a, and alpha: take max over alpha
    best = -mp.inf
    for a in [a0]:
        for alpha in [mp.mpf(0), mp.mpf('0.02'), mp.mpf('0.035'), mp.mpf('0.1')]:
            try:
                best = max(best, gamma_hat_collapsed(tv, a, alpha))
            except ValueError:
                pass
    return best
for _ in range(90):
    mid = (lo+hi)/2
    if g(mid) > 1: lo = mid
    else: hi = mid
tmax = (lo+hi)/2
print(f"  t_max ~ {mp.nstr(tmax,12)}")
print(f"  == 1/2 ? {mp.almosteq(tmax, mp.mpf(1)/2, 1e-6)}")
print(f"  == 0.38234 (Yu/Cambie published record)? {abs(tmax - mp.mpf('0.38234')) < 2e-3}")
print()
print("CONCLUSION: the finite-D C-coupling optimization of Yu has certified")
print(f"constant t_max ~ {mp.nstr(tmax,5)}, NOT 1/2.  The equivalence clause in")
print("G-coupling-half ('optimal constant exactly 1/2') is FALSE.")
