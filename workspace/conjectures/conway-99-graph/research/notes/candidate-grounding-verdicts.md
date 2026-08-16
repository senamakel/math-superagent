# Candidate line-of-attack grounding — literature verdicts

Per the research-specialist task and the inventor's three proposals. Each candidate
was taken to the literature (search from several angles: named theory, named object,
standard reference treatment). Status set in `research/approaches/*.md`; this note
holds the sharper reasoning and the URLs.

## 1. incidence-code-of-triangle-geometry — GROUNDED, computationally unresolved

Object: point-block incidence matrix N (99x231) of the triangle geometry; p-ranks,
hull, SNF. Named theory: Assmus–Key "Designs and their Codes"; STS p-rank.

- The p-rank of an STS genuinely varies with the system, so N is NOT a
  spectrum-determined invariant like the two refuted A-based routes.
  - Assmus, "On 2-ranks of Steiner triple systems", Electron. J. Combin. (1995),
    https://doi.org/10.37236/1203 : for STS of deficient 2-rank the "carrier"
    code depends on order AND 2-rank.
  - Bonisoli, Designs Codes Crypt. 8 (1996) 29-43,
    https://link.springer.com/article/10.1007/BF00130567 : binary code spanned by
    the point-by-block incidence matrix of an STS; classical STS characterized by
    their codes.
  - Shi, Xu, Krotov, J. Combin. Des. (2019), https://doi.org/10.1002/jcd.21663 :
    number of STS(v) of given 2-rank r2<v and 3-rank r3<v-1; no STS has both
    r2<v and r3<v-1 — both ranks discriminating.
  - Haemers, Peeters, van Rijckevorsel, "Binary Codes of Strongly Regular Graphs"
    (1998), https://research.tilburguniversity.edu/en/publications/dca56971-63a6-4942-b8f7-5a3ddc69ae31 :
    p-ranks of incidence/adjacency of designs and SRGs are "often, but not always,
    determined by the parameters".

DECISIVE STEP IS A COMPUTATION: rank_2(N), rank_3(N), SNF(N) for the two controls
(rook: 9x6; bvls: 243x891). Not in the literature. If the two controls give the
SAME ranks, the invariant is parameter-determined and the approach reverts to
refuted (same verdict as macwilliams/higman). If they differ, it is live and the
99-value is the next question. **No execution tool in this run**, so this is a
concrete first-step for a later coding pass, not a conclusion.

## 2. least-eigenvalue-minus-4-structure — GROUNDED, mechanism PARTLY does not fire

Object: graphs with least eigenvalue exactly -4. Named theory: CGSS (least
eigenvalue >= -2 => generalized line graph), Woo–Neumaier Hoffman-graph, and the
geometric-SRG / -m classification programmes.

- The -4 gate IS genuinely 99-specific: rook(3) least eigenvalue -2, BvLS(243)
  least eigenvalue -5, srg(99,14,1,2) would be -4. No refuted parameter-driven
  route separates the three this way.
- Neumaier's geometric-SRG dichotomy (as surveyed in Koolen–Cao–Yang, arXiv:2011.11935,
  Thm 5.1): a primitive SRG with smallest eigenvalue -lambda is geometric
  (Latin-square or Steiner family) if (lambda+1)(a+1) - k > (c-1)(lambda+1)/2.
  At (99,14,1,2): lambda (magnitude) = 4, a=lambda=1, c=mu=2, k=14.
    LHS = (4+1)(1+1) - 14 = 10 - 14 = -4
    RHS = (2-1)(4+1)/2 = 5/2 = 2.5
    -4 > 2.5 is FALSE. HYPOTHESIS FAILS at 99, so the geometric classification
  does NOT fire. The "dichotomy forces a family" mechanism is grounded for the
  parameter ranges it covers but explicitly does not cover 99.
