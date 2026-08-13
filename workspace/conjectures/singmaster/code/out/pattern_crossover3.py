import math
# exact asym constant: n_j = F_{2j+2}F_{2j+3}-1. Asymptotically F_m ~ phi^m/sqrt5.
# ln n_j ~ ln(F_{2j+2}F_{2j+3}) = ln phi^{4j+5}/5 = (4j+5)A - ln5
# ln k_j ~ (4j+3)A - ln5. (checked numerically earlier: k/n->1/phi^2)
phi=(1+math.sqrt(5))/2
A=math.log(phi)
for eps in [0.3,1/3,0.3334,0.35,0.4]:
    # crossover where lnk == cutpow: (4j)A ~ ((4j+5)A)^{2/3+eps}
    # solve numerically for j
    lo,hi=1,10**12
    f=lambda j: (4*j+5)*A - math.log(5)  # lnn
    g=lambda j: ((f(j))**(2/3+eps)) - ((4*j+3)*A - math.log(5))  # cutpow - lnk
    if g(2)<0:
        print("eps=%.4f already interior at j=2"%eps); continue
    for _ in range(200):
        mid=(lo+hi)/2
        if g(mid)>0: lo=mid
        else: hi=mid
    print("eps=%.4f: crossover J0 ~ %.4e"%(eps,(lo+hi)/2))
