# Reference-library findings for PE1006

The source-by-source digest is in `research/summaries/library-digest-pe1006-2026-08-18.md`.

## Durable findings requested

The memory service was unavailable during this cycle, so the following verified findings are recorded locally and should be submitted to durable memory when it recovers:

1. Lothaire's Sturmian chapter (DOI https://doi.org/10.1017/CBO9781107326019.003) states the defining complexity `p(n)=n+1` and the equivalence of Sturmian words with balanced aperiodic and irrational mechanical words. The Fibonacci morphism fixed point is Sturmian. This proves the structural count `|F_k|=k+1` and licenses mechanical coding, but not the weighted sum required here.
2. Perrin's mechanical-word lecture gives `s_{alpha,rho}(n)=floor(alpha(n+1)+rho)-floor(alpha n+rho)`, the rotation interval coding, equality of factor sets for common irrational slope, and identifies the Fibonacci word as characteristic of slope `1/phi^2`. It supplies the exact floor representation but no all-intercept weighted aggregation.
3. Berstel–Vuillon, https://ar5iv.labs.arxiv.org/html/math/0106217, give a finite-state interval-coding recoding and transition rule for rotation codings. This supports rotation automata but does not prove the PE1006 decimal second-moment collapse.
4. Sivasankar–Rama, https://arxiv.org/abs/2207.04304, give block-based enumeration and affine occurrence-location formulas for 1D Fibonacci factors, including boundary cases. This is useful for bounded checks and boundary analysis, not a full-size weighted distinct-factor sum.
5. The universal Euclidean algorithm source `research/sources/oi-wiki-universal-euclidean-floor-sum.full.md` gives Euclidean recursion plus binary exponentiation for monoid-valued affine floor paths, with logarithmic coefficient complexity, and explicitly describes monoids for first/second floor moments. It handles an individual path or fixed-dimensional moments, not the k+1-cell joint aggregation required by PE1006.

## Contradictions flagged

The recalled general pair-correlation identity is contradicted by executed evidence: it fails at k=3, j=j'=1, and the proposed collapse produces 20402 instead of 20302. The identity must not be used outside its restricted Fibonacci-length domain. The proposed scalar Fibonacci-block summary is refuted by the `01`/`10` append-0 counterexample in `code/out/current_attempt_report.md`.

## Sources not useful for this objective

Peltomäki's repetition/continued-fraction paper is mathematically relevant to Sturmian words but gives no weighted decimal factor-moment formula. Automatic-sequence decision-procedure sources do not apply to this non-automatic Fibonacci/decimal weighted computation. Least-period, Christoffel-conjugacy, catalogue/OEIS, and 2D Fibonacci-array material provide context or unrelated structure, not the missing aggregation theorem. No Project Euler solution, answer, forum, or commentary was searched.
