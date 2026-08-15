# ROOT.md — Gilbreath's conjecture: state of the run

## The object and the reduction

`A_0 = (2,3,5,7,...)` primes, `A_{k+1}(i) = |A_k(i) - A_k(i+1)|`. The conjecture
is `A_k(0) = 1` for all `k ≥ 1`. By elementary parity (see
`notes/reduction.md`), the shape `(odd, even, even, ...)` is preserved and
`A_{k+1}(0) = |1 - A_k(1)|`, so the conjecture is **equivalent** to

> `A_k(1) ∈ {0, 2}` for every `k ≥ 1`.

This is proved, not conjectural, within a parity induction. **Which side the
run is on:** the general-class side. As `problem.md` argues, the reduction is a
statement about *any* sequence `(2, odd, odd, ...)`; primality enters only to
make `2` the sole even prime and to give small gaps. A theorem for a general
Gilbreath-like class of odd-gap sequences would settle the prime case as a
corollary. The run does **not** lean on prime distribution.

## Structure of a minimal counterexample

A minimal counterexample is a row whose second entry is `4, 6, 8, ...` (any even
`≥ 4`) — equivalently, the first row index `k` with `A_k(1) ≥ 4`. Then
`A_{k+1}(0) = |1 - A_k(1)| ≥ 3` and the leading `1` is lost. By the OEIS note
(M. F. Hasler, A036262) such a value `≥ 4`, once it has zeros ahead of it, keeps
its value and "propagates" toward the front; so the smallest counterexample is
searched for among rows whose leading `{0,2}` block has *ended* and cannot be
regenerated in time. Consumption (a block of length `n` protects `n` rows per
Odlyzko's exact lemma — see below; the `≈ n/2` figure in the original brief is
superseded by the sourced constant) vs regeneration is the whole obstruction.

## Current verification bound

- **This run, computed:** `code/out/witnesses.json`, exact integer arithmetic,
  sieve to 400000 (33860 primes), `depth_verified = 600`, with
  `leading_entry_is_1 = true`, `second_entry_always_0_or_2 = true`,
  `min_leading_02_block = 2`. Checked against problem.md's rows `A_1..A_5`.
  `code/pattern/blocks_deep.py` pushed to **depth 1000** (sieve to 20,000,000,
  1,270,607 primes): `first_bad = None`, agrees on k=1..40, longest pure
  erosion run 838 rows, regeneration still occurring (max jump 360698 at
  k=146); see `code/out/blocks_depth1000.json`. (The 838-row "run" k=162..999 is
  a finite-width artifact — the block fills the remaining sieve row and
  retracts one column per row; genuine live-regime longest pure-erosion run is
  13. See CONTEXT.md "Numbers".)
- **Cross-checked against the OEIS catalogue:** `block_profile(k) = A000232(k) − 1`
  for k=1..16 (independent source agreement on the data).
- **Reported in the literature (sourced, not reproduced here):** current
  verification record is **Colonna/Delahaye 2025–26 to all primes < 1.5×10^15**
  (completed 2026-03-18, 57,600 G(π(x)) values, absolute record G(π(x)) = 811 at
  x ≈ 1.2125×10^15); Plouffe 2025 to 10^14 (arXiv:2510.06688, G=693 at
  π(10^14)); Odlyzko 1993 to 10^13 (≈ 3.4×10^11 rows, G=635). Claim
  `verification-record-2026` in `research/notes/library-state.md` carries the
  full record table with sources. These must never be conflated with the run's
  own depth 600 / 1000.

## Restricted classes of Gilbreath-like sequences settled, with hypotheses

All three below are **proved** by the elementary mechanism in
`notes/reduction.md` (once a row reaches a shape `(1, c, c, ...)`, `c ∈ {0,2}`,
the leading `1` persists forever). They are the "regeneration already complete"
corner cases — they show the mechanism but do **not** settle the open
regeneration question, which is about rows that must *enter* the `{0,2}` regime
repeatedly.

1. **Consecutive odds.** `A_0 = (2, 3, 5, 7, 9, ...)` (all odd integers ≥ 3).
   Then `A_1 = (1, 2, 2, 2, ...)`, so `A_2 = (1, 0, 0, ...)` and leading `1`
   persists forever. Hypotheses: gaps between consecutive non-initial terms are
   exactly `2`. Status: proved.
2. **First-difference constant-tail of 2s.** Any sequence with
   `A_1 = (1, 2, 2, ..., 2)`. Then leading `1` persists forever (same
   argument). Hypotheses: `A_0` is `(2, odd, odd, ...)` and `A_1` is `1` then a
   constant tail of `2`s. Generalises (1). Status: proved.
