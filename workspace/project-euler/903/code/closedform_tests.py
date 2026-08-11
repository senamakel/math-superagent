import math
from fractions import Fraction

A={2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,10:5514150297600,11:680309947699200}
B={3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,10:-85305830400,11:-9900701798400}
def fact(n): return math.factorial(n)

print("=== residual R_n = (n!)^2/2 - A_n ===")
R={}
for n in range(2,12):
    R[n]=fact(n)*fact(n)//2 - A[n]
    print(n, R[n])
print("\nR_n/(n-1)! :", {n: Fraction(R[n],fact(n-1)) for n in range(2,12)})
print("\nR_n / (n!) :", {n: Fraction(R[n],fact(n)) for n in range(2,12)})
print("\nH1: A_n = (n!)^2/2 - c*(n-1)!*n!  => c = R_n/((n-1)!*n!):")
for n in range(2,12):
    print("  n=",n, float(Fraction(R[n],fact(n-1)*fact(n))))
print("\nH2: A_n/(n!)^2 as 1/2 - c/n  , c=(0.5 - A/(n!)^2)*n:")
for n in range(2,12):
    r=Fraction(A[n],fact(n)**2)
    print("  n=",n," c=",round(float(Fraction(1,2)-r)*n,6))
print("\nH3 B: c=(B/(n!)^2)*(-n):")
for n in range(5,12):
    r=Fraction(B[n],fact(n)**2)
    print("  n=",n, round(float(-r)*n,6))

# test c_n=|B|/(n-1)! against (n-2)!/(n-3)! style and n^2
print("\nc_n=|B|/(n-1)! :", {n: Fraction(abs(B[n]),fact(n-1)) for n in range(6,12)})
# ratio to n^2
print("\nc_n / n^2:")
for n in range(6,12):
    cb=Fraction(abs(B[n]),fact(n-1))
    print("  n=",n, round(float(cb)/n**2,6))

# asymptotic check: A_n/(n!)^2 - 1/2 ; want c
print("\nA_n/(n!)^2 :", {n: round(float(Fraction(A[n],fact(n)**2)),6) for n in range(2,12)})
