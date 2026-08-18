# Dukov 2023 — multiplicities of limit cycles from perturbed hyperbolic polycycles

Full text: [[dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.html.full]]
(arXiv:2201.03652; Russian original Mat. Sb. 214(2):90–111, 2023; trans.
Sb. Math. 214(2):226–245, DOI 10.4213/sm9747e).

## What the source establishes (held full text, Russian with abstract)

**Setup.** A hyperbolic polycycle γ of a smooth field v₀ on an orientable
surface, formed by n separatrix connections of hyperbolic saddles
S₁,…,Sₙ (some may coincide), with characteristic numbers λ₁,…,λₙ
(λ_i = |λᵢˢ|/λᵢᵘ — modulus of the ratio, negative eigenvalue in the
numerator). A limit cycle of multiplicity m is born from γ in a family
{v_δ} if a sequence of parameter values δ_α → 0 gives fields with limit
cycles LC(δ_α) of multiplicity m converging in Hausdorff metric to γ or a
nonempty part of it.

**Main results.**

- **Theorem 1**: perturbing γ in a *typical* n-parameter family, the
  multiplicity of every born limit cycle is ≤ n. Typicality condition: the
  characteristic numbers satisfy ℒₙ(λ₁,…,λₙ) ≠ 0, where ℒₙ is a nontrivial
  polynomial that can be chosen independent of γ and v₀ (it arises as the
  resultant of a polynomial system whose nontrivial solution corresponds to
  the existence of a multiple limit cycle).
- **Corollary**: if v₀ ∈ Vect^∞(M) with such γ and (1) holds, then in the
  whole space Vect^∞(M) no limit cycle of multiplicity > n is born from γ.
- **Theorem 2** (explicit small-n typicality polynomials):
  ℒ₁(λ₁) = Λ₁(λ₁);
  ℒ₂(λ₁,λ₂) = Λ₂(λ₁,λ₂);
  ℒ₃(λ₁,λ₂,λ₃) = Λ₃(λ₁,λ₂,λ₃);
  ℒ₄(λ₁,λ₂,λ₃,λ₄) = Λ₄(λ₁,λ₂,λ₃,λ₄) · M(λ₁,λ₂,λ₃)M(λ₁,λ₂,λ₄)M(λ₁,λ₃,λ₄)M(λ₂,λ₃,λ₄),
  where Λₙ(λ₁,…,λₙ) = ∏_{I≠(0,…,0)} (λ^I − 1) over multi-indices I with
  components in {0,1} (e.g. Λ₂ = (λ₁−1)(λ₂−1)(λ₁λ₂−1)) and
  M(λ₁,λ₂,λ₃) = 4(λ₁λ₂λ₃−1) − (λ₁−1)(λ₂−1)(λ₃−1).

**Method.** The Poincaré map Δ(δ,·) = fₙ∘⋯∘f₁ with fᵢ(x) = τᵢ(δ) ± Δᵢ(δ,x)
(Δᵢ the saddle correspondence maps). A limit cycle of multiplicity ≥ n+1
gives Δ = x, Δ′ = 1, Δ^{(l+1)} = 0 (l=1,…,n−1). Passing to 𝒟 = ln Δ′, the
high derivatives of 𝒟 take a convenient form Σ ln|fᵢ′(F_{i−1})|; the
existence of a multiple fixed point is turned into a polynomial system in
the λᵢ with a nontrivial solution; the resultant ℒₙ ≠ 0 kills those
solutions. History recapped: E(1)=1 (Andronov–Leontovich/Hopf), E(2)=2
(1970s–1993, Mourtada/Roussarie/Rousseau/Dumortier etc.), E(3)=3 (Trifonov
1997), Ilyashenko–Yakovenko E(k)<∞, Kaloshin E(k) ≤ 2^{25k²}, Kaleda–
Shchurov E(n,k) ≤ C(n)k^{3n}, C(n)=2^{5n²+20n}.

## What it lets this run conclude

