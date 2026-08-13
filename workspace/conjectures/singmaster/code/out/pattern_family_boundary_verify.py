import math
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
eps=0.5
print("eps=%.3f. Family reps and boundary status (exact ints), j=2..9:"%eps)
for j in range(2,10):
    n=fib(2*j+2)*fib(2*j+3)-1
    k=fib(2*j)*fib(2*j+3)-1
    # reps: (n+1,k+1) and (n,k+2)
    reps=[(n+1,k+1),(n,k+2)]
    left=[]
    for (nn,kk) in reps:
        in_left = kk<=nn/2
        cut=math.exp((math.log(nn))**(2/3+eps))
        in_b = (kk+1)<cut  # skeleton uses k+1<cut with the rep's n
        left.append(in_left and in_b)
    print("  j=%d n=%d k=%d  reps %s -> both left-half+boundary=%s"%(j,n,k,reps,all(left)))
print()
print("Exact closed-form crossover (asymptotic) J0(eps): largest boundary j for eps<1/3")
phi=(1+math.sqrt(5))/2
A=math.log(phi)
for eps in [0.10,0.20,0.25,0.30,0.32,0.3330]:
    if eps>=1/3: 
        print("  eps=%.4f: infinite (boundary for all j)"%eps); continue
    # boundary iff (4j+3)A-ln5 < ((4j+5)A-ln5)^(2/3+eps)
    f=lambda j: (4*j+5)*A-math.log(5)
    g=lambda j: f(j)**(2/3+eps) - ((4*j+3)*A-math.log(5))
    # find largest j with g>0
    if g(1)<0:
        print("  eps=%.4f: j=1 already interior"%eps); continue
    lo,hi=1,1  # g grows...
    hi=2
    while g(hi)>0: hi*=2
    for _ in range(60):
        mid=(lo+hi)/2
        if g(mid)>0: lo=mid
        else: hi=mid
    print("  eps=%.4f: largest boundary j ~ %.3e"%eps, (lo+hi)/2)
