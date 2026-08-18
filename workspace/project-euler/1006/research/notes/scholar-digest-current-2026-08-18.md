# Scholar digest — current reference-library refresh (2026-08-18)

## Sources that help

### Babichev & Babichev, *Counting all lattice rectangles in the square grid in near-linear time*
Source: https://arxiv.org/html/2604.22456v2; full text: [[lattice-rectangles-weighted-floor-sum-html.full]]

The paper proves that a finite constant-size family of polynomially weighted floor moments is closed under affine normalization and reciprocal (Euclidean staircase) transformations; its Corollary 6 gives O(log) recursion depth. This is an independent theorem-level anchor for the structural floor-moment approach used by PE1006. It does **not** state the geometric-weight monoid with weights 10^{-i}, nor anything about Fibonacci words or Ψ, so the exact geometric implementation remains supported by OI-Wiki/fhq/LOJ138 and executable tests.

### Binner, *Reciprocity Relations for Summations of Squares of Floor Functions and Fractional Parts of Fractions*
Source: https://arxiv.org/abs/2107.08308; full text: [[binner-reciprocity-fulltext]]

For positive coprime parameters it gives Euclidean reciprocity for fractional-part squares, weighted first floor moments, and floor squares; the floor-square quantity has O((log t)^2) evaluation. This independently supports the second-moment Euclidean basis. Scope is limited: no geometric index weights, no general affine/non-coprime case, and no Ψ reduction. `remember_memory` was attempted but the memory server timed out; retry when healthy.

### Perrin–Restivo / Perrin mechanical-word sources
Sources: [[perrin-sturmian-words-lecture2-mechanical.full]], [[perrin-restivo-note-sturmian-2011]]

They establish the lower mechanical representation `s(n)=floor((n+1)alpha+rho)-floor(n alpha+rho)`, intercept-independent factor language, and the Sturmian characterization/complexity theorem. For PE1006 the slope is alpha=1/phi^2=(3-sqrt(5))/2, hence exactly k+1 length-k factors. This confirms the object model and the arc-midpoint mechanical construction, but does not evaluate Ψ.

### Sivasankar–Rama
Source: https://arxiv.org/html/2207.04304; full text: [[sivasankar-rama-fibonacci-factors-2022.full]]

It gives enumeration/location methods for Fibonacci-word factors and explicit first-occurrence structure, useful as an independent finite contiguous-window oracle. The digest does not itself establish the exact one-dimensional window identity currently used by the run, and it says nothing about decimal second moments.

### AtCoder / OI-Wiki / fhq / LOJ138
Sources: [[atcoder-floor-sum-editorial]], [[atcoder-internal-math-hpp]], [[oiwiki-universal-euclidean-floor-sum-2026.full]], [[universal-euclidean-geometric-weight-fhq.full]], [[loj138-universal-euclidean-floor-moments.full]]

AtCoder gives the ordinary floor_sum Euclidean reciprocity in O(log). OI-Wiki/fhq give the operation-string merge/flip recursion and geometric-weight monoid; LOJ138 gives binomial moment-array closure. Together they support the exact executable primitive (count, geometric sum, first and second floor moments), conditional on the run's indexing and reduction being checked against brute/mechanical values. These are algorithmic notes, not peer-reviewed proofs.

## Sources that do not help the current computation

- Allouche–Shallit and Lothaire DOI landing pages: broad background only; no usable new theorem beyond the already-held Sturmian/automatic facts.
- de Luca DOI landing response (114 bytes): no mathematical content; provenance only.
- Automatic-sequence decision-procedure material and Cobham/numeration sources: relevant to a rejected Zeckendorf-automatic route, not to the committed mechanical/floor-sum evaluator.
- OEIS and Wikipedia records: catalogue/encyclopedic corroboration, useful for sanity checks but not an independent proof of the target residue.
- Babichev–Shpakova weighted lattice-rectangle paper (arXiv:2607.17961): concerns a different O(n log n) rectangle-count algorithm; its weighted-floor discussion is not the exact PE geometric monoid and does not remove the evaluator-wiring obligation.

## Contradictions / status changes

No new source contradicts the durable beliefs. The main scope warning is consistent across sources: polynomial-weight floor-moment closure is not the same as the required geometric-weight closure. The literature still does not independently certify the complete PE reduction or any target residue. Corrected anchors remain asserted until reproduced in-container.

Memory persistence was partially unavailable: `remember_memory` successfully stored the Babichev theorem-level finding, but attempts for Binner and Sivasankar–Rama timed out. Retry those two durable memories once Cognee health recovers.
