# Ilyashenko–Llibre and Fishkin restricted H(2) bounds — scholar digest and data-hygiene correction

## Date and context
2026-08-18 continuation pass. The librarian cycle added two restricted-H(2)
bound sources: Ilyashenko–Llibre 2010 (full text held) and Fishkin 2010
(abstract level only). This digest verifies the claims against what is actually
held, and corrects a data-hygiene defect in the Fishkin row.

## Ilyashenko–Llibre 2010 — verified from held full text

**Theorem 5 (Main Theorem).** For any δ, σ, κ ∈ (0, 0.1), the number of
δ-tame limit cycles of a normalized quadratic vector field (ż = μz + Az² + Bzz̄ +
Cz̄², μ = λ₁ + i, λ₁ ≥ 0, one of three normal forms) that is σ-distant from
centers (Σ_{j=1}^{4}|g_j(λ)| ≥ σ with the four Zoladek-form center conditions)
and κ-distant from singular quadratic fields (line of singular points) is at
most

    H(2,δ,σ,κ) = |log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2})).

Verified verbatim at research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md
lines 113–122. This is a genuine restricted bound on H(2), result-category 2 in
problem.md. It does NOT prove H(2) < ∞: the constant diverges as σ,κ → 0, δ → 0,
exactly the centres / singular-degenerate (DRR graphics) regime.

**The appendix (lines 633–698) carries the explicit Bautin-ideal decomposition
of the displacement's seven-jet** (Lemma 10, lines 275–288): a₁ ≡ 1, a₂ ≡ 0,
a₃ = α₀g₂, a₄ = α₁g₂, a₅ = β₀g₃ + β₁g₂, a₆ = β₂g₃ + β₃g₂,
a₇ = γ₀g₄ + γ₁g₃ + γ₂g₂, with α₀ = −2π, β₀ = −2π/3, γ₀ = −5π/4 and explicit
polynomial β₁, γ₁, γ₂. This is primary evidence for the Bautin-ideal Lean work
(code/lean/Lib/Bautin.lean) and the Lyapunov-quantity oracle (code/bautin/).
Caveat: Lemma 10 is stated to have been computed with Mathematica; a clean-room
re-derivation of the decompositions is the check that keeps this row from
resting on an unverified computation.

**Proof structure.** Theorem 6 (Growth-and-Zeros: Bernstein-index bound for
holomorphic functions) is the counting instrument. First Main Lemma 9 gives the
lower estimate of max |P_λ − id| on K_λ (≥ 10^{−26}σ for λ₁ ≤ 0.1; ≥ 10^{−26/δ}
for λ₁ > 0.1). Second Main Lemma 12 gives the universal gap between δ-tame
limit cycles and the curve θ̇ = 0. The paper is "the first in a series": a
subsequent paper proves that for κ ≤ κ₀(δ,σ) the field (8) has only one
δ-tame limit cycle.

## Fishkin 2010 — data-hygiene correction

**The two AMS "full text" captures hold NO mathematics.** They are generic
journal landing pages (research/sources/fishkin-perturbed-center-quadratic-limit-cycles.full.md
and -ams.full.md). The only abstract obtainable is the OpenAlex record
(research/sources/fishkin-openalex.full.md), reconstructed from its inverted
index:

> "We investigate the number of limit cycles of a planar quadratic vector field
> with perturbed center-like singular point. An upper bound is obtained on the
> number of δ-good such cycles (Theorem 1)... κ ... distance to the set
> consisting of fields with a line [of singular points]. Earlier, Ilyashenko
> [and] Llibre found ... complement each other and yield new ... field,
> regardless of its distance to [a center-like] point (Theorem 2)."

**The specific numerical exponents quoted in earlier reports (10⁷², 10⁷⁷,
δ^{−33}) appear in NO held source and are UNVERIFIED.** They were written into
research/REFERENCE-SET-REPORT-2026-08-18-restricted-h2.md,
research/LIBRARY-STATUS-restricted-h2.md, and the previous form of
research/claims/fishkin-perturbed-center-quadratic-bound.md as if
abstract-level, without any held source containing them. This is a
data-hygiene defect: the theorem STRUCTURE (perturbed-center Theorem 1; uniform
Theorem 2 without center-distance assumption; complements Ilyashenko–Llibre)
IS confirmed by the abstract; the CONSTANTS are not. The claim file and summary
now state exactly this.

**Upgrade path.** Retry the AMS free-archive PDF
(https://www.ams.org/journals/mosc/2010-71-00/S0077-1554-2010-00181-1/S0077-1554-2010-00181-1.pdf,
vol 71 is >5 years old so a retry is legitimate) when the server allows
(429 rate-limit this cycle, three separate attempts). CiteSeerX copy
(doi 10.1.1.309.2425) was unreachable this cycle.

## What this implies for the run

1. Ilyashenko–Llibre is the strongest held restricted-H(2) bound: it excludes
   centres (σ-distant) and singular fields (κ-distant), exactly the DRR-graphics
   regime. The bound diverges there — the quantitative shadow of the
   finite-cyclicity obstruction.
2. The seven-jet Bautin decomposition is direct primary evidence that the
   Bautin ideal ⟨g₁,g₂,g₃,g₄⟩ (complex form) controls the displacement's first
   seven Taylor coefficients at a centre — a kernel-checkable target for the
   Bautin-ideal Lean work.
3. Any run report that quotes the Fishkin exponents without the primary text
   is repeating an unverified figure. The claim ledger now says `holds-here:
   unchecked` for the exact constants.

## Falsifiers
- A counterexample field in the Ilyashenko–Llibre class with more δ-tame limit
  cycles than |log σ|·exp(exp(10²⁵δ^{−31}κ^{−2})).
- Any discrepancy between the Fishkin quoted exponents (10⁷²/10⁷⁷/δ^{−33}) and
  the paper itself, once the primary text is obtained.
- A clean-room re-derivation of Lemma 10's seven-jet that disagrees with the
  appendix's α,β,γ coefficients.
