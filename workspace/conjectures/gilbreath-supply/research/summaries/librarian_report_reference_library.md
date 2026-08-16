# Librarian report — reference library state (this pass)

Author: librarian. Date: this pass. What is now available locally in
`research/sources/` (full texts, never edited) with digests in
`research/summaries/`, all indexed and reachable via `search_documents`.

## Scope of this pass

The workspace was reopened because the first pass's closing argument — that
every functional of the fold collapses at the coarsest scale to the mod-4
switch-pair correlation — was refuted by an explicit witness at `n=8` and
measured witnesses at correlation order `K*(n) ≈ ⌈n/2⌉`. The whole of this
pass's territory is **correlation order `1 < K ≲ n/2`** (GOAL priorities 1–4),
i.e. *beyond-pair* structure. The librarian's task is to verify and complete
the library's coverage of that specific territory.

## Coverage verdict

The library was already **mature and fully digested** (43 full texts, ~50
digests, all indexed) for the pair-correlation (K=1/switch-density) side, the
fold's own geometry (Lucas, Rule-90, k-regular, Pascal-mod-2, coding theory),
the equal-residue side (Shiu, Maynard, BFTB, Freiberg), the ergodic/CA side
(Pivato–Yassawi, Takei), and the value-domain analytic-NT side (Matomäki–
Radziwiłł, MRTF, Green–Tao).

**Gap found and closed this pass.** The reopened `K>1` territory had its
*prime-index* side (Lacasa forbidden gap-blocks congruent mod 6, unconditional;
Wu length-k residue-pattern frequencies, conditional; LES sawtooth; Lau
non-constant patterns) but lacked the *value-domain higher-moment machinery* —
the Montgomery–Soundararajan beyond-pair-correlation framework that the LOS/Wu
pair-bias work is arithmetically built on. This is the "pair correlation ↔
Cramér second-moment discrimination + singular series" layer. Fetched and
digested:

| Source | File in `research/sources/` | Source URL | Summary | Claim |
| --- | --- | --- | --- | --- |
| Montgomery–Soundararajan, *Beyond pair correlation* (Bolyai Soc. 11, 2000) | `montgomery_soundararajan_beyond_pair_correlation.full.md` | https://arxiv.org/pdf/math/0003234 | `summaries/montgomery_soundararajan_beyond_pair_correlation.md` | `msbeyond-second-moment-discriminates-plus-singular-series` |

## Honest bearing of the new source (what it does NOT do)

The Montgomery–Soundararajan source is **value-domain** (primes in short
intervals `(x,x+h]`, indexed by location `x`), while SUPPLY's fold reads
**consecutive-prime residues at prime indices**. The index-versus-value
obstruction that killed eight value-domain routes applies to it verbatim: it
does **not** transfer to the fold's prime-index residue input, does **not**
prove anything about consecutive-prime residue frequencies, and closes **no**
open request. Its genuine use is the *template* — "a K=2 (beyond-pair) second
moment separates the pair-correlation structure from the Cramér independent
model" — and the singular-series arithmetic behind the LOS/Wu heuristic. It is
a caution, not a key: even where the machinery works (short intervals), the
beyond-pair part is heuristic (prime k-tuple) and the twin-prime error term
blocks the remainder.

## The K>1 library, complete (verified)

The reopened territory (`1 < K ≲ n/2`) is now covered on both sides:

- **Prime-index, unconditional:** Lacasa et al. 2018 (forbidden gap-blocks mod 6,
  exact counts; claim `lacasa-forbidden-gap-blocks-unconditional`) — but the
  mod-6 structure **does not survive** the fold's mod-4 parity projection
  (`research/notes/lacasa_parity_projection_transfer.md`).
- **Prime-index, conditional/heuristic:** Wu 2019 (length-k pattern frequencies
  open for all k≥2; `wu-length-k-pattern-frequencies-open`), LES 2018 sawtooth
  (averaged-equidistribution; `los-sawtooth-averaged-bias-equidistributed`),
  Lau 2024 (non-constant patterns open; `lau-nonconstant-pattern-open`), LOS 2016
  (`los-switch-preferred-mod4`).
- **Value-domain higher moments (this pass):** Montgomery–Soundararajan 2000
  (`msbeyond-second-moment-discriminates-plus-singular-series`).

## Verification bound / phase-1 (unchanged, established)

Per `research/ROOT.md`: oracle to n=8000 with convention pinned; pointwise and
second-moment ceiling N=40000; dyadic sample ceiling n=2^25; three settled
restricted classes (uniform/rank, all-ones kernel, anti-dyadic balanced). This
pass added no new computation.

## Report of unavailability

- The **finite-prefix / index-domain transfer** (from the ergodic CA and
  value-domain analytic-NT theorems to the single deterministic finite-string
  fold `wt(Φ_n h)`) appears in no source and is not in the library — it is the
  run's own open step (thread `finite-prefix-transfer`).
- No source states a Walsh/subset-sum lower bound on `wt(Φ_n h)` for the fixed
  prime string (request `walsh-spectral-subset-b904`) — a gap in theorems, not a
  gap in the library.
- The `code/librarian/lacasa_projection_check.py` script verifying the
  projection-transfer conjecture is written but was not run (no computation
  tool in the librarian role); its hand-checked m=2 case confirms the claim.

## Indexing integrity

All 44 full-text sources and their digests are indexed (`index_document` run on
the new source). `search_documents` reaches every source. The `wu_*` source was
found indexed despite not appearing in earlier coverage reports — confirmed
present with its digest.
