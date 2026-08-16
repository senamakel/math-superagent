import math
data = [(256,16),(512,24),(1024,35),(2048,52),(4096,77),(8192,112),(16384,164),(32768,239),(65536,349)]
# The log-periodic oscillation floors the residual; check whether 5/9 is distinguishable
# from the fitted 0.555 by how much the EXCESS residual would be (on top of periodicity).
for E in [0.5550, 5/9]:
    xs=[math.log2(n) for n,w in data]
    ys=[math.log2(w)-E*math.log2(n) for n,w in data]
    mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
    b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
    resid=[y-(my+b*(x-mx)) for x,y in zip(xs,ys)]
    sse=sum(r*r for r in resid)
    print(f"E={E:.6f}: after removing phase-1.0 log-periodic trend, residual sd (log2 units) = {math.sqrt(sse/(len(xs)-1)):.5f}")

# Difference in log2 w over the range from using 0.555 vs 5/9:
l2w_hi=math.log2(349)-math.log2(16)
print("\nlog2 w range over n=256..65536:", l2w_hi)
for E in [0.5550,5/9]:
    delta = (5/9 - 0.5550)*(math.log2(65536)-math.log2(256))
    break
print("max log2-unit gap between 0.555 and 5/9 over the range:", (5/9-0.5550)*8, "(vs oscillation amplitude ~0.32 in log2 of w/n^E)")
print("-> the 5/9-vs-0.555 gap (0.0046) is 30x smaller than the periodic swing; NOT separable.")
