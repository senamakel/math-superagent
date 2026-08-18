# Library status — restricted-H(2) bounds row

## This cycle (2026-08-18): two restricted H(2) bounds added

### Ilyashenko–Llibre, "A restricted version of the Hilbert's 16th problem for quadratic vector fields"
- Moscow Math. J. 10(2):317–335 (2010); arXiv:0910.3443
- **Full text held:** `research/sources/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.full.md` (URL https://ar5iv.labs.arxiv.org/html/0910.3443)
- **Claim:** `research/claims/ilyashenko-llibre-restricted-h16-quadratic-bound.md`
- **The bound:** # δ-tame limit cycles ≤ |log σ|·exp(exp(10²⁵δ^{−31}κ^{−2})) for quadratic fields σ-distant from centers, κ-distant from singular fields.
- **Library value:** only known estimate of this kind; appendix carries the explicit seven-jet Bautin decomposition (a₃=α₀g₂, a₅=β₀g₃+β₁g₂, a₇=γ₀g₄+γ₁g₃+γ₂g₂) — primary evidence for `code/lean/Lib/Bautin.lean` and `code/bautin/`.

### Fishkin, "On the number of limit cycles of planar quadratic vector fields with a perturbed center"
- Trans. Moscow Math. Soc. 71 (2010); DOI 10.1090/s0077-1554-2010-00181-1
- **Abstract-level held:** `research/sources/fishkin-perturbed-center-quadratic-limit-cycles.full.md` + `-ams.full.md` (both generic AMS landing pages, NO mathematics); **abstract obtained via OpenAlex** (`research/sources/fishkin-openalex.full.md`); **full text NOT obtained** (AMS PDF 429 this cycle; free archive vol 71, retry legitimate)
- **Claim:** `research/claims/fishkin-perturbed-center-quadratic-bound.md`
- **What is established (structure, from the OpenAlex abstract):** Thm 1 bounds δ-good limit cycles of a quadratic field with a perturbed center-like singular point (κ = distance to fields with a line of singular points); Thm 2 drops the center-distance assumption, complementing Ilyashenko–Llibre. **DATA-HYGIENE CORRECTION (scholar pass 2026-08-18):** the exponent figures previously quoted here (10⁷²κ^{−2}δ^{−33}, 10⁷⁷κ^{−2}δ^{−33}) appear in NO held source — they are UNVERIFIED and must not be repeated without the primary text.

## Standing state (re-confirmed, unchanged)
- ~172 full-text sources in `research/sources/`, each with digest in `research/summaries/` and URL in header.
- Canonical tier held: Encyclopedia of Mathematics, MathWorld, Scholarpedia, Ilyashenko 2002 Centennial, Hilbert 1900, Ilyashenko–Yakovenko Lectures.
- DRR status ledger: **no consolidated post-2015 graphic-by-graphic ledger exists**; triangulated picture 89/121 + boundary-only 3 + (H³₁₄) open w/ Lu 2026 unrefereed + ≥11 degenerate open. Both DRR-ledger requests stay open.
- Not obtained (genuine): DRR 1994 raw catalogue (paywalled), DRR 1994/1996 Nonlinearity full texts (paywalled), Roussarie 1998 book, Fishkin full text (rate-limited this cycle), Marín–Villadelprat corrigendum (403), ADL 2009 DI2a full text (403).

## Evidence discipline
- Ilyashenko–Llibre: asserted-by-source from held full text. Fishkin: asserted-by-source abstract-level only, upgrade flagged. Lemma 10's Mathematica-computed seven-jet flagged for clean-room re-derivation. No claim of H(n)<∞ or H(2)=4.
