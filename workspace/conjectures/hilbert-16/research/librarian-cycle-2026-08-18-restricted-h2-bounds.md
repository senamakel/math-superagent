# Librarian cycle report — restricted-H(2) bounds acquired; DRR ledger re-confirmed unfindable

**Cycle:** 2026-08-18 (librarian continuation). **Problem:** Hilbert's 16th, Part II — `H(n) < ∞` for planar polynomial vector fields, frame = displacement function / Bautin ideal / DRR graphics.

## What this cycle added to the library

### 1. Ilyashenko–Llibre 2010 — restricted bound on H(2) (NEW, full text)

- **Source URL:** https://ar5iv.labs.arxiv.org/html/0910.3443 (arXiv:0910.3443)
- **Held at:** `research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md`
- **Published:** Moscow Math. J. 10(2):317–335 (2010), DOI 10.17323/1609-4514-2010-10-2-317-335
- **Summary:** `research/summaries/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.md`
- **Claim:** `research/claims/ilyashenko-llibre-restricted-h16-quadratic-bound.md`
- **What it settles:** For quadratic vector fields σ-distant from centers (Σ|g_j| ≥ σ over the four Zoladek-form center conditions) and κ-distant from singular fields (line of singular points), the number of δ-tame limit cycles is ≤ |log σ|·exp(exp(10²⁵δ^{−31}κ^{−2})). This is the only known estimate of this kind — a genuine restricted bound on H(2), result-category 2 in problem.md. It does NOT prove H(2) < ∞ (diverges where centres/degenerate graphics live).
- **The appendix carries the explicit seven-jet of the displacement:** a₃ = α₀g₂, a₅ = β₀g₃ + β₁g₂, a₇ = γ₀g₄ + γ₁g₃ + γ₂g₂ with α₀=−2π, β₀=−2π/3, γ₀=−5π/4 and explicit β₁, γ₁, γ₂ — direct primary evidence for the Bautin-ideal Lean work (`code/lean/Lib/Bautin.lean`, `code/bautin/`).

### 2. Fishkin 2010 — companion uniform bound for the perturbed-center case (NEW, abstract-level)

- **Source URL:** https://doi.org/10.1090/s0077-1554-2010-00181-1
- **Held at:** `research/sources/fishkin-perturbed-center-quadratic-limit-cycles.full.md` + `-ams.full.md` (both AMS landing page; **full text NOT obtained** — PDF returned 429 rate-limit this cycle; vol 71 is in the free archive so a retry is legitimate)
- **Claim:** `research/claims/fishkin-perturbed-center-quadratic-bound.md`
- **What it settles (abstract-level):** Theorem 1 bounds δ-good limit cycles for fields κ-distant from singular fields and close to a perturbed center-like point; Theorem 2 drops the center-distance assumption, complementing Ilyashenko–Llibre 2010. **DATA-HYGIENE CORRECTION (scholar pass):** the exponent figures previously quoted here (10⁷²κ^{−2}δ^{−33} / 10⁷⁷κ^{−2}δ^{−33}) appear in **NO held source** — the two AMS captures are generic landing pages, and no obtainable abstract (AMS, MathSciNet, Semantic Scholar, OpenAlex) contains them. They are UNVERIFIED and must not be repeated without the primary text. What IS confirmed (OpenAlex abstract, `research/sources/fishkin-openalex.full.md`): the theorem structure and the complementarity with Ilyashenko–Llibre.

## What was re-confirmed (not obtained)

- **The consolidated post-2015 DRR graphic-by-graphic ledger remains unfindable.** A citation walk on DRR 1994 (129 citers) and targeted searches for a 2024–26 Rousseau/Roussarie survey returned only the held picture: 88/121 closed by RSZ 2015 (with (I¹₁₂),(I¹₁₃) closed, count to 88), (I¹₁₄) closed by Roussarie–Rousseau 2015 (run arithmetic 89), (I¹₆b),(H³₁₃),(DI₂b) boundary-only, (H³₁₄) open with Lu 2026 unrefereed claim, ≥11 degenerate graphics open (DF1b, DF2b, DH1, DH2, DI1a, DI1b, DI2a, DI2b, DH3, DH4, DH5). Both open requests (`complete-current-ledger-cb3d`, `dumortier-roussarie-rousseau-9c4f`) stay open.
- **Artés–Dumortier–Llibre 2009 (DI2a) full text** — still 403 at ScienceDirect; the held DR 2009 CPAA full text (Theorem 3.1, the P* obstruction) is the primary source for the degenerate-graphics attack.
- **Marín–Villadelprat corrigendum** — still not held (403 at SSRN).

## Evidence discipline

- The Ilyashenko–Llibre bound is **asserted-by-source** from the held full text (Theorem 5 + supporting lemmas verified present with line anchors).
- The Fishkin bound is **asserted-by-source at abstract level only** — and the specific exponent figures (10⁷²/10⁷⁷/δ^{−33}) previously carried in the row files are UNVERIFIED (in no held source), corrected this pass. Only the theorem structure is confirmed (OpenAlex abstract).
- Lemma 10's seven-jet is stated in the paper to have been computed with Mathematica; a clean-room re-derivation is recorded as the check that keeps the claim from resting on an unverified computation.
- No claim of H(n) < ∞ or H(2) = 4 is made anywhere.
