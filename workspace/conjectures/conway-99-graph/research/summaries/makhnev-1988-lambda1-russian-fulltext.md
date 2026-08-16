# Makhnev 1988 "Strongly regular graphs with λ=1" — PRIMARY SOURCE, full Russian text now in library

<!-- source: https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=rus&paperid=4220&what=fullt -->
<!-- full text: research/sources/makhnev-1988-lambda1-russian-fulltext.full.md -->

**This was the run's single most valuable open gap (LIBRARY-REPORT.md / REQUESTS
falsifier #1). It is now closed from the primary source, in the original
Russian, openly available on mathnet.ru.** The paper: A. A. Makhnev, "О сильно
регулярных графах с λ=1" (On strongly regular graphs with λ=1), Mat.
Zametki 44(5) 667–672 (1988); English translation Math. Notes 44 847–850;
DOI 10.1007/BF01158426. The German/English translation is paywalled but the
Russian original full text is open on mathnet.ru (paperid=4220).

## The condition (*), and the two theorems

Makhnev defines the triangle graph Γ_Δ: vertices = triangles of Γ; two
triangles adjacent iff they share exactly one vertex. He *weakens* strong
regularity of Γ_Δ to the condition:

> **(∗)** any pair of triangles of Γ joined by at least two edges is joined by
> exactly three edges.

This is *exactly* Reimbayev's `n_3 = 0` (n_3 = number of pairs of triangles
joined by two edges). So Reimbayev's citation of Makhnev is a faithful one — the
link is confirmed against the primary text.

**THEOREM 1.** Let Γ be a strongly regular graph with λ=1 satisfying (∗).
Then either μ ≤ 3, or Γ is the unique graph with parameters (27, 10, 1, 5).

**THEOREM 2.** There is no strongly regular graph with parameters (99,14,1,2)
or (115,18,1,3) satisfying (∗). Makhnev explicitly calls Theorem 2 "a partial
answer to Seidel's question on the existence of an srg(99,14,1,2)".

### Proof of Theorem 2 for (99,14,1,2) — the mechanism (from the primary text)
For a triangle A=ABC of Γ, let Γ(A) = [A]∪[B]∪[C] be the closure of A under
neighbours. Since A,B,C are pairwise adjacent and share exactly λ=1 common
neighbour each (with triple intersection empty), |Γ(A)| = 3·14 − 3 = 39
(verified against the primary text: Lemma 6 counts the 36 points of Γ(A)−A
lying in 12 triangles joined to A by exactly 3 edges, so |Γ(A)| = 36+3 = 39).
This is NOT the 9-vertex rook's graph; a 9-point closure would leave 90 points
outside, contradicting Lemma 7's "60 points outside" and 9+60≠99. The "closure
= srg(9,4,1,2) on 9 vertices" phrasing sometimes used in the run is a misreading
(see code/out/check_makhnev_n3_counts.py).  Under (∗):
- Lemma 6: the triangle graph on triangles meeting Γ(A) is edge-regular with
  k_Δ=12, λ_Δ=1.
- Lemma 7: each of the 99−39 = 60 points outside Γ(A) lies in exactly one
  triangle disjoint from Γ(A); so there are 20 such outer triangles.
- Makhnev then shows (Lemmas 8, 9) that these 20 outer triangles + the 12
  meeting Γ(A) + A form a subgraph Λ₀ which is an srg(33, 12, 1, 6) satisfying
  (∗) — the 33 triangle-vertices partition the 3+36+60 = 99 points exactly.
  But an srg(33,12,1,6) has μ=6>3 and is not (27,10,1,5), contradicting
  Theorem 1. Hence no srg(99,14,1,2) satisfying (∗) exists.  Independently,
  srg(33,12,1,6) is parameter-INFEASIBLE by eigenvalue-multiplicity integrality
  (code/out/check_srg33_12_1_6.py), so the forced subobject cannot exist at all.

## What this means for the run — and the negative controls

