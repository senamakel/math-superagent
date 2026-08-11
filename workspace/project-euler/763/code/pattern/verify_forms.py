import sympy
n = sympy.Symbol('n')

table = {}
for N in range(2,13):
    from collections import Counter
    with open(f"data/level_{N}.txt") as f:
        lines=f.read().splitlines()
    c=Counter()
    for ln in lines:
        c[int(ln.split("|")[1].strip())]+=1
    table[N]=dict(c)
table[13]={7:612,8:9342,9:51678,10:172044,11:393660,12:590490,13:531441}
table[14]={7:267,8:7122,9:54756,10:237897,11:688905,12:1417176,13:1948617,14:1594323}

def R(N,M,table):
    k=N-M
    return sympy.Rational(table[N][M], 3**(N-2*k-1))

# Closed forms claimed:
forms = {
 0: lambda n: 1,
 1: lambda n: n-3,
 2: lambda n: (n-5)*(n+2)/2,
 3: lambda n: (n**3-73*n+168)/6,
}

# Verify k=0..3 on every available point (N up to 14, including fresh 13,14)
print("=== k=0..3 closed forms vs exactly-measured R ===")
for k, f in forms.items():
    ok=True
    for N in sorted(table):
        for M,cnt in table[N].items():
            if N-M==k:
                val = R(N,M,table)
                pred = sympy.simplify(f(n)).subs(n,N)
                match = (val==pred)
                if not match: ok=False; print(f"  k={k} N={N} M={M}: R={val} pred={pred} MISMATCH")
                else: print(f"  k={k} N={N}: R={val} pred={pred} OK")
    print(f"  -> k={k} all match: {ok}")

# k=4: fit degree-4 polynomial on N=9..13 (5 points), predict N=14
print("\n=== k=4 out-of-sample: fit degree 4 on N=9..13, predict N=14 ===")
pts = [(N, R(N,N-4,table)) for N in range(9,14)]
print("fit points:", [(p,str(v)) for p,v in pts])
x=sympy.symbols('x')
coef = sympy.symbols('c0:5')
poly = sum(coef[i]*x**i for i in range(5))
sols = sympy.solve([sympy.Eq(poly.subs(x,p), v) for p,v in pts], coef)
fit = sympy.expand(poly.subs(sols))
print("fitted Q_4(x) =", fit)
pred14 = sympy.simplify(fit.subs(x,14))
actual14 = R(14,10,table)
print(f"predict x=14: {pred14}, actual R(14,10)={actual14}, match={pred14==actual14}")

# provided Q_4 closed form
Q4 = sympy.expand(n**4/24 + n**3/4 - sympy.Rational(205,24)*n**2 + sympy.Rational(97,4)*n + 27)
print("claimed Q_4 =", Q4)
print("fit==claimed:", sympy.simplify(fit-Q4)==0)
