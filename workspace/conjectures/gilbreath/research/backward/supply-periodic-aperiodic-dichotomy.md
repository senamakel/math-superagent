# Supply side via the periodic/aperiodic dichotomy — the sharpest form of the one open content

This file does **not** restate `route-b-supply-consolidated.md` (which records
that everything below the supply line is discharged and the single residual gap
is `ν₂ ≥ c·n`). It decomposes **that one gap** into the structural dichotomy the
library has now accumulated the pieces for, and which the broken
`supply-nu2-factorization.md` did *not* state correctly.

## What the broken factorization got wrong, and what survives

`supply-nu2-factorization.md` broke because its prime-side hypothesis
(`G-supply-nonconcentration`: no constant run of length ≥ L in the halved-gap bit
string) is refuted by Shiu 2000 — arbitrarily long runs of primes ≡ 1 mod 4 give
arbitrarily long all-0 runs. But Shiu kills only *long runs*, not *periodicity*,
and the newer claims in the library distinguish exactly those two things:

- `transfer-matrix-kernel-allones` (checked): the fold matrix Φ_n has rank n−3
  and kernel span(all-ones) — the all-ones string (consecutive odds) collapses
  to ν₂ = 0.
- `rule90-periodic-window-collapse` (asserted): **any** eventually periodic h
  collapses to ν₂ = O_p(1) — not just all-ones.
- `nu2-transfer-not-restored-by-nondegeneracy` (checked): the alternating-2/4
  family (h = 1010…, period 2) is successful yet ν₂ = O(1), killing the weak
  non-degeneracy hypotheses (H_a–H_e). Its h is **periodic**.

The pattern: every recorded collapse is a periodic (or density-0/1) bit string.
That makes the natural hypothesis the **dichotomy**: periodic h collapses, and
aperiodic positive-density h is linear. This is the sharpest restatement of
Directive 56's candidate (b) — "h non-eventually-periodic" — and it is *not*
refuted by anything the library holds (Shiu's long runs are compatible with
aperiodicity; the alternating-2/4 family is periodic).

## What is honestly open vs. discharged

The fold (ν₂ = wt(Φ_n h)) and the collapse direction (periodic ⟹ O(1)) are in
the library. The prime's balance (positive density of both bits) is **measured**
(w/n ≈ 0.60), and its aperiodicity is a three-line corollary of Shiu + Dirichlet.
The single genuinely open lemma is the converse of the collapse: *aperiodic +
positive density ⟹ ν₂ = Ω(n)*. That lemma is the entire content of this file,
stated with a falsification-first `next` so it cannot quietly turn into a claim.