1. **Reimbayev's load-bearing claim is TRUE, against the primary source.**
   "If n_3 = 0 then no srg(99,14,1,2) exists" is Theorem 2 of Makhnev 1988.
   This upgrades the n_3=0 branch from `asserted-by-source` (Reimbayev's word)
   to `sourced` (primary text in library). The n_3-pivot attack now has a real
   theorem behind it.

2. **Negative controls behave correctly.** Both control graphs have μ=2:
   - rook(3) = srg(9,4,1,2): μ=2≤3, so Theorem 1's first branch absorbs it;
     also k=4=2μ (the degenerate local case). NOT ruled out — correct.
   - BvLS = srg(243,22,1,2): μ=2≤3, absorbed by the same branch. NOT ruled
     out — correct.
   Theorem 2's 99-proof uses k=14-specific counts (60 outer points, 20 outer
   triangles) and produces an srg(33,12,1,6) intermediate with μ_0=6>3 that
   conflicts with Theorem 1. For 9 and 243 the k=2μ / μ≤3 branch holds instead,
   so the mechanism genuinely does not transfer. **The oracle check that rook(3)
   and BvLS satisfy (∗) is written (code/out/check_makhnev_condition.py) and is
   PENDING tool_builder/coder execution** — the admissibility run that GOAL.md
   demands before Theorem 2 is cited as a 99-argument. (Expected on the theory:
   both satisfy (∗) since μ=2≤3; the oracle must confirm.)

3. **The honest cost of the n_3 route.** Makhnev's Theorem 2 converts
   "n_3=0" into "no 99-graph". But n_3=0 is itself NOT established — it is
   Reimbayev's *conjecture* (hexagon bound attained). So the chain is
   Conjecture ⟹ n₃=0 ⟹ (Makhnev Thm 2) no 99 — two conjectures stacked, the
   first of which Reimbayev supports only by "many symmetries". Proving n_3≥1
   would NOT give existence; it only defeats this one route.

```claim
id: makhnev1988-condstar-theorems
statement: Makhnev 1988 (primary Russian full text) proves: under condition
  (*) [any two triangles joined by >=2 edges are joined by exactly 3 edges =
  Reimbayev's n_3=0], a lambda=1 SRG is either mu<=3 or (27,10,1,5) (Thm 1);
  and no srg(99,14,1,2) or srg(115,18,1,3) satisfies (*) (Thm 2). The 99
  proof builds an srg(33,12,1,6) subobject from a triangle's closure and its
  60 exterior points, contradicting Thm 1.
hypotheses: Gamma is srg with lambda=1; condition (*) holds.
holds-here: yes — directly answers REQUESTS falsifier #1 on the n_3=0 branch:
  Reimbayev's citation is correct; the theorem is real.
status: sourced (full Russian primary text of Makhnev 1988 now in
  research/sources/makhnev-1988-lambda1-russian-fulltext.full.md; translated
  above). The oracle verification that rook(3) and BvLS satisfy (*) is pending.
bearing: legitimises the n_3-pivot route as a real theorem-backed leading
  attack; clarifies that n_3=0 is only a conjecture and that proving n_3>=1
  does not give existence.
anchor: research/sources/makhnev-1988-lambda1-russian-fulltext.full.md
answers: makhnev-1988-condstar (the gap previously recorded as fillable by a
  traceable statement of Makhnev 1988's main theorem)
```

## Residual
- Behbahani–Lam–Östergård 2012 "On triple systems and strongly regular graphs"
  (JCTA 119, 1414–1426, DOI 10.1016/j.jcta.2012.03.013) — still paywalled; the
  triple-system/partial-line-space route it serves is relevant to the triangle
  geometry but not load-bearing for the n_3 attack (which Makhnev 1988 now covers).
- Lou & Murin (forbidden 9-vertex subgraph for k=14, per Reimbayev ref [9]) —
  still untraceable in any index; lead only.
