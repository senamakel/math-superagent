#!/usr/bin/env python3
"""Verify the reading of Bremner II (2001) used to assess the Brauer-Manin approach.

Facts checked (exact integer arithmetic, no floats):
1. Bremner II Category III square (Figure 1) is a magic square with SIX square
   entries: the six conditions +-a+c, +-b+c, +-(a+b)+c are all perfect squares.
2. The (a,b,c) recovered from that square put a rational point
   (T,U,V,W,X,Y) on the K3 surface S: T^2+U^2 = V^2+W^2 = X^2+Y^2 and
   TU+VW+XY = 0, with a=2TU, b=2VW, a+b=-2XY, c=T^2+U^2=...  Hence S(Q) is
   nonempty, so no Brauer-Manin obstruction can prove S(Q)=empty.
3. Dimension sanity: the four-AP condition (8 non-centre entries squares) is
   the full nine-square condition (all 9 entries covered by the four APs).
"""

def is_sq(n):
    if n < 0:
        return False, None
    r = int(n ** 0.5)
    while (r+1)*(r+1) <= n: r += 1
    while r*r > n: r -= 1
    return r*r == n, (r if r*r == n else None)

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

# recover (a,b,c) from parametrisation (3):
#   a+c   -a-b+c   b+c
#   -a+b+c  c      a-b+c
#   -b+c   a+b+c   -a+c
c = grid[1][1]
a = grid[0][0] - c
b = grid[0][2] - c
print("a =", a, " b =", b, " c =", c)
# verify all nine entries reproduce
rec = [[a+c, -a-b+c, b+c],
       [-a+b+c, c, a-b+c],
       [-b+c, a+b+c, -a+c]]
print("reproduced grid matches:", rec == grid)

# six square conditions for Category III: +-a+c, +-b+c, +-(a+b)+c
conds = {
    "a+c": a+c, "-a+c": -a+c,
    "b+c": b+c, "-b+c": -b+c,
    "(a+b)+c": a+b+c, "-(a+b)+c": -(a+b)+c,
}
print("\nCategory III square conditions:")
for k, v in conds.items():
    ok, r = is_sq(v)
    print(f"  {k:>10} = {v:>8}  square? {ok} ({r if r is not None else '-'})" )

# --- rational point on S ---
# a = 2TU, b = 2VW, a+b = -2XY, c = T^2+U^2 = V^2+W^2 = X^2+Y^2
def try_pt():
    sqa_c, ra_c = is_sq(a+c)      # (T+U)^2
    sqc_a, rc_a = is_sq(c-a)      # (T-U)^2
    sqb_c, rb_c = is_sq(b+c)      # (V+W)^2
    sqc_b, rc_b = is_sq(c-b)      # (V-W)^2
    sqab_c, rab_c = is_sq(a+b+c)  # (X+Y)^2
    sqcab, rcab = is_sq(c-(a+b))  # (X-Y)^2
    print("\nsqrt values:", ra_c, rc_a, rb_c, rc_b, rab_c, rcab)
    found = []
    for T0 in range(-600, 601):
        for U0 in range(-600, 601):
            if 2*T0*U0 != a: continue
            for V0 in range(-600, 601):
                for W0 in range(-600, 601):
                    if 2*V0*W0 != b: continue
                    TT = T0*T0+U0*U0
                    if TT != V0*V0+W0*W0: continue
                    for X0 in range(-600, 601):
                        for Y0 in range(-600, 601):
                            if 2*X0*Y0 != -(a+b): continue
                            if X0*X0+Y0*Y0 != TT: continue
                            if T0*U0 + V0*W0 + X0*Y0 == 0:
                                found.append((T0,U0,V0,W0,X0,Y0))
    return found

pts = try_pt()
print("\nRational points on S (T,U,V,W,X,Y):", pts[:10], "count:", len(pts))

# --- four-AP coverage check ---
# grid in (c,u,v) parametrisation, entries covered by the four centre lines
c, u, v = 'c', 'u', 'v'
g = [[f"c+{u}", f"c-{u}-{v}", f"c+{v}"],
     [f"c-{u}+{v}", "c", f"c+{u}-{v}"],
     [f"c-{v}", f"c+{u}+{v}", f"c-{u}"]]
lines = {
    "diff u (main diag)": [g[0][0], g[1][1], g[2][2]],
    "diff v (anti diag)": [g[0][2], g[1][1], g[2][0]],
    "diff u+v (mid col)": [g[0][1], g[1][1], g[2][1]],
    "diff u-v (mid row)": [g[1][0], g[1][1], g[1][2]],
}
print("\nFour centre lines and their third-difference d:")
for name, L in lines.items():
    print(f"  {name}: {L}")
covered = set(c for L in lines.values() for c in L)
all9 = set(c for row in g for c in row)
print("distinct entries covered by the four APs:", covered)
print("all nine grid entries:", all9)
print("four APs cover all nine entries (centre counted once):", covered == all9)
print("extra entries beyond the four APs:", all9 - covered)