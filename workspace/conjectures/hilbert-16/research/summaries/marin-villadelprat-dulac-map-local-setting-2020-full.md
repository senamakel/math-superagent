# Marín–Villadelprat 2020 — asymptotic expansion of the Dulac map/time, local setting

Full text: [[marin-villadelprat-dulac-map-local-setting-2020-full.full]]
(accepted version, URV repository; J. Differential Equations 269(10):8425–8467,
2020, DOI 10.1016/j.jde.2020.06.024). **A corrigendum exists** (Marín–
Villadelprat, 2026 — see frontier/SSRN record) — the corrected statements must be
read before relying on this paper quantitatively.

## What the source establishes (held full text)

**Setup.** C^∞ unfolding {X_μ}_{μ∈V} of a hyperbolic saddle at the origin,
X_μ = A(x,y;μ)x∂x + B(x,y;μ)y∂y, A>0, B<0, hyperbolicity ratio
λ(μ) = −B(0,0;μ)/A(0,0;μ). The polar factor 1/(x^m y^n) is allowed (to cover
saddles at infinity in the Poincaré disc / divisor points after desingularizing
degenerate singularities — the exact DRR situation). By the normal-form theorem
[10, Thm A], near a resonance λ₀ = p/q the family is C^k-conjugated to

  Y_μ^NF = 1/(η(μ) x^m y^n + u^ℓ Q(u;μ)) ( x∂x + (−λ(μ) + P(u;μ)) y∂y ),  u = x^p y^q,

and for λ₀ irrational P = Q = 0 (the Dulac map is then explicit).

**Key notion — flatness with parameters.** ψ ∈ F^K_L(μ̂): for all
ν = (ν₀,…,ν_N), |ν| ≤ K, there is a neighbourhood V of μ̂ and C,s₀ > 0 with
|∂_s^{ν₀}∂_μ^{ν₁…ν_N} ψ(s;μ)| ≤ C s^{L−ν₀} for s ∈ (0,s₀), μ ∈ V. This is
**stronger** than the usual "flat in s only" notion: it also bounds mixed
s/μ-derivatives. The Ecalle–Roussarie compensator:
ω(s;κ) = (s^{−κ}−1)/κ (κ≠0), = −ln s (κ=0), and (s,κ)↦ω ∈ F^∞_{−ε}({κ<ε}).

**Theorem A (local Dulac map).** For the Dulac map D(·;α) of X_α = x∂x +
(1/q)(−p + Σ_{i=0}^{N−1} α_{i+1} u^i) y∂y between (0,1)×{1} and {1}×(0,1),
for each L ∈ ℝ there is a unique ∆(z,w;α) ∈ ℚ[z,w,α] with
deg_(z,w) ∆ ≤ L/(p) − 1/q, and D_L ∈ F^∞_L(U₀), U₀ = {α₁ = 0}, such that

  D(s;α) = s^λ ∆(s^p, s^p ω; α) + D_L(s;α),   ω = ω(s;α₁), λ = λ(α₁).

∆(0,0;α) = 1 if L ≥ p/q, ∆ ≡ 0 otherwise. So the Dulac map is the linear
saddle's map s↦s^λ times a polynomial in s^p and s^p·(deformed log), plus a
remainder flat (with parameters) at s = 0.

**Theorem B (local Dulac time).** Let κ = ⌈max(m/p, n/q)⌉ ≥ 0. Then for each L:

  T(s;α,β) = τ₀(β) ln s + s^{λn} τ₁(s^p, s^p ω; α,β) − s^m τ₁(s^p, 0; α,β)
              + s^{κp} τ₂(s^p, s^p ω; α,β) + T_L(s;α,β)

with τ₀ ∈ ℚ[β], τ₁ ∈ ℚ(α₁)[z,w,α₂,…,α_N,β] linear in β and pole-free along
α₁=0, τ₂ ∈ ℚ[z,w,α,β] linear in β with τ₂(z,0;α,β)=0; τ₁ = 0 if mq−np = 0;
τ₀ = −β₀ if (m,n)=(0,0), = −β₁ if ℓ=0, else 0. Remainder T_L ∈ F^∞_L(U₀×ℝ^{M+1}).

