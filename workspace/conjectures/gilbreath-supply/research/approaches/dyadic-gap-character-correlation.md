# The fold is a dyadic-gap correlation of the quadratic character (−1/q) — endpoint character-sum route

```approach
idea: >
  Fuse the Möbius/ANF reading of the fold (candidate 1, correct but inert as a
  relabeling) with the on-disk run-telescope, and fix its sign. The image
  coordinate T(n,d) = ⊕_{o⊆d} h[n−1−d+o] telescopes run-by-run to endpoint
  comparisons of the mod-4 residue string r, and EVERY run of the down-set ↓d has
  the SAME length 2^{ν₂(d+1)}. Hence depth d reads the primes only at pairs
  (a, a+2^{ν₂(d+1)}) — a single dyadic shift. Exponentiating, the character sum
  controlling ν₂ collapses to

      (−1)^{T(n,d)} = ∏_{R ∈ runs(↓d)} χ(r_{a_R}) χ(r_{b_R}),
      S(n) := Σ_{d=2}^{n−1} (−1)^{T(n,d)} = Σ_{d=2}^{n−1} ∏_R χ(r_{a_R})χ(r_{b_R}),

  with NO extra (−1)^{#runs(d)} factor (the on-disk skeleton's factor is spurious;
  hand-verified d=2 and d=3). Since r_j = q_j mod 4 ∈ {1,3} for odd primes and χ
  is the nontrivial character mod 4, χ(r_j) = (−1/q_j) — the Legendre symbol of
  −1, i.e. (−1)^{(q_j−1)/2} (quadratic reciprocity: the quadratic character of
  conductor 4). So SUPPLY is exactly: the sum of products of the quadratic
  character (−1/·) along the primes, over dyadic-shift-structured index pairs,
  is o(n) — and by `excess-is-negative-character-sum` (checked on disk),
  ν₂(n) = (n−2−S(n))/2.

mechanism: >
  Three independent structure facts reduce ν₂ to a named arithmetic object.
  (1) Lucas ⇒ the fold is the down-zeta: T(n,d) = ⊕_{o⊆d} h[n−1−d+o]
  (lucas-submask-odd, problem.md facts 1–2). (2) The down-set ↓d is a disjoint
  union of 2^{popcount(d)−ν₂(d+1)} runs, each of length 2^{ν₂(d+1)} — the
  run-telescope G-run-telescope. Within a run [u,v], adjacent switch indicators
  telescope: ⊕_{o∈[u,v]} h[j+o] = [r_{j+u} ≢ r_{j+v+1}], so
  T(n,d) = ⊕_R [r_{a_R} ≢ r_{b_R}] with b_R − a_R = 2^{ν₂(d+1)} for every run.
  (3) [r_a ≢ r_b] = (1 − χ(r_a)χ(r_b))/2 over the nontrivial character χ mod 4,
  so (−1)^{[r_a≢r_b]} = χ(r_a)χ(r_b), giving the product identity above. The
  character is the single quadratic Dirichlet character of conductor 4:
  χ(r_j) = (−1/q_j) = (−1)^{(q_j−1)/2}. Thus the whole of SUPPLY is a
  correlation bound for one quadratic character at dyadic shifts — the arithmetic
  input is a statement about (−1/q_j)(−1/q_{j+2^g}) and higher products, NOT
  about adjacent switch density (gap 1). This is orthogonal to the ABGS
  switch-density dead end in the same sense the Lucas-mixing precision note
  established for Bernoulli(ρ): it tests pattern correlations at non-adjacent,
  dyadic separations, not the nearest-neighbour mean.

status: refuted

precedent:
  - "Run-telescope and down-set run structure (G-run-telescope): ↓d decomposes
    into runs of length 2^{ν₂(d+1)}, count 2^{popcount(d)−ν₂(d+1)}; telescoping
    over a run gives an endpoint comparison of the mod-4 residue string. On disk
    in research/backward/supply-from-endpoint-parity.md (status: open, not yet
    machine-grounded)."
  - "Character-sum bridge: 2·ν₂(n) − (n−2) = −S(n) exactly (claim
    excess-is-negative-character-sum, checked: brute + SOS)."
  - "Quadratic character identification: χ mod 4 is the nontrivial character,
    χ(r_j) = χ(q_j) = (−1/q_j), the Legendre symbol of −1 = (−1)^{(q_j−1)/2}
    (quadratic reciprocity; the unique quadratic character of conductor 4)."
  - "The F₂ zeta/Möbius transform is self-inverse (supply-fold-submask-zeta-involution,
    checked) — subsumes candidate 1's ANF dictionary as the transform step."
killed-by: >
  The route's own falsifier fired (tool_builder, this attempt). S(n) stratified by
  popcount(d) for the primes at n=400/1000/4000 (exact SOS, cross-checked vs
  s_direct and s_char_runs; S(4000)=48 -> nu2=1975 matches canonical) shows NO
  low-popcount (few-run) stratum dominates S(n): largest per-stratum |sum|/n is
  0.0375@400 -> 0.020@1000 -> 0.008@4000, shrinking with n, weight spread across
  p=1..11, essentially the same profile as a random-{1,3} control. The route's
  premise (bulk of S(n) in few-run strata where a pointwise single-dyadic-shift
  correlation bound on chi(r)=(-1/q) could bite) is falsified on finite inputs;
  the needed arithmetic input is as strong as the mean, so the route collapses
  toward plain switch density. The corrected identity (-1)^{T(n,d)}=prod_R
  chi(r_a)chi(r_b), no spurious (-1)^#runs factor, is verified on all 6868
  (n,d) pairs for n=20..120 against the literal oracle (spurious form fails 449
  pairs incl. d=3), but the so-grounded identity is inert for a bound.
  Captures: code/out/dyadic_stratify_by_popcount.captured.txt,
  code/out/dyadic_verify_character_identity.captured.txt. Measured, not proved.
open-step: >
  The arithmetic heart, now named precisely: bound the dyadic-gap correlation of
  (−1/·) along the primes. Candidate weak inputs, in increasing strength: (i) for
  each fixed g, Σ_{j≤N} χ(r_j)χ(r_{j+2^g}) = o(N) (single dyadic-shift
  autocorrelation of the character along primes); (ii) a second-moment bound
  E[(−1)^{T(n,d)}·(−1)^{T(n,d')}] = o(1) averaged over (d,d'), which via the
  zeta involution is a statement about the symmetric differences ↓d △ ↓d′; (iii)
  full bounded-correlation of χ(r) with every 2-regular index template. Each of
  (i)–(iii) is strictly weaker-sounding than positive adjacent switch density and
  must be priced against it; (i) is the cheapest and is a genuine, possibly
  provable, arithmetic statement (equidistribution of (−1/q) at dyadic shifts).
  None of (i)–(iii) reopens the five closed doors: they are statements about the
  character values χ(r_j), not about h's weight, runs, aperiodicity,
  anti-dyadicity, or periodicity.
first-step: >
  tool_builder, pure F₂ + character arithmetic, no number theory beyond the real
  prime residue string r_j = q_j mod 4 (available): (1) verify the corrected
  identity (−1)^{T(n,d)} = ∏_R χ(r_{a_R})χ(r_{b_R}) against brute submask-XOR for
  n ≤ 200 and ALL d ∈ [2,n−1], with an explicit assertion that the spurious
  (−1)^{#runs(d)} factor is absent (fails on d=3, passes on the corrected form),
  and a random-{1,3} negative control; (2) verify the run-count/length formula
  (2^{ν₂(d+1)} length, 2^{popcount(d)−ν₂(d+1)} count) for d ≤ 2^14; (3) compute
  S(n) = Σ_d (−1)^{T(n,d)} stratified by popcount(d) for n up to the oracle
  ceiling, and print the per-stratum partial sums — the falsifier: if the bulk of
  S(n) comes from low-popcount (few-run) strata where a pointwise dyadic-gap
  correlation bound can be applied, the route is live; if every stratum carries
  full n-weight, the correlation input needed is as strong as the mean and the
  route collapses to switch density (GOAL priority 3).
```

