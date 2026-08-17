#!/usr/bin/env python3
"""liu_c3_sweep.py — honest density sweep for Liu's C3 class.

Purpose: the plain multistart MIN E_M[X] s.t. objective>=1 on the full
9-d + beta C3 class collapses to a DEGENERATE point (mass concentrated on a
single atom where D=E_M[h(X)]->0), reporting a spurious E_M[X]=0 / c=1.
That is a vacuous over-certification (the documented degenerate-atom hole),
NOT a certificate of density 1/2.

The meaningful question is: at a FIXED target density E_M[X]=t, is there a
point of the class with objective N/D >= 1?  If the largest objective
attainable at E_M[X]=t is >=1, then C3 certifies that density t (-c=1-t);
if at t=0.5 it stays below 1, C3 is capped and cannot certify density 1/2.

So we sweep t over a grid and, for each t, MAXIMISE objective subject to the
equality constraint E_M[X]=t and a D floor (non-degeneracy), then report
whether max objective >= 1 at that t and how close.

Honesty: verified-numerically (scipy SLSQP from many starts), NOT a proof.
"""
import time
import numpy as np
from scipy.optimize import minimize

# ---- same objective as liu_c3_attack.py ------------------------------------
def h(x):
    x = np.asarray(x, dtype=float); x = np.clip(x, 0.0, 1.0)
    if x.ndim == 0:
        if x <= 0.0 or x >= 1.0: return 0.0
        return -x*np.log(x) - (1-x)*np.log(1-x)
    out = np.zeros_like(x); m = (x>0.0)&(x<1.0); xm = x[m]
    out[m] = -xm*np.log(xm) - (1-xm)*np.log(1-xm)
    return out

def coupled_arg(x, y):
    return x*y + x*y*(1.0-x)*(1.0-y)

def evaluate(params):
    a1, a2, q, b0, b2, b4, b1, b3, b5, beta = params
    a3 = 1.0 - a1 - a2
    qbar = 1.0 - q
    if a3 < -1e-14 or a3 > 1.0: return 0.0, np.inf, 0.0
    a3 = min(max(a3, 0.0), 1.0)
    P0v = np.array([b0, b2, b4]); P1v = np.array([b1, b3, b5])
    w3 = np.array([a1, a2, a3])
    Mv = np.concatenate([P0v, P1v]); Mw = np.concatenate([w3*qbar, w3*q])
    D = Mw[0]*h(Mv[0])+Mw[1]*h(Mv[1])+Mw[2]*h(Mv[2])+Mw[3]*h(Mv[3])+Mw[4]*h(Mv[4])+Mw[5]*h(Mv[5])
    E_iidM = 0.0
    for i in range(6):
        for j in range(6):
            E_iidM += Mw[i]*Mw[j]*h(Mv[i]*Mv[j])
    def Ec(atomv, wts):
        tot = 0.0
        for i in range(3):
            for j in range(3):
                tot += wts[i]*wts[j]*h(coupled_arg(atomv[i], atomv[j]))
        return tot
    EcP0 = Ec(P0v, w3); EcP1 = Ec(P1v, w3)
    N = (1.0-beta)*E_iidM + beta*(qbar*EcP0 + q*EcP1)
    if D <= 1e-12: return 0.0, np.inf, D
    EMX = qbar*(a1*b0+a2*b2+a3*b4) + q*(a1*b1+a2*b3+a3*b5)
    return EMX, N/D, D

C_PRIME = 0.382709087918741

def max_obj_at_density(t, n_starts=500, seed=0):
    """Maximise objective over C3 with E_M[X] == t (equality) and D>=floor.
    Returns (best_obj, best_x, n_feasible_pts_checked)."""
    rng = np.random.default_rng(seed)
    bnd = [(0.0,1.0)]*10
    best = -1e9; best_x=None
    for k in range(n_starts):
        x0 = rng.uniform(0,1,10)
        if rng.random()<0.5: x0[2]=rng.random()*0.2
        # start near the two-atom q=0 structure to help the optimiser
        cons = ({"type":"ineq","fun":lambda x: 1.0-x[0]-x[1]},
                {"type":"ineq","fun":lambda x: evaluate(x)[2]-1e-8},
                {"type":"eq","fun":lambda x: evaluate(x)[0]-t})
        def pen(x):
            EMX, obj, D = evaluate(x)
            if D<=1e-12: return 1e6
            return -obj + abs(EMX-t)*1e6   # maximise objective, hard tie to t
        res = minimize(pen, x0, method="SLSQP", bounds=bnd, constraints=cons,
                       options={"maxiter":300,"ftol":1e-11})
        EMX, obj, D = evaluate(res.x)
        if D>1e-12 and abs(EMX-t)<1e-3 and obj>best:
            best, best_x = obj, res.x.copy()
    return best, best_x

def main():
    print("liu_c3_sweep.py — density sweep over Liu C3 (objective>=1 feasibility)")
    print("question: is objective N/D >= 1 feasible at E_M[X]=t for t down to 0.5?")
    print("if yes at t=0.5, C3 certifies density 1/2; else it is capped.")
    print("verified-numerically, NOT a proof.  D floor = 1e-8.")
    print()
    # the record point for reference
    p=0.893604513905457; x=0.690787593924988; b=0.100052559862974
    _,obj_rec,_=evaluate((p,0.0,0.0,x,0.0,0.0,0.5,0.5,0.5,b))
    print(f"Liu record point: E_M[X]=1-c'={1-C_PRIME:.6f}, objective={obj_rec:.6f}")
    print(f"(record c'={C_PRIME:.10f}; iid cap (3-sqrt5)/2={(3-np.sqrt(5))/2:.6f})")
    print("-"*78)
    tvals = [0.50,0.52,0.54,0.56,0.58,0.60,0.6173,0.62,0.64,0.66,0.68,0.70]
    print(f"{'E_M[X]=t':>10} {'max objective':>14} {'>=1?':>5}  c=1-t   verdict")
    for t in tvals:
        obj, bx = max_obj_at_density(t, n_starts=700)
        ok = obj >= 1.0 - 1e-6
        verdict = "certifies" if ok else "NOT certified"
        print(f"{t:10.4f} {obj:14.6f} {'YES' if ok else 'no':>5}  {1-t:6.4f}  {verdict}")
        if bx is not None:
            a=["a1","a2","q","b0","b2","b4","b1","b3","b5","beta"]
            print(f"           argmax={{{', '.join(f'{a[i]}={bx[i]:.4f}' for i in range(10))}}}")

if __name__=="__main__":
    main()
