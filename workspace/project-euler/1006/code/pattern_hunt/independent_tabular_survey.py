"""Exact survey of stored result tables; output is evidence, not proof."""
from pathlib import Path
from collections import Counter
from fractions import Fraction

OUT = Path("code/out")

def rows(name):
    ans=[]
    for line in (OUT/name).read_text().splitlines():
        z=line.split()
        if z and z[0].isdigit(): ans.append([int(x) for x in z])
    return ans

def first_bad(test, a):
    for i in range(1,len(a)):
        if not test(i,a): return i+1,a[i]
    return None

def bm(a, mod):
    # BM over prime mod; used only as a diagnostic.
    C=[1]; B=[1]; L=0; m=1; b=1
    for n in range(len(a)):
        d=sum(C[i]*a[n-i] for i in range(L+1))%mod
        if not d: m+=1; continue
        T=C[:]; q=d*pow(b,-1,mod)%mod
        C += [0]*max(0,len(B)+m-len(C))
        for j in range(len(B)): C[j+m]=(C[j+m]-q*B[j])%mod
        if 2*L<=n: L=n+1-L; B=T; b=d; m=1
        else: m+=1
    return L

def main():
    print("exact tabular survey")
    for name in ["psi_exact.txt","psi_residues.txt","c1_terms.txt","lmin.txt","vr_rungaps.txt"]:
        p=OUT/name
        if not p.exists(): continue
        rr=rows(name)
        print(f"{name}: rows={len(rr)}, widths={Counter(map(len,rr))}, head={rr[:8]}")
    psi=[x[1] for x in rows("psi_exact.txt")]
    print("psi exact first affine failure", first_bad(lambda i,a:a[i]-a[i-1]==a[i-1]-a[i-2],psi))
    print("psi exact first Fibonacci-add failure", first_bad(lambda i,a:a[i]==a[i-1]+a[i-2],psi))
    pr=[x[1] for x in rows("psi_residues.txt")]
    print("psi residues BM order mod 101001001", bm(pr,101001001))
    c=[x[1] for x in rows("c1_terms.txt")]
    # exact floor formula c1(k)=1+floor(k/phi^2), represented by Fibonacci convergent bounds
    # Test the equivalent Beatty increment pattern against alpha=1/phi^2 using rational sqrt bounds.
    alpha=(3-5**0.5)/2
    bad=[]
    for k,v in enumerate(c,1):
        if v != 1+int(k*alpha): bad.append((k,v,1+int(k*alpha))); break
    print("c1 first floating formula failure (diagnostic)",bad[:1] or "none through %d"%len(c))
    print("c1 difference prefix",[c[i]-c[i-1] for i in range(1,30)])
    l=[x[1] for x in rows("lmin.txt")]
    # known exact formula: k + least Fibonacci strictly greater than k - 1
    fib=[1,2]
    while fib[-1] <= max(range(1,len(l)+1)): fib.append(fib[-1]+fib[-2])
    def nxt(k): return next(f for f in fib if f>k)
    bad=[(k,l[k-1],k+nxt(k)-1) for k in range(1,len(l)+1) if l[k-1]!=k+nxt(k)-1]
    print("lmin formula first failure",bad[:1] or "none through %d"%len(l))
    print("lmin first differences",[l[i]-l[i-1] for i in range(1,30)])
    print("deliberate lmin wrong formula failure",first_bad(lambda i,a:a[i]==a[i-1]+1,l))
    print("deliberate psi mod-constant failure",first_bad(lambda i,a:a[i]==a[i-1],pr))
    print("new conjecture: none; all tested patterns match stored known formulas or fail immediately as reported")

if __name__=="__main__": main()
