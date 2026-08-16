# χ₄-of-endpoint-products: Dirichlet L-function machinery on the second moment

```approach
idea: >
  Use the complete multiplicativity of the quadratic character χ₄ to collapse
  each second-moment term to a single character value at a structured prime
  product, then attack the resulting double sum with Dirichlet-series and
  L-function machinery. The run telescope gives
  ∏_{j∈M_d△M_{d'}} u_j = ∏_{runs R} χ(q_{a_R})χ(q_{b_R}); by χ(ab)=χ(a)χ(b)
  this equals χ₄( ∏_R q_{a_R} q_{b_R} ) = χ₄(P_{d,d'}), a value of the Dirichlet
  character at an explicit product of primes whose factors are the run endpoints
  at dyadic separations. Reorganize Σ_{d,d'} χ₄(P_{d,d'}) by the endpoint
  multiset and the separation 2^g. Each separation-g stratum is a sum of χ₄ over
  prime k-tuples with prescribed index gaps — a Dirichlet-type series
  Σ χ₄(product) governed by products of L(s,χ₄) and their twists. The load-bearing
  input from the squared-excess route (claim: no symmetric difference M_d △ M_{d'}
  is a singleton) says every P_{d,d'} is a product of ≥ 2 prime factors, so the
  fold never reads a single switch sign u_j = χ(q_j)χ(q_{j+1}) standalone: it
  reads products u_a u_b (and longer products) at classified non-adjacent
  separations. The open question is whether those ≥2-factor switch-sign
  correlations are strictly weaker than the 1-factor switch-density mean, or
  equivalent to it. Outcome: either the ≥2-factor correlations are bounded by
  unconditional PNT-in-AP / L-function machinery and a strictly weaker input
  exists (priority 4), or they are as hard as the adjacent-pair object (ABGS §9)
  and SUPPLY ⟺ switch density is proved as a theorem (priority 5).
mechanism: >
  Named machinery: Dirichlet L-functions with the explicit formula and Perron
  inversion; the Hardy–Littlewood k-tuple singular series for prime tuples with
  prescribed residues; the Selberg–Delange / convolution treatment of
  Σ χ₄(n) and its twists. The point of the reformulation: χ₄ evaluated at a
  PRODUCT of primes is a multiplicative function of one structured argument,
  placing the fold's second moment inside the L-function framework that the raw
  adjacent-pair switch density is excluded from (ABGS §9). This is distinct from
  the refuted level-set-explicit-formula-index-correlation route (which tried to
  move the INDEX into a value-domain weight z^{π(p')−π(p)} and failed): here the
  index structure is kept, and the character is contracted by multiplicativity
  onto a product, so no index→value transfer is claimed.
status: proposed
first-step: >
  tool_builder + research, exact arithmetic, real residue string r_j = q_j mod 4.
  (1) For n ≤ 64 enumerate every ordered pair (d,d') and print the endpoint
  multiset of M_d △ M_{d'}: for each maximal run [a,b] record the prime-index
  pair (a, b+1) and the separation b+1−a (a power of 2 for downset runs; to be
  checked for symmetric differences). (2) Produce the exact generating function
  F(z) = Σ_{d,d'} ∏_{runs} z^{sep}·χ₄(q_a)χ₄(q_b), and report the endpoint-factor
  count and separation distribution, confirming every term has ≥ 2 factors (no
  singleton). (3) Price the ≥2-factor strata: state the precise unconditional
  bound for Σ χ₄(q_a)χ₄(q_{a+ℓ}) at the fold's classified separations ℓ ≥ 2 that
  PNT-in-AP / L-function machinery supplies, and record what is missing if none.
  FALSIFIER: if the ≥2-factor correlations reduce to the same adjacent-pair
  object (as hard as the 1-factor switch density), the route collapses to the
  parity barrier and priority 5 is the truth; if not, it yields the first
  strictly weaker input.
falsifies: >
  (a) the endpoint multiset of M_d △ M_{d'} is not closed under χ₄-contraction
  (a bookkeeping defect); (b) every separation-g stratum with g ≥ 1 provably
  requires the adjacent-pair switch density (then the L-function route adds
  nothing and priority 5 is the truth, recorded as such); (c) the endpoint
  products χ₄(P_{d,d'}) have no Dirichlet-series structure (the reformulation
  is inert).
```
