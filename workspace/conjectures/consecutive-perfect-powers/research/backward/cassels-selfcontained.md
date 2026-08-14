# Cassels's divisibility theorem, self-contained (no external source)

This skeleton decomposes Cassels's theorem — the entry point to every
divisibility condition downstream — into lemmas that can each be attacked
in-workspace. It exists because the other skeletons' `next` for this theorem
says "librarian fetches Cassels 1960", and fetching is dead at the network
layer (see CONTEXT.md, Workspace character). Nothing here needs a source;
each gap has a runnable first move.

```skeleton
goal: If x^p - y^q = 1 with x, y > 0 and p, q distinct odd primes, then p | y and q | x.
implies: |
  Let (x, p, y, q) be a solution with p, q distinct odd primes. Rewrite the
  equation as x^p - 1 = y^q. In the cyclotomic ring Z[zeta_p], zeta_p a
  primitive p-th root of unity,

      x^p - 1 = (x - 1) * prod_{i=1}^{p-1} (x - zeta_p^i) = y^q.

  G-cv-cyclo-coprime says the ideals (x - zeta_p^i), i = 1,...,p-1, are
  pairwise coprime off the unique ramified prime (1 - zeta_p): for i != j,
  gcd((x - zeta^i), (x - zeta^j)) is supported only on (1 - zeta_p), because
  zeta^i - zeta^j is a unit times (1 - zeta_p). Since the product is the
  q-th-power ideal (y)^q, each factor ideal (x - zeta^i) is a q-th power
  times a power of (1 - zeta_p); summing (1 - zeta_p)-adic valuations gives
  an identity in which the left side is v_p(x^p - 1) and the right side is
  q * v_p(y). G-cv-vp-transfer states this identity precisely and shows its
  only integral solution has v_p(y) >= 1, i.e. p | y. Its elementary core is
  G-cv-lte (the minus form), which controls v_p(x^p - 1) in terms of
  v_p(x - 1). The mirror rewriting y^q + 1 = x^p, factored as
  (y + 1) * prod_{j=1}^{q-1} (y + zeta_q^j) in Z[zeta_q], applies
  G-cv-lte (plus form) and G-cv-vq-transfer to force q | x. Both halves
  together are exactly Cassels's conclusion.
  Known solution: (3, 2, 2, 3) has p = 2 even, so it is excluded by the
  odd-prime hypothesis; and even outside the hypothesis the conclusion is
  consistent — p | y is 2 | 2 and q | x is 3 | 3. Nothing here refutes it.
status: sketched
rests-on: none — research/CLAIMS.md is empty, no claim ids established
killed-by: (none)
```

```gap
id: cv-lte
lemma: >
  Lifting-the-exponent (both signs). For an odd prime r and integers a, b
  with r | (a - b) and r ∤ ab: v_r(a^r - b^r) = v_r(a - b) + 1. Equally, for
  r | (a + b) and r ∤ ab: v_r(a^r + b^r) = v_r(a + b) + 1. The special cases
  needed are b = 1: v_p(x^p - 1) = v_p(x - 1) + 1 when p | x - 1 and p ∤ x,
  and v_q(y^q + 1) = v_q(y + 1) + 1 when q | y + 1 and q ∤ y.
status: open
next: >
  theorem_prover / lean_prover: state and prove the general LTE identity by
  expanding a^r = ((a - b) + b)^r via the binomial theorem and reading off the
  valuation of the r (a - b) b^{r-1} term; report #print axioms, no sorry.
  In parallel symbolic_math verifies both sign forms on ~100 concrete (r, a, b)
  by exact integer arithmetic. This is pure elementary number theory — no
  source needed, and it is the core that G-cv-vp-transfer and G-cv-vq-transfer
  reduce to.
```