```skeleton
goal: |
  The supply bound: for the prime sequence, ν₂(q_n) ≥ c·n for a fixed c > 0 and
  all sufficiently large n (ν₂ = #2s in the maximal {0,2} suffix of the right
  diagonal δ(q_n)). This is the single remaining open content of Route B; with
  Lemma 5.4 and the demand side it implies Gilbreath's conjecture.
implies: |
  Work in the fixed coordinates of route-b-supply-consolidated.md. Let
  h ∈ {0,1}^{n-2} be the halved-gap bit string, h[j] = ((p_{j+2} − p_{j+1})/2) mod 2,
  so h[j] = 1 ⟺ gap_{j+2} ≡ 2 (mod 4).

  (0) LINEARIZATION [discharged].  ν₂(q_n) = wt(Φ_n h), where Φ_n is the F₂ fold
      matrix with entries Φ_n[k][j] = C(k−1, j−(n−k)) mod 2 over tail rows
      k = 2..n−2 and ancestor columns j = 2..n−1. Per cell this is
      rule90-interior-xor (proved); the matrix form, rank n−3, kernel
      span(all-ones), is transfer-matrix-kernel-allones (checked); the equality
      is verified 0 violations over 8 sparse + 2951 dense samples
      (g-supply-transfer-measured, carry-bridge-nu2-reproduction).

  (1) COLLAPSE [discharged].  h eventually periodic with period p ⟹ ν₂ = O_p(1)
      (rule90-periodic-window-collapse). Every recorded sublinear/constant case —
      consecutive odds (h = 1^n), alternating-2/4 (h = (10)^{n/2}) — is periodic.

  (2) NON-DEGENERATE LINEAR [SPAD-nondegenerate-linear, OPEN].  If h is not
      eventually periodic and both bits occur with density ≥ δ (a fixed δ > 0),
      then ν₂(q_n) = wt(Φ_n h) ≥ c·n for an absolute c = c(δ) > 0.

  (3) PRIME NON-DEGENERATE [SPAD-prime-nondegenerate, OPEN, nearly discharged].
      The prime h satisfies the hypothesis of (2): (a) aperiodicity — h is not
      eventually periodic; (b) balance — w(n)/n ≈ 0.60
      (g-supply-transfer-measured, measured; both bits at density ≥ 0.4).

  COMBINE:  (3) puts the prime h in the hypothesis class of (2), so
      ν₂(q_n) ≥ c·n.  That is SC-supply-nu2-linear.  With Lemma 5.4
      (lemma54-re-derived-proof, discharged) turning the budget
      g*_n ≤ 2ν₂(q_{n−1})+2 into success, and the demand g*_n ≤ n^{0.525+ε}
      (gap-bounds-cannot-force-block-growth, BHP, discharged), strong induction
      on n over the right diagonals gives every prime prefix successful, hence
      Gilbreath's conjecture (gilbreath-reduces-to-second-in-02).  This is a
      theorem CONDITIONAL on (2); (2) itself is NOT claimed proved.

  Honesty: (2) is exactly the kind of "prime-free provable half" the board
  lesson (Directive 55/56) warns keeps collapsing.  The `next` for (2) is a
  bounded exhaustive search DESIGNED to refute it cheaply; if it finds a
  low-complexity aperiodic positive-density h with ν₂ = o(n), this skeleton is
  `broken` and that refutation is the result (it would confirm the supply side
  is irreducibly arithmetic, matching abgs-2011-s9-mod4-switch-limit-open).
status: sketched
rests-on: rule90-interior-xor, transfer-matrix-kernel-allones,
  rule90-periodic-window-collapse, g-supply-transfer-measured,
  carry-bridge-nu2-reproduction, lemma54-re-derived-proof,
  gap-bounds-cannot-force-block-growth, gilbreath-reduces-to-second-in-02,
  shiu-2000-strings-of-congruent-primes, abgs-2011-s9-mod4-switch-limit-open
```

```gap
id: SPAD-linearization
lemma: |
  ν₂(q_n) = wt(Φ_n h) with Φ_n[k][j] = C(k−1, j−(n−k)) mod 2 (tail rows
  k = 2..n−2, ancestor columns j = 2..n−1), i.e. each halved {0,2}-tail cell is
  the XOR of a Pascal-mod-2 window of the halved-gap bits h, and the union of
  the ancestor windows is the fixed interval [2, n−1].
status: discharged
discharged-by: rule90-interior-xor (proved, per-cell fold) + transfer-matrix-kernel-allones
  (checked, the Φ_n matrix with rank n−3, kernel span(all-ones)); equality verified
  0 violations on 8 sparse + 2951 dense samples (g-supply-transfer-measured,
  carry-bridge-nu2-reproduction).
next: none — restating this as open re-opens a proved identity.
```

```gap
id: SPAD-periodic-collapse
lemma: |
  If h is eventually periodic with period p, then every {0,2}-tail cell is an
  XOR-fold of a window of h of bounded length (≤ p), so the cell values take
  finitely many values and ν₂(q_n) = O_p(1).
status: discharged
discharged-by: rule90-periodic-window-collapse (asserted; the O_p(1) constant should be
  made explicit — a one-line theorem_prover promotion of rule90-interior-xor).
next: none — the statement is in the library; the explicit-constant promotion is a
  theorem_prover sub-task, not a re-derivation.
```

