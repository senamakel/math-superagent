"""Exact check of the Nullstellensatz colouring edge polynomial for k=4.
Verifies that the edge polynomial S_e over the 4th roots of unity vanishes
iff the two vertices receive distinct colours.
"""
import sympy as sp

roots = [sp.I**j for j in range(4)]  # 1, i, -1, -i ; the 4th roots of unity

def S(xu, xv):
    return xu**3 + xu**2*xv + xu*xv**2 + xv**3

print("i  j  | S(root_i, root_j) == 0 ?  (expect True iff i != j)")
all_ok = True
for i in range(4):
    for j in range(4):
        val = sp.simplify(S(roots[i], roots[j]))
        zero = sp.simplify(val) == 0
        expect = (i != j)
        ok = (zero == expect)
        all_ok = all_ok and ok
        print(f"{i}  {j}  | {zero}   expect {expect}   ok={ok}")
print("ALL CORRECT:", all_ok)

# Also verify the rational-form identity S = (x_u^4 - x_v^4)/(x_u - x_v)
xu, xv = sp.symbols('xu xv')
lhs = S(xu, xv)
rhs = sp.simplify((xu**4 - xv**4)/(xu - xv))
print("Identity S == (xu^4-xv^4)/(xu-xv):", sp.simplify(lhs - rhs) == 0)
