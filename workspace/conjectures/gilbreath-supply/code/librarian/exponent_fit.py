#!/usr/bin/env python3
import math
pairs = [
    (8, 3), (10, 3), (12, 3), (14, 4), (16, 3), (32, 5), (64, 7),
    (128, 11), (256, 16), (512, 24), (1024, 35), (2048, 52), (4096, 77),
]
print("n, first_w, log2(w/n)")
for n, w in pairs:
    print(f"  {n:5d}  {w:3d}   {math.log2(w/n):+.4f}")
print("\nConsecutive-doubling slopes:")
slopes = []
for (n1, w1), (n2, w2) in zip(pairs, pairs[1:]):
    s = math.log2(w2 / w1) / math.log2(n2 / n1)
    slopes.append(s)
    print(f"  n {n1}->{n2}: {s:.4f}")
m = len(slopes)
mean = sum(slopes)/m
std = (sum((s-mean)**2 for s in slopes)/m)**0.5
print(f"  mean={mean:.4f}  std={std:.4f}")
print("\nLeast-squares fit log2(w) = beta*log2(n) + c")
for label, cut in [("n>=16",16),("n>=32",32),("n>=64",64),("n>=128",128)]:
    pts=[(n,w) for n,w in pairs if n>=cut]
    X=[math.log2(n) for n,_ in pts]; Y=[math.log2(w) for _,w in pts]
    m=len(pts); mx=sum(X)/m; my=sum(Y)/m
    Sxx=sum((x-mx)**2 for x in X); Sxy=sum((x-mx)*(y-my) for x,y in zip(X,Y))
    beta=Sxy/Sxx; c=my-beta*mx
    r=[y-(beta*x+c) for x,y in zip(X,Y)]
    sig2=sum(ri*ri for ri in r)/(m-2)
    err=math.sqrt(sig2/Sxx)
    print(f"  {label}: beta={beta:.4f} +/- {err:.4f}  (m={m})")
print("\ncandidates: 1/2=%.4f  log4(3)=%.4f"%(0.5, math.log(3)/math.log(4)))
