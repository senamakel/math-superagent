# Ilyashenko–Llibre restricted H16.2: explicit bound away from centers and singular fields

```claim
id: ilyashenko-llibre-restricted-h16-quadratic-bound
statement: For any δ, σ, κ ∈ (0, 0.1), the number of δ-tame limit cycles of a normalized quadratic vector field v_λ : ż = μz + Az² + Bzz̄ + Cz̄², μ = λ₁ + i, λ₁ ≥ 0 (one of the three normal forms (2)–(4) of the paper: A=1 with |B|≤2,|C|≤1; or B=2 with |A|≤1,|C|≤1; or C=1 with |A|≤1,|B|≤2) that is (i) σ-distant from centers, meaning Σ_{j=1}^{4} |g_j(λ)| ≥ σ with the Zoladek-form center conditions g₁=λ₁, g₂=Im(AB), g₃=Im[(2A+B̄)(A−2B̄)B̄C], g₄=Im[(2A+B̄)(|B|²−|C|²)B̄²C]; and (ii) κ-distant from singular quadratic vector fields (fields with a line of singular points), meaning ‖r⁻²u‖₂ > κ in the decomposition v = v_s + u of (8); is at most H(2,δ,σ,κ) = |log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2})).
hypotheses: Quadratic planar polynomial vector fields with a focus at 0, normalized to one of the three glued cells Λ ≅ ℝ⁺×𝔻²×𝔻² (λ₁ ≥ 0, with time-reversal if needed); δ-tame limit cycle = one lying in B(λ,δ) = {|z| ≤ δ⁻¹} minus the open δ-neighborhoods of all singular points (real and complex) except 0; the bound depends on the vector parameter (δ,σ,κ) — the restricted problem as posed in the paper.
holds-here: yes — a genuine restricted bound on H(2), result-category 2 in problem.md. It does NOT prove H(2) < ∞: the constant diverges as σ,κ → 0 and δ → 0, precisely where centres and singular/degenerate fields (the DRR graphics territory) live.
status: asserted-by-source
evidence: sourced-held — full text at research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md. Theorem 5 (Main Theorem) lines 113-122; Theorem 6 (Growth-and-Zeros / Bernstein-index bound for holomorphic functions) lines 129-158; First Main Lemma 9 (lower estimate of max |P_λ − id| on K_λ) lines 235-266; Second Main Lemma 12 (universal gap between δ-tame limit cycles and the curve θ̇=0) lines 399-430; Lemma 10 (seven-jet of the Poincaré map in the centre case) lines 275-288; the appendix (lines 633-698) gives the explicit α,β,γ decompositions.
falsifier: A counterexample field in the stated class with more δ-tame limit cycles than H(2,δ,σ,κ), or a source showing the σ/κ/δ hypotheses do not exclude the divergence regime. Also: Lemma 10 is stated to have been proved with Mathematica — a clean-room re-derivation of the a₃,a₅,a₇ decompositions would be the check that keeps this row from resting on an unverified computation.
sources: https://arxiv.org/abs/0910.3443 ; https://ar5iv.labs.arxiv.org/html/0910.3443 ; https://doi.org/10.17323/1609-4514-2010-10-2-317-335
anchors: research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md lines 113-122 (Theorem 5), 275-288 (Lemma 10), 633-698 (appendix)
note: The appendix carries the explicit Bautin-ideal decomposition of the displacement's seven-jet: a₁≡1, a₂≡0, a₃=α₀g₂, a₄=α₁g₂, a₅=β₀g₃+β₁g₂, a₆=β₂g₃+β₃g₂, a₇=γ₀g₄+γ₁g₃+γ₂g₂, with α₀=−2π, β₀=−2π/3, γ₀=−5π/4 and explicit polynomial β₁,γ₁,γ₂ — primary evidence for the workspace's Bautin-ideal Lean work (code/lean/Lib/Bautin.lean) and its Lyapunov-quantity oracle (code/bautin/). The paper is "the first in a series": a subsequent paper proves that for κ ≤ κ₀(δ,σ) the field (8) has only one δ-tame limit cycle; a similar non-quantitative result is attributed to the Dumortier–Rousseau preprint (held as the CPAA 2009 degenerate-graphics full text).
follows-from:
answers:
```

## Why this claim block exists

The previous file at this path had a YAML-bullet header (`- id:` lines) instead of a
fenced `claim` block, so it never reached the claims ledger. This block records the
theorem with its held anchors and evidence class. The seven-jet Bautin decomposition
is the direct connection between this source and the run's Bautin-ideal Lean work.
