import gmpy2, sys
from math import comb
sys.set_int_max_str_digits(0)
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
def ndigits(a):
    return len(gmpy2.digits(a,10))
for j in range(1,9):
    n = fib(2*j+2)*fib(2*j+3) - 1
    k = fib(2*j)*fib(2*j+3) - 1
    a = comb(n+1, k+1)
    s = 1 + 8*a
    r = gmpy2.isqrt(s)
    is_sq = (r*r == s)
    x = (r+1)//2 if is_sq else None
    print("j=%d a_j digits=%d  col-2 rep exists=%s %s" % (
        j, ndigits(a), is_sq, ("x=%d" % x) if x else ""))
print("DONE")