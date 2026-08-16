# Grounding report: the three current proposals (Furstenberg-diagonal, log-Chowla, van der Corput)

Date: this run. Author: research role (grounding pass).

Task: take each of the inventor's three proposals to the literature and report
per candidate: what the reformulation is actually called, the precise statement
of any theorem it relies on and whether its hypotheses hold *here*, whether
anyone has applied it to this problem, and what it would buy — then set `status`
grounded or refuted with `killed-by`.

## Verdicts

- `spacetime-diagonal-furstenberg` — **refuted**. Furstenberg's hypothesis
  (rationality of the bivariate generating function) fails: the boundary that
  computes `ν₂(n)=wt(Φ_n h)` is the non-rational prime gap-parity string h.
- `log-chowla-entropy-decrement-switch` — **refuted**. Tao's entropy-decrement /
  log-averaged Chowla machine requires correlations of a bounded MULTIPLICATIVE
  function at affine-INTEGER shifts in its own index; the fold's switch products
  are correlations of χ at PRIME indices, and j↦χ(q_j) is not multiplicative in
  j. Same index-vs-value obstruction that has killed five prior routes.
- `vandercorput-differencing-excess` — **refuted**. The differencing identity is
  a real deterministic theorem, but it converts a first-moment bound into bounds
  on SHIFTED autocorrelations, which are the same switch-product correlations
  (second-moment) the squared-excess route already prices; for shifted windows
  the even-symmetric-difference evasion (no standalone switch sign) is not
  established, so the collapse to the switch-density parity barrier stands
  (directive 32).

---

## 1. `spacetime-diagonal-furstenberg` — refuted

### What the reformulation is actually called
Reformulate `ν₂(n)=wt(Φ_n h)` as the anti-diagonal row-sum of the 2-D F₂ fold
array `A_k(i)` (reduction of the absolute-difference triangle mod 2), reading the
anti-diagonal extraction as the **diagonal** operation on the bivariate
generating function `F(x,y)`, and applying **Furstenberg's theorem** (diagonal of
a rational bivariate power series is algebraic) plus an algebraic-growth
dichotomy.

### The theorems it relies on, and whether hypotheses hold here
- **Pólya 1922 / Furstenberg 1967** (diagonal ⟹ algebraic; converse):
  `f ∈ K[[t]]` is algebraic iff it is the diagonal of a bivariate rational power
  series. Confirmed in Bostan–Lairez–Salvy, "Multiple binomial sums", J.
  Symbolic Comput. 2016 (Thm 3.2), DOI 10.1016/j.jsc.2016.04.002; Bostan–Dumont–
  Salvy, "Algebraic diagonals and walks", JSC 2016, DOI 10.1016/j.jsc.2016.11.006;
  Y. Hu, arXiv:1505.01379. Real and exactly stated; the "diagonal ⟹ algebraic"
  direction is unconditional.
- **The hypothesis that fails**: Furstenberg needs **F(x,y) rational**. Over F₂
  a rational formal power series has eventually-periodic coefficients. The
  boundary that actually produces `ν₂(n)=wt(Φ_n h)` is the prime **gap-parity**
  string `h` (linearisation claim `linearisation-fold-weight`) — the string
  `h[j]=((q_{j+1}−q_j)/2) mod 2`. `F(x,y)` rational would force `h` eventually
  periodic, hence the primes eventually periodic — false (Shiu 2000, conditional;
  non-automaticity of the prime indicator: Hartmanis–Shank 1968 DO
  10.1145/321466.321470, Coons arXiv:0810.3709, Dubbe arXiv:2409.04314). The
  boundary the mechanism *names* is the raw-primes-mod-2 string `A_0(i)≡q_{i+1}
  mod 2`, which is essentially constant (odd primes ≡ 1) — rational but giving
  the trivial/incorrect object, not the gap-parity fold. Either reading blocks
  the theorem.
