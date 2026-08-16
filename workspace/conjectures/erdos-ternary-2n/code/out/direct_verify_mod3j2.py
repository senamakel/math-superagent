"""Unambiguous direct-sieve check of |A_k mod 3^j| = 2^j for k>j only."""
def digit01_ternary(x):
    d=[]
    if x==0: return [0]
    while x: d.append(x%3); x//=3
    return all(v in (0,1) for v in d)

def direct_Ak(k):
    per=2*3**(k-1); mod=3**k
    return {r for r in range(per) if digit01_ternary(pow(2,r,mod))}

ok=True
for k in range(2,9):
    A=direct_Ak(k); assert len(A)==2**(k-1)
    for j in range(1,k):   # strict k>j only
        n=len({r%(3**j) for r in A})
        if n!=2**j:
            ok=False; print(f"FAIL k={k} j={j}: {n}!={2**j}")
print("direct sieve, strict k>j, k<=8: |A_k mod 3^j|==2^j all PASS:", ok)
