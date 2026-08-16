# Reimbayev, "Nonexistence of srg(19,6,1,2): Combinatorial Proof" (arXiv:2511.06569, Nov 2025)

<!-- source: https://arxiv.org/html/2511.06569v1 -->
<!-- full text: research/sources/reimbayev-srg19612-combinatorial.full.md -->

A **purely combinatorial** (no spectrum) proof that there is no srg(19,6,1,2),
the smallest nonexistent member of the λ=1, μ=2 family. Puts the family in
order: K₃ (k=2) and Paley(9) (k=4) exist; k=6 (v=19) does not; k=8 (v=33) fails
Integrality; the surviving integrality-passing cases, in the paper's own words,
are "k = 14, 22, 112, 994" — of which **only k=22** (BvLS 243) is known to
exist and "for the other ones the question of existence has not been resolved."
So the paper's framing independently confirms: (99,14,1,2) is one of exactly
four integrality-surviving unresolved sets. (This agrees with the five-member
list but notes K₃(v=3,k=2) and Paley(9) as the small existing members; 33 is
the k=8 integrality-failure.)

## The combinatorial mechanism (a template, worked at 19)

Fix a triangle {a,b,c}. Define A,B,C = neighbours of a/b/c except the triangle
vertices, and W = rest (distance 2). For srg(19,6,1,2): |A|=|B|=|C|=|W|=4.
Steps:
1. G[W] is empty; each w∈W is adjacent to exactly 2 vertices in each of A,B,C.
   Triangle count: 12 W-based + 7 through {a,b,c} = all 19 (=nk/6=19), so
   **G[A∪B∪C] has no triangles**.
2. Nonadjacent μ=2 forces a bijection f:A→B (each ã∈A has a unique b̃∈B with
   ãb̃∈E; two such b̃'s would give ã and b three common neighbours). Similarly
   B→C, C→A. So G[A∪B∪C] is 3-regular and decomposes into cycles of length
   3,6,9,12; 3 and 9 are impossible (no triangles in the 3 case; C9+C3+chords
   in the 9 case), leaving **C6+C6** or **C12**.
3. Case 1 (C6+C6): each of the 6-cycle edges is the base of a triangle with a
   third vertex on W. Assigning the 4 W-vertices to the six triangle bases to
   keep every edge in exactly one triangle runs out of W-vertices → impossible.
4. Case 2 (C12): the forced W-assignment leaves two W-vertices w₁,w₄
   nonadjacent (G[W] empty) but with three common neighbours a₁,b₂,c₃,
   contradicting μ=2.

**This is an explicit local-configuration contradiction at 19.** Its steps
(empty W, the f:A→B μ=2 bijection, per-edge triangle-uniqueness, run-out of
W-vertices) are exactly the "forced extension of a pair of intersecting
triangles" and local-extension machinery GOAL.md names. At 99 the analogue needs
the partition A,B,C (each of size k−2 = 12), W of size v−1−3(k−1) = 99−1−39=59,
and many more lines; the bijection and triangle-uniqueness arguments should
transfer in outline but the case split (C6+C6/C12) is specific to v=19.

## What it establishes for this run
- A clean, short, **spectrum-free** nonexistence for a nearby member — evidence
  that the local-extension route can close a λ=1,μ=2 case without eigenvalues.
- Independent confirmation of the family order and that (99,14,1,2) is open.

## Status / caution
- arXiv preprint (Nov 2025), not peer-reviewed; proof read and summarised from
  the full text, not machine-checked here. The mechanism is sound-looking (no
  spectral step) but is asserted-by-source as the run has not re-derived v=19.

```claim
id: reimbayev-19612-combinatorial-proof
statement: srg(19,6,1,2) does not exist, by a spectrum-free local argument:
  fix a triangle, partition the other 16 vertices into A,B,C (4 each) and W (4
  each); G[W] empty, W-vertices each meet 2 of A/B/C, total triangle count
  forces G[A∪B∪C] triangle-free; mu=2 forces bijections A->B->C->A making it
  3-regular (C6+C6 or C12); the requirement that every edge lie in exactly one
  triangle then exhausts the 4 W-vertices (C6+C6) or leaves two nonadjacent W
  vertices with 3 common neighbours (C12) — contradiction. Paper also states
  the integrality-surviving unresolved family is k in {14,22,112,994} with only
  k=22 (BvLS) known to exist.
hypotheses: srg(v,k,1,2) existence; elementary common-neighbour counting.
holds-here: yes as method template (lambda=1,mu=2 local extension at small v);
  does not decide 99 (k=14, v=99, W of size 59, different case structure).
status: asserted-by-source (arXiv preprint, not peer-reviewed; not re-verified
  here). The family-order/29 statements in it are consistent with the library's
  five-member list and K3(k=2), Paley9(k=4) as the small existing members.
bearing: a distillable spectrum-free local-extension contradiction at v=19, and
  independent confirmation that (99,14,1,2) is among exactly four unresolved
  integrality-surviving sets; the f:A->B mu=2 bijection and per-edge
  triangle-uniqueness are reusable lemmas.
anchor: research/sources/reimbayev-srg19612-combinatorial.full.md
contradicts: none; consistent with c1 (five-member list), integrality-five-members
```

[[reimbayev-srg19612-combinatorial.full]]
