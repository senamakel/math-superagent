import sympy as sp

D = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086, 44499, 151263, 514419, 1749267, 5949063]
N = len(D)

# Out-of-sample test: fit order-7 recurrence to first 14 terms (relations i=0..6),
# a 7x7 square system -> unique coefficients, then predict D(14).
order = 7
c = sp.symbols('c0:7')
eqs = []
for i in range(7):  # relations i=0..6 use terms 0..13
    lhs = D[i+order]
    rhs = sum(c[j]*D[i+j] for j in range(order))
    eqs.append(sp.Eq(lhs, rhs))
sol = sp.solve(eqs, c, dict=True)
print("Unique coeff solution from first 14 terms:", sol)
sol = sol[0]
pred14 = sum(sol[c[j]]*D[6+j] for j in range(order))  # D[14] = sum c_j D[6+j], i=7... wait
# D[n+7] = sum c_j D[n+j]; for D[14], n=7: D[14]=sum c_j D[7+j]
pred14 = sum(sol[c[j]]*D[7+j] for j in range(order))
print("Predicted D(14):", sp.nsimplify(pred14))
print("Actual D(14):   ", D[14])
print("MATCH:", sp.simplify(pred14 - D[14]) == 0)

# Also test with even fewer terms: fit to first 12 terms (relations 0..4 = 5 eqs, 7 unk -> 2 free)
# check the 2-param family still passes relations 5,6 and term 14.
print("\n--- Fit to first 12 terms only (relations i=0..4), 7 unknown, 5 eqs ---")
eqs2 = []
for i in range(5):
    lhs = D[i+order]
    rhs = sum(c[j]*D[i+j] for j in range(order))
    eqs2.append(sp.Eq(lhs, rhs))
sol2 = sp.linsolve(eqs2, c)
# check that relations at i=5 and i=6 are automatically satisfied by any solution
free = sp.symbols('t0 t1')
# We'll substitute a generic particular+null space and check residual of unfitted relations
# Instead: solve param solution and plug into remaining 3 relations (i=5,6, and D14)
F = sp.Matrix(eqs2)  # not matrix form; let's do linear algebra
# Build matrix A (5x7) and b
A = sp.zeros(5, order)
b = sp.zeros(5, 1)
for i in range(5):
    for j in range(order):
        A[i, j] = D[i+j]
    b[i] = D[i+order]
# particular solution
sol_p = sp.linsolve((A, b)).args[0]
nulls = A.nullspace()
print("nullspace dim:", len(nulls))
# generic solution = sol_p + combos
t = sp.symbols('t0:{}'.format(len(nulls)))
gen = list(sol_p)
for k, v in enumerate(nulls):
    for row in range(order):
        gen[row] = gen[row] + t[k]*v[row]
# check residual for relations i=5,6 and for D14
for rel, target in [(5, D[5+order]), (6, D[6+order])]:
    res = sum(gen[j]*D[rel+j] for j in range(order)) - target
    print(f"residual relation i={rel}:", sp.simplify(res))
res = sum(gen[j]*D[7+j] for j in range(order)) - D[14]
print("residual D14:", sp.simplify(res))
