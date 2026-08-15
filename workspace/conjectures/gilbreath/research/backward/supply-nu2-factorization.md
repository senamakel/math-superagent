# Supply ν₂ factorization — what would prove the ν₂ ≥ c·n bound

This skeleton does **not** restate the Granville reduction. `granville-nu2-reduction.md`
already decomposes Gilbreath into three legs, of which two are settled
(`GN-demand-record-gap-bhp` discharged by Baker–Harman–Pintz; `GN-lemma54-runway`
proved on the even domain as claim `lemma54-re-derived-proof`) and exactly one —
`GN-supply-nu2-density`, ν₂ > n^β for β > 0.525 — is open.

This file breaks **that one open gap** into what would actually suffice to close
it, because as stated it is not yet attackable: it is a density statement about
the count of 2s in a right diagonal, and a forward attempt would not know which
of the two genuinely different ingredients (an F2-linear structure fact, or a
prime-residue fact) it is trying to prove.

## The obstruction that forces this decomposition to be honest

The rising-sea board lesson asserts G-supply "reduces cleanly to a prime-gap-mod-4
density claim" via a transfer ν₂ ≥ w/c. **That transfer is false as a universal
statement**, and it is false inside the class the conjecture lives in:

Take a 2-then-odds sequence with *every* gap ≡ 2 mod 4, e.g. gaps (1, 2, 6, 6, 6, …):
```
A_0 = (2, 3, 5, 11, 17, 23, 29, …)
A_1 = (1, 2,  6,  6,  6,  6,  6, …)
A_2 = (1, 4,  0,  0,  0,  0,  0, …)
A_3 = (3, 4,  0,  0,  0,  0,  0, …)   ← second entry 4, row 3 starts with 3: FAILS
```
Here the halved-gap bit string is `h = 1111…` (weight w = n, the *maximal* mod-4
transition density) yet the halved triangle is all-0 below row 1 (Rule-90 of a
constant string), so the {0,2} tail of the right diagonal has ν₂ = 0. Symmetrically
all gaps ≡ 0 mod 4 gives `h = 0000…` and fails even sooner. **Mod-4 density alone
does not imply ν₂ ≥ c·n; a non-concentration hypothesis on h is load-bearing, not
a nicety.** This is the same 2-separated / no-long-constant-run condition that CHT
Theorem 1.6 and the run's 2-separation hypothesis both point at.

```skeleton
goal: For the prime sequence, ν₂(q_n) ≥ c·n for an absolute constant c > 0 and all sufficiently large n, where ν₂(q_n) is the number of 2s in the maximal {0,2} suffix (0-2 cycle) of the right diagonal δ(q_n). This is strictly stronger than the demand n^{0.526} in granville-nu2-reduction, so it discharges GN-supply-nu2-density.
implies: |
  Let h ∈ {0,1}^{n-2} be the halved-gap parity bits, h[j] = ((p_{j+2} − p_{j+1})/2) mod 2,
  so h[j] = 1 ⟺ gap ≡ 2 (mod 4).

  (1) LINEARIZATION [G-supply-linearization, OPEN]  ν₂(q_n) = wt(Φ_n h), where Φ_n is the
      explicit F2 matrix whose (row, column) entry is [C(k,j) mod 2] over the fixed ancestor
      window columns [2, n-1] and tail rows k = K..n-2. This is rule90-interior-xor (each
      halved tail cell is the XOR of a Pascal-mod-2 window of the halved row-1 bits) composed
      with the proved ancestor-window interval fact: the row-1 ancestors of the tail cells
      (k, n-k), k = K..n-2, are exactly the fixed interval [2, n-1] of A_1.

  (2) WEIGHT TRANSFER [G-supply-weight-transfer, OPEN]  For the explicit family Φ_n, there is
      an absolute L such that any h ∈ {0,1}^{n-2} with no constant run (all-0 or all-1) of
      length ≥ L satisfies wt(Φ_n h) ≥ c·n for an absolute c = c(L) > 0.

  (3) NON-CONCENTRATION OF PRIMES [G-supply-nonconcentration, OPEN]  The prime h has no
      constant run of length ≥ L (with the same absolute L as in (2)).

  COMBINE: (1)+(2)+(3) give ν₂(q_n) = wt(Φ_n h) ≥ c·n. Since c·n > n^{0.526} for all large n,
  this discharges GN-supply-nu2-density; that lemma, with the proved GN-lemma54-runway
  (lemma54-re-derived-proof) and the discharged GN-demand-record-gap-bhp (BHP), proves GC by
  strong induction over n exactly as in granville-nu2-reduction.md.

  The two trivial killers — all-ones h and all-zeros h — are excluded by (3), and the fact that
  they are the ONLY asymptotic obstruction to wt(Φ_n h) = o(n) is the content of (2), which is
  the F2 nilpotence/involution classification, not a fresh dynamical claim.
status: sketched
rests-on: rule90-interior-xor, gilbreath-reduces-to-second-in-02, lemma54-re-derived-proof, granville-nu2-density-measured, los-2016-consecutive-pair-mod4-bias, bcz-2023-left-edge-stabilization, ducci-avart-nilpotent-concatenation
```

