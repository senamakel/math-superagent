"""Ground the three inventor approaches on their checkable structural claims.

1. Delsarte/Krawtchouk LP: minimize a_1 (average internal degree) over the
   Delsarte polytope of H(2,n) with |S| = 2^{n-1}+1. Compare LP value to f(n)
   and to sqrt(n).  a_1 = 2e(S)/|S| = average internal degree, and D(S) >= a_1,
   so LP min a_1 is a valid lower bound on f(n) -- the question is how far it
   reaches (the averaging obstruction says not sqrt(n)).

2. Clifford extremal-set claim "S = parity class + one excitation": check the
   exact exhaustive n=4 witness against it.
"""
from scipy.optimize import linprog
import math

def krawtchouk(n, i, x):
    """K_i(x) for binary Hamming scheme."""
    from math import comb
    tot = 0.0
    for k in range(i + 1):
        tot += (-1) ** k * comb(x, k) * comb(n - x, i - k)
    return tot

def delsarte_lp_a1(n, M):
    """LP value: min a_1 s.t. a_0=1, a_i>=0, sum a_i=M, (K a)_j >=0."""
    N = n + 1
    c = [0.0] * N
    c[1] = 1.0  # minimize a_1
    # constraints: A_ub a <= b_ub, A_eq a = b_eq
    A_eq = [[0.0] * N]
    A_eq[0][0] = 1.0
    b_eq = [1.0]
    A_ub, b_ub = [], []
    # (K a)_j >= 0  ->  -K a <= 0
    for j in range(N):
        row = [0.0] * N
        for i in range(N):
            row[i] = -krawtchouk(n, i, j)
        A_ub.append(row)
        b_ub.append(0.0)
    bounds = [(0.0, None)] * N
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")
    if not res.success:
        return None, res.message
    val = res.fun
    # report a vector too
    return val, res.x

f = {1: 1, 2: 2, 3: 2, 4: 2, 5: 3}
print("n  M=2^(n-1)+1  f(n)  sqrt(n)  LP min a_1")
for n in range(1, 7):
    M = 2 ** (n - 1) + 1
    val, _ = delsarte_lp_a1(n, M)
    vs = f"{(val if val is not None else 'infeasible'):>8}" if not isinstance(val, str) else val
    print(f"{n}  {M:>7}  {f.get(n,'?'):>3}  {math.sqrt(n):7.3f}  {vs}")

print("\n--- n=1..5 LP a vector (a_0..a_n) ---")
for n in range(1, 6):
    M = 2 ** (n - 1) + 1
    val, x = delsarte_lp_a1(n, M)
    if x is not None:
        print(f"n={n} LPa1={val:.4f}  a={[round(t,3) for t in x]}")

print("\n--- Clifford extremal-set claim: n=4 exact witness ---")
# witness from f-exact-1..5 note: n=4, S={0,1,2,5,6,11,12,13,14}, size 9
S4 = [0, 1, 2, 5, 6, 11, 12, 13, 14]
pc = [bin(v).count("1") for v in S4]
print("n=4 witness:", S4)
print("popcounts:", pc)
# parity class of size 2^{n-1}=8 is {x : popcount even}. parity+one would be
# that set plus any one extra vertex.
even = [v for v in range(16) if bin(v).count("1") % 2 == 0]
odd = [v for v in range(16) if bin(v).count("1") % 2 == 1]
print("even parity class (size 8):", even)
print("odd parity class (size 8):", odd)
def parity_plus_one(S):
    S = set(S)
    if len(S) != 9:
        return False
    for v in range(16):
        if S == set(even) | {v}:
            return True
        if S == set(odd) | {v}:
            return True
    return False
print("witness is parity-plus-one?", parity_plus_one(S4))
