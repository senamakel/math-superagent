import math
data = [(256,16),(512,24),(1024,35),(2048,52),(4096,77),(8192,112),(16384,164),(32768,239),(65536,349)]
print("Phase-1.0 residual spread at candidate exponents (bounded periodic => best fit):")
for E in [0.555, 5/9, 0.5568, 0.5, math.log(3)/math.log(2)-1, 0.56, 0.557]:
    vals=[w/n**E for n,w in data]
    mn,mx=min(vals),max(vals)
    # also linear-trend residual: fit residual against log2 n, get slope
    xs=[math.log2(n) for n,w in data]
    ys=[math.log2(w)-E*math.log2(n) for n,w in data]
    mx_=sum(xs)/len(xs); my_=sum(ys)/len(ys)
    b=sum((x-mx_)*(y-my_) for x,y in zip(xs,ys))/sum((x-mx_)**2 for x in xs)
    print(f"  E={E:.5f}: spread={mx-mn:.4f}  drift-slope={b:+.5f}  (want small spread AND slope~0)")
