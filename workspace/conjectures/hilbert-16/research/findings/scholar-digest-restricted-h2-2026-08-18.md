# Scholar digest — restricted-H(2) bound sources (2026-08-18 pass)

## What this pass did

Read the two sources the librarian cycle added — Ilyashenko–Llibre 2010
(restricted H(2) bound, full text held) and Fishkin 2010 (companion
perturbed-center bound, abstract level) — against the held texts, turned them
into claim blocks and Lean statements, and corrected a data-hygiene defect in
the Fishkin row.

## Established

**Ilyashenko–Llibre 2010, Theorem 5** (verified verbatim against the held full
text, lines 113–122): for any δ, σ, κ ∈ (0, 0.1), the number of δ-tame limit
cycles of a normalized quadratic field that is σ-distant from centers and
κ-distant from singular quadratic fields is at most

    |log σ| · exp(exp(10²⁵ · δ^{−31} · κ^{−2})).

This is the only known estimate of its kind — a genuine restricted bound on
H(2), result-category 2 in problem.md. It does NOT prove H(2) < ∞: the
constant diverges as σ,κ → 0, δ → 0, precisely the centres /
singular-degenerate (DRR graphics) regime.

**The appendix carries the explicit Bautin-ideal seven-jet decomposition** of
the displacement at a centre (Lemma 10): a₁≡1, a₂≡0, a₃=α₀g₂, a₄=α₁g₂,
a₅=β₀g₃+β₁g₂, a₆=β₂g₃+β₃g₂, a₇=γ₀g₄+γ₁g₃+γ₂g₂ with α₀=−2π, β₀=−2π/3,
γ₀=−5π/4 — direct primary evidence for the Bautin-ideal Lean work
(`code/lean/Lib/Bautin.lean`). Caveat: Lemma 10 was computed with Mathematica;
a clean-room re-derivation is the check that keeps this row from resting on an
unverified computation.

**Fishkin 2010, abstract-level**: the OpenAlex abstract confirms the theorem
structure — Theorem 1 bounds δ-good limit cycles of a quadratic field with a
perturbed center-like singular point (κ = distance to fields with a line of
singular points); Theorem 2 drops the center-distance assumption, complementing
Ilyashenko–Llibre.

## Data-hygiene correction (the most important finding)

**The specific exponents quoted in earlier reports (10⁷² / 10⁷⁷ / δ^{−33})
appear in NO held source and are UNVERIFIED.** They were written into
research/REFERENCE-SET-REPORT-2026-08-18-restricted-h2.md,
research/LIBRARY-STATUS-restricted-h2.md, and the previous form of
research/claims/fishkin-perturbed-center-quadratic-bound.md as if
abstract-level, but:

- the two AMS "full text" captures are generic journal landing pages with no
  mathematics;
- no obtainable abstract (AMS, MathSciNet, Semantic Scholar, OpenAlex,
  Math-Net.Ru) contains the constants;
- only the theorem structure is confirmed (OpenAlex inverted index).

The claim now states `holds-here: unchecked` for the constants. Any future
report quoting those figures without the primary text would be repeating an
unverified number.

## Files written this pass

- `research/claims/ilyashenko-llibre-restricted-h16-quadratic-bound.md` —
  fenced claim block (rewritten from invalid YAML-bullet format; the old format
  never reached the ledger).
- `research/claims/fishkin-perturbed-center-quadratic-bound.md` — fenced claim
  block with the data-hygiene correction.
- `code/lean/Lib/IlyashenkoLlibreRestricted.lean` — Cited axiom + kernel-checked
  wrapper; hypotheses are opaque axioms (not True/0), so the verdict is
  conditional, never formalised. AWAITS `lean_check` (no compiler in this pass).
- `research/summaries/ilyashenko-llibre-restricted-h16-quadratic-ar5iv.md`,
  `research/summaries/fishkin-perturbed-center-quadratic-limit-cycles.md`,
  `research/summaries/fishkin-openalex.md`,
  `research/summaries/fishkin-perturbed-center-quadratic-limit-cycles-ams.md`,
  `research/summaries/fishkin-mathnet-vol71.md`,
  `research/summaries/fishkin-mathnet-search.md`,
  `research/summaries/fishkin-perturbed-center-mathnet.md`,
  `research/summaries/fishkin-semanticscholar.md`,
  `research/summaries/fishkin-mathnet-semanticscholar-records.md`,
  `research/summaries/ilyashenko-llibre-restricted-h16-quadratic-arxiv.md`.
- `research/findings/ilyashenko-llibre-fishkin-restricted-bounds-2026-08-18.md`,
  `research/findings/fishkin-abstract-reconstruction-2026-08-18.md`,
  `research/findings/durable-local-fallback-restricted-h2-2026-08-18.md`.
- `research/threads/restricted-h2-bounds.md` — open thread: the Fishkin
  constants gap, blocked on the AMS free-archive PDF (429 this cycle).
- CONTEXT.md — Established section updated.
- Corrected the three stale report files that quoted the unverified exponents.

## Contradictions to recalled memory

None new. The pass confirmed the standing picture: no source proves H(2) < ∞;
the restricted bounds diverge exactly where the DRR-graphics obstruction lives.

## What the run still lacks

- Fishkin 2010 primary text (for the constants) — AMS free-archive PDF, 429
  rate-limited this cycle; request to the research ledger was auto-refused
  (the claim file is treated as answering it), so the gap is tracked in the
  thread `restricted-h2-bounds` instead.
- `lean_check` on `IlyashenkoLlibreRestricted.lean` (no compiler in this pass).
- Clean-room re-derivation of Ilyashenko–Llibre Lemma 10's seven-jet.
- Cognee memory store (3 failed attempts this pass; durable local fallback
  written, retry on recovery).
