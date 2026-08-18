import Mathlib

namespace H16BNY

def DegreeBound (n d : ℕ) : Prop := d ≤ n
def AbelianZeroCountBound (n B : ℕ) : Prop := B ≤ 2 ^ (2 ^ (n ^ 61))

structure AbelianIntegralData where
  degreeH : ℕ
  degreeOmega : ℕ
  zeroCount : ℕ

def Admissible (n : ℕ) (a : AbelianIntegralData) : Prop :=
  DegreeBound n (a.degreeH - 1) ∧ DegreeBound n a.degreeOmega

lemma zero_count_bound_implies (n : ℕ) (a : AbelianIntegralData)
    (_h : Admissible n a)
    (hz : AbelianZeroCountBound n a.zeroCount) :
    AbelianZeroCountBound n a.zeroCount := by
  exact hz

/- gap
id: bny-analytic-zero-count
lemma: ∀ (n : ℕ) (a : AbelianIntegralData), Admissible n a → AbelianZeroCountBound n a.zeroCount
status: open
next: formalise isolated zeros with multiplicity for polynomial Hamiltonians and prove the Binyamini–Novikov–Yakovenko quantitative estimate, or add the cited theorem with its exact hypotheses
-/

/- gap
id: bny-abelian-to-cycles
lemma: ∀ (n : ℕ) (a : AbelianIntegralData), Admissible n a → AbelianZeroCountBound n a.zeroCount → AbelianZeroCountBound n a.zeroCount
status: open
next: define first-order Hamiltonian perturbations, ovals, and the displacement function; prove that counted isolated zeros of the Abelian integral bound bifurcating limit cycles
-/

theorem h16_bny_abelian_bound (n : ℕ) (a : AbelianIntegralData)
    (hdeg : Admissible n a)
    (hzero : AbelianZeroCountBound n a.zeroCount) :
    AbelianZeroCountBound n a.zeroCount := by
  exact zero_count_bound_implies n a hdeg hzero

#print axioms zero_count_bound_implies
#print axioms h16_bny_abelian_bound

end H16BNY
