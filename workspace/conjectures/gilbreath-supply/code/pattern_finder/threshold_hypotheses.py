import math

# exact-mean threshold weights w*(n) from the verified captures
nlist  = [8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
wlist  = [3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239]

log43 = math.log(3)/math.log(4)   # log_4(3) = 0.79248

print("n        w    w/sqrt(n)   w/(sqrt(n)ln n)  w/n^log4(3)   local-exp(dlog2w/dlog2n)")
print("-"*95)
prev_n=None; prev_w=None
slopes=[]
for n,w in zip(nlist,wlist):
    s=math.sqrt(n)
    ln=math.log(n)
    c1=w/s
    c2=w/(s*ln)
    c3=w/(n**log43)
    if prev_n is not None:
        slope=(math.log2(w)-math.log2(prev_w))/(math.log2(n)-math.log2(prev_n))
        slopes.append((n,slope))
    else:
        slope=float('nan')
    print(f"{n:6d} {w:4d}   {c1:10.5f}  {c2:14.6f}   {c3:10.5f}    {slope:8.4f}")
    prev_n,prev_w=n,w

print()
print("Local per-doubling slopes (d log2 w / d log2 n):")
for n,s in slopes:
    print(f"  -> {n:6d}: {s:.4f}")
last4=[s for n,s in slopes if n>=2048]
print("last four slopes:", ["%.4f"%s for s in last4], "mean=%.4f"% (sum(last4)/len(last4)))
last6=[s for n,s in slopes if n>=512]
print("last six slopes mean=%.4f"% (sum(last6)/len(last6)))

# OLS on log2 w vs log2 n over the large-n tail (n>=256, the task tail)
xs=[math.log2(n) for n,w in zip(nlist,wlist) if n>=256]
ys=[math.log2(w) for n,w in zip(nlist,wlist) if n>=256]
mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
a=my-b*mx
resid=[y-(a+b*x) for x,y in zip(xs,ys)]
sse=sum(r*r for r in resid)
se=math.sqrt(sse/(len(xs)-2)/sum((x-mx)**2 for x in xs))
print()
print(f"OLS log2 w = {a:.4f} + {b:.4f}*log2 n, se={se:.5f}, npts={len(xs)}")
print("is 1/2 in range? |b-0.5|/se =", abs(b-0.5)/se)

# w^2 / n test for w=c*sqrt(n): if w~c sqrt n then w^2/n ~ c^2 constant
print()
print("w^2/n (constant iff w ~ c*sqrt(n)):")
for n,w in zip(nlist,wlist):
    if n>=64:
        print(f"  n={n:6d}  w^2/n={w*w/n:.5f}")
