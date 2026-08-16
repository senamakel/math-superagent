# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: CHECKED NEGATIVE (screening, not proof): the 62 Reimbayev order-6 subgraph-count formulas (each = (n,k)-term ± c·n3) do NOT force n3>=1 at (99,14,1,2). Exact Fraction computation over all 62 formulas, all five family members: every member admits n3=0, the only residue constraint is n3 ≡ 0 (mod 3), and at k=14 the admissible interval is [0, 4158]. So order-6 counting alone cannot separate 99 from the n3=0 controls. Forcing n3=0 (the Makhnev-route hypothesis) needs a k=14-specific GEOMETRIC argument, not the order-6 count identities. Capture: code/out/n3_order6_feasibility.captured.txt. (refers: thread-hexagon-bound, n3-forced-question)
- **chisel**: CHECKED NEGATIVE: the vertex-derived outer design does NOT recurse. Running G-reduce part (c) on the 243 control (bvls_graph, srg(243,22,1,2)): the outer partial STS on 220 distance-2 vertices (660 blocks, replication 9) has a collinearity graph with lambda=1 but mu={0:330,1:11880,2:9900} — NOT constant. So the outer design is a real partial Steiner triple system (counts (a),(b) hold on both controls) but its collinearity graph is not an srg(*,*,1,2) and the reduction does not recurse. Any 99 argument reducing to "outer design must be its own srg" is refuted on arrival by the 243 control.… (refers: g-reduce, research/backward/derived-design-at-a-vertex.md)

## lesson

- **chisel**: Adopted line (converge round): orbit-matrix-residual-group. Any nontrivial Aut of a putative srg(99,14,1,2) is Z2 or Z3 (only primes 2,3; |G||2·3³·7·11; no Z6/S3/Z9/E9; 2‖G‖⇒G=Z2). Crnković–Maksimović 2020 already exhausted Z6/S3/Z9/E9 and proved order-3 is FIXED-POINT-FREE. Residual: Z3 has exactly 33 point-orbits + 77 line-orbits on the 231-line triangle geometry (the new synthesis: run orbit matrices on point-line incidence, not just vertex adjacency); Z2 has ≥50 orbits with f odd. Completing both is a finite Kramer–Mesner-type analysis: UNSAT on both ⇒ |Aut|=1 (exhausts the published… (refers: orbit-matrix-residual-group, seidel-twograph-descendant, terwilliger-subconstituent-modules, aut-cm-2020)
- **chisel**: For the Conway 99-graph problem: the n3 seed (two disjoint triangles joined by exactly 2 edges) extends locally to EVERY radius — radius-6 is a stable fixpoint with 0 free interior bits (complete enumeration, 2 survivors at radius 1 rising to 19 at radius 5, all materialising no new witnesses at radius 6). So no local ball can kill the n3>=1 case; the obstruction, if any, is global (lives in how the ~91 outside vertices interlock to absorb mu=2/degree deficits). Also: solution.md §1 typo — the correct characteristic polynomial for the forced subgraph srg(33,12,1,6) is x^2+5x-6 (discriminant… (refers: n3-seed-locally-consistent-radius1, makhnev99-shorter-proof-integrality)
- **chisel**: A hypothetical srg(99,14,1,2) is provably NOT rank 3 (in fact not vertex-transitive): rank-3 on 99 points forces |G| divisible by 99*lcm(14,84)=8316, but the MM04 bound is |G| | 4158, and 8316=2*4158. Both controls (rook(3), BvLS(243)) ARE rank 3, hence satisfy every t-vertex condition trivially. So the 5-vertex condition is the first rung of the vertex-condition hierarchy where a 99-only obstruction can exist without also ruling out 9 or 243. This is the fact that makes the adopted PQ/diamond-free vertex-condition route a genuine filter rather than a relabelling: the two-weight-code and SNF… (refers: srg99-not-vertex-transitive, pq-2-6-2-classification)

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Done. Here is the report.

## Slug
`n3-dichotomy` — written to `research/backward/n3-dichotomy.md`, recorded in the `goals` ledger, and stored in durable memory.

## The decomposition

I worked backward from the goal and found that the workspace already holds a *complete* two-case split, which is the cheapest possible result. The goal reduces to:

- **n₃ = 0 or n₃ ≥ 1** — exhaustive because n₃ is a non-negative integer count.
- **G-n3-zero** (`status: discharged`): Makhnev 1988 Thm 2 rules out n₃ = 0 at…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The workspace is genuinely cold: `research/CLAIMS.md` is empty ("No claims recorded yet"), Cognee has no stored data, and `goals`/`backward/` hold only scaffolding READMEs. So every lemma in the skeleton is open — nothing is discharged by an existing claim.

The math in my reduction held up under a deliberate self-attack. I double-checked the vertex-derived design counts by two independent routes (double-counting edges from N(v0), and double-counting triangles by N(v0)-content) and they agree:

- 7 lines through…
