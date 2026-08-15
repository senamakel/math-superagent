# CHT inverse-theorem route — decompose the goal through the proved obstruction theorem

This file does **not** restate Route B (`route-b-supply-consolidated.md`, whose
single gap is the named-open supply bound `ν₂ ≥ c·n`), and it does **not** open a
fourth coordinate form of the supply side. It records the one decomposition the
run's library already holds the theorem for but has not yet written as a
skeleton: the **deterministic inverse theorem** of Chase–Hunter–Tao 2026
(`cht-inverse-theorem`, proved), which says the *only* ways an array with small
initial data fails to decay to `{0,1}` are (i) an oversized entry, (ii) a long
zero-block, or (iii) a long shallow `{0,d}`-block in the right half.

The point of this skeleton is that it collapses (ii) **unconditionally and
trivially** for the primes, leaving exactly two Cramér-level hypotheses — a
*different* conditional route from Route B's HL/LOS two-point correlation. It is
recorded so the ledger stops offering "reduce to CHT" as a loose idea and instead
names the two hypotheses whose conjunction would close the goal.

Conventions (matching the run): the CHT array is generated from the normalized
gaps `a_n = (p_{n+2} − p_{n+1})/2 − 1` (so `a_n = 0 ⟺ gap = 2`, a twin prime
step); `a^{(N−1,1)}` is its entry at depth `N−1`, position 1, and
`cht-normalized-gap-definition` gives GC ⟺ the array's left diagonal is
eventually `{0,1}`-valued.

```skeleton
goal: Gilbreath's conjecture for the primes — A_k(0) = 1 for every k ≥ 1,
      equivalently every finite prime prefix is successful.
implies: |
  (0) EQUIVALENCE [discharged]
      A_k(0)=1 ∀k ⟺ A_k(1)∈{0,2} ∀k (gilbreath-reduces-to-second-in-02, proved;
      gilbreath-second-entry-equivalence, Lean IFF). By cht-normalized-gap-definition
      (proved) this is the statement that the left diagonal of the normalized-gap
      array a_n = (p_{n+2}−p_{n+1})/2 − 1 is eventually {0,1}-valued.

  (1) INVERSE THEOREM [discharged — the proved theorem]
      cht-inverse-theorem (CHT 2026, proved; verbatim in cht-theorem16-verbatim-fullpdf):
      if a_n ≤ 2^M, there is no length-L zero-block in (a_n), and no right-half
      {0,d}-block with 2^{M−m} < d ≤ 2^{M−m+1} of length ≥ R_m − 3R_{m−1} at depth
      ≤ 2R_{m−1} (R_m ≥ 4R_{m−1}, R_0 ≥ 100·L·8^M), then a^{(N−1,1)} ∈ {0,1}.
      So the goal reduces to the three hypotheses of this theorem holding for the
      prime array. (Note: holds-here is recorded "no" for this claim *because* its
      hypotheses are not established for the primes — that is exactly what the two
      gaps below are. The theorem itself is proved.)

  (2) ZERO-BLOCK OBSTRUCTION [discharged — elementary, unconditional]
      H2, "no length-L zero-block in (a_n)", holds trivially for the primes.
      a_n = 0 ⟺ p_{n+2} − p_{n+1} = 2, so a zero-block of length L means L+1
      primes p, p+2, …, p+2L. Among any three of the form p, p+2, p+4 one is
      ≡ 0 (mod 3); for p > 3 that one is > 3 and hence composite. Therefore a
      zero-run in (a_n) has length ≤ 2, and the only length-2 run is at the very
      start (primes 3,5,7, i.e. a_1 = a_2 = 0 — check the first nine
      0,0,1,0,1,0,1,2,0). CHT's L is astronomically large (≈ log^10 N), so H2 is
      satisfied by the primes unconditionally. This is a mod-3 fact, not a gap.

  (3) SIZE [CHT-size-bound, OPEN]
      H1, a_n ≤ 2^M with M = O(log log n) — equivalently the record gap
      g*_n = O(log^2 n) (Cramér). This is what makes R_0 = 100·L·8^M a power of
      log N, keeping the inverse theorem non-vacuous. Measured at sieve 6e8:
      max a_n = 140 ≤ 256 = 2^8, so M = 8 works at that scale
      (cht-right-half-0d-scan-6e8). Open asymptotically.

  (4) 0d-BLOCK OBSTRUCTION [CHT-0d-block-absence, OPEN]
      H3, no right-half {0,d}-block (d ≥ 2) of length ≥ R_m − 3R_{m−1} at depth
      ≤ 2R_{m−1}. Measured at sieve 6e8 / depth 400: the longest such block has
      length 25 (row 14, d=2) against a smallest threshold T_1 = 5.63e16
      (cht-right-half-0d-scan-6e8) — absent at every reachable scale. Open
      asymptotically.

  COMBINE:  (2)+(3)+(4) give the three hypotheses of (1), hence a^{(N−1,1)} ∈ {0,1}
  for every large N; by (0) that is A_k(1) ∈ {0,2} for every large k, hence
  A_k(0) = 1 for every k — Gilbreath's conjecture.

  This is a CONDITIONAL theorem. Its two hypotheses, (3) and (4), are both
  Cramér-level statements about prime-gap arrangement, and are distinct from
  Route B's single hypothesis (the two-point consecutive-prime mod-4 correlation,
  abgs-2011-s9-mod4-switch-limit-open). The run's honest deliverable can therefore
  be stated under EITHER hypothesis family; this file makes the Cramér family
  explicit and reduces it from CHT's "three obstructions" to effectively one
  obstruction plus a size bound, by discharging the zero-block for free.

status: sketched
rests-on: gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, cht-normalized-gap-definition, cht-inverse-theorem, cht-theorem16-verbatim-fullpdf, cht-right-half-0d-scan-6e8, gap-bounds-cannot-force-block-growth
killed-by: (none — new decomposition through the proved CHT inverse theorem; its two gaps are Cramér-level and are NOT disguised as provable)
```

