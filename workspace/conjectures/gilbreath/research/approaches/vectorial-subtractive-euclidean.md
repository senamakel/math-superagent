```approach
idea: vectorial-subtractive-euclidean
mechanism: |
  The pair operation (a,b) -> |a-b| is exactly ONE STEP of the subtractive
  Euclidean algorithm (gcd(a,b) = gcd(|a-b|, min(a,b))). The Gilbreath triangle
  is the same operation applied SIMULTANEOUSLY to all adjacent pairs of a row,
  so the left column A_k(1) is the outcome of a *vectorial subtractive
  Euclidean process* driven by the initial row (1, g_1, g_2, ...) of halved
  prime gaps.

  This is a change of representation: instead of tracking the {0,2} block and
  its boundary, view the whole triangle as a multi-dimensional continued
  fraction / vectorial Euclidean algorithm. The classical named theory is the
  family of SIMULTANEOUS generalisations of Euclid's algorithm used in
  Diophantine approximation:

    - the Jacobi–Perron algorithm,
    - the Brun algorithm and the fully subtractive algorithm,
    - the Selmer algorithm.

  These algorithms come with a battery of proved results the run has never
  invoked: existence of invariant measures, convergence of the "Brun map",
  Lyapunov spectra of the associated matrix products, and a first-return /
  acceleration structure telling you how often the "digit" is visited. The
  conjecture A_k(1) in {0,2} is, in this language, an accelerated-digit
  recurrence-rate question for a specific vectorial subtractive scheme.

  Named mathematics: subtractive Euclidean algorithm, Jacobi–Perron, Brun,
  Selmer and fully-subtractive algorithms, simultaneous Diophantine
  approximation, ergodic theory of multidim. continued fractions.

  Speculative: the exact adjacency-absolute-value scheme does not match any one
  classical algorithm term-for-term, and the absolute value may or may not
  have a known invariant measure. Establishing the dictionary is the whole
  first step.
status: refuted
disposition: (b) parked — refuted, not a route to G-supply; no classical subtractive scheme matches (no renormalisation/simplex, overlapping windows) (Directive 44 item 2).
killed-by: |
  Research (this cycle) established that NO classical simultaneous-Diophantine
  scheme matches the Gilbreath map, and that the match is structurally
  impossible. The load-bearing premise — that the row map is a
  "vectorial subtractive Euclidean algorithm" in the sense of
  Jacobi–Perron/Brun/Selmer/fully-subtractive — is false on three independent
  grounds:

  (1) The classical algorithms are NORMALISED, PERMUTED, RENORMALISED maps on a
      bounded simplex (coordinates 0 =< x1 =< ... =< xn, subtract the largest
      from smaller / divide by the largest, reorder), precisely so that an
      invariant measure and an absorbing simplex exist (Miernowski–Nogueira,
      "Absorbing sets of homogeneous subtractive algorithms", arXiv:1104.3762;
      Schweiger, "Ergodic and Diophantine properties of algorithms of Selmer
      type", Acta Arith. 114 (2004); Mercat, "Computation of invariant
      densities for continued fraction algorithms", arXiv:2311.10046). The
      Gilbreath row map h_{k+1}(i)=|h_k(i)-h_k(i+1)| has NO renormalisation,
      NO permutation, NO normalisation to a bounded simplex, and acts on
      OVERLAPPING windows (each entry is shared by two differences), which no
      classical subtractive scheme does. Every theorem those algorithms carry
      (invariant measure on the simplex, convergence, absorbing set) is a
      theorem about a renormalised system; there is no such system here.

  (2) No paper applies, or even relates, the iterated-absolute-difference
      (Ducci/Gilbreath) map to any simultaneous-Diophantine algorithm. The
      searches surface the rich JP/Brun/FS ergodic literature on the one hand
      and the large Ducci-periodicity literature (Cyclic Ducci: eventually
      periodic, nilpotent-to-zero for power-of-two lengths; e.g.
      Breuer 2010, Lewis–Tefft arXiv:2410.18204, Calkin–Stevens–Thomas 2005)
      on the other, and NOTHING connects them. The Ducci literature is exactly
      the right test of the "return to small set" idea, and its central
      structural result is the opposite of what this approach needs: the
      CYCLIC Ducci map is eventually periodic (returns to a finite cycle or to
      the zero vector), whereas the HALF-INFINITE Gilbreath map is exactly the
      object where Eppstein 2011 (anti-gilbreath-construction, held claim)
      builds sequences whose right edge escapes to >=4 and re-enters 1
      infinitely often. So the return-time question this approach wants to hand
      the ergodic theory is precisely the open regeneration rate, and the
      ergodic machinery transfers to neither the periodic Ducci (returns to
      zero) nor the Gilbreath half-line (escapes).

  (3) Even a successful dictionary would be a re-description, not a resolution:
      an accelerated-return/return-time statement in a scheme whose return
      rate is unproved is the recharge/renewal question in new variables —
      the same structure as the refuted zero-sum-flow-conservation-mincut
      (held claim), whose "key lemma" (pump mass bounded below) is exactly the
      open regeneration rate. There is no digit/quotient structure here that
      would give a non-tautological bound.

  The candidate itself forecast this outcome ("if no such scheme exists in the
  literature the approach collapses to a re-description"). Research checked:
  no such scheme exists, and on the structural evidence (no
  renormalisation/simplex/permutation, overlapping-window action, no
  number-conserving or digit structure) the dictionary is not merely missing
  but false. Refuted on evidence, not absence.
precedent: |
  - https://arxiv.org/abs/1104.3762 (Miernowski–Nogueira 2011: absorbing sets
    of homogeneous subtractive algorithms; the ergodic structure this approach
    would need, shown to be a normalised-simplex object)
  - https://doi.org/10.4064/aa114-2-1 (Schweiger 2004: Selmer/fully subtractive
    ergodic + Diophantine properties — again a simplex/normalisation object)
  - https://doi.org/10.48550/arxiv.2311.10046 (Mercat 2023: invariant densities
    for JP/Brun/fully-subtractive via matrices-graph; domains are simplices /
    Rauzy gasket, none matches the row map)
  - https://doi.org/10.48550/arxiv.2410.18204 (Lewis–Tefft 2024, and Breuer
    2010, Calkin–Stevens–Thomas 2005: the Ducci-periodicity literature — the
    actual return-to-small-set theory for the absolute-difference map, and it
    is cyclic and eventually-periodic, not a Gilbreath half-line hit)
  - held claim: anti-gilbreath-construction (Eppstein 2011) — half-infinite
    escapes refute any return-rate transfer
  - held claim: zero-sum-flow-conservation-mincut-refuted — the re-description
    pattern this approach would repeat
first-step: |
  Closed by research: the dictionary does not exist and cannot exist (no
  renormalisation/simplex structure, no digit/quotient, overlapping windows).
  Do not re-propose the Euclidean/continued-fraction frame.
```

