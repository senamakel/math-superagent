# Newton-series support: the fold rows are single-direction difference operators

```approach
idea: > Φ_n's d-th row is exactly the d-th iterate of the unit difference operator
  (1+σ)^d acting on the window, so ν₂(n) = wt(Φ_n h) is precisely the number of
  nonzero Newton-series (binomial-basis) coefficients c_d = Δ^d h(0) of the
  window's polynomial representation: h(x) = Σ_d c_d · C(x, d). SUPPLY says the
  prime switch window has a linear number of nonzero Newton coefficients.
mechanism: > Over F_2, (1+σ)^d h = Σ_{o⊆d} h[·+o] by Lucas, so the fold cell
  T(n,d) = ((1+σ)^d h)[n−1−d] IS the d-th finite difference of the window.
  This is the natural basis of the problem — it is NOT the Walsh/Reed–Muller
  (Hadamard) basis of the refuted ANF route and NOT the multi-direction U^k
  norm of the refuted Gowers route: it is the single-direction, all-orders
  difference sequence (the Pascal/binomial transform, umbral calculus). The
  engine is the classical rigid dichotomy of finite differences: Δ^d h ≡ 0
  ⟺ h is a polynomial of degree < d (over F_2, a polynomial in x of degree
  < d). A quantitative inverse statement — if the Newton support of the window
  has density o(1) (equivalently ν₂(n)=o(n)) for all n on a density-1 set, then
  the windows are approximated by FIXED low-degree polynomials, hence the
  infinite prime switch string is a low-degree 2-adic/nil sequence — would turn
  SUPPLY into the statement "the prime switch string is not eventually a
  low-degree polynomial in the prime index." That input is strictly weaker than
  switch density and is priced by the run's existing kernel/dyadic-collapse
  facts: degree-0 (constant) is exactly ker span(all-ones), degree-1 is
  span(even-alt, odd-alt), and eventual 2-periodicity (= degree ≤1 over F_2) is
  closed door 4's dyadic collapse.
status: refuted

killed-by: >
  BASIS IDENTITY. Over F_2 the "Newton/binomial basis" this candidate
  advertises as its distinguishing feature is the SAME coordinate system as the
  Möbius/Reed–Muller (ANF) basis of the already-refuted
  `anf-mobius-reed-muller` route. The classical identity is: for a function
  g : {0,…,n} → F_2, the Newton coefficient c_d = Δ^d g(0), where Δ = (1+σ) is
  the unit forward difference, equals c_d = Σ_{o≤d} C(d,o)(−1)^{d−o} g(o) =
  Σ_{o⊆d} g(o) mod 2 — the last equality by Lucas (C(d,o) ≡ 1 mod 2 iff o is a
  bitwise submask of d) and (−1) ≡ 1 over F_2. That sum IS the Möbius/ANF
  coefficient a_d for the subset indexed by the binary expansion of d. So the
  Newton support and the ANF support are literally the same multiset of
  coefficients. And the fold cell T(n,d) = (1+σ)^d h[n−1−d] = Σ_{o⊆d} h[n−1−d+o]
  = Σ_{o⊆d} r(o) for the reversed window r(t) = h[n−1−t] (substituting
  o ↦ d−o, a bijection on submasks) equals Δ^d r(0). Hence ν₂(n) is the
  Newton/ANF support of the single reversed window — exactly what the ANF route
  already established (claim supply-fold-submask-zeta-involution). The route is
  therefore a change of NAME, not of ground: it needs the same quantitative
  inverse the ANF route could not obtain.
  TWO LOAD-BEARING GAPS NO SOURCE FILLS. (i) The dichotomy Δ^d h ≡ 0 ⟺
  deg h < d is about a SINGLE window h with ALL differences of order ≥ d
  vanishing; it does NOT engage the candidate's counterfactual hypothesis,
  which is that the Newton/ANF support has density o(1) (equivalently
  ν₂(n) = o(n)) on a density-1 set of windows — a density condition on
  NONZERO coefficients, not a degree bound. No theorem turns "density-o(1)
  nonzero Newton coefficients, window by window" into "the infinite string is
  (eventually) a low-degree polynomial", and over F_2 the Frobenius structure
  (1+σ)^{2^j} = 1+σ^{2^j} makes the operator periodic in d, so the window
  support is not a clean size-by-degree object. (ii) The promised "strictly
  weaker than switch density" arithmetic input (eventual non-low-degree) is the
  claims `mahler-2kernel-contrapositive-refuted` / closed-door positions all
  over again: low-degree 2-adic/nil structure is a GLOBAL rigidity whose denial
  no sparse-window-density premise reaches. Refuted for the same reason
  `anf-mobius-reed-muller` and `sparse-anf-structure-classification` were
  refuted. Nothing here reproduces a settled claim that the ANF basis does not
  already reproduce — so even the Scholze gate adds no new ground.

precedent: >
  - Claim on disk already stating the identity: `supply-fold-submask-zeta-`
    `involution` (T(d) = XOR_{s⊆d} τ[s] is the F_2 zeta/Möbius transform,
    self-inverse); `linearisation-fold-weight` (ν₂ = wt(Φ_n h)).
  - The Newton-coefficient = submask-XOR identification is standard: Lucas's
    theorem (Mestrovic survey on disk, mestrovic_lucas_theorem_survey) gives
    C(d,o) ≡ 1 mod 2 iff o ⊆ d, and Δ^d g(0) = Σ_o C(d,o)(−1)^{d−o}g(o) is the
    classical k-th finite difference at 0 (umbral/Newton-series calculus). Over
    F_2 this coincides with the Möbius/ANF coefficient; see the Boxall–Keller /
    ANF literature cited on `anf-mobius-reed-muller` (Springer
    s12095-023-00660-4; arXiv:2004.11146).
  - No source was found establishing a QUANTITATIVE inverse "sparse Newton
    support on a density-1 set ⟹ eventual low-degree/nil" over F_2 — the gap
    the mechanism requires. Searches: "finite differences sparse support
    polynomial rigidity inverse theorem", "Newton coefficients Boolean
    functions", "quantitative inverse finite difference low degree F2".
  - The Frobenius collapse (1+σ)^{2^j} = 1+σ^{2^j} over F_2, which is what the
    candidate flags as its extra structure, is a computational fact of the
    difference operator; it makes COLLAPSES (DING) more likely, not the desired
    rigidity — the collapse witnesses of the closed doors are exactly the
    inputs where these powers annihilate (all-ones degrees 2^j vanish), which is
    why the Newton reading reproduces closed door 1 (all-ones = degree-0,
    ν₂ = O(1)) rather than escaping it.

  Newton coefficients c_d = Δ^d h(0) three independent ways (brute submask XOR,
  the Pascal-matrix inverse, and the direct recurrence c_d = c_{d−1} + σ c_{d−1})
  and assert they equal the fold row cells up to the known shift/reversal. Then
  print the Newton-support profile (which orders d contribute) for the prime h,
  all-ones, and Thue–Morse, and check the claimed dichotomy on the two controls:
  all-ones has support {0} (degree 0), Thue–Morse has sublinear but not O(1)
  support (its failure to be exactly low-degree is what must be quantified).
falsifies: > (a) The Newton coefficients of the window are NOT the fold cells up to
  shift/reversal — then the natural-basis claim is wrong and the route is a
  relabeling with no engine. (b) The quantitative inverse "sublinear Newton
  support on a density-1 set ⟹ eventual low-degree/nil structure" fails to exist
  as a theorem (or fails over F_2 where the difference operator has the extra
  Frobenius structure (1+σ)^{2^j} = 1+σ^{2^j}) — then the dichotomy is not
  available and the route reduces to relabeling like the ANF route.
scholze-gate: > Reproduces on disk: `fold-rank-is-n-2-nullity-2-alternating`
  (ker = degree ≤1 part = span(even-alt, odd-alt)), closed door 1 (all-ones =
  degree-0 polynomial, ν₂=O(1) exactly), closed door 4 (2-periodic/anti-dyadic
  inputs = degree ≤1, ν₂∈{1,2}), and the dyadic-collapse fact (eventually
  2-periodic ⟹ ν₂=O(1)). The Newton basis is the basis in which every one of
  these settled classes is the statement "low degree ⟹ small support," so the
  new setting reproduces them by construction.
```

