# Wojcik — Formal intercepts of Sturmian words (arXiv:1803.02073)

<!-- source: https://ar5iv.labs.arxiv.org/html/1803.02073 | read 2026-08-19 (§3 full) -->

Full text: `[[formal-intercepts-sturmian-2018.full]]` (66 KB, 857 lines).

## What it establishes

A combinatorial treatment of the **second parameter** (the intercept) of Sturmian words via Ostrowski expansions.

- **Ostrowski conditions (Prop 8)**: N = Σ_{i=0}^{k−1} b_{i+1} q_i with the prefix sums < q_l iff (i) 0 ≤ b_1 ≤ a_1−1; (ii) 0 ≤ b_i ≤ a_i for all i; (iii) b_{i+1} = a_{i+1} ⇒ b_i = 0. **Prop 9**: every N ∈ [0, q_n) has a unique such representation — the Ostrowski numeration in terms of the continuants q_i of the slope's CF.
- **Formal intercept (Def 12)**: I_α = { (k_n)_{n>0} ∈ ∏ [0,q_n) : k_n = k_{n+1} mod q_n } — the projective limit of the finite ranges [0,q_n), i.e. an integer sequence that is coherent mod each q_n. Every Sturmian word of slope α is T^ρ(c_α) for a **unique** formal intercept ρ (Prop 12); the shifts T^{ρ_n}(c_α) agree on prefixes of length q_n−1 (Prop 10).
- **Prefix-extension bound (Prop 10–11)**: T^ρ(c_α) and T^{ρ_n}(c_α) share a common prefix of length λ_n = q_{n+1} + q_n − ρ_{n+1} − 2, and λ_n → ∞; the exact longest-common-prefix length is λ_N where N ≥ n is the first index with b_{N+1} ≠ 0.
- Example: the words 0·c_α and 1·c_α have formal intercepts Σ_{i≥0} a_{2i+2} q_{2i+1} and (a_1−1) + Σ_{i≥1} a_{2i+1} q_{2i}.
- §1–2: re-proves Morse–Hedlund, balanced ⟺ Sturmian, characteristic words from CF, standard/central words, the repetition function (Prop 5: R(n) = q_{k+1} + q_k + q_{k−1} − 2 for q_k ≤ n < q_{k+1}, from the Rauzy-graph cycles), Rauzy graph structure of Sturmian words.

## Why it matters here

- Gives the **Ostrowski parametrisation of the intercept** — the exact coordinate in which the run's k+1 arc-midpoint intercepts x_m = frac(−m·a) live. The k+1 intercepts of PE1006 are a finite slice of formal intercepts; the prefix-extension bound λ_n is the precise version of "how far must a window range reach" that the run's first-occurrence / contiguous-window theorems (Cassaigne's Φ+1 bound, Lmin(k) = k + NextFib(k) − 1) quantify.
- Prop 8–9 is the source-level statement of the Ostrowski conditions the run's Ostrowski-prefix-decomposition axis (`ostrowski-prefix-decomposition-characteristic`) uses, with the canonical CF-continuant representation for α = 1/φ² = [0;2,1,1,…].
- **Does NOT give Ψ(k)**: no decimal weights, no squares, no joint-intercept aggregation. It fixes the numeration/coordinate machinery, not the weighted second moment.

## Claims anchored here

Corroborates `ostrowski-prefix-decomposition-characteristic` (Ostrowski representation of prefixes/positions), `fibonacci-first-occurrence-window-bound` (prefix-extension/recurrence structure). No new claim block.
