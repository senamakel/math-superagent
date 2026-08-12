from math import gcd
LIMIT=10**18
# Feasible (a,k): sigma(u)/u = (2k+1)2^{a-1}/(2^{a+1}-1) = N/D.
# D|u, u odd => u>=D_reduced, n=2^a u >= 2^a * D_reduced <= LIMIT.
pairs=[]
maxa={}
for a in range(1,35):
    D=2**(a+1)-1
    for k in range(1,7):
        N=(2*k+1)*2**(a-1)
        g=gcd(N,D)
        den=D//g
        if 2**a*den <= LIMIT:
            pairs.append((a,k))
            maxa[k]=a
print("feasible (a,k) pairs:", len(pairs))
print("max a overall:", max(a for a,k in pairs))
print("max a per k:", maxa)
