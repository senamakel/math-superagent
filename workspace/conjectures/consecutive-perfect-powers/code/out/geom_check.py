import sympy as sp

# Diagnose the step-5 geometric-sum FAIL: is it a real identity breach or a
# sympy simplification artifact?  Use a concrete symbolic p (a Number), and
# also rationalize the (x^p-1)/(x-1) division.
x = sp.symbols('x')
kk = sp.symbols('kk', integer=True, nonnegative=True)

# Symbolic p: summation over 0..p-1 likely cannot simplify symbolically.
# Test with concrete positive integers p.
for p in [2, 3, 5, 7, 11, 17]:
    s = sp.summation(x**kk, (kk, 0, p - 1))
    closed = (x**p - 1) / (x - 1)
    # compare after expanding both fully
    diff = sp.simplify(sp.expand(s) - sp.expand(closed))
    print(f"p={p}: sum= {sp.expand(s)}, closed-diff simplifed= {diff}  "
          f"equal={diff == 0}")

# Also the summation expression with symbolic p should equal (x^p-1)/(x-1)
# as a rational function; sympy leaves sum unevaluated for symbolic p.
p = sp.symbols('p', integer=True, positive=True)
s_expr = sp.summation(x**kk, (kk, 0, p - 1))
print("\nsymbolic-p summation expr:", s_expr)
print("closed form:", (x**p - 1) / (x - 1))
print("Difference of expressions (may be unevaluated):",
      sp.simplify(s_expr - (x**p - 1) / (x - 1)))
