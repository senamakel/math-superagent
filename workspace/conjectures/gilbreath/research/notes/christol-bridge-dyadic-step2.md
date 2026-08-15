# Christol bridge for the dyadic thread's step (2) — landed

The adopted approach `dyadic-linear-complexity-supply` names its unmet research
step (2) as:

> Pin the named theorem "the F₂ subset-zeta transform preserves 2-automaticity"
> (Christol / automatic-sequences literature): ζ is an F₂-linear substitution
> x ↦ x/(1+x) on the generating function, so it should preserve the class of
> 2-automatic (= algebraic over F₂[[x]]) sequences.

This is now grounded. The two Christol primary sources are in the library:

- **Kedlaya 2006**, *Finite automata and algebraic extensions of function
  fields*, J. Théor. Nombres Bordeaux 18(2):379–420, doi 10.5802/jtnb.551
  (open access). Full text:
  `research/sources/kedlaya-2008-finite-automata-algebraic-function-fields.full.md`.
  States **Christol's theorem as Thm 4.1.1**: over 𝔽_q (q = p-power), the series
  Σ a_i t^i ∈ 𝔽_q[[t]] is algebraic over 𝔽_q(t) **iff** (a_i) is p-automatic.
  Generalises to p-quasi-automatic generalised Laurent series (Thm 4.1.3).
  Bibliography anchors Allouche–Shallit, *Automatic Sequences* (CUP 2003) — the
  standard encyclopedic treatment of p-automatic sequences/kernels.

- **Adamczewski–Bostan–Caruso 2023**, *A sharper multivariate Christol's
  theorem*, arXiv:2306.02640. Full text:
  `research/sources/adamczewski-bostan-caruso-2023-sharper-multivariate-christol.full.md`.
  Multivariate Christol with section-operator invariance (Thm 1.2 / Prop 4.2)
  and explicit automaton-state-complexity bounds — the machinery tuned to the
  subset-zeta / Möbius / rational-substitution action.

## The closing inference (the run's own, grounded on the above + bcz-2023)

- [held, proved] `bcz-2023-left-edge-stabilization`: over 𝔽₂[[X]], the
  left-edge operator of the Proth–Gilbreath triangle is
  `T(f)(X) = f(X/(1+X))·(1/(1+X))` and `T² = id`. This is the generating-
  function action of the F₂ subset-zeta (Möbius) transform.
- [source] Christol: 2-automatic ⟺ algebraic over 𝔽₂(t) (Kedlaya Thm 4.1.1).
- [standard closure] composition of an algebraic function with a **rational**
  function is algebraic; the algebraic functions over 𝔽₂(t) form a field closed
  under it.
- **Conclusion:** the F₂ subset-zeta image of a 2-automatic bit string is again
  2-automatic. Hence if the prime switching bit h is 2-automatic, so is its
  zeta-dual ζ(h) — the object whose positive density is exactly the supply
  bound ν₂ ≥ c·n.

**Status: the identification of the subset-zeta transform with the bcz
rational substitution, and the automaticity-preservation inference, are the
run's own and are NOT machine-verified here.** They rest on (a) the bcz-2023
identity (proved in that note) and (b) the Christol sources (asserted-by-source).
The step that still must NOT be skipped: confirm by a program (or a careful
generating-function computation) that the F₂ subset-zeta transform really acts
as t↦t/(1+t) on the generating function — i.e. that computing ζ(h) in the
subset lattice agrees with substituting t/(1+t) in Σ h[j] t^j. If that holds,
a 2-automatic h (e.g. any eventual-periodic or Thue–Morse switch bit) has
2-automatic ζ(h), so its density is either 0 or ≥ c>0 (automatic sequences
have rational limiting densities) — which would give the dichotomy
"density(ζ(h)) ∈ {0} ∪ [c,1]" for the whole automatic class, the transferable
half of the dyadic separation.

Recorded so the dyadic thread's step (2) is no longer an ungrounded
assumption, and the "confirm ζ ≡ t↦t/(1+t) generating-function substitution"
is the deliberate next check, not a skipped one.

```claim
id: subset-zeta-preserves-automaticity-christol
statement: The F2 subset-zeta (Mobius) transform preserves 2-automaticity of
  bit strings: if h is 2-automatic, so is its zeta-dual zeta(h). Grounding: by
  Christol's theorem (Kedlaya 2006 Thm 4.1.1; ABC 2023) a sequence over F2 is
  2-automatic iff its generating function is algebraic over F2(t); the
  subset-zeta transform acts on the generating function by the rational
  substitution t -> t/(1+t) (times (1/(1+t))), the bcz-2023 left-edge identity
  T(f)(X) = f(X/(1+X))·(1/(1+X)) with T^2 = id; rational substitution preserves
  algebraicity, hence automaticity. Corollary: any 2-automatic switch bit h
  (eventual-periodic, Thue-Morse) has zeta(h) with rational limiting density,
  i.e. density(zeta(h)) in {0} or >= c > 0 - the transferable dichotomy shape.
hypotheses: 2-automatic bit string over F2; F2 subset-zeta transform;
  Christol's theorem; bcz-2023 left-edge involution.
holds-here: yes (2-automatic class contains the periodic/dyadic and Thue-Morse
  collapse witnesses; the rational-closure fact is standard)
status: asserted - the identification of zeta with the bcz rational
  substitution, and the automaticity-preservation step, are the run's own and
  NOT machine-verified; they rest on the two Christol sources (asserted-by-
  source) + bcz-2023 (proved in that note).
bearing: grounds step (2) of dyadic-linear-complexity-supply - turns "prime h
  is 2-adically non-rigid, zeta(h) has positive density" into a statement
  transferable through the automatic-sequences literature; does NOT close
  G-supply (nu2 >= c*n for the aperiodic primes stays named-open; zeta(h)
  positive density is the combinatorial supply, not yet attached to the primes).
anchor: research/notes/christol-bridge-dyadic-step2.md;
  research/sources/kedlaya-2008-finite-automata-algebraic-function-fields.full.md;
  research/sources/adamczewski-bostan-caruso-2023-sharper-multivariate-christol.full.md
falsifier: a machine check showing zeta does NOT act as t -> t/(1+t) on the
  generating function (i.e. subset-zeta computation disagrees with the rational
  substitution), which would break the automaticity-preservation inference at
  its mechanism step.
```

