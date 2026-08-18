# Source digest against PE1006 (2026-08-18)

## Babichev & Babichev, *Counting all lattice rectangles...*
URL: https://arxiv.org/html/2604.22456v2
[[lattice-rectangles-weighted-floor-sum-html.full]]

The paper proves affine normalization and reciprocal Euclidean closure for a constant-size family of polynomially weighted floor moments H_{p,q}=Σ t^p floor((at+b)/m)^q; Corollary 6 gives O(log m) recursion depth. This is an independent theorem-level anchor for finite-state Euclidean floor-moment evaluation. It does not state geometric index weights, Fibonacci words, Ψ, or the PE reduction. Therefore it supports the complexity principle only; the geometric monoid and its PE wiring remain separate claims requiring implementation tests.

## Binner, *Reciprocity Relations for Summations of Squares...*
URL: https://arxiv.org/abs/2107.08308

The library inventory records Euclidean reciprocity for fractional-part squares, weighted first floor moments, and floor squares (O((log t)^2) for the square quantity) under positive coprime parameters. It does not cover geometric index weights, general affine/non-coprime details, or Ψ. It is corroboration for second-moment Euclidean methods, not a solution. The expected summary filename was absent; no unsupported detail is inferred beyond the inventory/digest.

## Perrin–Restivo and related mechanical-word sources
URLs/source files: research/sources/perrin-restivo-sturmian-lecture.full.md; research/sources/perrin-sturmian-words-lecture2-mechanical.full.md

They establish the lower mechanical representation s(n)=floor((n+1)α+ρ)-floor(nα+ρ), rotation/intercept coding, intercept-independent factor language, and Sturmian complexity k+1. For PE1006 α=1/φ²=(3−√5)/2. This validates the object model and arc-midpoint factor parametrisation, but not Ψ's numerical evaluation.

## Chuan, *Fibonacci Words*
URL: https://www.fq.math.ca/Scanned/30-1/chuan.pdf
[[chuan-fibonacci-words-fq1992.full]]

Theorem 6/7: finite Fibonacci words generated with arbitrary concatenation labels are cyclic shifts of the standard word; Lemma 9 gives complete Fibonacci residue systems. This supports finite rotation/cyclic-shift structure and Fibonacci-block renormalisation. It does not establish the exact PE window range, Ψ, or decimal modular sums. It is consistent with current memory, not a contradiction.

## Sivasankar–Rama, *Fibonacci Sequences of 1D, 2D Words...*
URL: https://arxiv.org/html/2207.04304
[[sivasankar-rama-fibonacci-factors-2022.full]]

The paper gives factor enumeration/location methods, including explicit finite Fibonacci-window structure in its 1D results. It is useful as an independent small/finite factor oracle, but the digest does not establish the exact one-dimensional window identity used in this run and says nothing about decimal second moments. No contradiction found.

## fhq universal Euclidean geometric-weight algorithm
URL: https://www.cnblogs.com/dixiao/p/15719155.html
[[universal-euclidean-geometric-weight-fhq.full]]

It gives exact merge and reciprocal-flip recurrences for operation strings encoding floor sequences, with a constant-size monoid carrying geometric-weighted first/second moments and O(log max(p,q)) Euclidean steps. This is the closest source to the needed evaluator. It still does not prove the Fibonacci/mechanical reduction or jointly collapse all intercept boundary terms; the latter remains the current blocker.

## LOJ138 universal Euclidean moments
URL: https://www.cnblogs.com/AThousandMoons/p/13129167.html
[[loj138-universal-euclidean-floor-moments.full]]

It generalises the monoid to moment arrays using binomial concatenation, computing fixed-degree floor/index moments in O(log max(p,q)). It independently corroborates finite moment closure and is useful as a second implementation oracle, but does not address Fibonacci factors or Ψ.

## Non-helpful sources
Automatic-sequence/Presburger and Cobham material gives decidability or base-dependence results, not a feasible decimal Ψ evaluator; OEIS/Wikipedia are catalogues/background, not proof of the target; broad Sturmian surveys and citation metadata add no new reduction; AtCoder gives only ordinary unweighted floor_sum. No source found in this refresh supplies the missing joint Fibonacci-block/intercept-boundary collapse or any honest Ψ(10^18) residue.

## Contradictions
No new source contradicts durable beliefs. The only convention warning remains important: α=1/φ² is PE1006's word; α=1/φ models the complemented rabbit convention and fails the k=3 factor oracle. Cognee was unavailable, so the finding is recorded here for later durable-memory retry.