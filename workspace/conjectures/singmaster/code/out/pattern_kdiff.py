import math
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a
N=12
ns,ks=[],[]
for i in range(1,N+1):
    ns.append(fib(2*i+2)*fib(2*i+3)-1)
    ks.append(fib(2*i)*fib(2*i+3)-1)
print("n diffs:", [ns[i]-ns[i-1] for i in range(1,N)])
print("k diffs:", [ks[i]-ks[i-1] for i in range(1,N)])
# check k diff == F(4i+5)?
for i in range(1,N):
    d=ks[i]-ks[i-1]
    print("kdiff i=%d =%d  F(4i+5)=%d match=%s"%(i,d,fib(4*i+5),d==fib(4*i+5)))
# n_i closed form F(2i)F(2i+1)-1? fact2 said False. Check what n_i equals.
print("n_i:", ns)
# try n_i = F(2i+1)^2-1? or product of consecutive
for i in range(1,6):
    print(i, ns[i-1], fib(2*i+1)**2-1, fib(2*i+2)*fib(2*i+2)-1)
