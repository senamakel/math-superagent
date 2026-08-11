# Goal

Solve Project Euler 579: "Lattice points in lattice cubes".

## Problem restatement (with symbols defined)

- A **lattice cube** is a cube with all 8 vertices at integer coordinates in Z^3.
- A cube is *within the box* if all 8 vertex coordinates lie in [0,n] (all coordinates integers between 0 and n inclusive).
- `C(n)` = number of **distinct** lattice cubes within the box. Two cubes differ if any of their vertices have different coordinates (so the same geometric cube found via different corner/ordering collapses to one).
- `S(n)` = sum, over all distinct lattice cubes within the box, of the number of lattice points contained in that cube (closed cube: interior + boundary, all included).

## Oracle (worked examples, from the statement)

C(1)=1, C(2)=9, C(4)=100, C(5)=229, C(10)=4469, C(50)=8154671.
S(1)=8, S(2)=91, S(4)=1878, S(5)=5832, S(10)=387003, S(50)=29948928129.
Find S(5000) mod 10^9.

## Worked point-count examples (for the point-in-cube logic)

Cube A, vertices (0,0,0),(3,0,0),(0,3,0),(0,0,3),(0,3,3),(3,0,3),(3,3,0),(3,3,3), side length 3: contains 64 lattice points = 56 on surface (incl. 8 vertices) + 8 interior.

Cube B, vertices (0,2,2),(1,4,4),(2,0,3),(2,3,0),(3,2,5),(3,5,2),(4,1,1),(5,3,3), also side length 3: contains 40 lattice points = 20 surface + 20 interior.

## Completion criteria

1. /workspace/brute.py runs and reproduces every oracle example it can reach (at minimum n<=5, ideally n=10). Output saved to /workspace/brute_output.txt.
2. Point-in-cube logic validated on cubes A and B via /workspace/pointcount.py.
3. Governing theory identified and recorded in /workspace/memory.md with source URLs.
4. Efficient method derived in /workspace/solution.md (complexity not growing with the answer / true for large n).
5. /workspace/solution.py implemented with exact arithmetic, agreeing with brute on all reachable cases.
6. Final answer S(5000) mod 10^9 computed and verified by a second independent route.
