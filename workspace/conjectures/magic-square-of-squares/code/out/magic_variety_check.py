#!/usr/bin/env python3
"""magic_variety_check.py — the 3x3 magic-square variety as a linear space.

Exact integer + sympy verification of the linear-variety structure of the
3x3 magic square variety X ⊂ P⁸ (coordinates = the nine entries; the eight
line sums — rows, columns, both diagonals — all equal).  NO square
conditions: this is the variety cut out by the line-sum equalities alone.

Facts established (all exact, all assert-guarded; exit code 0 iff every
assert passes):

  (1) The 8x9 line-sum INCIDENCE matrix (rows = the eight line-sum forms)
      has rank 7 over Q; its single left-null relation is the trace
      identity R0+R1+R2 = C0+C1+C2 (sum of rows = sum of columns).
  (2) The natural 7x9 DIFFERENCE system (line sums L_1..L_7 minus the
      reference sum L_0 = first row sum; seven rows) has rank 6, NOT 7:
      the trace identity reappears as the single row relation
         (R1-R0) + (R2-R0) - (C0-R0) - (C1-R0) - (C2-R0) = 0,
      i.e. R0 + R1 + R2 = C0 + C1 + C2.
      Rank 7 would give a 2-dimensional solution space (a P¹ in P⁸,
      contradicting the 3-parameter (c,u,v) description); the true rank 6
      gives dimension 9-6 = 3.
  (3) Hence X̂ = {all 8 line sums equal} ⊂ A⁹ is a 3-dimensional LINEAR
      subspace (it contains 0), so X = P(X̂) ≅ P² ⊂ P⁸ is a projective
      plane — a surface (dimension 2 in P⁸), smooth, cut by 6 independent
      linear equations (the 7th is a consequence).
  (4) Explicit basis of X̂: the constant grid C = grid_from_params(1,0,0)
      (all entries 1), the u-grid U = grid_from_params(0,1,0), the v-grid
      V = grid_from_params(0,0,1).  Verified: C,U,V ∈ ker(M), independent,
      and they span ker(M) (rank of [C|U|V] is 3; membership of the
      returned nullspace basis in span{C,U,V} and conversely, by exact
      rref pivot checks).
  (5) The parametrisation (c,u,v) ↦ grid_from_params(c,u,v) is a bijection
      A³ → X̂: all eight line sums of the symbolic grid are equal
      identically, and the inverse (centre, a00-centre, a02-centre)
      recovers (c,u,v) identically.  These are the 3 free parameters.
  (6) Lines: X is a linearly embedded P², so X contains a 2-parameter
      family of lines — every 2-dimensional subspace of the 3-dim cone
      projects to a line of X (the Grassmannian G(1,2) ≅ P²), and every
      two distinct points of X lie on a unique contained line.  A concrete
      symbolic witness: the line {s·C + t·U} satisfies all seven equations
      for all (s,t) ∈ A².  THE CLAIM "X CONTAINS NO LINES" IS FALSE FOR
      THIS LINEAR VARIETY.  The no-lines / 256-singular-points claims of
      the Michaud-Rodgers talk belong to the QUADRIC-CUT square variety
      (coordinates r_ij, equations Σ_line r² equal — six quadrics), a
      DIFFERENT object; the linear part is exactly the free (c,u,v) freedom.
  (7) Quantification: within X ≅ P², the MSS problem asks for all nine
      entries to be rational squares — nine quadratic conditions on the
      three parameters (c,u,v).  Best known rational point of X with square
      entries: 7 of 9 (Bremner's magic square, verified here to lie in X̂);
      Sallows LS1 has 9 square entries but is NOT a point of X (7 of its 8
      line sums agree only), so it does not contradict the 7-of-9 bound
      inside X.  The 8-square and 9-square questions inside X are open.

Correctness: every number below comes from exact integer/Fraction/symbolic
arithmetic (sympy QQ / symbols); the parametrisation identity is checked
twice (symbolic line sums and symbolic recovery); C,U,V ∈ ker(M) and the
span equality are checked by exact Gaussian elimination/rref; the witness
grids come from lib/mss.py (the run's verified construction of the two
near-misses).
"""

