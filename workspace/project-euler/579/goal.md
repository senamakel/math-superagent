# Goal

Current objective: **extract, restate, and record** the problem statement of
Project Euler 579 (as downloaded at `/workspace/problem.html`). Explicitly
**not** to solve the problem yet.

Completion criteria:
- [x] Read `/workspace/problem.html`.
- [x] Reproduce the problem statement verbatim in this document.
- [x] Provide a precise restatement in own words.
- [x] Define every symbol used in the statement.
- [x] Record the small cases / worked examples from the statement, clearly marked as the test oracle.
- [ ] (Future, separate task) Solve $S(5000) \bmod 10^9$ — not part of this task.

---

## 1. Verbatim problem statement (Project Euler 579)

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

Source: `/workspace/problem.html` (official Project Euler 579 statement, downloaded).

---

## 2. Restatement in my own words

- A *lattice cube* is a (three-dimensional) cube whose 8 vertices all have
  integer coordinates. Any cube is identified with its set of 8 vertices;
  two cubes are counted as the same cube exactly when their vertex sets are
  identical, and as different cubes when at least one vertex has different
  coordinates (i.e., a cube is a set of 8 points forming a cube, not an
  oriented/ordered object).

- For a non-negative integer $n$, $C(n)$ is the number of distinct lattice
  cubes all of whose vertex coordinates lie in the set $\{0, 1, \dots, n\}$
  (each coordinate of each vertex between $0$ and $n$ inclusive).

- Different such cubes can contain different numbers of *lattice points*, i.e.,
  points with integer coordinates lying in the (closed) cube. Two example cubes
  with the same side length 3 illustrate this: one contains 64 lattice points,
  the other only 40.

- $S(n)$ is the sum, over all distinct lattice cubes counted by $C(n)$, of the
  number of lattice points contained in each cube.

- The problem to solve (in a later task) is $S(5000) \bmod 10^9$.

### Scope constraints
- Dimension is fixed at 3 (cubes in $\mathbb{R}^3$).
- Coordinates: integers in $[0, n]$ inclusive.
- Counting: each geometric cube counted once (by its vertex set).
- The summand for a cube is the number of integer-coordinate points inside the
  closed cube (boundary included).

---

## 3. Definitions of every symbol used

| Symbol | Meaning |
|---|---|
| $n$ | Non-negative integer bounding box parameter: every vertex coordinate of every counted cube must satisfy $0 \le \text{coord} \le n$, i.e. lie in $\{0,1,\dots,n\}$. |
| **lattice cube** | A cube in $\mathbb{R}^3$ all of whose 8 vertices have integer coordinates. |
| $C(n)$ | Number of different lattice cubes with all vertex coordinates in $\{0,1,\dots,n\}$; two cubes differ iff some vertex of one has coordinates different from the corresponding feature of the other (equivalently, iff their vertex sets differ). Example values: $C(1)=1$, $C(2)=9$, $C(4)=100$, $C(5)=229$, $C(10)=4469$, $C(50)=8154671$. |
| **lattice point (contained in a cube)** | A point with integer coordinates lying in the closed cube (including boundary). |
| **surface points (of a cube)** | Lattice points lying on the cube's surface (boundary), including its 8 vertices. |
| **points within the cube** | Lattice points strictly inside the cube (not on the surface). |
| **side length** | The common Euclidean length of the cube's edges (statement uses it only in the comparison: both example cubes have side length 3). |
| $S(n)$ | Sum of the numbers of lattice points contained in the different lattice cubes counted by $C(n)$: $S(n) = \sum_{\text{cubes } Q \text{ counted by } C(n)} \#\{\text{lattice points in } Q\}$. Example values: $S(1)=8$, $S(2)=91$, $S(4)=1878$, $S(5)=5832$, $S(10)=387003$, $S(50)=29948928129$. |
| $10^9$ | The modulus for the final answer: the task is $S(5000) \bmod 10^9$ (residue in $\{0,1,\dots,10^9-1\}$). |

---

## 4. Test oracle (given in the statement)

These are the exact values and worked examples supplied by the problem
statement. **Any future method must reproduce all of these exactly.**

### 4.1 Counting cubes
$$C(1)=1,\quad C(2)=9,\quad C(4)=100,\quad C(5)=229,\quad C(10)=4469,\quad C(50)=8154671.$$

Observed consistency check (own deduction, not part of the statement): for
$n=1$ the only cube is the unit cube $[0,1]^3$, so $C(1)=1$; its 8 lattice
points are exactly its vertices, consistent with $S(1)=8$.

### 4.2 Worked example: axis-aligned cube (side length 3)
Vertices:
$$(0,0,0),\ (3,0,0),\ (0,3,0),\ (0,0,3),\ (0,3,3),\ (3,0,3),\ (3,3,0),\ (3,3,3).$$
This is the cube $[0,3]^3$. It contains **64 lattice points**:
- **56 lattice points on the surface**, including the 8 vertices,
- **8 lattice points within the cube** (strictly inside).

### 4.3 Worked example: rotated cube (side length 3, same side length)
Vertices:
$$(0,2,2),\ (1,4,4),\ (2,0,3),\ (2,3,0),\ (3,2,5),\ (3,5,2),\ (4,1,1),\ (5,3,3).$$
It contains only **40 lattice points**:
- **20 points on the surface**,
- **20 points within the cube**.

Key contrast stated: although both cubes have the same side length $3$, they
contain different numbers of lattice points (64 vs 40).

### 4.4 Sum values
$$S(1)=8,\quad S(2)=91,\quad S(4)=1878,\quad S(5)=5832,\quad S(10)=387003,\quad S(50)=29948928129.$$

### 4.5 Target
$$\text{Find } S(5000) \bmod 10^9.$$

---

*Note: this document intentionally does not solve the problem. The test oracle
above is the ground truth for validating any later method.*