# Librarian cycle — 2026-08-19: division-property claim + Glen survey; requests verified closed

## What this cycle did

1. **Verified all five open requests are answerable from disk.**
   - `citable-statement-theorem-039a` → answered by `fibonacci-sturmian-complexity`
     and `req-close-factor-complexity` (Lothaire C2 sec 2.1.1, Wikipedia Fibonacci
     word, Perrin–Restivo Thm 1 — all held as full texts).
   - `citable-name-treatment-0c91`, `citable-precise-statement-600d`,
     `citable-precise-statement-d2e7` → answered by
     `universal-euclidean-geometric-floor-sum` and `req-close-universal-euclidean`
     (fhq/OI-wiki/LOJ138/AtCoder floor_sum, all held; Binner arXiv:2107.08308 full
     text held as `bin̄ner-reciprocity-fulltext`).
   The renderer lag in derived/REQUESTS.md is cosmetic; the claims carry the
   `answers:` lines.

2. **Downloaded** Amy Glen, "On Sturmian and episturmian words, and related topics",
   Bull. Austral. Math. Soc. 74 (2006) 155–160 (survey abstract of her PhD thesis)
   → `research/sources/glen-sturmian-episturmian-words-thesis-2006.full.md`,
   summary at `research/summaries/glen-sturmian-episturmian-words-thesis-2006.md`.
   Fixes the standard history (Bernoulli III 1772; Christoffel 1875; Markoff 1882;
   Morse–Hedlund 1940), maps the singular-word/circular-word/division-property
   cluster, and Ch. 7 generalizes de Luca's division property to episturmian words.

3. **Recorded a new claim** `deluca-division-property-fibonacci-word`
   (`research/claims/deluca-division-property-fibonacci-word.md`): the infinite
   Fibonacci word is the concatenation of reversals of even finite Fibonacci words
   (Fici arXiv:1508.06754 Prop. 10–11, held; original de Luca IPL 54 (1995)
   307–312, paywalled), lexicographically minimal. **Convention-corrected** to the
   PE1006 S_n indexing: S_inf = S~_2 . S~_4 . S~_6 ... and S_inf = 0 . S~_3 . S~_5
   ... (Fici indexes f_1=1, f_2=0, f_{n+2}=S_n — the claim states both forms and
   the mapping, with the displayed blocks checked).
   Stored to Cognee memory.

4. **Frontier checks**: de Luca 1995, Berstel–de Luca 1997, de Luca–de Luca 2006,
   Droubay–Justin–Pirillo 2001, Vuillon 2001 are all paywalled primaries already
   covered by held surveys/full texts (Fici, Glen–Justin survey, Berstel survey,
   de Luca 1997 structure/arithmetics, Berstel–Vuillon, Masáková–Pelantová,
   Huang–Wen). No re-fetch.

## Where the run stands

- Library: saturated on Sturmian factor complexity, factor-position theorems,
  singular/circular words, standard factors, three-gap/floor-sum, and the
  universal-Euclidean second-moment primitive. No open request remains
  unanswerable.
- The run's live gap G4 (fixed-dimensional O(log k) aggregation over the k+1
  mechanical intercepts) is new mathematics: no source establishes it. The
  division property is recorded as the concatenation identity any Fibonacci-block
  renormalisation would rest on, with the reversal caveat stated.
- Next work is computational (acceptance 4–5 wiring of ueuclid through mech_psi,
  then k=10^18 under two Fibonacci approximants), not more source curation.
