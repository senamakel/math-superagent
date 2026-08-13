import math
def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
def digits(n, k):
    """Number of digits of C(n,k), via log-gamma (O(1); the giant binomial
    itself cannot be materialized for i>=7 — C(1e7,4e6) has millions of
    digits). Matches exact math.comb digit counts 4,29,205,1412 for i=1..4."""
    lnC = math.lgamma(n+1) - math.lgamma(k+1) - math.lgamma(n-k+1)
    return int(lnC / math.log(10)) + 1
print("i, n_i, k_i, u_i=5n+6, v_i=5k+9, a_i(digits)")
for i in range(1,9):
    n=fib(2*i+2)*fib(2*i+3)-1
    k=fib(2*i)*fib(2*i+3)-1
    print(i, n, k, 5*n+6, 5*k+9, digits(n+1,k+1))
