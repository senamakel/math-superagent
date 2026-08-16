# Moment method for S(n) under the Hardy-Littlewood k-tuples conjecture

```approach
idea: Compute the FULL moment sequence of S(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}
under the Hardy-Littlewood k-tuples conjecture (with prescribed residues, the
form that DOES capture the Lemke Oliver-Soundararajan mod-4 pair bias), and
conclude S(n) = O(sqrt n) via a number-theoretic central limit theorem — giving
POINTWISE SUPPLY with c -> 1/2.
mechanism: Expand the 2r-th moment S(n)^{2r} = sum_{d1..d2r} prod_ell eps_{d_ell},
eps_d = prod_{R in runs(down(d))} chi4(q_{a_R}) chi4(q_{b_R}). HL k-tuples gives
the expectation of each product as the singular series of its residue pattern.
The KEY CLAIM: the singular series resums so that E[S(n)^{2r}] =
(2r-1)!! (n-2)^r (1+o(1)) — Gaussian moments of variance n-2 — because the
distance enumerator F_n(z)=O(n) already gives the second moment. Then Markov on
high moments forces max|S(n)| = O(sqrt(n log n)), hence nu2 = n/2 - o(n).
The arithmetic input is HL k-tuples, a single named conjecture, claimed
STRICTLY WEAKER than proving the switch density.
first-step: compute S(n)^{2r} for r=1,2,3, n<=64 by the run-telescope formula,
print ratio to (2r-1)!!(n-2)^r; derive singular-series coefficients; check the
mod-4 biased HL pair frequencies reproduce LOS 57.5% switch.
falsifier: if any even moment is NOT O(n^r), the Gaussian resummation fails.
status: refuted
precedent:
  Hardy-Littlewood prime k-tuple conjecture and singular series:
  - "Kowalski, Averages of Euler products, distribution of singular series,
    Acta Arith. 2011, doi 10.4064/aa148-2-4 — S(h) singular series, moments."
  - "Large prime gaps and probabilistic models, Invent. Math. 2023,
    doi 10.1007/s00222-023-01199-0 — S(H), probabilistic sift, HL for
    admissible H."
  - "Merikoski, Averaged form of the Hardy-Littlewood conjecture,
    arXiv:1605.04757 — averaged (Gallagher) forms."
  Moment method / number-theoretic CLT (the named engine, real):
  - "Leung, Moments of primes in progressions to a large modulus,
    arXiv:2402.07941 — physical moment method for primes in AP under a
    uniform q-variant of HL."
  - "de la Bretèche-Fiorilli, Moments of moments of primes in arithmetic
    progressions, Proc. LMS 12542, doi 10.1112/plms.12542 — all even moments."
  - These all ASSUME a uniform HL variant (the exact graded input this route
    prices as "weaker") — confirming they are within the conjecture, not
    cheaper than it.
  Switch density is the m=2 HL pattern and is open / L-function-inaccessible:
  in-workspace claims abgs-p1-wide-open, abgs-pair-frequency-equality-open,
  los-switch-preferred-mod4, los-scale-bias-slowdecay.
  Second/fourth moment measurements for the real h: fold-second-moment-*,
  fourth-moment-plateau-3n2.
  No source applies the HL moment method to the fold weight wt(Phi_n h) or to
  the submask correlation excess S(n); searches return the HL/moment-CLT
  literature (Leung, de la Bretèche-Fiorilli, Dixit-Murty), none touching this
  object. Say plainly: I found no prior application of either the k-tuples or
  the moment method to the Pascal-mod-2 fold weight of the prime gap-parity
  string.
killed-by: >
  Three defects — two structural, one a price reversal — any one of which defeats
  the intended conclusion. Refuted on evidence, not on absence.

  (1) HL k-tuples is STRONGER than switch density, not weaker — the PRICE
  REVERSAL. The central claim is that HL k-tuples is "strictly weaker than
  proving the switch density". That is backwards. The switch density (positive
  fraction of consecutive-prime pairs differing mod 4) is ITSELF the m=2
  Hardy-Littlewood pattern frequency: #{n : n, n+d prime, prescribed residues}
  ~ S(d)·x/(log x)^2 with S(d) the 2-tuple singular series, summed over which
  gives the pair-class frequencies mod 4 (ABGS 2011 §9: this is the object
  whose asymptotic is open, claim abgs-p1-wide-open). HL for k-tuples with k
  > 2 (which the higher moments S(n)^{2r} need — each cell reads >= 2
  run-endpoint pairs, and a 2r-th moment term is a product of up to
  2r·(runs) distinct prime pairs) is a STRONGER input: it asserts asymptotics
  for r-tuples not even known for pairs. So the route accepts a stronger price
  to buy a weaker-grade conclusion, the reverse of GOAL priority 2's target.

  (2) The Gaussian moment resummation is the hard step, not a finite check. The
  mechanism leans on "the meet-semilattice geometry makes the higher-moment
  resummation a finite combinatorial check". But E[S(n)^{2r}] under HL is not a
  finite combinatorial count: computing the expectation of a product over 2r
  submask cells under the k-tuples singular series requires, for every
  (d_1..d_{2r}), the singular series of the union of their run-endpoint primal
  index sets — overlapping patterns, valuation of near-singular-series zeros,
  and cancellation across an a-priori Theta(n^{2r})-sized index set. The
  geometry (F_n(z)=O(n), claim fold-distance-enumerator-On) bounds the second
  moment because pairs are counted by popcount; the higher moments are NOT
  bounded by the same enumerator — the factorization F_n(z)^r the route would
  need fails for r >= 2 (cells overlap, the run-endpoint sets are not pairwise
  disjoint-index-independent). No source establishes the claimed (2r-1)!!
  factor for the prime string; it is asserted precisely where the difficulty
  lives. Measured evidence (claim fourth-moment-plateau-3n2: E[Z^4] ~ 2.95,
  kurtosis ~ 2.953 — Gaussian would be 3, so even the second-moment-normalized
  4th moment is not cleanly Gaussian for the real h).

  (3) The leading HL singular series is mod-4 UNBIASED — it does not reproduce
  the LOS switch bias at main term. The candidate says HL-with-residues "has
  the correct mod-4 bias". At its MAIN TERM the 2-tuple singular series assigns
  the four ordered mod-4 pair classes equal weight; the LOS 57.5% switch is a
  LOWER-ORDER / SECONDARY bias (LOS 2016; claim los-scale-bias-slowdecay:
  the equal/switch imbalance is lower-order, decaying on the slow
  loglog x / log x scale, not a change in the leading constant). So even at the
  pair level the "correct bias" is a secondary correction, not a main-term
  constant — the same unbias-defect that killed cramer-gallagher-second-moment
  at the level the moments would sample.

  Combined: the route demands a strictly stronger conjecture (HL k-tuples,
  k>=2), whose main term is mod-4 unbiased, and asserts the one step (Gaussian
  higher-moment resummation) that is both unproved and not a finite
  combinatorial fact. It is distinct from cramer-gallagher-second-moment (which
  used the Cramér model); the price reversal and the asserted-resummation
  defect are independent and fatal. The honest position is unchanged: even a
  fully proved HL-k-tuples theory would not deliver pointwise SUPPLY unless it
  first proved the m=2 switch frequency is positive — which is the very parity
  barrier.
```

## Distinctness and honesty

Not cramer-gallagher-second-moment (that used the Cramér/Gallagher model,
unbiased mod 4); this route uses HL-with-residues directly. Refuted on
evidence: the graded input is strictly stronger (not weaker) than the switch
density it claims to be cheaper than; the Gaussian higher-moment factor is
asserted where the difficulty lives; and the singular-series main term is
mod-4 unbiased.
