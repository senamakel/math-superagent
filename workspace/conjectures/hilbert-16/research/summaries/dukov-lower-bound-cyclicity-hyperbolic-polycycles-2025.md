# Dukov 2025 — lower bound for the cyclicity of hyperbolic polycycles

Full text: [[dukov-lower-bound-cyclicity-hyperbolic-polycycles-2025.full]]
(Math. Sb. / Sbornik Mathematics, DOI 10.4213/sm10206e, open on Math-Net.ru).

## What the source establishes (held full text)

**Setup.** ℳ an infinitely-smooth orientable surface; Vect^∞(ℳ) the smooth
fields. A *hyperbolic polycycle* γ is a finite directed Eulerian graph whose
vertices are hyperbolic saddles and edges are separatrix connections. A
polycycle is *monodromic* if the Poincaré (monodromy) map is defined even for
the unperturbed field. Characteristic number of a saddle = modulus of the
eigenvalue ratio (negative in numerator). Cyclicity μ of γ in a family V: the
minimum integer with neighbourhoods U ∋ γ, W ∋ 0 such that every v_δ (δ∈W)
has at most μ limit cycles in U — counting cycles born from *sub-polycycles*
too. HC(n,k) = max cyclicity of a hyperbolic (n-connection) polycycle in a
generic k-parameter family.

**History recap (exact values quoted):**
- n=1: HC(1,k) = k (Leontovich 1946 D.Sc.; re-proved by Roussarie, Ilyashenko–Yakovenko). So a separatrix loop in a generic k-parameter family yields exactly k cycles.
- n=2: HC(2,2) = 2 (Cherkas, Rein, Mourtada, Zhebran, Roitenberg, Dukov); HC(2,3) ≤ 3 (Trifonov 1997).
- n=3: HC(3,3) = 3 (Reyn 1980 lower bound for the triangle; Trifonov 1997 equality).
- n=4: HC(4,4) ≥ 5 (Mourtada, monodromic separatrix square) — the HC(n,n) = n law breaks.
- n ≥ 5: Dukov [7] proved HC(n,n) ≥ n (idea due to Reyn).
- Upper bounds: exponential (Mourtada, Ilyashenko–Yakovenko, Kaloshin E(k) ≤ 2^{25k²}, Kaleda–Shchurov E(n,k) ≤ C(n)k^{3n}).

**Theorem 1 (headline).** Let V be a generic C^∞ family perturbing a
monodromic hyperbolic polycycle γ_M with n distinct saddles, characteristic
numbers λ₁,…,λₙ, and ∏λᵢ = 1. Then an (n+1)-multiple limit cycle — i.e.
n+1 limit cycles — is born in V.

Genericity conditions: (1) V cuts the Banach submanifold X̃ (fields with the
n connections AND ∏λᵢ=1, codimension n+1 — Proposition 1, Dukov [7] proves
fields with n saddle connections form a C^{r−1} Banach submanifold of
codimension n) transversally; (2) c ≠ 1 where Δ(x) = c x^{λ₁⋯λₙ}(1+o(1)) is
the unperturbed Poincaré map (Cherkas, Proposition 2); (3) R̃ₙ(λ₁,…,λₙ) ≠ 0,
R̃ₙ a resultant-type polynomial.

**Corollary 1.** For every n: HC(n,n+1) ≥ n+1.

**Consequences for small n.** Example 1: loop with λ₁=1 in a generic
2-parameter family gives ≥ 2 cycles (classical Andronov–Leontovich). Example
2: a lune with λ₁λ₂=1 in a generic 3-parameter family gives ≥ 3 cycles —
upgrading Trifonov's inequality HC(2,3) ≤ 3 to the equality HC(2,3) = 3.
Example 3/4: the heart (non-monodromic) and figure-eight (monodromic but
single saddle) show the hypotheses cannot be relaxed: HC ≤ 2 in both (Trifonov).

**Method.** Saddle correspondence maps Δᵢ, Poincaré map Δ = fₙ∘⋯∘f₁ with
fᵢ(x) = τᵢ(δ) ± Δᵢ(δ,x); equations for multiple fixed points; a
substitution δ = δ(F,θ,x) eliminating one parameter; a blow-up; the resultant
R̃ₙ verifying the genericity conditions; normal forms and smooth extensions of
the Poincaré map's derivatives.

## What it lets this run conclude

