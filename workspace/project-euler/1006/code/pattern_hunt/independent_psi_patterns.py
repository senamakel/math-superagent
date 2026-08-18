"""Independent tests of simple recurrence/block hypotheses for stored Psi terms."""
from pathlib import Path

ROOT = Path(__file__).parents[1] / "out"

def read(path):
    out=[]
    for line in (ROOT/path).read_text().splitlines():
        if line.strip():
            a,b=line.split()[:2]; out.append((int(a),int(b)))
    return [v for _,v in out]

def first_fail(name, pred, vals):
    for i in range(1,len(vals)):
        if not pred(i, vals):
            return i+1, vals[i]
    return None

def main():
    exact=read(Path("psi_exact.txt")); res=read(Path("psi_residues.txt"))
    tests=[]
    # affine, Fibonacci, and fixed-coefficient order-1/2 recurrences
    tests.append(("exact affine first differences constant", lambda i,v: v[i]-v[i-1]==v[1]-v[0], exact))
    tests.append(("residue affine first differences constant", lambda i,v: (v[i]-v[i-1])%101001001==(v[1]-v[0])%101001001, res))
    tests.append(("exact Fibonacci Psi[n]=Psi[n-1]+Psi[n-2]", lambda i,v: v[i]==v[i-1]+v[i-2], exact))
    tests.append(("residue Fibonacci", lambda i,v: (v[i]-v[i-1]-v[i-2])%101001001==0, res))
    # block scaling candidates: Psi(k+1) == 100 Psi(k) modulo M, and exact
    tests.append(("exact decimal shift", lambda i,v: v[i]==100*v[i-1], exact))
    tests.append(("residue decimal shift", lambda i,v: (v[i]-100*v[i-1])%101001001==0, res))
    # Fibonacci-index block: first differences at F_j and F_{j+1} equal
    fib=[1,2]
    while fib[-1] <= len(res): fib.append(fib[-1]+fib[-2])
    for name, vals in [("exact",exact),("residue",res)]:
        good=True; fail=None
        for j in range(2,len(fib)):
            a,b=fib[j-2]-1,fib[j-1]-1
            if b>=len(vals) or a<1: continue
            if (vals[b]-vals[b-1]) != (vals[a]-vals[a-1]) if name=="exact" else ((vals[b]-vals[b-1]-vals[a]+vals[a-1])%101001001):
                good=False; fail=(fib[j-1], vals[b]) ; break
        print(name+" Fibonacci-boundary first-difference repeat", "PASS" if good else "FAIL at k=%s value=%s"%fail)
    for name,p,v in tests:
        f=first_fail(name,p,v)
        print(name, "PASS" if f is None else "FAIL at k=%d value=%d"%f)
    # exact order <= 6 recurrence over rationals using first terms, test remaining
    import sympy as sp
    for label, vals, mod in [("exact",exact,None),("residue",res,101001001)]:
        for d in range(1,7):
            cs=sp.symbols('c:'+str(d))
            eq=[sp.Eq(vals[n],sum(cs[j]*vals[n-j-1] for j in range(d))) for n in range(d,len(vals))]
            sol=sp.solve(eq[:max(d, len(eq)//2)],cs, dict=True)
            if sol:
                s=sol[0]; bad=None
                for n in range(d,len(vals)):
                    lhs=vals[n] if mod is None else vals[n]%mod
                    rhs=sum(s[cs[j]]*vals[n-j-1] for j in range(d))
                    if mod: rhs=int(rhs)%mod
                    if lhs!=rhs: bad=n+1; break
                print(label,"order",d,"PASS" if bad is None else "FAIL at k=%d"%bad)
                break
        else: print(label,"no order<=6 recurrence identified")
if __name__ == '__main__': main()
