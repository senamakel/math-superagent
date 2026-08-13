"""Oracle check: confirm the geometric type of the two representative pairs,
C(x,2)=C(y,3) (genus 1, elliptic) and C(x,2)=C(y,5) (genus 2, hyperelliptic),
so the correct effective integral-point engine is attributed to each.

Mechanical fact: C(x,2)=x(x-1)/2. Complete the square:
  (2x-1)^2 = 1 + 8*C(x,2).
Let w = 2x-1. Then the curve C(x,2)=C(y,k) becomes
  w^2 = 1 + 8*C(y,k).
The genus comes from the degree/parity of the polynomial in y on the right,
as this is a 2:1 (hyperelliptic) or split cover of P^1.
"""
from sympy import symbols, expand, factor

x, y, w = symbols('x y w')

def C(n, k):
    p = 1
    for i in range(k):
        p *= (n - i)
    return p / __import__('math').factorial(k)

for k in (3, 5):
    rhs = expand(1 + 8 * C(y, k))
    # RHS degree in y:
    from sympy import degree, Poly
    poly = Poly(rhs, y)
    print(f"C(x,2)=C(y,{k}): after w=2x-1, curve is w^2 = {rhs}")
    print(f"   RHS degree in y = {poly.degree()}, "
          f"hyperelliptic genus floor((deg-1)/2) = {(poly.degree()-1)//2}")
    if poly.degree() == 3:
        print("   -> genus 1 elliptic curve (w^2 = cubic); "
              "effective tool: David elliptic logarithms (g=1).")
    if poly.degree() == 5:
        print("   -> genus 2 hyperelliptic (w^2 = quintic); "
              "effective tool: BMSST hyperelliptic method (g=2).")
