import sympy as sp
from fractions import Fraction

# Q_k(N) exact values (from prior run output, N -> Q_k(N))
Q = {
 0: {2:1,3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1},
 1: {4:1,5:2,6:3,7:4,8:5,9:6,10:7,11:8,12:9,13:10,14:11},
 2: {6:4,7:9,8:15,9:22,10:30,11:39,12:49,13:60,14:72},
 3: {8:16,9:40,10:73,11:116,12:170,13:236,14:315},
 4: {9:9,10:82,11:203,12:384,13:638,14:979},
 5: {11:72,12:418,13:1038,14:2028},
}

n = sp.symbols('n')
print("=== Degree of each column via exact interpolation ===")
for k in sorted(Q):
    pts = sorted(Q[k])
    # find polynomial degree: interpolate at different degrees, check if exact
    # just report points count; degree hypothesis = k
    # Verify Q_k is degree-k polynomial: fit degree k and k-1
    # Fit degree k polynomial through first k+1 points, check remaining
    fit_deg = k
    xs = [sp.Integer(x) for x in pts[:fit_deg+1]]
    ys = [sp.Integer(Q[k][x]) for x in pts[:fit_deg+1]]
    poly = sp.interpolate(list(zip(xs, ys)), n)
    ok = all(poly.subs(n, N) == Q[k][N] for N in pts)
    print(f"k={k}: degree-{k} interpolant fits ALL {len(pts)} points: {ok}")
    if ok:
        # leading coefficient
        lc = sp.Poly(poly, n).LC()
        print(f"    Q_{k}(n) = {sp.expand(poly)}")
        print(f"    leading coeff = {lc}  (1/k! = {Fraction(1, __import__('math').factorial(k))})")
    print()

# Explicit closed forms from prior run and fresh check
print("=== Verify prior closed forms at ALL points (incl fresh 13,14) ===")
forms = {
 0: (sp.Integer(1), lambda n: sp.Integer(1)),
 1: (n-3, lambda n: n-3),
 2: ((n-5)*(n+2)/2, lambda n: (n-5)*(n+2)//2),
 3: (n**3/6 - sp.Rational(73,6)*n + 28, lambda n: (n**3 - 73*n + 168)//6),
}
for k,(expr,fn) in forms.items():
    pts = sorted(Q[k])
    ok = all(fn(N) == Q[k][N] for N in pts)
    print(f"Q_{k}(n)={sp.expand(expr)}: matches all {len(pts)} points (incl fresh 13,14): {ok}")

# Q_4 explicit: prior claimed N^4/24+N^3/4-205N^2/24+97N/4+27
q4 = lambda n: n**4//24 + n**3//4 - 205*n**2//24 + 97*n//4 + 27
# careful with integer division for non-divisible; recompute as rational
def q4r(n):
    return (n**4 + 6*n**3 - 205*n**2 + 582*n + 648)//24
pts4 = sorted(Q[4])
print(f"\nQ_4 claimed closed form (n^4+6n^3-205n^2+582n+648)/24:")
ok = all(q4r(N) == Q[4][N] for N in pts4)
print(f"   matches all {len(pts4)} points incl fresh 13,14: {ok}")
for N in pts4:
    print(f"   N={N}: claimed={q4r(N)} measured={Q[4][N]}")
