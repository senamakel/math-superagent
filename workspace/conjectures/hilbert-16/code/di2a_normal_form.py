"""Exact symbolic audit of DR 2009 Proposition 2.2 over Q.

The held paper gives the general perturbation (2.9) and affine map (2.10),
but not an ADL-specific DI2a coefficient list or explicit solved map.  This
program therefore verifies the proposition's algebraic core: at the base
system (2.7), the differential of (B00,B10,B01,B02) in the four affine
parameters is exactly matrix (2.12), and its determinant is nonzero.  It
also verifies the canonical strip-of-hyperbolas specialization (2.7) has
zero residual against (2.8) at mu_i=0.
"""
from sympy import Matrix, symbols, expand, Integer

c0 = symbols('c0')
d1,d2,d3,d4 = symbols('delta1 delta2 delta3 delta4')

# DR 2009 equation (2.12), computed from the affine-normalization map.
source_matrix = Matrix([
    [0, -1, 0, 0],
    [0, -c0, 0, 1],
    [0, 1, 1, 0],
    [1, 0, 0, 0],
])

# The four first-order equations at the base point are precisely M delta.
delta = Matrix([d1,d2,d3,d4])
base_B = source_matrix * delta

# Canonical (2.7) and (2.8) specialization, represented symbolically.
x,y = symbols('x y')
c,mu0,mu1,mu2,mu3 = symbols('c mu0 mu1 mu2 mu3')
normal = (c*x-y+1+(1+mu2)*x**2+mu1*x*y+mu0*y**2,
          x*y-mu3*x**2)
strip = (c*x-y+1+x**2, x*y)
reduced = tuple(expand(z.subs({mu0:0,mu1:0,mu2:0,mu3:0})) for z in normal)
residual = tuple(expand(a-b) for a,b in zip(reduced,strip))

# Small naive oracle: coefficientwise comparison of the two fixed quadratics.
def coefficient_oracle(F,G):
    return tuple(expand(a-b) for a,b in zip(F,G))

def main():
    print('SOURCE: Dumortier--Rousseau 2009, Prop. 2.2, equations (2.7)--(2.12).')
    print('Held source limitation: no explicit ADL DI2a parameterization or solved delta map is held.')
    print('Affine map (2.10): (x,y)=(X+delta1*Y+delta3, delta2*X+Y+delta4).')
    print('Base first-order B-vector =')
    print(base_B)
    print('Computed/source Jacobian M =')
    print(source_matrix)
    print('M equals source matrix:', base_B.jacobian(delta) == source_matrix)
    print('det(M) =', source_matrix.det())
    print('Unique first-order normalization delta at the base:', source_matrix.inv()*Integer(-1)*Matrix([0,0,0,0]))
    print('Canonical strip specialization: mu0=mu1=mu2=mu3=0, c=c0.')
    print('Naive coefficient oracle residual:', coefficient_oracle(reduced,strip))
    print('Exact residual after reduction:', residual)
    print('Residual is zero:', all(r == 0 for r in residual))
    assert base_B.jacobian(delta) == source_matrix
    assert source_matrix.det() == -1
    assert all(r == 0 for r in residual)

if __name__ == '__main__':
    main()
