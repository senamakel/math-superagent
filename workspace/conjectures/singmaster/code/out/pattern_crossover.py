import math
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
phi=(1+math.sqrt(5))/2
A=math.log(phi)
epsilons=[0.2,0.3,1/3,0.34,0.4,0.5]
for eps in epsilons:
    # boundary iff ln(k_j) < (ln n_j)^{2/3+eps}
    # find min j (up to 2000) and last-checked status
    status=[]
    for j in [1,2,3,4,5,10,20,50,100,200,500,1000,2000]:
        if j>600:  # avoid giant ints for huge j; use asymptotics only
            continue
        n=fib(2*j+2)*fib(2*j+3)-1
        k=fib(2*j)*fib(2*j+3)-1
        lnk=math.log(k)
        cut=math.exp((math.log(n))**(2/3+eps))
        status.append((j, lnk<math.log(cut)))
    print("eps=%.4f (2/3+eps=%.4f) boundary flags j=..."%(eps,2/3+eps), [t for t in status])