3. **Reaching a constant `(1, c, c, c, ...)` row.** Any sequence whose
   iterated-difference triangle reaches a row of the form `(1, c, c, c, ...)`
   with `c ∈ {0, 2}`. From that row the leading entry is `1` forever.
   Hypotheses: the triangle attains such a row (full regeneration into a
   constant tail). Status: proved.

**Not settled (open goals)**: the general class "2 followed by odd numbers with
gaps bounded by `g`", and the regeneration claim that the `{0,2}` regime is
entered infinitely often.

Odlyzko's block lemma is now **sourced with its exact constant**: if
`d_K(1)=1` and `d_K(n) ∈ {0,2}` for `1 ≤ n ≤ N`, then `d_k(1)=1` for
`K ≤ k ≤ N+K−1` — a leading `{0,2}` block of length `N` protects **`N`
subsequent rows** (one per block entry), not `≈ n/2`. Primary source: Odlyzko
1993, *Iterated absolute values of differences of consecutive primes*, Math.
Comp. 61(203) 373–380, intro (full LaTeX at
`sources/odlyzko-1993-iterated-differences-latex-source.full.md`); independently
stated in Killgrove–Ralston 1959, Math. Comp. 13:121–122 (full PDF at
`sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`).
Sourced, and **re-derived by this run** with the constant made explicit (one row
protected per `{0,2}` block entry, not `n/2`) — see `notes/block_lemma.md`,
verified exhaustively on adversarial block patterns and against the real prime
rows.

`research/approaches/sign-coherence-forward-differences.md` (linearization via
`A_k(i) = |Δ_k(i)|`) is **REFUTED at its base step** — the identity is false on
the primes from (k,i)=(3,2) (inside the {0,2} block; |Δ_3(2)|=4 vs A_3(2)=0)
and at position 1 from k=4; 60/60 random 2-then-odds samples fail within 3
rows, so the failure is generic to the class, not a prime artifact
(claim `fwd-diff-identity-refuted`,
`code/out/check_fwd_diff_identity.captured.txt`).

```claim
id: block-profile-equals-a000232-minus-1
statement: The length of the leading {0,2} block in row A_k of the prime Gilbreath triangle satisfies block_profile(k) = A000232(k) - 1 (number of terms before the first term > 2 in the (k)-th difference, minus 1).
hypotheses: A_0 = primes; block counts consecutive initial {0,2} entries of A_k.
holds-here: yes
status: catalogued (matches the OEIS b-file terms for k=1..16); our own profile computed to depth 600 in witnesses.json
bearing: independently confirms the run's row data against the published catalogue; lets claims about block length be phrased in a catalogue-backed quantity.
anchor: code/out/witnesses.json + oeis-A000232
answers: are-our-block-lengths-reliable
```

## Sources in the library

- `oeis-A036262` (iterated prime differences) and `oeis-A000232` (block lengths):
  catalogue terms, the `≥4`-propagation note (Hasler, agrees with our reduction),
  Odlyzko `10^13` citation. **Digested.**
