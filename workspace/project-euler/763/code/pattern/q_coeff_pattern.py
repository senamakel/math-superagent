import sympy as sp
from fractions import Fraction
from math import factorial

n = sp.symbols('n')

# Exact Q_k(N) values from prior run (N -> Q_k(N))
Q = {
 1: {4:1,5:2,6:3,7:4,8:5,9:6,10:7,11:8,12:9,13:10,14:11},
 2: {6:4,7:9,8:15,9:22,10:30,11:39,12:49,13:60,14:72},
 3: {8:16,9:40,10:73,11:116,12:170,13:236,14:315},
 4: {9:9,10:82,11:203,12:384,13:638,14:979},
}

print("=== Q_k(n) - n^k/k! (the lower-order part) ===")
for k in sorted(Q):
    pts = sorted(Q[k])
    xs = [sp.Integer(x) for x in pts[:k+1]]
    ys = [sp.Integer(Q[k][x]) for x in pts[:k+1]]
    poly = sp.interpolate(list(zip(xs, ys)), n)
    base = n**k / sp.Integer(factorial(k))
    lower = sp.expand(poly - base)
    print(f"k={k}:  Q_k(n) = {sp.expand(poly)}")
    print(f"       lower part Q_k - n^k/{k}! = {lower}")
    print()

# Reconstruct D(N) from columns k=0..4 and see where k=5+ matters
print("=== D(N) reconstruction from model columns ===")
D_true = {2:3,3:9,4:30,5:99,6:336,7:1134,8:3855,9:13086,10:44499,
          11:151263,12:514419,13:1749267,14:5949063}
# Q_0=1, Q_1=n-3, Q_2=(n-5)(n+2)/2, Q_3, Q_4 closed forms
def Q0(n_): return sp.Integer(1)
def Q1(n_): return n_-3
def Q2(n_): return (n_-5)*(n_+2)//2
def Q3(n_): return (n_**3 - 73*n_ + 168)//6
def Q4(n_): return (n_**4 + 6*n_**3 - 205*n_**2 + 582*n_ + 648)//24
for N in range(2,15):
    val = 0
    for k in range(0,5):
        exp = N-2*k-1
        if exp < 0: break
        Qk = [Q0,Q1,Q2,Q3,Q4][k]
        val += Qk(N) * 3**exp
    print(f"N={N}: model k=0..4 => {val},  true D={D_true[N]}, "
          f"match={val==D_true[N]}  (k=5+ contributes if k<=N-2)")
