# Supply bound via the dyadic kernel — a decomposition of SC-supply-nu2-linear

This skeleton does **not** restate the Route B reduction and does **not** re-propose
any of the four broken/consolidated supply skeletons. It decomposes the **single
remaining open content of the whole conjecture** — the supply lower bound
`ν₂(q_n) ≥ c·n` (id `SC-supply-nu2-linear`, the sharp form of
`GN-supply-nu2-density`) — along the axis the live thread
`research/threads/dyadic-periodicity-collapse.md` (Directive 57) has already
committed to.

## What this reduction is OF and a reduction TO

The route below the supply line is discharged: equivalence
(`gilbreath-reduces-to-second-in-02`), the runway (`lemma54-re-derived-proof`,
kernel-checked as `lemma54-descent-lean-formalised-even`), and the demand side
(`gap-bounds-cannot-force-block-growth` / BHP 2001, sharpened by
`li2023-short-interval-052`; immaterial once a linear supply bound holds). So the
goal reduces to `ν₂(q_n) ≥ c·n`, and this file breaks **that** into a
prime-free classification plus one prime-specific statement.

## Why the dyadic axis is the right one (and what it survives)

The transfer `ν₂ ≥ c·w` died on **two** successful families, and Directive 57
points out they share one shape: consecutive odds (`h = 111…`, period 1) and
alternating 2/4 (`h` of period 2) are both **dyadic-periodic** (`2^k`). The
thread's prediction: `ν₂ = O(1)` exactly when `h` is eventually periodic with
period a power of 2, and `ν₂` grows whenever the period has an odd factor. This
moves the load-bearing hypothesis from "no long constant run" — which Shiu 2000
**kills** (`shiu-2000-strings-of-congruent-primes`: arbitrarily long same-residue
runs, i.e. long all-0 stretches, which are locally 1-periodic) — to **global
aperiodicity**, which Shiu does *not* kill: a long local all-0 run is consistent
with `h` being globally far from the all-0 string.

```skeleton
goal: For the prime sequence, ν₂(q_n) ≥ c·n for an absolute c > 0 and all sufficiently large n, where ν₂(q_n) is the number of 2s in the maximal {0,2} suffix of the right diagonal δ(q_n). (This is SC-supply-nu2-linear; discharging it closes the single open gap of route-b-supply-consolidated and, via the discharged runway/demand/equivalence legs, proves Gilbreath's conjecture.)
implies: |
  Let h ∈ {0,1}^ℕ be the mod-4 switch bit, h[j] = ((p_{j+2} − p_{j+1})/2) mod 2
  (so h[j]=1 ⟺ consecutive primes switch residue class mod 4), and Φ_n the
  Pascal-mod-2 fold over the fixed ancestor window [2, n−1].

  (0) LINEARIZATION [DPC-linearization, discharged]  ν₂(q_n) = wt(Φ_n h):
      the halved {0,2}-tail cell at depth d is the XOR of a binom(d,·)-window of
      h (rule90-interior-xor, proved), and the row-1 ancestor union of the tail
      cells (k, n−k), k = K..n−2, is exactly the fixed interval [2, n−1] (proved
      in the nu2_vs_gap_parity session, not yet promoted to a claim block — the
      promotion is housekeeping, not a gap).

  (1) DYADIC COLLAPSE [DPC-dyadic-collapse, open]  h eventually 2^k-periodic
      ⟹ wt(Φ_n h) = O_k(1). Prime-free; from Lucas' theorem alone (the binomial
      window weights C(d,j) mod 2 are supported on the binary submasks of d, so
      a 2^k-periodic h collapses every large-depth window sum to a constant).
      This explains both recorded counterexamples and is a provable theorem, not
      a conjecture.

  (2) KERNEL CLASSIFICATION [DPC-kernel-classification, open]  the converse,
      quantitatively: there is an absolute ε₀ and constants such that
      wt(Φ_n h) < ε₀·n ⟹ h|[1,n] is within o(n) Hamming distance of a 2^k-periodic
      string for some k ≤ K₀. I.e. the only h for which the fold has sublinear
      weight are those asymptotically dyadic-periodic. This is the
      CHT-inverse-theorem in ν₂-coordinates: it isolates the *kernel* of the fold.

  (3) PRIME ANTI-DYADICITY [DPC-prime-antidyadic, open]  the prime h is not
      asymptotically 2^k-periodic for any fixed k — quantitatively, for every
      k ≤ K₀ the prime h stays ≥ δ·n Hamming-far from every 2^k-periodic string
      for all large n.

  COMBINE:  Suppose for contradiction ν₂(q_n) < c·n with c := ε₀. By (0) and (2),
  h|[1,n] is close to a 2^k-periodic string (k ≤ K₀), which contradicts (3) for
  n large. Hence ν₂(q_n) ≥ ε₀·n for all large n. Feeding ε₀·n > n^{0.52} ≥ g*_n
  into the runway (lemma54-re-derived-proof) and strong induction from the
  verification base (verification-record-2026) gives every finite prime prefix
  successful, hence GC via gilbreath-reduces-to-second-in-02.

  The one place this inference is more delicate than "contradiction" suggests:
  (2) must be stated in its *uniform* quantitative form — "wt < ε₀·n at some n
  forces closeness to a dyadic string at that n" — because the runway needs
  ν₂ ≥ c·n at *every* large n, not just along a subsequence. That uniformity is
  precisely where the sublinear classification is upgraded to a uniform lower
  bound, and it is the real content of (2)+(3); it is flagged, not assumed.
status: live
rests-on: gilbreath-reduces-to-second-in-02, gilbreath-second-entry-equivalence, lemma54-re-derived-proof, lemma54-descent-lean-formalised-even, gap-bounds-cannot-force-block-growth, li2023-short-interval-052, li2023-not-bottleneck, verification-record-2026, rule90-interior-xor, bcz-2023-left-edge-stabilization, ducci-avart-nilpotent-concatenation, abgs-2011-s9-mod4-switch-limit-open
```

