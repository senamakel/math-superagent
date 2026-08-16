import math

nlist  = [8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
wlist  = [3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239]
log43 = math.log(3)/math.log(4)

def ols(xs, ys):
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
    a=my-b*mx
    resid=[y-(a+b*x) for x,y in zip(xs,ys)]
    sse=sum(r*r for r in resid)
    return a,b,sse,resid

# Use the large-n tail consistently: n>=256 (the task tail)
idx=[i for i,n in enumerate(nlist) if n>=256]
nT=[nlist[i] for i in idx]; wT=[wlist[i] for i in idx]

print("== Model 1: w = c*n^E  (log2 w vs log2 n), tail n>=256 ==")
xs=[math.log2(n) for n in nT]; ys=[math.log2(w) for w in wT]
a,b,sse,resid=ols(xs,ys)
se=math.sqrt(sse/(len(xs)-2)/sum((x-sum(xs)/len(xs))**2 for x in xs))
print(f"  E={b:.5f} se={se:.5f}  |E-0.5|/se={abs(b-0.5)/se:.2f}  1/2 at {abs(b-0.5)/se:.1f} sigma")
print(f"  residuals: {['%+.4f'%r for r in resid]}")

print()
print("== Model 2: w = c*sqrt(n)*(log n)^g  (log2 w - 0.5 log2 n vs log2 log2 n) ==")
# test if some g makes residual flat: fit log2(w/sqrt n) = log2 c + g log2(log2 n)
xs=[math.log2(math.log2(n)) for n in nT]; ys=[math.log2(w)-0.5*math.log2(n) for w,n in zip(wT,nT)]
a,b,sse,resid=ols(xs,ys)
se=math.sqrt(sse/(len(xs)-2)/sum((x-sum(xs)/len(xs))**2 for x in xs))
print(f"  g={b:.4f} se={se:.4f}  (log-correction exponent; g=0 => pure sqrt)")
print(f"  residuals: {['%+.4f'%r for r in resid]}")

print()
print("== Model 3: w = c*log2(n)^? / n^log4(3) family ==")
# w / n^log43 should be constant if log43; check slope of log(w/n^log43) vs log n
xs=[math.log2(n) for n in nT]
ys=[math.log2(w)-log43*math.log2(n) for w,n in zip(wT,nT)]
a,b,sse,resid=ols(xs,ys)
print(f"  slope of log2(w/n^log43) vs log2 n = {b:.4f}  (should be 0 for log43 to hold; clearly not)")

print()
print("== Where does the exact-mean actually cross 0.40? (the mechanism) ==")
# Compute mean_n(w) exactly from the closed form over ALL n (not sampled)
# mean_n(w) = (1/n) sum_{d=2}^{n-1} P_d(w); P_d(w)=Pr[XOR odd].
# We only have w* per n; but let's test the Poisson approximation of the mechanism:
# check whether w* ~ n^{log2 3 - 2 + something}. mean ~ (1/n)sum (1-exp(-2 w 2^{pc}/n))/2.
# Leading sparse term (exp small): mean ~ (1/n)*sum w*2^{pc}/n = (w/n^2)*sum 2^{pc}.
# sum_{d=0}^{n-1} 2^{pc(d)} for n=2^m = 3^m = n^{log2 3}.
# => mean ~ w * n^{log2 3 - 2} = w n^{-0.415}.  w ~ 0.4 n^{0.415} would give E=0.415, not 0.557.
import numpy as np
print("  Leading sparse term predicts E = log2(3)-2 =", math.log(3)/math.log(2)-2, " (0.415)")
print("  Measured E ~ 0.557 => higher-order (multi-one) terms dominate; sparse leading term FAILS.")
