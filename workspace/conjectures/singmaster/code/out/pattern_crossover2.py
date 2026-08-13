import math
phi=(1+math.sqrt(5))/2
A=math.log(phi)
for eps in [0.24,0.30,1/3-0.001,1/3,0.34,0.40,0.50]:
    bnd=[]; int_=[]
    for j in range(1,2001):
        lnn=(4*j+5)*A - math.log(5)   # log n ~ (4j+5)A - log5 (n~phi^{4j+5}/5)
        lnk=(4*j+3)*A - math.log(5)
        cutpow=lnn**(2/3+eps)
        (bnd if lnk<cutpow else int_).append(j)
    print("eps=%.4f: last boundary j=%d, first interior j=%d, count boundary=%d of 2000"%(
        eps, max(bnd) if bnd else -1, min(int_) if int_ else -1, len(bnd)))
