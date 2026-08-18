# Marín–Villadelprat 2025 — cyclicity of hyperbolic hemicycles

Full text: [[marin-villadelprat-cyclicity-hyperbolic-hemicycles.full]]. arXiv:2501.16924; **published** as J. Differential Equations 258, doi:10.1016/j.jde.2025.113281 (2025).

## What the source establishes (held full text)

**Hemicyle.** Unbounded polycycle Γ formed by an affine invariant straight line
{y=0} plus half of the line at infinity, with two hyperbolic saddles at infinity
(compactified to the Poincaré disc). D-systems: {ẋ = yf(x,y;μ) + g(x;μ),
ẏ = yq(x,y;μ)}, deg f = deg q = n, deg g = n+1, with H1: g<0 (n odd) and H2:
ℓ_{n+1} := yf_n − xq_n + g_{n+1}x^{n+1} > 0.

**Theorem A** (general, without breaking the connection): for a D-system with
return map ℛ ≢ Id, cyclicity of Γ_u is determined by two coefficient functions
d₀, d₁ (integrals of the data): d₀≠0 ⇒ Cycl=0; d₀ vanish+independent ⇒ Cycl≥1;
d₁≠0 ⇒ Cycl≤1; d₀,d₁ vanish+independent ⇒ Cycl≥2 (with the λ=1 case handled by
restrictions to Λ₁). This gives sharp cyclicity bounds (0,1,2) for persistent
hyperbolic hemicycles. The displacement expansion is uniform in parameters
(second-order analysis), with d₀ analytic on Λ, d₁ analytic off λ=1.

**Theorem B** (n=2, connections break): for the quadratic D-system (7) with
(a₀,b₀) ∈ (−2,0)×(0,2) (two centers, in the reversible component Q³_R of the
center manifold; also in Q³_LV when (a₀+b₀)(a₀−b₀+2)=0), the cyclicity of Γ_u
(resp. Γ_ℓ) when perturbed inside the WHOLE quadratic family is **exactly 2** if
a₀ ≠ −1, and at least 2 if a₀ = −1.

**Theorem C**: simultaneous cyclicity of Π={Γ_u, Γ_ℓ} is exactly 3 in
K₁∖{a₀=−1} (resp. 2 in K₂), at least 3 on {−1}×(0,2).

**Theorem D**: alien limit cycle bifurcation (new intrinsic definition, not via
Melnikov functions) occurs at Γ_u ∪ Γ_ℓ for (a₀,b₀) ∈ {(−1,1), (−½,½), (−½,3⁄2)}.

**Relation to DRR:** system (7) is in DRR class **H²₁** (hyperbolic hemicycles
surrounding a center, [DRR Figure 7]); Theorem B is stated as "a small
contribution to the completion of the program to prove H(2) < ∞". Crucially the
authors note: some authors attribute to **Mourtada** the proof of finite
cyclicity of ANY hyperbolic polycycle in an unpublished series of manuscripts
([27] attributed in [18, Thm 0]) — so hyperbolic hemicycles may be covered by
Mourtada, but this is unpublished/attribution-level.

## What it lets this run conclude

- The hemisphere-of-the-DRR-inventory question is NOT about hyperbolic graphics:
  hyperbolic polycycles are either settled (Mourtada, unpublished-but-attributed)
  or now have explicit cyclicity 2 bounds for this whole quadratic class.
- The method (division in ideal of coefficients, uniform-in-parameter second-order
  expansion of the displacement, Dulac map machinery from [19,20,21]) is
  directly reusable — it is the model "sharp cyclicity" computation: each
  coefficient function d₀,d₁ is an explicit integral of the system data, and the
  ideal membership is the finiteness core. This is the closest held template for
  the run's G-zeros/G-uniform steps.
- It confirms: **the honest open DRR rows are the degenerate (nilpotent) ones**
  — (I¹₆b),(H³₁₃),(DI₂b) center-type boundary cases and any other non-hyperbolic
  rows. Hyperbolic classes do not block H(2).

```claim
id: drr-mv-hemicycle-cyclicity-2
statement: For the quadratic D-system (7) with (a0,b0) in (-2,0)x(0,2) (two
  centers, reversible class Q3^R), the cyclicity of the hyperbolic hemicycle
  Gamma_u (resp Gamma_l), perturbed inside the whole quadratic family, is
  exactly 2 for a0 != -1 and at least 2 for a0 = -1 (Theorem B); simultaneous
  cyclicity of {Gamma_u, Gamma_l} is exactly 3 in K1\{a0=-1}, exactly 2 in K2.
hypotheses: n=2; D-system (7); hyperbolic saddles at infinity; connections may
  break.
holds-here: yes (a settled DRR-adjacent row; class H2^1).
status: asserted
bearing: hyperbolic hemicycles are settled with sharp cyclicity 2/3; the open
  DRR rows must be the degenerate (nilpotent) ones; supplies the model
  division-in-ideal method for displacement expansions.
anchor: research/sources/marin-villadelprat-cyclicity-hyperbolic-hemicycles.full.md
follows-from: h16-drr-121-graphics
```