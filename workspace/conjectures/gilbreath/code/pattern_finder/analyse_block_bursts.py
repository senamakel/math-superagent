#!/usr/bin/env python3
"""Check the burst structure of the block profile: CONTEXT says it grows by
roughly-doubling bursts at k~15,20,23,35,39. Quantify log2 of ratios between
local maxima. Also verify locally that no exact short multiplicative law holds.
"""
import json, math
with open("code/out/blocks_depth1000.json") as f:
    data=json.load(f)
b=data["b"][:161]  # genuine dynamics rows 1..161
# local maxima
mx=[]
for i in range(1,len(b)-1):
    if b[i]>b[i-1] and b[i]>=b[i+1]:
        mx.append((i+1,b[i]))
print("local maxima (k, b_k):", mx)
print("growth within: log2 ratios between successive maxima:")
for i in range(1,len(mx)):
    r=math.log2(mx[i][1]/mx[i-1][1])
    print(f"  k={mx[i-1][0]}->{mx[i][0]}: {mx[i-1][1]}->{mx[i][1]}  log2={r:.2f}")

# is b monotone nondecreasing at local min level? compute envelope at post-max
# Check whether block length is bounded below by k (CONTEXT: block grows across range,
# never falls to 0). Report min over windows.
print("min b over rows 1..161:", min(b), "at row", b.index(min(b))+1)
# how often is b close to (k-1) floor vs huge
floors=[i for i,v in enumerate(b) if v<=i+1]
print("rows where b<=k (near floor):", [i+1 for i in floors][:20] if floors else "none")
