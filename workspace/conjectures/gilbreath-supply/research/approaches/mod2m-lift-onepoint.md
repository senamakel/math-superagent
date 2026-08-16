# Higher-modulus lift: price whether one-point equidistribution mod 2^m forces the fold

```approach
idea: > SUPPLY's only unconditionally-available arithmetic input is ONE-POINT
  equidistribution of primes in reduced residue classes: for every fixed m,
  π(x; 2^m, a) ~ π(x)/2^{m−1} uniformly in a (PNT in AP / Siegel–Walfisz, with
  an effective version avoiding the exceptional-zero caveat). Switch density
  (the open barrier) is a TWO-POINT (index-adjacent) statistic. This route
  asks: does wt(Φ_n h) ≥ c·n follow from one-point equidistribution mod 2^m for
  some fixed m? If yes, SUPPLY is proved from a known input strictly weaker
  than switch density; if provably no, that is a genuine negative theorem
  locating SUPPLY's minimal correlation order.
mechanism: > The fold cell T(n,d) is the parity of a product over the run
  telescope: (−1)^{T(n,d)} = ∏_R χ(q_{a_R}) χ(q_{b_R}) with χ the quadratic
  character mod 4. Every such product is a monomial in the residue indicators
  r_j = q_j mod 2^m for m ≥ 2, of degree 2·(#runs). Summing cells over a chosen
  family of d collapses the monomial by character orthogonality: products of
  characters at REPEATED indices reduce to lower-degree (eventually one-point)
  statistics whenever the index multiset has even multiplicity. The route is to
  search over linear combinations of fold cells — i.e. over the image
  F_2-linear map — for a functional whose value is a provable function of the
  one-point counts π(x;2^m,a), using the orthogonality relations of the
  characters of (Z/2^m)^* to eliminate all but one residue. Concretely the
  object to price is the F_2-span of {χ_4(q_{j})χ_4(q_{j+2^g}) : g} intersected
  with the space of one-point statistics, and the question is whether the fold
  weight (a sum of squares of these monomials) is bounded below by any such
  span element. This is higher-order Fourier analysis over (Z/2^m)^* applied to
  the fold's multilinear form — the marginalization problem, not the large
  sieve (which needs value shifts and died for that reason).
status: refuted

killed-by: >
  ONE-POINT EQUIDISTRIBUTION DOES NOT DETERMINE THE TWO-POINT (CONSECUTIVE
  PAIR) DISTRIBUTION — and the fold's cells are ≥2-point objects, so no
  one-point statistic mod 2^m can force wt(Φ_n h) ≥ c·n. The route's
  mechanism would need some F_2-linear combination of fold cells to telescope,
  by character orthogonality mod 2^m, into a one-point statistic (a function of
  a single q_j mod 2^m). But by the run telescope (claim g-run-telescope-
  verified, checked) every nonzero fold cell is (−1)^{T(n,d)} = ∏_R χ(r_{a_R})
  χ(r_{b_R}), a product over the runs of ↓d of a character PAIR χ(r_a)χ(r_b)
  with a ≠ b (the gap b−a ≥ 2 for every odd d ≥ 3, a ≥ 1). Collapsing a
  product of distinct-index characters to one-point requires the index multiset
  to have all multiplicities even, which a run product never does (each of the
  2·#runs distinct indices appears once, and no two runs share an index).
  Character orthogonality therefore never reduces a single fold cell to a
  one-point statistic; and the weight wt(Φ_n h) = #{d : T(n,d)=1} is a count of
  CELLS (each ≥2-point), not a single multilinear form — so it is not in the
  F_2-span the mechanism proposes to marginalise. The route's own expected
  output — "the one-point-realizable subspace of the fold's row space is O(1)"
  — is what the mechanism structurally forces, and it matches the literature
  verdict below.
  LITERATURE CORROBORATION: over the integers, one-point equidistribution of
  primes in reduced residue classes mod 2^m (PNT in AP / Siegel-Walfisz, the
  only unconditional input the route prices) does NOT determine the
  consecutive-pair distribution mod 4. Lemke-Oliver–Soundararajan 2016
  (PNAS, DOI 10.1073/pnas.1605366113): "When r ≥ 2, little is known about the
  distribution of such patterns"; Wu 2019 (arXiv:1908.07095) and Kim 2020
  (Prime Running Functions, 10.1080/10586458.2020.1786863) state explicitly
  that equidistribution of single primes among residue classes does not by
  itself determine consecutive-pair frequencies. For q=4 the fair-share of the
  four pair classes is open (ABGS §9, claim abgs-p1-wide-open);
  lau-nonconstant-pattern-open says even ONE non-constant 2-term pattern is not
  known to occur infinitely often. Since switch density (the two-point input,
  which is what the fold's g=0 cells read) is exactly this open object, NO
  one-point input suffices. This closes GOAL priority 2 negatively for this
  candidate and corroborates priority 5: SUPPLY is a ≥2-point statement.
  A genuine (already-known) negative theorem is the honest deliverable here,
  and the route's own risk statement said as much.

precedent: >
  - Lemke-Oliver, Soundararajan, "Unexpected biases in the distribution of
    consecutive primes", PNAS 113 (2016) / arXiv:1603.03720, DOI
    10.1073/pnas.1605366113 — r≥2 patterns not determined by one-point class
    equidistribution.
  - Wu, "Nonuniform Distributions of Residues of Prime Sequences in Prime
    Moduli", arXiv:1908.07095 — single-prime equidistribution does not
    determine consecutive-pair patterns.
  - Kim, "Prime Running Functions", Exp. Math. 2020, DOI
    10.1080/10586458.2020.1786863 — pair counts conjectural, biased; one-point
    does not fix pairs.
  - ABGS 2011 §9 (on disk ash_beltis_gross_sinnott_prime_residues) — the
    fair-share pair problem is open / L-function-inaccessible; claims
    abgs-p1-wide-open, abgs-pair-frequency-equality-open.
  - Lau, "Residue Class Patterns of Consecutive Primes", arXiv:2409.12819,
    claim lau-nonconstant-pattern-open — even one non-constant 2-term pattern
    not known to occur infinitely often.
  - Claims on disk it reproduces (as the ≥2-point requirement): g-run-telescope-
    verified (each cell is a product of character pairs at distinct indices),
    excess-is-negative-character-sum (2ν₂−(n−2) = −S(n), S = sum of the
    ≥2-point cells).

  combinations of fold cells whose ±1 product telescopes to a one-point
  statistic (a function of a single q_j mod 2^m), verify each against the
  oracle and against the known one-point equidistribution, and record the
  maximum such functional's growth. The decisive output is a table: for each m,
  the largest one-point-realizable subspace of the fold's row space and whether
  it grows linearly in n. If no m yields a linear-size subspace, price the
  minimal correlation order of SUPPLY (a 2-point, 3-point, ... statement) and
  file it as a negative result toward GOAL priority 3.
falsifies: > (a) For every fixed m, the one-point-realizable subspace of the fold's
  row space is O(1) in size — then SUPPLY is provably a ≥2-point statement and
  no known unconditional input suffices, closing GOAL priority 2 negatively
  (which is itself a deliverable). (b) The orthogonality collapse requires
  characters of (Z/2^m)^* beyond quadratic, and those higher characters at
  prime arguments are NOT controlled one-point by PNT in AP (they are, but only
  via the same theorem with conductor 2^m — Siegel–Walfisz covers all
  nonprincipal characters mod 2^m, so this must be checked: it holds, which is
  the point of the lift).
scholze-gate: > Reproduces on disk: `excess-is-negative-character-sum` (the ±1
  identity 2ν₂−(n−2) = −S(n) is the starting point), the PNT-in-AP/single-point
  equidistribution claim (the input), and `g-run-telescope-verified` (the run
  product form of each cell, which is what gets collapsed by orthogonality).
```

