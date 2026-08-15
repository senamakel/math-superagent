from sympy import Rational, Matrix, sqrt, simplify

# 24-cell vertices are all permutations of (+-1, +-1, 0, 0), integer coordinates.
# Two pairs with DIFFERENT source squared lengths:
#   A: (1,1,0,0) vs (1,-1,0,0)  -> diff (0,2,0,0),  squared length 4
#   B: (1,1,0,0) vs (1,0,1,0)   -> diff (0,-1,1,0), squared length 2
dA = Matrix([0, 2, 0, 0])
dB = Matrix([0, -1, 1, 0])

# Projection rows a, b (the two directions of the plane in R^4).
a = Matrix([0, 1, 3, 0])
b = Matrix([0, 0, 0, 1])

def Q(d, a, b):
    return simplify((a.dot(d))**2 + (b.dot(d))**2)

qA = Q(dA, a, b)
qB = Q(dB, a, b)
print("source |dA|^2 =", sum(x**2 for x in dA))
print("source |dB|^2 =", sum(x**2 for x in dB))
print("Q_pi(dA) =", qA)
print("Q_pi(dB) =", qB)
print("EQUALIZE:", simplify(qA - qB) == 0, " at value", qA)

# Also confirm the claim stated in the approach file: rows give Q = 4 for both.
assert simplify(qA - 4) == 0, "qA != 4"
assert simplify(qB - 4) == 0, "qB != 4"
print("PASS: two distinct source lengths (2 and sqrt2) project to the same planar length 2.")
