import math
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
# Check J0(eps) via exact ints for several eps<1/3: largest j whose family reps are boundary
for eps in [0.10,0.20,0.25,0.30,0.32,0.3330]:
    Jmax=0; Jall=[]
    for j in range(1,401):
        n=fib(2*j+2)*fib(2*j+3)-1
        k=fib(2*j)*fib(2*j+3)-1
        nn,kk=n+1,k+1
        cut=math.exp((math.log(nn))**(2/3+eps))
        b = (kk+1) < cut   # skeleton form k+1<cut using rep n
        if b: Jmax=j; Jall.append(j)
    print("eps=%.4f: largest boundary j (exact, j<=400)=%d, count=%d"%(eps,Jmax,len(Jall)))
