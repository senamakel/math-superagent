import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

-- ============================================================================
-- REFUTATION of the literal "clean composition lemma" in the HALVED domain.
--
-- The task ledger proposed, as the minimal formalisation, the statement
--
--     runAbs w el ∈ {0,2}   given   w ≤ 2·ν₁ + 2
--
-- with el a HALVED {0,1}-pattern and ν₁ = countOnes el (Generalise
-- descent_claim1).  This statement is FALSE.  The mistake is a domain
-- confusion: a {0,1} input pattern under |·-e| for e ∈ {0,1} keeps the orbit
-- inside {0,1} generally (when the start is in {0,1} or below budget), so the
-- correct conclusion from the halved core is `∈ {0,1}` (descent_claim1), not
-- `∈ {0,2}`.  A {0,2}-VALUED orbit requires the EVEN {0,2} pattern and an even
-- starting value -- which is exactly `lemma54_even_forward` (already
-- kernel-checked in code/lean/lemma54_even_domain.lean).
--
-- This file is a LOCATED ERROR artifact: it states the false generalisation
-- and exhibits a witness on which the hypotheses hold and the conclusion
-- fails.  It is intentionally NOT a `formalised` claim; it is a refuted
-- statement, recorded so a later attempt does not walk into it.
-- ============================================================================

-- The orbit / trajectory: x_0 = w, x_{s+1} = |x_s - e_s|.
def runAbs : Nat → List Nat → Nat
  | w, [] => w
  | w, e :: rest => runAbs (Nat.dist w e) rest

-- ν₁ : the number of 1s in a halved {0,1} pattern.
def countOnes : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 1 then 1 else 0) + countOnes rest

-- ---------------------------------------------------------------------------
-- THE COUNTEREXAMPLE:  el = [0],  w = 1.
--   * the pattern is a valid {0,1} pattern: 0 = 0 ∨ 0 = 1.
--   * ν₁ = countOnes [0] = 0, so the budget bound is  w = 1 ≤ 2·ν₁ + 2 = 2.
--   * but  runAbs 1 [0] = 1,  and 1 ∉ {0,2}.
-- So the hypotheses hold and the conclusion fails.
-- ---------------------------------------------------------------------------

-- The budget bound holds:  1 ≤ 2·(countOnes [0]) + 2.
lemma budget_holds : 1 ≤ 2 * countOnes [0] + 2 := by
  simp [countOnes]

-- The orbit value:  runAbs 1 [0] = 1.
lemma runAbs_value : runAbs 1 [0] = 1 := by
  simp [runAbs, Nat.dist]

-- 1 is not in {0,2}.
lemma one_not_in : ¬ (1 = 0 ∨ 1 = 2) := by
  omega

-- The full refutation: hypotheses of the proposed literal lemma hold,
-- conclusion fails.
theorem halved_composition_refuted :
    runAbs 1 [0] = 1 ∧ ¬ (runAbs 1 [0] = 0 ∨ runAbs 1 [0] = 2) := by
  constructor
  · exact runAbs_value
  · rw [runAbs_value]
    exact one_not_in

-- The EXISTENCE form: there is a valid halved {0,1} pattern, a start below
-- the budget 2·ν₁+2, for which the orbit is not in {0,2}.
theorem halved_composition_not_a_theorem :
    ∃ (el : List Nat) (w : Nat),
      (∀ e ∈ el, e = 0 ∨ e = 1) ∧        -- valid {0,1} pattern
      w ≤ 2 * countOnes el + 2 ∧         -- budget bound (literal lemma's premise)
      ¬ (runAbs w el = 0 ∨ runAbs w el = 2) := by
  refine ⟨[0], 1, ?_, ?_, ?_⟩
  · intro e he
    simp at he
    simp [he]
  · simp [countOnes]
  · rw [runAbs_value]
    exact one_not_in

-- Why the EVEN domain is the right setting for {0,2}-valued orbits:
-- a {0,1} pattern has outcomes in {0,1} under the correct budget
-- (descent_claim1 in code/lean/lemma54_even_domain.lean), NOT {0,2}.  The
-- {0,2} outcome is an even-domain theorem (lemma54_even_forward).  Those are
-- separate files; see the note, not an import (cross-file import impossible
-- in this container).

-- ---------------------------------------------------------------------------
-- Axiom footprint.
-- ---------------------------------------------------------------------------
#print axioms budget_holds
#print axioms runAbs_value
#print axioms one_not_in
#print axioms halved_composition_refuted
#print axioms halved_composition_not_a_theorem
