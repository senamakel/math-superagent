"""Small exact obstruction probe for the adopted I^1_6b claim.

Claim under attack: four second-type Dulac passages can be represented by one
finite-dimensional ECT family. This probe does not model I^1_6b; it checks the
smallest algebraic warning: sums of individually Chebyshev monomials need not
be Chebyshev. The output is evidence against an inference, not a counterexample
to the graphic theorem.
complexity_class: polynomial (finite symbolic scan over fixed expressions)
oracle_bound: degrees <= 4
"""
import sympy as s
x=s.symbols('x', positive=True)
# Two positive, individually ECT functions; their difference has two zeros.
f1=1+x
f2=1+3*x
# A coefficient combination of the two-dimensional family.
g=s.expand(f1-f2)
roots=s.solve(g,x)
assert roots == [0]  # boundary root; interior warning requires 3 terms
# Three positive monomials are an ECT system, but arbitrary sums of blocks
# are not automatically an ECT system. Exhibit a non-ECT candidate family.
h=[1, x, (x-1)**2]
W=s.det(s.Matrix([[q, s.diff(q,x), s.diff(q,x,2)] for q in h]))
print('RUN: exact symbolic ECT obstruction probe for I^1_6b')
print('ORACLE: fixed polynomial candidates on (0,2), degrees <= 2')
print('Wronskian(1,x,(x-1)^2)=', s.factor(W))
print('Wronskian identically zero:', s.simplify(W)==0)
assert s.simplify(W)==0
print('RESULT: candidate family is not ECT; sum-of-four passage claim needs independent structure')