**Remark 1.4 — a gap in Roussarie [14],[15],[16] is identified and fixed.** The
very similar Theorem F in Roussarie [14] (also Theorem 14 in [15, p.103]) proves
only s-derivative flatness of the remainder, but *states* it extends to a C^L
function in (s,α) at s=0 — "this inexactness yields to a crucial gap in a
subsequent paper by the same author [16]" (smoothness of the bifurcation diagram
of the generic codim-2 saddle-loop unfolding), where an ad hoc implicit function
theorem is applied to the (unproved) smooth remainder. MV's Theorem A proves the
stronger F^∞_L class and Lemma A.1 shows any F^K_L (L>K) function extends C^K at
{0}×U₀ — filling the gap between statement and proof of [14, Thm F] and
validating [16, Prop 3.2]. (They credit their motivation: "this was in fact our
initial motivation to tackle the problem.")

## What it lets this run conclude

- **This is the primary instrument for the displacement-function analysis at a
  hyperbolic vertex**: the expansion D(s;α) = s^λ·poly(s^p, s^pω;α) + flat is
  exactly the shape BGS 2024 and QAS 2025 quote and refine; the finitely-flat
  remainder with *parameter* derivatives is what makes cyclicity bounds uniform
  in parameters (the "uniformity comes from here" step).
- **The smooth-test (Test 1 of problem.md) is sharpened by Remark 1.4**: a flat
  remainder that merely *vanishes fast in s* does not determine the map — the
  historical failure mode (Dulac 1923; Roussarie's Theorem-F gap). The fix is
  the stronger parameter-uniform flatness, which is where analyticity/regularity
  enters. Any argument this run builds must carry the F^∞_L class, not just
  s-flatness.
- **Corrigendum pending**: the 2026 corrigendum to this paper must be read
  before quantitative use; the main theorems' statements may shift in the
  corrected version. Record as open check.
- For the DRR rows: saddles at infinity and divisor points (the polar factor
  x^m y^n) are explicitly in scope — this is the local tool the hemicycle /
  elementary-graphics closures (DGR 2002; MV 2025) rest on.

## Claim

```claim
id: h16-mv-dulac-map-local-expansion-2020
status: asserted
statement: Marin-Villadelprat (2020), "Asymptotic expansion of the Dulac map
  and time for unfoldings of hyperbolic saddles: local setting", JDE
  269(10):8425-8467: for a C^infty unfolding of a hyperbolic saddle with
  hyperbolicity ratio lambda = p/q (p,q coprime) and polar factor 1/(x^m y^n),
  the local Dulac map and Dulac time admit expansions
  D(s;alpha) = s^lambda Delta(s^p, s^p omega; alpha) + D_L(s;alpha),
  T(s;alpha,beta) = tau_0(beta) ln s + s^{lambda n} tau_1(...) - s^m tau_1(...)
  + s^{kappa p} tau_2(...) + T_L(s;alpha,beta),
  with remainder D_L, T_L in the parameter-uniform flat class F^infty_L
  (mixed s/mu derivatives bounded by C s^{L-nu_0}), Delta polynomial with
  rational coefficients, and the Ecalle-Roussarie compensator omega(s;kappa)
  = (s^{-kappa}-1)/kappa. Remark 1.4 identifies and fixes a gap in Roussarie's
  Theorem F (the remainder was only shown s-flat yet stated C^L in (s,alpha)),
  which had caused a gap in Roussarie's later saddle-loop bifurcation-diagram
  paper [16]; the parameter-uniform flatness F^infty_L is what validates the
  implicit-function step. A 2026 corrigendum to this paper exists (SSRN) and
  must be read before quantitative use.
hypotheses: planar C^infty unfoldings of hyperbolic saddles; resonance
  lambda_0 = p/q rational (irrational case explicit); transverse sections close
  enough to the saddle that normal-form coordinates apply (the "local setting"):
  sections at arbitrary distance require the general-setting successor paper.
evidence-class: sourced (accepted full text held from URV repository,
  research/sources/marin-villadelprat-dulac-map-local-setting-2020-full.full.md;
  DOI 10.1016/j.jde.2020.06.024; corrigendum SSRN 2026 recorded, not held).
falsifier: an error in the corrigendum that changes Theorem A/B statements, or
  a counterexample to the parameter-uniform flatness claim for the remainder
  (the paper itself demonstrates why s-only flatness fails with s^mu-type
  examples) -- none known at this level; the corrigendum is the live check.
holds-here: yes -- the local instrument for every hyperbolic saddle vertex of a
  DRR graphic including saddles at infinity (polar factor); the shape
  s^lambda * poly(s^p, s^p*omega) + flat(parameter-uniform) is what BGS 2024 and
  QAS 2025 quote, and the flatness-with-parameters is the uniformity step this
  run must carry through its own arguments.
anchor: research/sources/marin-villadelprat-dulac-map-local-setting-2020-full.full.md
follows-from: h16-mourtada-1991-hyperbolic-finite-cyclicity-primary
```

## Corrigendum status (open check)

The 2026 corrigendum (SSRN 6809315 / JDE) to this exact paper was surfaced in
search; not held. The general-setting (JDE 275, 2021) and coefficient-properties
(JDE 404, 2024) successors build on this — they are the next acquisitions in
this instrument chain. Coefficient-properties arXiv:2105.09785 is now held
(`marin-villadelprat-dulac-coefficient-properties-2024-arxiv.full.md`).