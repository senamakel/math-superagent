import math
# phase-1.0 points: powers of 2, n=256..65536 (all frac=1.000, same phase => removes periodic bias)
data = [(256,16),(512,24),(1024,35),(2048,52),(4096,77),(8192,112),(16384,164),(32768,239),(65536,349)]
xs=[math.log2(n) for n,w in data]
ys=[math.log2(w) for n,w in data]
mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
a=my-b*mx
resid=[y-(a+b*x) for x,y in zip(xs,ys)]
sse=sum(r*r for r in resid)
se=math.sqrt(sse/(len(xs)-2)/sum((x-mx)**2 for x in xs))
print(f"phase-1.0 (powers of 2) exponent: E = {b:.5f} +/- {se:.5f}  ({len(xs)} pts)")
print(f"  |E-0.5|/se = {abs(b-0.5)/se:.1f}   |E-0.585|/se = {abs(b-0.58496)/se:.1f}")
print("  per-doubling slopes at power-of-2 phase:", ["%.4f"%(ys[i+1]-ys[i]) for i in range(len(ys)-1)])

# phase ratio: w*(2n)/w*(n) at n=2^m
print()
print("phase-1.0 doubling ratios w*(2n)/w*(n):")
for i in range(len(data)-1):
    n1,w1=data[i]; n2,w2=data[i+1]
    print(f"  n {n1}->{n2}: ratio {w2/w1:.4f}  = 2^{math.log2(w2/w1):.4f}")
