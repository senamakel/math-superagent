# Reference-library build cycle (2026-08-18)

## Search-first record

Searched Exa across four independent angles: (i) Fibonacci/Sturmian factor complexity and mechanical words; (ii) explicit Fibonacci-factor location; (iii) weighted/universal Euclidean floor sums; (iv) canonical Fibonacci-word references. Results identified Perrin–Restivo, Perrin's mechanical-word lecture, Sivasankar–Rama, Fici, and OI/AtCoder-style Euclidean sources. Citation graphs were queried for Sivasankar–Rama and Fici; Perrin–Restivo's DOI graph lookup failed because a URL was supplied instead of a DOI, so no claim is based on that failed call.

## Sources available locally

The relevant full texts and summaries already exist under `research/sources/` and `research/summaries/`, notably:

- `perrin-sturmian-words-lecture2-mechanical.full.md` and summary: mechanical-word floor differences, rotation coding, factor intervals, Morse–Hedlund equivalence, and Fibonacci slope \(\alpha=1/\varphi^2\).
- `perrin-restivo-note-sturmian-2011` summary/citation record: Sturmian factor generation and exactly \(n+1\) factors.
- `sivasankar-rama-fibonacci-factors-2022.full.md`: explicit first-occurrence/location structure for Fibonacci factors.
- `fici-factorizations-fibonacci-infinite-word-ar5iv.full.md`: Fibonacci factorizations and finite-word/Ostrowski structure.
- `oi-wiki-universal-euclidean-floor-sum.full.md`, `universal-euclidean-geometric-weight-fhq.full.md`, `loj138-universal-euclidean-floor-moments.full.md`, and AtCoder floor-sum sources: Euclidean recursion and moment monoids.
- `wikipedia-fibonacci-word.full.md`, `wikipedia-sturmian-word.full.md`, and `oeis-A003849-fibonacci-word.full.md`: canonical encyclopedic/catalogue tier.

No source was downloaded from an unsearched or invented URL. Download attempts for already-held DOI/PDF records were correctly refused as duplicates.

## Verified mathematical findings

Perrin's source states that lower mechanical words are
\[
s_{\alpha,\rho}(n)=\lfloor(n+1)\alpha+\rho\rfloor-\lfloor n\alpha+\rho\rfloor,
\]
and that factors correspond to nonempty rotation intervals; the factor language is independent of intercept. Morse–Hedlund gives equivalence between Sturmian, balanced aperiodic, and irrational mechanical words. The PE1006 Fibonacci word is the characteristic mechanical word of slope \(1/\varphi^2=(3-\sqrt5)/2\). Thus its factor complexity is exactly \(k+1\), and the arc-midpoint representatives used by the solver are structurally justified.

The local universal-Euclidean sources establish the relevant algorithmic theory: Euclidean reciprocity recursively evaluates floor sums, while a composable monoid/moment tuple carries geometric weights and first/second floor moments in logarithmic recursion depth. This is an algorithmic analogue/reference for the executable primitive; the exact PE1006 reduction remains a run-local derivation and must be checked against the brute oracle.

## Coverage assessment

The library is broad on the governing theory, explicit Fibonacci factor location, canonical references, and weighted floor sums. No additional source gap was found in this cycle. The remaining risk is not bibliography but executable reduction/indexing: the universal-Euclidean evaluator must reproduce the in-container brute/mechanical checks and the corrected anchors before the full-size result is trusted.
