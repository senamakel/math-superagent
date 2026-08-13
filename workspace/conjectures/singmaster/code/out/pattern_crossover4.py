import math
phi=(1+math.sqrt(5))/2
A=math.log(phi)
for eps in [0.10,0.20,0.25,0.30,0.32,0.3330]:
    if eps>=1/3-1e-9:
        print("  eps=%.4f: infinite (boundary for all j)"%eps); continue
    f=lambda j: (4*j+5)*A-math.log(5)
    g=lambda j: f(j)**(2/3+eps) - ((4*j+3)*A-math.log(5))
    if g(2)<0:
        print("  eps=%.4f: j=2 already interior"%eps); continue
    lo,hi=2,2
    while g(hi)>0: hi*=2
    for _ in range(60):
        mid=(lo+hi)/2
        if g(mid)>0: lo=mid
        else: hi=mid
    print("  eps=%.4f: largest boundary j ~ %.3e"%(eps,(lo+hi)/2))
