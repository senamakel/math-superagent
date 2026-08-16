# Derived design at a vertex — what would prove nonexistence of srg(99,14,1,2)

This skeleton takes the problem's own geometric restatement seriously. Every edge of
`srg(99,14,1,2)` lies in a unique triangle, so the 231 triangles are the *lines* of a
partial linear space on 99 points (3 points per line, 7 lines per point), and `μ = 2`
is the one remaining condition: two points **not** on a common line have exactly two
points collinear with both. The reduction below pins down, vertex by vertex, exactly
what that geometry must look like, and turns "does srg(99,14,1,2) exist" into a finite
design question on 84 points.

Everything here was derived by hand and the counts are the same argument for every
member of the `(v,k,1,2)` family; nothing below is yet machine-checked. The two
existing members — the 3×3 rook's graph and Berlekamp–van Lint–Seidel — must pass
every step that is not the *final* parameter-specific obstruction.

```skeleton
goal: no srg(99,14,1,2) exists
implies: G-reduce gives "srg exists iff vertex-derived design D exists"; G-encode gives "D exists iff phi(99) is satisfiable"; G-unsat gives "phi(99) is UNSAT"; chaining the three equivalences forces nonexistence.
status: sketched
rests-on: problem.md restatement (edge-in-unique-triangle + nonadjacent-pair-in-unique-4-cycle forces srg(99,14,1,2)) and the partial-linear-space view; no claim ids yet, research/CLAIMS.md is empty
killed-by:
```

```gap
id: G-reduce
lemma: Fix a vertex v0 of any srg(v,k,1,2) with v = 1 + k + k(k-2)/2 (k even). Then (a) N(v0) induces (k/2)K2 and the k(k-2)/2 vertices at distance 2 from v0 are in bijection with the k(k-2)/2 non-edges of N(v0), each w sent to its two neighbours in N(v0); (b) the triangles partition as k/2 lines through v0, k(k-2)/2 cross lines with one point in N(v0) and two at distance 2, and k(k-2)(k-4)/12 outer lines wholly among the distance-2 vertices, which form a partial Steiner triple system of replication (k-4)/2; (c) conversely, any structure of this shape whose collinearity graph has lambda=1 and mu=2 is an srg(v,k,1,2). At (99,14,1,2): 84 distance-2 vertices, 84 cross lines, 140 outer blocks, replication 5. This is a reduction, not a contradiction — it holds verbatim at (9,4,1,2) with 4/0 outer blocks and at (243,22,1,2) with 220/660.
status: open
next: tool_builder verifies (a)-(c) on the rook's graph and BvLS through the canonical oracle (assert the 84<->non-edge bijection, the 84/140 split, lambda=1, mu=2); theorem_prover/lean_prover proves (a)-(c) from A^2 = kI + lambda*A + mu*(J-I-A), a short bijective counting argument and the first statement to formalise.
```

```gap
id: G-encode
lemma: There is an exact CP-SAT/SAT encoding of the partial Steiner triple system on 99 points, 231 blocks of size 3, replication 7, with the mu=2 condition (equivalently, of the vertex-derived design D), whose Boolean models are in bijection with the graphs in question up to the choice of v0. The same encoder at (9,4,1,2) and (243,22,1,2) must have models decoding to the rook's graph and Berlekamp–van Lint–Seidel — the GOAL-mandated proof that the encoding is faithful.
status: open
next: sat_solver builds the encoder and runs it at (9,4,1,2) and (243,22,1,2), confirming it finds both graphs before any UNSAT at 99 is admissible; tool_builder writes the decoder from a Boolean model to an adjacency matrix on disk and runs it through the canonical oracle.
```

```gap
id: G-unsat
lemma: The vertex-derived design at (99,14,1,2) does not exist: there is no partial Steiner triple system on 84 points with 140 blocks and replication 5, attached by 84 cross lines to the 7 matched edges of a 7K2, whose collinearity graph has mu=2. Equivalently phi(99) is unsatisfiable.
status: open
next: sat_solver runs phi(99) with a stated search space and symmetry reduction (fix v0 and the 7K2), recording the space, worker count, and the wall-clock at which it is abandoned if it does not terminate — that boundary is itself a reportable result. In parallel, inventor/theorem_prover seeks a counting obstruction on the 84-point outer design specific to (84,140,5); any candidate must fail on the rook's graph and BvLS before effort is spent.
```

## Notes on the discipline this skeleton imposes

- **G-reduce and G-encode are parameter-uniform.** They survive the two positive
  controls by construction; they are the *setup*, not the contradiction. Only G-unsat
  is allowed to be parameter-specific, and its `next` enforces the `v=9`/`v=243` test.
- The chain `srg exists <=> D exists <=> phi satisfiable` is the inference in
  `implies`; each `<=>` is a separate claim (G-reduce's (c), G-encode's bijection) and
  must be proved, not assumed.
- The final search, if it is attempted at full 99, is the one place enumeration is
  being contemplated; it is admissible only with the GOAL.md exhaustiveness argument,
  and the honest outcome may be the frontier (space, reduction, wall-clock) rather
  than UNSAT.
