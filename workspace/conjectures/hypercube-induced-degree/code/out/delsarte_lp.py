from scipy.optimize import linprog
from math import comb, sqrt

def krawtchouk(n, i, x):
    tot = 0.0
    for k in range(i + 1):
        tot += (-1) ** k * comb(x, k) * comb(n - x, i - k)
    return tot

def delsarte_lp_a1(n, M):
    N = n + 1
    c = [0.0] * N
    c[1] = 1.0
    A_eq = [[0.0] * N]
    A_eq[0][0] = 1.0
    b_eq = [1.0]
    A_ub, b_ub = [], []
    for j in range(N):
        row = [0.0] * N
        for i in range(N):
            row[i] = -krawtchouk(n, i, j)
        A_ub.append(row)
        b_ub.append(0.0)
    bounds = [(0.0, None)] * N
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq,
                  bounds=bounds, method="highs")
    return res

f = {1: 1, 2: 2, 3: 2, 4: 2, 5: 3}
print("n  2^(n-1)+1  f(n)  sqrt(n)  LPmin_a1")
for n in range(1, 7):
    M = 2 ** (n - 1) + 1
    res = delsarte_lp_a1(n, M)
    val = res.fun if res.success else None
    print(f"{n}  {M:>6}  {f.get(n,'?'):>3}  {sqrt(n):6.3f}  {val}")

print()
for n in range(1, 6):
    M = 2 ** (n - 1) + 1
    res = delsarte_lp_a1(n, M)
    if res.success:
        print(f"n={n} a1={res.fun:.5f} a={[round(t,3) for t in res.x]}")
