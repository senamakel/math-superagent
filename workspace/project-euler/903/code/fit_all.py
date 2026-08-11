import sympy as sp
from sympy import Rational, Matrix, linsolve

A = {2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,
     10:5514150297600,11:680309947699200}
B = {3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,
     10:-85305830400,11:-9900701798400}
def fact(n): return sp.factorial(n)
def H(n): return sum(Rational(1,k) for k in range(1,n+1))

def tryfit(name, vals, basis_builder, ns):
    """basis_builder(n)->list of rational expressions. Try linear combination fitting all ns exactly."""
    nlist=list(ns)
    rows=[]; tgt=[]
    for n in nlist:
        rows.append([sp.simplify(b) for b in basis_builder(n)])
        tgt.append(Rational(vals[n]))
    Am=Matrix(rows)
    try:
        sol=list(linsolve((Am, Matrix(tgt))))
    except Exception as e:
        print(f"{name}: general-pose -> {len(nlist)} eqs vs {len(basis_builder(nlist[0]))} unk; solve failed {e}")
        return
    if len(sol)==1:
        args=list(sol[0])
        print(f"{name}: EXACT linear combo: {[sp.simplify(a) for a in args]}")
        # report formula
        bb=basis_builder(nlist[0])
        expr=sum(sp.simplify(args[i])*bb[i] for i in range(len(bb)))
        print(f"     formula: v[n] = {sp.simplify(expr)}")
    elif len(sol)>1:
        print(f"{name}: {len(sol)} solutions (underdetermined)")
    else:
        print(f"{name}: no solution")

# ------- I_n/(n!)^2 -------
I={n: (A[n]*n*(n-1)//2 + B.get(n,0)*n*(n-1)*(n-2)//6) for n in range(2,12)}
Irat={n:Rational(I[n],fact(n)**2) for n in range(2,12)}

ns=range(3,12)
def basis_general(n):
    Hn=H(n)
    return [Rational(1), n, n**2, Hn, Hn*n, Hn/(n), Rational(1,n), Rational(1,n**2), Hn**2]
tryfit("I/(n!)^2", Irat, basis_general, ns)

# same for I_n/(n!(n-1)!)
I2={n:Rational(I[n], fact(n)*fact(n-1)) for n in range(2,12)}
tryfit("I/(n!(n-1)!)", I2, basis_general, ns)

# ------- c_n = |B|/(n-1)! (n=6..11) -------
c={n:Rational(abs(B[n]), fact(n-1)) for n in range(6,12)}
tryfit("c_(=|B|/(n-1)!)", c, basis_general, range(6,12))

# ------- A_n / (n-1)! -------
A2={n:Rational(A[n], fact(n-1)) for n in range(2,12)}
tryfit("A/(n-1)!", A2, basis_general, range(4,12))
