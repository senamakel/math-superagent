from fractions import Fraction

def S(k):
    return Fraction(4**(k-1)) * (Fraction(k) - Fraction(13,6)) + Fraction(2*k-1,3)

# Let's FIRST verify the theoretical claim properly with a symbolic recurrence finder
# on exact rationals over enough terms. We'll solve the linear system directly.
#
# Guess: a_j = S_{3j} satisfies a constant-coefficient linear recurrence.
# Solve for order-4 recurrence coefficients (u1..u4) with
#   a_{j+4} = u1 a_{j+3} + u2 a_{j+2} + u3 a_{j+1} + u4 a_j
# using 8 equations from j=1..8 (overdetermined -> check consistency).

def solve_recurrence(seq, order, eqs):
    # build matrix [a_{j+3}, a_{j+2}, a_{j+1}, a_j] and target a_{j+4}
    from fractions import Fraction as F
    A = []; b = []
    for j in range(eqs):
        row = [seq[j+order-1], seq[j+order-2], seq[j+order-3], seq[j]]  # j+3...j
        A.append(row); b.append(seq[j+order])
    # Gaussian elimination
    m = order
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for col in range(m):
        piv = next((r for r in range(col, len(M)) if M[r][col] != 0), None)
        if piv is None: return None
        M[col], M[piv] = M[piv], M[col]
        pv = M[col][col]
        M[col] = [x/pv for x in M[col]]
        for r in range(len(M)):
            if r != col and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f*b for a,b in zip(M[r], M[col])]
    sol = [M[r][m] for r in range(m)]
    # check on remaining equations
    for j in range(eqs, len(seq)-order):
        lhs = seq[j+order]
        rhs = sum(sol[q]*seq[j+order-1-q] for q in range(order))
        if lhs != rhs:
            return ("fail", j, lhs, rhs)
    return sol

# gather enough terms of a_j
a = [S(3*j) for j in range(1, 30)]
print("a_1..a_8:", a[:8])
sol = solve_recurrence(a, 4, eqs=8)
print("order-4 recurrence coeffs [u1,u2,u3,u4] (a_{j+4}=sum u a_{j+...}):", sol)
if isinstance(sol, list):
    # verify the whole sequence obeys it
    ok = all(sum(sol[q]*a[j+3-q] for q in range(4)) == a[j+4] for j in range(len(a)-4))
    print("holds for all a_j j=1..29:", ok)

# Also do it for the raw S_k to confirm (E-4)^2(E-1)^2
s = [S(k) for k in range(1, 30)]
sol2 = solve_recurrence(s, 4, eqs=8)
print("raw S_k order-4 coeffs:", sol2)
