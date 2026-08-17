import sympy as sp

# k-union-closed generalized Boppana: alpha_k * h(x^k) >= x^(k-1) * h(x)
# where alpha_k is the positive root of x(1+x)^(k-1) = 1.
# The resulting UC constant is alpha_k/(1+alpha_k).  k=2 must give (3-sqrt5)/2.
for k in [2,3,4,8,16]:
    x = sp.symbols('x')
    root = sp.nsolve(x*(1+x)**(k-1) - 1, 0.5)
    c = root/(1+root)
    print(f"k={k:2d}: alpha={float(root):.6f}  constant={float(c):.6f}")

print("(3-sqrt5)/2 =", float((3-sp.sqrt(5))/2))
