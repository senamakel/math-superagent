# Library completeness audit — PE156

Question this answers: what is the state of the reference library for the PE156
run, and which searches are now spent?

## Updated this cycle (librarian)

The precedent tier for the two open approaches is now on disk, closing the only
`precedent: _unchecked_` rows in `research/APPROACHES.md`:

- Allouche–Shallit 1992 ("ring of k-regular sequences") is paywalled and recorded as
  unobtainable for free; its three needed theorems are on disk **quoted verbatim** in
  freely-available primary sources downloaded this cycle:
  - Coons, "Regular sequences and the joint spectral radius", arXiv:1511.07535
    (`sources/coons-regular-sequences-joint-spectral-radius.full.md`) — A–S Lemma 4.1
    linear-representation theorem (stated in full, §1), plus the growth-exponent
    theorem log_k ρ(A_f) = GrExp(f).
  - Krenn & Shallit, "Decidability and k-regular sequences", arXiv:2005.09507v3
    (`sources/krenn-shallit-decidability-k-regular.full.md`) — A–S Thm 3.1 (prefix-sum
    closure) and Thm 6.1 (per-digit count is k-regular), both cited by number; also a
    worked 2-regular linear representation.
- Mahler ⟺ regular: Adamczewski, Bell & Smertnig, JEMS 25 (2023) 2525–2571,
  arXiv:2003.03429 (`sources/abs-height-gap-mahler-regular.full.md`), Thm 1.2(b).
- Stephan, "Divide-and-conquer generating functions I", arXiv:math/0307027
  (`sources/stephan-divide-and-conquer-generating-functions.full.md`), the two-citation
  frontier lead from the Ruskey paper.

All recorded with claim blocks in `research/notes/k-regular-and-mahler-theory-precedents.md`
(ids `as-linear-representation`, `as-digit-count-and-prefix-closure`,
`abs-mahler-regular-height-ologn`, `coons-growth-exponent-joint-spectral-radius`,
`stephan-dc-generating-functions-classification`). Shallit's papers page
(`sources/shallit-papers-page.full.md`) is on disk as the bibliography lead for anything
his group published on these sequences; it adds no new working row.

## Verdict: the library is complete for this problem

Every angle the problem needs is on disk, sourced, and claim-ledgered:

| Angle | Source(s) on disk | Claim/note |
| --- | --- | --- |
| Problem statement (official) | `problem.md` (projecteuler.net/minimal=156) | — |
| Governing theory — digit-count closed form (G1) | Khovanova & Marton §7 (arXiv + AMM), math.SE 47477, GfG/LearnYard per-position/Digit-DP | `G1-digit-count-closed-form`, `G1-checked` |
| Finite search bound (G2) — Prop 9.1: x ≤ d·b^b | Khovanova & Marton, arXiv:2305.10357v2 §9 (proof) + AMM 132(8) 2025 §4 (statement, Table 3) | `G2-solution-bound`, `km-prop91-bound` |
| Skip/jump completeness (G3) | K&M Lemma 7.1; Bentley–Yao unbounded searching (independent justification) | `km-lemma71-skip`, `bentley-yao-unbounded-search` |
| Solution catalogues | OEIS A014778 (84 terms incl. 0, b-file), A094798 (f(n,1)), per-digit IDs A101639–A101641, A130427–A130431; counts A130432 = [84,14,36,48,5,72,49,344,9] | `oeis-per-digit-counts`, `d1-sequence-finiteness` |
| d=0 boundary | OEIS A364972 (bases with no zero fixed point), K&M Theorem 8.1 | note `oeis-A364972-zeros-bases` |
| Provenance / puzzle family | IBM Ponder This April 2004 (Michael Brand); MathWorld news on Google Labs Aptitude Test 2004 item 17 | `mathworld-provenance` |
| Answer | computed by run's own programs, two independent routes | `PE156-grand-total-verified` |

## The open request is answered — and REQUESTS.md is stale

`REQUESTS.md` still lists `identify-sticker-numbers-eeda` ("sticker numbers /
exactly numbers" paper) as open. It is not: the paper is **Tanya Khovanova and
Gregory Marton, "Archive Labeling Sequences"**, arXiv:2305.10357v2 (proof of
Prop 9.1, §9) and Amer. Math. Monthly 132(8) 2025, 780–787, DOI
10.1080/00029890.2025.2525050 (bound statement, §4, Table 3). Both full texts
are on disk. The claims `G2-solution-bound` (note `claim-g2-solution-bound.md`)
and `km-prop91-bound` (note `khovanova-marton-archive-labeling.md`) carry
`answers: identify-sticker-numbers-eeda`. The row closes when the derived
ledger is next rewritten.

## Searches that are spent — do not re-run

- The per-position digit-count identity: saturated (primary source + three
  independent formulations + run's own oracle check to n ≤ 20000). See
  `km-citation-and-corroboration-map.md` for the surrounding literature status
  (POJ 2282, LeetCode 1067, Baeldung, math.SE 1228366, JACKA paper — all
  recorded, none needed).
- Follow-up citations of arXiv:2305.10357: ADS records zero as of this cycle;
  the AMM article only appeared 2025-08-22. Re-check "cited by" in months, not
  now.
- OEIS infrastructure links (oeisf.org, oeis.org) cited by the A014778 page
  itself: navigation, not leads.

## What would justify a new download

A source that (a) supersedes or corrects Prop 9.1's bound, (b) carries
per-digit solution *counts* that disagree with A130432 (completeness flag), or
(c) is a genuinely new proof route for G3. Nothing matching surfaced this
cycle; none is expected.

---

## Librarian audit addendum (2026 cycle)

Re-verified the whole corpus against the physical files; the audit held
everywhere it could be checked, and two small gaps were fixed:

- **Gap fixed:** `research/summaries/oeis-A364972-zeros-bases.md` claimed a
  full text at `research/sources/oeis-A364972-zeros-bases.full.md` that did not
  exist. The b-file was downloaded from https://oeis.org/A364972/b364972.txt
  (62 terms: bases ≥ 2 with no zero-count fixed point; 10 ∈ A364972, matching
  K&M Theorem 8.1 that a=(0) is undefined in base 10), placed at that path,
  and both files re-indexed into Cognee.
- **Dangling pointers fixed** in three summaries (A014778 b-file location,
  Ruskey abstract-page location) so every `research/sources/...` reference
  resolves to a file that exists.
- **Request closure confirmed:** REQUESTS.md now re-derives to "None open"
  for `identify-sticker-numbers-eeda`, whose answer (K&M, Prop 9.1) has been
  on disk since before this cycle.
- **Verification of prior-run evidence:** `code/out/brute-oracle-output.txt`
  reproduces the statement's oracle (f(n,1) table n=0..12, f(22,2)=6, first
  solutions 0,1,199981, f(n,1)=3 never in 0..300000); `code/out/verify-output.txt`
  and `code/out/solution-run.log` agree on the grand total 21295121502550 with
  per-digit sums and counts equal to the sourced A130432;
  `code/out/solutions-d1.txt` equals the OEIS A014778 b-file term-for-term,
  84 terms ending in 1111111110.
- **Answer-source boundary respected:** A216398's term list is quarantined
  (the search-results page still physically holds it — flagged, never read as
  data). The run's answer was computed by its own programs; catalogue entries
  were used only for counts, finiteness, and the search bound.
- No `INDEX.md` was created under `research/` (Cognee is the sole durable
  catalogue there); the `refresh_index` refusal on those paths is the
  workspace rule doing its job, not an error.