```gap
id: cv-cyclo-coprime
lemma: >
  In Z[zeta_p] (p an odd prime), for distinct i, j in {1,...,p-1} the ideals
  (x - zeta_p^i) and (x - zeta_p^j) have gcd supported only on the ramified
  ideal (1 - zeta_p); explicitly, zeta_p^i - zeta_p^j is a unit times
  (1 - zeta_p), so (x - zeta^i) - (x - zeta^j) = zeta^j - zeta^i is divisible
  by (1 - zeta_p) and by nothing else that can be common to both factors.
status: open
next: >
  symbolic_math: for small odd p and concrete x (say p <= 11, 2 <= x <= 30),
  compute gcd((x - zeta^i), (x - zeta^j)) in Q(zeta_p) and confirm it is a
  power of (1 - zeta_p) up to a unit, for all pairs i != j; the unit factor
  zeta^i - zeta^j is verified once symbolically. theorem_prover then formalises
  "zeta^i - zeta^j = unit * (1 - zeta_p)" — a one-line cyclotomic identity
  (zeta^a - 1 = (zeta - 1)(zeta^{a-1} + ... + 1)). No source needed.
```

```gap
id: cv-vp-transfer
lemma: >
  The valuation-transfer descent, p | y half. Let x^p - 1 = y^q with p, q
  distinct odd primes, x, y > 0. From G-cv-cyclo-coprime, each ideal
  (x - zeta_p^i) is a q-th power times a power of (1 - zeta_p); the resulting
  (1 - zeta_p)-adic valuation identity — built from G-cv-lte's minus form
  v_p(x^p - 1) = v_p(x - 1) + 1 on the case p | x - 1, and the trivial
  v_p(x^p - 1) = v_p(x - 1) = 0 when p ∤ x - 1 — forces v_p(y) >= 1.
  Concretely: v_p(x^p - 1) = q * v_p(y), and the coprimality/descent argument
  rules out v_p(x^p - 1) = 0, i.e. forces p | y.
status: open
next: >
  symbolic_math: first pin the exact valuation identity — compute, for small
  odd p, q and hypothetical x, y with x^p - 1 = y^q (there are none at small
  size, so compute the valuation of prod_{i=1}^{p-1}(x - zeta^i) symbolically
  and read off its (1 - zeta_p)-adic valuation), and confirm it equals
  q * v_p(y). This discovers the precise identity that G-cv-vp-transfer states;
  the descent that rules out the p ∤ y branch (compare (x - zeta) with its
  conjugate (x - zeta^{-1})) is then handed to theorem_prover. The known
  solution is consistent: with p = 2 the hypothesis fails, and 2 | y = 2 holds
  anyway, so nothing is refuted.
```

```gap
id: cv-vq-transfer
lemma: >
  The mirror valuation-transfer descent, q | x half. Let y^q + 1 = x^p with
  p, q distinct odd primes, x, y > 0. Factoring y^q + 1 = (y + 1) *
  prod_{j=1}^{q-1}(y + zeta_q^j) in Z[zeta_q], the same coprimality and
  (1 - zeta_q)-adic comparison — with G-cv-lte's plus form
  v_q(y^q + 1) = v_q(y + 1) + 1 on the case q | y + 1 — forces v_q(x) >= 1,
  i.e. q | x.
status: open
next: >
  symbolic_math: mirror the cv-vp-transfer computation in Q(zeta_q) for small
  odd q, p — compute the (1 - zeta_q)-adic valuation of prod_j (y + zeta_q^j)
  and confirm it equals p * v_q(x), pinning the exact identity. theorem_prover
  then formalises the descent that rules out the q ∤ x branch. Known solution:
  q = 3 | x = 3 holds, and the odd-prime hypothesis fails at p = 2, so
  nothing is refuted.
```

**Inference check.** The two transfer gaps are the real content of Cassels; the
LTE gap is the elementary core they reduce to, and the cyclotomic-coprimality
gap is the structural fact the transfer rests on. LTE and cyclotomic coprimality
are both attackable today with zero dependencies; the transfer gaps begin with a
symbolic_math discovery computation that pins their exact statement. This is
finer than the existing single gap `G-odd-cassels` / `G-Cassels`, whose `next`
pointed at a dead fetch.
