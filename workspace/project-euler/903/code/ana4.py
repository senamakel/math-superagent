from fractions import Fraction as F
from math import factorial

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}

print("alpha_n = A/(n!(n-1)!), beta_n = |B|/(n!(n-1)!)")
for n in range(2,12):
    base=F(factorial(n))*F(factorial(n-1))
    al = F(A[n],base)
    be = F(abs(B[n]),base) if n>=3 else F(0)
    print(f"n={n}: alpha={al} float={float(al):.8f}   beta={be} float={float(be):.8f}")

print("\n== 2*alpha-n, 3*alpha-n, 4*alpha-3n? ==")
for n in range(2,12):
    base=F(factorial(n))*F(factorial(n-1))
    al = F(A[n],base)
    print(f"n={n}: 2a-n={float(F(2)*al-n):.6f}  3a-n={float(F(3)*al-n):.6f}  4a-3n={float(F(4)*al-3*n):.6f}")

print("\n== alpha*(n-2)! == (A/(n!(n-1)!))*(n-2)! = A/(n!(n-1)) ==")
for n in range(3,12):
    v=F(A[n], F(factorial(n))*(n-1))
    print(f"n={n}: alpha*(n-2)! = A/[n!(n-1)] = {v} float={float(v):.6f}")

print("\n== beta*(n-2)! == |B|/[n!(n-1)] ==")
for n in range(3,12):
    v=F(abs(B[n]), F(factorial(n))*(n-1))
    print(f"n={n}: |B|/[n!(n-1)] = {v} float={float(v):.6f}")
