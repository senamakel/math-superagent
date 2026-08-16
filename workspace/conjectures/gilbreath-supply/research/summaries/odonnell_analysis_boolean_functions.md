# Summary — Analysis of Boolean Functions (Ryan O'Donnell, CUP 2014 / arXiv May 2021)

Source: Ryan O'Donnell, *Analysis of Boolean Functions*, Cambridge University Press (2014), May 2021 arXiv revision. Full text: `[[odonnell_analysis_boolean_functions.full]]`. Free PDF (author-hosted, noncommercial personal use): http://www.cs.cmu.edu/~odonnell/papers/Analysis-of-Boolean-Functions-by-Ryan-ODonnell.pdf . Official site with materials: analysisofbooleanfunctions.org

## What this establishes

The canonical graduate text on the **Fourier/Walsh analysis of Boolean functions** `f : {−1,1}ⁿ → {−1,1}` (also written `{0,1}ⁿ`). This is the analytic counterpart the fold's order-K question needs: the fold's input is the binary gap-parity string `h ∈ {0,1}ⁿ`, and a functional of the fold "sensitive to correlation order K" is precisely an object studied by Fourier analysis of Boolean functions / high-degree analysis. The library already held the algebraic tier (Krawtchouk, MacWilliams, Delsarte); this supplies the analytic tier.

Key content, verified from the volume:

1. **Fourier expansion (Ch. 1).** Every `f : {−1,1}ⁿ → ℝ` has a unique multilinear (Fourier/Walsh) expansion; the parity functions `χ_S(x) = ∏_{i∈S} x_i` form an orthonormal basis under the uniform measure, and `χ_S·χ_T = χ_{S△T}` (Fact 1.6). Fourier coefficient `̂f(S) = ⟨f, χ_S⟩ = E_x f(x)χ_S(x)` (Prop 1.8); `E[f] = ̂f(∅)` (Fact 1.12). Convolution on `F₂ⁿ` and the Fourier transform of densities (Props 1.21–1.27). The BLR linearity test and its structural consequence (Thm 1.30): a function accepted by BLR with prob `1−ε` is `ε`-close to linear.

2. **Influence and derivative (Ch. 2).** Influence `Inf_i[f]` = fraction of dimension-i cube edges that are boundary edges for f (Fact 2.14); the discrete derivative `D_i f` and its Fourier formula `(D_i f)^(S) = ̂f(S∪{i})` (Prop 2.19); `Inf_i[f] = Σ_{S∋i} ̂f(S)²` (Thm 2.20). Total influence `I[f] = Σ_i Inf_i[f]`, and the fraction of cube boundary edges equals `I[f]/n` (Fact 2.29). Monotone functions have `Inf_i[f] = ̂f({i})` (Prop 2.21); transitive-symmetric monotone functions have `Inf_i[f] ≤ 1/√n` (Prop 2.22).

3. **Degree-k Fourier weight / low-degree concentration** — the crux for the reopened pass. Fourier weight on degree `k` (the sum of squared coefficients over k-sets, `(̂f(S))_{|S|=k}`) is the standard bookkeeping for how much of a function lives at correlation order k. Low-degree concentration (Ch. 3): low-degree Fourier terms control behaviour, culminating in Friedgut's junta theorem (a function with < k influential variables is an ε-close junta). Note: the notion of *multi-bit / joint influence of a set S of size K tied to W_{≥K}[f]* is **not** in this 2014 text — it is a newer (Tal 2019; Przybyłowski 2024) refinement that a search surfaced separately. What O'Donnell supplies is moderately-priced: degree-k Fourier weight, single-coordinate influence (KKL), low-degree concentration, and hypercontractivity.

