# Approach: algebraic-elimination-chebyshev

```approach
idea: Convert the transcendental phase congruences of the W-model (research/threads/offcentre-mesh-phase-model.md) into a univariate polynomial equation via rational parametrisation of the planet-centre ellipse, then count real roots exactly using Sturm sequences. The planet-centre ellipse has foci at O (ring centre) and S (sun centre), major semiaxis a = (c+s)/(4π), linear eccentricity e = d/2. Parametrise by eccentric anomaly E. The triangle angles φ = ∠PSC, χ = ∠PCS, γ = ∠SPC have cosines that are rational functions of cos E: specifically, cos φ = (e − a cos E)/a_t and cos χ = (a cos E + e)/b_t where a_t = (s+t)/(2π), b_t = (c−t)/(2π). The mirror-pair per-type meshing condition is s·φ + c·χ ∈ πℤ. Using φ = arccos(u), χ = arccos(v) with u, v rational in cos E, write cos(s·φ) = T_s(u) and sin(s·φ) = U_{s−1}(u)·√(1−u²) where T_s, U_s are Chebyshev polynomials of the first and second kind. Then tan(s·φ + c·χ) = (tan(s·φ) + tan(c·χ))/(1 − tan(s·φ)·tan(c·χ)). The condition tan = 0 means the numerator vanishes, giving an equation involving √(1−u²) and √(1−v²). Substitute t = tan(E/2): cos E = (1−t²)/(1+t²), sin E = √(1−cos²E) = (2t)/(1+t²). Clear all square roots to obtain a single polynomial P_{c,s,t}(t) ∈ Z[t] whose real roots in the valid interval correspond to valid planet positions. The degree is at most 2(c+s). Count real roots via Sturm sequences to get g(c,s,p,q) without any numerical scanning or transcendental function evaluation.

mechanism: The dead models all fail because they evaluate transcendental congruences numerically on a grid, missing the discrete solutions. Algebraic elimination converts "d such that congruence holds" into "roots of a polynomial" — an exact, non-probabilistic computation. Chebyshev polynomials T_n and U_n express cos(n·θ) and sin(n·θ)/sin θ as degree-n polynomials in cos θ with integer coefficients, so cos(s·arccos(u)) = T_s(u) is polynomial in u. The square roots √(1−u²) from sin φ can be cleared by squaring (after isolating them on one side of the equation), which doubles the degree. The final polynomial has integer coefficients (clearing the rational-function denominators from u, v) and degree bounded by about 2(c+s). For the oracle case (16,5,5,6) this is degree ~42 — easily handled exactly. For the full problem (c up to ~500) degree may reach ~1000, but Sturm sequences remain exact (rational arithmetic), and factorisation structure from the problem's symmetries likely reduces the effective degree.

status: grounded
precedent: https://www.cecm.sfu.ca/personal/monaganm/papers/trigpoly.pdf (Mulholland & Monagan: tangent half-angle substitution, trig polynomial → rational of degree ≤2d) ; https://en.wikipedia.org/wiki/Sturm%27s_theorem ; https://encyclopediaofmath.org/wiki/Sturm_theorem ; https://www-sop.inria.fr/hephaistos/logiciels/ALIAS/ALIAS-C++/node4.html ; https://link.springer.com/article/10.1007/BF02238233 (Chebyshev + Sturm exact root-location) ; https://hal.science/hal-00451221/document (exact real-root isolation of Chebyshev-composite polynomials) ; https://www.sciencedirect.com/science/article/abs/pii/002001909190020I (trig polynomials with simple roots) ; thread `offcentre-mesh-phase-model` (claim `offcentre_dual_mesh_phase_invariant`) ; sibling [[tangent-half-angle]] (grounded)
first-step: Derive the closed-form expressions for cos φ, cos χ, cos γ in terms of cos E for fixed c,s,t,d. Eliminate d using the relationship d = (c−s−2t)/(2π cos E). Substitute t_param = tan(E/2), express cos φ = u(t_param), cos χ = v(t_param) as rational functions. Then form the numerator of tan(s·φ + c·χ) = 0 via sin(s·φ+c·χ) = 0 using Chebyshev expansions, clear radicals, and count real roots via Sturm sequences.
```

## Research verdict — the machinery is grounded; the guarantee is upstream

This candidate is the same pipeline as the sibling `tangent-half-angle` (already
grounded in this run) with Chebyshev polynomials replacing the tangent
addition-formula route to the polynomial, plus Sturm sequences replacing naive
root counting. Every ingredient is standard exact computer algebra with a
source:

