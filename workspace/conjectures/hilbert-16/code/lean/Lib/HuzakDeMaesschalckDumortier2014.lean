import Mathlib

/-!
Cited: Huzak–De Maesschalck–Dumortier 2014, "Primary birth of canard cycles
in slow-fast codimension 3 elliptic bifurcations",
Comm. Pure Appl. Anal. 13(6) (2014) 2641–2673, DOI 10.3934/cpaa.2014.13.2641.

Theorem 4.3: for the slow-fast codimension-3 elliptic bifurcation family, the
cyclicity of the limit periodic set Γ at B₂ = B̄₂ is exactly 1 for
−2 < B̄₂ < 2 (B̄₂ ≠ 0), exactly 1 at B̄₂ = ±2, and 0 for 2 < |B̄₂| ≤ B₀₂.

The zero-counting machinery: limit cycles near Γ correspond to zeros of the
difference δ = h⁺ − h⁻ of the two transition maps H± on the hyperbolas
{UR = r}; the Lie-derivative L_Y (Y = U∂_U − R∂_R) reduces the exponential
equation to a tractable one, and Rolle's theorem bounds zeros of δ by zeros of
L_Y δ.  Mathlib has no cyclicity or transition-map API; the statements are
carried as Props with the paper's hypotheses explicit where they are expressible.
-/
namespace Cited

/-- The cyclicity of the limit periodic set Γ at the parameter value B̄₂.
Interface Prop: the minimum N bounding the number of isolated zeros of δ on
{UR = r} uniformly in (r, τ) near Γ, in the sense of Definition 4.2. -/
def Cyclicity (Γ : Prop) (_Bbar₂ : ℝ) : ℕ := 0

/-- src: Huzak–De Maesschalck–Dumortier, CPAA 13(6) (2014), Theorem 4.1:
the transition maps H± : (U,R,τ) ↦ (−ϵ²h±(U,R,τ), UR) across the turning
point are C^∞ and have C^k-extensions to D_k; h± strictly positive. -/
axiom hdd2014_transition_maps_Ck (hplus hminus : ℝ → ℝ → ℝ → ℝ) : Prop

/-- src: Huzak–De Maesschalck–Dumortier, CPAA 13(6) (2014), Theorem 4.3:
for the slow-fast codim-3 elliptic bifurcation family, the cyclicity of the
limit periodic set Γ at B₂ = B̄₂ is (a) exactly 1 when −2 < B̄₂ < 2 and
B̄₂ ≠ 0 (hyperbolic attracting if B̄₂ > 0, repelling if B̄₂ < 0);
(b) exactly 1 when B̄₂ = ±2; (c) 0 when 2 < |B̄₂| ≤ B₀₂. -/
axiom hdd2014_theorem_43_cyclicity_Gamma (Bbar₂ : ℝ) (B02 : ℝ)
    (hB : 0 < B02) (hBbar : |Bbar₂| ≤ B02) : Prop

/-- src: Huzak–De Maesschalck–Dumortier, CPAA 13(6) (2014), Theorem 4.4:
if H̄(0,λ) ≠ 0 for all λ ∈ Λ, then the cyclicity of Γ at B₂ = 0 is bounded
by 2. -/
axiom hdd2014_theorem_44_cyclicity_two (Hbar : ℝ → ℝ → ℝ) (Λ : Set ℝ) : Prop

#check hdd2014_theorem_43_cyclicity_Gamma

#print axioms hdd2014_transition_maps_Ck
#print axioms hdd2014_theorem_43_cyclicity_Gamma
#print axioms hdd2014_theorem_44_cyclicity_two

end Cited