```gap
id: CHT-size-bound
lemma: |
  The normalized prime gaps a_n = (p_{n+2} − p_{n+1})/2 − 1 satisfy a_n ≤ 2^M
  for M = O(log log n) — equivalently the record prime gap satisfies
  g*_n = max_{2≤k≤n}(p_k − p_{k−1}) = O(log^2 n), with constants chosen so that
  R_0 = 100·L·8^M = poly(log N). This is Cramér's record-gap conjecture (or a
  weaker sufficient sub-log^2 form); the measured value is max a_n = 140 at
  sieve 6e8 (M = 8), far below any Cramér-consistent M.
status: open
next: |
  STATUS HONESTY: the unconditional record-gap bound is BHP 2001, g*_n < n^{0.525+ε}
  (sharpened to n^{0.52+ε} by li2023-short-interval-052). That gives M = O(log n),
  which makes R_0 = 100·L·8^M a power of n and the inverse theorem vacuous
  (obstruction depth 2R_{m−1} exceeds the array). So the non-vacuous form of this
  gap is Cramér-level and is OPEN — it must be stated as a hypothesis, never as
  "nearly closed". Two first moves:
  (a) tool_builder (cheap anchor): extend the record-gap measurement to the
      largest sieve the 8 GiB cap allows (one pass, O(n) memory), report max a_n
      and its growth against log^2 n. This only sharpens the measured constant;
      it does NOT move the asymptotic status — say so in the capture.
  (b) request_research: the exact status of Cramér's conjecture and the sharpest
      unconditional sub-polynomial record-gap bound short of Cramér; what would
      falsify is a citation of an unconditional g*_n = O(log^2 n), which does not
      exist. This is a research request, not a task — the unconditional theorem
      is not attackable by the run.
```

```gap
id: CHT-0d-block-absence
lemma: |
  For the M and L fixed by CHT-size-bound, the prime normalized-gap array has no
  right-half {0,d}-block (d ≥ 2) with 2^{M−m} < d ≤ 2^{M−m+1} of length
  ≥ R_m − 3R_{m−1} at depth ≤ 2R_{m−1}. Equivalently: the descent never stalls
  in a long shallow {0,d} regime in the right half of the array — this is the
  regeneration obstruction (the same open content as Route B's supply side,
  restated as block-absence rather than as a mod-4 switch density).
status: open
next: |
  STATUS HONESTY: this is the single real obstruction left after the zero-block
  discharge, and it is Cramér-level open — the measured max {0,d}-block is 25
  (row 14, d=2) against a threshold 5.63e16 (cht-right-half-0d-scan-6e8), so it
  is absent at every scale the run can reach, but proving absence at the
  theorem's threshold is not a finite check. It is a DIFFERENT hypothesis from
  Route B's two-point mod-4 correlation (here: gap-arrangement / long
  {0,d}-run absence, attackable in principle by Cramér-type density-increment),
  which is why this is a distinct conditional route rather than a restatement.
  Two first moves:
  (a) tool_builder (cheap, extends the anchor): rerun the right-half {0,d} scan
      at a larger sieve/depth (the existing 6e8/400-row scan is the template,
      one row live, exact int64, O(W) memory), and report the longest {0,d}-block
      per dyadic scale d = 2^{M−m}..2^{M−m+1}. This measures how far below the
      thresholds the real blocks sit and would catch any scale where the
      obstruction starts to appear — it does not close the gap.
  (b) theorem_prover / request_research: reduce "no long shallow {0,d}-block" to
      a gap-distribution statement (e.g. the frequency of near-clustered gap
      patterns), and locate the weakest unconditional gap-distribution result
      that would rule out a {0,d}-block of length ≥ R_m at depth ≤ 2R_{m−1}.
      A positive citation of a sub-log^2 bound strong enough here is exactly what
      would falsify the claim that this is Cramér-level; the run has none
      (gap-bounds-cannot-force-block-growth says input upper bounds cannot force
      output lower bounds, and no held source controls block-length growth).
thread: research/threads/regeneration.md
```
