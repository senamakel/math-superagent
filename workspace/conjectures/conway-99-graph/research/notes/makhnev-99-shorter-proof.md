# Makhnev 1988 Thm 2, 99 case — the re-derivation as ONE note

This note reconstructs, from the primary Russian text and exact integer
arithmetic, the 99-case mechanism of Makhnev 1988 Thm 2 ("Strongly regular
graphs with λ = 1"): under condition (\*) (i.e. n3 = 0, no pair of triangles
sharing two edges) the argument forces a subobject srg(33,12,1,6), and this
run shows that subobject is INFEASIBLE by multiplicity integrality alone —
a shorter, self-contained route than Makhnev's own rejection via Thm 1.

This note asserts **nothing** about whether srg(99,14,1,2) exists. It records
only that the n3 = 0 mechanism rests on a genuinely infeasible intermediate and
that the infeasibility is visible by integrality on its own.

## The forced-subgraph chain (both anchors)

Both captures live in `code/out/`:

1. `check_makhnev_n3_counts.captured.txt` — exact-integer reconstruction of
   Makhnev 1988 Lemmas 6–9 count arithmetic at (99,14,1,2):
   - the closure of a triangle A = {A,B,C} is Γ(A) = [A]∪[B]∪[C], and since
     A,B,C are pairwise adjacent with λ = 1, |Γ(A)| = 3·14 − 3 = **39** (not 9 —
     the script flags "closure = 9" as a defect; Lemma 6's 36 points of
     Γ(A)−A in 12 inner triangles forces 39);
   - the 99 − 39 = **60** points outside Γ(A) each lie in exactly one triangle
     disjoint from Γ(A) (Lemma 7), giving **20** outer triangles;
   - the 1 (A) + 12 (inner) + 20 (outer) = **33** triangle-vertices partition
     the 3 + 36 + 60 = **99** points and form the claimed subobject
     Λ₀ = srg(33,12,1,6).
   - VERDICT: corrected primary-source counts are internally SELF-CONSISTENT
     with v = 99, k = 14 (exact integer; no graph, no floats).
2. `check_srg33_12_1_6.captured.txt` — exact-integer/Fraction feasibility of
   the sub-parameter-set (33,12,1,6):
   - eigenvalues 1, −6 (δ = 49, √δ = 7);
   - the multiplicity numerator `2k + (v−1)(λ−μ) = 24 + 32·(−5) = −136` is
     **not divisible by 7**, so the smaller multiplicity g is non-integral;
   - VERDICT: srg(33,12,1,6) is **INFEASIBLE by multiplicity integrality**.
   Contrast rows: (27,10,1,5) FEASIBLE and EXISTS (Thm 1's exception:
   r = 1, s = −5, f = 6, g = 20, all integers); (9,4,1,2), (99,14,1,2),
   (243,22,1,2) all FEASIBLE; (33,8,1,2) INFEASIBLE by the same −16 not ÷ 5
   mechanism (consistency check).

## What this upgrades

- Makhnev's published text rejects Λ₀ = srg(33,12,1,6) via **Thm 1**: a λ = 1
  SRG satisfying (\*) has μ ≤ 3 OR is the unique (27,10,1,5); Λ₀ has μ = 6 > 3
  and is not (27,10,1,5).
