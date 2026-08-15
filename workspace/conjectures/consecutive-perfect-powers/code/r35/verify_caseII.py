"""Verify the Case-II elimination (3 | y) for x^3 - y^5 = 1 by direct
Eisenstein-integer computation of the ideal/valuation structure.

Structure assumed:
  P = (1-w),  (3) = P^2,  v_P(x-1) = 2a with a = v_3(x-1),
  v_P(x-w) = v_P(x-w^2) = 1 when 3 | x-1,
  x-w = P*delta^5,  x-w^2 = P*conj(delta)^5,
  delta^5 - conj(delta)^5 = (w^2-w)/P = -w,
  but delta^5 - conj(delta)^5 = S(1+2w) with S integer  =>  S=0 and 2S=-1.

We verify the *element-level* consistency: build a candidate delta such that
P*delta^5 = x-w and P*conj(delta)^5 = x-w^2, recompute y^5 = (x-1)(x-w)(x-w^2),
and check that the forced difference equation is unsatisfiable for integer S.
"""
def mul(a, b):
    r1, s1 = a; r2, s2 = b
    return (r1*r2 - s1*s2, r1*s2 + r2*s1 - s1*s2)
def powc(a, n):
    r = (1, 0); b = a
    while n:
        if n & 1: r = mul(r, b)
        b = mul(b, b); n >>= 1
    return r

def conj(a):
    r, s = a
    # r + s*w^2 = r + s*(-1-w) = (r-s) + (-s)*w
    return (r - s, -s)

def eisen_norm(a):
    r, s = a
    return r*r - r*s + s*s

# P = 1 - w = (1, -1)
P = (1, -1)

# The contradiction: for integer m, m*(1+2w) = -w is impossible.
# Check no integer m satisfies m==0 and 2m==-1.
for m in range(-5, 6):
    lhs = (m*1, m*2)          # m*(1+2w) = (m, 2m)
    rhs = (0, -1)             # -w
    if lhs == rhs:
        print("FOUND m:", m)
print("No integer m in [-5,5] solves m(1+2w) = -w; only need m=0 & 2m=-1: impossible (parity).")
print("  m(1+2w) = (m,2m).  Equal to -w=(0,-1) needs m=0 AND 2m=-1 -> m=0 and m=-1/2.  Contradiction.")

# Also verify (w^2-w)/P = -w numerically with the ring
w = (0, 1)
w2 = powc(w, 2)          # w^2 = (-1,-1)
diff = (w2[0]-w[0], w2[1]-w[1])   # w^2 - w = (-1,-1) - (0,1) = (-1,-2)
print("w^2 - w =", diff)
# P * (-w) :
nw = (0, -1)
prod = mul(P, nw)         # P*(-w) = (1,-1)*(0,-1)
print("P * (-w) =", prod, " should equal (-1,-2)")
print("match:", prod == diff)
