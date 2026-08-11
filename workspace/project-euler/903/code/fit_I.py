import sympy as sp
from sympy import Rational, Matrix, linsolve

A = {2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,
     10:5514150297600,11:680309947699200}
B = {3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,
     10:-85305830400,11:-9900701798400}
def fact(n): return sp.factorial(n)
def H(n): return sum(Rational(1,k) for k in range(1,n+1))

I={n:(A[n]*n*(n-1)//2 + B.get(n,0)*n*(n-1)*(n-2)//6) for n in range(2,12)}
Irat={n:Rational(I[n],fact(n)**2) for n in range(2,12)}
print("I/(n!)^2:", [Irat[n] for n in range(3,12)])

def fit(name, vals, basisnames, builder, nlist):
    rows=[];tgt=[]
    for n in nlist:
        rows.append([sp.simplify(b) for b in builder(n)])
        tgt.append(Rational(vals[n]))
    Am=Matrix(rows)
    try:
        sol=list(linsolve((Am,Matrix(tgt))))
        if len(sol)==1:
            args=list(sol[0])
            print(f"{name}: SOL args={[sp.simplify(a) for a in args]}")
            bb=builder(nlist[0])
            expr=sum(sp.simplify(args[i])*bb[i] for i in range(len(bb)))
            print(f"   = {sp.simplify(expr)}")
        else:
            print(f"{name}: {len(sol)} sols")
    except Exception as e:
        print(f"{name}: {e}")

nlist=list(range(3,12))
# guess: I/(n!)^2 = a n^2 + b n + c + (d n + e) H_n + f H_n^2
def b1(n):
    Hn=H(n)
    return [n**2, n, Rational(1), Hn*n, Hn, Hn**2]
fit("I/(n!)^2 basis {n^2,n,1,nHn,Hn,Hn^2}", Irat, None, b1, nlist)

def b2(n):
    Hn=H(n)
    return [n**2, n, Rational(1), Hn*n, Hn, Rational(1,n)]  
    # {n^2,n,1,nHn,Hn,1/n}
fit("I/(n!)^2 basis {n^2,n,1,nHn,Hn,1/n}", Irat, None, b2, nlist)

def b3(n):
    Hn=H(n)
    return [n, Rational(1), Hn*n, Hn, Rational(1,n), Hn/n]
fit("I/(n!)^2 basis {n,1,nHn,Hn,1/n,Hn/n}", Irat, None, b3, nlist)

# try I_n/(n!(n-1)!) 
I2={n:Rational(I[n], fact(n)*fact(n-1)) for n in range(2,12)}
print("\nI/(n!(n-1)!):", [I2[n] for n in range(3,12)])
def b4(n):
    Hn=H(n)
    return [n, Rational(1), Hn*n, Hn, Rational(1,n), Hn**2]
fit("I/(n!(n-1)!) basis {n,1,nHn,Hn,1/n,Hn^2}", I2, None, b4, nlist)

def b5(n):
    Hn=H(n)
    return [n**2, n, Rational(1), Hn*n, Hn, Hn**2]
fit("I/(n!(n-1)!) basis {n^2,n,1,nHn,Hn,Hn^2}", I2, None, b5, nlist)
