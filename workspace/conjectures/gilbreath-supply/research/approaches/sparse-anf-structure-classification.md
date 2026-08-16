# Converse by classification: sublinear fold weight forces a sparse ANF, and a sparse Boolean polynomial is a rigid object — structure theorem for low-weight fold images

```approach
idea: >
  Run the refuted ANF/Möbius route in the OPPOSITE direction. The zeta (Möbius /
  Reed–Muller) transform is self-inverse, so ν₂(n) = wt(Φ_n h) is exactly the
  number of nonzero ANF monomials of the window h[n−1−d .. n−1] read as a Boolean
  function of the bit-index d. A counterexample to SUPPLY means ν₂(n) = o(n) on a
  set of n, i.e. the windows have SPARSE ANF. The claim to attack: a Boolean
  function on m bits with ≤ ε·2^m monomials is a *sparse polynomial* — low
  algebraic degree, decomposing into few low-degree factors — and the only way an
  infinite string h has sparse-ANF windows on a density-1 set of n is that h is
  either (i) switch-sparse, or (ii) dyadically structured (2-regular). The primes
  are neither (Shiu kills (i)-density; non-automaticity kills (ii)), so SUPPLY
  holds. This is GOAL priority 3 made constructive: a *classification* of
  low-weight fold images rather than a bound on their number.

mechanism: >
  The engine is the SAME involution the refuted route used (supply-fold-submask-
  zeta-involution: T(n,d) = a_d = ⊕_{s⊆d} τ[s], self-inverse), but the direction
  is reversed. The refuted `anf-mobius-reed-muller` route needed to show the ANF
  support is LARGE — that is the Reed–Muller weight-spectrum enumeration problem,
  which is open (Carlet). This route assumes the ANF support is SMALL and asks what
  that forces: "few monomials ⇒ structured truth table" is the tractable direction
  of sparse-polynomial theory (a Boolean polynomial with k monomials has algebraic
  degree ≤ log₂ k and is a product/OR of few low-degree factors), NOT the open
  enumeration problem. Concretely, ν₂(n) ≤ ε n says the window τ on ⌈log₂ n⌉ bits
  equals a XOR of ≤ ε n monomials; by Möbius inversion the window itself is a
  sparse polynomial, so it is determined by its low-degree part — which is a
  global rigidity statement about h once it holds on a density-1 set of window
  lengths. The two named risks to price are: (a) whether sparse-ANF windows on a
  density-1 set force a single global sparse-polynomial / 2-regular description of
  h (the local-to-global step that killed `mahler-2kernel-automaticity`, but here
  the target structure — sparse polynomial, hence low degree — is strictly
  stronger than "finite 2-kernel", and it is exactly the place to test); (b) the
  Thue-Morse witness, which has ~50% switch density yet sublinear fold weight —
  under this classification it must land in case (ii) (2-regular), which is the
  prediction to verify mechanically.

status: refuted

precedent: >
  The sparse-polynomial / low-degree foundation is real, but only for GENUINELY
  sparse representations (polynomially many monomials), which is NOT the regime a
  counterexample to SUPPLY lives in. Sources:
  - Chattopadhyay–Dahiya–Lovett, "Restriction Trees for Sparsity and Applications",
    STOC 2026 / arXiv, DOI 10.1145/3798129.3800895 — exact vs approximate sparsity
    polynomially related on a log-scale; log of De Morgan sparsity characterizes
    communication complexity. Genuine-sparsity rigidity (sparsity = poly(n)).
  - Learning sparse Boolean polynomials, IEEE (2013), DOI 10.1109/ISIT.2013.6620416 /
    URL https://ieeexplore.ieee.org/document/6483472 — recovery from m = O(s² n)
    samples when f is s-sparse (s ≪ 2^n). Again genuinely-sparse regime.
  - Carlet et al., average degree-k monomial density bounds, Cryptogr. Commun.
    (2023/2025), DOI 10.1007/s12095-025-00839-x and 10.1007/s12095-023-00660-4 —
    degree-k monomial densities: the low-degree / ANF-sparsity structure literature.
  - Inside-workspace: supply-fold-submask-zeta-involution (the identity is real);
    mahler-2kernel-automaticity (refuted on the same local-to-global transfer);
    anf-mobius-reed-muller (identity grounded, payoff ungrounded).

killed-by: >
  Scale error: at the window's own variable count, a counterexample's ANF is
  DENSE, not sparse, so the "few monomials ⇒ low degree ⇒ factorization" engine
  cannot engage. The window τ_n is a Boolean function on m = ⌈log₂ n⌉ bits, so it
  has at most 2^m = n possible ANF monomials, and its ANF weight IS ν₂(n). The
  counterexample hypothesis is ν₂(n) = o(n) = o(2^m), e.g. ~ n/log n = 2^m/m
  monomials — an EXPONENTIALLY LARGE number of monomials, i.e. a constant-to-1/f(m)
  FRACTION of the full monomial space. The degree bound the route invokes is
  deg ≤ log₂(#monomials) = log₂(εn) = m + log₂ ε, so the algebraic degree is within
  an additive constant of the MAXIMUM m. No low-degree, no factorization, no
  rigidity: a degree-(m−O(1)) polynomial with ~2^{m}/m monomials is an unstructured,
  generic Boolean function, and the sparse-polynomial classification theorems
  (Chattopadhyay–Lovett et al.) apply only where the monomial count is poly(n),
  not a constant fraction of an exponential space. So "ν₂ ≤ ε n" is NOT the
  sparse-ANF hypothesis the mechanism needs; relative to the window it is a dense
  weighted condition, and the tractable converse direction evaporates.
  Second, independent defect: even granting a low-degree conclusion on individual
  windows, the local-to-global step — "sparse/low-degree windows on a density-1
  set of n force h to be switch-sparse or 2-regular globally" — is exactly the
  unsupported transfer that killed mahler-2kernel-automaticity. The e_{2^m}
  amplification witness (h = e_{2^m}: wt(h)=1 but wt(Φ_n h)=n−O(1)) shows sparse
  input with LINEAR fold weight, so the converse implication the classification
  needs (sublinear fold weight ⇒ structured input) has no supporting instance, and
  the positive witnesses all run the wrong way. Nothing in the sparse-polynomial
  literature supplies a global transfer from local window ANF-weight to a global
  description of an infinite string.

first-step: >
  (parked — the decisive count is already available and rules the route out
  before execution.) tool_builder could still machine-verify the *identity*
  direction (T(n,d)=a_d at n=8..64), which is worth having as a checked claim and
  a negative control, but it cannot rescue the classification: the enumeration in
  the original first step (strings h with wt(Φ_n h) ≤ εn at small n) would
  reproduce exactly the measured Thue-Morse / anti-dyadic witnesses and confirm
  that low fold weight coexists with richly-structured (not sparse-low-degree)
  windows. Run it if a checked ANF dictionary is wanted; do not rest any proof
  route on it.
```

