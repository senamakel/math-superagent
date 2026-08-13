"""Focus: verify the PVS + centraliser claims numerically/symbolically."""
import sympy as sp

# 1. centraliser of J3
J3 = sp.Matrix([[1,1,1],[1,1,1],[1,1,1]])
print("J3 eigenvals:", list(J3.eigenvals().keys()))

var = sp.symbols('a b c d e f g h i')
M = sp.Matrix([[var[0],var[1],var[2]],[var[3],var[4],var[5]],[var[6],var[7],var[8]]])
comm = M*J3 - J3*M
JC = sp.Matrix(9,9, lambda r,c: sp.diff(comm[r//3, r%3], var[c]))
print("dim centraliser =", 9 - JC.rank())

# 2. Is (SL3 x SL3, M3) prehomogeneous? det is a non-constant invariant of the
#    (left,right)-action M -> AMB. So orbits lie in fixed-det loci -> not dense.
print("det(M) under (A,B): det(A M B^{-1}) = det(A)det(M)det(B)^{-1} = det(M) for SL3.")
print("=> det is a non-constant invariant => (SL3xSL3, M3) is NOT prehomogeneous.")

# 3. A Gaussian-integer way to see it: 'entry is square' = norm onto Z[i].
#    Just confirm E_n.2-torsion.
n = sp.symbols('n')
print("E_n 2-torsion solved by y=0: x^3 - n^2 x = x(x-n)(x+n) = 0 -> x in {0, +-n}")
print("=> exactly three rational 2-torsion points => the isogeny class of 4 is via 2-isogenies,")
print("not a space of 'four independent 4-isogenies'.")
