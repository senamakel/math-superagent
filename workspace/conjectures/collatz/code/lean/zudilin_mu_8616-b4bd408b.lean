import Mathlib

/-!
Formal rendering of node `zudilin-mu-8616`.

The source's irrationality exponent is represented by the standard infimum
formalisation below.  The cited theorem is kept as an attributed axiom because
this run is formalising the consequence of the literature, not reproving
Zudilin's Padé/irrationality-measure argument.

Binder correspondence: `γ` is the nonzero Q-linear combination; `hγ` is its
nonzeroness; `hspan` is membership in the Q-span of `log 2` and `log 3`; `a,b`
inside the definition are integer numerator and denominator; `c` is the
candidate exponent.
-/

noncomputable def irrationalityExponent (γ : ℝ) : ℝ :=
  sInf {c : ℝ | Set.Finite {p : ℤ × ℤ |
    ((p.2 : ℝ) ≠ 0) ∧ |γ - (p.1 : ℝ) / p.2| ≤ |(p.2 : ℝ)| ^ (-c)}}

noncomputable def log23Span : Submodule ℚ ℝ :=
  Submodule.span ℚ ({Real.log 2, Real.log 3} : Set ℝ)

namespace Cited

/-- src: Zudilin 2004, arXiv:math/0404523, Theorem 3 (after G. Rhin). -/
axiom zudilin_theorem_3
    {γ : ℝ} (hγ : γ ≠ 0) (hspan : γ ∈ log23Span) :
    irrationalityExponent γ < (8.616 : ℝ)

end Cited

/-- Zudilin Theorem 3 at `log 3/log 2`; `hlog2` is the denominator
nonzeroness needed for the ratio.  The remaining span-membership fact is
currently an explicit gap: the informal source's phrase “in the span” does
not by itself specify a Lean proof of membership for this quotient. -/
theorem zudilin_mu_8616_log_ratio
    (hlog2 : Real.log 2 ≠ 0) :
    irrationalityExponent (Real.log 3 / Real.log 2) < (8.616 : ℝ) := by
  apply Cited.zudilin_theorem_3
  · exact div_ne_zero (by positivity) hlog2
  · change Real.log 3 / Real.log 2 ∈
      Submodule.span ℚ ({Real.log 2, Real.log 3} : Set ℝ)
    sorry

#print axioms zudilin_mu_8616_log_ratio
#print axioms Cited.zudilin_theorem_3
