"""Check that the stable mod-3^j survivor class sets are exactly the exponent
residues r (even) with 2^r mod 3^(j+1) digit-{0,1}-free, and confirm the
2^j count is pure injectivity (survivors all even, so mod-3^j projection of a
mod 2*3^j survivor set cannot collapse two even residues)."""
def ternary01(x):
    d=[]
    if x==0: return [0]
    while x:
        d.append(x%3); x//=3
    return all(v in (0,1) for v in d)

def survivor_sets(K):
    sets={1:{0}}; A={0}; cur=1
    while cur<K:
        L=2*3**(cur-1); nm=3**(cur+1); g=pow(2,L,nm); p3k=3**cur
        An=set()
        for r in A:
            base=pow(2,r,nm); gp=1
            for j in range(3):
                d=(base*gp % nm)//p3k %3
                if d in (0,1): An.add(r+j*L)
                gp=gp*g%nm
        A=An; cur+=1; sets[cur]=A
    return sets

K=24
sets=survivor_sets(K)

# (A) stable class sets mod 3^j == exponent-domain full-precision survivor condition
allmatch=True
for j in range(1,9):
    mod=3**j
    cls=sorted({r%mod for r in sets[K]})
    pred=sorted(r for r in range(mod) if r%2==0 and ternary01(pow(2,r,3**(j+1))))
    ok=(cls==pred)
    if not ok: allmatch=False; print("MISMATCH j=",j)
    print(f"j={j}: classes=={cls}, pred-match={ok} (size {len(cls)})")
print("ALL classes == exponent-domain preimage:", allmatch)

# (B) injectivity check: |A_{j+1} mod 3^j| == |A_{j+1}| == 2^j  (all even, no collapse)
print("--- injectivity of mod-3^j projection of A_{j+1} ---")
for j in range(1,13):
    A=sets[j+1]
    proj={r%(3**j) for r in A}
    print(f"j={j}: |A_{j+1}|={len(A)}, |A_{j+1} mod 3^j|={len(proj)}, 2^j={2**j}, injective={len(A)==len(proj)}")
