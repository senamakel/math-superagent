"""Two clean corollaries of the survival-depth membership restatement,
verified independently of the survivor-lifting machinery (which used mod-3^k
arithmetic) by a direct big-int route.

Corollary A (3-adic determination): g(m)>=k depends only on m mod 3^(k-1).
Corollary B (nested tree): the set B_k (halved survivor residues mod 3^(k-1))
lifts to B_{k+1} (mod 3^k) as the digit-{0,1} heirs, |B_k|=2^(k-1).

We verify A directly by brute membership from A_k (mod-3^k lifting) vs the
direct big-int survival scan, then record B's cardinalities.
"""
from erdos.oracle import digit_free

def f_of_n(n):
    if n in (0,2,8): return None
    m=2**n; i=0
    while m>0:
        if m%3==2: return i
        m//=3; i+=1
    return None

def survivor_set(k):
    A={0}; cur=1
    while cur<k:
        L=2*3**(cur-1); nm=3**(cur+1); g=pow(2,L,nm); p3k=3**cur
        An=set()
        for r in A:
            base=pow(2,r,nm); gp=1
            for j in range(3):
                v=(base*gp)%nm; d=(v//p3k)%3
                if d in (0,1): An.add(r+j*L)
                gp=gp*g%nm
        A=An; cur+=1
    return A

def main():
    print("=== Corollary A: g(m)>=k depends only on m mod 3^(k-1) ===")
    # for each k, pick two values m1,m2 same mod 3^(k-1) but far apart, check same profile
    # simpler: verify g(m)>=k  <=>  (m mod 3^(k-1)) in B_k  for a fresh range m in
    # [period, 2*period) not used before (period=3^(k-1))
    total=0
    for k in range(2,11):
        per=3**(k-1)
        A=survivor_set(k); B={ (r//2)%per for r in A }
        # fresh second window [per,2per+marge]
        bad=0
        for m in range(per, per+min(per,600)):
            f=f_of_n(2*m)
            surv=(2*m in (0,2,8)) or (f is not None and f>=k)
            mem=(m%per) in B
            if surv!=mem: bad+=1
        total+=bad
        print(f"k={k} second-window mismatches={bad}")
    print("TOTAL second-window mismatches:", total)
    print()
    print("=== Corollary B: |B_k| = 2^(k-1), B_k = halved A_k ===")
    for k in range(2,12):
        per=3**(k-1); A=survivor_set(k)
        B={ (r//2)%per for r in A }
        print(f"k={k}: |A_k|={len(A)} |B_k|={len(B)} (expect 2^{k-1}={2**(k-1)})")

if __name__=="__main__":
    main()
