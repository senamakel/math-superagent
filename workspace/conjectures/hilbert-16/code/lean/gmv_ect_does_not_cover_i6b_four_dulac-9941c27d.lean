import Mathlib

/-
Decomposition of the node
`gmv-ect-does-not-cover-i6b-four-dulac`.

The formalisation deliberately represents the source-level objects abstractly:
`ECTCriterion` records the hypotheses supplied by GMV, while `I6bFourDulac`
records the complete displacement problem.  The intended conclusion is a
non-implication: the cited ECT theorem does not, by itself, establish the
complete I^1_6b four-Dulac assertion.
-/

structure ECTCriterion where
  family : Type
  separatedHamiltonianOvals : Prop
  firstOrderAbelianIntegrals : Prop
  ectConclusion : Prop

structure I6bFourDulac where
  displacementFamily : Type
  completeFourDulac : Prop
  uniformHypotheses : Prop
  finiteZeroConclusion : Prop

def GMVApplies (c : ECTCriterion) (d : I6bFourDulac) : Prop :=
  c.separatedHamiltonianOvals ∧
    c.firstOrderAbelianIntegrals ∧
    d.completeFourDulac

def GMVReducesTo (c : ECTCriterion) (d : I6bFourDulac) : Prop :=
  GMVApplies c d → d.finiteZeroConclusion

/-
The missing bridge is represented explicitly.  It is not supplied by the
statement of the ECT criterion: this is the exact research gap, rather than a
claim that a mathematical counterexample to the reduction is known.
-/

/- gap
id: gmv-ect-four-dulac-reduction
lemma: ∀ c : ECTCriterion, ∀ d : I6bFourDulac, GMVReducesTo c d
status: open
next: formalise a concrete GMV family and the I^1_6b four-Dulac displacement, then test whether GMV's separated-oval and first-order hypotheses imply the required uniform reduction
-/
axiom gmv_ect_four_dulac_reduction :
  ∀ c : ECTCriterion, ∀ d : I6bFourDulac, GMVReducesTo c d

/- gap
id: gmv-ect-hypotheses-not-identified-with-i6b
lemma: ¬ (∀ c : ECTCriterion, ∀ d : I6bFourDulac, GMVApplies c d)
status: open
next: extract the exact hypotheses of GMV's ECT theorem and compare them line-by-line with the four-Dulac I^1_6b family
-/
axiom gmv_ect_hypotheses_not_identified_with_i6b :
  ¬ (∀ c : ECTCriterion, ∀ d : I6bFourDulac, GMVApplies c d)

theorem gmv_ect_does_not_cover_i6b_four_dulac :
    (∀ c : ECTCriterion, ∀ d : I6bFourDulac, GMVReducesTo c d) →
      False := by
  intro h
  apply gmv_ect_hypotheses_not_identified_with_i6b
  intro c d
  sorry

#print axioms gmv_ect_four_dulac_reduction
#print axioms gmv_ect_hypotheses_not_identified_with_i6b
#print axioms gmv_ect_does_not_cover_i6b_four_dulac
