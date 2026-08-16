import numpy as np
ns = [8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
ws = [3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239]
lnn=np.log(np.array(ns,float)); lnw=np.log(np.array(ws,float))
for lo in [8,9,10,11,12]:
    idx=list(range(lo,len(ns)))
    x=lnn[idx]; y=lnw[idx]
    A=np.vstack([x,np.ones_like(x)]).T
    coef,*_=np.linalg.lstsq(A,y,rcond=None)
    resid=y-A@coef; n=len(x); s2=(resid@resid)/(n-2)
    se=np.sqrt(s2/(((x-x.mean())**2).sum()))
    print(f"last {len(idx)} pts (from n={ns[lo]}): alpha={coef[0]:.4f} +- {se:.4f}  C={np.exp(coef[1]):.4f}")

print("\ncandidates at large-n (exponent, predicted w(32768)):")
for name,e in [("1/2",0.5),("log4(3)=ln3/ln4",np.log(3)/np.log(4)),
               ("ln3/ln4",np.log(3)/np.log(4)),("log_3(2)?",np.log(2)/np.log(3)),
               ("ln2/ln3",np.log(2)/np.log(3)),("0.55",0.55),("0.565",0.565)]:
    idx=list(range(9,len(ns)))
    lnC=(lnw[idx]-e*lnn[idx]).mean()
    pred=np.exp(e*np.log(32768)+lnC)
    print(f"  {name:18s} e={e:.4f}  pred w(32768)={pred:.1f} (actual 239)")
