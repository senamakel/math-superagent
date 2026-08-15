# Lemma 5.4 chain — accurate settlement (scholar reconciliation)

Source anchor for the lemma: `research/notes/lemma54-re-derived-proof.md`
(claim `lemma54-re-derived-proof`). This note reconciles what durable memory
and the `research/threads/regeneration.md` thread still claim with what is
actually on disk, so no later role re-runs a closed test or treats a proved
claim as open.

## The stale claim, and the correction

**Stale (still in `regeneration.md` blocked-by and in Cognee memory):**
"Lemma 5.4 needs two final links before it is an established proof:
(1) v ≤ g*_n — verifier written but NOT run; (2) the failing-side success
identification — vacuous on the failing side, needs a failing-side test."

**Current ledger:** both are resolved.

1. **The abstract lemma is PROVED on the even domain** (`lemma54-re-derived-proof`,
   `status: proved`). The proof is a clean parity-preserving descent: with
   `eps ∈ {0,2}^L`, even `v ≤ 2ν_2+2`, the orbit lands in `{0,2}` by step L and
   stays (even δ never hits 1; each ε=2 with δ≥2 drops δ by exactly 2; the
   δ=0 case bounces into {0,2}, which is absorbing). Machine-brute-forced over
   all {0,2}^L patterns L=1..16 (2.6M even pairs, 0 violations), budget exactly
   tight, validated on 281 real prime diagonals (all satisfy the hypothesis).
   The "two links" framing is superseded: the served `v` need not be the
   budget-constrained quantity for the real application — what is measured
   directly is `v_n ≤ 2ν_2(q_{n-1})+2` (281/281).

2. **The failing-side test HAS been run, non-vacuously.** The claim
   `lemma54-sufficiency-survives-proper-domain` (`status: checked`,
   `code/out/lemma54_rederive_filtered.notes.md`) ran random valid 2-then-odds
   sequences that genuinely fail: 390,657 total failing columns across three
   gap families, yet **zero** counterexamples in the 187,123 columns where the
   Lemma-5.4 hypothesis holds on a successful prefix. The earlier "vacuous"
   remark applied only to the all-successful prime columns; the synthetic
   failing side closed that gap.

**What remains open is unchanged and separate:** the **supply-side lower
bound** `ν_2(q_{n-1}) ≥ c·n` for some c > 0 (measured c ≈ 0.5). Lemma 5.4
itself is not the gap; the linear-density bound on 2s in the right diagonal
is. `li2023-not-bottleneck` records that the demand exponent α ∈ {0.52,0.525}
is immaterial once a positive-linear supply bound holds (any β < 1 suffices).

## What the scholar verified while reconciling

- The two primary theoretical sources (Granville 2026, CHT 2026 FULLPDFs) are
  fully digested with verbatim statements, located proof gaps, and claim
  blocks: `research/notes/lemma54-re-derived-proof.md`,
  `research/notes/lemma54-re-derived.md`, `research/notes/cht-2026-summary.md`.
- Key sourced structural claims all carry `status: proved`:
  `lemma54-re-derived-proof` (even domain), `odlyzko-block-lemma-exact`
  (protection constant 1), `step-law-theorem-proved` (recharge identity),
  `cht-theorem16-verbatim-fullpdf` (inverse theorem, holds-here no),
  `bcz-2023-left-edge-stabilization` (F2 involution → independent ν_2~n/2
  corroboration), `edge-interior-invertibility-sharpened`.
- Sourced claims that **do not help** are recorded so nobody re-reads them:
  p-adic Ducci corpus (Giacomelli, Lewis–Tefft — use the p-adic norm/sum, not
  the integer |a−b| map); crank-alerted Zenodo "resolutions" (Zarkouna, Okolo,
  Maréchal, Keen); Proth 1878 (retracted myth — no proof to locate).
- Contradictions in the ledger are few and already listed:
  `caldwell-proth-myth-repeats` vs `proth-myth-retracted`/`proth-citation-correction`.

## The one still-truly-open cosmetic item

`code/out/verify_lemma54_v_le_gstar.py` (Link A: `v ≤ g*_n` by the elementary
`|a−b| ≤ max(a,b)` induction) has **two captures on disk but they are vacuous** (Directive 45: `checked: 0`,
`max margin 0.000` — the suffix scan breaks on the terminal left-column 1), so
the *g*-composed* form of Lemma 5.4's sufficiency is **unverified**, not
`checked`, even though the abstract lemma and the served-v form are
proved/checked. This does not
block Route B: the real-prime application measures `v_n` directly rather than via
g*. Worth running if a coder touches it, but not a live gap.
