"""Schema-aware exact audit of stored integer sequence artifacts.

Evidence target: determine whether stored sequences support a new structural
relation useful for PE1006. No full-size solver is attempted.
"""
from pathlib import Path
from fractions import Fraction
import sympy as sp

OUT = Path(__file__).resolve().parents[1] / "out"

# Deliberately restrict to compact sequence tables, not logs/reports or huge
# primary tables whose schema is already handled by dedicated programs.
NAMES = [
    "counts.txt", "c1_terms.txt", "lmin.txt", "psi_exact.txt",
    "psi_residues.txt", "ext_recurrence.txt", "extrecur_res.txt",
    "dj_raw.txt", "dj_mod.txt", "topelitz_defects.txt", "vr_rungaps.txt",
    "vr_runvals.txt", "vR_exact.txt", "vR_res.txt", "s1_exact.txt",
    "s1_res.txt", "r_runs_wythoff.txt", "vr_runvals.txt",
]

def integer_rows(name):
    rows=[]
    p=OUT/name
    if not p.exists(): return rows
    for line in p.read_text(errors="replace").splitlines():
        z=line.split()
        vals=[]
        for tok in z:
            try: vals.append(int(tok))
            except ValueError: pass
        if vals: rows.append(vals)
    return rows

def choose_schema(rows):
    """Return (indices, values, schema), preferring explicit 2-column tables."""
    if not rows: return [], [], "empty"
    if all(len(r)>=2 and r[0] == i+1 for i,r in enumerate(rows)):
        return [r[0] for r in rows], [r[1] for r in rows], "index,value"
    if all(len(r)>=2 and r[0] == i for i,r in enumerate(rows)):
        return [r[0] for r in rows], [r[1] for r in rows], "zero-index,value"
    if all(len(r)==1 for r in rows):
        return list(range(1,len(rows)+1)), [r[0] for r in rows], "value-only"
    return list(range(1,len(rows)+1)), [r[-1] for r in rows], "last-numeric-column (ambiguous)"

def first_bad_recurrence(a, coeffs):
    d=len(coeffs)
    for n in range(d,len(a)):
        if a[n] != sum(coeffs[j]*a[n-j-1] for j in range(d)):
            return n+1, a[n], sum(coeffs[j]*a[n-j-1] for j in range(d))
    return None

def rational_recurrence(a, max_order=12):
    """Find a recurrence only if exact rational coefficients fit every term."""
    for d in range(1,min(max_order,len(a)//2)+1):
        cs=sp.symbols(f'c0:{d}')
        equations=[sp.Eq(a[n],sum(cs[j]*a[n-j-1] for j in range(d)))
                   for n in range(d,len(a))]
        sol=sp.solve(equations,cs,dict=True)
        if len(sol)==1 and all(c in sol[0] for c in cs):
            coeff=[Fraction(sol[0][c]) for c in cs]
            return d, coeff
    return None

def fibs_until(n):
    f=[1,2]
    while f[-1] <= n: f.append(f[-1]+f[-2])
    return f

def main():
    data={}
    print("SCHEMA-AWARE INTEGER SEQUENCE AUDIT")
    for name in NAMES:
        rows=integer_rows(name)
        if not rows: continue
        idx,val,schema=choose_schema(rows)
        data[name]=(idx,val,schema)
        rec=rational_recurrence(val)
        print(f"{name}: rows={len(rows)} schema={schema} range={idx[0]}..{idx[-1]} "
              f"head={val[:5]} recurrence={rec}")

    # Deliberate structural tests on correctly parsed columns.
    if "counts.txt" in data:
        idx,a,_=data["counts.txt"]
        bad=next(((idx[i],a[i],idx[i]+1) for i in range(len(a)) if a[i]!=idx[i]+1),None)
        print("counts=k+1 first bad:",bad)
    if "c1_terms.txt" in data:
        idx,a,_=data["c1_terms.txt"]
        # exact integer comparison to floor(k(3-sqrt(5))/2), using SymPy algebraic exactness
        bad=None
        for k,v in zip(idx,a):
            expected=1+int(sp.floor(sp.Rational(k,2)*(3-sp.sqrt(5))))
            if v!=expected: bad=(k,v,expected); break
        print("c1 floor law first bad:",bad)
    if "lmin.txt" in data:
        idx,a,_=data["lmin.txt"]
        fib=fibs_until(max(idx))
        bad=None
        for k,v in zip(idx,a):
            nxt=next(x for x in fib if x>k)
            e=k+nxt-1
            if v!=e: bad=(k,v,e); break
        print("Lmin strict-next-Fibonacci law first bad:",bad)

    # Cross-sequence relations keyed by explicit index intersection.
    def aligned(left,right):
        if left not in data or right not in data: return []
        il,al,_=data[left]; ir,ar,_=data[right]
        L=dict(zip(il,al)); R=dict(zip(ir,ar))
        return [(k,L[k],R[k]) for k in sorted(set(L)&set(R))]
    for left,right,mod in [("psi_residues.txt","c1_terms.txt",100),
                           ("psi_residues.txt","c1_terms.txt",1000),
                           ("psi_residues.txt","c1_terms.txt",101001001)]:
        ar=aligned(left,right); bad=next(((k,x,y) for k,x,y in ar if (x-y)%mod),None)
        print(f"{left} == {right} mod {mod} first bad:",bad)

    # A structural relation candidate: sequence differences versus another
    # sequence, tested by exact affine fit from the first two common points and
    # then all remaining points. This is not a scalar recurrence.
    for left,right in [("c1_terms.txt","lmin.txt"),("dj_raw.txt","vr_rungaps.txt"),
                       ("s1_exact.txt","vR_exact.txt")]:
        ar=aligned(left,right)
        if len(ar)<3:
            continue
        # test y = A*x+B and y differences = A*x differences
        x0,y0=ar[0][1],ar[0][2]; x1,y1=ar[1][1],ar[1][2]
        if x1==x0: affine=None
        else: affine=Fraction(y1-y0,x1-x0)
        bad_aff=None if affine is None else next(
            ((k,x,y) for k,x,y in ar if Fraction(y-y0)-affine*(x-x0)!=0),None)
        diffs=[(ar[i][0],ar[i][2]-ar[i-1][2],ar[i][1]-ar[i-1][1]) for i in range(1,len(ar))]
        ratio=None
        if diffs and all(dx!=0 for _,dy,dx in diffs[:2]): ratio=Fraction(diffs[1][1],diffs[1][2])
        bad_diff=None if ratio is None else next(((k,dy,dx) for k,dy,dx in diffs if Fraction(dy)!=ratio*dx),None)
        print(f"cross {left} vs {right}: affine_slope={affine} first_affine_bad={bad_aff} "
              f"difference_ratio={ratio} first_difference_bad={bad_diff}")

    # Fibonacci-lag tests on every sequence with enough terms. This searches a
    # named family only; failure is reported at the first explicit index.
    for name,(idx,a,schema) in data.items():
        pos={k:i for i,k in enumerate(idx)}
        fib=fibs_until(max(idx))
        bad=None
        for f in fib:
            if f+1 in pos and f in pos and f-1 in pos:
                if a[pos[f+1]] != a[pos[f]]+a[pos[f-1]]:
                    bad=(f+1,a[pos[f+1]],a[pos[f]]+a[pos[f-1]]); break
        if bad is not None:
            print(f"{name} Fibonacci-index additive first bad:",bad)

if __name__ == "__main__": main()
