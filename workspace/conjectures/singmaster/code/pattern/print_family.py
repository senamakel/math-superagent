import math
def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
def digits(n, k):
    """Number of digits of C(n,k), via log-gamma: materializing the binomial
    is only feasible for i<=4 (<=1412 digits); for i>=5 it is millions-to-
    billions of digits. Matches exact math.comb counts 4,29,205,1412."""
    lnC = math.lgamma(n+1) - math.lgamma(k+1) - math.lgamma(n-k+1)
    return int(lnC / math.log(10)) + 1
print("i, n_i, k_i, a_i(digits)")
for i in range(1,13):
    n=fib(2*i+2)*fib(2*i+3)-1
    k=fib(2*i)*fib(2*i+3)-1
    d=digits(n+1,k+1)
    if i<=4:
        a=math.comb(n+1,k+1)
        print(i, n, k, d, a)
    else:
        print(i, n, k, d)
