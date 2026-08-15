# Supply side via the dyadic/anti-dyadic dichotomy — the sharpest form of the one open content

This file does **not** restate `route-b-supply-consolidated.md` (which records
that everything below the supply line is discharged and the single residual gap
is `ν₂ ≥ c·n`). It decomposes **that one gap** into the structural dichotomy the
library has now accumulated the pieces for, and which the broken
`supply-nu2-factorization.md` did *not* state correctly. It is aligned with —
and is the goal-ledger form of — the live weakened ladder
`research/weakened/dyadic-collapse-ladder.md` (Directive 57): the ladder states
the climb; this file states what would *suffice* at each rung.

## What the broken factorization got wrong, and what survives

`supply-nu2-factorization.md` broke because its prime-side hypothesis
(`G-supply-nonconcentration`: no constant run of length ≥ L in the halved-gap bit
string) is refuted by Shiu 2000 — arbitrarily long runs of primes ≡ 1 mod 4 give
arbitrarily long all-0 runs. But Shiu kills only *long runs*, not *periodicity*,
and the library now distinguishes exactly those two things:

- `transfer-matrix-kernel-allones` (checked): the fold matrix Φ_n has rank n−3
  and kernel span(all-ones) — the all-ones string (consecutive odds, period 1)
  collapses to ν₂ = 0.
- `nu2-transfer-not-restored-by-nondegeneracy` (checked): the alternating-2/4
  family (h = 1010…, period 2) is successful yet ν₂ = O(1), killing the weak
  non-degeneracy hypotheses (H_a–H_e). Its h is **period-2**.
- `dyadic-collapse-ladder` (Directive 57, live): the two measured collapses are
  exactly the period-2^k cases k = 0, 1, and the live prediction is that the
  *dyadic* periods 1, 2, 4, 8 collapse while odd-factor periods grow. This
  dichotomy is **open** (tasks `test-dyadic-periodicity-prediction`,
  `prove-dyadic-periodicity-collapse-lemma`), so the collapse leg is NOT a
  settled fact to discharge against.

The pattern: every *recorded* collapse is a period-2^k bit string. That makes
the natural hypothesis the **dyadic dichotomy**: period-2^k collapses (the open
collapse leg), and non-dyadic-periodic positive-density h is linear (the open
converse). This is Directive 56's candidate (b) — "h non-eventually-periodic" —
sharpened to its dyadic form, and it is *not* refuted by anything the library
holds.

## What is honestly open vs. settled

The fold (ν₂ = wt(Φ_n h)) is **settled** (proved per-cell + checked matrix).
The two *measured* dyadic collapses (period 1, period 2) are **checked**. The
collapse **theorem** for all period-2^k, and the converse (anti-dyadic ⟹ linear),
are **both open** — they are the live `R-dyadic-collapse-lemma` and
`R-anti-dyadic-certificate-implies-supply` rungs of the ladder. The prime's
balance (w/n ≈ 0.60) is measured; its dyadic aperiodicity is a short corollary
of Shiu + Dirichlet (sketched below, to be formalised). The single genuinely
new proposition this file adds is the *converse-shaped* lemma: anti-dyadic +
balanced ⟹ ν₂ = Ω(n), stated with a falsification-first `next` so it cannot
quietly turn into a claim.

