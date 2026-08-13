# Abram–Lagarias: Intersections of multiplicative translates of 3-adic Cantor sets (Part I)

**Source:** arXiv:1308.3133 (Abram, Lagarias), J. Fractal Geom. 1 (2014) 349–390. Full text at `research/sources/abram-lagarias-cantor-intersections-I.full.md`.

## Setup (pinned by this paper, terminology the run should reuse)

- **3-adic Cantor set** `Σ_{3,2̄} = {λ ∈ ℤ_3 : all 3-adic digits ∈ {0,1}}`. `dim_H(Σ_{3,2̄}) = log_3 2 ≈ 0.630929`.
- **Exceptional set** `ℰ(ℤ_3) = {λ ∈ ℤ_3 : for infinitely many n ≥ 0, (2^n λ)_3 omits the digit 2}`.
- **Weak Erdős ⟺ 1 ∉ ℰ(ℤ_3).** The full Erdős conjecture (only {0,2,8}) is stronger; since the witnesses {0,2,8} are known, weak ("finitely many exceptions") is equivalent to 1 ∉ ℰ(ℤ_3), and the strong form claims the exceptions are exactly {0,2,8}.
- **Exceptional Set Conjecture** (Lagarias 2009, Conj. 1.2): `dim_H ℰ(ℤ_3) = 0`. Still open; `dim_H ℰ(ℤ_3) ≤ ½` was the starting bound.
- Nesting constant `Γ = lim_k dim_H ℰ^(k)(ℤ_3)` where `ℰ^(k) = {λ : at least k values of (2^n λ)_3 omit 2}`; `dim_H ℰ(ℤ_3) ≤ Γ`; `ℰ^(k) = ⋃_{m_1<…<m_k} 𝒞(2^{m_1},…,2^{m_k})` with `𝒞(r_1,…,r_n) = ⋂ (1/r_i)Σ_{3,2̄}`.
- **Algorithm A/B** (Thm 3.1, 3.3): a terminating algorithm builds a right-resolving automaton whose path labels are exactly the 3-adic expansions of 𝒞(1,M_1,…,M_n); `dim_H = log_3 β` with `β` the Perron eigenvalue, an algebraic integer with `1 ≤ β ≤ 2`.

## Results that matter here

1. **dim_H ℰ⁽²⁾ ≥ log_3 φ ≈ 0.438018** and **dim_H ℰ⁽³⁾ ≥ log_3 β₁ ≈ 0.228392** where β₁ ≈ 1.2852 is the root of λ⁶−λ⁵−1=0 (Thm 5.2). Both bounds are *attained at the known witnesses*: `𝒞(1,2²) = 𝒞(1,4)` has dim log_3 φ; `𝒞(1,2²,2⁸) = 𝒞(1,4,256)` has dim log_3 β₁. **So the finite approximations ℰ⁽²⁾, ℰ⁽³⁾ have positive Hausdorff dimension precisely because of the exceptions 4 and 256.** Unknown whether dim ℰ⁽ᵏ⁾ > 0 for any k ≥ 4; 𝒞(1,4,256) is the only component of ℰ⁽³⁾ known to have positive dimension.
2. **Generalized exceptional set** (relax to arbitrary M ≢ 0 mod 3 instead of powers of 2): `dim_H ℰ_* ≥ ½ log_3 2 ≈ 0.315464` (Thm 1.9/5.1; set Y of numbers with 1s only at even digit positions has exactly this dimension and lies in 𝒞(1,N_{2k+1}) for all k, N_k = 3^k+1). **Consequence: no progress on the Exceptional Set Conjecture can come from relaxing "powers of 2" to general integers — the relaxed problem provably has positive dimension.** Only integers with the special structure of 2^k can work (1.6, "Extensions").
3. dim_H 𝒞(1,M) = 0 if M ≡ 2 (mod 3) (smallest nonzero digit 2); positive if all M_i ∈ Σ_3 (digits only 0,1) (Thm 4.1). Neither converse holds: 43 = (1121)_3 has dim 0; 64 = (2101)_3 has dim > 0.
4. Family L_k = (1^k)_3 = (3^k−1)/2: `dim_H 𝒞(1,L_k) = log_3 β_k`, β_k the root > 1 of λ^k − λ^{k−1} − 1 = 0; `= log_3 k/k + O(log log k / log k) → 0` (Thm 1.7/4.2).
5. Family N_k = 3^k + 1 = (10^{k−1}1)_3: `dim_H 𝒞(1,N_k) = log_3 φ` exactly, constant in k (Thm 1.8/4.4; adjacency matrix of the 2^k-vertex automaton has the positive eigenvector (φ^j) with Perron eigenvalue φ itself).

