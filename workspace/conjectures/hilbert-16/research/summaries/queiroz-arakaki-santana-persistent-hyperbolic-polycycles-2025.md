# Queiroz Arakaki–Santana 2025 — cyclicity of persistent hyperbolic polycycles

Full text: [[queiroz-arakaki-santana-persistent-hyperbolic-polycycles-2025.html.full]]
(arXiv:2504.07225, math.DS, 2025; published J. Dyn. Diff. Eq., DOI 10.1007/s10884-025-10469-9).

## What the source establishes (held full text)

**Setup.** {X_μ} a smooth family of planar *analytic* vector fields, Λ ⊂ ℝ^N,
with a **persistent** polycycle Γ: n hyperbolic saddles p₁,…,pₙ, none of the
separatrix connections breaking along the family. The return map
ℛ(s; μ) = Dₙ ∘ ⋯ ∘ D₁(s; μ) is the composition of the Dulac maps Dᵢ of the
saddles, and its isolated fixed points are the limit cycles. Graphic number
r(μ) = ∏ λᵢ(μ), λᵢ the hyperbolicity ratio of pᵢ.

**Theorem A** (the return map of a persistent polycycle is a Dulac-type germ):
For any ℓ ∈ (0, min{Λ_{i,n} : i = 0,…,n}) the first return map is

  ℛ(s; μ) = s^{r(μ)}(A_{1,n} + ℱ_ℓ^∞(μ₀))

with ℱ_ℓ^∞(μ₀) a remainder ℓ-flat at s=0 uniformly in μ near μ₀. Consequently:
- (a) Cycl(Γ, μ₀) = 0 if r(μ₀) ≠ 1;
- (b) Cycl(Γ, μ₀) ≥ 1 if r(μ₀) = 1, r(μ)−1 changes sign at μ₀ and
  ℛ(·; μ₀) ≢ Id;
- (c) Cycl(Γ, μ₀) ≤ 1 if A_{1,n}(μ₀) ≠ 1;
- (d) Cycl(Γ, μ₀) ≥ 2 if r(μ₀) = A_{1,n}(μ₀) = 1, the functions r−1 and
  A_{1,n}−1 are independent at μ₀ and ℛ(·; μ₀) ≢ Id.

The A_{i,n} are explicit leading coefficients built from the Dulac-map
coefficients Δ_{jk}^i (themselves C^∞ in (λ, μ) off the resonant set).

**Theorem B** (refined expansion ⇒ higher cyclicity). With the saddles split
λᵢ(μ₀) < 1 for i ≤ m and > 1 for i > m, set Λ_{0,m} = ∏_{i≤m} λᵢ. Then

  ℛ(s; μ) = s^{r(μ)}(A_{1,n} + 𝒜 s^{Λ_{0,m}} + ℱ_ℓ^∞(μ₀)), ℓ ∈ (Λ_{0,m}⁰, min{r(μ₀), 2Λ_{0,m}⁰, 1})

with 𝒜 = Λ_{m,n}A_{1,m}A_{1,n}(S₁^{m+1} − S₂^m). Then:
- (a) Cycl(Γ, μ₀) ≤ 2 if 𝒜(μ₀) ≠ 0;
- (b) Cycl(Γ, μ₀) ≥ 3 if r = A_{1,n} = 1, 𝒜(μ₀) = 0, r−1, A_{1,n}−1, 𝒜
  independent at μ₀, ℛ(·; μ₀) ≢ Id.

To get the non-leading term of the return map it is enough to know the
non-leading terms of the Dulac maps of indices m and m+1 (the interface of the
λ<1 and λ>1 blocks).

**Theorems C/1** (displacement-map equivalence): the analogous statement holds
for the displacement map ℛ(s;μ) − s with the same coefficients; the two notions
are interchangeable for cyclicity computations.

**Appendix B (Prop 4/5)** (from MV [13]): explicit formulas for the Dulac-map
coefficients Δ_{10}, Δ_{01} in terms of S₁, S₂ with
Δ_{10} = λ·Δ₀₀·S₁, Δ_{01} = −(Δ₀₀)²·S₂ — the concrete data one would compute
for a specific polycycle.

**Application (Thm 2)**: a persistent polycycle of a game-theory ODE model has
its cyclicity determined by the criteria above.

## What it lets this run conclude

