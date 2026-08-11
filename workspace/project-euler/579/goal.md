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

## Completion criteria

1. [DONE] /workspace/brute.py reproduces every oracle example it can reach.
2. [DONE] Point-in-cube logic validated on cubes A and B.
3. [DONE] Governing theory identified and recorded (Ehrhart / Ionascu Thm 3.1; primitive-frame parametrization).
4. [IN PROGRESS] /workspace/frame_method.py validates the efficient frame-based method (primitive frames + Ehrhart point formula) against the oracle for small/medium n (1,2,4,5,10,50).
5. [ ] Full efficient method derived in solution.md (complexity not growing with the answer).
6. [ ] Final answer S(5000) mod 10^9 computed and verified by a second independent route.
