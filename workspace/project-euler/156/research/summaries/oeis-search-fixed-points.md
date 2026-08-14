# OEIS search — "equal to the number of" "in the decimal digits of all numbers"

**Source:** https://oeis.org/search?q=%22equal+to+the+number+of%22+%22in+the+decimal+digits+of+all+numbers%22&fmt=text (OEIS full-text search with fmt=text, witnessed). Full text: `research/sources/oeis-search-fixed-points.full.md`.

## ⚠ CONTAINS THE PUBLISHED ANSWER — DO NOT USE AS DATA OR AS VERIFICATION

The full search-results file **physically contains the entry for A216398**, whose %S line is the per-digit sum sequence s(1)..s(9) — **exactly the answer PE156 asks for**. These numbers are on disk (lifted with the search page before the answer-source exclusion rule was enforced). They are the values the run must DERIVE, never read back. Rules for anyone touching this file:
- Do not copy A216398's terms into any report, claim, or verification.
- Do not use any of the per-digit b-file data quoted here as a shortcut; the catalogue NOTE `research/notes/oeis-catalogue-pe156.md` already flags A216398 and the per-digit b-files as excluded.
- The granted use of this file: the *catalogue structure* it establishes (which A-numbers exist, their declared term counts, their finiteness/cross-references) — same information as the paper's Table 2.

## What the search establishes (catalogue facts only)

- It is a full-text OEIS search for "equal to the number of [X]'s in the decimal digits of all numbers", returning 11 sequences: A014778, A130427, A130428, A130429, A130430, A130431, A130432, A216398, A101639/A101640/A101641.
- Each entry is the list of numbers n with n = count of digit d in 0..n (d = the sequence's digit), declared **finite and complete** (keyword `fini,full`):
  - A130427 (d=5): exactly 0,1e10,2e10,3e10,4e10 — 5 terms (matches paper Table 2).
  - A130431 (d=9): 0,1e10,…,8e10 — 9 terms.
  - A130432: per-digit counts incl. 0 = 84,14,36,48,5,72,49,344,9 (d=1..9).
  - Cross-references: "A014778 for proof these sequences are finite"; all count entries cite Khovanova–Marton AMM 2025 p. 783 (Table 2) and arXiv:2305.10357.
- A014778 full entry (d=1, 84 terms) with: finiteness proof sketch (Joseph L. Pe: A(k)/k → ∞), structure comment (six runs of ten, ten pairs, four isolated — David Wasserman), history (final term 1111111110 shown complete by H. van Haeringen & L. Kok Dec 2004, independently Propper & Pratt Jan 2005, no more terms ≤ 10^9 per Propper Dec 2004).

## Implications for PE156

- Provides the catalogue term counts (already in claim `oeis-per-digit-counts`) and the finiteness/history for d=1 — nothing about the sums.
- The only new, act-on-this information: **the answer data physically lives in this folder**; the run's verification must come from its own programs, and nobody should treat a "surprising agreement" with anything in this file as a certificate.

## Does not settle

- The actual s(d) values (forbidden to read), nor the search bound proof (that is Prop 9.1 of the arXiv v2 paper, not here).