from lib.rightdiag import incremental_diagonals, cycle_and_nu2
def popcount(j): return bin(j).count("1")
N=600
h=[popcount(j)&1 for j in range(N+2)]
q=[2,3]
for j in range(N+2):
    q.append(q[-1]+(2 if h[j] else 4))
y=incremental_diagonals(q)
vals=[]
for n in range(0, N+1):
    dd=next(y)
    _,nu2=cycle_and_nu2(dd)
    vals.append(nu2)
# print nu2 at powers of two and at n=2^k-1 and 2^k+1
for k in range(0,10):
    m=1<<k
    if m<=N:
        print("n=%5d nu2=%d  floorlog2+1=%d" % (m, vals[m], k+1))
print("---")
# where does nu2 jump?
import math
prev=None
for n in range(N+1):
    if vals[n]!=prev:
        print("n=%5d nu2=%d" % (n, vals[n]))
        prev=vals[n]
