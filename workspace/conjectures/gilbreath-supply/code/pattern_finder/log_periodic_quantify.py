import math

# (n, w*) exact from the extended computation
data = [(256,16),(512,24),(768,32),(1024,35),(1536,47),(2048,52),(3072,70),(4096,77),
        (5120,95),(6144,102),(8192,112),(10240,138),(12288,149),(16384,164),
        (20480,202),(24576,218),(32768,239),(40960,296),(49152,319),(65536,349)]

E1 = 0.5568
print("== log-periodic decomposition: w/n^E1 by in-cell phase frac = n/2^floor(log2 n) ==")
bins = {}
for n, w in data:
    l2 = math.log2(n)
    frac = n / math.pow(2, math.floor(l2))
    val = w / n**E1
    bins.setdefault(round(frac,2), []).append((n, val))

print("phase       values of w/n^0.5568 at successive doublings      mean   halfrange")
for ph in sorted(bins):
    entries = bins[ph]
    vals = [v for _,v in entries]
    mean = sum(vals)/len(vals)
    half = (max(vals)-min(vals))/2
    print(f" {ph:.3f}   "+" ".join(f"{v:.4f}" for v in vals)+f"   {mean:.4f}  {half:.4f}")

# amplitude of periodic part = max phase-mean - min phase-mean
means = [sum(v for _,v in bins[ph])/len(bins[ph]) for ph in bins]
print()
print("phase means:", ["%.4f"%m for m in means])
print("amplitude of oscillation (max-mean - min-mean): %.4f"% (max(means)-min(means)))

# Now test: does w/n^E at FIXED phase stay flat (bounded) or trend (drift)?
# Compare largest-n vs smallest-n at same phase.
print()
print("== trend check at fixed phase (bounded<<drift)? ==")
for ph in sorted(bins):
    entries = sorted(bins[ph])
    first = entries[0]; last = entries[-1]
    print(f" phase {ph:.3f}: n {first[0]}→{last[0]}  w/n^E {first[1]:.4f}→{last[1]:.4f}"
          f"  drift={last[1]-first[1]:+.4f} over {len(entries)} doublings")

# Overall OLS exponent over ALL these points (not just powers of 2)
xs=[math.log2(n) for n,w in data]
ys=[math.log2(w) for n,w in data]
mx=sum(xs)/len(xs); my=sum(ys)/len(ys)
b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
a=my-b*mx
resid=[y-(a+b*x) for x,y in zip(xs,ys)]
sse=sum(r*r for r in resid)
se=math.sqrt(sse/(len(xs)-2)/sum((x-mx)**2 for x in xs))
print()
print(f"OLS log2 w = {a:.4f} + {b:.4f} log2 n over ALL extended points (n=256..65536, {len(xs)} pts), se={se:.5f}")
print(f"  |b-0.5|/se = {abs(b-0.5)/se:.1f}  |b-0.585|/se = {abs(b-0.58496)/se:.1f}")
