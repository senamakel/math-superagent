"""Verify the CORRECTED osculating-curve reformulation (char 0, exact sympy).

Facts to verify (hand-checked for n=2,3; extended here to n=4,5,6):
1. C_f(x) = [H_0 f : ... : H_{n-1} f] equals L_f . gamma_n(x), where
   gamma_n(x) = [1 : x : ... : x^n] is the moment curve in P^n, and
   L_f[i,j] = C(i+j, i) * c_{i+j}  (c_k = coeff of x^k, c_n = 1).
   So the universal entries C(n,i) sit on the ANTI-diagonal i+j = n.
2. The kernel of L_f is 1-dimensional; a point xi_f = [xi_0:...:xi_n] of P^n
   with L_f . xi_f = 0. For f = (x-a)^n, xi_f = gamma_n(a) (center on curve).
3. f pure power <=> xi_f lies on the moment curve gamma_n.
4. Incidence: (exists b: f(b)=H_i f(b)=0) <=> C_f(b) in H_0 cap H_i.
"""
import sympy as sp

def H(f, i):
    g = f
    for _ in range(i):
        g = sp.diff(g, sp.Symbol('x'))
    return sp.expand(g / sp.factorial(i))

x, a = sp.symbols('x a')

for n in (4, 5, 6):
    cs = sp.symbols(f'c0:{n}')  # c_0..c_{n-1} (c_n = 1)
    f = x**n + sum(sp.Symbol(f'c{k}') * x**k for k in range(n))
    coords = [H(f, i) for i in range(n)]  # f, H1 f, ..., H_{n-1} f

    # build L_f: rows i=0..n-1, cols j=0..n; entry C(i+j,i)*c_{i+j}, c_n=1
    c = {k: sp.Symbol(f'c{k}') for k in range(n)}
    c[n] = sp.Integer(1)
    L = sp.zeros(n, n+1)
    for i in range(n):
        for j in range(n+1):
            k = i + j
            if k <= n:
                L[i, j] = sp.binomial(k, i) * c[k]
    # check L . gamma == coords
    gamma = [x**j for j in range(n+1)]
    for i in range(n):
        lhs = sum(L[i, j]*gamma[j] for j in range(n+1))
        assert sp.expand(lhs - coords[i]) == 0, (n, i)
    # check anti-diagonal entries are C(n,i)
    for i in range(n):
        j = n - i
        assert sp.simplify(L[i, j]) == sp.binomial(n, i), (n, i, j, L[i, j])
    print(f"n={n}: C_f = L_f . gamma_n, anti-diagonal = C(n,i)  OK")

# kernel / projection center for pure power
for n in (4, 5):
    f = (x - a)**n
    c = {}
    # expand: c_k = coeff of x^k = C(n,k) (-a)^{n-k}
    for k in range(n+1):
        c[k] = sp.binomial(n, k) * (-a)**(n-k)
    L = sp.zeros(n, n+1)
    for i in range(n):
        for j in range(n+1):
            k = i + j
            if k <= n:
                L[i, j] = sp.binomial(k, i) * c[k]
    # candidate kernel: gamma_n(a) = [1, a, ..., a^n]
    xi = [a**j for j in range(n+1)]
    for i in range(n):
        val = sum(L[i, j]*xi[j] for j in range(n+1))
        assert sp.simplify(val) == 0, (n, i, val)
    print(f"n={n} pure power f=(x-a)^n: xi_f = gamma_n(a) in kernel  OK")

print("all checks passed")