## Why this is the fusion, and why it beats the three candidates

The research pass closed candidates 2 and 3 (Kummer valuation lift cannot
propagate without full 2-adic residues; Mahler's sparse-window ⇒ finite-2-kernel
inference fails on global-vs-local grounds) and judged candidate 1 correct but
inert — a relabeling that hands the problem to the Reed–Muller weight spectrum,
itself open (Carlet). But research also named the live target: **the
second-moment / Walsh bound on the character sum S(n) = Σ_d (−1)^{T(n,d)}**,
i.e. GOAL.md priority 2. This approach is that target, made concrete by two
things neither I nor research had named:

1. **The corrected sign.** The on-disk skeleton
   (`supply-from-endpoint-parity.md`, gap G-endpoint-comparison-density) carries
   a spurious `(−1)^{#runs(d)}` factor in its character-sum form. It is wrong:
   `(−1)^{⊕_R [switch_R]} = ∏_R (−1)^{[switch_R]} = ∏_R χ(r_{a_R})χ(r_{b_R})`
   with no sign, because each run telescopes independently. Hand-verified d=2
   (two runs) and d=3 (one run, where the spurious sign would flip the value).
   Fixing it turns S(n) from a signed mess into a clean product.

2. **The dyadic-gap uniformity.** All runs of ↓d share the length
   `2^{ν₂(d+1)}`, so depth d compares the residue string r only at separation
   `2^{ν₂(d+1)}`. The fold reads **one dyadic shift per depth**, not an
   unstructured family of pairs. And `χ(r_j) = (−1/q_j)` — the Legendre symbol
   of −1, the unique quadratic character of conductor 4 — so the whole object is
   a sum of products of a single quadratic Dirichlet character along the primes
   at dyadic shifts. That is a named, literature-friendly object
   (quadratic-character correlations), which the ANF/RM "spread spectrum"
   language never exposed.

