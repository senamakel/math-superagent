#!/usr/bin/env python3
"""Determine monotonicity of the C3 objective in E_M[X] around the record point,
and hence the correct direction of the density-1/2 attack."""
import numpy as np
def h(x):
    x=np.asarray(x,float); x=np.clip(x,0,1)
    if x.ndim==0:
        if x<=0 or x>=1: return 0.0
        return -x*np.log(x)-(1-x)*np.log(1-x)
    out=np.zeros_like(x); m=(x>0)&(x<1); xm=x[m]
    out[m]=-xm*np.log(xm)-(1-xm)*np.log(1-xm)
    return out
def coupled_arg(x,y): return x*y + x*y*(1-x)*(1-y)

def obj(p,x,beta):
    # q=0 two-atom family P0=p d(x)+(1-p)d(0)
    w=np.array([p,1-p]); v=np.array([x,0.0])
    D=w[0]*h(v[0])+w[1]*h(v[1])
    Eiid=0.0; Ec=0.0
    for i in range(2):
        for j in range(2):
            Eiid+=w[i]*w[j]*h(v[i]*v[j])
            Ec+=w[i]*w[j]*h(coupled_arg(v[i],v[j]))
    N=(1-beta)*Eiid+beta*Ec
    return N/D, p*x

p_star=0.893604513905457; x_star=0.690787593924988; beta_star=0.100052559862974
print("record: obj=%.12f E=p*x=%.12f" % obj(p_star,x_star,beta_star))
print("\nVary E by changing x* (keep p*,beta*):")
for dx in [0.15,0.10,0.05,0.02,0.01,0.0,-0.01,-0.02,-0.05,-0.10,-0.15]:
    o,E=obj(p_star, max(0.01,x_star+dx), beta_star)
    print(f"  x={x_star+dx:+.3f}: E={E:.5f} obj={o:.6f} {'cert' if o>=1 else 'FAIL'}")
print("\nVary E by changing p* (keep x*,beta*):")
for dp in [0.05,0.02,0.01,0.0,-0.01,-0.02,-0.05]:
    o,E=obj(max(0.01,p_star+dp), x_star, beta_star)
    print(f"  p={p_star+dp:+.3f}: E={E:.5f} obj={o:.6f} {'cert' if o>=1 else 'FAIL'}")
