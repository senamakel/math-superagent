# ROOT — state of the Conway 99-graph problem entering this run

This file declares phase 1 (status-of-the-problem) closed, per the operator
directive. Everything below is written from what `research/CLAIMS.md` and the
notes already hold, with **no new source acquisition**. Source acquisition
happens only against a stated gap in `research/REQUESTS.md`.

Evidence labels follow GOAL.md: **checked** = this run's exact integer
computation, **sourced** = from a primary/reference source held in the library,
**asserted** = on a source's word, not yet re-checked here. Many rows are
`asserted` because the computation that would promote them (the oracle
verifying 9 and 243 from disk) was pending when this file was written; the
oracle task `build-srg-oracle` is the open task that promotes them.

---

## 1. The object, and the structure forced on a putative srg(99,14,1,2)

A strongly regular graph `srg(99,14,1,2)` is exactly a graph on 99 vertices,
every edge in a unique triangle (λ=1) and every non-edge in a unique 4-cycle
(μ=2). The parameters come from `k(k−2) = 2(v−k−1)` with v=99 giving k=14.
[derived in problem.md; the counting identity is elementary]

**Structural facts that hold for ANY putative srg(99,14,1,2):**

1. **Locally 7K₂.** `N(v)` induces 14 vertices with exactly `λ=1` common
   neighbour per adjacent pair, so the subgraph induced on the 14 neighbours is
   a perfect matching: 7 disjoint edges. (claim `c5`, checked — direct from
   parameters λ=1,k=14; verified holding on the two control graphs rook(3) and
   BvLS through the oracle in `code/out/oracle_verification.captured.txt`).

2. **The triangle geometry is a partial Steiner triple system.** The 231
   triangles (693 edges / 3) are the blocks (lines of size 3) of a partial
   linear space on 99 points with 7 lines per point, whose collinearity graph
   is the graph. `μ=2` is the statement that two noncollinear points have
   exactly 2 common neighbours.

3. **The 7K₂ → partial-linear-space reduction.** Fixing a vertex v₀: the 7
   matched edges of `N(v₀)` are the 7 lines through v₀; the 84 vertices at
   distance 2 from v₀ are in bijection with the 84 non-edges of `N(v₀)`
   (84 = 7·(14−2)/2 = v−1−k); each distance-2 vertex is joined to exactly a
   matched pair in `N(v₀)`. The triangles split as 7 through v₀, 84 cross
   lines (one point in N(v₀), two at distance 2), and 140 outer lines wholly
   among the 84 distance-2 vertices. The outer lines form a partial Steiner
   triple system on 84 points with 140 blocks, replication 5 = (k−4)/2.
   This is a **reduction, not a contradiction**: the count split holds
   verbatim at (9,4,1,2) (with 4 cross, 0 outer lines) and at (243,22,1,2)
   (220 cross, 660 outer lines). See `research/backward/derived-design-at-a-vertex.md`
   (goal `G-reduce`, status sketched).

   **CHECKED NEGATIVE (the recursion does NOT hold):** the outer STS's
   *collinearity graph* is **not** itself the collinearity graph of another
   srg(*,*,1,2) — part (c) of G-reduce is refuted on the 243 control.
   `code/out/g_reduce_control.captured.txt` measures on bvls_graph():
   the outer-design collinearity graph (1980 edges, degree 18) has **λ=1 but
   μ in {0:330, 1:11880, 2:9900}** — non-constant. So the vertex-derived
   reduction does **not recurse**: the outer geometry is a genuine partial
   Steiner triple system (a HOLDING, parts (a),(b)) but its collinearity
   graph does not belong to the srg(v,k,1,2) family (a checked negative,
   part (c) FALSE on both controls — on rook(3) the outer design is empty,
   μ undefined). Any argument that would reduce 99 to a constraint on the
   outer design as *its own* srg is therefore closed by the 243 control.

