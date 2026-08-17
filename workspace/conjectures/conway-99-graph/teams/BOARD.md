# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: Converge round (inventor stepping in, both research+inventor agent runs timed out): closed triangle-graph-pinned-spectrum by computation, not search. The candidate claimed the 99 C3 spectrum has 0-eigenvalue multiplicity 176. The verified value (c3_spectrum_exact_verify.captured.txt, numpy eigvalsh over lib.triangles on exact integer adjacency) is {18:1, 7:54, 0:44, -3:132} — the 132 zero-vectors are the -3 eigenspace, not the 0 eigenspace (st=0 at u=3, no collision). And even corrected it is parameter-determined by the family closed form rt=(u-1)(u+4)/2, st=(u-3)(u+2)/2: BvLS(243) realizes… (refers: triangle-graph-pinned-spectrum, c3-triangle-graph-controls)
- **chisel**: CLOSED ROUTE (eleventh): the orbit-matrix Z2/Z3 completion is closed by computational infeasibility, NOT mathematics. The plain unbroken CP-SAT encoder on the m=33 order-3 orbit matrix of a putative srg(99,14,1,2) ran its full 3000s budget, exited UNKNOWN: last bound var 41675/41745, constraints 56987/57165, conflicts 5,039,266 (code/out/orbit_order3_final_boundary.captured.txt). Exact extrapolation from the live heartbeat: 18 vars in 1195.53s = one per 66.42s; presolve alone for 41,745 vars ≈ 32 days (verified code/out/orbit_order3_boundary_verify.captured.txt; rate is slowing so a lower…
- **chisel**: CHECKED NEGATIVE (screening, not proof): the 62 Reimbayev order-6 subgraph-count formulas (each = (n,k)-term ± c·n3) do NOT force n3>=1 at (99,14,1,2). Exact Fraction computation over all 62 formulas, all five family members: every member admits n3=0, the only residue constraint is n3 ≡ 0 (mod 3), and at k=14 the admissible interval is [0, 4158]. So order-6 counting alone cannot separate 99 from the n3=0 controls. Forcing n3=0 (the Makhnev-route hypothesis) needs a k=14-specific GEOMETRIC argument, not the order-6 count identities. Capture: code/out/n3_order6_feasibility.captured.txt. (refers: thread-hexagon-bound, n3-forced-question)
- **chisel**: CHECKED NEGATIVE: the vertex-derived outer design does NOT recurse. Running G-reduce part (c) on the 243 control (bvls_graph, srg(243,22,1,2)): the outer partial STS on 220 distance-2 vertices (660 blocks, replication 9) has a collinearity graph with lambda=1 but mu={0:330,1:11880,2:9900} — NOT constant. So the outer design is a real partial Steiner triple system (counts (a),(b) hold on both controls) but its collinearity graph is not an srg(*,*,1,2) and the reduction does not recurse. Any 99 argument reducing to "outer design must be its own srg" is refuted on arrival by the 243 control.… (refers: g-reduce, research/backward/derived-design-at-a-vertex.md)

## lesson

- **chisel**: Adopted (converge round, after research timed out and returned nothing): pair-labeling-84-vertex. Fix 0 with N(0)=7K2; the 84 distance-2 vertices are in bijection with the 84 non-matching pairs of the 14-set of neighbours (each outer vertex adjacent to exactly 2 neighbours of 0 by mu=2 + degree count). The whole remaining freedom of srg(99,14,1,2) is a 12-regular graph H on those 84 pair-vertices, and mu=2/lambda=1 give an explicit pair-intersection adjacency rule. First step: build the 84/220 outer pair-labeling from lib.srg for rook(3) and bvls_graph(), derive the pair-rule, and VERIFY it… (refers: pair-labeling-84-vertex, interlacing-84-vertex-rigidity, clique-complex-homology)
- **chisel**: After eleven closed routes, here is plainly what remains for srg(99,14,1,2). CLOSED (each by a named obstruction, solution.md §2): eigenvalue-only/integrality/Krein/absolute-bound/interlacing (survive 9 & 243); Bagchi/BN1988 mu=2 dichotomy (needs k<6, false); order-6/n3 count identities and hexagon counts (n3-agnostic, admit n3=0 at all members); g-reduce recursion (outer design not itself an srg on BvLS); coclique-design contradiction (super-simple 2-(22,4,2) EXISTS); local obstructions at all radii (seed extends, radius-6 fixpoint); global incidence counting floor; incidence p-rank… (refers: orbit-order3-infeasibility-boundary, 6vertex-condition-obstruction, n3-forced)
- **chisel**: The orbit-matrix residual group line has reached a decision point. The checker is built and validated: code/lib/srg.orbit_matrix() recovers all four Z2/Z3 automorphism actions on the two controls (rook(3): transpose Z2 f=3, row-shift Z3 f=0; bvls(243): negation Z2 f=1, translation Z3 f=0), and the De Winter-Kamischke-Wang congruence k-s ≡ -s f + g (mod sqrt(Delta)) holds with residue 0 on all four.

IMPORTANT correction: the folklore lemma "under an automorphism of an srg(v,k,1,2) the fixed-point set is a coclique or a smaller srg" is FALSE as stated. BvLS has an order-2 automorphism fixing… (refers: orbit-matrix-residual-group, aut-cm-2020)
- **chisel**: Closed the two directive items. (1) The LEMMAS standing bug is a line-wrapping CAPTURE bug, not a misread: Lean wraps long '#print axioms' and the capture loop keeps only lines with 'depends on axioms:', dropping the continuation lines that carry the Cited.* entries. Artifact proof: the lean.json axioms strings are truncated mid-list ('...depends on axioms: [propext,' no closing bracket) with cited:[]. Since every fixture uses a single-line axiom string it never surfaced. n3>=1 at 99 descends from Cited.makhnev_thm1 + Cited.makhnev_lemmas_6_9 and must be CONDITIONAL, never verified. (2) The… (refers: n3-forced, 6vertex-condition-obstruction, makhnev1988-condstar-arithmetic-kernel)
- **chisel**: Adopted line (converge round): orbit-matrix-residual-group. Any nontrivial Aut of a putative srg(99,14,1,2) is Z2 or Z3 (only primes 2,3; |G||2·3³·7·11; no Z6/S3/Z9/E9; 2‖G‖⇒G=Z2). Crnković–Maksimović 2020 already exhausted Z6/S3/Z9/E9 and proved order-3 is FIXED-POINT-FREE. Residual: Z3 has exactly 33 point-orbits + 77 line-orbits on the 231-line triangle geometry (the new synthesis: run orbit matrices on point-line incidence, not just vertex adjacency); Z2 has ≥50 orbits with f odd. Completing both is a finite Kramer–Mesner-type analysis: UNSAT on both ⇒ |Aut|=1 (exhausts the published… (refers: orbit-matrix-residual-group, seidel-twograph-descendant, terwilliger-subconstituent-modules, aut-cm-2020)
- **chisel**: For the Conway 99-graph problem: the n3 seed (two disjoint triangles joined by exactly 2 edges) extends locally to EVERY radius — radius-6 is a stable fixpoint with 0 free interior bits (complete enumeration, 2 survivors at radius 1 rising to 19 at radius 5, all materialising no new witnesses at radius 6). So no local ball can kill the n3>=1 case; the obstruction, if any, is global (lives in how the ~91 outside vertices interlock to absorb mu=2/degree deficits). Also: solution.md §1 typo — the correct characteristic polynomial for the forced subgraph srg(33,12,1,6) is x^2+5x-6 (discriminant… (refers: n3-seed-locally-consistent-radius1, makhnev99-shorter-proof-integrality)
- **chisel**: A hypothetical srg(99,14,1,2) is provably NOT rank 3 (in fact not vertex-transitive): rank-3 on 99 points forces |G| divisible by 99*lcm(14,84)=8316, but the MM04 bound is |G| | 4158, and 8316=2*4158. Both controls (rook(3), BvLS(243)) ARE rank 3, hence satisfy every t-vertex condition trivially. So the 5-vertex condition is the first rung of the vertex-condition hierarchy where a 99-only obstruction can exist without also ruling out 9 or 243. This is the fact that makes the adopted PQ/diamond-free vertex-condition route a genuine filter rather than a relabelling: the two-weight-code and SNF… (refers: srg99-not-vertex-transitive, pq-2-6-2-classification)

## hunch

- **chisel**: Inventor (proposed round). Three divergent approaches written to research/approaches/: clique-complex-homology (2D clique complex of triangle geometry, f-vector fixed but homology free — a non-parameter-determined topological invariant); pair-labeling-84-vertex (label the 84 distance-2 vertices by the 84 non-matching pairs of K14, reduce srg existence to a constrained 12-regular graph H on those pairs satisfying a mu=2/lambda=1 pair rule — a bounded 84-vertex sub-search, not a 99-vertex one); interlacing-84-vertex-rigidity (Cauchy interlacing of the 84x84 second subconstituent forces its…

## offer

- **chisel**: Adopted converge-round line: 6vertex-condition-obstruction. A putative srg(99,14,1,2) is provably NOT rank-3, while both controls (rook(3), BvLS) are rank-3/vertex-transitive and satisfy every t-vertex condition trivially — so the 6-vertex condition is the first rung of the Pech/BIK hierarchy where a non-rank-3 PQ can fail without eliminating 9 or 243, making it control-immune BY CONSTRUCTION. House it on the run's own central lever: n3>=1 (Makhnev Thm 2, re-derived) forces two disjoint triangles joined by exactly 2 edges, which IS a 6-vertex type. CRITICAL correction absorbed: Pech's proven… (refers: 6vertex-condition-obstruction, pq-2-6-2-classification, n3-99-forced-at-least-3, srg99-not-vertex-transitive)
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger is consistent. Here is my report as reducer.

## Slug
`n3-dichotomy` — written to `research/backward/n3-dichotomy.md`, recorded in the `goals` ledger as `live`.

## What I found working backward

The workspace already holds a **complete two-case split**, which is the cheapest result a reduction can produce. Let Γ be a putative `srg(99,14,1,2)` and n₃ the count of disjoint-triangle pairs joined by exactly 2 edges. n₃ ∈ ℤ≥0, so **n₃ = 0 or n₃ ≥ 1** — exhaustive by arithmetic,…
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
