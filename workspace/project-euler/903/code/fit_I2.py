import sympy as sp
from sympy import Rational, Matrix, linsolve, factorial

A = {2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,
     10:5514150297600,11:680309947699200}
B = {3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,
     10:-85305830400,11:-9900701798400}
def fact(n): return sp.factorial(n)
def H(n): return sum(Rational(1,k) for k in range(1,n+1))

I={n:(A[n]*n*(n-1)//2 + B.get(n,0)*n*(n-1)*(n-2)//6) for n in range(2,12)}
Irat={n:Rational(I[n],fact(n)**2) for n in range(2,12)}
M={n:Rational(fact(n)**2*(n-H(n)), 2) for n in range(2,12)}

# M_n/(n!)^2 = (n-H_n)/2  [proven]. Look at deficit D_n = I/(n!)^2 - (n-H_n)/2 correlation.
print("n | I/(n!)^2 | M/(n!)^2=(n-H)/2 | deficit D | D/(n-1) | D/n")
for n in range(3,12):
    rr=Irat[n]; mm=Rational(n-H(n),2); D=rr-mm
    print(f"{n}  {rr}  {mm}  {D}  {D/(n-1)}  {D/n}")

# Try D_n = a*(n-H_n)+b or polynomial*H
print("\n=== fit deficit D_n ===")
def fit(name, vals, builder, nlist):
    rows=[];tgt=[]
    for n in nlist:
        rows.append([sp.simplify(b) for b in builder(n)])
        tgt.append(Rational(vals[n]))
    Am=Matrix(rows)
    try:
        sol=list(linsolve((Am,Matrix(tgt))))
        if len(sol)==1:
            args=list(sol[0])
            bb=builder(nlist[0])
            print(f"{name}: {[sp.simplify(a) for a in args]}  ={sp.simplify(sum(sp.simplify(args[i])*bb[i] for i in range(len(bb))))}")
        else: print(f"{name}: {len(sol)} sols")
    except Exception as e: print(f"{name}: {e}")

D={n: Irat[n]-Rational(n-H(n),2) for n in range(3,12)}
nl=list(range(3,12))
def bD(n):
    Hn=H(n)
    return [n, Rational(1), (n-H(n)), Rational(1,n), Hn]
fit("D ~ {n,1,n-H,1/n,H}", D, bD, nl)

def bD2(n):
    Hn=H(n)
    return [(n-H(n)), Rational(1,n), Rational(1,n**2), Hn/n]
fit("D ~ {(n-H),1/n,1/n^2,H/n}", D, bD2, nl)

# Maybe I_n has the form (n!)^2*[a n^2 + b n + c + (d n+e)H_n + f/n]
print("\n=== fit I_n directly (not normalized) with poly*H basis ===")
# I_n/(n!)^2 as rational in n,H
def bI(n):
    Hn=H(n)
    return [n*n, n, Rational(1), n*Hn, Hn, Hn/n, Rational(1,n), Rational(1,n*n)]
fit("I/(n!)^2 ~ {n^2,n,1,nH,H,H/n,1/n,1/n^2}", Irat, bI, nl)
