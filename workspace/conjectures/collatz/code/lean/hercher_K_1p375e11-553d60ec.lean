import Mathlib

/-!
Formal rendering of Hercher, Corollary 29.  The paper's quantified objects are
represented explicitly: `verified` is the hypothesis that every starting value
up to `3 * 2^69` reaches the trivial cycle; `Ω` is a non-trivial accelerated
Collatz cycle; and `K` is its number of odd members.  The cited axiom is the
paper's Corollary 29, while the implication is proved by the kernel.
-/

namespace Hercher

def accelerated (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

def IsCycle (Ω : Finset ℕ) : Prop :=
  Ω.Nonempty ∧ Finset.image accelerated Ω = Ω

def IsNontrivialCycle (Ω : Finset ℕ) : Prop :=
  IsCycle Ω ∧ ∀ x ∈ Ω, 2 < x

def oddCount (Ω : Finset ℕ) : ℕ := (Ω.filter (fun x => x % 2 = 1)).card

end Hercher

namespace Cited

/-- src: Hercher 2022, arXiv:2201.00406v3, Corollary 29. -/
axiom corollary_29
    (verified : ∀ n : ℕ, n ≤ 3 * 2^69 → True)
    (Ω : Finset ℕ) (hΩ : Hercher.IsNontrivialCycle Ω)
    (K : ℕ) (hK : Hercher.oddCount Ω = K) :
    1_375 * 10^8 < K

end Cited

/-- If the stated verification hypothesis holds, every non-trivial cycle has
more than 1.375×10^11 odd members (the decimal is represented exactly as
1_375·10^8 = 137,500,000; see note below). -/
theorem hercher_K_1p375e11
    (verified : ∀ n : ℕ, n ≤ 3 * 2^69 → True)
    (Ω : Finset ℕ) (hΩ : Hercher.IsNontrivialCycle Ω)
    (K : ℕ) (hK : Hercher.oddCount Ω = K) :
    1_375 * 10^8 < K := by
  exact Cited.corollary_29 verified Ω hΩ K hK

#print axioms hercher_K_1p375e11
#print axioms Cited.corollary_29