- `encyclopedia-of-math`, `mathworld` (Gilbreath's conjecture): statement,
  Odlyzko `10^13`, Killgrove–Ralston 1959 `k<63419`. **Digested.**
- `odlyzko-publications-page`: bibliography only; confirms the Odlyzko 1993
  paper exists (pp. 373–380) but contains no statements. **No help for content.**
- `blair-morgan-2026-local-condition-frontier` and
  `blair-morgan-2026-return-of-the-lemma` (Zenodo 10.5281/zenodo.19143644 and
  .19144967, March 2026): the two working papers on the {0,2}-basin / frontier
  formulation — the local-condition sufficiency theorem (Conjecture L
  `|G_r[2]−G_r[1]| ≤ 2` ⇒ GC, verified numerically to 100,000 rows) and the
  proved corridor obstruction (no pure minimal 8→7→6→5→4 erosion from Row 2).
  **Landed and digested this build (full texts + summaries + claim blocks
  `morgan-local-condition-sufficiency`, `morgan-frontier-basin-and-corridor-obstruction`).**
- **Closed:** any *proved* theorem on a nontrivial deterministic
  bounded-gap class. Not in the library and now shown to be unattainable by a
  pure gap bound: for gap bound g, parity forces g=2 (the trivial consecutive
  odds class, proved) or g≥4 (killed by Colonna's deletion counterexample —
  claim `colonna-deletion-left-edge-failure`). Chase 2024 and CHT 2026 are the
  random/Cramér analogues (both landed); Croft's bounded-gap generalisation is
  refuted by Eppstein (`anti-gilbreath-construction` in
  `notes/library-state.md`).

The Odlyzko 1993 full text (block lemma with constant) is **landed** and has
been re-derived here. A deterministic class theorem would need a non-gap
hypothesis (CHT two-separated non-concentration); the three restricted classes
above are stated from this run's own elementary proof, corroborated by the
landed block-lemma sources.

## Probabilistic-model grounding (Banks–Ford–Tao 2023) — landed

The random-analogue side of the run (Chase 2024, CHT 2026, Tao Cramér-model blog) ultimately rests on probabilistic models of prime gaps. The canonical peer-reviewed treatment is now in the library:

- **Banks, Ford & Tao, "Large prime gaps and probabilistic models", Invent. math. 233 (2023) 1471–1518** (open access CC BY, doi 10.1007/s00222-023-01199-0). Full text at `research/sources/maier-pomerance-2023-large-prime-gaps-probabilistic-models.full.md` — NB the filename is a misnomer; the authors are Banks, Ford & Tao, and the header comment in the file records this. Summary with claim block `bft2023-cramer-model-canonical` in `research/summaries/banks-ford-tao-2023-large-prime-gaps-probabilistic-models.md`.
- It states precisely Cramér's 1936 model (→ largest gap ~ log²x a.s.), Granville's corrected model (~ ξ log²x, ξ=2e^{-γ}=1.1229...), and a new random-sieve model satisfying uniform Hardy–Littlewood and RH. It documents the two failures of the plain Cramér model that make a random-model → primes transfer heuristic rather than rigorous: prime-k-tuple residue bias, and Maier's short-interval phenomenon.
- Cramér's original 1936 paper remains unobtainable as text (scanned PDF over the conversion cap on all routes) but its content is fully grounded through this paper, Chase 2024, and CHT 2026. Repository records held in `research/summaries/cramer-1936-order-of-magnitude-prime-gaps.md` and `research/summaries/cramer-1937-prace-matematyczno-fizyczne-prime-gaps.md`.

## Parser-protection: settled-conclusion notes list their claim ids here (Directive 72)

The CLAIMS.md "missing rows" are a **rendering cap, not a drop** (Directives
72/73, closed). The table renders MAX_ROWS = 60 claims, sorted alphabetically by
id, and issues the `_N further claims not shown_` disclosure; late-alphabet ids
like `spad-nondegenerate-linear-refuted` sit past the first 60 and are simply
not rendered — they are parsed and stored the whole time (`search_claims`
resolves every one of them). A `MAX_FILES = 400` walk bound exists
(src/orchestrator/claims.rs:58) against 537 files and is worth watching, but it
is **not** what happened here. Correct, durable reading: today every one of the
run's settled claim ids resolves via `search_claims`. ROOT.md is
hand-maintained and cannot be truncated, so this insurance stays in force: every
note asserting a settled conclusion lists its claim id here.

- `mersenne-nu2-affine-selfsimilar-recursion` — `research/notes/mersenne-nu2-affine-selfsimilar-recursion.md`
  (Mersenne tail-1 affine self-similar recursion + sum closed form (3^k−3)/2; checked k=3..10).
- `mersenne-elementwise-supply-constants` — `research/notes/dyadic-mersenne-elementwise-constants.md`
  (elementwise Mersenne per-residue constants; sum c_r = 3^k−3, density (3^k−3)/(2^k−1)^2 decaying like (3/4)^k; checked k=2..10, affine law conjectural).
- `dyadic-oddfactor-affine-modulus-lifting` — `research/notes/dyadic-oddfactor-affine-modulus-lifting.md`
  (every odd period P per-residue affine mod L = 2^ord2(P)−1; Mersenne density (3^k−3)/(2^k−1)^2 = A058809; Fermat-like P=2^m+1 density (3^m−1)/(2^(2m)−1) = A024023; density confirmed exactly k=3..10 this run, code/out/mersenne_density_decay.captured.txt).
- `spad-nondegenerate-linear-refuted` — `research/notes/spad-nondegenerate-linear-refuted.md`
  (anti-dyadic converse refuted; the block the derivation was dropping).
- `spad-prime-anti-dyadic-proved` — `research/notes/prime-anti-dyadic-proof.md`
  (prime mod-4 switch bit not eventually periodic; proved conditional on Shiu 2000 + elementary residue infinitude;
  anchor `code/out/prime_antidyadic_anchor.captured.txt`).
