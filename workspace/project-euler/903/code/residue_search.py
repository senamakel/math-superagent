import math
from fractions import Fraction
A={2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,10:5514150297600,11:680309947699200}
B={3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,10:-85305830400,11:-9900701798400}
def fact(n): return math.factorial(n)

R={n: fact(n)*fact(n)//2 - A[n] for n in range(2,12)}
print("R_n (n!)^2/2 - A_n:", [R[n] for n in range(2,12)])

# candidate: A_n = (n!)^2/2 - (n!)(n-1)!/2 * r_n ; r_n = 2R_n/((n!)(n-1)!)
print("\nr_n = 2R_n/(n!(n-1)!) :")
for n in range(2,12):
    print("  n=",n, Fraction(2*R[n], fact(n)*fact(n-1)))

# candidate involving H_n
print("\nR_n / (n!(n-1)! H_n):")
H=0
from fractions import Fraction as F
for n in range(2,12):
    H += F(1,n)
    print("  n=",n, float(F(R[n],fact(n)*fact(n-1))*F(1,1))/(float(H)) if False else round(float(F(2*R[n],fact(n)*fact(n-1))/H),5))

# B: test |B_n| ~ 2/3*(n!)*(n-2)! ? compute (n!/?) 
print("\n|B_n|/(n!)(n-1)! * n : (should be ~ const if B ~ -c (n!)^2/n)")
for n in range(5,12):
    print("  n=",n, round(float(abs(B[n])*n/(fact(n)*fact(n-1))),5))

print("\n|B_n|/( (n-1)! (n-2)! ) :")
for n in range(5,12):
    print("  n=",n, round(float(abs(B[n])/(fact(n-1)*fact(n-2))),5))

print("\nc_n=|B|/(n-1)! and c_n - (n-1)*c_{n-1} style discrete differences:")
c={n: abs(B[n])//fact(n-1) for n in range(6,12)}
for n in range(7,12):
    print("  n=",n," c_n=",c[n]," c_n/c_{n-1}=",round(c[n]/c[n-1],5))
