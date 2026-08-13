# Abram–Bolshakov–Lagarias: Intersections of multiplicative translates of 3-adic Cantor sets II (Two infinite families)

**Source:** arXiv:1508.05967 (Abram, Bolshakov, Lagarias), Experimental Mathematics 26 (2017) 410–426. Full text at `research/sources/abram-bolshakov-lagarias-cantor-intersections-II.full.md`. Notation as in Part I summary (`Σ_{3,2̄}`, `ℰ`, `ℰ⁽ᵏ⁾`, `Γ`, `𝒞(1,M₁,…,Mₙ)`).

## What this paper establishes

1. **Improved upper bound on the exceptional set** (Thm 2.6 / eq. (1.10)): `dim_H ℰ(ℤ_3) ≤ Γ ≤ Γ_** = log_3 φ ≈ 0.438018`, down from ½. Here `α_n := sup{dim_H 𝒞(1,M) : (M)_3 has ≥ n nonzero digits}`, `Γ_** = lim_n α_n`, and the equality `Γ_** = log_3 φ` is proved. (φ = golden ratio, log_3 φ ≈ 0.438018.)
2. **The "number of nonzero ternary digits" statistic provably does not drive dimension to 0** (Thm 2.4, 2.6): family `Q_k = 3^{2k} − 3^k + 1 = (2^k 0^{k−1} 1)_3` has `d_3(Q_k) = k+1 → ∞` yet `dim_H 𝒞(1,Q_k) = log_3 φ` for every k ≥ 2, constant. The path set is `X(1,Q_k) = X(1,7)^{(*k)}` (k-fold interleaving), and interleaving preserves topological entropy (Prop 3.6, Cor 3.7). So `α_k = log_3 φ` for all k ≥ 2.
3. **Family P_k = 2·3^k + 1 = (20^{k−1}1)_3**: automata have `1+⌊k/2⌋` nested strongly connected components ("Matryoshka dolls"), `2^{k+1}` vertices; `dim_H 𝒞(1,P_k) ≥ (1/13) log_3 2` for all k and `liminf ≥ (1/8) log_3 2` (Thm 2.1, 2.2); dimension ≤ log_3 φ. Nonmonotonic in k.
4. **Stewart bound quoted** (Thm 6.1): `s_3(2^m) > log m/(log log m + c) − 3` for m ≥ 25 (number of nonzero ternary digits of 2^m grows at least this fast).
5. **The route via n_3(M) is closed**: it is *not* true that dim_H 𝒞(1,M) → 0 as the number of nonzero ternary digits of M → ∞ (Theorem 2.6: α_k = log_3 φ for all k ≥ 2). Since the number of nonzero ternary digits of 2^m does go to infinity (Senge–Straus, Stewart), the general "dimension → 0 as digits grow" programme (suggested in Part I §1.6 as a route to the Exceptional Set Conjecture) is refuted: some M with arbitrarily many nonzero ternary digits keep dimension log_3 φ.

## Bearing on the run

- The chain of upper bounds on the exceptional set is now: `dim_H ℰ(ℤ_3) ≤ Γ ≤ Γ_** = log_3 φ ≈ 0.438018`. It is a *bound*, not the conjecture (dim = 0). Part II also gives lower-bound evidence that the statistic-based routes stop at φ.
- The quantity `Γ` = lim_k dim_H ℰ⁽ᵏ⁾ has a positive lower bound (Part I Thm 5.2: dim ℰ⁽²⁾ ≥ log_3 φ, dim ℰ⁽³⁾ ≥ log_3 β₁ > 0) and an upper bound log_3 φ; the run's known-witness computation (𝒞(1,4), 𝒞(1,4,256)) matches both the lower ends and, by coincidence, the value log_3 φ appears on both sides of the sandwich for Γ.

## Claims
```claim
id: ABL-II-1
statement: dim_H ℰ(ℤ_3) ≤ Γ ≤ Γ_** = log_3 φ ≈ 0.438018, where Γ is the nesting constant and Γ_** = inf_k α_k with α_k = sup{dim_H 𝒞(1,M) : (M)_3 has ≥ k nonzero ternary digits}; moreover α_k = log_3 φ for all k ≥ 2, attained by Q_k = 3^{2k}−3^k+1.
hypotheses: none.
holds-here: yes.
status: proved (Theorems 2.5, 2.6, eq. (1.10))
bearing: the current best upper bound on the exceptional set; also the negative result that "dimension → 0 as the number of nonzero digits grows" is false.
anchor: research/sources/abram-bolshakov-lagarias-cantor-intersections-II.full.md
```
```claim
id: ABL-II-2
statement: dim_H 𝒞(1,Q_k) = log_3 φ for all k ≥ 2 with Q_k = 3^{2k}−3^k+1 = (2^k 0^{k−1} 1)_3, via X(1,Q_k) = X(1,7)^{(*k)} and entropy preservation under interleaving.
hypotheses: k ≥ 2.
holds-here: yes — a concrete infinite family with unbounded digit count but constant positive dimension.
status: proved (Theorems 2.3, 2.4; Prop 3.4, 3.6, Cor 3.7)
bearing: closes the "few-statistic" route: a statistic d_3(M) → ∞ does not force dim_H 𝒞(1,M) → 0.
anchor: research/sources/abram-bolshakov-lagarias-cantor-intersections-II.full.md
```
```claim
id: ABL-II-3
statement: s_3(2^m), the number of nonzero ternary digits of 2^m, satisfies s_3(2^m) > log m/(log log m + c) − 3 for m ≥ 25 (Stewart, quoted with proof sketch in Part II Thm 6.1).
hypotheses: m ≥ 25.
holds-here: yes — gives the growth rate of the "≥26 ones" case in DH-1.
status: asserted-by-source (quoted from Stewart 1980; proof sketch given)
bearing: quantifies the DH-1 residual: a counterexample has ≥26 ones, and the ones-count grows at least like log m/log log m.
anchor: research/sources/abram-bolshakov-lagarias-cantor-intersections-II.full.md
```