- **The return map of a persistent hyperbolic polycycle is a short
  Dulac-type germ s^{r(μ)}(A + flat)**, whose cyclicity is read off the
  coefficients r−1, A_{1,n}−1, 𝒜 — the leading coefficients play exactly the
  role the focus case's Lyapunov quantities do. This is the model for
  "finitely many coefficients decide the whole germ" that Roussarie's reduction
  needs at a hyperbolic vertex.
- The theorem composes Dulac maps: the flat-class calculus (finitely flat
  remainders, uniform in μ) is the analyticity-enters-here step — **the Test-1
  (smooth-test) relevant to this class**, because the ℱ_ℓ^∞ remainder is flat
  but need not be analytic; analyticity of the input fields is what the
  expansion uses.
- It confirms the persistent (connections unbroken) scenario is *simpler*:
  cyclicity 0/1/2/3 decided by the first three coefficients, exactly the shape
  the DRR hemicycle closures use (Marín–Villadelprat d₀,d₁).
- Persistent polycycles cannot be the source of the open DRR rows: if the
  graphic number ≠ 1 the cyclicity is 0. The open rows must be either
  non-persistent (connections break) or non-hyperbolic.

## Claim

```claim
id: h16-persistent-polycycle-cyclicity-qas2025
status: asserted
statement: Queiroz Arakaki-Santana (2025), "On the cyclicity of persistent
  hyperbolic polycycles", arXiv:2504.07225 / J. Dyn. Diff. Eq. (2025): for a
  smooth family of planar analytic fields with a persistent polycycle Gamma (n
  hyperbolic saddles, graphic number r(mu) = prod lambda_i(mu)), the first
  return map is R(s;mu) = s^{r(mu)}(A_{1,n} + F_ell^infty(mu_0)) with flat
  remainder uniform in mu. Cyclicity criteria: (a) r(mu_0) != 1 => Cycl = 0;
  (b) r(mu_0)=1, r-1 changes sign, R(.;mu_0) not Id => Cycl >= 1; (c)
  A_{1,n}(mu_0) != 1 => Cycl <= 1; (d) r = A_{1,n} = 1, r-1 and A_{1,n}-1
  independent, R not Id => Cycl >= 2. Theorem B refines: with lambdas < 1 on
  the first m saddles, R = s^r (A_{1,n} + A s^{Lambda_{0,m}} + flat),
  A = Lambda_{m,n} A_{1,m} A_{1,n} (S_1^{m+1} - S_2^m); A(mu_0) != 0 => Cycl
  <= 2; and under A=0 + independence of r-1, A_{1,n}-1, A => Cycl >= 3.
hypotheses: planar analytic vector fields; persistent polycycle (no separatrix
  connection breaks); hyperbolic saddles; hyperbolicity ratios as parameters;
  return map on a transversal; cyclicity in the sense of bifurcating limit
  cycles near Gamma.
evidence-class: sourced (arXiv full text held,
  research/sources/queiroz-arakaki-santana-persistent-hyperbolic-polycycles-2025.html.full.md;
  published DOI 10.1007/s10884-025-10469-9).
falsifier: an error in the composition/flat-class argument for the return map
  leading terms (rests on Marin-Villadelprat Dulac-map coefficient formulas);
  or a persistent hyperbolic polycycle with Cycl larger than the criteria
  predict (e.g. Cycl >= 2 with A != 1) -- no counterexample known.
holds-here: yes as the model "short Dulac germ decided by finitely many
  coefficients" for the persistent/hyperbolic part of the DRR inventory; the
  open DRR rows are non-persistent or non-hyperbolic, so this closes no open
  row by itself but fixes the exact shape the displacement argument must take
  at hyperbolic vertices.
anchor: research/sources/queiroz-arakaki-santana-persistent-hyperbolic-polycycles-2025.html.full.md
follows-from: h16-hyperbolic-polycycle-cyclicity-lower-bound-bgs2024
```

## Frontier additions

The Dulac-map coefficient data trace to Marín–Villadelprat 2020/21/24
(refs [10],[11],[13]) — the same trilogy BGS 2024 relies on. The
three-primary-source gap (Mourtada Ann. Inst. Fourier 1991; MV JDE 2020;
MV JDE 2021) is the next most valuable acquisition for the displacement-map
instrument chain.