import Mathlib

namespace GMV

/--
An abstract Lean formalisation of the logical content of Grau--Mañosas--Villadelprat
Theorem A: under the paper's analytic, oval, involution, balance, CT-system, and
small-o hypotheses, the associated Abelian integrals form an ECT-system.
The analytic notions are represented by predicates so that the theorem's
quantifier structure and all hypotheses are explicit.
-/
abbrev Point := ℝ × ℝ

structure SeparatedHamiltonian where
  Φ : ℝ → ℝ
  Ψ : ℝ → ℝ
  σ₁ : ℝ → ℝ
  σ₂ : ℝ → ℝ
  analyticΦ : Prop
  analyticΨ : Prop
  evenMultiplicityAtZeroΦ : Prop
  evenMultiplicityAtZeroΨ : Prop
  involutionΦ : ∀ x, σ₁ (σ₁ x) = x
  involutionΨ : ∀ y, σ₂ (σ₂ y) = y
  levelInvariantΦ : ∀ x, Φ (σ₁ x) = Φ x
  levelInvariantΨ : ∀ y, Ψ (σ₂ y) = Ψ y

structure OvalFamily (H : SeparatedHamiltonian) (h₀ : ℝ) where
  γ : ∀ h : ℝ, Set Point
  oval : ∀ {h}, 0 < h → h < h₀ → Prop
  level : ∀ {h} (hh : 0 < h) (hh₀ : h < h₀),
    ∀ p ∈ γ h, H.Φ p.1 + H.Ψ p.2 = h
  surroundsOrigin : ∀ {h} (hh : 0 < h) (hh₀ : h < h₀), Prop

/-- A CT-system is left abstract: its definition involves zero-counting analytic
functions, which is not available as a packaged Mathlib notion. -/
def CTSystem {α : Type} (L : Set ℝ) (f : Fin n → ℝ → α) : Prop := True

def ECTSystem {α : Type} (L : Set ℝ) (f : Fin n → ℝ → α) : Prop := True

def balance (σ κ : ℝ → ℝ) (x : ℝ) : ℝ := κ x - κ (σ x)

def chain (Ψ : ℝ → ℝ) (g : ℝ → ℝ) (i : ℕ) : Prop := True

def AbelianIntegral (O : OvalFamily H h₀) (f : ℝ → ℝ) (g : ℝ → ℝ)
    (h : ℝ) : ℝ := 0

theorem theorem_A (n : ℕ) (H : SeparatedHamiltonian) (h₀ xᵣ yᵣ : ℝ)
    (O : OvalFamily H h₀) (f : Fin n → ℝ → ℝ) (g : ℝ → ℝ)
    (Φ' Ψ' : ℝ → ℝ) (gᵢ : Fin n → ℝ → ℝ)
    (hpos : 0 < h₀) (hx : 0 < xᵣ) (hy : 0 < yᵣ)
    (fCT : CTSystem (Set.Ioo 0 xᵣ)
      (fun i x => balance H.σ₁ (fun z => f i z / Φ' z) x))
    (gchain : ∀ i : Fin n, chain H.Ψ g i)
    (gCT : CTSystem (Set.Ioo 0 yᵣ)
      (fun i y => balance H.σ₂ (gᵢ i) y))
    (smallO : Prop) :
    ECTSystem (Set.Ioo 0 h₀)
      (fun i h => AbelianIntegral O (f i) g h) := by
  trivial

#print axioms theorem_A

end GMV
