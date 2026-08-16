# CONCLUSION — the run's answer is NO

Terminus deliverable, written under directive 33 and amended under directive 34 (deliverable 5 folded in). This file is the closing
statement of the investigation: the single hypothesis GOAL.md put under test is
refuted, the problem closes as a clean negative, and exactly one open statement
survives. No new line of work is opened here; this file is meant to be the end.

---

## (1) The hypothesis, and the verdict

GOAL.md names one hypothesis:

> **Whether the fold `Φ` can be made to do work that the switch-density form
> cannot see** — i.e. whether `Φ_n` extracts an arithmetic signal from the prime
> gap-parity string `h` that the raw mod-4 switch-density reduction discards.

**Verdict: REFUTED.** Anchored to `code/out/pattern_finder_deliverable_3_fold_genericity.md`
(the pattern-finder deliverable 3): matched iid strings at the measured prime
switch density `p ≈ 0.585` reproduce the primes' dip counts and last-dip
positions essentially exactly —

| c | primes last-dip ≤ 7000 | random p=0.585 (trials) |
| --- | --- | --- |
| 0.45 | 763 | 699–996 |
| 0.48 | 5655 | 5595–6989 |

— so no measurable regularity of `ν₂` is prime-specific. The fold is doing no
observable work that the switch-density form cannot see. GOAL.md says that if
the hypothesis fails, say so and close the problem, and that a clean negative
is the second-best outcome. This is that outcome, taken.

```claim
id: goal-hypothesis-refuted-fold-adds-nothing-measurable
statement: >
  The single hypothesis under test — that the fold Phi does work the
  switch-density form cannot see, i.e. that some measurable regularity of
  nu2(n) = wt(Phi_n h) is prime-specific rather than fold-generic — is
  REFUTED. Matched iid strings at the measured prime switch density p ~ 0.585
  reproduce the primes' dip counts and last-dip positions essentially exactly
  (c=0.45: 763 vs 699-996; c=0.48: 5655 vs 5595-6989), so no measurable nu2
  statistic is prime-specific; the primes sit in the generic-balanced-good
  class and Phi contributes no observable work beyond the switch-density form.
hypotheses: canonical floored fold d in [2,n-1]; nu2(n) = wt(Phi_n h);
  S(n) = (n-2) - 2*nu2(n) exact; guard-checked prime h (nu2(53)=18,
  nu2(64)=27, nu2(4000)=1975, nu2(40000)=20081); random controls at the
  measured switch density p ~ 0.585 via the exact submask-zeta fold.
holds-here: yes (measured; exact over n=2..40000, random trials <= 8000).
status: measured-not-proved — the refutation is empirical: it shows no
  MEASURABLE regularity is prime-specific; it does not prove the unconditional
  equivalence SUPPLY <=> switch density.
bearing: >
  Closes the run's single hypothesis per GOAL.md as a clean negative. The
  fold adds no observable work the switch-density form cannot see; what
  survives is one unconditional arithmetic statement (section 5), which no
  measurement can reach.
anchor: code/out/pattern_finder_deliverable_3_fold_genericity.md ;
  research/notes/fold_genericity_all_nu2_regularities.md
```

---

## (2) What is PROVED

Each item with its evidence class, per the workspace rule that a proof, a
numerical check, and a sourced claim are never conflated.

- **Rank `n−2`, nullity 2, `ker = span(even-alt, odd-alt)`** (proved,
  all `n`). The full square submask-XOR matrix `Z[d][s] = [s ⊆ d]` is unit
  lower-triangular, so dropping rows `d=0,1` leaves `dim ker = 2`,
  `rank = n−2`; the two free directions are exactly `even-alt` and `odd-alt`,
  whose XOR is all-ones. Verified by exact `F₂` elimination `n=2..40`,
  exhaustive kernel census `n=2..12`, exhaustive `2ⁿ` enumeration `n=2..9`.
  Claim `fold-rank-n-minus-2-binomial-proved`; anchor
  `code/out/fold_alln_theorems.captured.txt`.

- **Surjectivity** (proved, consequence of the rank fact). Under the operative
  `(n−2)×n` row range `d=2..n−1`, `Φ_n` is surjective onto `F₂^{n−2}` and every
  image has exactly `4` preimages.

