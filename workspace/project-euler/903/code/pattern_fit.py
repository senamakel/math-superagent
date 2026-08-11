import sympy as sp
from sympy import Rational, factorial, symbols, linsolve, Matrix

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}
def fact(n): return int(sp.factorial(n))

def In_n(n):
    bc = B.get(n,0)
    S1 = sum((n-k) for k in range(1,n))
    S2 = sum((n-k)*(k-1) for k in range(1,n))
    return A[n]*S1 + bc*S2

def Mn_n(n):
    bc = B.get(n,0)
    return (n-1)*A[n] + bc*(n-1)*(n-2)//2

# I_n values
I = {n: In_n(n) for n in range(2,12)}
M = {n: Mn_n(n) for n in range(2,12)}

def H(n): return sum(Rational(1,k) for k in range(1,n+1))

def fit_ansatz(vals, name, basis):
    """basis: list of symbols (n,Hn) -> list of functions of (n,Hn).
    Solve v[n] = sum c_i * basis_i for all n in vals; if consistent (dim0) and
    one solution, report it."""
    # find rank
    rows = []
    for n in vals:
        Hn = H(n)
        rows.append([Rational(fn(n,Hn)) for fn in basis])
    target = [Rational(vals[n]) for n in vals]
    # build augmented system
    A_mat = Matrix(rows)
    from sympy import ones
    # solve A c = target over Q, with all rows
    cvec = A_mat.solve(target) if A_mat.shape[0]==A_mat.shape[1] else None
    # use least-squares-free: try linsolve
    sol = sp.linsolve((A_mat, Matrix(target)))
    return sol

# Let's guess I_n/(n!)^2 form. Try basis in n, Hn
print("=== FIT I_n/(n!)^2 ===")
n_vals = list(range(3,12))
Irat = {n: Rational(I[n], fact(n)**2) for n in n_vals}
basis = []
ns = sp.symbols('ns'); Hn=sp.symbols('Hn')
cands = [
    ("{1,n,1/n,Hn,Hn/n,nHn}", lambda n,Hn: Rational(1), lambda n,Hn:n, lambda n,Hn:Rational(1,n), lambda n,Hn:Hn, lambda n,Hn:Hn/n, lambda n,Hn:n*Hn),
    ("{n^2,n,Hn,nHn,Hn^2,1}", lambda n,Hn:n*n, lambda n,Hn:n, lambda n,Hn:Hn, lambda n,Hn:n*Hn, lambda n,Hn:Hn**2, lambda n,Hn:Rational(1)),
    ("{n^2,n,1,nHn,Hn}", lambda n,Hn:n*n, lambda n,Hn:n, lambda n,Hn:Rational(1), lambda n,Hn:n*Hn, lambda n,Hn:Hn),
    ("{n^2,n,1,nHn,Hn,Hn^2}", lambda n,Hn:n*n, lambda n,Hn:n, lambda n,Hn:Rational(1), lambda n,Hn:n*Hn, lambda n,Hn:Hn, lambda n,Hn:Hn**2),
    ("{n^2, n, nHn, Hn^2, 1}", lambda n,Hn:n*n, lambda n,Hn:n, lambda n,Hn:n*Hn, lambda n,Hn:Hn**2, lambda n,Hn:Rational(1)),
]
for name, *fns in cands:
    rows = []
    tgt = []
    for n in n_vals:
        Hn=H(n)
        rows.append([Rational(fn(n,Hn)) for fn in fns])
        tgt.append(Irat[n])
    Am=Matrix(rows)
    try:
        sol = sp.linsolve((Am, Matrix(tgt)))
        if len(sol)==1:
            args = list(sol)[0]
            print(f"{name}: SOL {args}")
        else:
            print(f"{name}: {len(sol)} solutions")
    except Exception as e:
        print(f"{name}: {e}")

print("\n=== I_n values ===")
for n in range(2,12):
    print(n, I[n])