4. **(p, q)-hypercontractivity, invariance principles** (Ch. 9–11): multilinear polynomials with low influences and bounded degree are distributionally invariant across product spaces; "Majority is Stablest" (Mossel–O'Donnell–Oleszkiewicz).

## What it implies here

The reopened pass (GOAL priority 2) asks: *is there a functional of the fold, sensitive to correlation order K with 1 < K ≲ n/2, controllable by an arithmetic input strictly weaker than pointwise mod-4 switch density?* The fold's cells are XORs over binary submasks of d (`T(n,d) = ⊕_{o⊆d} h[n−1−d+o]`). The submask XOR reads `|S_d| = 2^popcount(d)` distinct positions (the submasks of d are `2^popcount(d)` in number and map injectively to positions), so as a Walsh character the cell has **degree `2^popcount(d)`** — a power of two, NOT `popcount(d)`. The number of positions a cell reads (`2^popcount(d)`, in the gram/correlation sense) is the "correlation order K" of the reopened question, and the weight `wt(Φ_n h) = ν₂(n)` is a sum of Boolean-cell evaluations. O'Donnell supplies the standard analytic vocabulary and inequalities for a functional of such a fold: the Walsh/Fourier expansion, degree-k Fourier weight (how much of a function sits at correlation order k), single-coordinate influence (KKL), low-degree concentration / junta structure, and hypercontractivity as the tool that relates low-degree Fourier weight to expectation bounds. It does NOT itself prove anything about `wt(Φ_n h) ≥ c·n` — it is machinery for a route, not a theorem of this problem. Any K>1 functional built on it must still be priced against an arithmetic input on the prime parity string, which (Lacasa parity-projection note, Wu length-k barrier) is the genuinely open part. The specific notion of *multi-bit / joint influence of a set S of size K tied to W_{≥K}[f]* is **not** in this 2014 text.

## What it does NOT settle

- Nothing about the primes, `ν₂`, or `wt(Φ_n h) ≥ c·n` directly. It is a general toolkit for Boolean functions / Fourier analysis, not a statement about the fold.
- It does not supply the arithmetic input (any K>1 input on the prime gap-parity string beyond the parity-barred or projection-destroyed ones is open).
- The degree-k correlation objects it defines (degree-k Fourier weight, single-coordinate influence, hypercontractivity) are the *form* a K>1 functional would take; whether the primes' parity string admits such a controllable input is the open question this runs up against (see `notes/lacasa_parity_projection_transfer.md` and `summaries/wu_nonuniform_residues_prime_sequences.md`). The multi-bit/joint-influence notion is newer (Tal 2019, Przybyłowski 2024) and not in this source.

```claim
id: odonnell-boolean-fourier-degree-k-toolkit
statement: Every f : {−1,1}^n → R has a unique Walsh/Fourier expansion in the parity basis
  χ_S (orthonormal under uniform measure, χ_S·χ_T = χ_{S△T}); the influence of coordinate i is
  Inf_i[f] = Σ_{S∋i} ̂f(S)² and the derivative satisfies (D_i f)^(S) = ̂f(S∪{i}); degree-k Fourier
  weight is the sum of squared coefficients over k-sets; low-degree concentration (Friedgut junta
  theorem: < k influential variables ⇒ ε-close junta) and hypercontractivity (Bonami–Beckner)
  relate low-degree Fourier weight to expectation/variance bounds.
hypotheses: Boolean functions on the hypercube {−1,1}^n under the uniform measure; any f with a
  Fourier expansion, not necessarily {−1,1}-valued.
holds-here: yes — the fold's input is the binary gap-parity string h ∈ {0,1}^n, each fold cell
  T(n,d) = ⊕_{o⊆d} h[n−1−d+o] is an XOR over the 2^popcount(d) binary submasks of d, i.e. a parity
  character of degree 2^popcount(d) (a power of two, the number of distinct positions read), so
  "correlation order K" of the reopened pass corresponds to degree-K Fourier weight that this
  toolkit bookkeeps; wt(Φ_n h) = ν₂(n) is a sum of such cell evaluations. (The multi-bit/joint
  influence of a K-set tied to W_{≥K} is newer — Tal 2019; Przybyłowski 2024 — and NOT in this source.)
status: asserted (sourced from the canonical graduate text; standard textbook results).
bearing: supplies the standard analytic (Fourier/Walsh/influence/hypercontractivity) vocabulary and
  inequalities for a functional of order 1 < K ≲ n/2 — the exact territory of the reopened GOAL
  priority-2 question. It is machinery for a route, not a theorem about ν₂ ≥ c·n; the arithmetic
  input on the prime parity string is still the open part (Lacasa parity-projection negative, Wu
  length-k barrier).
anchor: odonnell_analysis_boolean_functions.full, Ch. 1 (Fourier), Ch. 2 (influence/derivative),
  Ch. 3 (low-degree concentration / junta), Ch. 9-11 (hypercontractivity, invariance, Majority-is-Stablest).
```

## Keyword map
Boolean functions; Walsh/Fourier expansion; influence; total influence; degree-k Fourier weight; low-degree concentration; junta theorem; hypercontractivity (Bonami–Beckner); isolation/Majority-is-Stablest; analysis of Boolean functions; correlation order.