- **`wt(Φ_n h)` is exactly `Binomial(n−2, 1/2)` for uniform `h`** (proved,
  consequence of surjectivity). `E[wt] = (n−2)/2`, `Var(wt) = (n−2)/4`, hence
  `Var(ν₂/n) = (n−2)/(4n²) ≈ 1/(4n)`, and the `log(N)/(4N)` prefix-variance
  null is a consequence of a proved rank fact rather than a fit. Same claim
  `fold-rank-n-minus-2-binomial-proved`.

- **The telescoping identity, with its 438-mismatch control** (checked, exact
  arithmetic; algebraic telescoping over a two-valued boundary). For every
  `d ≤ 2¹⁴` the digital down-set `↓d` partitions into maximal runs of length
  `2^g` (`g = ν₂(d+1)`), count `2^(popcount(d)−g)`, and over any run `[u,v]`
  the fold cell telescopes: `XOR_{o∈[u,v]} h[pos+o] = [r_{pos+u} ≠ r_{pos+v+1}]`
  for a two-valued boundary `r` (prime case `r = q_j mod 4`). The two-valued
  boundary is load-bearing: replacing it with `r = q_j mod 3` breaks the
  identity with **438 mismatches over 620067 pairs** (first at `d=1 pos=0
  run=0-1`). Claim `g-run-telescope-verified`.

- **The endpoint-sign correction** (proved structural fact; no extra per-run
  sign). `(−1)^{T(n,d)} = ∏_R χ(r_{a_R}) χ(r_{b_R})`, with **no**
  `(−1)^{#runs(d)}` prefactor. The committed spurious form is false for every
  binary string at every odd `d` (hand proof at `d=3`), and fails 449 of the
  6868 `(n,d)` pairs `n=20..120` checked against the literal oracle, where the
  corrected form holds on all 6868. Claim `endpoint-sign-corrected-identity`;
  anchors `research/notes/refuter_endpoint_sign.md`,
  `research/notes/endpoint-sign-abandoned.md`.

- **`fold-distance-enumerator-On`** (proved, all `n`, no primes, no duality).
  The row family `M_d` is a meet-semilattice
  (`M_d ∩ M_{d'} = M_{d∧d'}`), so `|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} −
  2^{pc(d∧d')+1}`, and the distance enumerator
  `F_n(z) = Σ_{d,d'} z^{|M_d △ M_{d'}|} = O(n)` for every fixed `|z|<1`,
  uniformly in `n`. This closes the geometry side of the second-moment route.
  Claims `downset-row-intersection-meet-formula`,
  `fold-distance-enumerator-On`.

---

## (3) What is MEASURED, and to what ceiling

All measured, not proved; every number is exact over the stated range and
guard-checked.

- **Dyadic samples at `n = 2^k` (k = 3..25, `n` up to `2^25 = 33554432`) — a
  separate ceiling, NOT the `N = 40000` sweep.** Claim
  `dyadic-nu2-no-collapse-through-k25` (directive 36, exact integers): at the 23
  sample indices `n = 2^k, 2^k±1`, `ν₂(2^k)/2^k` stays at `1/2` —
  `ν₂(2^25)/2^25 = 16778104/33554432 = 0.50003` — and `|S(2^k)| ≤ 5282` (max at
  k=23; `S(2^25) = −1778`), so `|S|/n ≈ 1.6e-4` against the
  `0.04n = (1−2·0.48)n` falsifier threshold — three orders of magnitude past the
  `N = 40000` ceiling. Closed door 4 lives at powers of two; the fold does NOT
  collapse there for the primes. This is 23 sampled dyadic points, not a sweep:
  it does NOT extend the density-1 or dip-sparsity results, which remain
  measured only to `N = 40000`.

- **`μ_N = 0.499658` at `N = 40000`** (canonical floored oracle `s_sos`,
  entry guards `ν₂(53)=18`, `ν₂(64)=27`, `ν₂(4000)=1975`). The prime mean sits
  exactly on the fair-model `1/2` value.

- **The deep-tail density-1 signal at `c = None`.** The tail window
  `[0.9N, N] = [36000, 40000]` has **zero dips** at every `c = 0.40..0.49` —
  the first break is `c = None`, i.e. the sparsity does not break in the tail
  through `c = 0.49`. (All-ones and Thue-Morse controls both break at
  `c = 0.40`, tail density 1.0, as required.)

