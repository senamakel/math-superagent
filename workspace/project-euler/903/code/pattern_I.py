import math
from fractions import Fraction as F

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}
def bc(n): return B.get(n,0)
def fact(n): return math.factorial(n)

print("n |  I_n = sum (n-k)f(k) (= sum_{(pi,i)} inv(pi^i))  |  I_n/(n!)^2")
for n in range(2,12):
    # sum_{k=1}^{n-1} (n-k)*f(k), f(k)=A+(k-1)B
    S2 = sum((n-k)*(k-1) for k in range(1,n))
    S1 = sum((n-k) for k in range(1,n))
    In = A[n]*S1 + bc(n)*S2
    print(f"{n}  {In}   {F(In,fact(n)**2)}")

# solve E1,E2 for A,B given M_n and I_n; but first: find closed form of I_n
In_seq = []
for n in range(2,12):
    S2 = sum((n-k)*(k-1) for k in range(1,n))
    S1 = sum((n-k) for k in range(1,n))
    In_seq.append(A[n]*S1 + bc(n)*S2)
print("\nI_n sequence (n=2..11):", In_seq)

# also record I_n/(n!)^2
print("\nI_n/(n!)^2:")
for i,n in enumerate(range(2,12)):
    print(n, F(In_seq[i], fact(n)**2))
