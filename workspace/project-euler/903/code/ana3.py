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
    be = F(abs(B[n]),base) if n>=3 else None
    print(f"n={n}: alpha={al} = {float(al):.8f}   beta={be} = {float(be):.8f}")

# Try: is alpha_n rational with small denominator relating to n?  Check alpha_n * n, alpha_n * (n choose...)
print("\n== look for exact pattern in alpha_n: test 2*alpha_n - n ==")
for n in range(2,12):
    base=F(factorial(n))*F(factorial(n-1))
    al = F(A[n],base)
    print(f"n={n}: 2*alpha-n = {F(2)*al-n} = {float(F(2)*al-n):.6f},",
          f" 3*alpha-n = {F(3)*al-n} = {float(F(3)*al-n):.6f}")

print("\n== beta_n * (n-2)! and alpha_n*(n-2)! ==")
for n in range(3,12):
    base=F(factorial(n))*F(factorial(n-1))
    al=F(A[n],base); be=F(abs(B[n]),base)
    print(f"n={n}: alpha*(n-2)!={F(al)*F(factorial(n-2))}, beta*(n-2)!={F(be)*F(factorial(n-2))}")

print("\n== try: A_n = n!(n-1)! * (u/n + v/n^2 + ...)?  compute A/(n!(n-2)!) ==")
for n in range(3,12):
    v=F(A[n], F(factorial(n))*F(factorial(n-2)))
    print(f"n={n}: A/(n!(n-2)!) = {v} float={float(v):.6f}")
