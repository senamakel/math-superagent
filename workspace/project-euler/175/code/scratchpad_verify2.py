from fractions import Fraction

def f(n):
    if n == 0: return 1
    if n % 2 == 1:
        return f(n//2)
    else:
        k = n//2
        return f(k) + f(k-1)

# User's ratio r_n = f(n)/f(n-1). Claim:
#   r_{2m}   = r_m + 1        (trailing 0 bit)
#   r_{2m+1} = r_m/(r_m+1)    (trailing 1 bit)
# root r_1 = 1/1.
def r(n):
    return Fraction(f(n), f(n-1))

ok0 = True; ok1 = True
for m in range(1, 200):
    ok0 &= (r(2*m) == r(m) + 1)
    ok1 &= (r(2*m+1) == r(m)/(r(m)+1))
print("r_1 =", r(1))
print("r_{2m} = r_m + 1 holds for m=1..199:", ok0)
print("r_{2m+1} = r_m/(r_m+1) holds for m=1..199:", ok1)

# Check the PE175 n=241 example: r_241 = f(241)/f(240)
print("n=241 ratio:", r(241), "=", float(r(241)))
print("expected 13/17 =", Fraction(13,17), r(241)==Fraction(13,17))

# Check f(10)=5
print("f(10)=", f(10))
