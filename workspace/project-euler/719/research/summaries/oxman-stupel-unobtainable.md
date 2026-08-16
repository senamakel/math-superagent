# Oxman & Stupel, "A number whose square root is the sum of its digits" — NOT OBTAINED

Reference:
V. Oxman and M. Stupel, "108.38 A number whose square root is the sum of its
digits", *The Mathematical Gazette* 108(573) (2024), 513–514.
DOI: https://doi.org/10.1017/mag.2024.122

**What it is.** A Gazette note about positive integers with sqrt(n) = sum of
the decimal digits of n (each block a single digit). That is the **single-block**
(1-block-per-digit) special case: by `proofwiki-digit-sum-bound` the only
solutions are 0, 1, 81 — a set already in the library.

**Why it was sought.** It is the closest primary source to the PE 719 rule
(`a038206-expr-recursion`) that is *not* the OEIS record itself. But the OEIS
entry A152147 records "k such that sum of digits of k^n = k" and cites this note
as background, confirming its subject is the digit-sum (single-block) case, not
the general multi-block split.

**Why it is NOT in the library.** The DOI resolves to a scanned PDF at Cambridge
Core with no text layer; `download_document` returned "no extractable text".
The content is paywalled behind a journal subscription. All authoritative
equivalents of what it would add are already held:
- the single-block result (0,1,81) — `research/summaries/proofwiki_sumofdigits_sqrt.md`;
- the two-block parametrisation — `research/summaries/iannucci-kaprekar-numbers.md`
  and `research/summaries/dudeney-torn-number-solution.md`;
- the general multi-block rule and its exact `expr` recursion — the OEIS records
  `research/summaries/oeis_a038206_b.md` / `oeis_a104113.md`.

**Do not re-fetch.** It is unobtainable in accessible form and adds nothing the
library does not already establish for PE 719.