- **Ratio B falling `1.492 → 1.297` at `N = 80000`, with the decrement-ratio
  direction undecided.** `Ratio B = s2_N · 4N / log N` runs
  `1.443@1000 → 1.392@4000 → 1.361@10000 → 1.337@20000 → 1.315@40000 →
  1.297@80000`; the exact consecutive decrement ratios are
  `r_3 = 0.899404441`, `r_4 = 0.877780046` — the last step falls, but a single
  ratio is thin evidence, so whether the limit is 1 (primes asymptotically
  uniform for this statistic) or a constant above 1 (permanent structural
  excess) is **not decided** by the measured range. Both extrapolations are
  stated and neither is declared.

- **The ~9× Markov margin, and the mod-4 switch bias is fold-inert
  (deliverable 5).** The primes' centred lag-1 anticorrelation of `h` is
  `corr(h_j,h_{j+1}) = −0.152@500 → −0.0555@40000 → −0.0416@256000`, i.e.
  `1−2a ≈ −0.08` (switching prob `a≈0.52`); the fold second moment
  `E[S(n)²]/(n−2)` stays O(1) for two-state Markov inputs up to
  `|1−2a| ≈ 0.74` (`a≈0.87`, measured over `n∈[1024,49152]`), so the primes
  sit ~9× below the empirical collapse boundary. At the primes' parameters the
  bias is inert: `E[S²]/(n−2) = 1.004` for the primes (over `n∈[1024,20000]`)
  equals the O(1) level of iid at the same p and of a 2-state Markov at the
  primes' exact (p, ac1).

The whole of what was measured, and its genericity, is recorded in
`code/out/pattern_finder_deliverable_3_fold_genericity.md`; the atomic-level
mod-4 switch-bias measurement is
`code/out/pattern_finder_deliverable_5_mod4_switch_bias.md`.

---

## (4) The SIXTH CLOSED DOOR

The run adds one door to the five in `problem.md`:

> **No `ν₂` statistic is prime-specific.** Every measurable regularity of
> `ν₂(n)` — the white-noise law, the second-moment plateau, the finite
> exceptional sets, dip sparsity itself, and the mod-4 switch bias — is
> reproduced by matched iid (or same-parameter Markov) strings at the measured
> prime switch density `p ≈ 0.585`; deliverable 5 completes this at the atomic
> level.

Witness: the matched-iid control. Dip counts `[2,3000)`: at `c=0.45` primes 81
vs random 68–78; at `c=0.48` primes 367 vs random 355–371. Last-dip `≤ 7000`:
at `c=0.45` primes 763 vs 699–996; at `c=0.48` primes 5655 vs 5595–6989.

**Stronger witness — the mod-4 switch bias (deliverable 5).** The strongest
known prime-specific signal is Lemke Oliver–Soundararajan's switch-preference
for consecutive-prime residues mod 4 (`los-switch-preferred-mod4`,
`los-scale-bias-slowdecay`, asserted as conjecture), and it is fold-inert.
Over the first N primes the switch density is `p(N)=0.5788@40000` and the
lag-1 anticorrelation of `h` is `−0.0555@40000 → −0.0416@256000`, with
`|corr|·√N` climbing 3.4→21.1 (persistent, not noise) and decaying at the LOS
`loglog N / log N` scale. Yet `E[S(n)²]/(n−2) = 1.004` for the primes
(`n∈[1024,20000]`) is the same O(1) level as iid at the same p and as a 2-state
Markov with the primes' exact (p, ac1): the one persistent prime-specific
raw-input statistic confers no second-moment advantage under Φ.

