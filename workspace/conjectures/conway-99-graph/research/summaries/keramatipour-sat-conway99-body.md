# Keramatipour, "Approaching the Conway-99 problem using SAT solvers" — FULL TEXT

**Source:** https://arxiv.org/html/2604.23037v1 (arXiv:2604.23037v1, 24 Apr 2026)
**Nature/quality caveat:** This is an **MPhil thesis** (University of Cambridge,
Churchill College, June 2023, supervised thesis; author Ali Keramatipour), an
arXiv preprint, **not peer-reviewed journal work**. Its structural lemmas are
informal but checkable; several are verified below against the run's own
controls. Treat its theorems as claims, not settled results. The bound-99
claims are provable-looking and should be checked if used.
Full text: `research/sources/keramatipour-sat-conway99-body.full.md`.

## What it establishes (claims; see verification notes)

### Paley(9) pattern analysis (Sec 3.4)
- **Definition 12 (Paley(9) pattern):** an `(n,k,1,2)` SRG has the Paley(9)
  pattern when, for every vertex v and every two matched edges
  `{v1,v2},{v3,v4}` of `N(v)`, the induced subgraph
  `{v, v1,v2,v3,v4, (v1,v3),(v1,v4),(v2,v3),(v2,v4)}` is a Paley(9) graph.
  (Notation `(a,b)` = the common neighbour of non-adjacent a,b, well-defined by
  μ=2.)
- **Lemma 3.4.1:** the Paley(9) pattern IS present in the Berlekamp–van Lint–
  Seidel graph srg(243,22,1,2).
- **Theorem 3.4.2:** a putative srg(99,14,1,2) CANNOT follow the Paley(9)
  pattern. Proof is a local forcing argument (λ=1 + μ=2 + 7K2 parallelism);
  the contradiction is that vertices `(1,3,x)` and `(1,3,x')` come to share
  three neighbours `{(1,3),(2,4,y),(2,4,y')}`, violating λ=1/μ=2. Read the
  proof in the full text before relying on it — it is an informal case analysis
  and should be independently verified.
- **Theorem 3.4.3:** no eleven independent Paley(9) subgraphs (proof omitted).
- **Conjecture 3.4.4:** no Paley(9) subgraph at all in a putative
  srg(99,14,1,2). (Conjecture, not proved.)

### Triangular graph analysis (Sec 3.4.3) — VERIFIED against run controls
- **Lemma 3.4.5:** the triangular graph C3(Γ) of an `(n,k,1,2)` SRG Γ (vertices
  = triangles of Γ; edges = triangles sharing a vertex) is
  - `nk/6` vertices,
  - `(3k−6)/2`-regular,
  - every two adjacent (sharing-a-vertex) triangles share exactly `k/2 − 2`
    common neighbours,
  - every two non-adjacent triangles share **at most three** common neighbours.
- Consequently for a putative `(99,14,1,2)`, C3 must be a `(231, 18, 5, ≤3)`
  graph (`nk/6=231`, `(42−6)/2=18`, `k/2−2=5`, non-adjacent ≤3).
- **Observation 3.4.6:** C3 of Paley(9) is K_{3,3} (6 vertices, 3-regular,
  triangle-free).
- The author notes this C3 is NOT strongly regular (λ≠μ in general), matching
  the run's Phillips-2026-based thread `triangle-graph`.

This is exactly the **triangle graph** computed by the run
(`code/out/check_triangle_graph.py`, thread `triangle-graph`), so the lemma is
independently verified on the controls:
- BvLS srg(243,22,1,2), k=22: prediction `(891, 30, 9, ≤3)`; run measured 891
  vertices, 30-regular, **all 26730 adjacent pairs share exactly 9** (=11−2)
  common neighbours, non-adjacent vary `{1:481140, 0:267300, 3:17820}` — all ≤3.
  **Lemma 3.4.5 confirmed exactly on the BvLS control.**
- rook(3) srg(9,4,1,2): C3 = K_{3,3} = srg(6,3,0,3), matching Observation 3.4.6.

## SAT search (Ch 4) — negative method evidence only
The SAT encoding of the Conway-99 search does not terminate usefully; the thesis
reports the **incapability of SAT solvers** on the problem and the mathematical
reasons for it. No search-space size, symmetry reduction or wall-clock boundary
is reported, so it adds no reportable boundary — consistent with the run's
standing that a blind search is the wrong method. (Confirmed by the run's own
failed sat_solver attempt, agent-run-81 ref in thread `n3-forced`.)

## Implication for this run
- The **Paley(9)-pattern theorem 3.4.2** is a genuinely 99-specific local
  forced/forbidden configuration — a candidate for the run's "forced or
  forbidden local configuration" deliverable. Its proof uses exclusively
  λ=1, μ=2, and the 7K2 local structure, and its contradiction is that two
  vertices would share three common neighbours. It does NOT obviously break on
  rook(3) (which IS Paley(9), c7+7K2, k=4) — the k=14 arithmetic enters where
  vertex 5 needs two neighbours in each N_{1,3} etc. Worth an independent
  verification pass before use, since it is claimed to rule out a configuration
  that the (9,4,1,2) member itself realises only at its own k.