from sympy import Matrix, symbols, simplify, zeros

# ---------------------------------------------------------------------------
# The line-sum systems
# ---------------------------------------------------------------------------


def line_sum_forms():
    """The eight line-sum forms as 9-vectors of Integers: rows 0,1,2;
    columns 0,1,2; principal diagonal; non-principal diagonal."""
    lines = (
        (0, 1, 2),   # row 0
        (3, 4, 5),   # row 1
        (6, 7, 8),   # row 2
        (0, 3, 6),   # col 0
        (1, 4, 7),   # col 1
        (2, 5, 8),   # col 2
        (0, 4, 8),   # principal diagonal
        (2, 4, 6),   # non-principal diagonal
    )
    rows = []
    for line in lines:
        v = [0] * 9
        for i in line:
            v[i] = 1
        rows.append(v)
    return rows, lines


LINE_FORMS, LINE_CELLS = line_sum_forms()
I8 = Matrix(LINE_FORMS)                       # 8x9 incidence matrix
M7 = Matrix([[LINE_FORMS[i][j] - LINE_FORMS[0][j]
              for j in range(9)] for i in range(1, 8)])   # 7x9 difference system
NINE = list(range(9))

c, u, v = symbols("c u v")
s, t = symbols("s t")
A_, B_, G_ = symbols("a_al b_be g_ga")        # generic coordinates of the cone