```gap
id: SPAD-nondegenerate-linear
lemma: |
  There are absolute constants δ > 0 and c > 0 such that: for every bit string
  h ∈ {0,1}^m that is (i) not eventually periodic and (ii) balanced (both 0 and 1
  occur at least δ·m times), the F₂ fold weight satisfies wt(Φ_m h) ≥ c·m.
  Equivalently: ν₂(q_n) = Ω(n) for every 2-then-odds sequence whose halved-gap
  bit string is aperiodic and balanced. This is the F₂ inverse theorem in the
  coordinates of the broken supply-nu2-factorization, with the refuted
  "no long constant run" hypothesis replaced by aperiodicity + balance.
status: open
next: |
  FALSIFICATION FIRST (tool_builder, cheap and decisive): exhaustively minimise
  wt(Φ_m h)/m over ALL h ∈ {0,1}^m for m = 4..18, subject to (i) h aperiodic
  (no period p ≤ m/2, i.e. h ≠ σ^p(h) for any p) and (ii) both bits ≥ 0.2·m.
  Report the minimiser h and its structure (run-length encoding, the period of any
  long prefix). ALSO run three named low-complexity aperiodic probes that are the
  standard would-be counterexamples: sparse-1s (h_j = [j is a power of 2], density
  → 0 — expected to be excluded by balance), a Sturmian/Beatty word (h_j =
  ⌊(j+1)φ⌋ − ⌊jφ⌋ mod 2, aperiodic, density φ−1 ≈ 0.618), and the period-doubling
  Toeplitz word. If any balanced aperiodic probe gives wt(Φ_m h)/m → 0, the lemma
  is REFUTED: record the structure as killed-by and move the skeleton to broken —
  that is the result (the supply side is then irreducibly arithmetic). If the
  minimum stays ≥ c·m, the lemma is numerically anchored and the target is a proof.

  theorem_prover (after the search): reduce to the F₂ involution/nilpotence
  structure already in the library — bcz-2023-left-edge-stabilization (T² = id,
  Υ⁶ = id over F2[[X]]) and the CHT inverse theorem (cht-inverse-theorem): the
  only small-image h are asymptotically periodic or one-sided in density. The
  first concrete theorem is the random analogue: for h i.i.d. unbiased,
  wt(Φ_m h) = m/2 + O(√(m log m)) with high probability (Azuma over the XOR
  folds), which pins the constant the deterministic aperiodic-balanced bound must
  reproduce.
thread: research/threads/gsupply-transfer-repair.md
```

```gap
id: SPAD-prime-nondegenerate
lemma: |
  The prime halved-gap bit string h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 satisfies
  the hypothesis of SPAD-nondegenerate-linear: (a) h is NOT eventually periodic;
  (b) both bits have positive density (w(n)/n ≈ 0.60, measured).
status: open
next: |
  Part (b) is discharged by measurement (g-supply-transfer-measured: w/n ≈ 0.60
  over n ≤ 30000; both bits at density ≥ 0.4). Part (a) is a three-line theorem
  the library already has the ingredients for — theorem_prover task, then Lean:

  (a1) h eventually periodic (period p) ⟹ the prime gaps satisfy
       g_j ≡ g_{j+p} (mod 4) eventually ⟹ p_{j+p} − p_j ≡ C (mod 4) for a fixed
       C, so p_j mod 4 is eventually periodic with period ≤ 4p.
  (a2) shiu-2000-strings-of-congruent-primes: for every M there are M consecutive
       primes all ≡ 1 mod 4. A run of M > P consecutive equal residues inside an
       eventual period-P sequence forces the whole period word to be 1.
  (a3) There are infinitely many primes ≡ 3 mod 4 (Dirichlet, or the elementary
       Euclid proof), contradicting an all-1 tail.
  Hence h is aperiodic. Formalise (a1)–(a3) and file as a proved claim; until
  then this gap is open and the composed argument above is the reason to expect
  it to close cheaply.
thread: research/threads/gsupply-transfer-repair.md
```
