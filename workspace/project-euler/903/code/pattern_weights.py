import json, math
from fractions import Fraction as F

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}
def bc(n): return B.get(n,0)
def fact(n): return math.factorial(n)
def H(n): return sum(F(1,k) for k in range(1,n+1))

print("=== Sum_k f(k) vs (n!)^2(n-H_n)/2 ===")
for n in range(2,12):
    s=(n-1)*A[n]+bc(n)*(n-1)*(n-2)//2
    target=F(fact(n)**2)*(n-H(n))//2  # careful: not int
    tf = F(fact(n),1)**2 * (n-H(n)) / 2
    ok = (F(s)==tf)
    print(f"n={n}: sum={s}  target={tf}  {ok}")

print("\n=== weighted sums (look for clean closed form) ===")
for n in range(2,12):
    kf = A[n]*(n-1)*n//2 + bc(n)*(n-1)*n*(n-2)//3
    k2f = A[n]*sum(k for k in range(1,n))+bc(n)*sum(k*(k-1) for k in range(1,n))
    print(f"n={n}: sum_k k f(k)={kf}  sum_k k^2f={k2f}")

print("\n=== sum_k k f(k) normalized by (n!)^2 ===")
for n in range(2,11):
    kf = A[n]*(n-1)*n//2 + bc(n)*(n-1)*n*(n-2)//3
    print(f"n={n}: {F(kf,fact(n)**2)}")

print("\n=== sum_k k f(k) where k=position, as (something) ===")
# interpretation: sum_{(pi,i)} (sum of positions k with tau(k)<tau(0))
# try matching poly in n times n!