- **Secondary growth dichotomy** ("algebraic + o(n) on a density-1 set ⟹
  eventually periodic"): not established as stated for 2-automatic/F₂-algebraic
  sequences; but the rational-boundary obstruction decides the route
  independently, so this is not reached.

### Who has applied it to this problem
Nobody. Furstenberg diagonals are standard in combinatorial enumeration, but
never to force linear fold weight of the prime gap-parity string; the specific
claim "rational boundary" fails at the non-automaticity wall, the same wall that
closed `diagonal-2regular-automaton`.

### What it would buy
A route to "ν₂ algebraic + sublinear ⟹ eventually periodic"; but it is
unreachable because the boundary is non-rational. Refuted.

---

## 2. `log-chowla-entropy-decrement-switch` — refuted

### What the reformulation is actually called
Attack the switch-sign product correlations (the open gate from the adopted
squared-excess route) with Tao's **entropy-decrement** method and the
**logarithmically averaged Chowla / Elliott** machinery, aiming for a priority-2
input strictly weaker than switch density.

### The theorems it relies on, and whether hypotheses hold here
- **Tao 2016**, "The logarithmically averaged Chowla and Elliott conjectures for
  two-point correlations", Forum of Mathematics Pi, DOI 10.1017/fmp.2016.6,
  arXiv:1509.05422: for any bounded multiplicative `g` and fixed `a₁,a₂,b₁,b₂`
  with `a₁b₂−a₂b₁≠0`,
  `Σ_{x/ω<x<n≤x} g(a₁n+b₁)g(a₂n+b₂)/n = o(log ω)`.
  Engine = entropy decrement + MRT short-interval averages + **multiplicativity
  at small primes**.
- **Tao–Teräväinen**, Algebra & Number Theory 13 (2019) 2103, DOI
  10.2140/ant.2019.13.2103 (k-point correlations at almost-all scales);
  Duke 2019, DOI 10.1215/00127094-2019-0002 (log-averaged). **Teräväinen**,
  Forum Math. Sigma, DOI 10.1017/fms.2020.30 (binary correlations).
  All require a bounded MULTIPLICATIVE function at INTEGER-argument affine shifts.
- **The hypothesis that fails**: Möbius inversion on the prime indicator
  converts the fold's second moment `Σ_{n≤N} S(n)²` into a sum over prime values
  `q_j, q_{j'}` of `χ(q_j)χ(q_{j'})` at prime-INDEX separations — a bilinear sum
  in the index-domain string `j ↦ χ(q_j)`. This string is **not multiplicative
  in j** (the primes are not multiplicative in their index), so there is no
  single bounded multiplicative `f` with the fold's switch products expressible
  as Σ f(an+b)-style one-point affine correlations. The entropy-decrement
  machinery (short-prime-factor reduction, entropy inequalities) never engages.
  This is the same index-vs-value obstruction that refuted
  `dispersion-bilinear-large-sieve`, `matomaki-radziwill-index-autocorrelation`,
  and `level-set-explicit-formula`.
- **Directive 32 corroborates criterion (c)**: the per-scale second-moment
  decomposition collapses to the g=0 switch-density scale (claim
  `per-scale-refinement-collapses-to-switch-density`), so the correlations are
  no weaker than switch density. Priority 4 (weaker input) is not reached; the
  honest position is priority 5 (equivalence to a switch-density-family
  statement).

### Who has applied it to this problem
Nobody applies Tao's Chowla machine to a bilinear prime-index character sum; all
settled applications are to integer-index multiplicative functions. Report of
no-found-precedent, not a theorem of absence — but the hypothesis failure above
is structural, not absence.

### What it would buy
Nothing over the adopted squared-excess route; the arithmetic content is the
switch-density parity barrier again. Refuted.

---

## 3. `vandercorput-differencing-excess` — refuted

### What the reformulation is actually called
Apply the deterministic **van der Corput (Weyl) differencing lemma** to the
excess `S(n)=Σ_d (−1)^{T(n,d)}` — a pure identity, no probability measure —
converting a bound on a single sum into bounds on shifted autocorrelations.

### The theorems it relies on, and whether hypotheses hold here
- **van der Corput differencing inequality**:
  `|Σ_{n≤N} z_n|² ≤ (N+M)/M² · Σ_{|m|<M}(M−|m|) Σ_n z_n z̄_{n+m}`.
  Real and deterministic. References: Bergelson–Moreira, "van der Corput's
  difference theorem: some modern developments", Indag. Math. 2015, DOI
  10.1016/j.indag.2015.10.014; van der Corput–Kemperman, Monatsh. Math. 92
  (1981) 139–152, DOI 10.1007/BF01295144; mean-square form in Bernert
  arXiv:2310.02039, Browning–Prendiville Crelle 2015, DOI
  10.1515/crelle-2014-0122. So the differencing step is a theorem.
- **The hypothesis that fails** (the tool-target mismatch + a new reason):
  (1) van der Corput is a FIRST-moment (mean) cancellation identity — it bounds
  `|Σ_{n≤N} S(n)|`, but the adopted target (A) is the SECOND moment
  `E[S(n)²]=O(n)`; bounding the mean does not give `S(n)=o(n)` on a density-1
  set. (2) The shifted autocorrelations `Σ_n S(n)S(n+m)` it produces are the
  SAME fold-weighted switch-product correlations the squared-excess route already
  prices, reached through a strictly weaker lens — dominated, not new. (3) For
  SHIFTED autocorrelations the two `S(n)` factors read OVERLAPPING windows, so
  the single symmetric-difference structure (whose evenness excludes a
  standalone switch sign in `S(n)²` for fixed n) does NOT transpose: a standalone
  switch-density term CAN appear in the shifted autocorrelation, collapsing to
  the parity barrier (candidate's own falsifier (b)).
  (4) Directive 32 corroborates criterion (c): correlations collapse to the
  switch-density scale (`per-scale-refinement-collapses-to-switch-density`).

### Who has applied it to this problem
Not to this fold. van der Corput differencing is standard for exponential sums
and equidistribution; its application here reaches no new arithmetic input.

### What it would buy
A reformulation (identity + geometry) that lands on the same switch-product
correlations; no input weaker than switch density. Refuted.

---

## The recurring lesson (the board)

All three candidates — and the five that died before them — hit the same two
walls: (a) the object lives in the PRIME INDEX, not the prime value, so
value-domain tools (log-Chowla over integer arguments, value-shifted character
sums, short-value-interval moments) do not reach it; and (b) every second-moment /
correlation object collapses, at the coarsest dyadic scale (g=0), to the mod-4
switch-pair correlation — the named parity barrier (ABGS §9, `abgs-p1-wide-open`,
`lau-nonconstant-pattern-open`). No literature tool supplies a two-point
non-constant mod-4 input. The family that survives is the one that bounds the
*second moment / row-code distance distribution without pointwise pair control*
(adopted `fold-second-moment-krawtchouk`, `downset-row-code-distance-closed-form`,
`squared-excess-higher-order-dyadic-correlations`); these price the same
surviving arithmetic statement `E[S(n)²]=O(n)`. GOAL priority 2 (an input
strictly weaker than switch density) remains open only as an unconditional
arithmetic theorem; priority 5 (equivalence) is increasingly indicated by every
collapse.
