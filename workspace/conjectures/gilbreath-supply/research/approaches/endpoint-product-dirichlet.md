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
status: refuted

killed-by: The chi4-contraction machinery the route mounts is real but lives in the VALUE domain, and the fold's endpoints are separated in the PRIME INDEX, not by value — the same index-vs-value obstruction that closed matomaki-radziwill-index-autocorrelation, dispersion-bilinear-large-sieve, and rubinstein-sarnak-prime-race-ergodic. Dummit–Granville–Kisilevsky, "Big biases amongst products of two primes" (J. London Math. Soc. 2016, arXiv:1105.5022), Theorem 1.1, is the named engine and it proves the exact object the route names — the count of pq <= x with chi4(p)=chi4(q)=eta equals (1/4)(1 + eta L(1,chi4)/log log x) of the total, with L(1,chi4) = sum_p chi4(p)/p. This is a hard, correct, citable theorem about a VALUE-ordered product. But every fold term chi4(P_{d,d'}) with P = product of run-endpoint primes is indexed by the PRIME-INDEX separation b-a = 2^g, not by the product's size: the route's own run telescope (claim no-standalone-switch-sign-in-squared-excess, proved in-workspace) says the endpoints q_a, q_b sit at index separation a power of 2. The DGK engine and the whole L(s,chi4) framework (Dirichlet series, Perron inversion, Selberg-Delange) converge over value-ordered products pq <= x; it has no handle on "consecutive-in-INDEX primes at separation 2^g", which ABGS (claim abgs-p1-wide-open) says is L-function-inaccessible. LOS's own K>=2 correction (arXiv:1709.06168) turns that index-domain term into a Dedekind-sum / phi-error object, not a clean L-function. So hypothesis (b) of the route's own falsifier fires: every separation-g stratum with g>=1 provably reduces to the same index-domain object as the adjacent-pair switch density, whose machinery is not L-functions. The contraction chi(ab)=chi(a)chi(b) is a correct bookkeeping identity but moves the difficulty only from "product of two characters at two indices" to "a character at a value-ordered prime product" — it does NOT move the index separation into the value ordering where L-functions act. Refuted on evidence (the DGK-LOS-ABGS value-vs-index split), not on absence.

precedent: >
  Dummit, Granville, Kisilevsky, "Big biases amongst products of two primes",
  J. London Math. Soc. 93 (2016) 424-446, arXiv:1105.5022; Theorem 1.1 — the
  value-domain chi4(product-of-two-primes) bias governed by L(1,chi4), the
  closest citable relative of the route's P_{d,d'} contraction. -, Ash,
  Beltis, Gross, Sinnott, "Frequencies of successive pairs of prime residues",
  Exp. Math. 17 (2008) sec.9 (claim abgs-p1-wide-open): index-domain
  consecutive-pair frequencies are L-function-inaccessible. -, Lemke Oliver,
  Soundararajan, "Unexpected biases in the distribution of consecutive primes",
  PNAS 113 (2016), arXiv:1709.06168; the K>=2 secondary bias term is a
  Dedekind-sum/Fourier-transform-of-phi-error object, not an L-function value.
  -, In-workspace (established): claim no-standalone-switch-sign-in-
  squared-excess (every non-diagonal S(n)^2 term is a product of >=2 switch
  signs at non-adjacent index separations — the object the route must bound),
  claim abgs-p1-wide-open, claim los-secondary-bias-orientation-invisible-to-fold.
  Indicates the route collapses to the parity barrier: priority 5 (SUPPLY
  equivalent to switch density) is indicated, priority 4 (a strictly weaker
  input) is not delivered by this machinery.

first-step: >
  superceded by the refutation. If reopened, the decisive check is a
  classification of the endpoint products: enumerate (d,d') at n<=64, record
  each P_{d,d'} = product of run-endpoint primes, and test whether ANY of them
  admits a value-domain L-function bound (i.e. whether the endpoint products
  can be ordered by size compatibly with the index separation). The DGK result
  shows the bias exists; it does not transfer to the index, so it cannot bound
  the fold's second moment.
falsifies: >
  (a) the endpoint multiset of M_d △ M_{d'} is not closed under χ₄-contraction
  (a bookkeeping defect); (b) every separation-g stratum with g ≥ 1 provably
  requires the adjacent-pair switch density (then the L-function route adds
  nothing and priority 5 is the truth, recorded as such); (c) the endpoint
  products χ₄(P_{d,d'}) have no Dirichlet-series structure (the reformulation
  is inert). Falsifier (b) fired in the grounding check.
```
