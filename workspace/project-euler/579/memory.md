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

- O(1)-per-frame power-sum summation: /workspace/solution_power.py replaces the
  per-frame t-loop with Faulhaber closed forms.  With X=n+1,
    T(t) = X^3 - X^2(A+B+C)t + X(AB+AC+BC)t^2 - (ABC)t^3
    pts(t) = ell^3 t^3 + ell*D t^2 + D t + 1
    g(t) = pts*T  (degree 6)
  C-contrib = sum_j p_j*P(j,tmax),  S-contrib = sum_k c_k*P(k,tmax), where
  P(k,n)=sum_{t=1}^n t^k via exact integer Faulhaber forms (P0..P6).  Cost per
  frame is O(1).  It imports the enumeration unchanged from frame_method.py (so
  identical), and only the summation differs.
  Validation (power_validate.txt): Faulhaber P(k,n) matched a literal loop for
  k=0..6, n=0..200; C/S matched oracle for n=1,2,4,5,10,50 (all OK); and at n=50
  the power-sum result is bit-for-bit identical (asserted) to the direct t-loop.
  n=50 O(1) summation wall time ~0.001s (enumeration, ~0.3s, excluded).

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

## Frame-based method VALIDATED (frame_method.py) — criterion 3/4 progress

The efficient method decomposes every cube into a **primitive frame** times an
integer scale t:
  * A primitive frame (u,v,w) has pairwise-orthogonal equal-norm integer edges,
    |u|^2=|v|^2=|w|^2=ell^2, with gcd of all 9 coordinates = 1.
  * A cube = frame scaled by t (t = gcd of the cube's 9 edge coords).
  * Coordinate spans of the t-scaled frame: t*A, t*B, t*C where
      A=|ux|+|vx|+|wx|, B=|uy|+|vy|+|wy|, C=|uz|+|vz|+|wz|.
  * Lattice-point count (Ionascu Thm 3.1, Ehrhart) of the t-dilated cube:
      pts(t) = ell^3 t^3 + ell*D t^2 + D*t + 1,
    with D = sum of the 3 edge-gcds of the primitive frame.
  * Box-fit corner count: T(t) = (n+1-tA)(n+1-tB)(n+1-tC) for 1<=t<=tmax,
    tmax = min(n//A, n//B, n//C).
  * C-contribution = sum_t T(t); S-contribution = sum_t pts(t)*T(t).

Verified by /workspace/frame_method.py against the oracle (all OK):
  n=1: C=1 S=8           (1 primitive)
  n=2: C=9 S=91          (1)
  n=4: C=100 S=1878      (5)
  n=5: C=229 S=5832      (11)
  n=10:C=4469 S=387003   (31)
  n=50:C=8154671 S=29948928129  (755)
Growth of distinct primitive-frame count:
  n=10:31, n=20:119, n=50:755, n=100:3053, n=200:12129.
Full run wall times: n=50 0.26s, n=100 1.70s, n=200 52.53s (enumeration cost
dominated by pairing vectors within norm groups, ~(2n+1)^3 vectors).

This structure is the key to efficiency: each primitive frame contributes a
polynomial (degree 3 in t for C, degree 6 for S) in t, and the t-sum can be
replaced by power-sum / Faulhaber identities — so the cost per frame is O(1)
after power sums. For n=5000 the enumeration must be primed by a canonical
parametrization (primary Hurwitz quaternions, Kiss-Kutas / Euler-Rodrigues),
NOT by the direct vector pairing used here (which gave n=200 in 52s and will
not reach n=5000). That quaternion enumeration is the next step.

## Failed approaches

(To be filled.)

## Open questions

- Efficient parametrization / enumeration of orthogonal equal-norm integer vector triples.
- Closed form for lattice point count in a lattice cube as function of u,v,w.