```skeleton
goal: | The supply bound: for the prime sequence, ν₂(q_n) ≥ c·n for a fixed c > 0 and all sufficiently large n (ν₂ = #2s in the maximal {0,2} suffix of the right diagonal δ(q_n)). This is the single remaining open content of Route B; with Lemma 5.4 and the demand side it implies Gilbreath's conjecture.
implies: | Work in the fixed coordinates of route-b-supply-consolidated.md. Let h ∈ {0,1}^{n-2} be the halved-gap bit string, h[j] = ((p_{j+2} − p_{j+1})/2) mod 2, so h[j] = 1 ⟺ gap_{j+2} ≡ 2 (mod 4). (0) LINEARIZATION [discharged].  ν₂(q_n) = wt(Φ_n h), where Φ_n is the F₂ fold matrix with entries Φ_n[k][j] = C(k−1, j−(n−k)) mod 2 over tail rows k = 2..n−2 and ancestor columns j = 2..n−1. Per cell this is rule90-interior-xor (proved); the matrix form, rank n−3, kernel span(all-ones), is transfer-matrix-kernel-allones (checked); the equality is verified 0 violations over 8 sparse + 2951 dense samples (g-supply-transfer-measured, carry-bridge-nu2-reproduction). (1) DYADIC COLLAPSE [SPAD-dyadic-collapse, OPEN].  h eventually periodic with period 2^k ⟹ ν₂(q_n) = O_k(1). This is the live ladder rung R-dyadic-collapse-lemma (theorem_prover, Lucas-only, prime-free). Only the k = 0, 1 cases are measured (consecutive odds, alternating-2/4); the general period-2^k theorem is NOT yet proved and is not discharged here. It is the direction that explains the dead universal transfer. (2) ANTI-DYADIC LINEAR [SPAD-anti-dyadic-linear, OPEN].  If h is NOT eventually periodic with period 2^k for any k, and both bits occur with density ≥ δ (a fixed δ > 0), then ν₂(q_n) = wt(Φ_n h) ≥ c·n for an absolute c = c(δ) > 0. This is the ladder rung R-anti-dyadic-certificate-implies-supply: the converse-shaped complement of the dyadic collapse, and the entire genuinely open combinatorial content of the supply side. (3) PRIME ANTI-DYADIC [SPAD-prime-anti-dyadic, OPEN, nearly discharged].  The prime h satisfies the hypothesis of (2): (a) h is not eventually periodic with period 2^k for any k (indeed not eventually periodic with ANY period); (b) balance — w(n)/n ≈ 0.60 (g-supply-transfer-measured, measured; both bits at density ≥ 0.4). COMBINE:  (3) puts the prime h in the hypothesis class of (2), so ν₂(q_n) ≥ c·n.  That is SC-supply-nu2-linear.  With Lemma 5.4 (lemma54-re-derived-proof, discharged) turning the budget g*_n ≤ 2ν₂(q_{n−1})+2 into success, and the demand g*_n ≤ n^{0.525+ε} (gap-bounds-cannot-force-block-growth, BHP, discharged), strong induction on n over the right diagonals gives every prime prefix successful, hence Gilbreath's conjecture (gilbreath-reduces-to-second-in-02).  This is a theorem CONDITIONAL on (2) (and the ladder's collapse leg (1), which is prime-free and separately attackable). Honesty: (2) is exactly the kind of "prime-free provable half" the board lesson (Directive 55/56) warns keeps collapsing, and the ladder names it as the difficulty expected to bite (`anti-dyadic-certificate`): the contrapositive of (1) — "ν₂ = O(1) ⟹ eventual period-2^k" — may FAIL. The `next` for (2) is a bounded exhaustive search DESIGNED to refute it cheaply; if it finds an anti-dyadic positive-density h with ν₂ = o(n), this skeleton is `broken` and that refutation is the result (it would confirm the supply side is irreducibly arithmetic, matching abgs-2011-s9-mod4-switch-limit-open).
killed-by: Its load-bearing converse SPAD-anti-dyadic-linear (= DPC-kernel-classification) is REFUTED, so the earlier 'superseded, not broken / nothing is false' note is wrong. Two independent witnesses, both balanced and dyadically aperiodic, both sublinear: (1) half-step strings h=1^{m/2}0^{m/2} give wt(Φh)=1 exactly, wt/m → 0 (0.125@8, 0.0625@16, 0.0833@24, 0.0313@32; captured in dyadic_halfstep_large.captured.txt — Directive 68); (2) Thue-Morse h[j]=wt(j) mod 2 is aperiodic (Hamming distance exactly n/2 from every 2^k-periodic string) with measured nu2/n collapsing 0.270->0.011, max nu2 ~ 219 over n<=4000 (dyadic-separating-invariant-three-strings; the exact O(log n) proof in thue-morse-sublinear-supply-witness is broken at its identification, thue-morse-subset-zeta-confirmed-identification-refuted). Hence 'anti-dyadic + balanced' does NOT force nu2 >= c*n, and the inference (SPAD-prime-anti-dyadic + SPAD-anti-dyadic-linear => supply) is broken. The collapse leg (SPAD-dyadic-collapse = dyadic-collapse-proved) survives as a proved artifact but yields no supply bound; the supply side reverts to the named-open arithmetic hypothesis abgs-2011-s9-mod4-switch-limit-open. See research/backward/dyadic-dichotomy-refuted.md.
reason: CLOSED by Directive 74 (not merely spent): SPAD-linearization discharged, SPAD-dyadic-collapse discharged, SPAD-anti-dyadic-linear REFUTED, SPAD-prime-anti-dyadic proved-but-inert. Every gap resolved and the route delivers nothing toward the supply bound; ν₂ ≥ c·n for the primes stays the named-open abgs-2011-s9-mod4-switch-limit-open, and the deliverable is now the conditional theorem (IF ν₂ ≥ c·n THEN Gilbreath), not any structural replacement.
rests-on: rule90-interior-xor, transfer-matrix-kernel-allones, g-supply-transfer-measured, carry-bridge-nu2-reproduction, nu2-transfer-not-restored-by-nondegeneracy, lemma54-re-derived-proof, gap-bounds-cannot-force-block-growth, gilbreath-reduces-to-second-in-02, shiu-2000-strings-of-congruent-primes, abgs-2011-s9-mod4-switch-limit-open
status: broken
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
id: SPAD-dyadic-collapse
lemma: |
  If h is eventually periodic with period 2^k (k ≥ 0), then ν₂(q_n) = O_k(1) as
  n → ∞. Mechanism (prime-free, from Lucas' theorem): the depth-d diagonal cell
  is the XOR of h over a binomial window with weights C(d,j) mod 2 = [j ⊆ d]
  (bitmask containment), and a period-2^k h collapses those sums for all large d.
status: discharged
discharged-by: dyadic-collapse-proved (proved, prime-free; sharp bound ν₂ ≤ N0 + 2^k, attained by 0…01).
  This gap was previously marked dropped-as-superseded; the lemma is in fact discharged.
next: |
  This is the live ladder rung R-dyadic-collapse-lemma and the live task
  `prove-dyadic-periodicity-collapse-lemma` (theorem_prover), gated on the
  dichotomy rung `test-dyadic-periodicity-prediction` (tool_builder) confirming
  that odd-factor periods grow. First move (tool_builder, settleable today): for
  periodic h with periods P = 1,2,4,8,3,5,6,7, measure ν₂(n) over n = 200..5000;
  the prediction is collapse (bounded ν₂) for P a power of 2 and growth for P with
  an odd factor. If a period-3 or period-5 family also gives ν₂ = O(1), the dyadic
  story is wrong and the ladder abandons at this rung (record failed). If it holds,
  theorem_prover: state the binomial-window identity exactly, apply Lucas
  (C(d,j) mod 2 = [j ⊆ d]), and show the period-2^k tail makes the XOR constant
  for d ≥ 2^k. This is prime-free and does NOT depend on (2).
thread: research/threads/gsupply-transfer-repair.md
```