```gap
id: DPC-linearization
lemma: ν₂(q_n) = wt(Φ_n h), where h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 and Φ_n is the F2 matrix with entries [C(k,j) mod 2] over tail rows k = K..n−2 and ancestor columns j = 2..n−1. Equivalently each halved {0,2}-tail cell is the XOR of a Pascal-mod-2 window of h, and the union of ancestor windows over the tail rows is exactly [2, n−1].
status: discharged
discharged-by: rule90-interior-xor (proved; the halved interior cell at depth d is the XOR of a binom(d,·)-window of the halved row-1 bits) composed with the ancestor-window interval fact (the row-1 ancestors of the tail cells (k, n−k), k = K..n−2, are exactly the fixed interval [2, n−1] — proved in the nu2_vs_gap_parity tool_builder session). Verified numerically with 0 violations at all 8 sparse samples {50,100,200,400,800,1600,3200,3999} and all 2951 dense n ∈ [50,3000] (code/out/linearization_verify.captured.txt). The only outstanding item is promoting the ancestor-window interval to a claim block; the composition itself is a write-down, not a conjecture.
```

```gap
id: DPC-dyadic-collapse
lemma: If h is eventually periodic with period 2^k (k ≥ 0), then ν₂(q_n) = wt(Φ_n h) = O_k(1): the fold weight is bounded by a constant depending only on k. Concretely consecutive odds (h = 111…, period 1) and alternating 2/4 (period 2) both give ν₂ = O(1), and this must generalise to every dyadic period.
status: open
next: |
  TWO first moves, tool_builder FIRST because it is decisive and cheap:
  1. tool_builder — test the falsifiable prediction before anyone proves it.
     ALREADY SETTLED (do not re-run): P ∈ {1,2,4} give ν₂ = O(1) — period 1 is
     the exact kernel of Φ_n (transfer-matrix-kernel-allones, ν₂=0); period 2
     (alternating 2/4) and period 4 give ν₂=O(1) (nu2-transfer-not-restored-by-nondegeneracy,
     "periodic {2,4}-gap families of period dividing 4"). The genuinely new tests
     are: (a) P = 8 (predicted: also O(1), since 8 is a power of 2); (b) odd
     periods P ∈ {3,5,6,7} (predicted: ν₂ GROWS, since the period has an odd
     factor). Build the 2-then-odds sequence (gaps from h, first gap 2), compute
     ν₂(n) over n = 200..5000. If a period-3 or period-5 family also gives
     ν₂ = O(1), the dyadic story is wrong — record DPC-dyadic-collapse as REFUTED
     (killed-by) and stop; that is the falsifier the thread names. Launch with
     timeout + tee into code/out/, state depth/width/workers.
  2. theorem_prover — if the prediction holds, prove it prime-free from Lucas'
     theorem: the depth-d diagonal cell is an XOR of h over a window with weights
     C(d,j) mod 2, which are supported on the binary submasks of d; a 2^k-periodic
     h makes every large-d window sum collapse to a constant. This is a
     combinatorial identity, no prime input, and it is the strongest provable
     artifact the dyadic axis can produce.
thread: research/threads/dyadic-periodicity-collapse.md
```

