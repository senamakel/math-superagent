# The shift-invariant correlation spectrum: K* as the max span of surviving monomial classes

```approach
idea: >
  Explain the cancellation that lowers K* from the naive width bound n-2 down to
  ⌈n/2⌉ by decomposing S² over the TRANSLATION orbits of the window, the
  symmetry the correlation statistics actually respect. Write
      S²(h) = Σ_A c_A ∏_{j∈A} x_j,   c_A = #{ (d,d') : M_d △ M_{d'} = A },
  with x_j = (−1)^{h_j}. The correlation vector C_K consists exactly of the
  ℤ-translation-invariant sliding sums of span ≤ K (the Fourier transform of the
  (K+1)-gram counts is the sliding autocorrelation of order ≤ K). So the
  "order" S² is sensitive to is the maximal span of a monomial class that
  SURVIVES the d,d' sum after grouping by translation orbit — and the run's
  measured K*(n) = ⌈n/2⌉ (with n=5 the exceptional value 2) should be exactly
  this maximal surviving span. The refuted naive width bound (orderk_correlation
  _capture.txt: max symmetric-difference width is n-1 at every n, yet K*=⌈n/2⌉)
  is then explained, not contradicted: the wide monomials cancel, and only
  translation classes of span ≤ ⌈n/2⌉ carry nonzero net coefficient.
  Speculative: the "surviving orbit coefficient ⇒ span ≤ K*" direction is the
  hypothesis to verify, not a theorem.

mechanism: >
  Named machinery: the ℤ translation action on the index window, class functions
  and orbit averaging (Burnside), and the sliding-autocorrelation spectrum (the
  standard Fourier-dual of gram counts). Why it suits the problem: the fold
  monomials M_d △ M_{d'} are right-anchored (M_d = {n-1-d+o : o ⊆ d}), so the
  window is not translation-invariant — and precisely this anchoring is what the
  boundary reflection x ↦ n-1-x (already used in the proved meet formula
  downset-row-intersection-meet-formula) can unwind. Grouping the distance
  distribution c_A by the translation orbit of A (after reflection to the
  downset) turns the observed "cancellation across the d,d' sum" into a
  spectral/combinatorial count on the row-code distance distribution, replacing
  the 2^n fibre search with a computation of orbit coefficients. This is NOT
  mobius-meet-factorization (which factors over the depth-bit lattice, not the
  shift symmetry) and NOT the refuted spectral-gap parseval route (which
  worked on the ℂ multiplier of the fold, not on the ±1 correlation spectrum).
status: grounded
precedent: >
  NAMED MACHINERY IS REAL AND SOURCED, but the SPECIFIC hypothesis
  "K*(n)=max span of surviving orbit coefficients, reproducing floor(n/2)"
  has NO literature precedent: it is the run's own novel decomposition, to be
  tested mechanically. Grounding the machinery is what lets the first-step
  falsifier be decisive rather than a guess.
  - Translation-orbit / class-function / Burnside orbit averaging on Boolean
    function monomials: rotation-symmetric Boolean functions literature —
    Cusick & Stănică, "Rotation Symmetric Boolean Functions — Count and
    Cryptographic Properties" (Electron. Notes Discrete Math. 2004; and their
    RSA2002 book), using Burnside orbit counting and grouping monomials by
    rotation orbit; Kawut & Yücel, "9-variable Boolean functions with
    nonlinearity 242 in the generalized rotation class" (arXiv:0808.0684) —
    orbit averaging under a permutation group, invariant functions as orbit
    class functions. These make "group monomials by a shift orbit, sum orbit
    coefficients" a recognized operation on ±1 monomial expansions.
  - Sliding autocorrelation as the Fourier dual of k-gram counts: the
    Wiener–Khintchine identity (autocorrelation = Walsh-spectrum-squared) in the
    Boolean-function/DLCT literature (e.g. "Thinking out of the box: hybrid SAT
    solving", arXiv:2506.00674, Walsh-Fourier expansion of an arbitrary Boolean
    constraint; the DLCT autocorrelation-table references at inria hal-03520200).
    This is the named basis for "the order S² is sensitive to = span of surviving
    monomial classes" — the ±1 monomial expansion of S², grouped by translation
    orbit, is exactly the object whose span the sliding autocorrelations see.
  - In-workspace: claim `downset-row-intersection-meet-formula` (the boundary
    reflection x↦n−1−x already unwinds the anchoring, mapping M_d bijectively to
    the digital downset ↓d); claim `kstar-exact-floor` (K*(n)=floor(n/2), with
    floor(5/2)=2 resolving the n=5 "exception" — this is the table the orbit
    hypothesis must reproduce, and the n=5 case is where the floor/ceil tell is).
    The candidate's stated "n=5 exception K*(5)=2" is consistent with floor(5/2)=2,
    so the decomposition should be tested against floor, not ceil.
  CAVEAT (must be priced by the run): the clean claim "surviving orbit
  coefficient of span ≤ K* and conversely the max surviving span equals K*" is
  not a sourced theorem. Whether orbit grouping is the RIGHT invariant to capture
  the cancellation (rather than some other symmetry of the M_d △ M_{d'} family)
  is exactly what the n=4..20 test decides; the mechanism is grounded, the
  specific characterization is open and novel.
first-step: >
  (tool_builder, exact ±1/integer arithmetic, no primes) For n = 4..20:
  (1) compute the full distance distribution c_A = #{ (d,d') : M_d △ M_{d'} = A }
  for the operative range d,d' ∈ [2,n-1]; (2) reflect each M_d to its digital
  downset ↓d and group the monomials by translation orbit of the symmetric
  difference; (3) for each orbit compute the surviving net coefficient and its
  span, then test the hypothesis
      K*(n) = max{ span(A) : surviving orbit coefficient ≠ 0 }
  against the measured K* = floor(n/2) table (n=4..20, including n=5 where
  K*(5)=2). FALSIFIER: a mismatch at any n, or any surviving orbit of span
  strictly larger than the measured K*, refutes the orbit characterization and
  records the exact obstruction (which class of wide monomials fails to cancel).
falsifies: >
  (a) a surviving orbit coefficient of span > measured K* (then the cancellation
  is not captured by translation orbits alone, and the exact surviving monomial
  class is the deliverable); (b) a surviving orbit coefficient of span < K* at
  some n (then the "max span" formula is incomplete and some other invariant
  governs K*); (c) the n=5 value (K*(5)=2=floor(5/2)) not emerging naturally from
  the orbit count (then the floor-vs-ceil tell is not a boundary artifact of this
  decomposition and must be explained elsewhere).
```
