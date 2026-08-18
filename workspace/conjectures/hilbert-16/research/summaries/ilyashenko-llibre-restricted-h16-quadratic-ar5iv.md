# Ilyashenko–Llibre, "A restricted version of the Hilbert's 16th problem for quadratic vector fields"

**Source URL:** https://ar5iv.labs.arxiv.org/html/0910.3443 (full text)
**Held at:** `research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md`
**Published:** Moscow Math. J. 10(2):317–335 (2010), DOI 10.17323/1609-4514-2010-10-2-317-335
**Claim:** `research/claims/ilyashenko-llibre-restricted-h16-quadratic-bound.md`
**Lean:** `code/lean/Lib/IlyashenkoLlibreRestricted.lean`

## What it establishes

A **restricted bound on H(2)** — the only known estimate of its kind (authors'
own words: "this is the only known estimate of this kind"). For quadratic
vector fields (normalized as ż = μz + Az² + Bzz̄ + Cz̄², μ = λ₁ + i, λ₁ ≥ 0, one
of three normal forms (2)–(4)) that are:

- **σ-distant from centers**: Σ|g_j| ≥ σ with the four Zoladek-form center
  conditions g₁ = λ₁, g₂ = Im(AB), g₃ = Im[(2A+B̄)(A−2B̄)B̄C],
  g₄ = Im[(2A+B̄)(|B|²−|C|²)B̄²C]; and
- **κ-distant from singular quadratic fields** (line of singular points):
  ‖r⁻²u‖₂ > κ in the decomposition v = v_s + u of (8);

the number of **δ-tame limit cycles** (lying in B(λ,δ) = {|z| ≤ δ⁻¹} minus the
open δ-neighborhoods of all singular points except 0) is at most

**H(2,δ,σ,κ) = |log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2}))**  (Theorem 5).

## Why it matters to this run

- Exactly problem.md's result category 2: a finite bound on H(2) under
  explicitly stated restrictions. It does NOT prove H(2) < ∞ — the bound
  diverges as σ,κ → 0, δ → 0, precisely where centres and singular/degenerate
  fields (the DRR graphics territory) live.
- The proof runs through the **displacement function** P_λ − id and its zeros —
  the same object the run's whole frame is built on. Theorem 6
  (Growth-and-Zeros: Bernstein-index bound for holomorphic functions) is the
  counting instrument; the First Main Lemma 9 gives the lower estimate of
  max |P_λ − id| on K_λ; the Second Main Lemma 12 gives the universal gap
  between δ-tame limit cycles and the curve θ̇ = 0.
- **The appendix carries the explicit Bautin-ideal decomposition of the
  displacement's seven-jet** (Lemma 10): a₁ ≡ 1, a₂ ≡ 0, a₃ = α₀g₂,
  a₄ = α₁g₂, a₅ = β₀g₃ + β₁g₂, a₆ = β₂g₃ + β₃g₂, a₇ = γ₀g₄ + γ₁g₃ + γ₂g₂,
  with α₀ = −2π, β₀ = −2π/3, γ₀ = −5π/4 and explicit polynomial β₁, γ₁, γ₂.
  This is primary evidence for the Bautin-ideal Lean work in
  `code/lean/Lib/Bautin.lean` and the Lyapunov-quantity oracle in `code/bautin/`.
- The paper is "the first in a series": a subsequent paper proves that for
  κ ≤ κ₀(δ,σ) the field (8) has only **one** δ-tame limit cycle; a similar
  non-quantitative result is attributed to the Dumortier–Rousseau preprint
  (held as the CPAA 2009 degenerate-graphics full text).

## Caveats

- Lemma 10 (the seven-jet) is stated to have been computed with Mathematica;
  the coefficient decompositions are asserted, not re-derived here. A
  clean-room re-derivation would be the check (see the claim row).
- The bound is "irrealistic" (authors' word) — doubly exponential in
  δ^{−31}κ^{−2}.
- Does not touch the DRR-graphics open rows; those live in the σ,κ → 0 limit
  this bound explicitly excludes.
- The estimate `|log σ|·exp(exp(10²⁵ δ^{−31} κ^{−2}))` and the seven-jet
  decomposition are verified verbatim against the held full text (Theorem 5 at
  lines 113–122; Lemma 10 at lines 275–288; appendix lines 633–698).

[[ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full]]
