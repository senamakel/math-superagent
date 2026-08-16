# Conway's 99-graph problem

> **(99)** Does there exist an undirected graph `G` on `99` vertices in which
> every edge lies in a **unique** triangle, and every non-adjacent pair of
> vertices lies in a **unique** 4-cycle?

Posed by John H. Conway, who attached a $1000 prize to it in his 2017 list of
five $1000 problems. It is a special case of a much older question — the
existence of a strongly regular graph with parameters `(99, 14, 1, 2)` — and it
is open: no construction is known and no nonexistence proof is known.

## The restatement that should be used everywhere

The two conditions force regularity, and the object is exactly a strongly
regular graph.

- "every edge is in a unique triangle" is `λ = 1`: two adjacent vertices have
  exactly one common neighbour.
- "every non-adjacent pair is in a unique 4-cycle" is `μ = 2`: two non-adjacent
  vertices have exactly two common neighbours (a 4-cycle through a non-adjacent
  pair `u, w` is a choice of two distinct common neighbours, so *unique* 4-cycle
  means exactly two common neighbours, not exactly one).
- Counting from a vertex `v` of degree `k`: `v` has `k` neighbours, and each
  non-neighbour is reached by exactly `μ = 2` paths of length two, of which
  there are `k(k − λ − 1)`. So

```
k(k − 2) = 2 (v − k − 1),     v = 1 + k + k(k − 2)/2.
```

  With `v = 99` this gives `k = 14`, so `G` is `srg(99, 14, 1, 2)`.
  **Derive this rather than importing it, and record the derivation.**

Immediate consequences to re-derive, not to assume:

- `|E| = 99 · 14 / 2 = 693`, and since edges are partitioned by triangles,
  there are `693 / 3 = 231` triangles; each vertex is in `14 / 2 = 7` of them.
- `λ = 1` means the neighbourhood of every vertex induces a **perfect matching**
  on `14` vertices: `G` is *locally* `7 K₂`.
- The `231` triangles are the lines of a partial linear space on `99` points
  with `3` points per line and `7` lines per point, whose collinearity graph is
  `G`. The `μ = 2` condition is a statement about that geometry.
- Eigenvalues: `r, s` are the roots of `x² − (λ − μ)x − (k − μ) = x² + x − 12`,
  so `r = 3`, `s = −4`, with multiplicities to be computed from the standard
  formula. **Compute them; integrality is a nontrivial check and the run should
  see it pass.**

## The family this sits in, and the negative controls

Feasibility of `srg(v, k, 1, 2)` needs `4k − 7` to be a perfect square (from the
eigenvalue formula `(−1 ± √(4k − 7))/2`), which with the counting relation
above gives the candidate list

```
k =  4,  v =   9
k =  8,  v =  33
k = 14,  v =  99
k = 22,  v = 243
k = 32,  v = 513
k = 44,  v = 969
...
```

**Verify this list by computation before using it.** Two members are known to
exist, and they are the sharpest tool in this workspace:

- `srg(9, 4, 1, 2)` — the `3 × 3` rook's graph `K₃ □ K₃`, equivalently the
  Paley graph of order 9. Exists.
- `srg(243, 22, 1, 2)` — the Berlekamp–van Lint–Seidel graph, from the perfect
  ternary Golay code. Exists.

*Consequence, and it is the structural fact that disciplines every nonexistence
argument here:* **any proof that `srg(99,14,1,2)` does not exist must fail on
`v = 9` and on `v = 243`.** An argument that uses only `λ = 1`, `μ = 2`,
regularity, eigenvalue integrality, counting of triangles and quadrilaterals,
interlacing, or the Krein / absolute bounds — all of which hold verbatim for 9
and 243 — cannot be a proof, and can be killed by running it against those two
graphs before any effort is spent on it. Every candidate argument in this
workspace must be run against that test and the outcome recorded.

Symmetrically: **any construction must explain why the same construction does
not produce members at the infeasible `k`**, and must be checked by the oracle
rather than believed.

## Known results — leads, not imports

**These are recalled from memory and must be re-established from primary
sources before anything is built on them. Print the source and the exact
hypothesis beside each one you confirm; strike any you cannot.**

