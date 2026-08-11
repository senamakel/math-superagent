import itertools, math
from fractions import Fraction

# A_n/n! and |B_n|/(n-1)! etc
A={2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,
   10:5514150297600,11:680309947699200}
B={3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,
   10:-85305830400,11:-9900701798400}

def fact(n): return math.factorial(n)

print("A_n/n!  n=2..11:")
for n in range(2,12): print(" ",n,Rational:=Fraction(A[n],fact(n)))

print("|B_n|/(n-1)! n=3..11:")
for n in range(3,12):
    if B[n]==0: print(" ",n,0)
    else: print(" ",n,Fraction(abs(B[n]),fact(n-1)))

print("A_n/|B_n| n>=5:")
for n in range(5,12):
    print(" ",n,Rational(A[n],abs(B[n])))

print("(n-1)! * A_n/|B_n| :")
for n in range(5,12):
    print(" ",n,Fraction(A[n],abs(B[n]))*fact(n-1) if False else float(Fraction(A[n],abs(B[n]))*fact(n-1)))

# attempt: is A_n = (n-1)! * a_n with a_n integers for some n?
print("\nA_n/(n-2)! :")
for n in range(2,12): print(" ",n,Fraction(A[n],fact(n-2)))

# try to see if |B_n|/(n-1)! relates to Bell-like or Stirling
# Bell numbers B(0..): 1,1,2,5,15,52,203,877,4140,21147,115975
bell=[1,1,2,5,15,52,203,877,4140,21147,115975,678570,4213597]
c = [Fraction(abs(B[n]),fact(n-1)) for n in range(6,12)]
print("\nc_n=|B|/(n-1)! n=6..11:", c)
# compare c_n to bell[n-1]
for i,n in enumerate(range(6,12)):
    print("  n=",n,"  c =",c[i]," bell[n]=",bell[n]," ratio=",float(c[i]/bell[n]))

# compare A_n/n! to bell-like; compute A_n/(n!·bell?) 
print("\nA_n/n! ratios against n^2 etc:")
for n in range(8,12):
    r=Fraction(A[n],fact(n))
    print("  n=",n," A/n!=",r," /n^2=",float(r/n**2)," /n^3=",float(r/n**3))
