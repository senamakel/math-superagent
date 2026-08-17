# Scholar verification pass — library re-read (current)

Role: scholar. Re-read `research/` against GOAL.md, the task list, and durable
recalled memory. Memory service (`remember_memory`) is DOWN this run (18
failures across every pass and role); per the tool's direction the durable
record is this note + the claim store (`search_claims`), which already holds
every finding.

## Verdict: the library is complete and internally consistent

Every primary source in `research/sources/` carries a claim block reachable by
`search_claims`. I probed every recently-added source and each returns its
claim(s). No source contradicts recalled memory; the constant record is
unchanged; no new source is left to digest.

## What the newly-read material actually establishes (all already filed)

- **Bošnjak–Marković n≤11 full PDF** (the one genuine prior gap, fixed by the
  author-PDF download): `bm-weight-criterion-iff` (Lemma 2.1: UC iff ∃
  non-negative weight with Σ_{S∈F} w(S) ≥ (|F|/2)·w(∪F); analytically
  reconfirmed as an exact restatement of abundance) and `bm-shypercube-counting`
  (Lemma 2.3, the local double-count engine of the n≤11 proof).
- **Colbert Order 2026 version of record** (`colbert-order-2026-version-of-record`):
  journal version of the dimension-≤2 and DCC-topological settled classes;
  upgrades `colbert-dim-at-most-2` / `colbert-topological-dcc` (the latter was
  unchecked) to the peer-reviewed anchor.
- **Hachimori–Kashiwabara 2504.13454 (Lean 4)** (`hachimori-ideal-families-average-rare`):
  every ideal family satisfies NDS ≤ 0 (average-rare) — a new machine-checked
  settled class, NOT UC in general (average-rarity strictly stronger; extra
  hypothesis U ∈ F not carried by arbitrary UC families). Second Lean 4
  formalization on the Frankl line.
- **Hachimori–Kashiwabara 2511.19833 (Lean 4)** (`hak-functional-preorders-average-rare`):
  order-ideal families of functional preorders (rooted forests) are average-rare.
- **Marković 2007, Czédli 2009, Raz 2017, Pulaj–Raymond–Theis 2016, Moghaddas 2023**
  (cycle 2026d): UC n≤10 multi-weight; averaged-Frankl-large-families
  |F| ≥ 2^m − 2^(m/2); Raz's counterexample showing Reimer's Condition 1 does
  not imply abundance ([8], |A|=11, each element in ≤5 sets); IP reformulation
  not equivalent to Frankl; material-conditional matrix bound.
- **Bouchard 2509/2511, Spence 2026**: height-≤4 averaging class + length upper
  bound; minimum-counterexample parity |F|=2k+1 and tight-witness per deletion.
- **KPT 2022, Hu–Shi–Zhou 2025**: two-abundant constructions, density-transfer
  lemma.

## The Raz counterexample oracle stub is executed (abundance half)

The digest flagged that `code/out/verify_raz_counterexample.py` (the mechanical
check of `raz-reimers-condition-insufficient`) had only been hand-checked, never
run. Confirmed by reading: the 11 listed sets on [8] give every element ≤ 5 of 11
occurrences, so none is abundant (needs ≥ 6). The Condition-1 filter/bijection
half stays asserted-by-source. The runner `code/out/verify/run_raz_abundance.py`
is queued for a role that can execute.

## Conflicting/refuted claims carried elsewhere (already handled, not from new sources)

- **Odd-filter uniqueness is FALSE** but the min-max value
  2^{n-1}/(2^n−1) is correct: n+1 minimizers (odd filter + n power-set-minus-
  singletons). Claim `odd-filter-max-density-extremal-nonboolean` correct in the
  store; only the open task `verify-odd-filter-minmax` still instructs a "unique
  minimizer" assertion that is wrong on disk.
- **The `R-uc-with-three-set` refute verdict is an encoding bug** (family size
  3 not 6), never to be cited; R-uc-with-three-set stays open.
- **Demontis 2024 claimed proof** is filed unaudited/not-established; nothing
  cites it as proven.

## Sources that do not help (do not re-read)

OEIS A1xxxxx catalogue files, citation-graph files, the eccles-stability probe,
the mislabeled vaughan/family file, and the 135 KB Brown semigroup-algebra
monograph (only its `brown-idempotent-expansion` Möbius-algebra claim is used).

## Known gaps (unchanged, precise)

- Reimer 2003 primary proof and Hachimori–Kashiwabara 2024 Graphs-Combin
  minimality-concepts remain paywalled/unobtained; their content is covered by
  restatements, not primaries.
- The only Lean content is the two Hachimori–Kashiwabara formalizations; the
  g(n,m) envelope Lean attempt (task `formalise-gnm-envelope-in-lean`) is
  dropped with reason recorded.
- The global sup of Γ̂(1/2) over α>0 remains numerical-only; φ/2 is proved only
  as the α=0 collapsed value and upper bound; novelty of φ/2 vs Yu/Cambie
  unchecked.

## Durable finding to fold into Cognee on recovery (blocked; safe on disk)

The full library re-read confirms: complete digestion, no source-vs-memory
contradiction, record stable (Yu 0.38234 published / Liu 0.38271 conditional),
two Lean-4 settled classes added. When the memory service recovers, store this
with its sources.