This is distinct from every closed door: it bounds the character's dyadic-gap
correlations, not h's weight/runs/aperiodicity/anti-dyadicity/periodicity, and
distinct from the refuted Walsh-subset-sum route, which sought a bound from Φ
alone — here the bound comes from the arithmetic of χ(r_j) = (−1/q_j), which Φ's
kernel vectors cannot kill (all-ones h corresponds to r alternating 1,3,1,3,…,
whose dyadic-gap character products are deterministic and their sum is exactly
the kernel collapse — a control to be exhibited).

## Relation to the concurrent `fold-second-moment-krawtchouk` approach

A sibling school has concurrently adopted `fold-second-moment-krawtchouk`: the
same S(n) bridge, but analysed through the **distance distribution of the row
code** (Delsarte/MacWilliams/Krawtchouk), which factorises the collapse into a
pure-Φ_n combinatorial term plus a single submask-autocorrelation input on h.
The two routes are **complementary, not rivals**: this file supplies the
*arithmetic identity* (what S(n) actually is, as dyadic-gap products of
(−1/q_j)) that the Krawtchouk route leaves as an abstract input; the Krawtchouk
route supplies the *geometry engine* (does Φ itself amplify submask
correlations, i.e. is its row-code distance distribution front-loaded) that this
file's character sum must eventually be tested against. The Krawtchouk route
subsumed candidate 1's ANF dictionary as a lemma (its file says so); this file
independently subsumes it as the zeta-transform step. That is the same identity,
used twice, and both uses are legitimate.

## Verification status (honest)

- `lucas-submask-odd`, `supply-fold-submask-zeta-involution`,
  `excess-is-negative-character-sum`: **checked** on disk.
- Run decomposition + telescoping (G-run-telescope): **checked** on disk —
  `code/gfold/g_run_telescope_verify.py` now runs and its capture
  `code/out/g_run_telescope_verify.captured.txt` verifies C1 (run structure,
  d = 0..2^14 = 16385 values) and C2 (telescoping identity) on the real
  prime-residue h (brute element enumeration d≤2^10 × 51 positions = 52275
  pairs; prefix-XOR full d≤2^14 × 101 positions = 1654885 pairs) and on 6
  random-h controls (313650 brute + 9929310 prefix pairs), ALL PASSED.
  Claim `g-run-telescope-verified` filed.
- Corrected sign identity (−1)^{T(n,d)} = ∏_R χ(r_a)χ(r_b): **hand-verified
  here for d=2 and d=3**; general case follows from run-by-run telescoping, but
  machine verification for all d ≤ 200 is the first step's gate, not yet run
  (inventor holds no execution tool).
- χ(r_j) = (−1/q_j): **sourced/classical** (quadratic reciprocity; the unique
  quadratic character of conductor 4). Note this is −1's symbol, NOT 2's — the
  first draft of this file wrongly wrote (2/q_j); corrected here.
- Nothing above is a claim of SUPPLY; it is a reduction. The arithmetic gap
  (dyadic-gap correlation of (−1/·) along the primes) is stated and priced, not
  proved.
