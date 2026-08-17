# Bugeaud & Laurent — *Combinatorial structure of Sturmian words and continued fraction expansions of Sturmian numbers*

Source: https://hal.science/hal-03571109 (PDF preview: hal-03571109v1/preview/Arxiv_Bu_La.pdf)
Full text: [[bugeaud-laurent-sturmian-continued-fractions.full]]

## What this source establishes

A research paper on Sturmian numbers (real numbers whose base-b expansion is a
Sturmian word) and their continued fractions. Relevant structural facts:

- **Sturmian words as rotation codings** (Section 2): s_{θ,ρ} and s′_{θ,ρ}
  (lower/upper mechanical words) with the rotation R(x) = {x+θ}. Theorem 2.1:
  if ρ ∉ Zθ+Z or ρ ∈ Z_{≥1}θ+Z then s_{θ,ρ} = s′_{θ,ρ} — the two mechanical
  forms agree off a measure-zero set of intercepts. This legitimises choosing
  the arc-midpoint intercepts in directive 2: they avoid the (at most finitely
  many, k-dependent) exceptional points.
- **Standard-word (convergent) recursion** (Lemma 3.4): V_{k+1} =
  V_k^{a_{k+1}−b*_{k+1}}·V_{k−1}·V_k^{b*_{k+1}} — the general directive-sequence
  recursion; for the Fibonacci slope 1/φ² the directive sequence is (1,1,1,…)
  and b*_k = 0, giving the plain Fibonacci-word recursion s_n = s_{n−1}s_{n−2}.
  Confirms the convergent structure behind the rational approximants
  F(n−2)/F(n) → 1/φ².
- Corollary 3.5 (product formula for prefixes): the prefix of length t < q_{n+1}
  of M_{n+1} decomposes by the convergent coefficients — a structural identity
  that could, in principle, decompose floor-sum inputs, though the run does not
  need it (the universal-Euclidean recursion already handles the sums).

## What it implies for PE1006

1. Confirms that the mechanical word with *any* non-exceptional intercept has
   the full factor set of slope 1/φ² — the arc-midpoint construction is
   sound. (The exceptional set is finite per k; explicit midpoints are not in
   it for the rational approximants used.)
2. Confirms the standard-word recursion s_n = s_{n−1}s_{n−2} is the
   directive-sequence (1,1,1,…) case, tying the problem's S_n to the standard
   words of the convergents F(n)/F(n+1) of 1/φ².

## Claims anchored here

Corroborates `governing-sturmian` and `mechanical-word-digit-rule`.

## What it does NOT establish

- No factor-complexity or Psi statements; no floor-sum algorithm. This is
  supporting (second-tier) structure, not a load-bearing primitive.
- The paper's focus (transcendence, continued fractions of Sturmian numbers) is
  irrelevant to PE1006.