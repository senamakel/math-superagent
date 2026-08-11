# Working memory

## Problem

Project Euler 579 "Lattice points in lattice cubes".

Every lattice cube with integer vertices: determined by integer corner P0 in Z^3 and three pairwise-orthogonal, equal-norm integer edge vectors u,v,w (|u|^2=|v|^2=|w|^2=m). Vertices: P0 + s1 u + s2 v + s3 w, si in {0,1}. C(n) = # distinct such cubes fully in [0,n]^3. S(n) = sum over those cubes of lattice points in the closed cube. Find S(5000) mod 10^9.

## Established results

All oracle examples reproduced by the brute-force oracle (exact integer
arithmetic, no floats):

| n | C(n) | S(n) | matches |
|---|------|------|---------|
| 1 | 1    | 8         | both OK |
| 2 | 9    | 91        | both OK |
| 4 | 100  | 1878      | both OK |
| 5 | 229  | 5832      | both OK |
| 10| 4469 | 387003    | both OK |

Extra ran beyond the required n<=5: n=3 C=36 S=496; n=6 C=473 S=15925.

- The lattice-point-count routine is validated on the statement's two worked
  cubes: cube A (side 3, axis-aligned) total 64 = 56 surface + 8 interior;
  cube B (side 3, oblique) total 40 = 20 surface + 20 interior.  Both OK via
  the independently-written /workspace/pointcount.py.

- Method: a cube is P0 + s1 u + s2 v + s3 w, s_i in {0,1}, with u,v,w pairwise
  orthogonal equal-norm integer vectors, |u|^2 = m a perfect square (m = k^2).
  The third edge from a frame is exactly w = (u x v) / k (integer division).
  A lattice point q is inside the closed cube iff 0 <= (q-P0).u <= m and same
  for v, w; it is on the surface iff any of those equals 0 or m.

- Independent cross-check: /workspace/research/verify_cross.py enumerates the
  cubes by a differently-derived parametrization (decompose u x v through its
  primitive direction, take w = (u x v)/k with k a square-divisor).  It agrees
  with brute.py on C and S for n = 1,2,4,5 (C: 1,9,100,229; S: 8,91,1878,5832).
  Together with the n=10 match this gives two independent routes to the small-n
  values, satisfying the verify-independently requirement at the oracle level.

## Failed approaches

- Initially derived w = (u x v) / m (dividing by the squared norm).  This is
  wrong: w must equal (u x v) / k where k^2 = m.  The assertion caught it.

## Open questions

- Efficient parametrization / enumeration of orthogonal equal-norm integer
  vector triples (the factorization structure of the frame count).
- Closed form for lattice point count in a lattice cube as function of u,v,w
  (needs a Pick-type / Ehrhart-style analysis).
- The brute force runs in time polynomial in n but with a large constant; it
  reaches n=10 comfortably but will not scale to n=5000.  Need the efficient
  method (criterion 4-6).

## Failed approaches

(To be filled.)

## Open questions

- Efficient parametrization / enumeration of orthogonal equal-norm integer vector triples.
- Closed form for lattice point count in a lattice cube as function of u,v,w.