## Why this is not the refuted ANF / Gowers / Mahler routes

- **Not ANF (`anf-mobius-reed-muller`, refuted):** that route used the
  Reed–Muller / Walsh (Hadamard) basis and mounted the open RM weight-spectrum
  problem. The Newton/binomial basis is a *different* basis — it is the basis
  in which Φ's own rows are elementary, so the weight is the support in the
  problem's natural coordinates, not a foreign spectrum.
- **Not Gowers U² (`gowers-u2-nilsequence-uniformity`, refuted):** that route
  used the Walsh-phase U² norm and the Green–Tao inverse theorem in the wrong
  (Walsh) basis. Here the object is the single-direction difference sequence
  (1+σ)^d, one order d at a time, not the averaged multi-direction U^k norm,
  and no nilsequence orthogonality is claimed — only the polynomial
  dichotomy Δ^d h = 0 ⟺ deg h < d.
- **Not Mahler 2-kernel (`mahler-2kernel-automaticity`, refuted):** that route
  needed the 2-kernel (all dyadic subsequences) to be finite-dimensional. The
  Newton support is a different, weaker rigidity — it lives on one window at a
  time and its vanishing forces polynomial (not merely automatic) structure.

The genuinely speculative half is the *quantitative* inverse theorem over F_2,
where Frobenius makes (1+σ)^d periodic in d (d and d XOR 1 collide when the
highest bit matches, so the operator is a product over set bits of (1+σ^{2^i})).
Whether "sublinear support on a density-1 set of windows ⟹ eventual
low-degree/nil structure" holds in this Frobenius-twisted setting is precisely
what research must check; if it fails, this is a relabeling and should be
refuted like ANF was.
