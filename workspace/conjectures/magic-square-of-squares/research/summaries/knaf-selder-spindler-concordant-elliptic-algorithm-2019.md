# Knaf, Selder & Spindler, "An Algorithm to Find Rational Points on Elliptic Curves Related to the Concordant Form Problem" (2019)

**Source:** arXiv:1907.02148v1 [math.AG], 03 Jul 2019. Full text at
`research/sources/knaf-selder-spindler-concordant-elliptic-algorithm-2019.html.full.md`.

## What it is

An algorithmic companion to Selder–Spindler 2014. It develops an explicit algorithm to
**find rational/integer points** on the elliptic curves E_{M,N}: y² = x(x+M)(x+N)
(M = pk > 0, N = −qk < 0, (p,q)=1, k squarefree) that correspond, via the concordant-form
correspondence, to solutions of Euler's concordant form problem (and hence to 3-term
APs of rational squares). This is a *search tool for the AP-of-squares / congruent-number
side* of the MSS problem, not an obstruction.

## Method

1. **2-descent** on E_{M,N} with full 2-torsion: E(Q)/2E(Q) ↪ Q(S,2)×Q(S,2) via the
   components φ_i(P) = x(P)−e_i (squarefree reps). Homogeneous spaces
   Q_{e₁,e₂,e₃,b₁,b₂} = Q₁∩Q₂ in P³ parametrise classes of rational points. Only finitely
   many (b₁,b₂) need be checked.
2. **Newton/patent parametrization** of quadrics: a ternary diagonal quadric with one
   known solution is parametrized by quadratics; substituting into the second quadric
   gives a **quartic** in the parameters plus a squared variable — the "weak algorithm"
   then just loops over the parameter pair and tests whether the remaining quartic value
   is a perfect square (quadratic complexity in parameter height).
3. **Strong algorithm**: if a separated-variables solution with one coordinate zero
   exists (a condition NOT always satisfied — counterexample k ≡ 23 mod 24 primes), the
   quartic collapses to a biquadratic → a quadratic form in squared parameters, giving a
   second parametrization and a final quartics-in-one-variable search, ~2× the digit
   reach (up to ~70–80 decimal places on a short search).

## Grounded data it produces (verified-by-the-source)

- Table 1: smallest solutions of X²−kY²=Z², X²+kY²=W² for primes k ≡ 5 mod 8 (k congruent,
  rank 1), up to k = 613, with up to 79-digit coordinates (e.g. the k=373 solution with
  W₀ a 79-digit integer). **Each row is a 3-term AP of squares with step k**.
- Table 2: for the 2π/3-congruent numbers 2ℓ, ℓ ∈ {7,103,199}, the rank-2 curves
  y² = x(x+2ℓ)(x−6ℓ) with three independent concordant-form solutions each (2-descent
  triplets (1,2,2),(2,−3,−6),(2,−6,−3), the third being the group-sum of the other two).
- Explicitly shows **Concordant form solutions are plentiful and enormous**; the smallest
  nontrivial solution has no known height bound (the algorithm does not guarantee
  termination, and Lang's observation about solution size vs. discriminant is violated).

## Bearing on the 3×3 magic square of squares

- This is the *computational attack* side of the concordant-forms dictionary in
  Selder–Spindler 2014. It confirms that **finding a single AP of squares with a given
  step is routine and its smallest solution can be astronomically large** — which frames
  why the MSS problem is so hard: an MSS requires FOUR such APs (steps u,v,u+v,u−v)
  sharing one middle term e², and each individual AP can be satisfied by huge but
  computable numbers. The obstruction is the simultaneous satisfaction of all four with
  additively-linked steps, which is exactly the additive relation the run's Φ-reduction
  (`phi-no-triple-m400`, no additive triple in Φ to m,n≤400) attacks.
- The 2-descent form here (x−e₁=A₁α² etc.) is the same homogeneous-space structure as
  the run's `simultaneous-congruent-numbers-2selmer` approach (already **refuted** in
  `research/APPROACHES.md` as subsumed by Bremner II's K3 data). This paper adds no new
  obstruction, only a concrete point-finding engine.

## Net assessment

`precedent` for any proposal that re-uses 2-descent on the four congruent-number curves
(Bremner's K3 already encodes all that data). Useful as the citation that **single-AP
concordant-form solutions are computable and large**, framing the four-AP
simultaneity as the crux. Does not resolve the additive-relation obstruction.

```claim
id: concordant-single-ap-solutions-computable-large
statement: For the congruent-number curves E_{M,N}: y²=x(x+M)(x+N) (M=pk>0, N=−qk<0, (p,q)=1, k squarefree), an explicit quadratic-complexity 2-descent + quadric-parametrization algorithm finds smallest concordant-form solutions (equivalently smallest 3-term APs of rational squares of a given step) whose coordinates can reach 70–80 digits quickly; no termination/height bound is known.
hypotheses: E has full 2-torsion; the strong algorithm additionally needs a separated-variables solution with one coordinate zero (fails, e.g., for primes k≡23 mod 24).
holds-here: yes — frames why four simultaneous APs is hard: each individual AP is satisfiable by computable but astronomically large coordinates; only the shared-middle/additive-link constraint is the obstruction.
evidence: source computation (Knaf–Selder–Spindler Table 1: primes k≡5 mod 8 up to 613, up to 79-digit coordinates; Table 2: rank-2 2π/3-congruent 2ℓ examples with three independent solutions).
bearing: precedent against re-deriving the 2-descent machinery (subsumed by Bremner II K3 data per simultaneous-congruent-numbers-2selmer refutation); no new obstruction.
anchor: research/summaries/knaf-selder-spindler-concordant-elliptic-algorithm-2019.md
```