- **This is the g-zeros-side bound for hyperbolic polycycles**: not how many
  cycles, but how *degenerate* each can be. A multiplicity bound is what the
  "bounded number of zeros of the displacement function" step needs when the
  zero count is done via multiplicity (counting roots with multiplicity).
- **The typicality polynomials are explicit and algebraic in the
  characteristic numbers** — a finite, checkable witness (Λₙ, M) exactly in
  the shape Lean can certify. The condition ℒₙ ≠ 0 is an open dense
  condition, matching Mourtada's G(k) generic conditions.
- Together with BGS 2024's lower bound Δ(Γⁿ) and the finite cyclicity upper
  bounds (Mourtada 1991), the hyperbolic-polycycle side now has: generic
  finite cyclicity (upper), explicit lower bounds, AND multiplicity bounds.
  The three are the full quantitative picture available for the hyperbolic
  class.
- It is consistent with (and sharpens) the smooth-test: the multiplicity
  bound is proved in Vect^∞ — no analyticity needed — exactly because the
  bound is *multiplicity* (an algebraic/differentiable statement), not a
  *count* of distinct cycles. The count needs analyticity (that is where
  G-transition's almost-regular expansions enter); the multiplicity cap does
  not.

## Claim

```claim
id: h16-dukov-multiplicity-hyperbolic-polycycles-2023
status: asserted
statement: Dukov (2023), "Multiplicities of limit cycles appearing after
  perturbations of hyperbolic polycycles", Mat. Sb. 214(2):90-111 / Sb. Math.
  214(2):226-245, arXiv:2201.03652: for a hyperbolic polycycle gamma with n
  separatrix connections of saddles with characteristic numbers lambda_1..n,
  in a typical n-parameter family (condition L_n(lambda_1..n) != 0, L_n a
  nontrivial resultant polynomial independent of gamma and v_0), every limit
  cycle born from gamma has multiplicity at most n; consequently no limit
  cycle of multiplicity > n is born from gamma in Vect^infty(M). For n <= 4
  explicit typicality polynomials: L_1 = Lambda_1, L_2 = Lambda_2,
  L_3 = Lambda_3, L_4 = Lambda_4 * prod_{3-subsets} M, where
  Lambda_n = prod_{I != 0, I in {0,1}^n} (lambda^I - 1) and
  M(a,b,c) = 4(abc-1) - (a-1)(b-1)(c-1).
hypotheses: planar/orientable-surface smooth vector fields; hyperbolic
  polycycle (all singularities hyperbolic saddles); finite-parameter families;
  typicality = characteristic numbers outside the zero set of L_n (an open
  dense condition); multiplicity of a fixed point of the Poincare map.
evidence-class: sourced (arXiv full text held,
  research/sources/dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.html.full.md;
  published DOI 10.4213/sm9747e).
falsifier: a hyperbolic polycycle satisfying L_n != 0 in a typical n-parameter
  family with a born limit cycle of multiplicity > n -- the paper's resultant
  argument is the proof that the polynomial system for a multiple fixed point
  has only the trivial solution; a counterexample would have to break that
  reduction. None known.
holds-here: yes -- the multiplicity-side bound for the g-zeros node applied to
  hyperbolic DRR rows; the explicit Lambda_n/M polynomials are Lean-statably
  checkable algebraic witnesses; complements Mourtada 1991 (finite cyclicity)
  and BGS 2024 (lower bounds).
anchor: research/sources/dukov-multiplicity-limit-cycles-hyperbolic-polycycles-2023-arxiv.html.full.md
follows-from: h16-mourtada-1991-hyperbolic-finite-cyclicity-primary, h16-hyperbolic-polycycle-cyclicity-lower-bound-bgs2024
```

## Frontier additions

The 2025 companion (Dukov, "Lower bound for the cyclicity of hyperbolic
polycycles", DOI 10.4213/sm10206e — generic (n+1)-parameter family gives ≥
n+1 cycles when ∏λᵢ = 1) is open on Math-Net and is the natural next
acquisition in this chain; also the Mourtada resonance/Leontovich history
items referenced. Both are recorded on the frontier.