#!/usr/bin/env python3
"""Quick probe: which interpretation of the C3 objective reproduces Liu's record
c'=0.382709087918741 at the point q=0, P0=p* d(x*) + (1-p*) d(0), beta=beta*?"""
import numpy as np

def h(x):
    x = np.asarray(x, float)
    x = np.clip(x, 0, 1)
    if x.ndim == 0:
        if x <= 0 or x >= 1: return 0.0
        return -x*np.log(x)-(1-x)*np.log(1-x)
    out = np.zeros_like(x)
    m = (x>0)&(x<1); xm=x[m]
    out[m] = -xm*np.log(xm)-(1-xm)*np.log(1-xm)
    return out

p_star=0.893604513905457
x_star=0.690787593924988
beta_star=0.100052559862974
cprime = 1-p_star*x_star

# P0 atoms: b0=x* w=a1=p*; b4=0 w=a3=1-p*.  q=0 so P1 irrelevant (weight 0)
w = np.array([p_star, 1-p_star])
v = np.array([x_star, 0.0])
D = w[0]*h(v[0]) + w[1]*h(v[1])   # = p* h(x*)

def coupled_arg(x,y, kind):
    if kind=="paper0":  # Pi(0,0)= sbar*tbar + sbar*s * tbar*t  with X=s,Y=t
        return (1-x)*(1-y) + ((1-x)*x)*((1-y)*y)
    if kind=="goal_lit": # XY + XY(1-X)(1-Y), XY=product
        return x*y + x*y*(1-x)*(1-y)
    if kind=="or_paper0": # Pi for OR interpretation
        return 1-coupled_arg(x,y,"paper0")
    raise ValueError

def eval_kind(kind, beta=beta_star):
    # iid M term & coupled term, q=0
    # iid: E_{P0 x P0}[h(arg)]  -- choose arg for "XY"
    # The task writes h(XY) for iid. Try two readings:
    Eiid=0.0
    for i in range(2):
        for j in range(2):
            a_ = v[i]*v[j]                  # product reading
            Eiid += w[i]*w[j]*h(a_)
    Ec=0.0
    for i in range(2):
        for j in range(2):
            Ec += w[i]*w[j]*h(coupled_arg(v[i],v[j],kind))
    N=(1-beta)*Eiid + beta*Ec
    return N, D, N/D, Eiid, Ec

print(f"p*={p_star:.12f} x*={x_star:.12f} beta*={beta_star:.12f}")
print(f"c'=1-p*x*={cprime:.15f} (paper 0.382709087918741)  -> E_M[X]=p*x*={p_star*x_star:.12f}")
print(f"D=p* h(x*)={D:.12f}")
for kind in ["goal_lit","paper0"]:
    N,Drat,obj,Eiid,Ec = eval_kind(kind, beta_star)
    print(f"\n[{kind}] Eiid={Eiid:.12f}  Ec={Ec:.12f}  N={N:.12f}  D={D:.12f}  obj=N/D={obj:.12f}")
    print(f"   objective>=1 ? {obj>=1.0}")

# What if coupled OR reading: use paper0 but we want h(1-Pi). Since h symmetric h(1-Pi)=h(Pi).
# So paper0 already symmetric-equivalent. Try goal_lit with "XY"=OR i.e arg=(x+y-xy):
def eval_or_everything():
    Eiid=0.0
    for i in range(2):
        for j in range(2):
            a_ = v[i]+v[j]-v[i]*v[j]   # OR reading
            Eiid += w[i]*w[j]*h(a_)
    Ec=0.0
    for i in range(2):
        for j in range(2):
            x,y=v[i],v[j]
            OR=x+y-x*y
            Ec += w[i]*w[j]*h(OR + OR*(1-x)*(1-y))
    N=(1-beta_star)*Eiid+beta_star*Ec
    return N,D,N/D,Eiid,Ec
N,Drat,obj,Eiid,Ec = eval_or_everything()
print(f"\n[OR reading everywhere] Eiid={Eiid:.9f} Ec={Ec:.9f} obj={obj:.9f}")
