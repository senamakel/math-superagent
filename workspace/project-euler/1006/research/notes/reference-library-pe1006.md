# Project Euler 1006 — local reference set

The workspace now has a substantial reference library for the problem's mathematics. The central theory is Sturmian/Fibonacci words; the computational references concern Euclidean floor-sum recursion.

## Primary mathematical sources

- `research/sources/morse-hedlund-sturmian.full.md` — Morse & Hedlund, **Symbolic dynamics II. Sturmian trajectories**. URL: https://www.jstor.org/stable/2371261
- `research/sources/berstel-vuillon-coding-rotations.full.md` — Berstel & Vuillon, **Coding rotations on intervals**. URL: https://arxiv.org/abs/math/0106217
- `research/sources/lothaire-sturmian-words-C2.full.md` — Lothaire, **Algebraic Combinatorics on Words**, Sturmian Words chapter. URL: https://www.cambridge.org/core/product/identifier/CBO9781107326019A016/type/BOOK_PART
- `research/sources/perrin-restivo-sturmian-lecture.full.md` — Perrin & Restivo lecture treatment of Sturmian words; URL is in the companion summary.
- `research/sources/berstel-sturmian-episturmian-survey-2007.full.md` — survey treatment; URL is in the companion summary.
- `research/sources/cmb-1993-descriptions-characteristic-sequence.full.md` — characteristic-sequence treatment of Fibonacci/Sturmian structure.
- `research/sources/richomme-saari-zamboni-standard-factors-sturmian.full.md` — standard factors of Sturmian words.
- `research/sources/sivasankar-rama-fibonacci-factors-2022.full.md` — Fibonacci-factor enumeration/location treatment.
- `research/sources/oeis-A213975-fibonacci-subwords-lexicographic.full.md` — catalogue/check only, not used as proof; URL is embedded in the file.

## Algorithmic sources

- `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md` — universal Euclidean/floor-sum recursion. URL: https://oi-wiki.org/math/number-theory/euclidean/
- `research/sources/chtholly-universal-euclidean-oiwiki.full.md` — related universal-Euclidean exposition.
- `research/sources/universal-euclidean-geometric-weight-fhq.full.md` — geometric-weight floor-sum treatment.
- `research/sources/atcoder-internal-math-hpp.full.md` and related AtCoder files — standard `floor_sum`; URL: https://atcoder.github.io/ac-library/production/document_en/math.html
- `research/sources/patricio-hartwig-euclid-corner-sums.full.md` — Euclidean recursion for related weighted floor/corner sums.

Complete downloaded texts are under `research/sources/`; bounded summaries are under `research/summaries/`. The source URLs are retained in the source files or companion summaries.