import sympy as sp
from sympy import Rational, factorial, symbols

A = {2:1,3:10,4:184,5:5052,6:191232,7:9851040,8:650626560,9:54052427520,
     10:5514150297600,11:680309947699200}
B = {3:1,4:0,5:-108,6:-3600,7:-208800,8:-12418560,9:-932601600,
     10:-85305830400,11:-9900701798400}
def fact(n): return sp.factorial(n)
def H(n): return sum(Rational(1,k) for k in range(1,n+1))

def fit_fixed_form(vals, form_fn):
    """Try v[n] == form_fn(n) * K for a constant K over all n; returns K if constant."""
    Ks=set()
    for n in vals:
        f=form_fn(n)
        if f==0: return None
        Ks.add(Rational(vals[n])/f)
    return Ks.pop() if len(Ks)==1 else None

# ---- A_n scale guesses ----
print("=== A_n : look for A_n/(n!^2) = c1 + c2 H_n + c3/n + c4 H_n/n ===")
# A_n/(n!)^2
rA={n:Rational(A[n],fact(n)**2) for n in range(2,12)}
# try rA_n - (n-H_n)/2  (this would be the const if A ~ partial)
for n in range(2,12):
    print(f"  n={n}: A/(n!)^2={rA[n]}  (n-H_n)/2={Rational(n-H(n),2)}  diff={sp.simplify(rA[n]-Rational(n-H(n),2))}")

print("\n=== B_n scale guesses ===")
rB={n:Rational(B[n],fact(n)**2) for n in range(5,12)}
for n in range(5,12):
    print(f"  n={n}: B/(n!)^2={rB[n]}   -2*B/(n!)(n-1)!={sp.simplify(Rational(-2*B[n],fact(n)*fact(n-1)))}")

# try B_n = - (n!)(n-1)! * c_n, c_n?  |B|/(n-1)! : integers only for n>=6
print("\n|B|/(n-1)! for n=5..11:")
for n in range(5,12):
    print(f"  n={n}: {Rational(abs(B[n]),fact(n-1))}")

# E1: (n-1)A + (n-1)(n-2)B/2 = (n!)^2 (n-H_n)/2  [PROVEN]
# solve for B given that; then A:
print("\n=== Using E1 (proven closed form), express A_n from B_n ===")
for n in range(3,12):
    # A = [ (n!)^2(n-Hn)/2 - (n-1)(n-2)B/2 ]/(n-1)
    val = (fact(n)**2*(n-H(n))//2 if (fact(n)**2*(n-H(n)))%2==0 else Rational(fact(n)**2*(n-H(n)),2))
    bc=B[n]
    Aexpr = (val - Rational(bc*(n-1)*(n-2),2))/(n-1)
    print(f"  n={n}: A_exp={sp.simplify(Aexpr)}  actual={A[n]}  check={sp.simplify(Aexpr)==A[n]}")
