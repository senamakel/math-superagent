"""Verify the algebraic step in Jailton Ferreira's claimed proof
(arXiv:1506.06621) that no 3x3 magic square of distinct squares exists.

The crux is equations (44)-(49) of the paper. Setup:
  2e^2 = m^2 + n^2            (44)  -- main diagonal AP (m^2, e^2, n^2)
  2e^2 = (m-z)^2 + (n+w)^2    (45)  -- middle column AP through centre
Subtracting (46):  (m-z)^2 + (n+w)^2 - (m^2 + n^2) = 0

The paper solves (46)/(41) for z:
  z1 = m + sqrt(m^2 - 2nw - w^2)
  z2 = m - sqrt(m^2 - 2nw - w^2)
rejects z1 because m - z1 < 0, keeps z2.

Then it claims: substituting (43)=z2 into (46) yields (47):
  n^2 - 2 n w - w^2 - (n+w)^2 = 0        (47)
which then forces w = 0 or w = -2n, giving the contradiction.

We check with sympy whether (47) really follows, and what the
substitution actually gives.
"""
import sympy as sp

m, n, w, z = sp.symbols('m n w z', positive=True)
S = sp.sqrt(m**2 - 2*n*w - w**2)   # the radicand

z2 = m - S

# Equation (46) expanded: (m-z)^2 + (n+w)^2 - m^2 - n^2 = 0
E46 = (m - z)**2 + (n + w)**2 - m**2 - n**2

# What does substituting z = z2 into (46) give?
sub_res = sp.simplify(E46.subs(z, z2))
print("substituting z2 into (46) gives (simplified):", sub_res)

# The paper's claimed (47):
claim47 = n**2 - 2*n*w - w**2 - (n + w)**2
print("paper's claimed (47):", claim47)
print("claimed (47) simplified:", sp.simplify(claim47))

# Check: is the correct substitution equal to the paper's (47)?
print("substitution == claimed (47)?", sp.simplify(sub_res - claim47) == 0)

# Now the paper's (47) roots:
roots = sp.solve(sp.Eq(claim47, 0), w)
print("roots of claimed (47):", roots)

# Correct relation from the true substitution (identity) -- solve (46) for z:
sol_z = sp.solve(sp.Eq(E46, 0), z)
print("true roots of (46) for z:", sol_z)
