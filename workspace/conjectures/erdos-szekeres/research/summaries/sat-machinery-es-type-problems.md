# SAT machinery for ES-type problems (four sources)

This note consolidates the four computational/SAT sources; each has its own claim blocks.

## Scheucher 2024, https://arxiv.org/pdf/2105.08406 — [[scheucher - A SAT Attack on Erdos-Szekeres Numbers in Rd and the Empty Hexagon Theorem full.full]]

SAT model on **acyclic chirotopes** (oriented matroids) — orientation variables with the
signature/transitivity axioms, UNSAT verified by DRAT certificates. Hierarchy results:
$g^{(3)}(7)=13$, $g^{(4)}(8)\le13$, $g^{(5)}(9)\le13$ (higher-dim ES numbers), and k-hole bounds
$h^{(3)}(7)\le14$ etc. Sharp in the acyclic-chirotope category. **This is the orientation-variable
SAT formulation the run should mirror for any planar ES(7) question**, and it supplies the
higher-dim adjacent-problem numbers that must be kept out of the planar claim.

```claim
id: scheucher-sat
statement: The acyclic-chirotope SAT model (orientation variables + transitivity) with DRAT-certified UNSAT computes higher-dimensional ES and hole numbers (g^(3)(7)=13, g^(4)(8)<=13, g^(5)(9)<=13).
hypotheses: higher dimensions d>=3
holds-here: no (adjacent problem; planar ES is d=2, and these numbers do not transfer)
status: proved (with DRAT certificates)
bearing: template for a planar SAT encoding to reproduce ES(5)=9 / ES(6)=17 before trust; the chirotope axioms are exactly the ones Peters–Szekeres use.
anchor: research/sources/scheucher - A SAT Attack on Erdos-Szekeres Numbers in Rd and the Empty Hexagon Theorem full.full.md
```

## Heule & Scheucher 2024, https://arxiv.org/pdf/2403.00737 — [[heule-scheucher - Happy Ending An Empty Hexagon in Every Set of 30 Points - 2024 full.full]]

Empty-hexagon number $h(6)=30$: every 30-point set contains an empty convex hexagon. Compact CNF
with $O(n^4)$ clauses, search-space partitioning giving linear speedup on thousands of cores,
17300 CPU hours. (Empty hexagon = a convex 6 points with no other point inside — the Ehrdős–Szekeres–Horton
problem, DIFFERENT from ES(6)=17 which does not require emptiness.) Keeping the two apart is
explicit GOAL.md guidance.

```claim
id: heule-scheucher-empty6
statement: Every 30-point planar set in general position contains an empty convex hexagon; h(6)=30.
hypotheses: planar general position; 'empty' means a convex hexagon with no point inside
holds-here: no (adjacent empty-hexagon problem, not ES(6))
status: proved (SAT + DRAT, 17300 CPU hours)
bearing: state of the art in SAT for a bounded geometric configuration; the encoding/partitioning technique is reusable, but the empty-hexagon result itself is NOT the ES result and must not be reported as such.
anchor: research/sources/heule-scheucher - Happy Ending An Empty Hexagon in Every Set of 30 Points - 2024 full.full.md
```

## Subercaseaux et al. 2024, https://arxiv.org/pdf/2403.17370 — [[subercaseaux-et-al - Formal Verification of the Empty Hexagon Number - ITP 2024 full.full]]

Lean 4 formalization of the empty-hexagon SAT proof, and tools connecting planar geometry to
propositional assignments; covers the ES encoding too. Directly the model for GOAL.md criterion 5
(the Lean file carrying the formal statement of ES(n) and the conjecture). Confirms the
orientation-variable formalism is Lean-friendly.

## Dumitru 2025, https://arxiv.org/pdf/2512.24061 — [[dumitru-notes-on-33-point-esz-arxiv2512.24061.full]]

The live ES(7) frontier. SAT encoding for the 33-point case (ES(7)=33): triple-orientation
variables, **4-set convexity criterion** (S in convex position iff every 4-subset is), no-convex-
7-gon constraint, convex-layer (hull-template) anchoring, and a sub-cubing parameter pinning
relative layer alignment. Gives UNSAT certificates for anchored subfamilies; heavy-tailed runtime,
some subproblems weeks on commodity hardware.

```claim
id: dumitru-es7
statement: There is a triple-orientation + 4-set-criterion + convex-layer-anchoring SAT encoding for ES(7); it yields UNSAT certificates for anchored subfamilies but does NOT settle ES(7) (no full 33-point UNSAT; runtime is heavy-tailed and currently dominant).
hypotheses: 33-point planar sets, general position
holds-here: yes
status: asserted (reports UNSAT certificates for anchored subfamilies; full ES(7) open)
bearing: the concrete next computational frontier; the 4-set criterion and layer-anchoring are directly reusable. An empty result only rules out the anchored subfamilies tested, NOT ES(7).
anchor: research/sources/dumitru-notes-on-33-point-esz-arxiv2512.24061.full.md
```

## Implication for the run

Any SAT/CP-SAT question the argument throws off must first reproduce a known answer with the *same*
encoder (ES(5)=9 minimum; ideally ES(6)=17 on 16 points). The 4-set convexity criterion is the
compact way to state "no convex k-gon" in Boolean terms, exactly as in these papers.
