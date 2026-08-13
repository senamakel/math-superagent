# Library acquisition cycle 1 — what was fetched, what was blocked

Status of the canonical tier and the open REQUESTS rows after this cycle.
All claims below are about *acquisition*, not mathematics; the mathematics is
in the notes/threads already in the library.

## New acquisitions this cycle

| Path | What it is | Verdict |
| --- | --- | --- |
| `research/sources/guy-unsolved-problems-number-theory-2nd-ed.full.md` | Guy, *Unsolved Problems in Number Theory*, 2nd ed. 1994, Springer; full text as converted from the unina2.on-line.it PDF | **PARTIAL ONLY**: contains pp. i–xvi (title, prefaces, contents listing B3 at p. 53, glossary of symbols). The §B3 body (pp. 53–55, the actual unitary-perfect problem text) is NOT in the converted text. Do NOT cite this file for B3 content. |
| `research/sources/goto-papers-list.full.md` | Goto's own publication list (ma.noda.tus.ac.jp) | Bibliographic control only; confirms the RMJM 37(2007) 1557–1576 citation and coauthor K. Okeya. |

## Gaps re-confirmed as OPEN (with new evidence)

1. **Frei 1978 primary text** (Elem. Math. 33 (1978) 95–96). Still captcha-walled
   at e-periodica; `retro.seals.ch` dead (connection refused). The OEIS-recorded
   theorem (UPN not divisible by 3 ⇒ `2^m | n`, m ≥ 144, ω ≥ 144, n > 10^440)
   remains **unverified against primary**. Load-bearing for "is 3 | n forced?".
2. **Goto 2007** full text — Project Euclid paywalled. MaRDI item Q2478044 and
   OEIS A002827 %F both state the UPN bound `m < 2^(2^k)` for ω(m) = k
   (k·2^k is the UHN bound; the A006086-derived "m < 2^(k·2^k)" wording in an
   earlier search hit was a misattribution — A006086 is the unitary *harmonic*
   numbers sequence).
3. **"Wall searched past 10^102"** remains an orphan claim. Held primaries
   (Wall 1975 full PDF; Wikipedia; OEIS; Guy front matter) contain no such
   figure. Actual Wall 1975 bound: eliminates N < W = 1.46×10^23 (a < 38,
   odd-part cap m < 20189 etc.). The compute-policy consequence is unchanged
   (10^23 already unreachable), but 10^102 must not be restated as sourced.
   The likely carriers are Guy §B3 (body not yet acquired) or the Wall–Hagis
   1972 letter (scanned, no text layer).
4. **Hagis 1984**, *Lower bounds for unitary multiperfect numbers*, Fib. Quart.
   22(2) (1984) 140–144 — open at `https://fq.math.ca/Scanned/22-2/hagis.pdf`
   (and `https://www.mathstat.dal.ca/FQ/Scanned/22-2/hagis.pdf`), scanned.
   Useful content (from the search-result excerpt, not yet from the file):
   Theorem 1 no odd unitary multiperfect numbers; for UMP n = 2^a·… with
   σ*(n) = kn: k = 4 or 6 ⇒ t > 51, n > 10^1010 and 2 | n... These bounds are
   for *multiperfect* numbers (k ≥ 4), not unitary perfect (k = 2), so they do
   not directly bound a sixth UPN; they are background for the budget/ω
   structure. Fetch failed this cycle; retry.

## Blocked acquisitions recorded so nobody retries the same dead routes

- Lelechenko TAAC 2014 PDF (`taac.org.ua/.../UA-2-Andrew Lelechenko-440.pdf`):
  403 Forbidden. (Alternative: the same author's *Exponential and Infinitary
  Divisors*, Ukr. Math. J., DOI 10.1007/s11253-017-1289-7, arXiv:1405.7597.)
- Subbarao 1970 AMM "Are there an infinity of unitary perfect numbers?"
  pp. 389–390: no open PDF (AMM archive paywalled); a≥11 attribution rests on
  Wall 1975/1987/1988 held texts (see `research/notes/subbarao-1970-a-ge-11.md`).
- Subbarao–Cook–Newberry–Weber 1972 Delta PDF (math.ualberta.ca): scanned,
  no text layer; download tool refuses.
- OEIS-linked letters (Wall→Hagis 1972, Subbarao→Sloane 1974): scanned, no
  text layer.
- LeanGenius erdos-1052 page: JS shell, no content (a `.lean` formal statement
  is separately held at `research/summaries/erdos-1052-formal-lean-statement.md`).

## What this cycle confirms about the library's shape

- The encyclopedic tier (Erdős problems #1052, MathWorld, Wikipedia OEIS A002827,
  Encyclopedia of Mathematics unitary divisor, Villemin) is present in the
  library (some as summaries only — the tool refuses re-download of already-held
  URLs, which is itself confirmation they are recorded with the source URL).
- The primary tier for the head theorem (Subbarao–Warren 1966, Wall 1975,
  Graham 1989, Wall 1987/1988) and for the H_even branch (Maciejewski 2026 full
  text with 3-Higgs definition at §1.1) is present.
- The genuinely missing items are exactly the four rows above, plus the B3 body
  of Guy 1994 and the Wikipedia/MathWorld full text where only summaries exist.