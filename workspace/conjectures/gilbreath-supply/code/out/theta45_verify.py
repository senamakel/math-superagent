import math
n = [64,128,256,512,1024,2048,4096,8192,16384,32768]
w = [7,11,16,24,35,52,77,112,164,239]
lx=[math.log2(x) for x in n]
ly=[math.log2(x) for x in w]
print("log2 n:", [f"{x:.3f}" for x in lx])
print("log2 w:", [f"{x:.3f}" for x in ly])

# per-doubling slope
print("\nper-doubling slopes:")
for i in range(1,len(n)):
    print(f"  {n[i]:6d} {(ly[i]-ly[i-1])/(lx[i]-lx[i-1]):.3f}")

# tail >= 1024 (index 4..)
lo=4
xs=lx[lo:]; ys=ly[lo:]
xb=sum(xs)/len(xs); yb=sum(ys)/len(ys)
Sxx=sum((x-xb)**2 for x in xs); Sxy=sum((x-xb)*(y-yb) for x,y in zip(xs,ys))
a=Sxy/Sxx; c=yb-a*xb
print(f"\ntail n>=1024: slope a={a:.4f} intercept={c:.4f}")
resid=[y-(c+a*x) for x,y in zip(xs,ys)]
print("residuals:", [f"{r:+.3f}" for r in resid])
import statistics
print("resid std:", statistics.pstdev(resid))
# std err of slope
se2=sum(r*r for r in resid)/(len(xs)-2)/Sxx
print("slope SE:", math.sqrt(se2), " |a-0.5|/SE =", abs(a-0.5)/math.sqrt(se2))

# full-table slope
xb=sum(lx)/len(lx); yb=sum(ly)/len(ly)
Sxx=sum((x-xb)**2 for x in lx); Sxy=sum((x-xb)*(y-yb) for x,y in zip(lx,ly))
a2=Sxy/Sxx; c2=yb-a2*xb
resid2=[y-(c2+a2*x) for x,y in zip(lx,ly)]
print(f"\nfull table: slope={a2:.4f} resid-std={statistics.pstdev(resid2):.4f}")

print("\nw/sqrt(n):", [f"{wi/math.sqrt(ni):.3f}" for wi,ni in zip(w,n)])
print("w/(sqrt ln n):", [f"{wi/(math.sqrt(ni)*math.log(ni)):.3f}" for wi,ni in zip(w,n)])
print("w/n^0.7925:", [f"{wi/ni**0.7925:.4f}" for wi,ni in zip(w,n)])

# nested: log w = lnC + 0.5 ln n + beta ln(ln n), n>=1024
import numpy as np
nn=np.array(n[lo:],float); ww=np.array(w[lo:],float)
lnn=np.log(nn); lnl=np.log(lnn); lww=np.log(ww)
A=np.vstack([np.ones(len(nn)), lnl]).T
coef,res,*_=np.linalg.lstsq(A, lww-0.5*lnn, rcond=None)
print("\nnested beta (fix a=1/2):", coef[1], "resid-std:", np.sqrt((res@res)/len(res)))
A=np.vstack([np.ones(len(nn)), lnn, lnl]).T
coef,res,*_=np.linalg.lstsq(A,lww,rcond=None)
dof=len(nn)-3; s2=(res@res)/dof; cov=s2*np.linalg.inv(A.T@A); se=np.sqrt(np.diag(cov))
print("full a,beta,lnC:", coef, "+-", se)