```claim
id: vectorial-euclidean-dictionary-refuted
statement: The Gilbreath half-infinite row map h_{k+1}(i) = |h_k(i)-h_k(i+1)| is not an instance, an acceleration, or a specialisation of any classical vectorial subtractive Euclidean / simultaneous-Diophantine algorithm (Brun, Selmer, Jacobi-Perron, fully subtractive). These algorithms are normalised maps on a bounded simplex (subtract a coordinate, reorder, renormalise) acting on non-overlapping coordinates, giving invariant measures on the simplex; the Gilbreath map has no renormalisation, no permutation, no bounded domain, and acts on overlapping windows. No source applies or relates the Ducci/Gilbreath absolute-difference map to any simultaneous-Diophantine scheme, and the natural comparison, cyclic Ducci, is eventually periodic (returns to zero/cycles) — the opposite of the half-infinite escape that Eppstein's construction exhibits.
hypotheses: the specific claim that the Gilbreath operator is a vectorial Euclidean algorithm in the JP/Brun/Selmer/FS family.
holds-here: yes
status: checked
bearing: Refutes the vectorial-subtractive-euclidean approach at its load-bearing dictionary step. The ergodic-return-rate machinery of multidimensional continued fractions does not apply, and the return-time question it would pose is the open regeneration rate restated.
anchor: research/approaches/vectorial-subtractive-euclidean.md
```