## Why this is not the refuted dispersion / large-sieve / prime-race routes

- **Not dispersion (`dispersion-bilinear-large-sieve`, refuted):** that route
  squared S(n) and needed VALUE shifts χ(n−l), which do not exist in the prime
  index. This route never squares; it searches the row space for a functional
  that is already one-point, using character orthogonality over a higher
  modulus. No value shift appears.
- **Not prime-race (`rubinstein-sarnak-prime-race-ergodic`, refuted):** that
  route was conditional on GRH+LI and one-point *in the bias sense*; this route
  is unconditional (PNT in AP mod 2^m, effective) and asks a finite linear-
  algebra question about the fold's row space, not a limit theorem.
- **Not Walsh discrepancy (`walsh-discrepancy-erdos-turan`, refuted):** that
  route was killed by Parseval (the L¹ Walsh norm is minimized by flat spectra).
  This route does not take L¹ over the Walsh system; it takes F_2-linear
  spans of the run-product monomials and marginalizes by character
  orthogonality mod 2^m — a different, finite computation.

The honest risk, stated up front: the natural guess is that the fold's cells are
irreducibly ≥2-point (the run telescope makes each cell read two or more
indices), in which case the first-step table returns O(1) subspaces and the
route produces the negative theorem "SUPPLY needs at least a 2-point input" —
which is exactly GOAL priority 5's honest closure and worth the pricing.
