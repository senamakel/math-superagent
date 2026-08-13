# Library acquisition cycle 7 — canonical-site gap closure, Subbarao bibliography anchor

Date: 2026-08-13. Librarian cycle.

## What this cycle added

| Path | What it is | Verdict |
| --- | --- | --- |
| `research/summaries/erdos-1052-discussion-forum.md` | Erdős Problems #1052 discussion thread (https://www.erdosproblems.com/forum/discuss/1052) | **NEGATIVE FINDING — empty.** 0 comments as of 2026-08-13. Nothing beyond the problem page (already held as `erdos-problem-1052`). The download tool stored the 3.7 KB conversion under `summaries/` only; no `sources/*.full.md` exists for it |
| `research/summaries/erdos-1052-proof-claims-thread.md` | Erdős Problems #1052 proof-claims thread (https://www.erdosproblems.com/forum/thread/1052/proof-claims) | **NEGATIVE FINDING — empty.** "No proof claims have been submitted yet." 0 claimed proofs. Do not re-fetch either forum page. Same storage note as the discussion thread |
| `research/sources/subbarao-publications-ualberta.full.md` | M.V. Subbarao's complete publication list, U. Alberta (`https://www.math.ualberta.ca/~subbarao/publications.html`), ~140 entries 1942–2007, direct PDF links to nearly all items | **BIBLIOGRAPHIC ANCHOR (primary).** Confirms the 1970 AMM note and 1972 Delta note exist with exact shelf data (see below). No mathematics beyond the list |
| `research/summaries/subbarao-1970-infinity-unitary-perfect.md` | Attempted full text of Subbarao, *Are There an Infinity of Unitary Perfect Numbers?*, AMM 77(4) (1970) 389–390, via the ualberta PDF link `documents/1970Infinity.pdf` | **COVER PAGE ONLY.** The PDF contains the JSTOR cover (stable URL `https://www.jstor.org/stable/2316150`), no article body. The entire downloaded content lives in this summary file (1547 bytes; the tool stored no separate `.full.md`); it must NOT be cited as the note's text |

## Attempts and confirmations this cycle

1. **Subbarao 1970 note body — still NOT held.** The ualberta link is the first genuinely new host to surface (previous cycles had JSTOR/T&F 403 and the scan-textless route). Result: JSTOR cover page only. The note is 2 pages (AMM 77(4):389–390). Its marginal content over the held 1966 paper is the elimination of **a = 8, 9, 10** (a = 0 is already 1966 Theorem 1 "no odd UPN"; a = 3, 4, 5, 7 and the classifications a = 1 → {6,90}, a = 2 → {60}, a = 6 → {87360} are 1966 Theorem 2, held in full). The claim `subbarao1970-a-ge-11` remains `asserted` — three Wall primaries (1975 §2, 1987 §2, 1988 intro, all held) attribute the full list; the body is the one falsifier. New REQUESTS row opened (see REQUESTS.md).
2. **Subbarao–Cook–Newberry–Weber 1972, Delta 3(1):22–26** — confirmed scan-textless (download exception: "no extractable text"). REQUESTS row stays OBSTRUCTED; the ualberta publications page is now the place a future OCR attempt would aim (PDF link `documents/Subbarao_Cook_Newberry_Weber1972.pdf`).
3. **McDaniel 1974, *On multiple prime divisors of cyclotomic polynomials* (Math. Comp.)** — located via search (DOI 10.2307/2005707); paywalled at JSTOR, no free text. Adjacent computational-attack item (repeated odd-prime-power divisors of cyclotomic values `Φ_n(q)`, q prime < 150); relevant context only — the run's `Φ_{4p}(2)` repeated-divisor question is exactly the shape McDaniel tables. Not fetched; recorded so nobody repeats the HTTPS 403/JSTOR attempt.
4. **Origin of the name "Higgs primes"** — fresh search found NO primary paper by Denis Higgs under this name (hits are particle-physics noise). OEIS A057447 (held) + Burris–Yeats 2004 (held, `research/sources/burris-yeats-saga-high-school-identities.full.md`) remain the definitional origin. Nothing further to acquire.

## Status of open REQUESTS rows

- Frei 1978: unchanged OPEN (captcha-walled; e-periodica Heft 4).
- Goto 2007: unchanged OPEN (paywalled at Project Euclid; MaRDI record held).
- Subbarao–Cook–Newberry–Weber 1972: confirmed OBSTRUCTED (textless scan).
- **NEW ROW: Subbarao 1970 note body** (JSTOR stable/2316150; ualberta PDF is cover-only): the single falsifier for `a ≥ 11` beyond the three Wall attributions.

## Library shape

Unchanged from cycle 6 plus the four items above. The canonical site's own pages are now fully held (problem page, discussion forum, proof-claims thread — all three; forum pages empty). The Subbarao primary bibliography is anchored. The core tier, branch target, analytic machinery, and reciprocity stack were already complete.