# Reference-library refresh: PE1006, cycle 3

## Search coverage
Searched broadly for (a) exact Fibonacci-factor window/location theorems, (b) characteristic-word/Zeckendorf location algorithms, (c) weighted floor-moment Euclidean methods, and (d) Fibonacci numeration automata. Citation graphs were walked for Chuan–Ho's location paper and Mignosi's Sturmian-factor paper; deep research and source triage were used before downloads.

## New material successfully filed
- `research/sources/li-wu-fibonacci-n-factor-complexity-2022.full.md`, source URL http://arxiv.org/pdf/2212.10069. Digest: `research/summaries/li-wu-fibonacci-n-factor-complexity-2022.md`. This is adjacent factor-complexity work, not a direct decimal-moment method.
- `research/sources/shallit-shan-fibonacci-representations-2023.full.md`, source URL https://arxiv.org/pdf/2309.02765. Digest: `research/summaries/shallit-shan-fibonacci-representations-2023.md`. It gives automata-theoretic completeness/uniqueness results and an O(log n) representation-finding theorem, useful vocabulary but not the PE sum itself.

## Important source leads / limitations
- Sivasankar–Rama arXiv 2207.04304 is already held and explicitly states the k+1 conjugate-prefix window theorem for F(n) <= k < F(n+1).
- Chuan–Ho's 2010 location paper is the primary direct treatment, but ScienceDirect returned 403. The citation graph identifies DOI 10.1016/j.tcs.2010.04.013 and the follow-up generalized-Zeckendorf paper DOI 10.1016/j.tcs.2012.04.015; neither was downloaded this cycle because the accessible landing-page URL was blocked and no verified alternate full-text URL was available.
- Babichev–Babichev arXiv 2604.22456 was already represented in local citation material; its Corollary 12 is a useful modern example of a constant-size weighted-floor kernel closed under Euclidean affine/reciprocal transformations, but it does not prove the PE reduction.

## Durable conclusion
The library now covers the canonical Sturmian theory, explicit Fibonacci factor windows/locations, Fibonacci numeration automata, and modern weighted-floor Euclidean kernels. It still does not contain a published theorem that directly collapses PE1006's decimal square sum to an O(log k) fixed-state computation; the exact PE reduction remains a local derivation requiring independent verification.