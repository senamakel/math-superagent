# Reference-library build report (2026-08-18)

## New/confirmed source coverage

- **Canonical Fibonacci/Sturmian background:** `research/sources/cassaigne-extremal-fibonacci-word-numdam.full.md` (Numdam PDF, DOI 10.1051/ita:2008003), with digest `research/summaries/cassaigne-extremal-fibonacci-word-numdam.md`. It identifies the Fibonacci word as the fixed point of ϕ(a)=ab, ϕ(b)=a and the archetypal Sturmian word, and surveys recurrence and factor structure.
- **Independent extremal Sturmian treatment:** `research/sources/de-luca-sturmian-extremal-preprint.full.md`, digest alongside it. Useful for standard/characteristic Sturmian terminology and morphic descriptions.
- **Adjacent factor/repetition theory:** `research/sources/abelian-repetitions-sturmian.full.md`, from arXiv 1209.6013 via ar5iv. It supplies an independent interval/factor viewpoint and Fibonacci-specific structural results.
- **Factor location and recurrence:** `research/sources/fibonacci-factor-location-search-result.full.md`, downloaded from the searched HAL result `hal-01829175v1/document`, with digest. This broadens coverage of factor complexity, special factors, and location methods.

## Search/citation work

Searched broadly for Fibonacci-word factor complexity, Sturmian mechanical representations, factor-location theorems, and weighted Euclidean floor moments. Ran citation graphs on Cassaigne (DOI 10.1051/ita:2008003), Sivasankar–Rama (arXiv 2207.04304), and the standard Sturmian survey DOI 10.1016/S0304-3975(96)00310-6; their leads are in `derived/FRONTIER.md`. Similar-source search around Cassaigne surfaced Numdam and related Sturmian papers.

## Retrieval limitations

The exact ScienceDirect factor-location article returned HTTP 403; a searched HAL source covering the same factor-location/complexity angle was obtained instead. The DOI landing page for 10.1016/S0304-3975(96)00310-6 produced only an unusable 114-byte response; the library already contains Perrin–Restivo, Lothaire, and Deluca treatments of the needed Sturmian facts. No Project Euler solution or published contest answer was searched or downloaded.

## Existing relevant shelf

The workspace already holds authoritative or near-primary sources for: Sturmian complexity and mechanical words; Fibonacci-word surveys; factor enumeration/location; three-distance/rotation structure; universal Euclidean weighted floor sums; Ostrowski/Zeckendorf numeration; and automatic-sequence limitations. The governing-theory note is `research/notes/pe1006-governing-theory.md`, and durable recall was updated after this build.