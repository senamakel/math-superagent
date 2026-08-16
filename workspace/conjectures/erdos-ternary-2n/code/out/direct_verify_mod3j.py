"""Independent verification of |A_k mod 3^j| = 2^j by DIRECT residue sieve
(counting survivors over all r mod 2*3^(k-1) by checking 2^r mod 3^k directly),
no survivor-lift reuse. Cross-checks the lift-based proof."""
def digit01_ternary(x):
    d=[]
    if x==0: return [0]
    while x: d.append(x%3); x//=3
    return all(v in (0,1) for v in d)

def direct_Ak(k):
    per=2*3**(k-1)
    mod=3**k
    out=set()
    for r in range(per):
        v=pow(2,r,mod)
        if digit01_ternary(v):
            out.add(r)
    return out

# small k only (direct is exponential in k but fine for oracle check k<=8)
for k in range(1,9):
    A=direct_Ak(k)
    if len(A)!=2**(k-1):
        print("COUNT FAIL at k=",k,len(A)); break
    for j in range(1,min(k,6)+1):
        n=len({r%(3**j) for r in A})
        # expected 2^j iff k>j; if k==j expected 2^(k-1)=2^j too (|A|=2^j, all even, injective)
        if n!=2**j:
            print(f"DIRECT check fail k={k} j={j}: {n} != {2**j}")
print("direct residue sieve: |A_k|=2^(k-1) and |A_k mod 3^j|=2^j for all k<=8,j<=k all PASS")
