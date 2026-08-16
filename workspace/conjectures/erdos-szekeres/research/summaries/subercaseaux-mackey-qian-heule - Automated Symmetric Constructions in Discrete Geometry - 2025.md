# Subercaseaux, Mackey, Qian, Heule — "Automated Symmetric Constructions in Discrete Geometry" (2025)

> **Source:** arXiv:2506.00224 (cs.DM / cs.CG), submitted 30 May 2025. Full text at `research/sources/subercaseaux-mackey-qian-heule - Automated Symmetric Constructions - HTML.full.md`.
> **Relevance:** the run's required SAT arm (orientation/chirotope variables + transitivity axioms, symmetry reduction, isomorph rejection) and the structural question of what an extremal 2^{k-2}-point no-k-gon set looks like.

## What it establishes

A computational method that **embeds s-fold rotational symmetry directly into the SAT encoding** of a discrete-geometry configuration (rather than post-hoc symmetry breaking), plus a local-search **realizability solver** ("Localizer") to turn abstract SAT designs into concrete point coordinates.

### Directly relevant to ES(7) — the headline structural result
**There is no realizable 4-fold-symmetric 32-point set with no convex 7-gon.**
- On 32 points, only s = 1, 2, 4 fold symmetries are even possible; the authors focused on s = 4 as it reduces the search space most.
- The formula was easy to satisfy. Enumerating **all** SAT solutions on a supercomputer (~1 CPU year) gave **310,187,713 non-isomorphic** 4-fold-symmetric 32-point configurations with no 7-gon.
- **All 310 million solutions have only 6 different inner-12-point configurations, and none of those 6 is realizable.** The outer 28 points are frequently realizable; the inner 12 never. Hence no realizable 4-fold symmetric 32-point 7-gon-free set exists.
- Implication for this run's structural thread: a hypothetical extremal 32-point no-7-gon set (if one exists at all) **cannot have 4-fold rotational symmetry**, and the obstruction is a local non-realizability of the 12 inner points. This is a concrete, citable restriction, and one of the few structural impossibility results on the ES(7) frontier.

### Small-k evidence (ES values already known, reproduced)
- **16 points avoiding 6-gons:** formula is UNSAT for 3-fold symmetry, SAT for 4-fold (66 non-isomorphic solutions after symmetry breaking, **18 realizable**) and 5-fold (932/948, **92 realizable**). Consistent with ES(6)=17 (16 points without a 6-gon exist; 17 force one).
- Realizable solutions tend to have relatively many 4-gons and few 5-gons (Figure 5), a heuristic for voting on likely-realizable SAT solutions.

### Everywhere-unbalanced-points (adjacent problem)
- Confirms the known 12-point 2-EU set is minimal (even).
- Refutes 2-EU sets with ≤ 19 points (odd case), and finds the **minimal 21-point 2-EU set** (improving the prior 23-point construction). Fully answers the minimality question.

### Methodology — encoding improvements this run's SAT arm can reuse
- **Dynamic point-ordering axioms (Prop 1, 2):** the left-to-right ordering of signotope axioms can be replaced by *any* linear ordering ≺ introduced as SAT variables, so rotational symmetry (which cannot fix a left-to-right order a priori) becomes compatible. Ordering axioms cost Θ(n³) clauses; the dynamic-ordering orientation axioms cost ≈ (4/3)·4!·C(n,4) ≈ (4/3)n⁴ clauses. For n = 32 that is ~1.3M clauses vs ~24M for the CC-system axioms — a large reduction.
- **Symmetry constraints (§3):** enforce s-fold symmetry by unifying the orientation-variable equivalence classes (treat the orbit literals as one variable with its negations), and filter constraints to lexicographically-smallest orbit representatives.
- **Symmetry breaking (§3.2):** CL (convex-layer) unit clauses fix which points form each convex layer and the cyclic order; Q (quadrant) clauses fix one point per layer in the bottom-left quadrant. Diagonalizes the dihedral symmetry without invalidating realizability.
- **k-gon constraint (§4.3):** conv_{i,j,k,l} auxiliary variables from the 4-set convexity criterion, 12·C(n,4) Tseitin clauses; "no k-gon" = for every k-subset X, ∨_{4-subset ⊂ X} ¬conv.
- **Realizability:** Localizer local-search solver; handles the ∃ℝ-complete realizability problem in practice. Cannot prove unrealizability (only find realizations), but unrealizability is certified here by finding an unrealizable 10-point subset.

## Claims

```claim
id: smqh-no-realizable-4fold-32-no7gon
statement: There is no realizable point set of 32 points in general position with 4-fold rotational symmetry and no convex 7-gon.
hypotheses: 32 points, general position, exact 4-fold rotational symmetry; all 310,187,713 orientation-type satisfying assignments share one of 6 non-realizable inner-12 configurations.
holds-here: true — direct to the ES(7)=33 question; restricts any hypothetical extremal set further.
status: asserted-by-source (SAT enumeration + Localizer realizability/10-point unrealizable certificates; the authors' computational claim, not reviewed here)
bearing: a hypothetical 32-point no-7-gon set cannot have 4-fold symmetry; the local obstruction is non-realizability of the inner 12 points.
formalisation: none
```

```claim
id: smqh-dynamic-ordering-axioms
statement: In a SAT encoding of point-set orientations, the signotope left-to-right ordering can be replaced by dynamically-assigned linear-ordering variables, reducing the orientation axioms to ≈(4/3)n⁴ clauses while preserving exactly the CC-system solutions (Prop 1: sound; Prop 2: complete).
hypotheses: point set in general position; orientation variables a_{i,j,k}; the linear order ≺ introduced as variables with totality/asymmetry/transitivity.
holds-here: true — gives this run's SAT arm a cheaper, symmetry-compatible chirotope encoding than the standard CC-system axioms.
status: asserted-by-source (proofs in Appendix D; Prop 2's completeness is computational, reduced to n=5)
bearing: the run's required SAT reproduction of ES(5)=9 / ES(6)=17 can use this encoding and the CL/Q symmetry breaking.
formalisation: none
```

## Further implications for the run

- The **6 non-realizable inner-12 configurations** are the crux — if extracted explicitly they would be a concrete forbidden local structure for 32-point no-7-gon sets (an exact restricted class). The paper does not list the coordinates, but the GitHub repo (`bsubercaseaux/automatic-symmetries`) may. A gap for `research/REQUESTS.md` if the run wants them.
- Symmetry is not evidence the conjecture is false for ES(7): no 4-fold symmetric 32-point no-7-gon set exists, but 1- and 2-fold symmetric ones are still open, and non-symmetric extremal sets are unconstrained by this result.
