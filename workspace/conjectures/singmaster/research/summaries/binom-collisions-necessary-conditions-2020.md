# Yamada 2020 — Necessary conditions for binomial collisions (PRIMARY)

Source: T. Yamada, "Necessary conditions for binomial collisions", arXiv:2002.07043
(Feb 2020). Full text read: `research/sources/binom-collisions-necessary-conditions-2020.full.md`.
URL: https://arxiv.org/pdf/2002.07043

## What the paper establishes

Study the collision equation in the **edge regime** where `y ≈ 2n` (b near y/2).
Write `y = 2n+δ` (δ=0,1), `x = 2n+l` (l > δ), `m = n−b`, `k = n−a`, so
`0 ≤ m < k < n/2` and the collision is

    (4)   C(2n+δ, n−m) = C(2n+l, n−k).

**Theorem 1.1.** If (4) holds with `0 ≤ m < k < n/2`, `m ≤ 0.735k`, then

    l > n(1.3132 log₂(2n) − 2.00271);

and for any `c < 0.68943`, `l > (cn/log n)^{40/21}` for sufficiently large n.
(Constants come from Dusart's explicit π(x) estimates and Robbins' Stirling
bounds; the exponent 40/21 = 2·20/21 from Baker–Harman–Pintz
`p_{n+1}−p_n ≪ p^{0.525}`.)

**Method (the part that matters):**
- Lemma 2.3: the largest prime factor of a product of the two blocks of
  consecutive integers `∏(n−i₁)·∏(n+i₂)` is `≤ k₀ = 2(k+l)−δ−1`. This is the
  engine: two equal products force all primes in both intervals to be small.
- The proof shows `l ≥ 0.001n` always, then uses prime gaps: if `l ≥ 0.001n`
  there is a prime in `[2n+δ+1, 2n+l]`; that prime must divide one of the
  `n+i` — forcing `l−t < (2n+l)/log³(2n+l)` and hence the log₂ bound; the
  BHP prime-gap bound upgrades `(cn/log n)^{40/21}`.
- The `m ≤ 0.735k` hypothesis is the "near the edge" condition: it means the
  two binomial rows are close together (both `n`-blocks overlapping).

**Generalization stated (Section 1):** the argument shows that for any constants
`η < 1` and `c < 0.68943`, (4) has only finitely many solutions with `m ≤ ηk`
and `l < (cn/log n)^{40/21}`. **Cramér's conjecture** would replace the exponent
by `exp(c₂√n)`.

**Converse difficulties (the wall):** "it seems difficult to obtain a general
result for (4) in cases such as m ∼ k but k−m→∞, and l > exp(n^A) with A>1/2.
Even specific equations such as `C(2n,n)=C(y,2)` seem to be far beyond present
techniques."

## Bearing for this run

- This is the **only held source giving quantitative necessary conditions
  inside the boundary regime** `2 ≤ k ≤ (log t)/(log₂t)^{3/2−ε}` that MRSTT
  leaves open. It does NOT bound N(a) (it needs the two representations to be in
  the same near-edge configuration `m ≤ 0.735k` and only forces the row-distance
  l to be large), so it is a partial structural tool for the boundary, not a
  multiplicity bound.
- The `C(2n,n)=C(y,2)` remark is a sharp statement of how hard even the simplest
  remaining boundary case is: no technique touches it.
- It corroborates the run's "boundary is where nothing effective is known" thesis
  with an actual theorem: for edge-adjacent collisions the rows must be far apart
  (`l ≫ (n/log n)^{40/21}`), so any multiplicity in the boundary needs the
  representations spread over different `(m,k)` scales, not clustered.
- **Not load-bearing for any existing claim**, and it does not change the
  uniform-in-(k1,k2) verdict — the necessary condition is effective but
  per-configuration (depends on k,m,n,δ and the Cramér-scale), not uniform.
- Warning: the paper's δ=0/1 covers `y=2n` or `2n+1`; the infinite Fibonacci
  family has `x/y→φ²≈2.618`, so it is NOT in this near-edge configuration —
  the theorem says nothing about the family that drives B≥6, consistent with
  the family being interior (row ratio ~2.618, not ~2).

## Claim

```claim
id: yamada-boundary-necessary-condition
statement: Yamada 2020 (arXiv:2002.07043, Thm 1.1): if C(2n+delta,n-m) =
  C(2n+l,n-k) with delta in {0,1}, 0 <= m < k < n/2, m <= 0.735k, then
  l > n(1.3132 log_2(2n) - 2.00271), and for n large, l > (cn/log n)^{40/21}
  for every c < 0.68943. Method: largest-prime-factor of the two products is
  <= k_0 = 2(k+l)-delta-1 (Lemma 2.3); prime-gap argument then forces l large.
  The same argument gives finiteness of solutions with m <= eta k and
  l < (cn/log n)^{40/21} for any eta<1, c<0.68943; Cramer's conjecture would
  give exp(c_2 sqrt n). Edge equations like C(2n,n)=C(y,2) are stated as far
  beyond present techniques.
hypotheses: fixed near-edge configuration; n sufficiently large (n >= 500000 used
  inside); m <= 0.735k.
holds-here: yes as a boundary-regime structural fact (the MRSTT small-m boundary
  is exactly where m/k can be small); the theorem does not apply to the infinite
  Fibonacci family (row ratio ~phi^2 ~ 2.618, not ~2) and does not bound N(a).
status: asserted-by-source (primary full text read; constants and inequalities
  quoted from the paper, not re-derived)
bearing: gives the only held quantitative necessary condition inside the
  MRSTT-open boundary regime; confirms the boundary is where the difficulty lies
  (even C(2n,n)=C(y,2) is out of reach); still per-configuration, not uniform.
anchor: research/sources/binom-collisions-necessary-conditions-2020.full.md
```