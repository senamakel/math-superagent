# Goal

## 1. Exact problem statement (verbatim)

> A **lattice cube** is a cube in which all vertices have integer coordinates. Let $C(n)$ be the number of different lattice cubes in which the coordinates of all vertices range between (and including) $0$ and $n$. Two cubes are hereby considered different if any of their vertices have different coordinates.
>
> For example, $C(1)=1$, $C(2)=9$, $C(4)=100$, $C(5)=229$, $C(10)=4469$ and $C(50)=8154671$.
>
> Different cubes may contain different numbers of lattice points.
>
> For example, the cube with the vertices
> $(0, 0, 0)$, $(3, 0, 0)$, $(0, 3, 0)$, $(0, 0, 3)$, $(0, 3, 3)$, $(3, 0, 3)$, $(3, 3, 0)$, $(3, 3, 3)$ contains $64$ lattice points ($56$ lattice points on the surface including the $8$ vertices and $8$ points within the cube).
>
> In contrast, the cube with the vertices
> $(0, 2, 2)$, $(1, 4, 4)$, $(2, 0, 3)$, $(2, 3, 0)$, $(3, 2, 5)$, $(3, 5, 2)$, $(4, 1, 1)$, $(5, 3, 3)$ contains only $40$ lattice points ($20$ points on the surface and $20$ points within the cube), although both cubes have the same side length $3$.
>
> Let $S(n)$ be the sum of the lattice points contained in the different lattice cubes in which the coordinates of all vertices range between (and including) $0$ and $n$.
>
> For example, $S(1)=8$, $S(2)=91$, $S(4)=1878$, $S(5)=5832$, $S(10)=387003$ and $S(50)=29948928129$.
>
> Find $S(5000) \bmod 10^9$.

## 2. Precise restatement and notation

- **Space.** We work in 3-dimensional Euclidean space $\mathbb{R}^3$ with the standard integer lattice $\mathbb{Z}^3 \subset \mathbb{R}^3$. A point with integer coordinates is a **lattice point**.
- **Lattice cube.** A (solid) cube whose 8 vertices all have integer coordinates. No restriction on orientation or side length beyond vertex integrality.
- **$n$.** A non-negative integer bounding box parameter. The box $B_n = \{0,1,\dots,n\}^3$ is the set of integer points whose coordinates are between (and including) 0 and $n$.
- **$C(n)$.** The number of **different** lattice cubes all of whose vertices lie in $B_n$ (i.e., every coordinate of every vertex is an integer in $[0,n]$). Two cubes are considered different if any of their vertices have different coordinates (so a cube is identified with its set of 8 vertices; the count is over distinct vertex-sets forming a cube).
- **Lattice points contained in a cube.** The number of integer-coordinate points lying in the closed cube (interior and surface, including vertices and edges and faces). The statement's examples give both the total and its split into surface and strictly interior counts.
- **$S(n)$.** The sum, over all distinct lattice cubes counted by $C(n)$, of the number of lattice points contained in each such cube: $S(n) = \sum_{\text{cube } K \in \mathcal{K}_n} |K \cap \mathbb{Z}^3|$, where $\mathcal{K}_n$ is the set counted by $C(n)$.
- **Side length.** The examples call both cubes' edge length 3; the axis-aligned example spans coordinates 0 to 3 in each axis, and the tilted example's vertices are claimed to have the same side length 3 (usable as a consistency check).
- **Target.** Compute $S(5000) \bmod 10^9$, i.e., the remainder of $S(5000)$ upon division by $1\,000\,000\,000$.

## 3. Completion criteria

For the extraction task currently requested:

- [ ] The verbatim problem statement is reproduced word for word in this file (Section 1) — **done**.
- [ ] Every symbol ($C$, $S$, $n$, lattice cube) and every count is defined precisely (Section 2) — **done**.
- [ ] All worked example values from the statement are recorded as the test oracle (Section 4) — **done**.
- [ ] Report the verbatim text and the exact numerical values of the worked examples in the final message — **done**.

For any future solution attempt (not part of this extraction task):

- [ ] A method must produce the single integer $S(5000) \bmod 10^9$.
- [ ] It must reproduce all given oracle values: $C(1),C(2),C(4),C(5),C(10),C(50)$ and $S(1),S(2),S(4),S(5),S(10),S(50)$ exactly.
- [ ] The oracle cube examples (64 = 56 surface + 8 interior for the axis-aligned side-3 cube; 40 = 20 surface + 20 interior for the tilted side-3 cube) must be reproduced by any per-cube lattice-point-counting routine.
- [ ] Per method policy: no answer-space search, no exponential time/space algorithms; use exact arithmetic; verify by an independent route.

## 4. Known small cases / worked example values (test oracle)

Counting function $C(n)$:

| $n$ | $C(n)$ |
|-----|--------|
| 1   | 1      |
| 2   | 9      |
| 4   | 100    |
| 5   | 229    |
| 10  | 4469   |
| 50  | 8154671 |

Sum function $S(n)$:

| $n$ | $S(n)$       |
|-----|--------------|
| 1   | 8            |
| 2   | 91           |
| 4   | 1878         |
| 5   | 5832         |
| 10  | 387003       |
| 50  | 29948928129  |

Worked per-cube lattice point counts (both cubes have side length 3):

- **Cube A (axis-aligned).** Vertices: $(0,0,0)$, $(3,0,0)$, $(0,3,0)$, $(0,0,3)$, $(0,3,3)$, $(3,0,3)$, $(3,3,0)$, $(3,3,3)$.
  Contains **64** lattice points in total = **56** on the surface (including the **8** vertices) + **8** within (interior).
- **Cube B (tilted).** Vertices: $(0,2,2)$, $(1,4,4)$, $(2,0,3)$, $(2,3,0)$, $(3,2,5)$, $(3,5,2)$, $(4,1,1)$, $(5,3,3)$.
  Contains only **40** lattice points = **20** on the surface + **20** within, despite same side length 3.