# The 99 case of Makhnev 1988 Thm 2 has a shorter proof — verified in exact arithmetic

The strongest verified result of this run: the subobject Makhnev Thm 2 forces at
(99,14,1,2) under condition (*) [n3=0] is srg(33,12,1,6), and that parameter set
is INFEASIBLE by plain eigenvalue-multiplicity integrality alone.

## The forced-subgraph chain (anchors)

Both captures are in `code/out/`:

- `check_makhnev_n3_counts.captured.txt` reconstructs Lemmas 6–9 arithmetically at
  (99,14,1,2) from the primary Russian text:
  - the closure Γ(A) = [A]∪[B]∪[C] of a triangle A has **39** points
    (= 3·14 − 3; Lemma 6 counts the 36 points of Γ(A)−A in 12 inner triangles);
  - the 99 − 39 = **60** outside points each lie in exactly one triangle disjoint
    from Γ(A) (Lemma 7), giving **20** outer triangles;
  - the 1 (A) + 12 (inner) + 20 (outer) = **33** triangle-vertices partition the
    3 + 36 + 60 = **99** points and form the claimed subobject Λ₀ = **srg(33,12,1,6)**.
  - VERDICT: corrected primary-source counts are internally SELF-CONSISTENT (True).
- `check_srg33_12_1_6.captured.txt` computes standard feasibility of (33,12,1,6):
  - eigenvalues 1, −6 (δ = 49, √δ = 7);
  - the multiplicity numerator `2k + (v−1)(λ−μ) = 24 + 32·(−5) = −136` is **not
    divisible by 7**, so the multiplicity g is non-integral;
  - VERDICT: srg(33,12,1,6) is **INFEASIBLE by multiplicity integrality**.
  - Contrast rows: (27,10,1,5) FEASIBLE and exists (Thm 1's exception: r=1,s=−5,
    f=6,g=20, all integers); (9,4,1,2),(99,14,1,2),(243,22,1,2) all FEASIBLE;
    (33,8,1,2) INFEASIBLE (consistency, same mechanism, −16 not ÷ 5).

## What this upgrades

Makhnev's published text rejects Λ₀ via **Thm 1** (a λ=1 srg satisfying (*) is
μ≤3 or the unique (27,10,1,5); Λ₀ has μ=6>3 and is not (27,10,1,5)). This run
rejects Λ₀ **directly by multiplicity integrality** — a strictly simpler,
self-contained route that does not need Thm 1 at all. So the 99 case of Thm 2
("no srg(99,14,1,2) satisfies (*) [n3=0]") has a shorter proof than the published
one, verified here in exact integer arithmetic.

Status labels:
- the lemma chain (39 / 12 inner / 60 outside / 20 outer / 33-point partition):
  **sourced** (primary Russian text, Lemmas 6–9) — the *count layer* of Lemmas 8–9
  (the Λ₀ parameters (33,12,1,6) and that it satisfies (*)) was not independently
  re-derived here, only the arithmetic;
- the infeasibility of (33,12,1,6): **checked** (exact integer run).

This asserts **nothing** about existence of srg(99,14,1,2). It only records that
Makhnev's n3=0 mechanism rests on a genuinely infeasible intermediate, and that
the infeasibility is visible by integrality alone.

```claim
id: makhnev-lambda0-1331216-infeasible-integrality
statement: The sub-parameter-set srg(33,12,1,6) — the subobject Makhnev 1988
  Thm 2 forces at (99,14,1,2) under condition (*) [n3=0] from a triangle's
  closure and its 60 exterior points — is INFEASIBLE by eigenvalue-multiplicity
  integrality: the g numerator 2k+(v-1)(lam-mu) = -136 is not divisible by
  sqrt(delta) = 7. Hence the 99 case of Makhnev Thm 2 has a shorter proof than
  the published one (which uses Thm 1: mu=6>3 and not (27,10,1,5)): the forced
  subobject cannot exist at all. States nothing about srg(99,14,1,2) existence.
hypotheses: a putative srg(99,14,1,2); condition (*) i.e. n3=0; Makhnev's
  Lemmas 6-9 (sourced).
holds-here: yes — check_srg33_12_1_6.py and check_makhnev_n3_counts.py both
  run to completion in exact integer arithmetic with the stated verdicts.
status: checked for the infeasibility step; sourced for the lemma chain.
bearing: upgrades 'no n3=0 srg(99,14,1,2)' from a sourced theorem to one whose
  critical step (infeasibility of (33,12,1,6)) is re-derived here; keeps the
  whole n3=0 branch (still a conjecture) as the only built-in 99 lever.
anchor: code/out/check_srg33_12_1_6.captured.txt,
  code/out/check_makhnev_n3_counts.captured.txt,
  research/sources/makhnev-1988-lambda1-russian-fulltext.full.md
```
