# Librarian cycle report — what is now available locally

**Date:** 2026-08-18 (continuation cycle)
**Problem:** Hilbert's 16th, Part II — limit cycles of planar polynomial vector fields

## Sources added this cycle

### 1. Ilyashenko–Llibre restricted H(2) bound — FULL TEXT
- **Title:** A restricted version of the Hilbert's 16th problem for quadratic vector fields
- **Authors:** Yulij Ilyashenko, Jaume Llibre
- **Published:** Moscow Math. J. 10(2):317–335 (2010), DOI 10.17323/1609-4514-2010-10-2-317-335
- **arXiv:** 0910.3443
- **Full text URL:** https://ar5iv.labs.arxiv.org/html/0910.3443
- **Workspace path:** `research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md` (70972 bytes, 738 lines)
- **Summary:** `research/summaries/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.md` (2861 bytes)
- **Claim block:** `research/claims/ilyashenko-llibre-restricted-h16-quadratic-bound.md` (4340 bytes)
- **What it establishes:** For quadratic vector fields σ-distant from centers and κ-distant from singular quadratic fields, the number of δ-tame limit cycles is bounded by |log σ|·exp(exp(10²⁵·δ^{−31}·κ^{−2})). The appendix carries the explicit Bautin-ideal decomposition of the displacement's seven-jet: a₃=α₀g₂, a₅=β₀g₃+β₁g₂, a₇=γ₀g₄+γ₁g₃+γ₂g₂ with α₀=−2π, β₀=−2π/3, γ₀=−5π/4 and explicit polynomial β₁, γ₁, γ₂.

### 2. Fishkin companion bound — ABSTRACT LEVEL (full text rate-limited)
- **Title:** On the number of limit cycles of planar quadratic vector fields with a perturbed center
- **Author:** A. Yu. Fishkin
- **Published:** Trans. Moscow Math. Soc. 71 (2010), DOI 10.1090/s0077-1554-2010-00181-1
- **Workspace paths:** `research/sources/fishkin-perturbed-center-quadratic-limit-cycles.full.md` (AMS landing page, 5745 bytes), `research/sources/fishkin-perturbed-center-quadratic-limit-cycles-ams.full.md` (5767 bytes)
- **Claim block:** `research/claims/fishkin-perturbed-center-quadratic-bound.md` (4838 bytes)
- **What it establishes (abstract-level only):** The OpenAlex abstract confirms the theorem structure: Theorem 1 bounds δ-good limit cycles of a quadratic field with a perturbed center-like singular point (κ = distance to fields with a line of singular points); Theorem 2 drops the center-distance assumption, complementing Ilyashenko–Llibre 2010. **DATA-HYGIENE CORRECTION (scholar pass):** the specific exponents previously quoted here (10⁷²κ^{−2}δ^{−33}, 10⁷⁷κ^{−2}δ^{−33}) appear in **NO held source** — the two AMS "full text" captures are generic landing pages with no mathematics, and no abstract obtainable (AMS, MathSciNet, Semantic Scholar, OpenAlex) contains them. They are UNVERIFIED until the primary text is obtained. Together with Ilyashenko–Llibre these are the only known uniform bounds for δ-tame/δ-good cycles of quadratic fields (structure-level statement; the constants await the full text).

## Not obtained (confirmed genuine gaps)

| Source | URL | Reason |
|--------|-----|--------|
| DRR 1994 raw 121-graphic catalogue | JDE 110(1):86–133 | Paywalled (ScienceDirect 403) |
| DRR 1994/1996 Nonlinearity full texts | IOP | Paywall |
| Roussarie 1998 book | Springer | Paywalled monograph |
| **Fishkin 2010 full text** | AMS free archive | 429 rate-limited this cycle (retry legitimate) |
| Marín–Villadelprat corrigendum | SSRN 6809315 | 403 |
| ADL 2009 DI2a full text | ScienceDirect | 403 |
| Post-2015 consolidated DRR 121-graphic ledger | — | None exists in the open literature |

## Standing requests (still open)

- `complete-current-ledger-cb3d` — DRR graphic-by-graphic status table
- `dumortier-roussarie-rousseau-9c4f` — same request

## Workspace locations

- **Sources:** `research/sources/` — ~172 files, each with source URL in header
- **Summaries:** `research/summaries/` — one digest per source
- **Claims:** `research/claims/` — each claim block with hypotheses, holds-here, falsifier
- **Ledgers:** `derived/CLAIMS.md`, `derived/FRONTIER.md`, `derived/THREADS.md`, `derived/APPROACHES.md`, `derived/REQUESTS.md` — read via `read_ledger { ledger: "claims" }` etc.