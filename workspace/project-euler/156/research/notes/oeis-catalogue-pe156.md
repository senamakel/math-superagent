# OEIS catalogue of the PE156 fixed-point sequences

Sourced from `research/sources/oeis-A014778-main.full.md`, `research/sources/oeis-A014778-full.md` (the b-file, 84 terms), `research/sources/oeis-search-fixed-points.full.md`, and the Khovanova–Marton full text (Table 2). All are on disk under research/sources/.

## The per-digit solution sequences (fixed points of f(n,d)=n)

For d = 1..9, the OEIS entries and their term counts (including n=0):

| d | OEIS (incl. 0) | terms | OEIS (pos. only) | terms |
| --- | --- | --- | --- | --- |
| 1 | A014778 | 84 | A014778 | 83 pos. |
| 2 | A101639 | 14 | A101639 | 13 |
| 3 | A101640 | 36 | A101640 | 35 |
| 4 | A101641 | 48 | A101641 | 47 |
| 5 | A130427 | 5 | A130427 | 4 |
| 6 | A130428 | 72 | A130428 | 71 |
| 7 | A130429 | 49 | A130429 | 48 |
| 8 | A130430 | 344 | A130430 | 343 |
| 9 | A130431 | 9 | A130431 | 8 |

A130432 = (number of solutions incl. 0) = 84, 14, 36, 48, 5, 72, 49, 344, 9 for d=1..9. (Divisible by d, as Khovanova–Marton explain via periodicity modulo 10^10 of the solution sets in each range [r·10^10, (r+1)·10^10), r < d.)

The d=1 sequence A014778 is famous: starts 0, 1, 199981, ... and is finite with 84 terms, the last being 1111111110. Its defining sequence is A094798 (f(n,1)), with generating function g(x) = x/((1-x)(1-x^10)) + ((1-x^10)/(1-x))^2 g(x^10).

## IMPORTANT — answer-source boundary

- A216398 is the sequence of per-digit sums s(d) — i.e. the published answer values for exactly this contest problem. **Do not download or use it.** Its first term equals the given s(1)=22786974071 only as a cross-check hint, not as data.
- **CONTAMINATION WARNING:** the on-disk search-results page `research/sources/oeis-search-fixed-points.full.md` contains A216398's %S line verbatim — the actual s(1)..s(9) values are physically in this folder. Nobody may read those numbers into a claim, a verification, or a report. The run's answer must come from its own programs; agreement with anything in that file is *not* a certificate, it is contamination. The summary `research/summaries/oeis-search-fixed-points.md` carries the same warning.
- The per-digit b-files (b014778.txt, b101639.txt, ... b130431.txt) are the complete solution lists. **Do not download them as a shortcut.** The b-file for A014778 is already on disk (it is the d=1 example the problem statement itself discusses and OEIS documents as a sequence); the run's own program must produce the rest.
- What the library legitimately holds: definitions, term counts, finiteness proofs, and the search bound. What the run must compute: the actual terms and sums.

```claim
id: oeis-per-digit-counts
statement: The number of fixed points of f(n,d)=n (counting n=0) for d=1..9 is 84, 14, 36, 48, 5, 72, 49, 344, 9 (OEIS A130432); positive-only counts are 83, 13, 35, 47, 4, 71, 48, 343, 8.
hypotheses: d ∈ {1..9}, f(n,d) counts digit d in 0..n inclusive; duplicate n across multiple d counted separately (per problem note).
holds-here: holds.
status: sourced (OEIS A130432, A014778, Khovanova–Marton Table 2; on disk)
bearing: the run's solution.py must find exactly these counts per digit; a disagreement is a red flag on completeness of the search.
anchor: research/sources/oeis-search-fixed-points.full.md
```

```claim
id: d1-sequence-finiteness
statement: A014778 (fixed points of f(n,1)=n) is finite with 84 terms, the last being 1111111110; it consists of six runs of ten consecutive numbers, ten pairs, and four isolated numbers. The finiteness follows from A(k)/k → ∞ where A(k) = (1/10)Σ_{i≤k}(1+⌊log10 i⌋) bounds the count of 1s below k.
hypotheses: decimal base; d=1.
holds-here: holds.
status: sourced (OEIS A014778 comments; on disk)
bearing: independent catalog check for d=1; the run's enumerator should recover the same 84 values.
anchor: research/sources/oeis-A014778-main.full.md
```

```claim
id: oeis-not-answer-source
statement: OEIS A216398 (per-digit sums s(d)) and the per-digit b-files are the published answer data for PE156 and are excluded from the library by the contest-answer rule.
hypotheses: n/a.
holds-here: n/a — policy mark, not a mathematical claim.
status: policy (contest-answer exclusion)
bearing: prevents the run from shortcutting; the answer must be derived by the run's own programs.
anchor: research/sources/oeis-search-fixed-points.full.md (where A216398 appeared and was flagged)
```