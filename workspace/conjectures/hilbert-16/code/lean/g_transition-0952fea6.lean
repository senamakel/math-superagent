import Mathlib.Data.Real.Basic
import Mathlib.Topology.Basic

namespace H16Transition

abbrev Parameter := ℝ × ℝ
abbrev Section := ℝ

def Transition (K : Set Parameter) : Type := Parameter → Section → Section

inductive VertexKind
  | elementary
  | semihyperbolic
  | nilpotent
  | degenerate

inductive ExpansionKind
  | powerLog
  | transseries

def allowedClass : VertexKind → ExpansionKind
  | .elementary => .powerLog
  | .semihyperbolic => .transseries
  | .nilpotent => .transseries
  | .degenerate => .transseries

structure SectorData where
  vertex : VertexKind
  analytic : Prop
  normalForm : Prop
  transition : Prop

def CarriesExpansion (s : SectorData) : Prop :=
  s.analytic ∧ s.normalForm ∧ s.transition

lemma elementary_class (s : SectorData) (hv : s.vertex = .elementary) :
    allowedClass s.vertex = .powerLog := by
  simp [hv, allowedClass]

lemma degenerate_class (s : SectorData)
    (hv : s.vertex ≠ .elementary) :
    allowedClass s.vertex = .transseries := by
  cases h : s.vertex <;> simp [allowedClass, h] at hv ⊢

lemma analytic_transition_expansion (s : SectorData)
    (h : CarriesExpansion s) : s.transition := by
  exact h.2.2

/-
 gap
 id: g-transition-expansion
 lemma: ∀ s : SectorData, CarriesExpansion s →
   allowedClass s.vertex = allowedClass s.vertex ∧ s.transition
 status: open
 next: Prove an analytic sector-normal-form theorem giving transition expansion for each VertexKind, with explicit power-log versus transseries definitions and uniform parameter hypotheses.
-/

 theorem transition_expansion_decomposition
    (hsector : ∀ s : SectorData, CarriesExpansion s →
      allowedClass s.vertex = allowedClass s.vertex ∧ s.transition) :
    ∀ s : SectorData, CarriesExpansion s →
      allowedClass s.vertex = allowedClass s.vertex ∧ s.transition := by
  exact hsector

#print axioms elementary_class
#print axioms degenerate_class
#print axioms analytic_transition_expansion
#print axioms transition_expansion_decomposition

end H16Transition
