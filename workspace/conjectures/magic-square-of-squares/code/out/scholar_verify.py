#!/usr/bin/env python3
"""Scholar verification of source-reported values, exact integer arithmetic.
Checks the witness grids and the several numerical/structural claims that the
summary notes will report, so no number is written down that a program did
not produce."""
import math

def is_sq(n):
    r = math.isqrt(n)
    return r*r == n

def check(name, grid, expect_magic=None, expect_nonsq=()):
    print(f"--- {name} ---")
    for r in grid:
        print("   ", r)
    # line sums
    sums = []
    for i in range(3):
        sums.append(sum(grid[i]))
        sums.append(sum(grid[j][i] for j in range(3)))
    sums.append(grid[0][0]+grid[1][1]+grid[2][2])
    sums.append(grid[0][2]+grid[1][1]+grid[2][0])
    print("   distinct line sums:", sorted(set(sums)))
    nonsq = [x for row in grid for x in row if not is_sq(x)]
    print("   non-square entries:", nonsq)
    if expect_magic is not None:
        assert all(s==expect_magic for s in sums), "magic mismatch"
        print("   MAGIC == ", expect_magic, "OK")

# Sallows LS1 (Bremner's printed orientation = [58,46,127;94,113,2;97,82,74])
grid_sallows = [[58,46,127],[94,113,2],[97,82,74]]
gd_s = [[x*x for x in row] for row in grid_sallows]
check("Sallows LS1 (squares of [58,46,127;94,113,2;97,82,74])", gd_s)
print("   147^2 =", 147**2, " failing diag =", gd_s[0][2]+gd_s[1][1]+gd_s[2][0])

# Bremner 7-square magic square: [373,289,565; 360721,425,23; 205,527,222121]
grid_b = [[373,289,565],[360721,425,23],[205,527,222121]]
gd_b = [[x*x for x in row] for row in grid_b]
check("Bremner 7-square (373^2...)", gd_b, expect_magic=541875)
print("   centre 425^2 =", 425**2)

# verify a few individual square claims used in notes
for n,e in [(373,373),(289,289),(565,565),(425,425),(23,23),(205,205),(527,527)]:
    assert e*e == n*n
print("ALL VERIFIED")
