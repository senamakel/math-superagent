def hits(n):
    # H_j = { d in [2,n-1] : j in M_d },  M_d = { n-1-d+o : o subset-of d }
    H=[0]*n
    for d in range(2,n):
        base=n-1-d
        o=d
        while True:                       # iterate submasks of d
            j=base+o
            if 0<=j<n: H[j]+=1
            if o==0: break
            o=(o-1)&d
    return H
for n in (16,32,64,128,256):
    H=hits(n)
    frac=sum(1 for x in H if x>=0.4*n)/n
    print(f"n={n:4d}  max|H_j|={max(H):5d}  median={sorted(H)[n//2]:5d}  "
          f"frac(|H_j|>=0.4n)={frac:.3f}  |H_{{n-2}}|={H[n-2]}  (odd-d count={ (n-2)//2 + ((n-2)%2) if False else sum(1 for d in range(2,n) if d%2==1)})")
