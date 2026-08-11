import json, math
from fractions import Fraction as F

# trusted A_n, B_n from extend_f.json (verified independent)
A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}
def fact(n): return math.factorial(n)

def ac(n):
    """A_n coefficient"""
    return A[n]
def bc(n):
    if n==2: return 0
    return B[n]

# sum_{k=1}^{n-1} f_n(k) = (n-1)*A_n + B_n*(n-1)(n-2)/2
print("n |  sum_k f_n(k)  |  sum_k f/(n!)^2  | =? pi-sum")
tot=0
for n in range(2,12):
    s = (n-1)*A[n] + bc(n)*(n-1)*(n-2)//2
    print(f"{n}  {s}   {F(s,fact(n)**2)}")
    tot+=0

print("\n=== theory check n=2..7: sum_k f_n(k) == sum_pi (n!/L0)*S0, L0=len(cycle of 0), S0=sum elems in it ===")
import itertools
for n in range(2,8):
    lhs = (n-1)*A[n] + B[n]*(n-1)*(n-2)//2
    rhs = 0
    for pi in itertools.permutations(range(n)):
        # cycle of 0
        seen=[False]*n; seen[0]=True
        cyc=[0]; c=pi[0]
        while c!=0:
            cyc.append(c); c=pi[c]
        L0=len(cyc); S0=sum(cyc)
        # value of pi^i(0) summed over i=0..n!-1 = (n!/L0)*S0
        rhs += fact(n)//L0 * S0
    assert rhs==lhs, (n,rhs,lhs)
    print(f"n={n}: sum_kf={lhs}  pisum={rhs}  MATCH")

print("\n=== sum_k f_n(k) recurrence/hints ===")
seqs=[]
for n in range(2,12):
    s=(n-1)*A[n]+B[n]*(n-1)*(n-2)//2
    seqs.append((n,s))
print(seqs)
