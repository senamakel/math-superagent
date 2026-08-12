#!/usr/bin/env python3
"""code/lib/mss.py — exact-integer core for the 3x3 magic square of squares.

One subject, one module: everything a second program would otherwise retype
for the (centre, u, v) parametrisation of problem.md — the grid map, the
verifier, the line diagnostics, the magic-graph incidence algebra, and the
(c, u, v) extraction.  No floats anywhere; square checks are math.isqrt.

Canonical orientation (problem.md, Bremner 1999 §1 via the map below):

    c + u      c - u - v    c + v
    c - u + v  c            c + u - v
    c - v      c + u + v    c - u

Bremner's (2) is (a-b, a+b+c, a-c; a+b-c, a, a-b+c; a+c, a-b-c, a+b)
with (c, u, v) = (a, b, c):  a-b        = c+u        [yes: a-b=c+u]
                             a+b+c = c-u-v  -> b = -u-v?  no: a+b+c = c - u - v
                             and a-b+c = c+u-v -> b-c = u-v.  Both hold with
                             b = -u-v, b-c = u-v -> c = -2v, a-b-c = c+v ->
                             a + u + v - c = c + v -> a - c = 0 -> a = c.
                             So a=c1(left)=c, b=c1mid=-u-v, c1... = -2v etc.
This is only documentation; the numerical facts are what the tests check.

The two historical near-misses reproduced by construction here:

  Sallows LS1 (Bremner 1999, (1); Sallows, "The Lost Theorem", 1997):
      [[127**2, 46**2, 58**2],
       [2**2,   113**2, 94**2],
       [74**2,  82**2, 97**2]]
   7 of 8 line sums equal 147**2 = 21609; fails at the non-principal
   diagonal (38307 = 147**2 + 16698).

  Bremner's magic square (Bremner 1999, p. 290):
      [[373**2, 289**2, 565**2],
       [360721, 425**2, 23**2],
       [205**2, 527**2, 222121]]
   all eight line sums = 541875; exactly 7 square entries; the two
   non-squares are 360721 and 222121 (distinct, positive).
"""

from math import isqrt

# ---------------------------------------------------------------------------
# Ground truth
# ---------------------------------------------------------------------------


def is_perfect_square(x):
    """Exact: is x a perfect square?  Rejects non-int (floats, bools)."""
    if type(x) is not int:
        return False
    if x < 0:
        return False
    r = isqrt(x)
    return r * r == x


def sqrt_or_none(x):
    """int square root of x if x is a perfect square, else None.  Exact."""
    if type(x) is not int or x < 0:
        return None
    r = isqrt(x)
    return r if r * r == x else None


def grid_from_params(c, u, v):
    """The parametrised grid of problem.md as a list of three rows.  Entries
    need not be squares and need not be positive."""
    return [
        [c + u,     c - u - v, c + v],
        [c - u + v, c,         c + u - v],
        [c - v,     c + u + v, c - u],
    ]


def params_from_grid(grid):
    """The completeness map: (centre, a00-centre, a02-centre).  Exact and
    total over 3x3 grids of ints; for any grid this recovers parameters
    whose grid_from_params is the input iff the input is magic."""
    return grid[1][1], grid[0][0] - grid[1][1], grid[0][2] - grid[1][1]


def lines_of(grid):
    """The eight lines: three rows, three columns, both main diagonals.
    Ordered: rows, columns, principal diagonal (top-left to bottom-right),
    non-principal diagonal (top-right to bottom-left)."""
    return [
        grid[0], grid[1], grid[2],
        [grid[0][0], grid[1][0], grid[2][0]],
        [grid[0][1], grid[1][1], grid[2][1]],
        [grid[0][2], grid[1][2], grid[2][2]],
        [grid[0][0], grid[1][1], grid[2][2]],
        [grid[0][2], grid[1][1], grid[2][0]],
    ]


LINE_NAMES = ("row 1", "row 2", "row 3",
              "col 1", "col 2", "col 3",
              "principal diagonal", "non-principal diagonal")


def line_sums(grid):
    """Tuple of the eight line sums, in lines_of order."""
    return tuple(sum(line) for line in lines_of(grid))


