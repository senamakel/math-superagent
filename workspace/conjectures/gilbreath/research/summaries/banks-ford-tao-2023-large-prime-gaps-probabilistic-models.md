<!-- source: https://link.springer.com/article/10.1007/s00222-023-01199-0 | Invent. math. 233 (2023) 1471–1518, open access CC BY -->
<!-- NOTE: the on-disk full file has the wrong filename research/sources/maier-pomerance-2023-...; the authors are BANKS, FORD & TAO. Read the header comment in that file. -->

# Banks–Ford–Tao 2023, "Large prime gaps and probabilistic models" (Invent. math. 233:1471–1518)

## What this is and why the run needs it

This is the canonical peer-reviewed grounding of the **probabilistic prime models** that the
random-analogue approaches to Gilbreath (Chase 2024, Chase–Hunter–Tao 2026, the Tao Cramér-model
blog) take as input. It states precisely Cramér's 1936 model, Granville's refinement, and a new
random-sieve model, and gives the rigorous leading-order behaviour of the *largest prime gap* in
each. It is the standard reference for "gap behaviour under a random model", which is exactly the
assumption behind the CHT geometric-Cramér result and the Tao-blog 2-separated-set analysis. Held
in full; this summary extracts the load-bearing statements.

## Cramér's model (central object for the run's random-analogue side)

Each integer n ≥ 3 is selected for inclusion with probability 1/log n, jointly independent in n
(§1.1). Then with probability one (from Hoeffding/Bennett), the number of primes-like elements
below x is asymptotic to the true π(x), and the largest gap satisfies G_S(x) ~ log²x a.s. Cramér
1936 proved this and remarked that it suggests the same for the actual primes (whence "Cramér's
conjecture" G(p) = O(log²p)).

**Documented weaknesses of the Cramér model** (the reason a Gilbreath random analogue cannot just
cite it blindly):
- For any finite set H it predicts the Hardy–Littlewood prime-k-tuple count with singular series
  ≡ 1, which is FALSE for the primes (bias of primes mod p against the other residue classes); e.g.
  no n with n, n+1, n+2 all prime. §1.1, §2.5.
- Maier's phenomenon: the Cramér model predicts primes equidistribute in every short interval of
  length ≥ log²x, but the real primes have both liminf<1 and limsup>1 ratios (Maier 1985). This is
  *the* standing warning that a Cramér-type independence model overshoots what the primes actually
  do on global/intermediate scales. §2.5, Pintz 2007.

## Granville's model

For each dyadic interval (x,2x], discard n with (n,Q)>1 for Q = ∏_{p≤A} p (A = log^{1-o(1)}x), then
keep the rest with probability Q/(φ(Q) log n). This corrects the residue-class bias: it satisfies
the Hardy–Littlewood analogues. Its largest gap satisfies the *factor-ξ* law
G ~ ξ log²x with ξ = 2e^{-γ} = 1.1229... (eq. 1.3), bigger than Cramér's by the Granville factor —
this is what the run's "granville-lucas/sierpinski" instincts and the Keen/Granville 2026 notes rely
on.

## The new random-sieve model and its theorems

Model S (eq. 1.10): for z(t) the largest prime with 1/Θ_{z(t)} ≤ log t (z(t) ~ t^{1/e^γ}), S is the set
of integers surviving sieving by a random residue class modulo each prime p ≤ z(n). It is designed
to satisfy the Hardy–Littlewood conjectures for many-tuples, unlike Cramér's.

- **Theorem 1.1.** With probability one, the largest gap in S∩[1,x] is
  g((ξ±ε)log²x) for all large x, where g(u) = max{y : W_y log y ≤ u} and W_y is the interval-sieve
  extremal quantity (min over residue-class choices of |[0,y]∩S_{(y/log y)^{1/2}}|).
- **Conjecture 1.2.** The real primes have largest gap ~ g((ξ±o(1))log²x); under the folklore
  W_y ~ y/log y this is ~ ξ log²x.
- **Theorem 1.3 (uniform Hardy–Littlewood for the model).** For c ∈ [1/2,1), a.s. the model obeys
  the HL asymptotic with error O(x^{1-c}) uniformly over admissible tuples |H| ≤ log^c x.
- **Theorem 1.4 (RH for the model).** a.s. π_S(x) = li(x) + O(x^{1/2}log^c x), c>3/2.
- **Theorem 1.5/1.6.** Deterministic converse: *any* set of integers satisfying a uniform
  Hardy–Littlewood-type conjecture has large gaps — the maximal gap length is tied to the range of
  uniformity (extends Gallagher 1976's exponential-normalized-gap distribution theorem).

Relevant tools the run can reuse: interval-sieve bounds on W_y (1.12), the sieve upper bound
(Lemma 3.1), Bennett/Azuma concentration, and the "gap j distribution" Poisson heuristic
(eq. 2.4: P(gap ≥ λ log p_n) → e^{-λ}).

## What it implies for this run

The CHT/Tao random-analogue side assumes a gap model; this paper is the clean, peer-reviewed
statement of what those models are and their documented failures at the k-tuple/short-interval
level. It does NOT resolve Gilbreath (none of these are about iterated absolute differences); but it
fixes the honest caveat for any "Cramér-model ⇒ Gilbreath" reasoning: the model differs structurally
from the primes (residue bias, Maier), so a random-analogue result is genuinely weaker than the
prime statement. Claim below.

```claim
id: bft2023-cramer-model-canonical
statement: (Banks–Ford–Tao 2023, Invent. math. 233:1471–1518) Cramér's model (each n≥3 in with prob 1/log n, jointly independent) gives largest gap ~ log^2 x a.s.; Granville's corrected model gives ~ xi log^2 x (xi=2e^{-gamma}=1.1229..); a new random-sieve model S (eq 1.10) gives g((xi±eps)log^2 x) a.s. (Thm 1.1), satisfies uniform Hardy-Littlewood (Thm 1.3) and RH (Thm 1.4), and any set obeying uniform HL has large gaps (Thm 1.5/1.6). Cramér's model fails on prime k-tuples (residue bias) and short intervals (Maier).
hypotheses: probabilistic models of the integers/primes; none needed by the Gilbreath operator itself.
holds-here: yes (this is the grounding for the random-analogue side; it does not itself settle Gilbreath)
status: proved (peer-reviewed Inventiones)
bearing: fixes the canonical probabilistic-prime-gap model underlying Chase 2024 / CHT 2026 / Tao random analogues, and records the documented ways a Cramér-type independence model differs from the real primes (so a random-model-to-Gilbreath transfer is heuristically supported, not rigorous). Also supplies the interval-sieve concentration tools (Lemma 3.1, Bennett/Azuma) the run can reuse.
anchor: research/sources/maier-pomerance-2023-large-prime-gaps-probabilistic-models.full.md (authors Banks, Ford & Tao — filename is a misnomer)
```

## Also available

- The Cramér original (Acta Arith. 2 (1936) 23–46, DOI 10.4064/aa-2-1-23-46) is cited and quoted
  here; its full text is unobtainable as text (scanned PDF over the conversion size cap on all
  routes) but its content is fully grounded through this paper + Chase 2024 + CHT 2026. See
  `research/summaries/cramer-1936-order-of-magnitude-prime-gaps.md` and
  `research/summaries/cramer-1937-prace-matematyczno-fizyczne-prime-gaps.md` for the repository
  records and full citation.
