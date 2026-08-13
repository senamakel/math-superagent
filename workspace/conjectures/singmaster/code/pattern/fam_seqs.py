import math, sys
sys.set_int_max_str_digits(1000000)
def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a
print("i, n_i, k_i, u_i=5n+6, v_i=5k+9, a_i(digits)")
for i in range(1,9):
    n=fib(2*i+2)*fib(2*i+3)-1
    k=fib(2*i)*fib(2*i+3)-1
    a=math.comb(n+1,k+1)
    print(i, n, k, 5*n+6, 5*k+9, len(str(a)))
