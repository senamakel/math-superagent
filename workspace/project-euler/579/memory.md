# Working memory

## Problem

Project Euler 579 (statement at `/workspace/problem.html`):
- A **lattice cube** = cube in $\mathbb{R}^3$ with all 8 vertices having integer coordinates.
- $C(n)$ = number of distinct lattice cubes with all vertex coordinates in $\{0,1,\dots,n\}$; cubes equal iff vertex sets equal.
- $S(n)$ = sum over those cubes of the number of lattice points (integer-coordinate points, closed cube including boundary) contained in each cube.
- Task (NOT yet attempted): find $S(5000) \bmod 10^9$.

Interpretation choices (to revisit at solve time):
- Cubes identified by their vertex sets (unordered); a cube counted once even though any vertex can be associated to multiple positions.
- "Lattice points contained" = integer points in the closed cube (boundary included; statement's surface/interior split confirms boundary counts).
- $n = 5000$ target; modulus $m = 10^9$.

## Established results

None solved yet — task was extraction/restatement only (see `goal.md`).

**Test oracle (from statement, to be reproduced exactly by any future method):**
- $C(1)=1,\ C(2)=9,\ C(4)=100,\ C(5)=229,\ C(10)=4469,\ C(50)=8154671$
- Axis-aligned cube $[0,3]^3$ (vertices $(0,0,0),(3,0,0),(0,3,0),(0,0,3),(0,3,3),(3,0,3),(3,3,0),(3,3,3)$): 64 lattice points = 56 surface (incl. 8 vertices) + 8 interior; side length 3.
- Rotated cube with vertices $(0,2,2),(1,4,4),(2,0,3),(2,3,0),(3,2,5),(3,5,2),(4,1,1),(5,3,3)$: 40 lattice points = 20 surface + 20 interior; same side length 3.
- $S(1)=8,\ S(2)=91,\ S(4)=1878,\ S(5)=5832,\ S(10)=387003,\ S(50)=29948928129$
- Target: $S(5000) \bmod 10^9$.

Sourced fact: all values above are taken verbatim from the official PE 579 statement (downloaded as `/workspace/problem.html`); they are the problem's own examples, not independent verification.

## Failed approaches

None yet.

## Open questions

- How to count lattice cubes $C(n)$ without enumerating cubes (suggested theory directions for the future solve: representation of lattice cubes via edge vectors $(a,b,c)$ with $\|v\|^2 = \|w\|^2 = \|v\cdot w\|$ orthogonality conditions; integer-orthogonal triples; counting by direction class times translations, i.e. $C(n)$ as sum over primitive direction classes of counts within box $[0,n]^3$).
- How to count lattice points inside each cube class (Ehrhart-type counting / number of integer points in the closed cube; note the contrast 64 vs 40 for side length 3).
- Relationship between per-cube lattice point counts and $S(n)$ accumulation.