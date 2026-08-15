# Equalization counterexample of the projection approach — hand-verified

**Source being checked:** `research/approaches/projection-distance-equalization.md`
first-step (3) and `research/sources/regular-4-polytope-projection-quaternions.md`.

## Claim

24-cell difference vectors `(0,2,0,0)` [source squared length 4] and
`(0,-1,1,0)` [source squared length 2] both map, under projection rows
`a=(0,1,3,0)`, `b=(0,0,0,1)`, to `Q_pi = 4` (planar squared length 4, planar
length 2). Hence a rank-2 projection is NOT a homothety — it equalizes two
distinct source lengths to one planar length, creating genuinely new unit edges.

## Hand verification (exact, integer arithmetic, no floats)

Rank-2 form: `Q_pi(x) = (a·x)^2 + (b·x)^2`.

- `a·(0,2,0,0) = (0)(0)+(1)(2)+(3)(0)+(0)(0) = 2` → `2^2 = 4`.
  `b·(0,2,0,0) = (0)(0)+(0)(2)+(0)(0)+(1)(0) = 0` → `0`.
  `Q_pi = 4 + 0 = 4`. Source norm² = `0+4+0+0 = 4`.
- `a·(0,-1,1,0) = (1)(-1)+(3)(1) = -1+3 = 2` → `2^2 = 4`.
  `b·(0,-1,1,0) = 0` → `0`.
  `Q_pi = 4`. Source norm² = `0+1+1+0 = 2`.

Both give `Q_pi = 4` while source squared lengths differ (4 vs 2). ✓

The 24-cell vertex set = 24 permutations of `(±1,±1,0,0)`: there are `C(4,2)=6`
choices of the two nonzero coordinate positions × `2^2=4` sign combinations =
24 distinct vertices. ✓ The difference vectors are differences of actual
24-cell vertices: `(0,1,1,0)-(0,-1,1,0)=(0,2,0,0)` and
`(0,0,1,0)-(0,1,0,0)=(0,-1,1,0)`, all four endpoints in the 24-cell set. ✓

## Status

Hand-verified by exact integer arithmetic (this is a machine-verifiable claim
awaiting the executor). A program `code/verify_polytope_equalization.py` has
been written to reproduce it symbolically with sympy but NOT yet executed — do
not report it as machine-checked until `code/out/verify_polytope_equalization.captured.txt`
exists and shows "ALL CHECKS PASSED".

```claim
id: polytope-projection-equalization-counterexample
statement: >
  Under projection rows a=(0,1,3,0), b=(0,0,0,1) the rank-2 form
  Q_pi(x)=(a.x)^2+(b.x)^2 sends both (0,2,0,0) and (0,-1,1,0) to Q_pi=4 while
  their source squared lengths are 4 and 2, so a rank-2 projection equalizes
  distinct source lengths to one planar length and is not a homothety.
hypotheses: 24-cell vertex set in Z^4; two specific difference vectors; given
  projection rows.
holds-here: yes
status: asserted
  (hand-verified exactly by integer arithmetic in this note; the symbolic
  program code/verify_polytope_equalization.py is written but NOT yet run —
  do not treat as machine-checked until code/out/verify_polytope_equalization.captured.txt exists)
bearing: justifies the adopted projection-distance-equalization construction; if
  it fails to reproduce symbolically the line is dead at its first step.
anchor: code/verify_polytope_equalization.py / research/sources/regular-4-polytope-projection-quaternions.md
answers: projection-distance-equalization first-step (3)
```
