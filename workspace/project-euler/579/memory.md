# Working memory

## Problem

Exact question (verbatim from /workspace/problem.html, Euler 579):

> A **lattice cube** is a cube in which all vertices have integer coordinates. Let $C(n)$ be the number of different lattice cubes in which the coordinates of all vertices range between (and including) $0$ and $n$. Two cubes are hereby considered different if any of their vertices have different coordinates.
>
> For example, $C(1)=1$, $C(2)=9$, $C(4)=100$, $C(5)=229$, $C(10)=4469$ and $C(50)=8154671$.
>
> Different cubes may contain different numbers of lattice points.
>
> For example, the cube with the vertices $(0, 0, 0)$, $(3, 0, 0)$, $(0, 3, 0)$, $(0, 0, 3)$, $(0, 3, 3)$, $(3, 0, 3)$, $(3, 3, 0)$, $(3, 3, 3)$ contains $64$ lattice points ($56$ lattice points on the surface including the $8$ vertices and $8$ points within the cube).
>
> In contrast, the cube with the vertices $(0, 2, 2)$, $(1, 4, 4)$, $(2, 0, 3)$, $(2, 3, 0)$, $(3, 2, 5)$, $(3, 5, 2)$, $(4, 1, 1)$, $(5, 3, 3)$ contains only $40$ lattice points ($20$ points on the surface and $20$ points within the cube), although both cubes have the same side length $3$.
>
> Let $S(n)$ be the sum of the lattice points contained in the different lattice cubes in which the coordinates of all vertices range between (and including) $0$ and $n$.
>
> For example, $S(1)=8$, $S(2)=91$, $S(4)=1878$, $S(5)=5832$, $S(10)=387003$ and $S(50)=29948928129$.
>
> Find $S(5000) \bmod 10^9$.

Interpretation choices: a cube is identified with its set of 8 vertices (two cubes different iff some vertex differs); "range between (and including) 0 and n" applies to every coordinate of every vertex; "contained lattice points" counts integer points in the closed solid cube. Side length of the two example cubes is 3 in both cases (axis-aligned and tilted).

## Established results

None yet — extraction task only (see goal.md). Test oracle values recorded in goal.md Section 4: C(1)=1, C(2)=9, C(4)=100, C(5)=229, C(10)=4469, C(50)=8154671; S(1)=8, S(2)=91, S(4)=1878, S(5)=5832, S(10)=387003, S(50)=29948928129; cube A 64=56+8, cube B 40=20+20.

## Failed approaches

Record attempts that should not be repeated without a new reason.

## Open questions

Record the next unresolved steps.
