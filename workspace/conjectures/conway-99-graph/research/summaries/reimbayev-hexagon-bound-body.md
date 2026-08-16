# Reimbayev, "The Lower Bound for Number of Hexagons in SRGs with λ=1 and μ=2" (arXiv:2409.10620) — FULL TEXT

<!-- source: https://arxiv.org/html/2409.10620v1 | full text at research/sources/reimbayev-hexagon-bound-body.full.md -->

## What the paper establishes (body now in library)

Works in the whole family srg(v,k,1,2) = (9,4),(99,14),(243,22),(6273,112),(494019,994).
Derives, by counting 6-vertex induced subgraphs against the coefficients of the
characteristic polynomial, a **lower bound on the number of hexagons (C₆)**:

```
n_12 >= (1/12)·n·k·(k−2)·(2k²−21k+53)
```

where n_12 is the number of hexagons. This is Theorem 2. The bound is achieved
exactly when n_3 = 0, where **n_3 is the number of pairs of triangles joined by
two edges** ("two triangles connected through two edges").

## The key consequence for (99,14,1,2)

The paper asserts (Section 4 / Conjecture): **if the hexagon count meets this
lower bound (equivalently n_3 = 0), then, given such condition, Makhnev has
proved srg(99,14,1,2) does not exist** [Makhnev 1988, ref [4] in the paper =
Makhnev, "Strongly regular graphs with λ=1", Mat. Zametki 44(5) 667-672 (1988),
Engl. trans. Math. Notes 44 847-850]. The conjecture is that the lower bound is
tight for the whole family; both known graphs srg(9,4,1,2) (Paley 9) and
srg(243,22,1,2) (BvLS) attain the lower value.

**This is a CONDITIONAL statement, not a proof of nonexistence.** Existence of
(99,14,1,2) remains open; the condition n_3 = 0 (or hexagon bound attained) may
or may not hold for a putative graph. The value of this paper is the **precise
structural pivot n_3**: a single parameter governing all order-6 subgraph counts.

## What the run should take from it

1. The counting-identity attack surface is concrete: n_3 is the parameter to
   attack. If one could show n_3 = 0 for any putative (99,14,1,2), then the
   Makhnev conditional would rule it out.
2. n_3 = "two triangles joined by two edges" is exactly the "union of two
   intersecting/adjacent triangles" configuration named in GOAL.md's local-
   structure candidates.
3. **Sourced since the first digest:** the Makhnev 1988 conditional is no
   longer on Reimbayev's word alone. The primary Russian full text is now in
   the library (`research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`,
   open on mathnet.ru paperid=4220); its Theorem 2 is exactly "no
   srg(99,14,1,2) satisfies (*) = n_3=0", and its mechanism builds an
   srg(33,12,1,6) subobject. See summary
   `makhnev-1988-lambda1-russian-fulltext.md` and claim
   `makhnev1988-condstar-theorems`. What remains genuinely open is n_3=0
   itself (Reimbayev's conjecture), not the conditional's truth.

## Verification bounds in the paper
c₆ values computed for the five members (n,k) = (9,4),(99,14),(243,22),(6273,112),
(494019,994) in Table 3 (e.g. c₆(99,14) = −47,288,703), computed in Julia/Wolfram,
presented without the program. Treat those numeric c₆ values as `asserted-by-source`
pending the run's own exact recomputation.

```claim
id: reimbayev-hexagon-bound-n3-pivot
statement: In any srg(v,k,1,2), the number of hexagons is at least
  (1/12) n k (k-2)(2k^2 - 21k + 53) (Theorem 2), attained iff n_3 = 0, where
  n_3 counts pairs of triangles joined by two edges. If n_3 = 0 then, per
  Makhnev 1988 Thm 2 (primary Russian full text in library), srg(99,14,1,2)
  does not exist. Verified: on both controls rook(3) and BvLS the identity
  n12 = formula + n3 holds exactly with n3 = 0 (checked).
hypotheses: srg(v,k,1,2); the five-member family; the c6/hexagon-counting
  derivation in the paper.
holds-here: yes for (99,14,1,2) — gives the concrete parameter n_3 to attack.
status: asserted-by-source for the bound derivation (arXiv preprint, not
  peer-reviewed); the Makhnev conditional is now sourced (claim
  makhnev1988-condstar-theorems) from the primary Russian text; the identity
  and n3=0 on the controls are checked by this run's exact computation.
bearing: turns GOAL.md's "counting identity" candidate into the single
  parameter n_3 = pairs of triangles joined by two edges; if n_3=0 could be
  forced, the Makhnev conditional (Thm 2) would rule out 99. n_3=0 is itself
  only a conjecture; proving n_3>=1 would not give existence.
anchor: research/sources/reimbayev-hexagon-bound-body.full.md
follows-from: makhnev1988-condstar-theorems
```
