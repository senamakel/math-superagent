from fractions import Fraction as F
from math import factorial

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}

print("== A_n / A_{n-1} and deviation from (n-1)(n-2) ==")
for n in range(3,12):
    r = F(A[n],A[n-1])
    dev = r - (n-1)*(n-2)
    print(f"n={n}: A_n/A_{n-1} = {r}   dev from (n-1)(n-2) = {float(dev):.4f}")

print("\n== A_n / [(n-1)!(n-2)!] ==")
for n in range(3,12):
    v = F(A[n], factorial(n-1)*factorial(n-2))
    print(f"n={n}: {float(v):.6f}")

print("\n== A_n / [(n)!^2] and A_n/(n!(n-1)!) ==")
for n in range(2,12):
    a1 = F(A[n], factorial(n)**2)
    a2 = F(A[n], factorial(n)*factorial(n-1))
    print(f"n={n}: A/n!^2 = {float(a1):.6f}  A/(n!(n-1)!) = {float(a2):.6f}")

print("\n== |B_n| / (n-1)!  (want integer for n>=6) ==")
for n in range(3,12):
    v = F(abs(B[n]), factorial(n-1))
    print(f"n={n}: |B|/(n-1)! = {v}  float={float(v):.6f}")

print("\n== |B|/(n-1)!  divided by various ==")
for n in range(6,12):
    c = F(abs(B[n]), factorial(n-1))
    print(f"n={n}: c=|B|/(n-1)!={c}  c/(n-2)!={F(c,factorial(n-2))}  c/(n-1)={F(c,n-1)}  c/[n]={F(c,n)}")

print("\n== relations B vs A ==")
for n in range(5,12):
    print(f"n={n}: |B|/A = {float(F(abs(B[n]),A[n])):.6f}  A*?   B/A*(n-1)={float(F(abs(B[n])*(n-1),A[n])):.4f}  B_at_n1/A_n: check A_{n+1}")

print("\n== A_{n+1} vs |B_n|×(n+1)??, A_{n+1}/(n+1) vs |B_n| ==")
for n in range(4,11):
    ratio = F(A[n+1], abs(B[n])) if B[n]!=0 else None
    print(f"n={n}: A_{n+1}/|B_n| = {ratio} (float {float(ratio):.4f} if set)")
