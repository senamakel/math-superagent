# Librarian report — 2026-08-18

## Acquisition status

The reference library is already substantial: it contains the Matschke surveys, Stromquist abstract, Rius Casado thesis PDF, Fung 2021 full text, Greene–Lobb papers, Asano–Ike papers, Pettersson–Tverberg–Östergård, and many adjacent works. This cycle checked the two stale gaps in `CONTEXT.md` and the canonical reference tier.

### Verified available locally

1. **Fung, Every Jordan curve inscribes uncountably many rhombi**
   - Full text: `research/sources/fung-2021-uncountably-many-rhombi.full.md`.
   - Primary identifiers: arXiv:2010.05101; DOI `10.1007/s10711-021-00659-2`.
   - Theorem: every Jordan curve, with no regularity assumptions, inscribes uncountably many rhombi; an open interval of angles always occurs, and all angles occur when there is no special corner.
   - Scope warning: this is not a square theorem. A rhombus has perpendicular diagonals, but the square additionally requires equal diagonal lengths.

2. **Rius Casado, The Square Peg Problem (University of Barcelona thesis, 2019)**
   - Full text: `research/sources/rius-casado-2019-square-peg-problem-thesis.full.md`.
   - Repository: `https://hdl.handle.net/2445/151918`.
   - The full PDF is genuinely on disk. It gives a detailed simplex/mod-2 degree exposition of Stromquist’s proof and distinguishes the stronger Condition A from the correct local-monotonicity hypothesis. The earlier context note saying this was only a landing page is stale and should be corrected.

3. **MathWorld, Square Inscribing**
   - Stored converted page: `research/summaries/mathworld-square-inscribing-reference.md`.
   - URL: `https://mathworld.wolfram.com/SquareInscribing.html`.
   - Reference-tier status only: it confirms the general problem remains open, convex and smooth special cases, and the distinction between inscribed and circumscribed squares. It is not primary evidence for the theorems.

4. **Wikipedia, Inscribed square problem**
   - Existing local source and summary: `research/sources/wikipedia-inscribed-square-problem.full.md` and `research/summaries/wikipedia-inscribed-square-problem.md`.
   - Reference-tier status only; do not use it in place of papers.

## Search and triage record

- Search queries covered Fung/rhombi, the Rius thesis and direct PDF, canonical encyclopedic pages, and current square-peg status.
- `read_sources` triaged the seen DOI/PDF/reference URLs before fetching.
- Attempts to download Fung, Rius, and Wikipedia by their already-known URLs were correctly refused as duplicates; the files/summaries already exist locally.
- The Matschke 2022 DOI currently exists locally as a citation-graph abstract (`research/summaries/citations_w4214890841.md`) but not as a verified full-text source. Its abstract is a lead, not evidence.
- `citation_graph` for Matschke 2022 was rate-limited (HTTP 429), so no claim was based on that failed request.

## Evidence and memory caveat

The memory server was unavailable during this cycle, so `remember_memory` calls failed. The verified findings are therefore recorded here and in the existing source summaries; they should be re-submitted to durable memory when the service recovers.

## Remaining concrete gaps

- Obtain a true full text of Matschke 2022 if the DOI landing page or a seen repository PDF becomes available; until then use only the 2014 survey and primary papers for theorem claims.
- If the team wants more adjacent coverage, acquire the seen Wright 2025 rhombi paper and Wright 2026 companion, but they are not needed to establish the current minimal library requirement.
- Update `CONTEXT.md` to remove the stale Rius and Fung acquisition-gap statements and to mark the rhombi theorem as sourced/published.
