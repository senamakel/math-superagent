import sympy as sp
from sympy import Rational, Matrix, linsolve, symbols

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}
def fact(n): return int(sp.factorial(n))
def bc(n): return B.get(n,0)
def In_n(n):
    bc_=bc(n)
    S1=sum((n-k) for k in range(1,n)); S2=sum((n-k)*(k-1) for k in range(1,n))
    return A[n]*S1 + bc_*S2
def Mn_n(n):
    bc_=bc(n)
    return (n-1)*A[n] + bc_*(n-1)*(n-2)//2
def H(n): return sum(Rational(1,k) for k in range(1,n+1))

I={n:In_n(n) for n in range(2,12)}
M={n:Mn_n(n) for n in range(2,12)}

# Try to solve A_n, B_n from E1 (verified closed form) + ansatz for B_n
print("Known: E1 -> sum_k f = (n!)^2 (n-H_n)/2")
for n in range(2,12):
    bc_=bc(n)
    lhs=(n-1)*A[n]+bc_*(n-1)*(n-2)//2
    rhs=fact(n)**2*(n-H(n))/2
    assert lhs==rhs, n
print("E1 confirmed for all trusted n=2..11\n")

# M_n = (n-1)A + B(n-1)(n-2)/2 = sum_k f. Solve for A in terms of B:
# (n-1)A = M_n - B*(n-1)(n-2)/2
print("A_n in terms of B_n and M_n:")
for n in range(2,12):
    bc_=bc(n)
    Aexpr = (M[n]-bc_*(n-1)*(n-2)//2)//(n-1)
    print(f"  n={n}: A={Aexpr}  (check {Aexpr==A[n]})")

# Now: I_n gives second equation. c_n = |B|/(n-1)!  (integer n>=6): 30,290,2464,23130,235080,2728368
# c_n / ? try ratios
c={6:30,7:290,8:2464,9:23130,10:235080,11:2728368}
print("\nc_n ratios c_n/c_{n-1}:")
for n in range(7,12):
    print(f"  {n}: {Rational(c[n],c[n-1])}")

# Try c_n / (something). c_n = |B|/(n-1)!.
# A_n/(n-1)!  : 1,5,30,210,1593,13682,129092,1340586,15195520,187475184
print("\nA_n/(n-1)!:")
for n in range(2,12):
    print(n, Rational(A[n], fact(n-1)))

print("\nI_n/(fact(n)*fact(n-1)):")
for n in range(2,12):
    print(n, Rational(I[n], fact(n)*fact(n-1)))
