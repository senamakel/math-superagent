from math import ceil
A = 1504170715041707
M = 4503599627370517
coins = [(1, A)]
n1, c1 = 1, A
n2, c2 = 3, (3 * A) % M
coins.append((n2, c2))
while True:
    alpha = ceil(c1 / c2)
    n3 = alpha * n2 - n1
    c3 = (A * n3) % M
    coins.append((n3, c3))
    if c3 == 0:
        break
    n1, c1 = n2, c2
    n2, c2 = n3, c3
cs = [c for _, c in coins]
ns = [n for n, _ in coins]

alphas = [ceil(cs[i] / cs[i + 1]) for i in range(len(cs) - 1) if cs[i + 1] != 0]
print("alphas:", alphas)

def runs(v):
    out=[]; i=0
    while i < len(v)-1:
        d=v[i+1]-v[i]; j=i+1
        while j<len(v)-1 and v[j+1]-v[j]==d: j+=1
        out.append((i,j,d)); i=j
    return out

rn = runs(ns)
print("\nindex runs (boundary, dn, alphas):")
for (i,j,d) in rn:
    print(f"  {i}..{j}  dn={d}  alphas_in_run={alphas[i:j]}")

def cf(p,q):
    out=[]
    while q:
        a=p//q; out.append(a); p,q=q,p-a*q
    return out
print("\nCF of A/M:", cf(A,M))
print("CF of M/A:", cf(M,A))
