# Durable memory retry list — scholar digest 2026-08-18 (restricted-H2 cycle)

Cognee (`http://cognee:8000`) was unreachable throughout this digest (health
timeouts / connection refused). The following findings are durably recorded
locally and MUST be retried through `remember_memory` when the service
recovers. Each carries its source URL and claim id.

## 1. Ilyashenko–Llibre restricted H(2) bound
- **Local record:** research/findings/ilyashenko-llibre-fishkin-restricted-bounds-2026-08-18.md
- **Claim:** ilyashenko-llibre-restricted-h16-quadratic-bound
- **Text to store:** Ilyashenko–Llibre 2010 (Moscow Math. J. 10(2):317–335,
  arXiv:0910.3443) Theorem 5: for any δ,σ,κ∈(0,0.1), the number of δ-tame
  limit cycles of a normalized quadratic field σ-distant from centers and
  κ-distant from singular quadratic fields is at most
  |log σ|·exp(exp(10²⁵·δ^{−31}·κ^{−2})). Full text held; genuine restricted
  bound on H(2) (result-category 2) but does NOT prove H(2)<∞ — the constant
  diverges in the DRR-graphics regime. Appendix gives the explicit Bautin-ideal
  seven-jet decomposition a₃=α₀g₂, a₅=β₀g₃+β₁g₂, a₇=γ₀g₄+γ₁g₃+γ₂g₂ with
  α₀=−2π, β₀=−2π/3, γ₀=−5π/4 (Lemma 10, Mathematica-computed).
- **Source URL:** https://ar5iv.labs.arxiv.org/html/0910.3443

## 2. Fishkin 2010 abstract-level bound — data-hygiene correction
- **Local record:** research/findings/ilyashenko-llibre-fishkin-restricted-bounds-2026-08-18.md
  and research/findings/fishkin-abstract-reconstruction-2026-08-18.md
- **Claim:** fishkin-perturbed-center-quadratic-bound (holds-here: unchecked)
- **Text to store:** Fishkin 2010 (Trans. Moscow Math. Soc. 71) proves an upper
  bound on δ-good limit cycles of planar quadratic vector fields with a
  perturbed center-like singular point (Theorem 1, with κ measuring distance
  to fields with a line of singular points) and a uniform bound dropping the
  center-distance assumption (Theorem 2), complementing Ilyashenko–Llibre 2010.
  The specific exponents 10⁷²/10⁷⁷/δ^{−33} quoted in earlier reports appear in
  NO held source and are UNVERIFIED — only the theorem structure is confirmed
  (OpenAlex abstract). Full text NOT held (AMS 429).
- **Source URL:** https://doi.org/10.1090/s0077-1554-2010-00181-1

## 3. Bautin-ideal seven-jet decomposition (evidence for Lean work)
- **Local record:** research/findings/ilyashenko-llibre-fishkin-restricted-bounds-2026-08-18.md
- **Text to store:** The Ilyashenko–Llibre appendix carries the explicit
  Bautin-ideal decomposition of the quadratic displacement's seven-jet in
  complex form (Lemma 10): a₁≡1, a₂≡0, a₃=α₀g₂, a₄=α₁g₂, a₅=β₀g₃+β₁g₂,
  a₆=β₂g₃+β₃g₂, a₇=γ₀g₄+γ₁g₃+γ₂g₂ with α₀=−2π, β₀=−2π/3, γ₀=−5π/4. This is
  primary evidence for the Bautin-ideal Lean work (code/lean/Lib/Bautin.lean)
  and the Lyapunov-quantity oracle (code/bautin/). Caveat: Mathematica-computed,
  clean-room re-derivation pending.
- **Source URL:** https://ar5iv.labs.arxiv.org/html/0910.3443

## Files created this digest
- research/findings/ilyashenko-llibre-fishkin-restricted-bounds-2026-08-18.md
- research/findings/fishkin-abstract-reconstruction-2026-08-18.md
- research/claims/ilyashenko-llibre-restricted-h16-quadratic-bound.md (rewritten
  from invalid YAML-bullet format to a fenced claim block)
- research/claims/fishkin-perturbed-center-quadratic-bound.md (rewritten; the
  unverified exponents are now flagged)
- research/summaries/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.md
- research/summaries/fishkin-perturbed-center-quadratic-limit-cycles.md
- code/lean/Lib/IlyashenkoLlibreRestricted.lean (Cited axiom + wrapper)
