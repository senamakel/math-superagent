# Citation and corroboration map for the PE156 governing sources

Coordination note: closes the open request `identify-sticker-numbers-eeda` (its
claim `km-prop91-bound`, in `khovanova-marton-archive-labeling.md`, carries the
`answers:` line) and records what searches this cycle established about the
sources' neighbourhood, so the same queries are not run again.

## Khovanova & Marton, "Archive Labeling Sequences" — surrounding literature status

- **Published record:** Amer. Math. Monthly 132(8), 2025, 780–787,
  DOI 10.1080/00029890.2025.2525050 (CC-BY; MIT dspace copy on disk at
  `research/sources/archive-labeling-amm-published.full.md`). MaRDI portal
  catalogue entry Q6901016 (zbMATH Open), MSC 00A08 recreational mathematics:
  https://portal.mardi4nfdi.de/wiki/Archive_Labeling_Sequences .
- **arXiv version with the proof:** arXiv:2305.10357v2 (on disk). ADS entry
  2023arXiv230510357K.
- **Citations:** ADS records **zero citations** of the arXiv paper as of this
  cycle's search. The AMM article appeared late 2025 (issued 2025-08-22), so
  a follow-up literature search is not yet worth repeating; the correct next
  check is "cite arXiv:2305.10357 on ADS/Semantic Scholar/Google Scholar".
- **Companion code (authors' own):** Colab notebook "Archive Labeling
  Sequences: Code"
  https://colab.research.google.com/drive/1pGfgQWvJR1IAG3t4dNnrTnc07UvyV4xC ,
  mirrored at https://github.com/gregory-marton/vhs (raw:
  raw.githubusercontent.com/gregory-marton/vhs/main/archive_labeling_sequences_code.py).
  The notebook implements counting in any base, the unbounded-binary-search
  iterator, and Table 1 verification — an independent implementation the run
  could cross-check against if ever needed. Not downloaded: the run already
  has three verified local implementations.
- **Provenance chain** already in the library: Google Labs Aptitude Test
  (Sept 30 2004, item 17) → MathWorld news (on disk) → IBM Ponder This
  April 2004 (Michael Brand, on disk) → K&M paper → OEIS catalogue.

## Corroborating universe for the per-position digit-count identity (G1)

The closed form f(n,d) = Σ_per-position contribution is standard across the
algorithmic corpus; searches this cycle surfaced these independent
statements, none of which needs downloading (the library already holds the
primary treatment, K&M §7, plus math.SE and GfG/LearnYard):

- **POJ 2282 "The Counting Problem"** (poj.org/problem?id=2282): counts all
  ten digits over [a,b], with worked sample inputs/outputs usable as oracle
  values for an independent implementation.
- **LeetCode 1067 "Digit Count in Range"**: the same [low,high] digit-count
  function, count(high) − count(low−1) per position.
- **Baeldung** (baeldung.com/cs/count-digit-occurrences) and a 2022 Stack
  Overflow thread: same column-wise periodic counting.
- **math.stackexchange 1228366** (String's answer): the symmetry identity
  f_i(10^k − 1) = k·10^(k−1) and the recursive decomposition
  f_i(10^k·a + b) by a < i / a = i / a > i — a genuinely different algebraic
  form (already reflected in `mathse-analytic-form` style claims for the
  other SE thread).
- **Mohmand, "Novel Formulae for Digit Frequency Analysis in Natural
  Numbers", JACKA 2(4) 2025, DOI 10.29103/jacka.v2i4.23794**: a published
  (low-tier, self-reported 92% speedup) restatement of the same identity.
  Recorded but deliberately **not downloaded**: it contributes no statement
  the library lacks, and the contest-answer rule prefers not storing
  unvetted journal restatements when the primary source is already on disk.

Conclusion: the identity's sourcing is saturated; no further search on it is
warranted. The run's own check (`G1-checked`) already ties the formula to the
oracle over 0..20000 for all d and to the 0..300000 d=1 solutions.

## Answer-source boundary (this cycle's action)

`research/summaries/oeis_a216398.md` previously held the published per-digit
answer terms s(1)..s(9) verbatim (filed by an early OEIS lookup before the
exclusion rule was enforced). This cycle it was **overwritten with a
quarantine notice** — the values are removed from the summaries and must not
be re-read from `research/sources/oeis-search-fixed-points.full.md` either
(which still physically contains them; that file is flagged and stays as a
source-of-record for catalogue structure only). Claims ledger and
coordination files were re-derived by that write.

```claim
id: km-citation-status
statement: >
  As of this cycle, ADS records 0 citations for Khovanova & Marton's
  arXiv:2305.10357; the paper is published (AMM 132(8) 2025, 780-787, CC-BY
  at MIT dspace) with a Colab/GitHub code companion by the same authors.
hypotheses: citation counts change over time; the published record is fixed.
holds-here: applies to the search for follow-up literature on the governing
  bound Prop 9.1 — none exists yet to fetch.
status: sourced (ADS 2023arXiv230510357K; publisher/MaRDI record; authors'
  code repository — URLs in this note)
bearing: tells later cycles not to re-search for follow-ups; the next useful
  citation check is an ADS/Scholar "cited by" query some months from now.
anchor: this note (URLs in text)
```