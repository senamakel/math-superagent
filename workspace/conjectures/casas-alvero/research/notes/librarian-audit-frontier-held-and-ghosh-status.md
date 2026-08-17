# Librarian audit — library completeness re-check (2026)

**Purpose:** Close out a librarian cycle by re-checking whether the two top rows of
`derived/FRONTIER.md` — which appear un-struck — are actually held, and re-confirm the
status of every claimed complete proof. What this note records is a *confirmation that
the library holds these sources*; it does not add claims.

## Result: the two top frontier rows are HELD (strike-through failed to render)

`derived/FRONTIER.md` lists, un-struck:
- `https://doi.org/10.48550/arxiv.1705.01704` "Casas-Alvero Conjecture is true" (cited by 11 of our sources)
- `https://doi.org/10.48550/arxiv.2312.08742` "A note on the Casas-Alvero Conjecture" (cited by 10)

Both are in the library already:
- **arXiv:1705.01704** (Dobrowolski, "Casas-Alvero Conjecture is true") —
  `research/sources/dobrowolski2017_casas-alvero-true.full.md`, source URL
  `https://arxiv.org/pdf/1705.01704`. **Confirmed WITHDRAWN**: "This paper has been
  withdrawn by Edward Dobrowolski", v2 7 May 2017, comments "Jacob Tsimerman found an
  irreparable error in the proof". No PDF license, withdrawn.
- **arXiv:2312.08742** (Schaub–Spivakovsky, "A note on the Casas-Alvero Conjecture") —
  `research/sources/schaub_spivakovsky_2023_note_html.full.md` (source
  `https://arxiv.org/html/2312.08742v7`, v7 11 Feb 2025).

**Why the strike-through missed:** the frontier rows carry the DOI-form URL
(`doi.org/10.48550/arxiv.X`) while the held sources record the arXiv-form URL
(`arxiv.org/pdf/X`). The dedup is URL-exact, so the two forms are not recognised as the
same document. This is a cosmetic failure of the FRONTIER rendering, not a genuine gap.
**No re-download is needed and should be refused** — both files hold real content.

## Every claimed complete proof held, with status

| Claimed proof | Source | Status |
| --- | --- | --- |
| Battiston 2015 (arXiv:1511.04932) | `battiston_casas-alvero-survey_2015.full.md` | WITHDRAWN ("crucial error in last page", Schicho) |
| Dobrowolski 2017 (arXiv:1705.01704) | `dobrowolski2017_casas-alvero-true.full.md` | WITHDRAWN (Tsimerman, irreparable) |
| Massri 2018 (degree 20) | `massri2018_degree20.full.md` + html | WITHDRAWN (v2/v3/v5) |
| Ghosh 2025 (arXiv:2501.09272) | `ghosh2025_proof_html.full.md` (v2 21 Mar 2026) | **UNVERIFIED PREPRINT**, not peer-reviewed, not published |

## Ghosh status re-confirmed live (2026)

A live `read_sources` on `https://arxiv.org/abs/2501.09272` returned: "it is a preprint
and there is no indication… of formal publication in a peer-reviewed journal, nor of an
official acceptance or status change." This matches the held record. The run correctly
treats CA as **open** (the refereed sources still list d=20 smallest open).

## Bottom line
The library is complete and current on every dimension of the working assumptions
(status of every claimed proof, smallest open degree = 20, the p^k family results, the
bad-prime framework). Nothing further to fetch. CA remains open.