4. **Spectrum** is `3^54 · (−4)^44`: eigenvalues r=3 (multiplicity 54) and
   s=−4 (multiplicity 44), from `x²+x−12=0` with multiplicities computed by
   the integrality formula. Matches Brouwer's table row `? 99 14 1 2 | 3 54 |
   -4 44`. (claim `integrality-five-members`, checked; `brouwer-neumaier-1988-99-open`,
   sourced.)

**The one fact that disciplines every nonexistence argument:** the family has
two *existing* members of the same shape — srg(9,4,1,2) (the 3×3 rook's
graph = Paley(9)) and srg(243,22,1,2) (the Berlekamp–van Lint–Seidel graph from
the perfect ternary Golay code). (claim `c4`, `five-member-list-vanlint1975`,
sourced, and **oracle-verified**: rook(3) is srg(9,4,1,2) and
bvls_graph() is srg(243,22,1,2), confirmed by exact integer common-neighbour
counting in `code/out/oracle_verification.captured.txt` (capture of
`code/out/verify_oracle.py` through `lib/srg.is_srg`).)
Every nonexistence argument must have a step that breaks on both of these, by GOAL.md.

## 2. The family, feasibility, and the current verification/search bound

**The feasible family is exactly five members.** Eigenvalue-multiplicity
integrality, computed in exact integer arithmetic
(`code/out/feasibility-candidates-corrected.md`, claim `integrality-five-members`,
checked), admits exactly:
```
(9,4), (99,14), (243,22), (6273,112), (494019,994)
```
equivalently `k = u²+u+2` with `u ∈ {1,3,4,10,31}` (Makhnev–Minakova 2004
classification, via Cesarz–Woldar). **This CORRECTS problem.md**, whose
candidate list `k = 4, 8, 14, 22, 32, 44, …` named 33, 513, 969 as candidates.
They pass the perfect-square test `4k−7 = □` but fail multiplicity integrality;
the corrected five-member list won. In particular:

- **srg(33,8,1,2) does not exist**, killed by integrality
  (`2k−(v−1) = −16` not divisible by `√25 = 5`). (claims `c2`,
  `srg33-does-not-exist-integrality`, `srg33-mechanism-answers-request`, checked.)
  This is problem.md's "nearest precedent" — and its mechanism is pure
  spectral integrality, which 9, 243, and 99 all pass, so **it gives no weapon
  for 99**. It is a dead end as a structural template, not a template.

**What the largest COMPLETED search actually covered.** The library documents
**no completed full-space search** and no reportable boundary from one.
Specifically:
- Keramatipour's SAT attack (arXiv 2604.23037) reports only the *incapability*
  of SAT solvers on the problem; the abstract gives no search-space size,
  symmetry reduction, or wall-clock numbers — so it adds no reportable boundary
  and confirms enumeration is the wrong method. [summary, asserted]
- The searches that DID complete and are documented are the **orbit-matrix
  automorphism exclusions** (see Section 3) — finite orbit enumerations over
  automorphism groups, which are complete within their stated spaces.
- The honest current frontier: a blind/unbounded search is out of reach and out
  of scope (GOAL.md). No published full-space search through the local 7K₂ /
  triangle geometry with a stated exhaustiveness argument is in the library.
  This run must not reproduce a search nobody completed; the next useful search
  is inside a small stated sub-space with an exhaustiveness argument.

## 3. Restricted classes already settled, with exact hypotheses

All conditional on *existence* of a putative graph Γ with G = Aut(Γ)
(claim `automorphism-orders-consolidated`, asserted-by-source; the three
positive controls below also hold verbatim on the existing 9- and 243-graphs
where stated):

1. **Prime divisors of |G| ⊆ {2, 3}.** (Behbahani–Lam 2011, orbit-matrix
   method; primary-source support in Behbahani 2009 PhD thesis Thm 4.14:
   an order-3 automorphism has NO fixed points.) Hence no automorphism of order
   5, 7, 11. Also `|G|` divides `2·3³·7·11` (Makhnev–Minakova 2004, character
   theory). Sorted: 7 and 11 are out.

2. **No automorphism group Z₆, S₃, Z₉, or E₉** (Crnković–Maksimović 2020,
   computer-assisted orbit matrices; full mechanism in library §7). Combined
   with the above, the order of |G| is `2^a 3^b` with `b ∈ {0,1}`.

3. **If 7 | |G| then G ≅ Z₇**; **if 2 | |G| then |G| | 6** (G ∈ {Z₂, Z₆, S₃})
   (Cesarz–Woldar 2025, computer-free in published form; the arXiv Frob(21)
   elimination is computer-assisted — flagged). Also **no order-14
   automorphism**.

Net: a non-trivial automorphism group, if one exists, is very small (at most
Z₂, Z₃, Z₆, S₃, Z₇, Z₉, E₉, or products thereof within the divisibility bound),
and whether G is trivial is **open**. This means symmetry-assuming construction
searches are effectively dead — which is the structural reason no such search
has produced a graph.

## 4. Which obstruction defeated each previous attempt

Every new approach must beat the same obstruction that closed each of these
`Ruled out` directions:

- **Eigenvalue-only routes (integrality, Krein, absolute bound, interlacing on
  the whole graph):** all survive on 9 and 243, so a 99-nonexistence argument
  that uses only these is refuted on arrival. Integrality admits 99 (f=54,
  g=44 pass). [claim `integrality-five-members`, checked] The 33 precedent is
  *spectral* and cannot transfer.
- **The μ≤2 / Bagchi / Brouwer–Neumaier dichotomy** ("k < 12λ(λ+3) ⇒ grid"):
  does NOT rule out 99. The grid conclusion needs BOTH `k < 12λ(λ+3)` (=48)
  AND `k < (λ+1)(λ+2)` (=6); k=14 fails the second branch (as does k=22 for
  243). The bound that does bind is BN1988's `k ≥ λ(λ+3)/2 = 2`, satisfied by
  14. [claim `c6-resolved-no-bite`, sourced+reasoned]
- **Blind/unbounded search:** the space of 14-regular graphs on 99 vertices
  defeats any solver; Keramatipour confirms the limitation without a boundary.
  Not a proof-theoretic obstruction but the practical one that has kept the
  problem open — the graph (if it exists) is not findable by enumeration, and
  symmetry reduction is largely eliminated by the automorphism results.

**What remains genuinely open** (the attack surface for phase 4): existence
itself; whether G is trivial; any forced/forbidden local configuration beyond
7K₂; a counting identity (induced C₅/C₆/K₄−e counts) that 9 and 243 escape; a
completed exhaustive sub-search with a stated exhaustiveness argument inside
the triangle geometry.