## Bearing on the run

- The Erdős conjecture's true content in this language: **1 ∉ ℰ(ℤ_3)**. Any proof attempt phrased in dimension/nesting terms must respect that the only known *lower* bounds on Γ come from the witnesses (4 and 256), and the *upper* bound chain: `dim_H ℰ(ℤ_3) ≤ Γ`, with `Γ ≤ ½` at this stage (Part II improves to log_3 φ).
- The path-set-automaton formalism is exactly the run's "which infinite survival paths are realised" question, made precise: an element of 𝒞(1, 2^{m_1}, …, 2^{m_k}) is a λ whose orbit hits the Cantor set at the k prescribed times. Erdős = no element of ℰ contains 1 as an *integer*, not just as a point of a fractal of dimension 0.

## Claims
```claim
id: AL-I-1
statement: The weak Erdős conjecture (only finitely many n with (2^n)_3 omitting digit 2) is equivalent to 1 ∉ ℰ(ℤ_3), where ℰ(ℤ_3) is the set of λ ∈ ℤ_3 whose orbit under ×2 meets the 3-adic Cantor set Σ_{3,2̄} (digits {0,1}) infinitely often; the strong form restricts the exceptions to {0,2,8}.
hypotheses: none.
holds-here: yes — the exact equivalence for the weak form; strong form is the run's target.
status: proved (Abram–Lagarias §1.1, citing Lagarias 2009)
bearing: pins the reformulation used throughout — the conjectures are about orbit visits of 1, not about counts.
anchor: research/sources/abram-lagarias-cantor-intersections-I.full.md
```
```claim
id: AL-I-2
statement: dim_H ℰ⁽²⁾(ℤ_3) ≥ log_3 φ ≈ 0.438018 (attained at 𝒞(1,4)) and dim_H ℰ⁽³⁾(ℤ_3) ≥ log_3 β₁ ≈ 0.228392, β₁ ≈ 1.2852 the root of λ⁶−λ⁵−1=0 (attained at 𝒞(1,4,256)); dim_H ℰ(ℤ_3) ≤ Γ ≤ ½.
hypotheses: none.
holds-here: yes.
status: proved (Theorem 5.2 + §1.1)
bearing: the finite approximations to the exceptional set have positive dimension exactly because the witnesses 4, 256 are in the orbit of 1 — any claim that "the sieve forces dimension/measure zero near 1" is falsified at k ≤ 3 by this theorem.
anchor: research/sources/abram-lagarias-cantor-intersections-I.full.md
```
```claim
id: AL-I-3
statement: The generalized exceptional set ℰ_*(ℤ_3) (M ranging over all integers ≢ 0 mod 3 rather than powers of 2) has dim_H ≥ ½ log_3 2 ≈ 0.315464.
hypotheses: relax powers of 2 to all M ≢ 0 (mod 3); M = 1 included.
holds-here: yes — it is a theorem about a relaxation, and it rules that relaxation out as a proof route.
status: proved (Theorem 1.9 / 5.1)
bearing: any approach replacing 2^m by general multipliers cannot settle the Exceptional Set Conjecture; the special arithmetic of powers of 2 is essential.
anchor: research/sources/abram-lagarias-cantor-intersections-I.full.md
```
```claim
id: AL-I-4
statement: dim_H 𝒞(1,M_1,…,M_n) = log_3 β where β ∈ [1,2] is the Perron eigenvalue of the automaton built by Algorithm A/B, an algebraic integer; the automaton is computable and right-resolving.
hypotheses: M_i ≡ 1 (mod 3) for positive dimension; M ≡ 2 (mod 3) forces dim 0.
holds-here: yes — this is the exact finite-automaton structure of "paths that hit the target"; matches the run's A_k/|A_k| picture in the λ-formulation.
status: proved (Theorems 1.6, 3.1, 3.3)
bearing: makes "which survival paths are realised" a question about path sets in finite automata; dimensions exactly computable in principle.
anchor: research/sources/abram-lagarias-cantor-intersections-I.full.md
```