- Greaves, Koolen, Park, "Improving the Delsarte bound" (arXiv:2012.09391): the
  right living repertoire — Delsarte bound + cubic maximal-clique constraint +
  claw-bound, used to RULE OUT infinite families of feasible SRG parameters with
  smallest eigenvalue -4,-5,-6,-7, with explicit nonexistence tables. (99,14,1,2)
  is not excluded there (remains open), but the tables should be checked directly.
- FORBIDDEN-induced-SUBGRAPH basis for the class "smallest eigenvalue >= -4" is
  REFUTED outright: Birkhoff–Jiang–Polyanskii, arXiv:2111.10366, sharp threshold
  lambda* ~ 2.0198. The class graphs-with-min-eigenvalue >= -lambda has a finite
  forbidden-induced-subgraph characterization iff lambda < lambda*. lambda=4
  exceeds it, so -4 admits NO finite forbidden-subgraph basis, and -4 is itself a
  limit point of smallest eigenvalues. Any plan to "list the forbidden subgraphs a
  -4 regular graph must avoid" is dead in the water.

Verdict: gate is live and 99-specific; the specific forced-substructure mechanism
described in the proposal (CGSS/Woo–Neumaier dichotomy => forced subgraphs) does
not fire at 99; the sound-remaining weapon is the Greaves–Koolen–Park Delsarte/
claw/cubic arsenal with its -4 nonexistence tables, plus the -m=-4 geometric-SRG
classification literature (van Dam, Koolen–Yang, Spence), where 99 is plausibly an
open case.

## 3. spread-resolvable-partial-sts — GROUNDED as a class, literature gives no 99-answer

Object: resolvability (7 spreads x 33 disjoint triangles covering 99 points) of the
partial STS.

- Ray-Chaudhuri & Wilson (Proc. Sympos. Pure Math. XIX, 1968): a KTS (resolvable
  STS) exists iff v = 3 (mod 6). The NAMED existence theorem — but it governs
  FULL STS (every point pair on a block). The 99 triangle geometry is PARTIAL
  (replication 7, only adjacent pairs joined by a line), so the hypothesis fails
  and the theorem gives no direct bound. v=99 = 3 mod 6 is consistent, nothing more.
- Stinson, "On partial parallel classes in partial Steiner triple systems",
  Discrete Math. 344 (2021), DOI 10.1016/j.disc.2020.112279 : the exact named
  framework — partial parallel classes (PPC) in PARTIAL STS, beta(rho,v) bounds.
  Right vocabulary for a spread of 33 disjoint blocks; no v=99 / mu=2 pin.
- Colbourn, Magliveras, Mathon (Math. Comp. 1992), DOI 10.1090/S0025-5718-1992-1106962-5 :
  the computational method the proposal's first-step suggests — block-nonintersection
  graph (vertices = blocks, edges = disjoint), parallel classes read off as cliques.
  Standard and applicable on exactly this object shape (99 -> 231 nonintersection-graph
  vertices).
- Buratti & Pasotti, "Heffter Spaces" (arXiv:2401.03940): resolvable partial linear
  spaces; collinearity graph of a resolvable PLS is regular of degree = sum of block
  sizes. A live construction framework, not specialized to mu=2.

Verdict: the reformulation is a real, named class and no dead end is known, but the
literature supplies neither an answer nor a positive mu=2 pin. Whether even ONE
spread exists in a putative srg(99,14,1,2) is open. The novel lever (parity/congruence
on the spread number 7 and block count per spread 33, coupled by mu=2) is unstated
in the literature and is a computation this run's first-step must do: count spreads
in rook(3) (spreads of 3) and bvls(243) (spreads of 81) first.

## Cross-cutting note

All three verdicts are `grounded` (supported-as-a-class / mechanism live) rather
than `refuted`, but each demands a decisive computation the literature does not
supply. None of the three is a finished 99-obstruction; each is a concrete next
first-step for a coding pass. The one outright refutation found is the forbidden-
subgraph basis for -4 graphs (BJP threshold).
