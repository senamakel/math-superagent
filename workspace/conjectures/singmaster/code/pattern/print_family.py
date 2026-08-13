import math
def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
def lucas(n):
    a,b=2,1
    if n==0: return a
    for _ in range(1,n):
        a,b=b,a+b
    return b
print("i, n_i, k_i, a_i(digits)")
for i in range(1,13):
    n=fib(2*i+2)*fib(2*i+3)-1
    k=fib(2*i)*fib(2*i+3)-1
    a=math.comb(n+1,k+1)
    print(i, n, k, len(str(a)), a if i<=4 else '')
