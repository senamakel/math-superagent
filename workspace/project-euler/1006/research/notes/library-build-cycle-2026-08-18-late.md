# Reference-library cycle (late 2026-08-18)

The PE1006 library was audited before searching. It already contains broad primary/standard coverage of Fibonacci and Sturmian words, mechanical rotations, factor-location theorems, universal Euclidean/floor-sum monoids, AtCoder `floor_sum`, and adjacent automatic/numeration theory.

## Search and additions

Searches used `exa_search` for (i) Fibonacci-word Sturmian factor complexity and mechanical words, (ii) universal Euclidean weighted floor sums, (iii) the official Project Euler statement, and (iv) factor-location/contiguous-window theorems. Citation graphs were also run on the Mignosi factor-complexity lead and the automatic-sequences survey lead.

Already present, so not downloaded again: Sivasankar–Rama factor-location source and Mignosi's factor-complexity citation record. New source records successfully downloaded from searched DOI URLs:

- `research/sources/allouche-shallit-automatic-sequences-book.full.md` (DOI https://doi.org/10.1017/cbo9780511546563); useful canonical background on automatic sequences and Fibonacci numeration, but the DOI endpoint is largely a publisher landing page.
- `research/sources/lothaire-combinatorics-words.full.md` (DOI https://doi.org/10.1017/cbo9780511566097); standard combinatorics-on-words reference, likewise primarily a publisher landing page.
- `research/sources/deluca-sturmian-structure-arithmetics-1997.full.md` (DOI https://doi.org/10.1016/S0304-3975(96)00310-6); only a 114-byte landing response was available, retained as provenance but not treated as evidence.

The source files are accompanied by generated summaries where available. `research/summaries/library-build-status.md` and `research/notes/reference-library-report.md` describe the existing canonical tier and the open requests. Cognee indexing was unavailable during this cycle; this note preserves the durable audit locally until memory recovers.

## Conclusion

No further source gap was found: the local library already anchors the governing Sturmian factor-complexity theorem and the universal-Euclidean reduction. The next productive work is solver execution/verification, not another literature search.