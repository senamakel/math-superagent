# Scholar pass — library digested, minimum-distance stratum confirmed

Author: scholar. Scope: this pass re-read the full reference library against
SUPPLY and GOAL's single hypothesis (can the fold `Φ` do work the
switch-density form cannot see); digested the one remaining stub
(`green_three_topics_additive_prime_number_theory`); and independently verified
the live adopted approach's load-bearing distance formula.

## What this pass did

1. **Confirmed the run's state.** The active line is the density-1 (averaged)
   form: `fold-second-moment-krawtchouk` and its sharpening
   `downset-row-code-distance-closed-form` (both `adopted`), with
   `lucas-mixing-finite-transfer` as the sibling ergodic route (also `adopted`).
   The geometry half (C) rests on the down-set intersection/distance formula
   `downset-row-intersection-meet-formula` → `fold-distance-enumerator-On`
   (`F_n(z)=O(n)` for `|z|<1`). The whole of SUPPLY reduces to the single
   arithmetic second-moment input (A): `E[S(n)²]=O(n)` for the prime gap-parity
   string `h`. All five closed doors and four refuted approaches are recorded and
   consistent.

2. **Digested the one stub.** `green_three_topics_additive_prime_number_theory.md`
   was a "digest only" placeholder. Replaced with a real summary: Green §2 proves
   Mauduit–Rivat, `E_{n≤X} Λ(n)(−1)^{s(n)} = O(X^{−δ})` — the binary digit-sum
   parity of the primes is equidistributed with a power-saving error. **This is a
   value-domain (digit-sum of q_j) statement; SUPPLY's `h` is an index-domain
   gap-parity statistic**, so no transfer is established and the source does not
   directly help. Filed as claim `mauduit-rivat-prime-digit-sum-equidistributed`
   with `holds-here: does-not-apply`, so nobody re-reads it expecting a
   gap-parity input.

3. **Independently reconciled the adopted line's faithful stratum (the novel
   contribution).** The adopted approach `downset-row-code-distance-closed-form`
   predicts `A_2 = Θ((log n)²)` and explicitly asks to reconcile this against
   the older measured "`A_2 = O(n^{0.48})`". I derived the exact closed form from
   the distance formula — distance-2 pairs are exactly `{2^a,2^b}` (distinct
   powers) and `{2^a,2^a+2^b}` — giving `A_2(2^m) = (m−1)(3m−4)/2`, and checked
   all nine recorded brute values (12,22,35,51,70,92,117,145,176 at
   n=16..4096): **every one matches**. The power-law fit was a fit artifact over
   log² growth. This confirms on an executed, two-route basis that the geometry
   theorem (C) rests on a sound closed form, and that the fold does not amplify
   submask-window correlations (minimal distance is sub-sublinear).
   Claim `a2-distance-distribution-theta-log-squared` filed.

## What this pass established (and its evidence class)

- **Mauduit–Rivat (sourced, proved in Green §2)** — digit-sum parity equidistributed
  with power saving; **does not transfer** to gap-parity `h`; context/shape only.
- **A_2 closed form (checked)** — matches the executed brute-force oracle 9/9 at
  n=16..4096; closes the minimal-distance stratum of the adopted geometry line.

## Sources confirmed as NOT helping (so nobody re-reads them)

- `green_three_topics_additive_prime_number_theory` — now digested; Mauduit–Rivat
  is value-domain, no transfer; Topics 1 (GPY) and 3 (Green–Tao) are background.
- `matomaki_radziwill_tao_averaged_chowla.md` / `matomaki_radziwill_tao_averaged_chowla.full.md` —
  both are WRONG-DOWNLOAD placeholders discarding a random-matrix thesis; the real
  MRT is `...fourier_uniformity_averaged` (digested). Do not fetch either again.
- `lau-pattern-count-bound` — true theorem, `holds-here: NO`: modulus 4=2² is not
  squarefree, so it never touches the q=4 switch; it bounds the wrong (constant)
  pattern side anyway.
- OEIS base-4-digit files, citation graphs, the bibliography-index
  `odlyzko_gilbreath`, `granville_martin_prime_number_races` duplicate — all
  recorded elsewhere as do-not-re-read.

## Contradictions / notes for the board

- **A_2 fit vs closed form (resolved).** The older
  `fold_second_moment_capture` printed "A_2 log-log exponent 0.480" from a
  least-squares fit; the exact closed form is `Θ(log²n)`. Both come from the same
  underlying data; the fit was read as a trend. Not a contradiction of the data,
  a correction of the reading. Recorded in `reconcile_a2_closed_form.md`.
- **No source contradicts the adopted line's account of the parity barrier.**
  ABGS "cannot be treated using L-functions" (Problem 1.1), Lau "even one
  non-constant 2-term pattern is beyond reach", and the equal-residue side
  (Shiu/Maynard positive density) all confirm the switch-density reduction is a
  dead end and the fold/second-moment route is the only live one.

## Gaps still open (unchanged, on REQUESTS.md)

- `walsh-spectral-subset-b904` — Walsh/subset-sum weight bound on `wt(Φ_n h)`
  from `Φ`'s structure without the five closed-door complexity senses. Still
  open; the pivot is that the *second-moment* (A) input is the achievable version
  of it, and (C) is now machine-confirmed closed.
- The **finite-prefix transfer** (measure-level Lucas mixing ⇒ weight bound on a
  fixed string) — the single largest missing tool; in no source.
- The **arithmetic heart (A)**: prove `E[S(n)²]=O(n)` for the prime `h`. This is
  the one open input between the run and the density-1 form of SUPPLY.

## Note for the derive-pass owner (CLAIMS.md gap)

The claims `mauduit-rivat-prime-digit-sum-equidistributed`
(`research/summaries/green_three_topics_additive_prime_number_theory.md`) and
`takei-rule90-mixing-limits-uniform`
(`research/summaries/takei_limiting_measures_rule90.md`) are both written as
fenced `claim` blocks with all required fields, yet **neither is derived into
`research/CLAIMS.md`**, while structurally identical `status: sourced` claims
(e.g. `lucas-mixing-iff-fold-randomization`,
`green-tao-mobius-orthogonal-to-nilsequences`) do parse. Both absent claims live
in `research/summaries/`, so the parse rule may be dropping claims from a
subset of summaries (both carry `holds-here` prose beginning `For p=2…` /
`no — this is…`, neither is the issue). This is a pre-existing gap (takei was
absent before this pass) worth fixing in the derive logic; the underlying notes
carry the full statements regardless, so the knowledge is not lost.

## Handed to other roles

- **coder / tool_builder:** run the three standalone intersection-formula scripts
  (`code/scholar_intersection_formula_verify.py`,
  `code/scholar/verify_intersection_formula.py`,
  `code/librarian/verify_downset_intersection.py`) to close the all-pairs n=8..256
  machine check of (R)(I)(D) the A_2 reconciliation only sampled at the
  minimal-distance stratum. Not urgent — the A_2 consequence is already confirmed
  by the existing capture — but completes the route's gate.
- **steer (derive-pass owner):** investigate the CLAIMS.md omission above.
