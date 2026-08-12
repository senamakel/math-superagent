# Approach: arrangement characteristic polynomial / parity-weighted volume

```approach
idea: Sum parity-weighted cell volumes via the arrangement's characteristic polynomial
mechanism: >
  p(n,L) = (n-1)! * Vol(even-parity region in simplex). Equivalently,
  (2p-1) * Vol(simplex) = sum_{cells} (-1)^{parity(cell)} * Vol(cell).
  The hyperplane arrangement A_n(L) has the property that crossing a hyperplane
  either swaps the final order of two boats (flipping parity) or changes only
  the bump chronology without affecting the final order. If the parity sign
  factorises as a product of signs assigned to each hyperplane, then the sum
  ∑ (-1)^{parity} Vol(cell) is the integral over the simplex of a sign product
  of affine-linear forms. This is exactly the kind of sum that the characteristic
  polynomial χ_A(t) governs: by Zaslavsky/Orlik–Solomon theory, signed sums of
  region volumes relate to χ_A evaluated at specific arguments. The arrangement
  has O(n^2) hyperplanes, so χ_A is a polynomial of degree n-1 computable
  without enumerating the O(exp(n^2)) cells — through the matroid / intersection
  lattice, for instance. If parity is a cohomology class on the arrangement
  complement, the signed-volume sum is a characteristic-polynomial evaluation.
status: refuted
killed-by: >
  The characteristic polynomial χ_A of the arrangement is a purely combinatorial,
  L-INDEPENDENT object (it depends only on the intersection lattice of the
  hyperplanes), whereas p(n,L) genuinely depends on L — verified exactly by the
  run: p(4,400)=521/1020 ≠ p(4,1800)=166802/317985, and similarly p(3,160)=56/135
  ≠ p(3,400)=542/1377. A parity-weighted volume sum that equals a pure
  characteristic-polynomial evaluation could not depend on L, so the specific
  claim "the sum is a characteristic-polynomial evaluation, computable without
  enumerating cells" cannot hold for the L-dependent volumes of THIS problem.
  For the charpoly theorems to apply the region weight must be of a specific
  class (conic intrinsic volumes / projection dimension / projection volume —
  Klivans–Swartz, Kabluchko, Goregaokar), and torpids parity is not such a
  statistic; a (±1)-weighted signed region-volume sum is outside what the
  characteristic-polynomial results cover. The library's own smoothing claims
  are all marked holds-here: unchecked, and exactly this gap is why.
note: >
  The route-PRINCIPLE is genuinely in the literature and is worth naming so it is
  not re-claimed later as novel: aggregate data over regions of a real hyperplane
  arrangement (projection volumes, projection-dimension profile, conic intrinsic
  volumes) are characteristic-polynomial / Whitney-number statistics and are
  computable WITHOUT enumerating regions, via the intersection lattice. That is
  the correct framing for "signed region aggregates are charpoly statistics".
  It collapses here only because (a) the weight (parity) is not of the covered
  class, and (b) the target is L-dependent while χ_A is L-independent. Running
  the run's own first-step (does parity factorise as a product of hyperplane
  signs at n=3?) is still a useful cheap diagnostic, and reporting a NON-
  factorization would close the idea completely; but even a positive answer
  could not yield p(n,L) because the volume weights carry the L-dependence.
precedent: >
  Route-principle (aggregate region data = charpoly/Whitney statistics, no
  enumeration) — all library claims, all holds-here UNCHECKED:
  - claim `arrangement-projection-volume-charpoly` (Klivans & Swartz 2011,
    arXiv:1001.5095, Discrete Comput. Geom. 46(3):417-426)
  - claim `affine-chamber-projection-profile-charpoly` (Kabluchko, arXiv:2008.06719)
  - claim `charpoly-signed-region-generating-function` (Goregaokar, arXiv:2506.00941)
  - claim `characteristic-element-charpoly-linear-functional` (Aguiar, Bastidas &
    Mahajan, arXiv:1902.07325)
  - Zaslavsky region-count: χ_A(-1)=#regions (inria.hal.science/hal-01185160;
    Springer link.springer.com/article/10.1007/s00454-023-00557-2)
  Kill: run's exact L-dependent values (code/out/exact_small_n_results.json) and
  CONTEXT.md table.
```
