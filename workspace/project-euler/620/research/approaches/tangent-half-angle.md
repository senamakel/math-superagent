```approach
idea: Rational parametrization of the phase congruences via eccentric anomaly and tangent half-angle substitution
mechanism: The planet-centre ellipse (foci at O and S, major semiaxis a = (c+s)/(4π), focal half-distance c_f = d/2) is parametrized by eccentric anomaly E:
  P(E) = (a cos E, a√(1−e²) sin E) in coordinates with origin at ellipse centre (midpoint of OS).
Equivalently, in the coordinate system with origin at S (sun centre), the distance to S is r_S(E) = a(1−e²)/(1+e cos E) (the polar equation with pole at S).
For a planet of type t, the tangency conditions fix |SP| = (s+t)/(2π) and |CP| = (c−t)/(2π); both are already satisfied for every E on the ellipse, so E is the single free arrangement parameter. The interior angles of triangle CPS are explicit functions of E:
  cos φ(E) = (|SP|² + d² − |CP|²)/(2|SP|·d), etc.
The phase invariant W(E) = s·φ(E) + c·χ(E) − t·γ(E) is a linear combination of arccos of rational functions of cos E and sin E.
Now substitute t = tan(E/2): cos E = (1−t²)/(1+t²), sin E = 2t/(1+t²). Every trigonometric expression becomes a rational function of t. The key step: tan(W(E)) = 0 (mod π for the mirror-pair congruence) means tan(s·φ + c·χ − t·γ) = 0. Using the tangent addition formula iterated, tan(n·θ) = P_n(tan θ)/Q_n(tan θ) where P_n, Q_n are related to Chebyshev polynomials. Since tan(φ) = √((1−cos φ)/(1+cos φ)) and cos φ is rational in t, tan φ = √(rational(t)), and similarly for tan χ, tan γ. After clearing square roots, the condition tan(W) = 0 becomes a polynomial equation in t. The degree of this polynomial is bounded by a function of c and s (specifically, by 2(c+s) after squaring twice). The number of valid centre distances d — hence g(c,s,p,q) — is the number of real roots t ∈ ℝ whose corresponding d(t) = 2c_f = 2·|OS| falls in the admissible interval [d_min, d_max], and which also satisfy the cross-type congruence. The root count can be obtained without numerical scanning via Sturm sequences or by computing the polynomial explicitly (using sympy to build it from the rational expressions) and solving exactly.
status: grounded
precedent: https://www.cecm.sfu.ca/personal/monaganm/papers/trigpoly.pdf ; https://en.wikipedia.org/wiki/Sturm%27s_theorem ; https://encyclopediaofmath.org/wiki/Sturm_theorem ; https://www-sop.inria.fr/hephaistos/logiciels/ALIAS/ALIAS-C++/node4.html ; thread `offcentre-mesh-phase-model` (claim `offcentre_dual_mesh_phase_invariant`)
first-step: Derive the explicit rational expressions for cos φ, cos χ, cos γ in terms of E for a planet of type t, then substitute t = tan(E/2). Write a sympy script that builds the polynomial P(t) = numerator of tan(s·φ(t) + c·χ(t) − t·γ(t)), counts its real roots in the relevant t-interval via Sturm's theorem, and checks whether each root also satisfies the cross-type congruence — reproducing g(16,5,5,6)=9.
```

## Research verdict (the technique is grounded; its guarantee is upstream)

**The technique is standard, exact, and well-sourced.** The tangent half-angle
substitution θ→t=tan(θ/2) is a ring morphism Q[sin,cos]→Q(t) with kernel
⟨s²+c²−1⟩; a trig polynomial of trigonometric degree d maps to a rational
polynomial a(t)/(1+t²)^d with deg_t(a) ≤ 2d (Mulholland & Monagan, Lemma 3–4),
and the map is invertible on the right class (Theorem 1). This confirms the
candidate's degree bound (≤ 2× trig degree) and that the result is rational in
t. Combined with Sturm's theorem — exact real-root counting of a square-free
real polynomial (Wikipedia; Encyclopedia of Mathematics) — the trig→polynomial→
Sturm pipeline is a *bona fide* exact route to root-counting with no numerical
scanning, exactly as implemented in the INRIA ALIAS root-counting system
("Analyzing trigonometric equations"). So the *machinery* the candidate proposes
is grounded.

**The guarantee for THIS problem is upstream, not in the technique.** The
candidate presumes the W-invariant phase model of the thread
`offcentre-mesh-phase-model` — W_j = s·φ_j + c·χ_j − t_j·γ_j pairwise congruent
mod 2π, the mirror-pair as s·φ+c·χ ≡ 0 mod π — and the t-substitution merely
turns that into a root-count. That phase model is the section's crux and is
**still oracle-unverified**: it has not yet been made to reproduce g(16,5,5,6)
= 9, G(16) = 9, G(20) = 205 (claim `offcentre_dual_mesh_phase_invariant`,
status asserted/unchecked). If that model is right, this is the exact route to
g; if it is wrong, the polynomial is root-counting a wrong condition. The
t-substitution does not by itself validate the discreteness.

Two technical caveats beyond the upstream model: (a) the candidate's phase terms
are arccos of rational functions, so tan(W) is a sum of terms
√(rational)·(Chebyshev) and clearing square roots can blow the degree well past
2(c+s) and inject spurious roots (which then need filtering against the
original congruence); (b) the candidate mixes eccentric anomaly E (about the
ellipse) with circle angles — the position-set for each type is still forced by
tangency (two mirror points per type, thread claim
`offcentre_two_positions_per_type`), which this parametrisation respects only
through the d-range.

Status: **grounded** as a route *conditional on* `offcentre_dual_mesh_phase_invariant` holding. Not a standalone guarantee; if that invariant is refuted, this approach is refuted with it (the polynomial would encode an incorrect discreteness).