def magic_sum(grid):
    """The common line sum if all eight lines agree, else None."""
    sums = line_sums(grid)
    return sums[0] if all(s == sums[0] for s in sums) else None


def entries_of(grid):
    """The nine entries, row-major."""
    return [grid[r][c] for r in range(3) for c in range(3)]


def failure_of(grid, require_distinct=True):
    """First condition violated, or None if the grid is a magic square of
    squares.  Diagnosis order: shape / non-integer / not-a-square /
    not-positive / not-distinct / not-magic."""
    if len(grid) != 3 or any(len(row) != 3 for row in grid):
        return "shape"
    entries = entries_of(grid)
    for x in entries:
        if type(x) is not int:
            return "non-integer"
    for x in entries:
        if not is_perfect_square(x):
            return "not-a-square"
    for x in entries:
        if x <= 0:
            return "not-positive"
    if require_distinct and len(set(entries)) != 9:
        return "not-distinct"
    if magic_sum(grid) is None:
        return "not-magic"
    return None


def is_magic_square_of_squares(grid, require_distinct=True):
    """THE decision oracle: nine distinct positive integer squares in all
    rows, columns and both main diagonals summing to one constant.  The
    open question is exactly: does any input return True?"""
    return failure_of(grid, require_distinct) is None


def count_squares(grid):
    """Number of perfect-square entries, by exact isqrt."""
    return sum(1 for row in grid for x in row if is_perfect_square(x))


# ---------------------------------------------------------------------------
# Magic-graph incidence algebra (over Q)
# ---------------------------------------------------------------------------


def magic_incidence_matrix():
    """8x9 exact-rational incidence matrix, sparse rows: row i = 1 on the
    cells of line i (lines_of order), 0 elsewhere.  Returned as a matrix of
    Fractions so rank works over Q."""
    from fractions import Fraction

    grid = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]  # cell indices, row-major
    rows = []
    for line in lines_of(grid):
        row = [Fraction(0)] * 9
        for cell in line:
            row[cell] = Fraction(1)
        rows.append(row)
    return rows


def rank_fraction_matrix(mat):
    """Rank of a matrix over Q by exact Gaussian elimination (row echelon).
    Entries must be Fractions; used with at most 8x9 matrices here."""
    from fractions import Fraction

    m = [[Fraction(x) for x in row] for row in mat]
    nrows, ncols = len(m), len(m[0]) if m else 0
    rank = 0
    pivot_col = 0
    while pivot_col < ncols and rank < nrows:
        pivot = None
        for r in range(rank, nrows):
            if m[r][pivot_col] != 0:
                pivot = r
                break
        if pivot is None:
            pivot_col += 1
            continue
        m[rank], m[pivot] = m[pivot], m[rank]
        pv = m[rank][pivot_col]
        for r in range(rank + 1, nrows):
            if m[r][pivot_col] != 0:
                factor = m[r][pivot_col] / pv
                for c in range(pivot_col, ncols):
                    m[r][c] -= factor * m[rank][c]
        rank += 1
        pivot_col += 1
    return rank


def nullspace_fraction_matrix(mat):
    """Exact basis of the right nullspace of an m x n Fraction matrix, as a
    list of n-vectors over Q, by RREF.  Returns [] if the kernel is zero."""
    from fractions import Fraction

    if not mat:
        return []
    ncols = len(mat[0])
    m = [[Fraction(x) for x in row] for row in mat]
    nrows = len(m)
    pivot_cols = []
    rank = 0
    r = 0
    for c in range(ncols):
        pivot = None
        for rr in range(r, nrows):
            if m[rr][c] != 0:
                pivot = rr
                break
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        pv = m[r][c]
        for cc in range(c, ncols):
            m[r][cc] /= pv
        for rr in range(nrows):
            if rr != r and m[rr][c] != 0:
                factor = m[rr][c]
                for cc in range(c, ncols):
                    m[rr][cc] -= factor * m[r][cc]
        pivot_cols.append(c)
        rank += 1
        r += 1
        if rank == nrows:
            break
    free_cols = [c for c in range(ncols) if c not in pivot_cols]
    basis = []
    for f in free_cols:
        vec = [Fraction(0)] * ncols
        vec[f] = Fraction(1)
        for i, pc in enumerate(pivot_cols):
            vec[pc] = -m[i][f]
        basis.append(vec)
    return basis


