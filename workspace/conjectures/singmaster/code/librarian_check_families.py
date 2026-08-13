import math

def C(n,k):
    if k<0 or k>n: return 0
    k=min(k,n-k)
    r=1
    for i in range(1,k+1):
        r=r*(n-k+i)//i
    return r

def fib(n):
    a,b=0,1
    for _ in range(n):
        a,b=b,a+b
    return a

# Infinite family: n=F_{2j+2}F_{2j+3}-1, m=F_{2j}F_{2j+3}-1 gives C(n+1,m+1)=C(n,m+2)
print("j | value | C(n+1,m+1)=C(n,m+2)?")
for j in range(1,6):
    n=fib(2*j+2)*fib(2*j+3)-1
    m=fib(2*j)*fib(2*j+3)-1
    v1=C(n+1,m+1); v2=C(n,m+2)
    print(j,n,m,v1,v2,v1==v2, v1)

# Also verify the six one-off collisions from MRSTT / witnesses
print("\none-off collisions independent recompute:")
pairs=[((16,2),(10,3)),((56,2),(22,3)),((120,2),(36,3)),
       ((21,2),(10,4)),((153,2),(19,5)),((221,2),(17,8)),
       ((78,2),(15,5)),((78,2),(14,6)),((15,5),(14,6))]
for (n,k),(m,l) in pairs:
    print(f"C({n},{k})={C(n,k):>6}  C({m},{l})={C(m,l):>6}  equal={C(n,k)==C(m,l)}")
