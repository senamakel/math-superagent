import math

nlist  = [8,10,12,14,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
wlist  = [3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239]
E = 0.5568

print("== directive 46: log-periodicity test. w*(n)/n^E vs log2(n) ==")
print("  (a bounded period-1 oscillation in log2 n => exponent E with periodic correction)")
print(f"n        log2(n)  frac(n)   w/n^{E}      log2(w/n^E)   residual-from-fit")
print("-"*90)
# OLS fit log2 w = a + E log2 n on n>=256 (recompute to get residuals)
idx=[i for i,n in enumerate(nlist) if n>=256]
xs=[math.log2(n) for i,n in enumerate(nlist) if i in idx]
ys=[math.log2(w) for i,w in enumerate(wlist) if i in idx]
mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
a=my-b*mx
# OLS on ALL points n>=16 for comparison
xs2=[math.log2(n) for n,w in zip(nlist,wlist) if n>=16]
ys2=[math.log2(w) for n,w in zip(nlist,wlist) if n>=16]
mx2=sum(xs2)/len(xs2); my2=sum(ys2)/len(ys2)
b2=sum((x-mx2)*(y-my2) for x,y in zip(xs2,ys2))/sum((x-mx2)**2 for x in xs2)
a2=my2-b2*mx2

rows=[]
for n,w in zip(nlist,wlist):
    l2=math.log2(n)
    frac=n/math.pow(2,math.floor(l2))  # n / 2^floor(log2 n) in [1,2)
    val=w/n**E
    lv=math.log2(val)
    res=lv-(a+b*l2)
    rows.append((l2,frac,lv,res,n,w))
for l2,frac,lv,res,n,w in rows:
    print(f"{n:6d}  {l2:7.3f}  {frac:6.3f}   {w/n**E:9.5f}   {lv:+9.4f}    {res:+8.4f}")

print()
print("residual v fraction in-cell (frac = n/2^floor(log2 n)):")
print("  frac   residuals  (want period-1 in frac if log-periodic)")
for l2,frac,lv,res,n,w in rows:
    if n>=64:
        print(f"  {frac:.3f}   {res:+.4f}   (n={n})")

# amplitude of oscillation over last ~8 points
tail=[r for l2,frac,lv,r,n,w in rows if n>=256]
print()
print("tail residual range (n>=256): min=%.4f max=%.4f amplitude=%.4f (log2 units)"%(min(tail),max(tail),max(tail)-min(tail)))
