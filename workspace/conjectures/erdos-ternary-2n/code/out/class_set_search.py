"""Find what the stable survivor-exponent class set C_j = A_{j+1} mod 3^j actually is.
Candidate relations to test against C_j (all r even, mod 3^j):
  1. value at SAME precision: 2^r mod 3^(j+1) digit-free?     (already failed for j+1... retry precise)
  2. value at precision j:    2^r mod 3^j digit-free
  3. exponent-sinc 2^r mod 3^(j+1) has low digit 1 (always true for even r)
Check against the actual C_j."""
def ternary01(x):
    d=[]
    if x==0: return [0]
    while x: d.append(x%3); x//=3
    return all(v in (0,1) for v in d)
def digitfree2(x):
    d=[]
    if x==0: return [0]
    while x: d.append(x%3); x//=3
    return all(v!=2 for v in d)

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

K=20
sets=survivor_sets(K)

for j in range(1,7):
    mod=3**j
    C=sorted({r%mod for r in sets[j+1]})   # stable class set (proved = A_k mod 3^j for k>j)
    # candidate 2: value at precision j digit-{0,1}, r even
    cand={r for r in range(mod) if r%2==0 and ternary01(pow(2,r,3**j))}
    # candidate 3: value at precision j avoids nothing extra... same as 2
    print(f"j={j} mod{mod}: |C|={len(C)}; cand2(value prec j,size {len(cand)}) match={set(C)==cand}")