```gap
id: DPC-kernel-classification
lemma: (Quantitative converse of the collapse.) The only way wt(Φ_n h) is sublinear is asymptotic dyadic periodicity: there is ε₀ > 0 and k₀ such that wt(Φ_n h) < ε₀·n at some n forces h|[1,n] to be within o(n) Hamming distance of a 2^k-periodic string for some k ≤ k₀. Equivalently the low-weight preimages of the fold Φ_n are exactly the strings close to a dyadic-periodic one — this is the kernel classification of the F2 fold, the CHT-inverse-theorem in ν₂-coordinates.
status: open
next: |
  This is the genuinely hard combinatorial half, but it is prime-free and has
  two concrete first moves:
  1. tool_builder (feasibility, before any proof): exhaustively over h ∈ {0,1}^m,
     m ≤ 16, minimise wt(Φ h)/m subject to "≥ δ·m Hamming distance from every
     2^k-periodic string, k ≤ 4". Report the worst-case ratio. If it stays
     bounded away from 0 as m grows, the classification is numerically anchored;
     if it decays, the lemma is FALSE as stated and the dyadic kernel is not the
     full story — a killed-by entry would itself be the result.
  2. theorem_prover: reduce to the F2 involution/nilpotence structure already in
     the library — bcz-2023-left-edge-stabilization (T² = id, Υ⁶ = id, the fold
     is invertible of period 6) and ducci-avart-nilpotent-concatenation (vectors
     killed by a fixed-depth Ducci power are exactly concatenations of
     power-of-2 blocks). Together they say: h with wt(Φ_n h) = o(n) must be
     asymptotically 2^k-periodic. The first concrete theorem to attempt is the
     random analogue — wt(Φ_n h) = n/2 + O(√(n log n)) w.h.p. for unbiased i.i.d.
     h (an Azuma bound over the XOR folds) — which pins the constant ε₀.
thread: research/threads/dyadic-periodicity-collapse.md
```

```gap
id: DPC-prime-antidyadic
lemma: The prime mod-4 switch bit h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 is not asymptotically periodic with period a power of 2, in the quantitative sense needed: for each k ≤ k₀ there is δ_k > 0 such that h|[1,n] differs from every 2^k-periodic string in at least δ_k·n positions for all sufficiently large n. This is a statement about prime gaps mod 4 (the sequence of residue classes p_j mod 4 is not eventually periodic with period dividing 2^{k+1}).
status: open
next: |
  This is the prime-specific residual, and it is strictly weaker than (hence a
  candidate route to) the named-open supply bound. Two first moves:
  1. tool_builder (cheap anchor): compute, for n up to 1e6 (sieve ≤ 1.6e7, O(n)
     memory), the Hamming distance of h|[1,n] to the nearest 2^k-periodic string
     for k = 0..6; report distance/n. Expectation: distance/n stays near 0.4–0.6
     (h is ~60% ones, far from the period-1 all-0/all-1 strings and from every
     short-period pattern). If any k gives distance/n → 0, DPC-prime-antidyadic
     is refuted empirically — say so.
  2. theorem_prover / request_research: reduce "p_j mod 4 is not eventually
     periodic with period 2^{k+1}" to known distribution of primes in APs —
     periodicity would force, for large j, p_j to sit in a fixed residue class
     pattern mod 4·2^{k+1}, which Dirichlet (infinitely many primes in every
     coprime class) and its refinements rule out. CRITICAL: this survives where
     G-supply-nonconcentration died — Shiu 2000's arbitrarily long same-residue
     runs are long *local* all-0 stretches (locally 1-periodic) and are fully
     consistent with global aperiodicity; the hypothesis here is global, not
     "no long constant run".
thread: research/threads/dyadic-periodicity-collapse.md
```
