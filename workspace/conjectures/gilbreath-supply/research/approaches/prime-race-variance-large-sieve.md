# The second moment of S(n) is the variance of the mod-4 prime race — an index-domain large-sieve engine

```approach
idea: >
  Treat S(n) = Σ_d (−1)^{T(n,d)} as a digital U-statistic of the prime-race
  sequence s_j = χ(q_j) = (−1/q_j), and bound its second moment Σ_{n≤N} S(n)² —
  exactly the averaged SUPPLY target (ν₂/n → 1/2 on a density-1 set) — by the
  VARIANCE of the prime race W(J) = Σ_{j≤J} s_j over dyadic subintervals. The
  engine is the orthogonal (Hájek/Hoeffding) decomposition of the U-statistic
  plus large-sieve / Barban–Davenport–Halberstam control of the race's mean
  square, in the INDEX domain rather than the value domain.

mechanism: >
  By the run telescope, (−1)^{T(n,d)} = Π_R s_{a_R} s_{b_R} with every run of ↓d
  of length 2^{ν₂(d+1)}, so each ε_d = (−1)^{T(n,d)} is a monomial in the
  sequence s of degree 2·#{runs}. S(n) = Σ_d ε_d is a sum of such monomials — a
  digital U-statistic of s. Averaging S(n)² over n ≤ N expands into correlations
  of s at digital offsets. Key structural claim: the Hájek (degree-one)
  projection of every ε_d vanishes because s has zero mean (χ is nontrivial), so
  the L² mass sits in degree ≥ 2; but those higher-degree products are products
  of INCREMENTS of the race W, and by summation by parts in the index they are
  bounded by the mean square of W over dyadic subintervals — the second moment
  of the prime race mod 4. This is a classical, named object (comparative prime
  number theory: Littlewood; Knapowski–Turán; Rubinstein–Sarnak; Granville–Martin;
  Fiorilli), and its variance is a large-sieve quantity for primes in arithmetic
  progressions (Barban–Davenport–Halberstam), in the INDEX domain — unlike the
  refuted dispersion route, whose value-shifts χ(n−a) never appear here and whose
  refutation was precisely that the bilinear form lives in the prime index rather
  than the value. Speculative half, to be priced not assumed: whether the race's
  mean square over dyadic subintervals is provable unconditionally (it is the
  variance of the error term of the prime race at conductor 4, classically hard),
  and whether that single input suffices WITHOUT any two-point switch
  correlation.

first-step: >
  tool_builder + symbolic_math: (1) derive the exact expansion of Σ_{n≤N} S(n)²
  as a sum over digital run-pattern pairs of products of s, group by the number
  of distinct indices, and verify against the oracle for N ≤ 200 on the real
  residue string and a random {±1} control; (2) summation-by-parts each term
  into the prefix sums W, identifying which terms are exactly the mean square of
  W over dyadic subintervals; (3) print the race's empirical variance
  Σ_{J≤N} W(J)² over dyadic subintervals and check its order against what
  large-sieve/BDH predicts. Falsifier: if the dominant terms of Σ_n S(n)²
  cannot be written in terms of W (genuine multi-index correlations at distance
  2^g persist at leading order), the race-variance input is insufficient and the
  route collapses to the two-point barrier.
status: refuted
killed-by: >
  Two independent defects, either alone fatal to the claimed engine.
  (1) The Höeffding/Hájek decomposition and BDH apply only in the VALUE
  domain, not the index domain, and this route's "index-domain BDH" does not
  exist. The Barban–Davenport–Halberstam theorem and its refinements (the
  quantities the route names) bound the second moment of the error term
  ψ(x;q,a) − x/φ(q) of primes in residue CLASSES mod q, averaged over moduli
  q ≤ Q (Vaughan, 10.1215/s0012-7094-03-12026-8; Fiorilli,
  arXiv:1301.5663; the classical statement is Σ_{q≤Q} Σ_{(a,q)=1}
  (ψ(x;q,a)−x/φ(q))² = O(x log Q)). Every settled instance evaluates the
  relevant character/prime sums at residue-class (value) arguments and averages
  over moduli. The objects here — two-point products χ(q_j)χ(q_{j+2^g}) at
  prime-INDEX separation 2^g — are not a value-modulus quantity at all, and no
  source bounds them (this is precisely the refuted dispersion route's finding:
  the bilinear form lives in the prime index, and q_{j+2^g} is not q_j plus a
  constant). So "BDH in the index domain" is not a real input; there is no
  classical theorem for the mean square of W(J)=Σ_{j≤J}χ(q_j) over dyadic
  subintervals that is small. (2) The empirical/algebraic shape confirms the
  route re-encounters the parity barrier. Naively Σ_{J≤X} W(J)² is
  diagonal-dominated: its main term is Σ_{j≤X} χ(q_j)² · #{J: J≥j} ≈ π(X)·X ≈
  X²/log X, so it is NOT small, and any improvement must come from cancellation
  in the off-diagonal Σ_{j<k}χ(q_j)χ(q_k)·(X−k), i.e. exactly the two-point
  switch correlation at separation k−j. The g=0 (separation 1, index-adjacent)
  stratum of Σ_n S(n)² is precisely that two-point object, whose positivity/
  decay is the named open parity barrier (research/CLAIMS.md abgs-p1-wide-open,
  lau-nonconstant-pattern-open, ash_beltis_gross_sinnott_prime_residues §9).
  Hence the "strictly weaker second-moment input" reduces to controlling the
  very correlation whose sign is open, and the route offers no input weaker than
  switch density. Refuted as a standalone engine; the second-moment objective
  it shares is better housed in the adopted fold-second-moment-krawtchouk route
  (which isolates the Delsarte/Krawtchouk part as a pure function of Φ).
precedent: >
  The named machinery is real and precisely what the route says, but only in
  the value domain: Höeffding decomposition / Hájek projection of U-statistics
  (Höeffding 1948; Bloznelis–Götze 10.1214/aos/1009210694; the projection
  vanishes in the degenerate/zero-influence case, which is the case here since
  χ_4 has zero mean); Barban–Davenport–Halberstam and its variance refinements
  (Barban; Davenport–Halberstam; Vaughan 10.1215/s0012-7094-03-12026-8;
  Fiorilli arXiv:1301.5663; Friedlander–Goldston). The mod-4 prime RACE is a
  real named object with a real literature (Littlewood; Knapowski–Turán;
  Rubinstein–Sarnak on disk; Granville–Martin on disk; Fiorilli), but it is
  about π(x;q,a) value races and their sign-oscillation, NOT about the mean
  square of the two-point index-separated correlation that this route needs;
  no source in that literature controls Σ_{j<k}χ(q_j)χ(q_{j+2^g})·(length).
  Inside-workspace parity barrier: abgs-p1-wide-open, lau-nonconstant-pattern-
  open, los-switch-preferred-mod4 (asserted/heuristic).
```

## Distinctness (not a restatement)

- Not `dispersion-bilinear-large-sieve` (refuted): that route squared S(n) and fed the four-fold χ-correlation to Linnik's dispersion with value-shifts χ(n−a); it died because q_{j+2^g} is not q_j plus a constant. This route stays in the index and bounds everything by the one-dimensional race W, using BDH/large-sieve on progressions of the INDEX, not shifts of the value.
- Not `fold-second-moment-krawtchouk` (adopted): that route computes E[S(n)²] for iid h and leaves the arithmetic autocorrelation as an unpriced input; this route supplies a candidate arithmetic engine (the race variance) for the selfsame input.
- Not `dyadic-gap-character-correlation` (adopted): that route prices two-point correlations χ(q_j)χ(q_{j+2^g}) directly; this route replaces them with the strictly weaker-looking second moment of the one-point partial sums W.