- The **triangular-graph constraint `(231,18,5,≤3)`** is a new, verified
  structural fact about a putative 99-graph's triangle graph, consistent with
  the run's own C3 computation and Phillips-2026. The non-adjacent-triangle
  shared-neighbour count at BvLS is `{1:481140,0:267300,3:17820}`; whether a
  99-graph's C3 must hit the extreme values and whether that forces a counting
  contradiction is open.
- The author's "triangular view" (triangles adjacent iff sharing a vertex) is
  the SAME object as Makhnev's triangle graph Γ_Δ and the run's C3 — NOT the
  n_3 configuration. Do not conflate (n_3 = pairs of triangles joined by
  exactly 2 edges).

#claim-block
```claim
id: keramatipour-paley9-pattern-holds-on-controls
statement: Lemma 3.4.1's Paley(9) pattern (Definition 12: for every vertex v
  and every two matched edges {v1,v2},{v3,v4} of N(v), the 9-vertex induced
  subgraph on {v, v1..v4, and the four common neighbours of the cross pairs}
  is Paley(9)) is CONFIRMED present on BOTH existing controls: rook(3) =
  srg(9,4,1,2) (9 pattern-configurations, all Paley(9)) and bvls = srg(243,22,1,2)
  (13365 configurations, all Paley(9)), exact check.
hypotheses: srg(v,k,1,2); the Paley(9) pattern as in Keramatipour Def 12.
holds-here: yes on both controls. Contrast: Theorem 3.4.2 (asserted-by-source,
  unchecked) says a putative (99,14,1,2) CANNOT follow the pattern. Since the
  pattern holds on the k=4 and k=22 members, Theorem 3.4.2's claim is a genuine
  k=14-specific separator ONLY IF its proof genuinely uses a k=14 dependence
  absent at k=4,k=22 — the thesis proof is informal and must be independently
  verified before it is used as a 99-forbidden-configuration deliverable.
status: checked (this run's exact computation, code/out/paley9_pattern_check_fixed.captured.txt).
bearing: confirms the control-side of the Paley(9) pattern line; marks
  Theorem 3.4.2 as the candidate 99-specific forbidden configuration whose
  soundness (does it rule out rook(3)?) is the open verification.
anchor: research/sources/keramatipour-sat-conway99-body.full.md
```

```claim
id: keramatipour-trian-graph-nk6-3k-6-2
statement: The triangular graph C3(Gamma) of an (n,k,1,2) strongly regular
  graph Gamma (vertices = triangles, edges = triangles sharing a vertex) has
  nk/6 vertices, is (3k-6)/2-regular, every two adjacent triangles share k/2-2
  common neighbours, and every two non-adjacent triangles share at most three
  common neighbours (Lemma 3.4.5, Keramatipour 2023 thesis).
hypotheses: Gamma is srg(n,k,1,2); triangles counted as 3-cliques.
holds-here: yes — prediction for the family member reproduced exactly on both
  controls by this run's own computation (BvLS: 891 vtx, 30-regular, adjacent
  pairs all share 9 = 11-2 common neighbours, non-adjacent share in {0,1,3};
  rook(3): C3 = K_{3,3} = srg(6,3,0,3)). At n=99,k=14 the lemma forces a
  (231, 18, 5, <=3) triangle graph.
status: asserted-by-source (thesis), but the nk/6 and (3k-6)/2 and k/2-2 parts
  are verifiable counting facts and were confirmed on the run's controls; the
  "<=3 non-adjacent" part is a short argument reproduced in the thesis proof
  and confirmed on BvLS.
bearing: gives the run's triangle-graph lead a concrete family-uniform
  structural constraint on a putative 99-graph's triangle graph; consistent
  with the Phillips-2026-based thread triangle-graph (C3 not strongly regular),
  and a candidate host for a 99-specific counting identity.
anchor: research/sources/keramatipour-sat-conway99-body.full.md
```

```claim
id: keramatipour-no-paley9-pattern-99
statement: A putative srg(99,14,1,2) cannot contain the Paley(9) pattern
  (Definition 12: for every vertex v and matched pair of N(v)-edges the 9-vertex
  induced subgraph is Paley(9)) — Theorem 3.4.2, Keramatipour 2023 thesis. The
  proof forces a 9-vertex local structure from lambda=1, mu=2, 7K2 parallelism
  until two vertices would share three common neighbours, a contradiction.
  (Conjecture 3.4.4 extends this to: no Paley(9) subgraph at all.)
hypotheses: Gamma is srg(99,14,1,2); the Paley(9) pattern as defined.
holds-here: not yet independently checked; the thesis proof is an informal case
  analysis and the pattern is realizable at the k=4 member (rook(3)=Paley(9)
  itself) where the k=14 counting that drives the contradiction is absent.
status: asserted-by-source (unrefereed thesis); flagged for independent
  verification before any reliance.
bearing: candidate 99-specific forbidden local configuration, in the shape the
  run's deliverable (forced/forbidden local structure) asks for; but it must be
  verified and checked that it does not also rule out rook(3) under an
  invalid-for-k=4 step.
anchor: research/sources/keramatipour-sat-conway99-body.full.md
```