```gap
id: G-supply-linearization
lemma: ν₂(q_n) = wt(Φ_n h), where h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 is the halved-gap parity bit string and Φ_n is the explicit F2 matrix with entries [C(k,j) mod 2] over tail rows k = K..n-2 and ancestor columns j = 2..n-1 (the fixed ancestor window). Every halved tail cell equals the XOR of a Pascal-mod-2 window of h, and the union of ancestor windows over the tail rows is exactly [2, n-1].
status: open
next: |
  This is a write-down, not a conjecture: it is the composition of two already-established facts.
  (a) rule90-interior-xor (proved): a halved {0,2} cell at depth k equals XOR_j [C(k,j) mod 2]·h[base+j].
  (b) the ancestor-window interval fact, proved in the nu2_vs_gap_parity tool_builder session
      (research/out/code memo) but not yet promoted to a claim block: the row-1 ancestors of tail
      cells (k, n-k), k = K..n-2, form exactly [2, n-1].

  tool_builder task: extend code/gap_analysis/nu2_vs_gap_parity.py to emit Φ_n explicitly for
  samples n ∈ {50,100,200,400,800,1600,3200,3999} and verify wt(Φ_n h) == ν₂(q_n) exactly against
  the recorded nu2 values; also run the all-ones and all-zeros h through Φ_n to lock the convention
  (expected ν₂ = 0 both, confirming the weight-transfer hypothesis (3) below is necessary).
  theorem_prover task: state and prove the identity ν₂ = wt(Φ_n h) from rule90-interior-xor,
  and promote the ancestor-window interval to a claim with the same note.
thread: research/threads/regeneration.md
```

```gap
id: G-supply-weight-transfer
lemma: For the explicit F2 family Φ_n (as in G-supply-linearization), there is an absolute L such that every h ∈ {0,1}^{n-2} with no constant run of length ≥ L satisfies wt(Φ_n h) ≥ c·n for an absolute c = c(L) > 0. Equivalently: the only way wt(Φ_n h) = o(n) is for h to contain an all-0 or all-1 stretch of length growing with n — i.e. the weight of the Rule-90 fold of a non-concentrated bit string is linear.
status: open
next: |
  This is the combinatorial heart and it is genuinely open; it is the CHT inverse theorem / Ducci
  nilpotence classification in ν₂ coordinates, not a corollary of anything the run has proved.

  tool_builder task (feasibility, before any proof attempt): exhaustively over all h ∈ {0,1}^m,
  m ≤ 16, minimize wt(Φ h)/m subject to "no constant run ≥ L" for L = 3,4,5; report the worst-case
  ratio. If min wt/m stays bounded away from 0 as m grows, the lemma is numerically anchored and
  the honest target is a proof; if it decays, the lemma is FALSE as stated and must be repaired
  (a killed-by entry would be the result).

  theorem_prover task: reduce to the F2 involution/nilpotence structure already in the library.
  bcz-2023-left-edge-stabilization (proved) gives T² = id for the halved left-edge map and Υ⁶ = id,
  so the fold map is invertible (period 6); ducci-avart-nilpotent-concatenation gives that vectors
  killed by a fixed-depth cyclic Ducci power are exactly concatenations of blocks of power-of-2
  length. Together these say: h with wt(Φ_n h) = o(n) must be asymptotically periodic with period a
  power of 2, and every such non-constant string has constant runs of length ≥ 2^m — so a single
  absolute L breaks it. The first concrete theorem: the random analogue, wt(Φ_n h) = n/2 + O(√(n log n))
  with high probability for unbiased i.i.d. h (an Azuma bound over the XOR folds).
thread: research/threads/regeneration.md
```

```gap
id: G-supply-nonconcentration
lemma: The prime halved-gap parity string h[j] = ((p_{j+2} − p_{j+1})/2) mod 2 has no constant run of length ≥ L for some absolute L. Since h[j] = 1 ⟺ consecutive primes lie in different residue classes mod 4, an all-0 run is a stretch of consecutive prime gaps all ≡ 0 mod 4 (primes staying in one class mod 4), and an all-1 run is a stretch all ≡ 2 mod 4 (primes alternating class at every step).
status: open
next: |
  This is the prime-specific half and it is a clean analytic target, distinct from the combinatorics.

  tool_builder task (cheap, bounded): one pass over the first 10^6 prime gaps (sieve ≤ 1.6e7, O(n)
  memory, well under the cap) recording the longest all-0 run and all-1 run of h. Depth-1000 data
  suggests these are small (the run's own records show gaps mix mod-4 classes at ~60% transition),
  but the actual maximal run length is not recorded anywhere in the library.

  request_research task: unconditional bound on the longest run of consecutive prime gaps all ≡ 0 mod 4,
  or all ≡ 2 mod 4. Falsifier: a theorem or construction giving arbitrarily long runs of primes
  staying in a single class mod 4 (equivalently arbitrarily long stretches of gaps ≡ 0 mod 4) would
  kill (3) and require a weaker hypothesis — the honest demand is then only ν₂ > n^{0.526}, not c·n.
  Note los-2016-consecutive-pair-mod4-bias gives the *leading term* of the transition count only
  under the Hardy–Littlewood k-tuple conjecture; an unconditional constant-run bound is the real gap.
thread: research/threads/regeneration.md
```
