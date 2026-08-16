# Meet-semilattice Möbius factorization of the second moment

```approach
idea: >
  Factor the one open arithmetic input — E[S(n)²] = O(n) for the prime string,
  equivalently Σ_{d,d'} ∏_{j ∈ M_d △ M_{d'}} u_j = O(n) with
  u_j = χ(q_j)χ(q_{j+1}) the switch sign — over the meet-semilattice of the
  fold's windows using Rota's Möbius inversion on the Boolean lattice. By the
  proved meet formula M_d ∩ M_{d'} = M_{d∧d'} (claim
  downset-row-intersection-meet-formula), the symmetric difference is the
  disjoint union M_d △ M_{d'} = (M_d ∖ M_j) ⊔ (M_{d'} ∖ M_j), j = d∧d'. Each
  piece M_d ∖ M_j is a union of subcubes indexed by the set bits of d ∖ j on
  the m = ⌈log₂ n⌉-bit lattice. Inclusion–exclusion (subcube Möbius inversion)
  should therefore write the monomial ∏_{M_d△M_{d'}} u_j as a product over the
  set bits of d △ d' of per-bit factors; then the constraint d∧d' = j makes the
  double sum an INDEPENDENCE POLYNOMIAL of a disjointness graph on m bit
  positions: Σ_{d,d' : d∧d'=j} (monomial) = ∏_{b ∉ j} (1 + 2λ_b(j)) up to the
  meet-j sum. This would reduce the second moment to a first-moment (two-point)
  input per bit — a candidate arithmetic input strictly weaker than positive
  mod-4 switch density (GOAL priority 2/4).
mechanism: >
  Named machinery: Rota's Möbius function μ(x,y) of the subset lattice, subcube
  inclusion–exclusion, and the independence polynomial (the hard-core/transfer
  structure) of the disjointness graph on the depth-index bits. This is NOT the
  refuted ANF/Reed–Muller route (which reads the FIRST moment's Möbius transform
  and was inert as a relabeling) and NOT the spectral diagonalization of
  meet-join-parseval-self-duality (which proved geometry carries no pointwise
  force): it is a combinatorial factorization of the SECOND-moment monomial into
  a product over the m depth bits, converting a coupled double sum into an
  independence-polynomial evaluation. The load-bearing conjecture is that
  M_d ∖ M_j is a disjoint union of subcubes whose character product is
  per-bit-multiplicative; the first step exists to prove or kill exactly that.
status: refuted

killed-by: The load-bearing per-bit factorization of M_d \ M_j is FALSE, shown by an exact F2 counterexample that the meet formula makes trivial to exhibit. Take d=3 (bits {0,1}) and j=0 (d∧d'=0, i.e. disjoint windows). Then D = {s⊆3 : s⊄0} = {1,2,3}, a single interval of length 3. The claimed decomposition D = ⊔_{a⊆(d∖j), a≠0} (a + downset(j)) = {1} ⊔ {2} ⊔ {3} with each piece a singleton (run length 2^{ν₂(j+1)} = 2^0 = 1), so the "runs stay separated" half predicts 3 runs of length 1 — but {1,2,3} is one run of length 3. The translated downset copies MERGE across distinct set bits of d∖j, so the character product over M_d△M_{d'} does NOT factor per-bit, and the independence-polynomial decoupling Σ_{d∧d'=j}(monomial) = ∏_{b∉j}(1+2λ_b(j)) has no basis. This is falsifier (a) of the route's own statement: the exact interleaving/merging obstruction is the deliverable, not the factorization. The meet formula and Rota/Baker/independence-polynomial machinery remain correct and stay grounded as tools, but they do not decouple the second moment. (The run-telescope run-length fact is 2^{ν₂(d+1)} with g the trailing-1 count of d, and each downset's runs have length 2^{ν₂(j+1)} only when the low bits are aligned; the translated copies over d∖j are adjacent in exactly the case that kills per-bit independence.)

precedent: >
  The Boolean-lattice machinery is classical and fully grounded. Rota, "On the
  foundations of combinatorial theory I: theory of Möbius functions",
  Z. Wahrscheinlichkeitstheorie 2 (1964) 340-368 (link.springer.com/article/
  10.1007/BF00531932) establishes Möbius inversion on the Boolean lattice, of
  which subcube inclusion–exclusion is the special case; Baker, "Hodge theory
  in combinatorics", Bull. AMS 2017 (arXiv:1711.08900) states the Möbius
  inversion formula on a finite poset and its specialization to the Boolean
  lattice, with the meet-as-intersection structure. The independence polynomial
  of a graph (the hard-core/transfer object) is standard (Dohmen–Poenitz–
  Tittmann, Discrete Math. Theor. Comput. Sci. 2003, arXiv:math/0305362, place
  it alongside the chromatic and matching polynomials as specializations). The
  run's own meet-semilattice structure is proved in-workspace as claim
  downset-row-intersection-meet-formula (M_d ∩ M_{d'} = M_{d∧d'}, hence
  |M_d △ M_{d'}| = 2^pc(d) + 2^pc(d') − 2^{pc(d∧d')+1}). What the literature
  does NOT contain — and no search found — is ANY application of Möbius
  inversion / independence-polynomial machinery to a Pascal-mod-2 sliding-window
  fold weight, nor a prior factorization of the symmetric-difference monomial
  ∏_{j∈M_d△M_{d'}} u_j into per-bit factors. The load-bearing step — "M_d ∖ M_j
  is a disjoint union of subcubes whose character product is per-bit-
  multiplicative" — is a conjecture that is neither sourced nor refuted; it is
  a pure-F2 fact the first-step is designed to prove or kill. So the route's
  MACHINERY is grounded and its per-bit factorization is an open, checkable,
  in-workspace conjecture (no external theorem needed). If the factorization
  holds, it genuinely reduces the coupled double sum to an independence-
  polynomial evaluation — a new algorithmic/structural step, not a relabeling.
first-step: >
  tool_builder, exact F₂/integer arithmetic, no number theory (the prime string
  is not needed). (1) For every pair (d, j) with j ⊆ d and d ≤ n−1, n ≤ 64,
  compute the reflected-downset difference M_d ∖ M_j, its maximal runs, and
  test whether the runs are subcubes in the reflected index — i.e. whether
  ∏_{runs} χ(r_a)χ(r_b) factorizes as a product over the set bits of d ∖ j.
  (2) For each j, compute the double sum C(j) = Σ_{d,d' : d∧d'=j} ∏_{M_d△M_{d'}} u_j
  as a polynomial in the switch signs and test the independence-polynomial
  identity against it. FALSIFIER: if M_d ∖ M_j has a run that is not a subcube
  (interleaving across two set bits), the per-bit factorization fails; the route
  then records the exact interleaving obstruction as a priced negative instead of
  forcing the factorization.
falsifies: >
  (a) a non-subcube run in M_d ∖ M_j (the factorization is false and the exact
  obstruction is the deliverable); (b) the independence-polynomial identity
  fails in degree or in the λ_b(j) dependence (then the meet factorization does
  not decouple, and the second moment is genuinely a non-product object); (c) the
  resulting per-bit λ_b(j) quantities turn out to need the switch density itself
  (then the route collapses to the parity barrier, i.e. priority 5 is the truth).
```
