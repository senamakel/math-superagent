"""Confirm the PROOF of |A_k mod 3^j| = 2^j (k>j):
(1) nesting: A_k mod 2*3^(k-2) == A_{k-1} (set equality) -- verified
(2) all survivors even
(3) A_{j+1} mod 3^j injective (even survivors: two can't differ by 3^j, which is odd)
(4) hence |A_{j+1} mod 3^j| = |A_{j+1}| = 2^j, stable for k>j.
Also produce the sequence of stabilised class counts mod 3^j for the tools."""
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

K=26
sets=survivor_sets(K)

print("=== (1) nesting A_k mod 2*3^(k-2) == A_{k-1}, set equality ===")
nest_ok=True
for k in range(2,K+1):
    pp=2*3**(k-2)
    got={r%pp for r in sets[k]}
    if got!=sets[k-1]:
        nest_ok=False; print("  NEST FAIL k=",k)
print("nesting holds k=2..%d:"%K, nest_ok)

print("=== (2) all survivors even ===")
print(all(r%2==0 for k in range(1,K+1) for r in sets[k]))

print("=== (3)+(4) |A_{j+1} mod 3^j| = 2^j, and stability for all k in (j,26] ===")
ok=True
seq=[]
for j in range(1,13):
    proj={r%(3**j) for r in sets[j+1]}
    if len(proj)!=2**j or len(proj)!=len(sets[j+1]):
        ok=False; print("  INJECT FAIL j=",j)
    seq.append(len(proj))
    # stability
    for k in range(j+2,K+1):
        if {r%(3**j) for r in sets[k]}!=proj:
            ok=False; print("  STABILITY FAIL j,k=",j,k)
print("count identity + stability hold:", ok)
print("class-count seq mod 3^j, j=1..12:", seq)