def normalized(v):
    """Integer coefficients of v scaled so the first nonzero entry is 1."""
    entries = [int(x) for x in v]
    first = next(x for x in entries if x != 0)
    return tuple(x // first for x in entries)


def proportional(a, b):
    """Exact: two integer tuples (same length, not both zero) are
    Q-scalar multiples.  Handles zero entries: zeros must match, and all
    nonzero cross-ratios a[i]/b[i] must be equal."""
    if len(a) != len(b) or not any(a) or not any(b):
        return False
    pair = None
    for ai, bi in zip(a, b):
        if ai == 0 or bi == 0:
            if ai != bi:
                return False
            continue
        if pair is None:
            pair = (ai, bi)
        else:
            if ai * pair[1] != bi * pair[0]:
                return False
    return pair is not None


def in_span(cols, vec):
    """Exact: is vec in the Q-span of cols?  rref pivot check."""
    aug = Matrix.hstack(*cols, vec)
    _, pivots = aug.rref()
    return len(cols) not in pivots


def section(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


# ---------------------------------------------------------------------------
section("1. The two linear systems and their ranks (exact, over Q)")
print("8x9 line-sum incidence matrix I8 (rows: R0,R1,R2,C0,C1,C2,D0,D1):")
print(I8)
print("7x9 difference system M7 (rows: L_i - L_0 for i = 1..7):")
print(M7)

rI = I8.rank()
rM = M7.rank()
print("\nrank(I8) =", rI)
print("rank(M7) =", rM)
assert rI == 7, "expected incidence rank 7"
assert rM == 6, "expected difference-system rank 6 (one trace relation)"

# ---------------------------------------------------------------------------
section("2. The relations (left nullspaces)")
relI = I8.T.nullspace()
assert len(relI) == 1
relM = M7.T.nullspace()
assert len(relM) == 1
nI = normalized(relI[0])
nM = normalized(relM[0])
print("relation among the 8 line forms (R0 R1 R2 C0 C1 C2 D0 D1):")
print("   ", nI)
print("   -> the trace identity: R0 + R1 + R2 = C0 + C1 + C2")
assert proportional(nI, (1, 1, 1, -1, -1, -1, 0, 0)), nI
print("relation among the 7 difference rows (R1-R0 R2-R0 C1-C0 C2-C0 D0-R0 D1-R0 C0-R0):")
print("   ", nM)
print("   rows are (R1-R0, R2-R0, C0-R0, C1-R0, C2-R0, D0-R0, D1-R0);")
print("   -> (R1-R0) + (R2-R0) - (C0-R0) - (C1-R0) - (C2-R0) = 0")
print("   i.e. R0 + R1 + R2 = C0 + C1 + C2  (the trace identity again)")
assert proportional(nM, (1, 1, -1, -1, -1, 0, 0)), nM
print("So the '7 line-sum equations' are NOT independent: rank 6, and")
print("the variety is cut by 6 independent linear equations (plus the")
print("consequence that re-states the trace identity).")

# ---------------------------------------------------------------------------
section("3. The kernel: a 3-dimensional linear subspace of A^9  =>  P^2 in P^8")
kerM = M7.nullspace()
print("nullspace basis of M7 (dim =", len(kerM), "):")
for i, w in enumerate(kerM):
    print(f"   w{i} =", list(w))
assert len(kerM) == 3, "kernel of the difference system must be 3-dimensional"

Ccol = Matrix([1] * 9)                       # constant grid,  all entries 1
Ucol = Matrix([1, -1, 0, -1, 0, 1, 0, 1, -1])   # u-grid
Vcol = Matrix([0, -1, 1, 1, 0, -1, -1, 1, 0])   # v-grid

print("\nexplicit generators (from the (c,u,v) parametrisation):")
for name, gd in (("C (constant grid)", Ccol), ("U (u-grid)", Ucol), ("V (v-grid)", Vcol)):
    print(f"   {name}:", list(gd))
    assert M7 * gd == zeros(7, 1), name + " must satisfy all 7 equations"

print("\nindependence of C, U, V: rank([C | U | V]) =",
      Matrix.hstack(Ccol, Ucol, Vcol).rank())
assert Matrix.hstack(Ccol, Ucol, Vcol).rank() == 3

print("span equality (kernel basis <-> {C,U,V}) by exact rref checks:")
for i, w in enumerate(kerM):
    ok = in_span([Ucol, Vcol, Ccol], w)
    print(f"   w{i} in span{{C,U,V}}: {ok}")
    assert ok
for name, gd in (("C", Ccol), ("U", Ucol), ("V", Vcol)):
    ok = in_span(kerM, gd)
    print(f"   {name} in span(kerM): {ok}")
    assert ok
print("   -> span(C,U,V) = ker(M7), a 3-dimensional linear space")

dim_aff = 9 - rM
dim_proj = dim_aff - 1
print(f"\ndimension of solution space in A^9: 9 - {rM} = {dim_aff}")
print(f"hence X = P(ker M) is a P^{dim_proj} ⊂ P^8 — a surface (dim 2), smooth.")
print("A rank-7 system WOULD have given a 2-dim affine kernel (a P^1), which")
print("contradicts the 3-parameter (c,u,v) description; the true rank 6 is")
print("forced by the trace relation and gives exactly the P^2 the")
print("parametrisation describes.")

# ---------------------------------------------------------------------------
section("4. The parametrisation (c,u,v) |-> grid is a bijection A^3 -> X-hat")
g = Matrix([c + u, c - u - v, c + v,
            c - u + v, c, c + u - v,
            c - v, c + u + v, c - u])
sums = [sum(g[i] for i in line) for line in LINE_CELLS]
ok_sums = all(simplify(sums[i] - sums[0]) == 0 for i in range(1, 8))
print("all eight line sums of the symbolic grid equal:", ok_sums)
assert ok_sums

rec = (g[4], g[0] - g[4], g[2] - g[4])       # (centre, a00-centre, a02-centre)
print("recovery: (centre, a00-centre, a02-centre) = (c, u, v):",
      all(simplify(rec[i] - (c, u, v)[i]) == 0 for i in range(3)))
assert simplify(rec[0] - c) == 0 and simplify(rec[1] - u) == 0 and simplify(rec[2] - v) == 0

g2 = Matrix([rec[0] + rec[1], rec[0] - rec[1] - rec[2], rec[0] + rec[2],
             rec[0] - rec[1] + rec[2], rec[0], rec[0] + rec[1] - rec[2],
             rec[0] - rec[2], rec[0] + rec[1] + rec[2], rec[0] - rec[1]])
ident = all(simplify(g[i] - g2[i]) == 0 for i in NINE)
print("rebuilding the grid from the recovered parameters is the identity:", ident)
assert ident
print("injectivity: (c,u,v) are read off the three pinned entries (centre,")
print("top-left, top-right), so two grids agree  =>  equal parameters.")
print("-> EVERY magic grid (all 8 line sums equal) is uniquely in the image.")

# Every point of the cone is a solution, generically:
Pgen = A_ * Ccol + B_ * Ucol + G_ * Vcol
ok_gen = (M7 * Pgen).applyfunc(simplify) == zeros(7, 1)
print("generic cone point a*C + b*U + g*V satisfies all 7 equations:", ok_gen)
assert ok_gen

# ---------------------------------------------------------------------------
section('5. Lines: X = P^2 contains a 2-parameter family of lines')
print("X is the projectivisation of the 3-dim cone; every 2-dimensional")
print("subspace of the cone is a line of X.  Lines of a P^2 form the")
print("Grassmannian G(1,2) ≅ P^2: a 2-parameter family, and any two distinct")
print("points of X span a unique contained line.")

line = s * Ccol + t * Ucol                     # explicit line through [C], [U]
all_zero = (M7 * line).applyfunc(simplify) == zeros(7, 1)
print("explicit witness line {s*C + t*U}: M7 * (s*C + t*U) == 0 for all s,t:",
      all_zero)
assert all_zero
print("Reason it is exact: L_i(P + t Q) = L_i(P) + t L_i(Q) for linear forms,")
print("so P + tQ ∈ X for all t iff P, Q ∈ X — and every P, Q ∈ X work here.")

print("\n*** THE CLAIM 'X CONTAINS NO LINES' IS FALSE FOR THIS LINEAR VARIETY. ***")
print("The linear space X ≅ P² is saturated with lines (a P²'s worth).")
print("The no-lines / 256-singular-points claims of the Michaud-Rodgers talk")
print("must refer to the QUADRIC-CUT square variety (entries' values r_ij with")
print("Σ_line r² equal, six quadrics) — a different object.  The linear part")
print("contributes no obstruction: it is exactly the free (c,u,v) freedom.")

# ---------------------------------------------------------------------------
section("6. What the square conditions become inside the P^2")
from lib.mss import bremner_magic_grid, sallows_ls1_grid, entries_of, line_sums

brem = Matrix(entries_of(bremner_magic_grid()))
sall = Matrix(entries_of(sallows_ls1_grid()))
inX_b = (M7 * brem == zeros(7, 1))
inX_s = (M7 * sall == zeros(7, 1))
print("Bremner 7-square witness is a point of X (all 8 sums equal):", inX_b)
assert inX_b
print("   its 8 line sums:", [int(x) for x in line_sums(bremner_magic_grid())])
print("   square entries: 7 of 9  (the two non-squares are 360721 and 222121)")
print("Sallows LS1 is NOT a point of X (only 7 of 8 sums agree):", not inX_s)
assert not inX_s
print("   its 8 line sums:", [int(x) for x in line_sums(sallows_ls1_grid())])
print("   square entries: 9 of 9 — a 9-square grid OUTSIDE X, so it does not")
print("   contradict the best-in-X count.")
print("\nInside X ≅ P² the MSS problem is: all nine entries")
print("   (c+u, c-u-v, c+v, c-u+v, c, c+u-v, c-v, c+u+v, c-u)")
print("simultaneously rational squares — NINE quadratic conditions on the")
print("THREE parameters (c,u,v).  Best known point of X: 7 of 9 squares")
print("(Bremner).  8-square and 9-square points of X are open.")

print("\n" + "=" * 74)
print("ALL CHECKS PASSED — linear magic variety is P^2 ⊂ P^8, rank 7")
print("(incidence) / rank 6 (differences), kernel dim 3, generators")
print("(C, U, V) = (constant, u, v) grids, no-line claim refuted for X.")
print("=" * 74)