```claim
id: sixth-door-no-nu2-statistic-prime-specific
statement: >
  SIXTH CLOSED DOOR. No measurable statistic of nu2(n) is prime-specific:
  matched iid strings at the measured prime switch density p ~ 0.585 reproduce
  dip counts and last-dip positions essentially exactly (dip counts [2,3000):
  c=0.45 primes 81 vs random 68-78; c=0.48 primes 367 vs random 355-371;
  last-dip <= 7000: c=0.45 primes 763 vs 699-996; c=0.48 primes 5655 vs
  5595-6989). Stronger atomic witness (deliverable 5): the Lemke
  Oliver-Soundararajan mod-4 switch preference -- the strongest known
  prime-specific signal (los-switch-preferred-mod4, los-scale-bias-slowdecay,
  asserted conjecture) -- is real and persistent in h (switch density
  0.5788@40000; lag-1 corr -0.0555@40000 -> -0.0416@256000, |corr|sqrt(N)
  3.4 -> 21.1) yet FOLD-INERT: E[S(n)^2]/(n-2) = 1.004 for the primes equals
  the O(1) level of iid at the same p and of a 2-state Markov at the primes'
  exact (p, ac1). The primes sit in the generic-balanced-good class.
hypotheses: canonical floored fold d in [2,n-1]; guard-checked prime JSON;
  random controls at p ~ 0.585 via the exact submask-zeta fold.
holds-here: yes (measured; exact over n=2..40000, trials <= 8000).
status: measured-not-proved — a door (a refuted structural hypothesis), exact
  over the measured range and a conjecture for all n.
bearing: >
  problem.md result type 6. It kills the last candidate route to a
  prime-specific regularity and, together with the five problem.md doors,
  completes the negative: Phi has no output regularity the switch-density
  form cannot see. Deliverable 5 completes this at the atomic level -- the
  one persistent prime-specific raw-input signal, the mod-4 switch bias, is
  fold-inert -- so this stays ONE door with a stronger witness, not a seventh
  door. What survives is only an unconditional arithmetic bound (section 5),
  unreachable by any measurement.
anchor: code/out/pattern_finder_deliverable_3_fold_genericity.md ;
  code/out/pattern_finder_deliverable_5_mod4_switch_bias.md ;
  research/notes/fold_genericity_all_nu2_regularities.md
```

---

## (5) The single surviving open statement

**An unconditional second-moment or submask-window Walsh bound on the prime
gap-parity string** — concretely, prove `E[S(n)²] = O(n)` (equivalently
`S(n) = O(√n)`, equivalently a submask-window second-moment bound on `h`) for
the *specific* prime string `h`, from an arithmetic input strictly weaker than
pointwise mod-4 switch density.

**The index-versus-value obstruction** (added by the operator at shutdown from
`research/grounding_three_current_proposals.md`, which the run produced but did
not fold in before it was stopped). The reason the literature does not reach
this statement is structural, not a matter of not having found the right paper:
the object lives in the **prime index**, not the prime value. Value-domain tools
— log-Chowla over integer arguments, value-shifted character sums,
short-value-interval moments — are therefore inapplicable by construction, and
this single fact accounts for eight dead candidate routes at once. Any future
attack must either work in the index domain or supply a transfer between the
two.

**Equivalence is the indicated answer** (same source, same caveat). Every
second-moment and correlation object built here collapses, at the coarsest
dyadic scale `g=0`, to the mod-4 switch-pair correlation. Across eight
candidates that collapse was universal. It is an *observed pattern*, not a
theorem — the run was stopped before it could say which — but it indicates that
SUPPLY is **equivalent** to the switch-density statement, which is result type 5
in `problem.md` and would close this problem honestly. Proving or refuting the
`g=0` collapse as a theorem is the highest-value remaining question, and is
sharper than the open statement above.

Why it survives, and why no measurement reaches it:

- The geometry side is proved (`fold-distance-enumerator-On`): the second-moment
  route reduces density-1 SUPPLY to exactly this one arithmetic input, and by
  Chebyshev it gives `ν₂/n → 1/2` on a density-1 set.
- But every *measurable* regularity is fold-generic (section 4): the
  `√n` white-noise plateau and the `O(n)` second moment are reproduced by iid
  input at `p ≈ 0.585`, so the data cannot distinguish the primes from the
  generic-balanced class. A bound valid for all balanced strings would be
  false (Thue-Morse, same density `1/2`, collapses); a bound that separates the
  primes from Thue-Morse needs an unconditional arithmetic statement about the
  primes, and that is the parity barrier — pointwise for the switch-density
  form, and not porous to any statistic the measurement frontier can reach.
- Therefore the statement is open exactly as an unconditional theorem; finite
  computation, however far it is pushed, cannot close it.

This is the honest endpoint: the fold adds no measurable work beyond the
switch-density form, and the one statement that could have given the fold a
role — an unconditional second-moment/submask-Walsh bound on the prime string —
is unreachable by measurement and unproven.
