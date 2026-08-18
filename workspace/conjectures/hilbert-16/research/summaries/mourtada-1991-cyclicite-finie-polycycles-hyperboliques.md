# Mourtada 1991 — finite cyclicity of hyperbolic polycycles (primary)

Full text: [[mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.full]]
(Ann. Inst. Fourier 41(3):719–753, 1991, DOI 10.5802/aif.1271, open access on
Numdam/Centre Mersenne).

## What the source establishes (held full text, French)

**Definitions.** A *graphic* (graphique) is a continuous image of S¹ formed by
finitely many isolated singular points (vertices) and regular orbits connecting
them (ω- and α-limits at vertices). A graphic is *monodromic* if a first-return
map exists on a transversal. A *polycycle* is a graphic with finitely many
regular orbits; *hyperbolic* if all vertices are hyperbolic saddles with
hyperbolicity ratios rᵢ = |λᵢ¹|/λᵢ², λᵢ¹ < 0 < λᵢ² the eigenvalues. A compact
limit set F has *finite cyclicity* in a family (X_λ) if ∃N, ε, W with every
X_λ (λ∈W) having ≤ N limit cycles at distance < ε from F.

**Théorème 0** (the headline): for every n there is an open dense O_n ⊂ P_n
(planar polynomial fields of degree ≤ n) such that problem (H) — a locally
uniform bound on the number of limit cycles — holds in a neighbourhood of each
X ∈ O_n: for each X there is V_X and N_X with every Y ∈ V_X having ≤ N_X
limit cycles.

**Théorème 3** (the engine): there is a finite set G(k) of algebraic *generic
conditions* on the hyperbolicity ratios (r₁,…,r_k), containing all
"hyperbolic conditions" ∏_{j∈J} rⱼ ≠ 1 (J ⊆ {1,…,k}), and an integer e(k)
depending only on k, such that every hyperbolic monodromic polycycle Γ_k
satisfying G(k) has cyclicity ≤ e(k) in **every** C^∞ family. The conditions
are polynomial in the ratios with integer coefficients; they grow with k; for
k ≤ 3 all are of product form ([M2]); for k ≥ 4 some are NOT of product form
([M4]); e(k) satisfies recurrences in k, and the paper gives an explicit (but
very coarse) upper bound in k. (This is the finiteness *algorithm* of the
title.)

**Théorème 1 [M1]** (structure): for any K ∈ ℕ there are ε, a neighbourhood V
of 0 in ℝ^N, continuous positive ρ(λ), η(λ), and C^K transversals σ₁(λ), τ₁(λ)
such that the displacement Δ(x,λ) = p(x,λ) − x has the required structure —
the C^K normal-form setup that later papers (BGS 2024, QAS 2025) quote as
[M1] Mourtada LNM 1445 (1990).

## What it lets this run conclude

- **Primary source** for "generic hyperbolic polycycles are finitely cyclic
  in C^∞ families" — the result Mourtada 1990–94 and the modern Dulac-map
  literature (Marín–Villadelprat) refine. It is the *generic* (open dense in
  ratio-space) statement: cyclicity ≤ e(k) under G(k). Non-generic ratios
  (e.g. rⱼ = 1 or resonant products) are where the modern coefficient-level
  analysis (BGS Δ(Γⁿ), QAS A_{1,n}) continues.
- **Théorème 0** is the exact "finite cyclicity on an open dense set ⇒
  H16(2) locally true on an open dense set" statement. It is LOCAL
  (neighbourhood of each field) not uniform over the whole family; the DRR
  program is precisely the attempt to remove genericity.
- For the DRR inventory: the hyperbolic graphics of the 121 (hemicycles,
  elementary saddles at infinity) are covered by this generic finiteness in
  the C^∞ category; the DRR-adjacent closures (DGR 2002, MV 2025) give
  explicit small bounds in the quadratic family. The open rows are the
  non-hyperbolic ones, untouched by Mourtada 1991.

## Claim

```claim
id: h16-mourtada-1991-hyperbolic-finite-cyclicity-primary
status: asserted
statement: Mourtada (1991), "Cyclicite finie des polycycles hyperboliques de
  champs de vecteurs du plan. Algorithme de finitude", Ann. Inst. Fourier
  41(3):719-753: (Theorem 0) for every n there is an open dense O_n in the
  space P_n of planar polynomial fields of degree <= n such that H16-part-2 is
  locally true on O_n: every X in O_n has a neighbourhood V_X and bound N_X on
  the number of limit cycles of all Y in V_X. (Theorem 3) there is a finite
  set G(k) of algebraic generic conditions on the hyperbolicity ratios
  (r_1,..,r_k) of a hyperbolic monodromic polycycle Gamma_k, containing all
  product conditions prod_{j in J} r_j != 1, and an integer e(k) such that
  every Gamma_k satisfying G(k) has cyclicity <= e(k) in every C^infty family.
  For k <= 3 all G(k) conditions are of product type; for k >= 4 some are not;
  e(k) satisfies recurrences in k with an explicit coarse bound.
hypotheses: planar vector fields; hyperbolic monodromic polycycles (vertices
  hyperbolic saddles, possibly at infinity); C^infty families; generic =
  hyperbolicity-ratio point in an open dense subset of R^k.
evidence-class: sourced (open-access PDF full text held,
  research/sources/mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.full.md).
falsifier: a generic hyperbolic polycycle (ratios satisfying G(k)) and a C^infty
  family with more than e(k) limit cycles bifurcating from it — none known;
  the recurrences defining e(k) are stated but the coarse bound is what is
  explicit, so any quantitative use must cite the bound form actually given.
holds-here: yes as the primary anchor for "hyperbolic polycycles are finitely
  cyclic" in the C^infty category (the DRR hyperbolic classes, hemicycles,
  elementary saddles at infinity); does NOT cover non-hyperbolic graphics
  (nilpotent, degenerate, semi-hyperbolic), i.e. exactly the open DRR rows.
anchor: research/sources/mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.full.md
follows-from: h16-dulac-finiteness-theorem
```