- This run rejects Λ₀ **directly by multiplicity integrality** (the −136 not
  divisible by 7 / the 2k+(v−1)(λ−μ) divisibility), a strictly simpler route
  that needs no appeal to Thm 1. So the 99 case of Thm 2 ("no srg(99,14,1,2)
  satisfies (\*) [n3 = 0]") has a shorter proof than the published one, and the
  decisive step is re-derived here in exact integer arithmetic.

## Status

- The lemma chain (39 / 12 inner / 60 outside / 20 outer / 33-point partition):
  **sourced** (primary Russian text, research/sources/
  makhnev-1988-lambda1-russian-fulltext.full.md, Lemmas 6–9). The count layer of
  Lemmas 8–9 — that Λ₀ is exactly (33,12,1,6) and satisfies (\*) — was not
  independently re-proved here, only its arithmetic reproduced; that layer is
  taken from the source.
- The infeasibility of (33,12,1,6): **checked** (exact integer run,
  rerun this pass).

## Verification this pass

- `python3 code/out/check_makhnev_n3_counts.py` rerun: reconfirms |Γ(A)| = 39,
  12 inner triangles, 60 outside points, 20 outer triangles, 1+12+20 = 33
  triangle-vertices partitioning 3+36+60 = 99 points. All OK, VERDICT True.
- `python3 code/out/check_srg33_12_1_6.py` rerun: reconfirms (33,12,1,6)
  INFEASIBLE by multiplicity integrality (2k+(v−1)(λ−μ) = −136 not divisible by
  √δ = 7), against the feasible/existing (27,10,1,5), (9,4,1,2), (243,22,1,2)
  and open (99,14,1,2).

```claim
id: makhnev99-shorter-proof-integrality
statement: Under Makhnev 1988 Thm 2's condition (*) [n3 = 0] at (99,14,1,2),
  the argument forces, from the closure of a triangle and its 60 exterior
  points, a subobject Lambda_0 = srg(33,12,1,6): the closure has 39 points
  (= 3*14-3), its 36 non-A points lie in 12 inner triangles, the 60 outside
  points give 20 outer triangles, and the 1 + 12 + 20 = 33 triangle-vertices
  partition all 3 + 36 + 60 = 99 points. srg(33,12,1,6) is INFEASIBLE by
  eigenvalue-multiplicity integrality: the g numerator 2k+(v-1)(lam-mu) = -136
  is not divisible by sqrt(delta) = 7. Makhnev rejects Lambda_0 via Thm 1
  (mu = 6 > 3 and not (27,10,1,5)); this run rejects it directly by
  multiplicity integrality, a shorter self-contained proof of the 99 case of
  Thm 2's n3 = 0 branch. This asserts nothing about whether srg(99,14,1,2)
  exists.
hypotheses: a putative srg(99,14,1,2); condition (*) i.e. n3 = 0; Makhnev 1988
  Lemmas 6-9 (sourced from the primary Russian text). The re-derived steps are
  the count arithmetic and the parameter feasibility.
holds-here: yes — check_srg33_12_1_6.py and check_makhnev_n3_counts.py both
  rerun this pass in exact integer arithmetic with the stated verdicts
  (39 / 12 / 60 / 20 / 33 self-consistent; (33,12,1,6) INFEASIBLE by
  multiplicity integrality, -136 not divisible by 7).
status: conditional for the theorem-level claims (srg33_12_1_6 infeasible by
  integrality, and the n3=0 branch of Thm 2's 99 case) — both rest on the Cited
  axioms Cited.srg_multiplicity_integrality (Bose-Mesner eigenvalue
  multiplicity integrality) and Cited.makhnev_lemmas_6_9 (the forced-subobject
  chain), checked in Lean at code/lean/makhnev99_shorter_proof_integrality.lean
  (lean_check verified, no sorries; #print axioms names the two Cited axioms).
  The arithmetic kernel only (discriminant 49=7^2, numerator -136, 7 not
  dividing -136, and the multiplicity-integrality arithmetic) is kernel-checked
  outright: theorem Makhnev99.not_seven_dvd_33_12_1_6_numerator depends only
  on propext and Quot.sound. The count layer (39/12/60/20/33) and the
  exact-integer infeasibility check remain checked in Python as recorded above.
formalisation: code/lean/makhnev99_shorter_proof_integrality.lean
bearing: upgrades the short n3 = 0 rejection of srg(99,14,1,2) from a
  sourced theorem with a critical infeasibility to one whose critical step
  (infeasibility of (33,12,1,6)) is verified in exact integer arithmetic in
  Python AND whose arithmetic kernel is kernel-checked in Lean; the forced-
  subobject chain and the spectral integrality step remain sourced (Cited
  axioms), so the theorem-level statements are conditional, not formalised.
  Keeps the whole n3 = 0 branch as the only built-in 99 lever and draws no
  existence conclusion for srg(99,14,1,2).
anchor: code/lean/makhnev99_shorter_proof_integrality.lean,
  code/out/check_makhnev_n3_counts.captured.txt,
  code/out/check_srg33_12_1_6.captured.txt,
  research/sources/makhnev-1988-lambda1-russian-fulltext.full.md
```
