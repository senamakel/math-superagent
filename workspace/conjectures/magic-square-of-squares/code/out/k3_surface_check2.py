#!/usr/bin/env python3
"""Independent verification of the claims encoded in code/out/k3_surface_checks.py.

Route differs from the original script: 
  - magic-square facts via lib/mss.py (grid_from_params, magic_sum, count_squares,
    is_perfect_square) instead of hand-rolled checks;
  - the rational point on the K3 S: T^2+U^2 = V^2+W^2 = X^2+Y^2, TU+VW+XY=0,
    found by brute force over a bounding box on the Pythagorean split factors,
    exact integer arithmetic throughout.
The (a,b,c) for Bremner II Category III Figure 1 are recovered from the printed
grid via the (c,u,v) parametrisation (params_from_grid), which is itself
verified (near-miss-baseline-and-incidence).
"""

from lib.mss import (grid_from_params, params_from_grid, magic_sum,
                     count_squares, is_perfect_square, sqrt_or_none,
                     lines_of, LINE_NAMES)

# --- Figure 1 Category III square (Bremner II 2001, p. 291) ---
grid = [
    [541**2, 421**2, 49**2],
    [-132839, 157441, 447721],
    [559**2, 371**2, 149**2],
]

rows = [sum(r) for r in grid]
cols = [sum(grid[i][j] for i in range(3)) for j in range(3)]
diags = [grid[0][0]+grid[1][1]+grid[2][2], grid[0][2]+grid[1][1]+grid[2][0]]
print("row sums", rows, "col sums", cols, "diag sums", diags)
print("magic constant =", rows[0])

c, u, v = params_from_grid(grid)
print("params_from_grid: c =", c, " u =", u, " v =", v)
print("grid_from_params reproduces:", grid_from_params(c, u, v) == grid)
print("magic_sum:", magic_sum(grid), " count_squares:", count_squares(grid))

# Category III six-square conditions: +-a+c, +-b+c, +-(a+b)+c with a=u, b=v
conds = {"u+c": c+u, "-u+c": c-u,
         "v+c": c+v, "-v+c": c-v,
         "(u+v)+c": c+u+v, "-(u+v)+c": c-(u+v)}
print("\nCategory III conditions (u=%, v=% as a,b):" )
for k, val in conds.items():
    r = sqrt_or_none(val)
    print(f"  {k:>10} = {val:>9}  square? {r is not None} ({r if r is not None else '-'})")

# --- rational point on S: T^2+U^2 = V^2+W^2 = X^2+Y^2, TU+VW+XY = 0 ---
# From the six-square parametrisation: u = 2TU, v = 2VW, u+v = -2XY (Bremner II).
def find_point(ub):
    found = []
    for T in range(-ub, ub+1):
        for U in range(-ub, ub+1):
            if 2*T*U != u: continue
            T2 = T*T + U*U
            for V in range(-ub, ub+1):
                for W in range(-ub, ub+1):
                    if 2*V*W != v: continue
                    if V*V + W*W != T2: continue
                    for X in range(-ub, ub+1):
                        for Y in range(-ub, ub+1):
                            if 2*X*Y != -(u+v): continue
                            if X*X + Y*Y != T2: continue
                            if T*U + V*W + X*Y == 0:
                                found.append((T,U,V,W,X,Y))
    return found

pts = find_point(700)
print("\npoints on S with 2TU=u, 2VW=v, -2XY=u+v (box 700):")
for p in pts[:10]:
    print("  ", p, "T^2+U^2 =", p[0]**2+p[1]**2)
print("count:", len(pts))

# --- four-AP coverage of the nine entries ---
g = grid_from_params('c', 'u', 'v')
lines = {
    "diff u (main diag)": [g[0][0], g[1][1], g[2][2]],
    "diff v (anti diag)": [g[0][2], g[1][1], g[2][0]],
    "diff u+v (mid col)": [g[0][1], g[1][1], g[2][1]],
    "diff u-v (mid row)": [g[1][0], g[1][1], g[1][2]],
}
covered = set(x for L in lines.values() for x in L)
all9 = set(x for row in g for x in row)
print("\nentries covered by the four centre APs:", sorted(covered))
print("all nine:", sorted(all9))
print("four APs cover all nine (centre once):", covered == all9)
print("not covered:", sorted(all9 - covered))