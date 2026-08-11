from fractions import Fraction as F
from math import factorial

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}

print("== A_{n+1} / |B_n| for n=4..10 (B_4=0 skip) ==")
B = {3:1,5:108,6:3600,7:208800,8:12418560,9:932601600,10:85305830400,11:9900701798400}
for n in range(5,11):
    r = F(A[n+1], B[n])
    print(f"n={n}: A_{n+1}/|B_n| = {r}  float={float(r):.4f}")

print("\n== |B_n|/(n-1)!  ratio to (n-2)(n-3)... look at normalized c_n = |B|/(n-1)! ==")
# c_n: 30,290,2464,23130,235080,2728368  for n=6..11
print("n=6..11 c: 30,290,2464,23130,235080,2728368")

# ratio c_n / c_{n-1}
print("\n== c_n / c_{n-1} ==")
c = {6:30,7:290,8:2464,9:23130,10:235080,11:2728368}
for n in range(7,12):
    print(f"n={n}: c_n/c_{n-1} = {float(F(c[n],c[n-1])):.6f}")

print("\n== c_n / (n-2)! ==")
for n in range(6,12):
    print(f"n={n}: c/(n-2)! = {F(c[n],factorial(n-2))} float={float(F(c[n],factorial(n-2))):.6f}")

print("\n== c_n / [n*(n-1)*(n-2)!]? or c / [3*(n-1)!]  try simple: c/(n-1)! vs n ==")
# c was /(n-1)! so c*(n-1)! = |B|.  Let's try |B| / [(n-1)! * n*(n-1)] = c/(n(n-1))
for n in range(6,12):
    print(f"n={n}: |B|/[(n-1)! * n(n-1)] = {F(B[n], factorial(n-1)*n*(n-1))} float={float(F(B[n],factorial(n-1)*n*(n-1))):.6f}")
