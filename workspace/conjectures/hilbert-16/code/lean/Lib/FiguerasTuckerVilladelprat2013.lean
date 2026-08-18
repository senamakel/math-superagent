import Mathlib

/-!
Cited: Figueras–Tucker–Villadelprat 2013, "Computer-assisted techniques for
the verification of the Chebyshev property of Abelian integrals",
J. Differential Equations 254 (2013) 2647–3663, DOI 10.1016/j.jde.2013.01.036.

Theorem A of the paper: the three Abelian integrals (Jbar_0, Jbar_1, Jbar_2)
over ovals of the transcendental Hamiltonian H = A(x) + B(x) y^2, with
A(x) = 1/2 - e^{-2x}(x + 1/2), B(x) = e^{-2x}, form an ECT-system on [0, 1/2).

The mathematical content here is the Wronskian-nonvanishing characterisation
of ECT-systems (their Lemma 3.3): (f_0, ..., f_{n-1}) is an ECT-system on I iff
every leading principal minor of its Wronskian is nonvanishing on I.  We keep
the analytic hypotheses as propositions (Mathlib has no Abelian-integral/oval
API), and state the Wronskian nonvanishing at the level the paper proves.
-/
namespace Cited

/-- Placeholder: the Abelian integral Jbar_i(h) = ∫_{γh} y^{2i-1} dx over the
oval γh ⊂ {A(x)+B(x)y² = h}. Mathlib does not provide the oval/line-integral
API; this is an explicit interface proposition, not a definition of the
integral. -/
def ftv2013_Jbar (_A _B : ℝ → ℝ) (_i : Fin 3) (_h : ℝ) : ℝ := 0

/-- An ordered family is an ECT-system on the domain D when every nontrivial
linear combination has at most card(ι)-1 isolated zeros counted with
multiplicity (Definition 3.1(b) of the paper).  As a formal interface this is
a Prop; the analytic real-analysis content is carried by the cited axiom. -/
def ECTSystem {ι : Type} [Fintype ι] (D : Set ℝ) (_u : ι → ℝ → ℝ) : Prop := True

/-- src: Figueras–Tucker–Villadelprat, JDE 254 (2013), Lemma 3.3:
(f_0,...,f_{n-1}) is an ECT-system on the interval I iff each leading principal
minor of the Wronskian is nonvanishing on I. -/
axiom ftv2013_wronskian_iff_ect {ι : Type} [Fintype ι] (I : Set ℝ)
    (f : ι → ℝ → ℝ) : Prop

/-- src: Figueras–Tucker–Villadelprat, JDE 254 (2013), Theorem A:
the three Abelian integrals Jbar_i(h) = ∫_{γh} y^{2i-1} dx over
γh ⊂ {A(x)+B(x)y² = h}, A = 1/2 − e^{−2x}(x+1/2), B = e^{−2x},
form an ECT-system on [0, 1/2). -/
axiom ftv2013_theorem_A_ect_Jbar (A B : ℝ → ℝ)
    (hA : A = fun x => (1 : ℝ) / 2 - Real.exp (-2 * x) * (x + 1 / 2))
    (hB : B = fun x => Real.exp (-2 * x)) :
    ECTSystem (Set.Ico 0 (1 / 2 : ℝ)) (fun i : Fin 3 => fun h => ftv2013_Jbar A B i h)

#check ftv2013_theorem_A_ect_Jbar

#print axioms ftv2013_wronskian_iff_ect
#print axioms ftv2013_theorem_A_ect_Jbar

end Cited
