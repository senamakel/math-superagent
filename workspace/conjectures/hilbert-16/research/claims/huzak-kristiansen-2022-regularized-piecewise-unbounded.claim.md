```claim
id: huzak-kristiansen-2022-regularized-piecewise-unbounded
statement: There exists a quadratic vector-field Z₊(·,λ) and a linear vector-field Z₋(·,λ),
  depending smoothly on λ ∈ ℝ, such that in a compact domain U: for every k ∈ ℕ there are
  ε_k > 0, a C^∞ regularization function φ_k : ℝ → ℝ, and a continuous λ_c^k : [0,ε_k[ → ℝ
  such that the regularized field Z(z) = Z₊(z,λ_c^k(ε))·φ_k(y·ε⁻¹) +
  Z₋(z,λ_c^k(ε))·(1−φ_k(y·ε⁻¹)) has at least k limit cycles in U for all ε ∈ ]0,ε_k[.
  The singular limit is a piecewise-smooth two-fold bifurcation of type VI₃ (visible-invisible).
source: Huzak–Kristiansen, "The number of limit cycles for regularized piecewise polynomial
  systems is unbounded", J. Differential Equations (2022), DOI 10.1016/j.jde.2022.09.028;
  arXiv:2109.07759v2. Theorem 1.1, full text held at
  research/sources/huzak-kristiansen-regularized-piecewise-unbounded-html.full.md.
holds-here: yes — this is a counterexample construction for the SMOOTH test (problem.md test 1):
  a smooth (C^∞) family of polynomial fields with unbounded limit cycles, existing exactly
  because the regularization family is NOT o-minimal (authors' own words). It does NOT
  falsify H(2)<∞ for smooth polynomial fields (the unboundedness stems from the
  regularization, not from Z±), but it marks where uniform boundedness fails: at the loss
  of o-minimality/quasianalyticity.
status: asserted
evidence: asserted-by-source, full text held and read (Theorem 1.1 verbatim at lines 63-73).
falsifies: (a) a correction/withdrawal of Theorem 1.1; (b) a source proving H(2)<∞ while the
  open graphics' return maps are provably not o-minimally definable — that would disconnect
  o-minimality from uniform boundedness. Neither known.
note: research/findings/huzak-kristiansen-2022-ominimality-converse-2026-08-18.md
related: h16-ominimality-route-roussarie
```
