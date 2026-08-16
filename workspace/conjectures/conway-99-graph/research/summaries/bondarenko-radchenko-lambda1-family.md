# Bondarenko & Radchenko, "On a family of strongly regular graphs with λ=1" (arXiv:1201.0383 / JCTB 2013) — FULL TEXT

<!-- source: https://arxiv.org/pdf/1201.0383 | full text at research/sources/bondarenko-radchenko-lambda1-family.full.md -->

## What the paper proves

A **complete classification** of the subfamily of srg with λ=1 whose negative
eigenspace dimension equals the valency (g = k). Their parameter family is
```
((n² + 3n − 1)², n²(n + 3), 1, n(n + 1)),   n ≥ 0
```
(This is exactly the λ=1 family with g=k; for reference, the Conway-99 family
srg(v,k,1,2) has g = k−... which is different.)

**Theorem 1:** such an SRG exists iff n ∈ {1, 2, 4}, giving exactly:
- n=1: **L₃,₃** = 3×3 lattice graph = srg(9,4,1,2) (the rook's graph / Paley 9)
- n=2: **Brouwer–Haemers** graph = srg(81,20,1,6)
- n=4: **Games** graph = srg(729,112,1,20), and Theorem 2 proves it unique up to
  isomorphism.

**Method (of value as a template):** prove vertex-transitivity of Aut, derive a
vector-space structure over F₃ on the vertex set (via involutions σ_u indexed by
vertices satisfying (σ_v σ_w σ_u)² = e), conclude |V| is a power of 3, then solve
the Diophantine equation to get n ∈ {1,2,4}.

## Relation to (99,14,1,2)

The (99,14,1,2) case is **NOT in this subfamily** — it has g = 44, k = 14,
g ≠ k, so this theorem does not touch 99. Its value is:
1. A complete λ=1 classification method (vertex-transitivity ⟹ F₃ vector space
   ⟹ power-of-3 ⟹ Diophantine) — the kind of structural template GOAL.md wants.
2. Confirms the two "easy" existence controls: L₃,₃ (9,4,1,2) and BvLS
   (243,22,1,2) belong to λ=1 families with clean structure, while 99 is the
   odd one out without g=k.
3. Proves uniqueness of the Games graph (729,112,1,20) — one of the five-member
   family's big members gets uniqueness.

## History / relation to Makhnev 1988
The paper's λ=1 classification is exactly the topic of Makhnev 1988 ("Strongly
regular graphs with λ=1"), whose primary Russian full text is now in the library
(`research/sources/makhnev-1988-lambda1-russian-fulltext.full.md`, open on
mathnet.ru; the English Springer translation is paywalled). This arXiv full text
is a peer-reviewed (JCTB 2013) classification of a λ=1 subfamily and stands as
a freely-held λ=1 structural reference alongside the in-library Makhnev 1988
original.

## Status / correction record
- **CORRECTED DOWNLOAD**: an earlier attempt with guessed arXiv id 1303.3164
  fetched a wrong entity-search paper (Sawant & Chakrabarti). Correct id is
  1201.0383, verified against the abstract/title before reliance. This re-fetch
  overwrote the wrong file. Lesson (matches the library's existing safety rule):
  never guess an arXiv id from the DOI; look up the id first.
- Status: peer-reviewed (JCTB 103 (2013) 561-567, DOI 10.1016/j.jctb.2013.05.005).
  Classifications are asserted-by-source here; the run has not re-derived the
  Diophantine/uniqueness arguments.

```claim
id: bondarenko-radchenko-lambda1-gk
statement: The subfamily of srg with lambda=1 and negative-eigenspace dimension
  g=k, parameters ((n^2+3n-1)^2, n^2(n+3), 1, n(n+1)), consists exactly of
  L_{3,3} (9,4,1,2) for n=1, the Brouwer-Haemers graph (81,20,1,6) for n=2,
  and the Games graph (729,112,1,20) for n=4 (unique). n in {1,2,4} only.
hypotheses: srg with lambda=1 and g=k (negative-eigenspace dimension equals
  valency); the parameter family.
holds-here: yes lambda=1, but (99,14,1,2) is NOT in this subfamily (g=44 != k=14),
  so this does not decide 99. Provides the vertex-transitive -> F3 vector space
  -> power-of-3 -> Diophantine method as a classification template.
status: asserted-by-source (peer-reviewed JCTB 2013; classification not
  re-derived here).
bearing: a complete lambda=1 subfamily classification and a reusable method;
  the two controls L33 and BvLS sit in clean lambda=1 families while 99 does
  not fit g=k. Not a 99 decision.
anchor: research/sources/bondarenko-radchenko-lambda1-family.full.md
```