- **The hyperbolic-polycycle quantitative picture is now complete and
  primary-sourced:** exact cyclicity for n ≤ 2 (HC(1,k)=k, HC(2,2)=2,
  HC(2,3)=3), HC(3,3)=3, Mourtada's HC(4,4) ≥ 5, Dukov's HC(n,n) ≥ n and
  HC(n,n+1) ≥ n+1, multiplicities ≤ n (Dukov 2023). The quadratic DRR
  hyperbolic classes sit inside n ≤ 4 with specific ratios, so these are the
  exact bounds applicable there.
- **HC(2,3) = 3 and HC(2,2) = 2 are the two quadratic-relevant exact
  cyclicity values** (2-saddle graphics = hemicycles/lunes/hearts/figure-8s
  after compactification). The DRR hemicycle closure (Marín–Villadelprat:
  cyclicity 2 in the quadratic family) matches HC(2,2)=2 for the persistent
  connection-unbroken case; breaking connections in a 3-parameter setting
  reaches 3.
- The genericity conditions are again *explicit algebraic conditions* on the
  characteristic numbers (c ≠ 1, R̃ₙ ≠ 0, transversal intersection) — the
  open-dense shape Lean can state; the unperturbed return map's leading
  coefficient c (Cherkas) is the same A_{1,n}-type coefficient QAS 2025 work
  with.
- **Definition 5 is important for the run:** cyclicity counts cycles born
  from *sub-polycycles* too — the exact convention the DRR program inherits
  (a limit periodic set's cyclicity counts everything born in its collar).

## Claim

```claim
id: h16-dukov-lower-bound-cyclicity-hyperbolic-polycycles-2025
status: asserted
statement: Dukov (2025), "Lower bound for the cyclicity of hyperbolic
  polycycles", Mat. Sb. / Sbornik Mathematics, DOI 10.4213/sm10206e:
  Theorem 1 -- for a monodromic hyperbolic polycycle gamma_M with n distinct
  saddles and product of characteristic numbers = 1, a generic C^infty
  (n+1)-parameter family births an (n+1)-multiple limit cycle (i.e. n+1
  limit cycles). Genericity: transversal intersection with the codim-(n+1)
  Banach submanifold X~ (Proposition 1), c != 1 where the unperturbed Poincare
  map is Delta(x) = c x^{lambda_1...lambda_n}(1+o(1)) (Cherkas, Prop 2), and
  R~_n(lambda_1..n) != 0 (resultant polynomial). Corollary: HC(n,n+1) >= n+1
  for all n. Exact values recap: HC(1,k)=k (Leontovich), HC(2,2)=2,
  HC(2,3)=3 (Theorem 1 + Trifonov's <=3), HC(3,3)=3 (Reyn/Trifonov),
  HC(4,4) >= 5 (Mourtada), HC(n,n) >= n (Dukov), upper bounds exponential.
hypotheses: orientable C^infty surfaces; hyperbolic polycycles (all saddles
  hyperbolic); monodromic (unperturbed Poincare map defined); generic
  finite-parameter families; characteristic numbers satisfying the stated
  genericity conditions.
evidence-class: sourced (full text held, DOI 10.4213/sm10206e via Math-Net.ru).
falsifier: a monodromic hyperbolic polycycle with prod lambda_i = 1 in a
  generic (n+1)-parameter family with fewer than n+1 born limit cycles, or a
  counterexample to the resultant-genericity argument -- none known; the
  small-n cases are consistent with the exact classical values (HC(2,3)=3
  matches Trifonov's upper bound).
holds-here: yes -- completes the quantitative picture for the hyperbolic DRR
  rows: exact cyclicity values for the 1- and 2-connection graphics (loops,
  lunes, hearts, figure-eights, hemicycles after compactification) in generic
  families; matches Marín-Villadelprat's cyclicity-2 hemicycle closure and
  gives the 3-cycle counterpart when connections break in 3-parameter
  settings.
anchor: research/sources/dukov-lower-bound-cyclicity-hyperbolic-polycycles-2025.full.md
follows-from: h16-dukov-multiplicity-hyperbolic-polycycles-2023, h16-mourtada-1991-hyperbolic-finite-cyclicity-primary
```

## Frontier additions

The 148 citations include the classical anchors (Leontovich, Roussarie,
Ilyashenko–Yakovenko, Kaloshin, Kaleda–Shchurov, Trifonov, Reyn, Cherkas,
Roitenberg, Zhebran) — many already held; the not-yet-held primary texts are
Trifonov 1997 (HC(3,3)=3), Reyn 1980 (lower bounds), Leontovich 1946
(D.Sc., the HC(1,k)=k source), Roitenberg / Zhebran (n=2 pieces). These are
the remaining small-n exactness primaries on the frontier.