## Research verdict (grounding check)

**The reformulation is named and the sparse-polynomial theory is real and
well-developed — but it applies at the wrong scale. At the window's own variable
count a counterexample's ANF is dense, not sparse, so the classification engine
cannot engage; and the remaining local-to-global step is the same unsupported
transfer that already killed the mahler-2kernel route.**

**The scale count (the killer).** The window `τ_n` is a Boolean function on
`m = ⌈log₂ n⌉` bits, so it can have at most `2^m = n` ANF monomials, and its ANF
weight is exactly `ν₂(n)`. A counterexample gives `ν₂(n) = o(n)`, i.e. up to
`o(2^m)` monomials — for instance `~2^m/m`. Relative to the `2^m`-dimensional
monomial space, that is a *dense* (almost full) family, not sparse. The route's
engine is `deg f ≤ log₂(#monomials)`; with `#monomials = ε·2^m` this gives degree
`m + log₂ ε`, within an additive constant of the maximum degree `m`. So the
conclusion "low algebraic degree, few low-degree factors" does not follow — a
degree-`(m−O(1))` polynomial with a constant fraction of all monomials is a
generic unstructured Boolean function. The sparse-polynomial theorems found
(Chattopadhyay–Dahiya–Lovett sparsity rigidity; the sparse-learning recovery
bounds) all concern genuinely sparse representations with polynomially many
monomials (s ≪ 2^n), and none transfers to the dense `Θ(2^m/m)` regime a
counterexample occupies.

**The local-to-global step (independent second defect).** Even a low-degree
conclusion on each window would not imply the global classification "h is
switch-sparse or 2-regular": that transfer is precisely the unsupported step that
closed `mahler-2kernel-automaticity` (sparse local windows on a density-1 set do
not force a global structural description of the infinite string). The `e_{2^m}`
amplification witness shows a *sparse* input with *linear* fold weight — the
converse the classification needs (sublinear fold weight ⇒ structured input) has
no supporting instance and the witnesses run the wrong way.

**Does it reopen a closed door?** It is a repackaging of a closed door: the "h is
structured" family (door 3's aperiodicity and door 4's 2-regularity), guarded by
the same failed local-to-global transfer. Not a new ground. As a route to SUPPLY
or to the SUPPLY⇔switch equivalence: **refuted**, on evidence (the scale count),
not on absence.

## Sources
- Chattopadhyay, Dahiya, Lovett, "Restriction Trees for Sparsity and Applications",
  STOC 2026, DOI 10.1145/3798129.3800895.
- "Learning sparse Boolean polynomials", IEEE ISIT (2013),
  https://ieeexplore.ieee.org/document/6483472.
- Carlet et al., "Bounds for the average degree-k monomial density of Boolean
  functions", Cryptogr. Commun. (2025), DOI 10.1007/s12095-025-00839-x; and
  "Probabilistic estimation of the algebraic degree of Boolean functions" (2023),
  DOI 10.1007/s12095-023-00660-4.
- Inside-workspace: supply-fold-submask-zeta-involution; mahler-2kernel-automaticity
  (refuted, same transfer); anf-mobius-reed-muller (refuted as a route).