- **Tangent half-angle substitution θ→t=tan(θ/2)** is a ring morphism
  Q[sin,cos]→Q(t) with kernel ⟨s²+c²−1⟩; a trig polynomial of trigonometric
  degree d maps to a rational polynomial of degree ≤ 2d (Mulholland & Monagan,
  Lemma 3–4, invertible on the right class, Theorem 1). This *confirms* the
  candidate's degree bound (~2(c+s)) and that the result is rational in t.
- **Chebyshev identity** T_n(cos θ)=cos(nθ), U_{n−1}(cos θ)·sin θ=sin(nθ): lets
  cos(s·φ) and sin(s·φ) be written as T_s(u) and U_{s−1}(u)·√(1−u²) with u a
  rational function of t (hal.science/hal-00451221 uses exactly these
  identities for exact root work on Chebyshev-composite polynomials).
- **Sturm's theorem** counts real roots of a square-free real polynomial
  exactly in rational arithmetic (Wikipedia; Encyclopedia of Mathematics), and
  is the mechanism used by the INRIA ALIAS system ("Analyzing trigonometric
  equations"). A Chebyshev-plus-Sturm exact root-location algorithm is given in
  Computing 54 (1995) (link.springer.com/article/10.1007/BF02238233).

So the *technique* is a bona fide exact, non-scanning route to "count d-values
satisfying a phase congruence". It grounds the candidate as *machinery*.

**The guarantee for THIS problem is upstream, not in the technique.** The
polynomial is built from the W-model phase congruences of the thread
`offcentre-mesh-phase-model` (claim `offcentre_dual_mesh_phase_invariant`:
s·φ+c·χ−t·γ pairwise congruent, mirror-pair s·φ+c·χ ∈ πℤ). That model is
**oracle-unverified** — it has not reproduced g(16,5,5,6)=9, G(16)=9, G(20)=205.
If the W-model is right, this is the exact route to g; if wrong, the polynomial
root-counts a wrong condition. The substitution/Sturm machinery does not by
itself validate the discreteness.

Two technical caveats: (a) clearing the square roots √(1−u²), √(1−v²) by
squaring can inject spurious roots and blow the degree well past 2(c+s) — each
root must be re-checked against the original congruence (and against the
cross-type condition for the two planet sizes); (b) as `tangent-half-angle`
notes, the per-type position set is still forced by tangency (two mirror points
per type, thread claim `offcentre_two_positions_per_type`), which this
parametrisation respects only through the d-range.

Status: **grounded** as an exact root-counting route *conditional on*
`offcentre_dual_mesh_phase_invariant` holding. Refuted with it if that invariant
is ever refuted.

```claim
id: chebyshev_sturm_exact_root_count_grounded
statement: The pipeline 'rational parametrize the planet-centre ellipse by eccentric anomaly E → express cos phi, cos chi as Chebyshev of a rational function of cos E → substitute t=tan(E/2) (trig polynomial of trig-degree d maps to a rational of degree <=2d, Mulholland & Monagan) → clear radicals → count real roots exactly via Sturm's theorem' is a bona fide exact, non-scanning way to count the d-values at which a phase congruence of the W-model (s*phi+c*chi-t*gamma in pi*Z / 2pi*Z) holds.
hypotheses: Chebyshev identities T_n(cos)=cos(n.), U_{n-1}(cos)sin=sin(n.); tangent half-angle is a ring morphism Q[sin,cos]->Q(t); Sturm's theorem counts real roots of a square-free real polynomial exactly in rational arithmetic.
holds-here: yes for the machinery; the guarantee is UPSTREAM — the polynomial encodes the W-model phase condition (claim offcentre_dual_mesh_phase_invariant) which is oracle-unverified (has not reproduced g(16,5,5,6)=9). If that invariant is wrong the polynomial root-counts a wrong condition.
status: grounded (conditional).
bearing: gives the exact route to g once the W-model discreteness is validated; radical-clearing can inject spurious roots (re-check against the congruence) and blow the degree past 2(c+s).
anchor: research/approaches/algebraic-elimination-chebyshev.md (also sibling tangent-half-angle)
```


## Grounded — what the literature actually says vs. the candidate's claim

The candidate's central factual claims were confirmed by search:

1. Chebyshev's identity and the tangent-half-angle degree bound (≤2× trig
   degree) — confirmed (Mulholland & Monagan; hal-00451221).
2. Sturm's theorem for exact real-root counting — confirmed (Sources above).
3. That trig/polynomial exact root-counting is a practised, published pipeline
   — confirmed (Computing 54, 1995; INRIA ALIAS; about trig polynomials with
   simple roots, sciencedirect.com/article/abs/pii/002001909190020I).

Nothing in the literature contradicts the candidate; its dependency is entirely
upstream (the oracle-unverified W-model). This is why it is marked **grounded**
(conditional), not refuted.