- **The parameter set passes every standard feasibility test.** Integrality of
  eigenvalue multiplicities, the Krein conditions, the absolute bound, and the
  claw / clique bounds are all satisfied by `(99, 14, 1, 2)`. That is why the
  question is hard: the easy obstructions are exhausted.
- **`srg(33, 8, 1, 2)` is believed to be ruled out**, i.e. the next member up
  from the rook's graph does not exist. **Confirm this and record the proof's
  mechanism** — if a nonexistence proof exists for 33, its method is the single
  most relevant precedent in the literature, and whether it can reach 99 (or
  provably cannot) is a first-class question for this run.
- **Automorphisms are heavily constrained.** A line of work (Behbahani–Lam on
  strongly regular graphs with prescribed automorphisms; Makhnev and coauthors
  specifically on `(99,14,1,2)`) rules out automorphisms of various prime
  orders, and it is believed that any such graph has a very small — possibly
  trivial — automorphism group. **Establish exactly which orders are excluded
  and by whom.** This matters practically: it says the graph cannot be found by
  the usual symmetry-assuming search, which is why the computational literature
  has not settled it.
- **No vertex-transitive example**, and more generally no example admitting a
  large group, follows from the above. Confirm the exact statement.
- **Exhaustive search is out of reach.** The number of graphs to consider is
  astronomically beyond enumeration; published searches are all under symmetry
  assumptions or partial-extension frameworks (orderly generation / canonical
  augmentation on the triangle geometry). **Find what the largest completed
  partial search actually was**, because that is the honest current frontier and
  this run should not re-do it.
- **Conway's prize.** $1000, announced 2017 in "Five $1,000 Problems (Update
  2017)"; Conway died in 2020 — record whether the prize is still administered,
  purely as a fact about the problem's status, and spend no further effort on
  it.

## What is genuinely unknown

- Existence or nonexistence of `srg(99, 14, 1, 2)`.
- Whether the local structure (`locally 7K₂`) plus `μ = 2` forces a
  contradiction by a counting or geometric argument that is *not* an eigenvalue
  argument — the eigenvalue route is provably exhausted, since 9 and 243 pass
  it.
- The exact automorphism group: whether the trivial group is the only
  possibility, and whether that can be proved outright.
- Whether the triangle geometry (a partial Steiner triple system on 99 points,
  231 blocks, replication 7) can be constrained enough to be enumerated modulo
  isomorphism — the reduction to a design-theoretic classification is the most
  promising route to a *finite* decision procedure, and its true cost is
  unknown.
- Nonexistence for any later member of the family (513, 969, …) — a proof for a
  larger member whose mechanism does not apply to 9 or 243 would be a genuine
  advance even if it misses 99.

## What counts as a result

In descending order of value.

1. A construction of `srg(99, 14, 1, 2)`, certified by the oracle in `code/`
   from an explicit adjacency matrix committed to this workspace.
2. A proof of nonexistence, with the step that fails for `v = 9` and `v = 243`
   named explicitly and checked against both graphs.
3. A theorem constraining any such graph beyond what the literature has: an
   automorphism order excluded that was not excluded before, a forced
   substructure, a bound on the number of `K₄`-free / `C₅` configurations, a
   forced or forbidden local configuration in the triangle geometry — proved,
   not measured.
4. A completed exhaustive sub-search with a stated, checkable search space:
   "no `srg(99,14,1,2)` contains configuration `X`" where the enumeration is
   reproducible from `code/` and its exhaustiveness argument is written out.
   The exhaustiveness argument is the result; the run time is not.
5. A refutation of a published or folklore approach, with an explicit witness
   — for instance, the rook's graph or the Berlekamp–van Lint–Seidel graph
   satisfying every hypothesis of a proposed nonexistence argument.
6. A sharp statement of the boundary: which sub-searches are feasible on this
   machine and which are not, with the measured cost and the extrapolation.

**Do not claim the problem.** A proof or a construction produced in a run of
this length is, on prior, an error; if you believe you have one, the deliverable
is the argument or the adjacency matrix with every step's status labelled and
the `v = 9` / `v = 243` test applied to it explicitly, not an announcement.
A claimed construction is worth nothing until the canonical oracle in `code/lib`
has verified the matrix from disk.
