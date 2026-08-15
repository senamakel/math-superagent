# Gilbreath 2011 primary — eponymous source, paywalled, corroborated from a held primary

## What is missing
The canonical eponymous reference — Norman Gilbreath, "Processing process:
The Gilbreath conjecture", *J. Number Theory* 131 (2011) 2436–2441,
doi:10.1016/j.jnt.2011.06.008 — is NOT held as a primary source. The library's
claim `gilbreath-2011-expository` (Gilbreath developed the conjecture ~1958;
"the great number theorist Erdős believed it was true, he also believed it
would take about 200 years to prove") is checked against the **Houston blog
quotation**, not against Gilbreath's paper.

## What was attempted (2026, librarian)
1. `download_document` of the DOI https://doi.org/10.1016/j.jnt.2011.06.008
   returned a 110-byte "Redirecting" wrapper — Elsevier paywall stub. The
   `.full.md` landing in `research/sources/` was not written (only a 110-byte
   summary `research/summaries/gilbreath-2011-processing-process-jnt.md`, which
   is just the redirect stub and useless).
2. `citation_graph` on the DOI resolved it correctly to the 2011 paper (4
   citations), filed `research/summaries/citations_w1964428229.md`.
3. `exa_search` confirmed no open PDF mirror exists — the MaRDI portal entry
   only links back to the paywalled DOI; the arXiv mirror search returned
   nothing.

## What it is corroborated by (independent of the blog)
The paper is cited by **Bhat–Cobeli–Zaharescu, "On quasi-periodicity in
Proth-Gilbreath triangles"** — which the library HOLDS in full
(`research/sources/bhat-cobeli-zaharescu-quasi-periodicity-proth-gilbreath.full.md`).
That held primary also carries the mod-4 bicolor left-edge conjecture (digits
{0,2}, limiting proportion 1/2 each) that is directly relevant to the run's
G-supply / mod-4 switch question. The citation graph also shows the Gilbreath
2011 paper cited by the held *Filtered rays* paper (Chaos Solitons Fractals).

## Content status
The only load-bearing content of Gilbreath 2011 for this run is historical
(origin ~1958, Erdős's "200 years" belief), which IS already quotable from the
held Houston blog that reproduces the offprint's introduction verbatim
(`research/sources/houston-2012-gilbreath-conjecture-blog.full.md`). Nothing
mathematical is lost: the paper is autobiographical/expository, not a proof
attempt, and its proof-side content is fully covered by the held Odlyzko,
CHT, Chase, Ducci, and Cobeli–Zaharescu primary sources.

## Decision
Do NOT re-attempt the Elsevier DOI — no open mirror exists in two searches.
The canonical reference tier is otherwise complete (encyclopedia-of-math,
Caldwell glossary, MathWorld, OEIS A000232/A036262/A089582, Wikipedia all
held). The eponymous paper stays a named paywalled-gap with the blog+quasi-
periodicity corroboration recorded, which is a bounded, documented absence —
not an unrecorded one.
