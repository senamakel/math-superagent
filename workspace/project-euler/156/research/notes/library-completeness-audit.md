# Library completeness audit — PE156

Question this answers: what is the state of the reference library for the PE156
run, and which searches are now spent?

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
