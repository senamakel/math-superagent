import sympy as sp

# Ponder This (IBM) May 2001: threshold T for goblin/swimmer on circular lake.
# Governing equations: cos(B) = 1/T, sin(B) = (1/T)*(pi + B)
# => tan(B) = pi + B,  and T = 1/cos(B).
# Let x = pi + B (smallest positive solution of tan(x) = x, x ~ 4.4934).
# Then B = x - pi, T = 1/cos(x-pi) = -1/cos(x) = sqrt(1+x^2).

x = sp.Symbol('x', real=True)
# solve tan(x) = x, smallest positive nonzero solution
sol = sp.nsolve(sp.tan(x) - x, 4.5)
print("x (root of tan x = x):", sol.evalf(20))

B = sol - sp.pi
T = sp.sqrt(1 + sol**2)
print("B = x - pi:", B.evalf(20))
print("T = sqrt(1+x^2):", T.evalf(20))

# Also directly solve the two governing equations
B2 = sp.Symbol('B2', real=True)
T2 = sp.Symbol('T2', real=True)
sol2 = sp.nsolve([sp.cos(B2) - 1/T2, sp.sin(B2) - (sp.pi + B2)/T2], [B2, T2], [1.35, 4.6])
print("Direct solve: B =", sol2[0].evalf(20), " T =", sol2[1].evalf(20))

# Check the naive 'stage at radius 1/v diametrically opposite then dash radially' bound.
print("Naive staging bound pi+1 =", (sp.pi+1).evalf(10), " (WRONG constant; escape only below this)")
