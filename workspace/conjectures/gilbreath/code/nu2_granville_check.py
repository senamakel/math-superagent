N=3000000
s=bytearray([1])*(N+1); s[0]=s[1]=0
for i in range(2,int(N**0.5)+1):
    if s[i]: s[i*i::i]=bytearray(len(s[i*i::i]))
P=[i for i in range(N+1) if s[i]]
M=4000                      # number of columns to examine
rows=[P[:M+2]]
for k in range(1,M+1):
    prev=rows[-1]
    rows.append([abs(prev[i+1]-prev[i]) for i in range(len(prev)-1)])
def diag(n):                # delta_k(q_n) = rows[k][n-k], k=0..n-1
    return [rows[k][n-k] for k in range(n)]
import math
print("n      nu2      n^0.525    n/2     nu2/n    last  ok")
bad=0
for n in [50,100,200,400,800,1600,3200,3999]:
    d=diag(n)
    last=d[-1]
    # 0-2 cycle: maximal suffix of d[2:-1] containing only 0 and 2
    tail=d[2:-1]; i=len(tail)
    while i>0 and tail[i-1] in (0,2): i-=1
    cyc=tail[i:]
    nu2=cyc.count(2)
    gstar=max(rows[1][1:n+1])
    ok = gstar <= 2*nu2+2
    if not ok: bad+=1
    print("%-6d %-8d %-10.1f %-8.1f %-8.3f %-5d %s  gstar=%d cyclen=%d"%(n,nu2,n**0.525,n/2,nu2/n,last,ok,gstar,len(cyc)))
print("lemma5.4 hypothesis g* <= 2*nu2+2 failed at:",bad,"of the sampled n")
