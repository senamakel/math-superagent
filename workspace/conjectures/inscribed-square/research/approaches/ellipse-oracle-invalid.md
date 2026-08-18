# Dead end: the first ellipse-oracle check is invalid

**Status: closed — do not use `check_oracle.py`'s ellipse numbers.**

## What was wrong

1. `code/square_peg/check_oracle.py` begins with `sys.path.insert(0, "/workspace/code")`,
   which the workspace rules forbid (modules are importable by name because
   `/workspace/code` is on `PYTHONPATH`).
2. More seriously, `rat_ellipse_polygon(a, b, n)` builds vertices using the
   tangent half-angle substitution with `t = 2k/n`, i.e. angle
   `2·arctan(2k/n)`, not `2πk/n`. So the polygon vertices are **not** evenly
   spaced on the circle and do **not** approximate the intended ellipse with
   the claimed Hausdorff bound. The whole `report_ellipse`/`report_circle`
   section is therefore invalid and its numbers must not be cited.

## What stands instead

The **valid** exact oracle is `code/brute.py` (executed, output reproduced in
this run): it checks every 4-vertex subset in exact rational arithmetic and
found

- unit square → exactly 1 square `[(0,1,2,3)]`
- 2×1 rectangle → 0 squares
- diamond (rotated square) → exactly 1 square `[(0,1,2,3)]`

matching the hand-checked exact distance sets `{1,1,1,1,2,2}`, `{1,1,4,4,5,5}`,
`{2,2,2,2,4,4}`.

## Consequence

The CDM 2022 Prop. 26 anchor (non-circular ellipse inscribes exactly one
square) is **not** verified computationally in this run. A correct rational
ellipse approximation would need evenly spaced rational points on the
Pythagorean circle (rational parametrization of `x²+y²=1` with the correct
angle distribution), which is a separate piece of work.

## What would settle it

A corrected rational parametrization of the circle with the proper even
spacing, then `find_squares` on the scaled polygon converging to the single
ellipse square, with the exact Hausdorff bound stated.