```gap
id: SPAD-anti-dyadic-linear
lemma: |
  There are absolute constants δ > 0 and c > 0 such that: for every bit string
  h ∈ {0,1}^m that is (i) NOT eventually periodic with period 2^k for any k ≥ 0,
  and (ii) balanced (both 0 and 1 occur at least δ·m times), the F₂ fold weight
  satisfies wt(Φ_m h) ≥ c·m. Equivalently: ν₂(q_n) = Ω(n) for every 2-then-odds
  sequence whose halved-gap bit string is dyadically aperiodic and balanced.
  This is the ladder rung R-anti-dyadic-certificate-implies-supply — the
  converse-shaped complement of the dyadic collapse, and the genuinely open
  combinatorial content of the supply side.
status: refuted
discharged-by: (refuted, not discharged) half-step strings h=1^{m/2}0^{m/2} (balanced, dyadically
  aperiodic) give wt(Φh)=1, wt/m→0 (dyadic_halfstep_large.captured.txt); Thue-Morse gives
  measured sublinear nu2 (dyadic-separating-invariant-three-strings). The converse does not hold.
next: |
  FALSIFICATION FIRST (tool_builder, cheap and decisive): exhaustively minimise
  wt(Φ_m h)/m over ALL h ∈ {0,1}^m for m = 4..18, subject to (i) h dyadically
  aperiodic (no eventual period 2^k for any k ≤ ⌈log2 m⌉; in practice check the
  prefix period p ≤ m/2) and (ii) both bits ≥ 0.2·m. Report the minimiser h and
  its structure (run-length encoding, any long-prefix period). ALSO run named
  low-complexity anti-dyadic probes that are the standard would-be
  counterexamples: sparse-1s (h_j = [j is a power of 2], density → 0 — expected
  excluded by balance), a Sturmian/Beatty word (h_j = ⌊(j+1)φ⌋ − ⌊jφ⌋ mod 2,
  aperiodic, density φ−1 ≈ 0.618), and the period-doubling Toeplitz word. If any
  balanced anti-dyadic probe gives wt(Φ_m h)/m → 0, the lemma is REFUTED: record
  the structure as killed-by, move this skeleton to broken — that is the result
  (the supply side is then irreducibly arithmetic, matching
  abgs-2011-s9-mod4-switch-limit-open, and the ladder's anti-dyadic-certificate
  difficulty has bitten exactly as predicted). If the minimum stays ≥ c·m, the
  lemma is numerically anchored and the target is a proof.

  theorem_prover (after the search): first prove the CONTRApositive of (1) — if
  ν₂(q_n) = O(1) then h must carry an eventual period-2^k structure — and read
  off Π as its negation; if that contrapositive fails, the finding is the
  negative characterisation. Then the random analogue: for h i.i.d. unbiased,
  wt(Φ_m h) = m/2 + O(√(m log m)) with high probability (Azuma over the XOR
  folds), which pins the constant the deterministic anti-dyadic-balanced bound
  must reproduce. Do NOT claim a universal transfer ν₂ ≥ c·w — that is refuted
  (g-supply-transfer-universal-refuted, nu2-transfer-not-restored-by-nondegeneracy).
thread: research/threads/gsupply-transfer-repair.md
```

```gap
id: SPAD-prime-anti-dyadic
lemma: |
  The prime halved-gap bit string h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 satisfies
  the hypothesis of SPAD-anti-dyadic-linear: (a) h is NOT eventually periodic
  with period 2^k for any k (indeed not eventually periodic with ANY period);
  (b) both bits have positive density (w(n)/n ≈ 0.60, measured).
status: open
discharged-by: (none — see next) previously marked dropped-as-superseded; now open but vacuous: this lemma no
  longer closes anything toward GC because the converse SPAD-anti-dyadic-linear it feeds is refuted.
next: |
  Part (b) is settled by measurement (g-supply-transfer-measured: w/n ≈ 0.60 over
  n ≤ 30000; both bits at density ≥ 0.4) — it is a fact about the primes to the
  measured depth, and its unbounded-horizon form is the named-open two-point mod-4
  content (abgs-2011-s9-mod4-switch-limit-open), which the conditional theorem
  does not need to resolve beyond the measured anchor. Part (a) is a short
  theorem the library already has the ingredients for — theorem_prover task, then
  Lean:

  (a1) h eventually periodic with period p ⟹ the prime gaps satisfy
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
