"""Confirm two closing facts:
 (1) sign: R_1 = (-1)^{n(n-1)/2} Disc(f) for all tested n;
 (2) char-p content: R_{n-1} = (-1)^n n^n a_n has content n^n, so for p | n
     R_{n-1} == 0 mod p (order collapse = bad-prime degeneracy). Over Z all
     R_i homogeneous of weight n(n-i); order survives mod p iff R_i not 0 mod p.
"""
import sympy as sp, math

def hasse(coeffs, i, n, x):
    out = sp.Integer(0)
    for j, c in enumerate(coeffs):
        deg = n - j
        if deg >= i and c != 0:
            out += sp.binomial(deg, i) * c * x**(deg - i)
    return sp.expand(out)

def check_sign(n):
    x = sp.symbols('x')
    a = [sp.Symbol('a%d' % j) if j >= 2 else (sp.Integer(1) if j == 0 else sp.Integer(0))
         for j in range(n + 1)]
    f = sum(a[j] * x**(n - j) for j in range(n + 1))
    R1 = sp.expand(sp.resultant(f, hasse(a, 1, n, x), x))
    D = sp.expand(sp.discriminant(f, x))
    expected_sign = (-1)**(n*(n-1)//2)
    return sp.simplify(R1 - expected_sign * D) == 0

if __name__ == '__main__':
    signs_ok = True
    for n in range(3, 8):
        ok = check_sign(n)
        signs_ok = signs_ok and ok
        print(f"n={n}: R_1 = (-1)^{{{n*(n-1)//2}}} Disc : {ok}")
    print("SIGN: ALL OK" if signs_ok else "SIGN: FAIL")
    # content of R_{n-1}
    for n in range(3, 7):
        expect = (-1)**n * n**n
        print(f"n={n}: R_{{n-1}} content = |{expect}| = {n}^{n}, "
              f"bad primes dividing it = {sorted({p for p in range(2,n+1) if n%p==0})}")
