# Scratchpad (provisional)

## Problem restatement (PE 579)
A **lattice cube** is a cube whose 8 vertices are integer-coordinate points in Z^3.
C(n) = number of distinct lattice cubes with ALL vertex coordinates in [0,n].
Two cubes distinct iff any vertex differs.
S(n) = sum over those cubes of the number of lattice points (integer points) the cube contains
(8 vertices + interior + surface lattice points).
Find S(5000) mod 10^9.

Worked examples to reproduce (oracle):
C(1)=1, C(2)=9, C(4)=100, C(5)=229, C(10)=4469, C(50)=8154671
S(1)=8, S(2)=91, S(4)=1878, S(5)=5832, S(10)=387003, S(50)=29948928129
Example cubes, both side 3: axis-aligned => 64 lattice points; skewed set given => 40.

## Ideas
- A cube (up to translation) = orthogonal equal-length integer edge vectors (u,v,w) from a vertex,
  R=[u v w], R^T R = L^2 I. w = (u x v)/L requires L | (u x v).
- Translation-class shapes; overcount of ordered triples = 6 (only edge orderings from reference vertex 0).
- Translations fitting in [0,n]^3 for a shape with bbox extents e=(e1,e2,e3): t = prod (n-e_i+1) if e_i<=n.
- lattice point count in cube uses orthogonal slabs: q inside iff 0<=u·(q-o), v·(q-o), w·(q-o)<= L^2
  (exact rational check).
- Determine whether full frame = integer multiple of a "primitive" frame; quaternion correspondence;
  count frames efficiently without enumerating to n = 5000.

## Next steps
[ ] brute.py reproduces C,S small examples
[ ] theory: integer orthogonal frames enumeration + LP-in-cube formula
[ ] solution.py efficient, agree with brute on reachable n, then S(5000) mod 1e9