def magic_params_basis():
    """The (c, u, v) basis of the space of magic assignments.

    Returns (kernel_basis, witness): kernel_basis is a list of two exact
    Fraction vectors of length 9 spanning {assignments with all 8 line
    sums 0}; witness is one non-zero magic assignment with all 8 line sums
    equal (grid_from_params(1, 3, -5) flattened).

    Facts established by exact computation in
    code/check_near_misses.py (and re-derived with sympy in the scratch
    probe): the 8x9 line-incidence matrix over Q has rank 7, so the
    zero-sum kernel has dimension 2, spanned exactly by the u-grid and
    the v-grid.  The vectors are each another's reflection of the same
    two-parameter family, and there is one Q-relation among the eight
    line equations, L1+L2+L3 = L4+L5+L6 (rows vs columns; the diagonals
    are not involved).  Consequently the AFFINE space of magic
    assignments (all eight line sums equal, no zero constraint) has
    dimension 9 - rank(L2-L1,...,L8-L1) = 9 - 6 = 3, spanned by the
    constant grid, the u-grid and the v-grid — matching the (c, u, v)
    parametrisation.  NOTE: the wording "the space of magic assignments
    has dimension 4" (task brief) is not what the incidence algebra gives;
    the dimension over the line-sum equations is 3.  The user-facing
    parametrisation itself is untouched: every 3x3 magic grid is exactly
    grid_from_params(centre, a00-centre, a02-centre), verified in both
    directions by the completeness test."""
    one = grid_from_params(1, 0, 0)   # all entries equal to 1
    u_g = grid_from_params(0, 1, 0)   # (1,-1,0; 1,0,1; 0,1,-1) pattern
    v_g = grid_from_params(0, 0, 1)   # (0,-1,1; 1,0,-1; -1,1,0) pattern
    kernel = nullspace_fraction_matrix(magic_incidence_matrix())
    witness = entries_of(grid_from_params(1, 3, -5))
    return kernel, witness


# ---------------------------------------------------------------------------
# Corner/AP diagnostics and the (c, u, v) algebra of square conditions
# ---------------------------------------------------------------------------


def left_square_root(c, v):
    """sqrt(c - v) if c - v is a perfect square else None.  Exact."""
    return sqrt_or_none(c - v)


def two_square_splits(c):
    """All Pythagorean split pairs (x, y) with x >= y > 0 and
    x^2 + y^2 = c, i.e. every way the centre c = 425^2 splits as a sum of
    two positive squares.  Exact isqrt arithmetic."""
    if type(c) is not int or c <= 0:
        return []
    out = []
    for x in range(1, isqrt(c // 2) + 1):
        y2 = c - x * x
        y = sqrt_or_none(y2)
        if y is not None and y >= x:
            out.append((y, x))  # y >= x, so 2xy and x^2-y^2 are positive
    return out


# ---------------------------------------------------------------------------
# The two known near-misses, constructed directly from the sources
# ---------------------------------------------------------------------------


def sallows_ls1_grid():
    """Sallows LS1 as printed in Bremner 1999 (1): rows
    [58^2, 46^2, 127^2; 94^2, 113^2, 2^2; 97^2, 82^2, 74^2].
    7 of 8 line sums equal 147^2; the non-principal diagonal fails."""
    return [[58 ** 2, 46 ** 2, 127 ** 2],
            [94 ** 2, 113 ** 2, 2 ** 2],
            [97 ** 2, 82 ** 2, 74 ** 2]]


def bremner_magic_grid():
    """Bremner 1999 p. 290: rows
    [373^2, 289^2, 565^2; 360721, 425^2, 23^2; 205^2, 527^2, 222121].
    All eight line sums = 541875; exactly 7 square entries."""
    return [[373 ** 2, 289 ** 2, 565 ** 2],
            [360721, 425 ** 2, 23 ** 2],
            [205 ** 2, 527 ** 2, 222121]]