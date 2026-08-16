import numpy as np
ns = [128,256,512,1024,2048,4096,8192,16384,32768]
ws = [11,16,24,35,52,77,112,164,239]

# Model A: w = C n^alpha  (pure power)
# Model B: w = C n^{1/2} (log n)^beta
# Model C: w = C n^alpha (log n)^beta
lnn=np.log(np.array(ns,float)); lnw=np.log(np.array(ws,float)); ll=np.log(lnn)

def fit(X,y):
    ones=np.ones((y.size,1))
    A=np.hstack([X.reshape(-1,1) if X.ndim==1 else X, ones])
    coef,*_=np.linalg.lstsq(A,y,rcond=None)
    resid=y-A@coef; n=len(y); dof=n-coef.size; s2=(resid@resid)/dof
    cov=s2*np.linalg.inv(A.T@A)
    se=np.sqrt(np.diag(cov))
    return coef,se,resid

# Model A: ln w = alpha ln n + ln C
for lo in [0,2,4]:
    idx=range(lo,len(ns)); coef,se,r=fit(lnn[idx],lnw[idx])
    print(f"A pure power  from n={ns[lo]}: alpha={coef[0]:.4f}+-{se[0]:.4f} C={np.exp(coef[1]):.3f} resid_std={r.std():.4f}")

# Model B: ln w = 0.5 lnn + beta lnlnn + lnC  =>  y-0.5x = beta*ll + lnC
print("\nModel B (n^0.5 (ln n)^beta):")
yb = lnw - 0.5*lnn
coef,se,r=fit(ll,yb)
print(f"  beta={coef[0]:.4f}+-{se[0]:.4f}  resid_std={r.std():.4f}  (beta should be stable if model right)")
for lo in [0,3,5]:
    idx=range(lo,len(ns)); c,se2,r2=fit(ll[idx],yb[idx])
    print(f"    from n={ns[lo]}: beta={c[0]:.4f}+-{se2[0]:.4f} resid_std={r2.std():.4f}")

# Model C: ln w = alpha lnn + beta lnlnn + lnC
print("\nModel C (n^alpha (ln n)^beta):")
X=np.vstack([lnn,ll]).T
coef,se,r=fit(X,lnw)
print(f"  alpha={coef[0]:.4f}+-{se[0]:.4f}  beta={coef[1]:.4f}+-{se[1]:.4f}  resid_std={r.std():.4f}")

# evaluate prediction quality at large n for each model
# B with fitted beta ~ use all data
print("\npredicted w(32768):")
# model B
bv = (yb).__class__  # dummy
coefB,seB,_=fit(ll,yb)
predB=np.exp(0.5*np.log(32768)+coefB[0]*np.log(np.log(32768))+coefB[1])
print(f"  B n^0.5(lnn)^{coefB[0]:.3f}: {predB:.1f} (actual 239)")
coefA,_,_=fit(lnn[:-1],lnw[:-1])
predA=np.exp(coefA[0]*np.log(32768)+coefA[1])
print(f"  A n^{coefA[0]:.3f} (fit to <32768): {predA:.1f}")
