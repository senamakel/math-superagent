# Shared context

The library is populated and the run has computed results. `research/CLAIMS.md`
holds ~40 claim blocks digested from the on-disk sources (ABGS §1/§9, Lemke
Oliver–Soundararajan, Shiu, Freiberg, Maynard, Rampersad–Wiebe, Bacher,
Szechtman, Pivato–Yassawi, Takei); `code/out/` carries this run's captures.
The `ν₂ = wt(Φ_n h)` oracle is the submask-product SOS transform, cross-checked
against a direct brute oracle (`s_sos == s_direct` on n=8..60). The
literal-vs-fold grounding defect is resolved (directive 6): the unfloored
bottom-end reading is identically 0 for every n≥2 because the bottom cell
`A_{n−1}(0)` is always 1, so the floor `k∈[2,n−1]` is load-bearing and
`literal_suffix_nu2` is the labelled negative control, not a bug. The
operative definition is the floored one; `wt(Φ_n h)` is a theorem about it.
`problem.md` is **not authoritative**: three imported values were wrong and
computation caught all three — treat every imported number as a claim to check
and keep printing the stated value beside the run's own.

**Claims renderer caveat (directive 15, live in this container):** the harness's
CLAIMS.md renderer mapped `status: measured` to `asserted` — `Status::parse` had
no `measured` variant — so every claim labelled "measured, not proved" rendered
in the derived table as "asserted by the source", the opposite of what happened.
That is a harness bug, fixed in the repository (not this container) with a
regression test. Until restart, do not treat the derived proved/checked/asserted
counts as evidence, do not relabel measured work "checked" to fix the table, and
keep writing "measured, not proved".

## Sources on disk (digested into claims; not all full texts downloaded)

The earlier run left these under `research/`. Each has a summary under
`research/summaries/`; most have a full text under `research/sources/`. The
bearings below are now carried as claim blocks in `research/CLAIMS.md`, so treat
this table as a pointer, not as evidence.

| Source | File (summary / full) | What it bears on |
| --- | --- | --- |
| Odlyzko 1993, *Iterated abs. values of differences of consecutive primes*, Math. Comp. 61 | `summaries/odlyzko_iterated_abs_values_diff_primes.md` / `sources/...full.md` | The absolute-difference triangle itself; Gilbreath verified to `10^13`; the `G(N)`/0-or-2 stop-block structure — closest direct prior work on this exact object |
| Lemke Oliver & Soundararajan 2016, *Unexpected biases... consecutive primes*, PNAS | `summaries/lemke_oliver_soundararajan_bias.md` / `sources/...full.md` | Consecutive-prime residue-pair biases — the object the switch-density reduction is about; conjectural (HL) explanation |
| Matomäki & Radziwiłł 2016, *Multiplicative functions in short intervals*, Ann. Math. 183 | `summaries/matomaki_radziwill_multiplicative_short_intervals.md` / `sources/...full.md` (arXiv:1501.04585) | Value-domain short-average cancellations of bounded multiplicative functions (μ, λ). Named engine of the **refuted** `matomaki-radziwill-index-autocorrelation` approach (not multiplicative in the prime index; g=0 = switch-density barrier) |
| Matomäki, Radziwiłł & Tao 2020, *Fourier uniformity ... short intervals on average*, Invent. Math. 220 | `summaries/matomaki_radziwill_tao_fourier_uniformity_averaged.md` / `sources/...full.md` (arXiv:1812.01224) | Quantified averaged correlations of multiplicative functions vanish. Same refuted approach as above; value-domain only, the index transfer it needs is exactly what the refutation says it cannot give |
| Green & Tao 2012, *Möbius function strongly orthogonal to nilsequences*, Ann. Math. 175 | `summaries/green_tao_mobius_nilsequences.md` / `sources/...full.md` (arXiv:0807.1736) | μ orthogonal to nilsequences with log-savings. Named engine of the **refuted** `gowers-u2-nilsequence-uniformity` approach (basis mismatch: fold on ANF/zeta basis, not Walsh/U²) |
| Ash, Beltis, Gross & Sinnott 2011, *Frequencies of successive pairs of prime residues*, Exp. Math. | `summaries/citations_w2027719385.md` (citation graph only, not read) | The named open problem `problem.md` says switch-density reduces to: frequency of consecutive-pair residues mod m |
| Encyclopedia of Math, *Gilbreath conjecture* | `summaries/encyclopedia_gilbreath.md` / `sources/...full.md` | Background; Gilbreath is out of scope, do not claim |
| Odlyzko paper list | `summaries/odlyzko_gilbreath.md` / `sources/...full.md` | Bibliography; not itself a result |
| Shiu 2000, *Strings of congruent primes*, J. London Math. Soc. | `summaries/shiu_strings_congruent_primes.md` + `summaries/shiu_strings_expository.md` / `sources/shiu_strings_expository.full.md` (Ethan Yang's freely-available expository of the primary, which is Wiley-paywalled) | `problem.md` fact 5's cited input: arbitrarily long runs of consecutive primes in one class mod 4. **Sourced here via the expository full text** (theorem `shiu-string-theorem`, verified against the expository Thms 1.1/1.2/4.1). The primary paper itself was not downloaded (Wiley cookie wall), but its content is fully reproduced by the expository. |

## The target (per `problem.md`)

**SUPPLY**: exists `c > 0` with `ν₂(n) ≥ c·n` for all large `n`, where `ν₂(n)`
counts 2s in the maximal {0,2} suffix of the right diagonal `δ_k(n) = A_k(n−1−k)`
through the absolute-difference triangle of the primes. Convention: suffix
floored at index 2 (`lib.rightdiag.cycle_and_nu2`); pick one, state it, keep it.
Identical to a `2`-suffix floored at index 0 up to ±1, asymptotically unchanged.
Never materialise the triangle (parent run OOM-killed at depth 4000); stream one
row at a time and collect only the single diagonal cell per depth.

## Asserted by `problem.md`, unverified here

Claims the file lists as "established" but that **no workspace artifact
supports** (not even a source on disk, in most cases). If the run relies on any,
it must re-derive or source it first. GP = "Gilbreath parent workspace", which
is **not reachable from this workspace** — citing it is impossible here.

1. **Linearisation.** `ν₂(n) = wt(Φ_n h)` over F₂, with `h[j] = ((q_{j+1}−q_j)/2) mod 2`
   and `Φ_n` the Pascal-mod-2 fold with entries `C(k−1, j−(n−k)) mod 2`. (Asserted; no derivation on disk.)
2. **Lucas.** `C(d,i) mod 2 = 1` iff `i` binary-submask of `d`. (True classical theorem; sourceable, but uncited here.)
3. **Kernel (corrected, directive 5).** `rank Φ_n = n−2` — **full row rank** — nullity 2, `ker Φ_n = span(even-alt, odd-alt)` with all-ones = even-alt ⊕ odd-alt. Machine-verified n = 2..20 (`fold-rank-is-n-2-nullity-2-alternating`); the all-n proof is the unit-lower-triangular submask-XOR argument (task `prove-fold-rank-all-n`). The old "rank n−3, nullity 1, ker = span(all-ones)" is wrong and fits no row-range convention — do not re-import it from any summary or note that still carries it. Full row rank means Φ_n is **surjective onto F₂^{n−2}**, the opposite of "nearly singular".
4. **Dyadic collapse.** Eventually-periodic `h` with power-of-two period ⇒ `ν₂(n) = O(1)`. "Proved from (1)+(2)" — proof absent here.
5. **Primes not eventually periodic.** "Proved, conditional on Shiu 2000, held at abstract level only" — the file itself flags this as **conditional, not proved**. The Shiu 2000 content (arbitrarily long constant mod-4 runs) is **sourced locally** via the Ethan Yang expository (`sources/shiu_strings_expository.full.md`, claim `shiu-string-theorem`); only the primary paper's own PDF is absent (Wiley paywall), and its theorem is fully reproduced by the expository.

## Measured (this run's own sweep; range operator-corrected)

`code/out/averaged_mean_capture.txt`, exact, convention d ∈ [2, n−1]:

| quantity | value |
| --- | --- |
| `ν₂(n)/n`, primes, n=50..4000 | min 0.3396, max 0.6170 (corrected — the old 0.42..0.52 was a sampled sub-window; claim `nu2-range-measured-wider`) |
| Cesàro mean `M(n)` of `ν₂/n`, primes | 0.4394 (n=100) → 0.4973 (n=4000), rising |
| Cesàro mean, Thue–Morse | 0.2255 → 0.0641, falling |
| Cesàro mean, all-ones (kernel vector) | 0.0000 throughout |
| `ν₂/n` at n=4000 | 0.4938 (literature 0.4933) |

Indicated truth `c ≈ 0.49`; even the min 0.34 is bounded away from 0. The
separation is clean and is **GOAL.md priority 1** — push the averaged form
(thread `averaged-mean-structure`).

**Fair model is PROVED, not measured (directive 10).** `code/out/fair_model_exact.txt`
is stronger than it was labelled: rank `Φ_n = n−2` (full row rank, nullity 2)
makes `Φ_n` surjective onto `F₂^{n−2}`, so every image has `2² = 4` preimages,
and for `h` uniform on the cube `wt(Φ_n h)` is **exactly Binomial(n−2, 1/2)** —
the table (`4·C(10,k)` at n=12) is the confirming check, not the evidence.
Corollary (Chernoff): SUPPLY holds for a uniformly random `h` with probability
`1 − exp(−cn)`. So the decaying `s2_N ≈ 1/N` is the fair-model prediction
(`Var(ν₂/n) = (n−2)/(4n²) ≈ 1/(4n)`), **not** prime-specific evidence; the
measured prime mean `0.4977` sits on the random prediction `1/2`. This touches
**none** of the five closed doors (it is about the fold on uniform input, not an
"h is complicated enough" hypothesis) — the whole remaining difficulty is that
the primes are not known to be non-adversarial for this fold (thread
`fair-model-non-adversarial-reframing`, tasks
`establish-fair-model-exact-binomial-proved`, `fair-model-variance-ratio-null`).

**Pointwise ceiling now N = 40000** (directive 8; claim
`smax-decay-through-40000`, status measured-not-proved): the streamed pipeline
`code/nu2_extended/track_smax.py` (s_sos == s_direct == s_char_runs, exact)
extends the |S(n)|/n decay to n=40000 — ten times the parent run's OOM depth
(4000) and double the prior smax ceiling (20000). Pointwise max |S(n)|/n keeps
decaying; max|S(n)| grows 104→712 from n=1000 to 40000, slower than n —
evidence for c = 1/2, not an argument. `code/out/nu2_terms.txt` is **superseded** (claim
`nu2-terms-superseded`): three cross-checked routes give ν₂(53)=18, ν₂(64)=27,
not the file's 19 and 28.

**Second-moment ceiling N = 40000** (directive 14; claim
`n40000-second-moment-density1-measured`, status measured-not-proved): `μ_N =
0.499658`; over `[30000,40000]` every n has `ν₂/n ≥ 0.49` (min 0.490114, zero
dips below 0.45); over `[50,40000]` only 1 n below 0.35, 3 below 0.40, 10 below
0.42, 51 below 0.45 (all densities < 0.0013); `s2_N` decays 0.000783@4000 →
0.0000934@40000. **Sharper than density-1:** the tail min of `ν₂/n` over `[X,N]`
is rising — 0.3396@50 → 0.4599@1000 → 0.4850@10000 → 0.4901@30000 — evidence
for `ν₂/n → 1/2` *pointwise*, no exceptional set in the tail. The sharpest open
problem: prove `s2_N → 0` (weaker input for SUPPLY, gives the density-1 form) or
that the exceptional set is finite (stronger, pointwise). The two are not
equivalent. The `s2_N/(1/(4N))` ratio is **dropped** (directive 14) — s2_N is a
prefix statistic and 1/(4n) a per-index variance, different objects.

**Prefix-variance null (directive 15):** the correct like-for-like test is the
primes' *prefix* variance `s2_N` against a Monte Carlo *fair-model prefix*
variance (uniform h, same overlapping-window statistic), not against the
analytic `1/(4N)` (that comparison was the flaw directive 14 dropped). Measured
primes/fair = 1.399@100 → 1.283@4000, falling steadily — the primes carry ~28%
more prefix variance than uniform at N=4000 and the excess is shrinking. Pushed
to the N=40000 ceiling (task `push-prefix-variance-null-40000`); the question is
whether the ratio tends to 1, to a constant above 1, or keeps falling — tending
to 1 means the primes are asymptotically indistinguishable from uniform for this
statistic, the sharpest framing of the difficulty.

**Prefix-variance null RESOLVED (directive 18):** the correct null is
`log(N)/(4N)`, not `1/(4N)` — each `ν₂(n)/n` has fair variance ≈ `1/(4n)`, so
the prefix variance is their average `(1/N)Σ 1/(4n) ≈ log(N)/(4N)` (established,
not fitted). Ratio A `= s2_N·4N = 13.94` fails the constant null; Ratio B
`= s2_N·4N/log N = 1.3155` tracks the log null with a ~32% excess at N=40000.
Ratio B across N: 1.443@1000 → 1.392@4000 → 1.361@10000 → 1.337@20000 →
1.315@40000 — a persistent excess falling with slowly-decaying decrements
(−0.0507, −0.0316, −0.0237, −0.0213; the last two steps are each ~a doubling of
N and the decrement only shrank from 0.0237 to 0.0213, ratio ≈0.9). The
measured range does NOT determine whether the limit is 1 (primes asymptotically
uniform for this statistic) or a constant above 1 (permanent structural
excess); a log-linear fit to the measured ratio reaches 1 near N ≈ 7×10^7,
unreachable here (directive 20), so the limit stays undetermined and the
'plateaued / CONSTANT ABOVE 1' verdict is withdrawn (task
`correct-ratio-b-overclaim`). Deep-tail
`[0.9N,N]`: primes' dip density is 0 at every c=0.40..0.49 (first break
`c=None`); all-ones and Thue-Morse both break at c=0.40. Claim
`fair-variance-log-null-tail-clean-40000` (measured), mirrored in ROOT.md.

## Ruled out (five closed doors — do not reopen; witnesses in `problem.md` §4)

1. **Weight alone.** `ν₂ ≥ c·wt(h)` false: `h` all-ones has max weight, `ν₂=O(1)` (it is a kernel vector — all-ones = even-alt ⊕ odd-alt; closed door 1 survives the rank correction untouched).
2. **No long constant runs.** False for primes (Shiu 2000: arbitrarily long same-class mod-4 runs ⇒ long all-zero runs in `h`; **sourced via the Ethan Yang expository** `sources/shiu_strings_expository.full.md`, claim `shiu-string-theorem` — only the primary's own PDF is absent behind the Wiley paywall).
3. **Aperiodicity.** Insufficient: Thue–Morse is aperiodic, `ν₂` sublinear.
4. **Anti-dyadicity.** Insufficient: balanced AND anti-dyadic half-step strings give `wt(Φ_m h) ∈ {1,2}`, m=8,16,24,32.
5. **Periodicity of primes.** True (conditional) and inert since 4 fails the converse.

**Unifying obstruction:** `Φ` has low-weight images on structurally rich
inputs; full row rank (n−2) pins the kernel to 2 dimensions but says nothing
about image weight. So *any* hypothesis of the form "h is complicated enough"
is refuted as a family. (GOAL.md repeats this: that family is closed, do not
reopen.)

## The known reduction, and why it is a dead end (per `problem.md`)

`ν₂ ≥ c·n` ⇐ positive fraction of consecutive prime pairs differing mod 4 —
a named open problem (Ash–Beltis–Gross–Sinnott 2011 §9: frequency limit
unknown, "cannot be treated using L-functions"), behind the parity barrier;
the unconditional literature bounds the wrong (equal-residue) side. The ABGS
2011 source is on disk but only as a citation graph with no abstract read. So
the switch-density form is understood as available and dead.

**The run's hypothesis to test (GOAL.md):** can the fold `Φ` do work the
switch-density form cannot see — i.e. is `ν₂ = wt(Φ_n h)` forced large by
`Φ`'s cancellation properties on weaker arithmetic inputs than positive switch
density?

## Established — the fold row-set geometry (this pass)

**Parity-projection erasure (this pass — confirms the settled `lacasa-mod6-forbidden-blocks-parity-invisible` by a second, CRT route):** the fold's input is `h[j] = ((q_{j+1}−q_j)/2) mod 2`, the **parity** of the half-gap. Lacasa's unconditional K>1 prime structure — forbidden mod-6 gap-residue blocks, from divisibility, symbols indexed by half-gap mod 3 — does **not** survive this projection: `gcd(2,3)=1`, so by CRT the mod-2 parity is independent of the mod-3 symbol, and the forbidden-block rule imposes **no constraint on the parity string `h`**. Hence this K>1 structure cannot be an arithmetic input strictly weaker than pointwise mod-4 switch density; the reopened `1 < K ≲ n/2` territory has no input of this form. The reopened question must look at the fold's own submask correlation reading or a structure that survives parity (LOS's K≥2 sawtooth term), not at mod-6 gap-block forbiddance. Touches none of the five/six closed doors; GOAL priority 2/3 stays open. Anchor: `research/notes/lacasa_projection.md`.

**LOS K≥2 orientation-merge erasure (new, this pass — `los-secondary-bias-orientation-invisible-to-fold`, proved):** the fold bit `h[j] = [q_{j+1} ≢ q_j mod 4]` is the **unoriented** mod-4 switch indicator, merging `(1,3)` and `(3,1)`. LOS's secondary (K≥2) consecutive-prime bias term `C(b−a)` is **odd** (`C(k)=−C(−k)`, only odd characters contribute, `L(0,χ)=0` for even χ), so the orientation it carries is invisible to `h`. Together with the Lacasa erasure above: the order-1 mod-4 switch density (sum over both orientations) is the *only* residue-pattern structure that survives to the fold's parity input; higher-order oriented/divisibility corrections the primes provably carry are erased. A K>1 functional of the fold, if one exists, must be driven by the fold's own submask-correlation reading, not by an additive residue-pattern input.

**Downset-row intersection formula (`downset-row-intersection-meet-formula`, proved-by-derivation, all n, no primes):** the fold row `M_d = {n−1−d+o : o ⊆ d}` maps under the reflection `x ↦ n−1−x` bijectively onto the digital downset `↓d`; downsets meet as `↓d ∩ ↓d' = ↓(d∧d')`, so `M_d ∩ M_d' = M_{d∧d'}`, `|M_d ∩ M_d'| = 2^{pc(d∧d')}`, `|M_d △ M_d'| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`. Independent hand-check on concrete instances (n=8,d=5,d'=3 → {6,7}; n=16,d=7,d'=10 → {13,15}) reproduces it; mechanical route `code/scholar/downset_verify.py` (n=4..199 + negative control) for coder/tool_builder. This is the geometry lemma behind the second-moment route.

**Consequence (`fold-distance-enumerator-On`, proved conditional on the meet formula, no primes, no duality):** `F_n(z) = Σ_{d,d'} z^{|M_d △ M_d'|} = O(n)` for every fixed `|z|<1`, uniformly in n. Proof is sound under attack — distinct rows with popcounts p≥q have dist ≥ 2^{p−1}, and the popcount split at K=c·log₂log₂ n gives `n²|z|^{2^K}=o(1)` for c>1, low-popcount pairs `n^{o(1)}`, diagonal `n−2`.

**What this settles:** the geometry side of the second-moment route is closed. Density-1 SUPPLY reduces to exactly **one open arithmetic input (A): `E[S(n)²] = O(n)` for the real prime gap-parity string h**, which by Chebyshev gives `ν₂/n → 1/2` on a density-1 set (GOAL priority 1). **Directive 31 pins the scope: (A) alone gives density-1 SUPPLY only, NOT pointwise SUPPLY** — the stronger uniform subgaussian/exponential tail on `Z(n)=S(n)/√n` is what makes every exceptional set `{ν₂/n<c}`, c<1/2, finite (claim `prime-E-S2-On-sharp-conjecture`, sharp form recorded in `code/out/pattern_normalized_white_noise.md`). Touches none of the five closed doors. NOT a proof of SUPPLY; (A) is genuinely open and `walsh-spectral-subset-b904` stays open. Anchors: `research/notes/scholar_intersection_formula.md`, `research/notes/subcube_intersection_claim.md`, mirrored in `research/ROOT.md`.

## What is missing (gaps => potential `request_research`)

- **A real Shiu-2000 source [RESOLVED].** The *primary* is Wiley-paywalled and was never downloaded, but the run holds the Ethan Yang expository (`sources/shiu_strings_expository.full.md`) which states and proves the full theorem (Thms 1.1/1.2/4.1) — verified by scholar passes, claim `shiu-string-theorem`. The primes-not-periodic / long-constant-runs input is **sourced locally**; only the primary's own PDF is absent.
- **The weakest arithmetic input that suffices** (GOAL priority 2): the run must
  price bounded autocorrelation of `h`, a second-moment/variance bound, a
  Walsh/Fourier coefficient bound, or an input on `h` only along binary-submask
  sets (which is what Lucas makes `Φ` read) — from which `wt(Φ_n h) ≥ c·n`
  follows. **Directive 9 sharpened the live target to the second-moment input,**
  and **directive 10 corrects its framing**: `s2_N → 0` is the fair-model null
  (`Var(ν₂/n) = (n−2)/(4n²) ≈ 1/(4n)` for uniform h), not prime-specific
  evidence — the decisive column is the ratio `s2_N/(1/(4N))` (≈1 = primes look
  uniform, deviation = where a theorem must live). Chebyshev plus `s2_N → 0`
  still gives density-1 `ν₂(n) ≥ c·n` (thread `variance-vanishing-density1`,
  task `chebyshev-second-moment-density1`; ratio task
  `fair-model-variance-ratio-null`). The reduction to switch density is
  known equivalent-direction but not known to be *necessary*. (Open request
  `walsh-spectral-subset-b904` in REQUESTS.md.) **Directive 7 freezes sources,
  restated by directive 27 after search restarted (sources 36→43, summaries
  48→57, frontier 310→348, 293 candidates still unworked):** no new source or
  download without first naming which unworked FRONTIER candidate was read and
  why none answers.
- Whether SUPPLY is *equivalent* to positive switch density (GOAL priority 3) —
  a genuine negative theorem that would close the problem honestly. The
  `switch-equivalence` skeleton for *arbitrary* h is already **broken** (sparse
  witness h = e_{2^m}); the restricted prime-windowed form survives in
  `supply-switch-equivalence.md`.

## Recalled

One durable finding stored this run (Cognee): the three analytic-number-theory
sources added (Matomäki–Radziwiłł, MRTF, Green–Tao) are value-domain
orthogonality/correlation-cancellation theorems; their named approaches
(`matomaki-radziwill-index-autocorrelation`, `gowers-u2-nilsequence-uniformity`)
are **refuted**, and the sources cannot by themselves reach the fold object.
The rest of Cognee is empty, so `recall_memory`/`recall_scratch` return nothing
for the measured and claim content — that is this run's capture
(`code/out/`), not recalled memory; trace it to those, not to `problem.md`.

## Contradictions

- **Stale "engine of the open approach" framing, resolved (this pass):** the
  three analytic-number-theory summaries (Matomäki–Radziwiłł,
  Matomäki–Radziwiłł–Tao, Green–Tao) initially described themselves as the
  "named engine of the open / proposed (not refuted)" `matomaki-radziwill-
  index-autocorrelation` and `gowers-u2-nilsequence-uniformity` approaches. Both
  approaches are recorded **refuted** in `research/APPROACHES.md` — MR for the
  index-domain object not being multiplicative in the prime index (and g=0 being
  exactly the switch-density parity barrier), Gowers/GT for a basis mismatch
  (the fold lives on the ANF/zeta basis, not the Walsh/U² basis). Corrected the
  three summaries' framing, added `contradicts` edges, and filed the finding in
  Cognee. The sources remain genuine value-domain machinery; their bearing is
  negative for those two routes.
- **Kernel is 2-dimensional, not 1 (directive 5, live consequence):** the
  correction to rank n−2 / nullity 2 means every low-weight-image argument
  calibrated against a 1-dimensional kernel needs recomputing — thread
  `kernel-recalibration`, task `kernel-component-of-prime-h` (does the prime
  switch bit h have a large component along even-alt / odd-alt?). All-ones
  stays in the kernel, so closed door 1 is **untouched** — do not read the
  correction as reopening it.
- `rw-not-the-submask-xor-fold` vs the earlier gloss "RW is the fold itself":
  recorded in `research/CLAIMS.md` (RW's run-length transform is NOT SUPPLY's
  submask-XOR fold Φ).
- **rw Theorem-9 mismatch** (task `reconcile-verifier-anomalies`): the
  positive-integers run-length transform disagrees for every n=1..19; either
  the sum_T parameters or the transform interpretation is off. The former
  "bacher rank n−1" anomaly is resolved — that was the d=1..n−1 row range,
  not the operative d=2..n−1; the rank question itself is settled by
  directive 5.
- **`code/out/dip_sparsity_monotonic.txt` is VACUOUS (directives 11/12):** it
  ran on the unfloored literal-suffix oracle (identically 0 for all n), so its
  M(N)=0 and density-1.0-for-every-threshold table would read as "SUPPLY
  refuted" by a bug. Do not cite or build on it; it is to be deleted, with the
  refuter's `code/out/refuter_dip_sparsity_findings.md` the surviving dip
  source (task `retire-vacuous-dip-capture`). The corrected N=20000 re-run
  shows c=0.48 half/tail = 0, conflicting with the refuter's N=3000 tail 0.030
  — resolve via `recompute-dip-sparsity-40000`.
- **`code/out/chebyshev_second_moment_N40000.txt` — discrepancy recorded, not chased (directive 14):** the run's own note said the capture was found at 0 bytes, but the operator read a populated file before this run carrying `mu=0.064146` — that is the **Thue-Morse negative-control** value at its own N=4000 ceiling, not contamination of the primes table (which reads `mu_N=0.499658` at N=40000). The capture is vindicated as the strongest artifact; claim `n40000-second-moment-density1-measured` is filed from it. The prior directive-13 "discredited" verdict is superseded.
- Convention edge in the sweep: `pattern_finder_nu2_structure.md` quotes
  ν₂(53)/53 = 0.3585 while the capture's min is 0.3396 — the ±1 suffix-floor
  convention difference `problem.md` warns about; quote the convention (here
  d ∈ [2, n−1]) when stating the min.
- **`nu2(4000)` guard constant is 1975, not 1976 (directive 16, authorized).**
  The operative floored range `k∈[2,n−1]` (problem.md) gives `nu2(4000)=1975`
  (ratio 0.4938); `1976` is the unfloored `k∈[0,n−2]` column of
  `code/out/averaged_mean_capture.txt` (ratio 0.4940) — a floored-versus-
  unfloored offset, not a discrepancy. `code/lib/nu2.py` and `code/avg_nu2.py`
  still quote 1976: do not re-import it as a 'correction'.
  `code/lib/nu2_guard.py` must assert 1975 and carry this reason beside the
  constant.

- **Guard/data-path call site RESOLVED (directive 18):** the call site that put
  Thue-Morse numbers under a primes header was `format_rows()` in
  `code/averaged/chebyshev_verify_oracle.py`, which hardcoded the row label
  `mu_N (Primes)` / `s2_N (Primes)` for every sequence — the THUE-MORSE and
  ALL-ONES control sections printed `mu_N (Primes)` under their own headers.
  It was a mislabel, not a wrong h in STAGE1: the prime h was fed correctly.
  The source now threads `seq` and carries the produced-array assert + h-bit
  print (task `fix-data-path-array-guard` closed); the on-disk capture
  `chebyshev_oracle_verified_N40000.txt` predates the fix and must be regenerated
  (task `run-chebyshev-second-moment-40000`).

## The two-pass state — read this before the terminus lines below

This workspace was **closed once and reopened** (`research/REOPENED.md`).
`GOAL.md` is the *second-pass* goal and it partly withdraws the first pass:
the first pass's closing claim that "equivalence to switch density is the
indicated answer" is **explicitly WITHDRAWN** in `research/CONCLUSION.md`
§5 and refuted in `REOPENED.md`. Do not read the "at terminus, stop opening
lines" framing below as the operative goal — that is the *first* pass's
terminus, and it says nothing that settles the second-pass question.

**Why it was reopened, precisely.** A dedicated run refuted the collapse
hypothesis (that every functional of the fold factors through pair
correlations) with an explicit witness at `n=8`: `h=00000010` and
`h'=00000100` share the correlation vector `C₁=(5,1,1,0)` yet have `S²=0`
and `S²=4`. The threshold was measured `n=4..20`: `K*(n) ≈ ⌈n/2⌉`
(`n=8→4, n=12→6, n=16→8, n=20→10`) — Φ sees structure up to correlation
order linear in `n`. The `⌈n/2⌉` guess **mismatches at `n=5`**, so the
closed form is not yet right (GOAL priority 3). **Definition-dependence
(directive 40):** this figure is not pinned until the operative reading of
`K*` is named — three readings diverge past `n=8`
(`code/out/orderk_def_resolve.txt`: at `n=12` imported 6, single-histogram
witness 9, single-histogram const 10, cumulative 7; the cumulative reading
corrected for its off-by-one gives `⌊n/2⌋`). Task
`settle-kstar-definition-budget` names the operative definition and corrects
the budget — **settled by directive 41: `K*(n) = ⌊n/2⌋` (three independent routes); cite it and move on.**

**The operative second-pass question (GOAL.md), and that it is UNWORKED.**
> Is there a functional of the fold, sensitive to correlation order `K` with
> `1 < K ≲ n/2`, that is controllable by an arithmetic input strictly weaker
> than pointwise mod-4 switch density?

Every prior route lived at `K=1`; the range `1 < K ≲ n/2` is unexplored.

**Directive 43 is now the head — the hit-set push is priced out, the pass's
answer is NO.** The hit-set functional (directives 41/42) is withdrawn: the
operator computed the hit-set profile directly and priced the positional
resource out. `H_j = {d ∈ [2,n-1] : j ∈ M_d}`; the fraction of positions with
a large hit set falls like `1/n` (0.312, 0.188, 0.109, 0.062, 0.035 at
n=16,32,64,128,256) while `median|H_j|` stays tiny (4,8,8,16,16), so an input
of the form "switch bits land on high-hit positions often enough" demands `h`
concentrate on a set of density → 0 — a STRONGER demand than positive switch
density, not weaker. The route fails priority 2's pricing test. Caveat:
`nu2` is an XOR over `M_d`, not a sum of `|H_j|`, so this prices the
positional resource, not every hit-set functional — a functional not controlled
by that scarcity is still open but unbuilt, and must be priced against the
table first. Recorded as closed candidate `hit-set-positional-supply`;
the second-pass conclusion `research/CONCLUSION-PASS2.md` says NO. **No
further K* capture** — six agree on `K*(n)=⌊n/2⌋`, zero information gain.

**Directive 41 (superseded as head; recorded for provenance) — priority 1, the hit-set functional.** The
correlation-order budget is SETTLED: `K*(n) = ⌊n/2⌋`, confirmed by three
independent routes (kstar_exact, the sat_solver oracle, the structural check);
`kstar_structural_capture.txt` honestly refutes its own candidate
characterisation `R(n)-1`, and `fold_cell_degree_correction.md` caught a wrong
structural fact in a library source (degree is `2^popcount(d)`, not
`popcount(d)`). Priority 3 is done — cite `⌊n/2⌋` and move on; no more K*
characterisation, and no further K* capture (directive 42: five captures
across n=2..18 already confirm floor(n/2); every further one has zero
information gain). Priorities 1 and 2 have not started. The head is priority 1:
from the n=8 witness (h=e_6 vs h'=e_5, equal pair correlations, S²=0 vs 4) the
separation is the arithmetic of the read-cone/hit-set of a position under the
submask relation (e_{n-2} hit exactly at odd d; e_{n-3} a different hit set) —
NOT any correlation of h. Name that functional, define it for general h (claim
`read-cone-closed-form-exact`: a 1 at position j is read by exactly
`#{d∈[2,n-1] : (n-1-j) ⊆ d}` depths), verify it is constant on C₁ fibres but
not on the whole cube, find the lowest K at which it becomes determined, then
price it against pointwise mod-4 switch density (task `build-hit-set-functional`
→ task `price-hit-set-functional`; thread `hit-set-functional`).

**Directive 38 (superseded as head; its capture template still holds).** The best-built capture either pass has produced,
`code/out/input_strictness_capture.txt`, is the template every new capture must
follow (sequence/oracle/range in the first three lines, canonical guard on the
produced array, a negative control marked DISCRIMINATING, and an independent
reproduction of the n=8 witness). What it exhibits is now stated precisely as
claim `enminus2-linear-supply-switch-density-not-necessary`: the per-window
family `h = e_{n-2}` has switch density `1/n -> 0` yet `nu2(n) = ceil((n-2)/2) ~ n/2`
(the fold reads position n-2 exactly at odd depths d, since `d-1 ⊆ d` iff d odd).
That settles: positive mod-4 switch density is NOT necessary for linear supply,
so supply is strictly weaker than switch density as a property of strings. It
gives NO input controlling the primes — SUPPLY stays open; this is problem.md
result type 4, not type 1. The productive next step was executed (task `linear-supply-by-weight-class`,
capture `code/out/linear_supply_by_weight.txt`, cross-checked
`linear_supply_independent.txt`): linear supply becomes TYPICAL (mean
`nu2/n >= 0.40` AND fraction `>= 0.5`) at weight ratio `w/n = 0.375@8` falling
`0.300, 0.250, 0.188, 0.156` to `0.125@64` and `0.125@128` — two consecutive n.
Directive 39 orders two follow-ups in sequence: (1) task
`linear-supply-threshold-limit` — push n as far as the sampled method allows
(300 samples per weight bounds the frac column) and say whether `w/n` tends to
0 (linear supply typical at ANY positive density) or plateaus near 1/8 (a real
threshold); (2) task `linear-supply-threshold-claim-block` — file the claim
block whose one-sentence gap is "typical is not this string": being above the
threshold does not prove the primes' h has linear supply. The result is a
density bound near 1/8 instead of full switch density — problem.md result type
4, NOT type 1; never written as SUPPLY solved or prime-specific. Scoping: per-window family vs fixed string is load-bearing (a fixed single 1 gives `nu2 = O(1)`, claim
`fixed-single-1-fold-weight-bounded-by-j`).
GOAL priorities in order: (1) build a functional provably not `K=1`,
generalising the `n=8` witness; (2) price each candidate against what it
demands of `h` vs pointwise switch density (see more, demand *less*); (3)
push the `K*` budget past `n=20` and settle whether `K* = ⌈n/2⌉` or merely
close — first naming the operative definition of `K*`, since it is
definition-dependent (directive 40, task `settle-kstar-definition-budget`). All first-pass rules carry forward: one canonical oracle with the
entry guard, temp-file-then-move captures, a negative control shown failing,
measurement labelled as measurement, the six closed doors never reopened.
The witness and the fold-genericity measurement are compatible: Φ *can* see
to order ~n/2; the primes were *not observed* to carry anything that
distinguishes them from random.

**THE RUN IS REOPENED — second pass (GOAL.md), order-`K` territory is UNEXPLORED.** The first pass is
closed: `research/CONCLUSION.md` refuted the single hypothesis (no measurable `ν₂` regularity is
prime-specific — sixth door, claim `sixth-door-no-nu2-statistic-prime-specific`; the mod-4 switch
bias is fold-inert, deliverable 5). The first-pass *closing argument* — "equivalence to switch
density is indicated" — is itself **refuted** (`research/REOPENED.md`): a dedicated run
(`2628fcfb`) produced an explicit witness (`n=8`: `h=00000010` and `h'=00000100` share
`C₁=(5,1,1,0)` but have `S²=0` and `4`) and measured witness existence up to correlation order
`K*(n) ≈ ⌈n/2⌉` (`n=4..20`; and `n=5` really gives `K*=2`, the `⌈n/2⌉=3` guess is wrong there —
check `research/witness-hunt-n20-imported.txt`). **No uniform bound on `K*` exists; Φ sees structure
to order linear in n.** The single open question of this pass: is there a functional of the fold,
sensitive to correlation order `K` with `1 < K ≲ n/2`, controllable by an arithmetic input strictly
weaker than pointwise mod-4 switch density? All eight first-pass routes lived at `K=1`; **the whole
range `1 < K ≲ n/2` is unexplored** — no functional at order `K>1` has been built, `K*` is measured
to n=20 only, and none of the priority-1/2/3/4 steps in GOAL.md has been attempted. Do NOT treat the
first-pass terminus as "the work is over": it is the negative foundation this pass builds on, and the
six closed doors + all settled results are cited, not re-derived. What is still verboten: reopening
the six doors, re-deriving the rank/binomial/telescope/endpoint/distance-enumerator results, and
claiming Gilbreath.

**Directive 34 was the pre-reopen head (recorded for provenance):** deliverable 5 is folded into
`research/CONCLUSION.md` (mod-4 switch bias = sixth door's stronger witness, not a seventh door;
Lemke Oliver–Soundararajan named the strongest known prime-specific mod-4 signal, fold-inert;
~9× Markov margin in the measured section). No new line of attack and no re-verification of settled
results was the rule *within the first pass*; the reopen supersedes the "stop opening lines" reading
for the order-`K` question but keeps the no-re-derive and no-six-door rules. The directive-30/29 work
queue below is first-pass terminal housekeeping, inherited but not the head.

**Directive 30 (superseded by directive 34) was the head.** (1) `code/refute/` lists 47 files: delete every file whose name begins with an underscore or matches `*_probe.py`, `*_run*.py`, `*_run*.sh`, or `*.p`, keeping only `endpoint_sign_check.py` (the single script the abandonment note cites to reproduce the blocker); count before and after and report BOTH numbers in `config/DIRECTIVES.md` — nothing else counts as done, and no new file may be created in `code/refute/` until the count is reported. (2) Search is ABSOLUTELY frozen: no exa_search and no download until the Ratio B decrement-ratio discriminator at N=160000 has a capture, or a note states the projected runtime and why it is unaffordable — there is no source that answers that question. (3) The endpoint-sign resolution is accepted as a real result: file the claim block (committed `(-1)^#runs` form false, corrected identity holds; range checked = 6868 (n,d) pairs n=20..120, 449 committed failures) and keep `endpoint-sign-abandoned.md` pointing at it.

**Directive 29 (superseded by directive 34; recorded for provenance).** The zero-byte captures are cleared — code/out has none (confirmed: `g_run_telescope_verify_negctrl_full.captured.txt` is 833 bytes, populated). The endpoint-sign investigation is **abandoned**, not consolidated: `research/notes/endpoint-sign-abandoned.md` names the blocker — the TPTP model-finder returns 'undecided' because the d=3 axioms pin every boolean atom, so a conjecture false for every input has no free model to exhibit; only the Python checks decide the question and they were never run to a capture. The refuter is redirected to the Ratio B decrement-ratio discriminator at **N=160000** (task `extend-ratio-b-n160000`, thread `ratio-b-decrement-limit`): does r_k keep falling (Ratio B → constant above 1) or turn back toward 1 (Ratio B → 1)? Unaffordable ⇒ state the projected runtime, do not substitute smaller experiments. `code/out/excess_seq.txt` still lacks its directive-13 header (task `header-excess-seq-capture`).

**Directive 28 (superseded in the endpoint-sign prong only):** (1) A NEW 0-byte capture — `code/out/g_run_telescope_verify_negctrl_full.captured.txt` (fifth occurrence, first since `code/lib/capture.py` was written) — CLEARED by directive 29: the file is now populated (833 bytes) and code/out holds no 0-byte capture. (2) Consolidate `code/refute/` — superseded by directive 29's abandonment; see the head and task `abandon-endpoint-sign-scratch`.

**Directive 27 (still current outside the endpoint-sign prong): the claim-block refresh and the search re-freeze.** Directive 26's negative control is now done: `code/gfold/g_run_telescope_verify.py` perturbs the telescoping identity with a 3-valued boundary (r = q_j mod 3) and it breaks — MISMATCHES = 438, first at d=1 pos=0 — shown in `code/out/g_run_telescope_verify_negctrl.captured.txt`; the full 30-trial capture is the 0-byte file directive 28 reopened (task `fix-truncation-mechanism-temp-file`). What remains of directive 26 is the claim block: `research/notes/g_run_telescope_verified.md` still says 6 random trials (capture has 30), records no negative-control count, and its `bearing` does not say what the identity buys for `wt(Φ_n h)` — 51M passes with zero failures is equally the signature of a predicate true by construction. Update the `g-run-telescope-verified` block: hypotheses to the exact counts (30 random h, not the stale '6'), `bearing` stating plainly that the identity restates the fold cell as run-endpoint products and by itself buys nothing direct for `wt(Φ_n h) ≥ c·n`; mirror in `research/ROOT.md` (task `g-telescope-negative-control-claim`).

**Directive 27 also corrects two regressions of directive 7.** (1) Search restarted: sources 36→43, summaries 48→57, frontier 310→348, 293 candidates still unworked — refreeze (task `refreeze-search-name-frontier-candidate`); before any new fetch, name the unworked FRONTIER candidate read and why it did not answer. The open questions (decrement-ratio discriminator, second-moment structure, telescoping identity's bearing) are all in-house computations; no source answers them. (2) The refuter's endpoint-sign spray is **abandoned** by directive 29 (see head): `code/refute/` is to be pruned to the single reproducer `endpoint_sign_check.py` with the pickles and near-identical runners deleted (task `abandon-endpoint-sign-scratch`), not consolidated. Code files went 116→134 this tick against 13 new captures.

**Directive 18 (earlier head): the fair-variance capture is vindicated and the prefix-variance null is settled.** `code/out/fair_variance_at_40000.txt` is correct and citable — `ν₂(40000)=20081` is the primes, both controls discriminate, and the null is `log(N)/(4N)` (Ratio B = 1.3155 at N=40000). Claim `fair-variance-log-null-tail-clean-40000` is filed and mirrored in ROOT.md. Directive 17's call site is named (see Contradictions); task `fix-data-path-array-guard` is closed.

**Directive 19 corrects one over-claim in that result.** Ratio B's falling
decrements (−0.0507 → −0.0316 → −0.0237 → −0.0213; the last two steps are each
~a doubling of N and the decrement only shrank to ≈0.9 of its predecessor) do
NOT separate a limit of 1 from a constant above 1 — the note's 'consistent with
a constant above 1, not with 1' reading is withdrawn. The established statement
is: the excess PERSISTS across N=1000..40000 (1.443 → 1.316) and the measured
range is silent on the limit. The two limits mean opposite things (uniform vs
permanent structural excess), so the honest settlement is NOT to extend the
range: a log-linear fit to the measured ratio reaches 1 near N≈7×10^7 —
unreachable here (directive 20) — so the limit stays undetermined and the
verdict 'plateaued / CONSTANT ABOVE 1' is withdrawn. The next step is task
`correct-ratio-b-overclaim` (fix the script verdict, regenerate the four
captures, stop dumping the mu_4000 Fraction; keep the fair-column
f·4N/lnN = 0.967→0.990 validation). A budget-capped Ratio B extension to
N=80000 is already captured (limit still undetermined); the stale
`chebyshev_oracle_verified_N40000.txt` regeneration stays queued.

**Directive 21 corrects a reasoning error in the decrement reading.** "The
decrements are still shrinking" is NOT a signature of a limit above 1 — the
harmonic sequence has strictly shrinking decrements yet diverges. The
discriminating statistic is the RATIO of consecutive decrements, computed at
FULL PRECISION. **Directive 25 resolves the re-check (directive 24's correction ran against the operator, not the run):** the run's exact decrement ratios are the record — r_3 = 0.899404441, r_4 = 0.877780046 (`code/out/directive21_exact_ratios.captured.txt`). The operator's 0.875 / 0.905 were rounded-table artifacts and must not be cited as data. The final exact ratio FALLS (r_4 < r_3), so the modest lean is toward a limit ABOVE 1 (convergent geometric tail ≈1.126), NOT toward limit 1 and not "neither" — the whole direction rests on that one number: a single ratio is thin evidence, keep the caution. Both extrapolations stay stated and undeclared. Purge the rounded figures and the stale "rising / leans toward limit 1" reading wherever they survive (task `purge-rounded-ratio-figures-directive25`).

**Directive 22: two fair-prefix captures are 0 bytes — restore, do not re-run.**
`code/out/fair_prefix_variance_N40000_5trials.txt` and
`code/out/fair_prefix_variance_40000.txt` are empty (third 0-byte capture; the
chebyshev settle note reported the same earlier). The 5-trial data survives
verbatim in `code/out/push_pv_run.log` — recover the table from there, do not
re-run (~530s of hard-won compute). Then apply only the directive-20/21
conclusion edits (drop "CONSTANT ABOVE 1 / plateaued"; report the
decrement-RATIO as the discriminator with FULL-precision exact ratios
r_3 = 0.899404441, r_4 = 0.877780046 — final falls, modest lean toward a limit
ABOVE 1, resting on that one number (thin evidence; directive 25 — the
operator's rounded 0.875/0.905 are NOT carried); both extrapolations stated,
neither declared) and leave every data row
untouched.
Rule for all roles: correcting a conclusion edits the conclusion and leaves the
data; a capture that must be replaced goes under a new name with the old marked
superseded in place. The truncation mechanism is to be found and fixed (likely
a `> file` redirection opening before the command succeeds — write to a temp
file and mv on exit 0), recorded in `code/out/INDEX.md`. Head is task
`restore-zero-byte-fair-prefix-captures`, then `fix-truncation-mechanism-temp-file`.

**Checker pre-flight (directive 21, solver):** before running a checker, read
the approaches ledger to confirm the approach it serves is still live, check
its input distribution against the real object (primes h, not iid/fair), and
file the result as a fenced claim block — otherwise the capture is discardable
bookkeeping (attempt 2's `anf_dictionary_check` / `anf_second_moment_check`;
task `anf-captures-disposition`).

**Directive 14 (already filed):** claim `n40000-second-moment-density1-measured`
is filed and mirrored in ROOT.md — the N=40000 capture is the strongest artifact
(`μ_N=0.499658`, tail min of `ν₂/n` over `[X,N]` rising 0.3396@50 → 0.4901@30000,
evidence for `ν₂/n → 1/2` pointwise). Directive 14 dropped only the *wrong-null*
comparison (`s2_N` vs the per-index `1/(4N)`); directive 18 now supplies the
correct null (`log(N)/(4N)`, Ratio B = 1.3155). Sharpest open problem unchanged:
prove `s2_N → 0` (weaker SUPPLY input, density-1 form) or that the exceptional
set is finite (stronger, pointwise). The guard module stays the structural fix:
ONE canonical oracle in code/lib (floored `s_sos`, ν₂(53)=18, ν₂(64)=27), every
script imports it, entry guards + capture-header discipline (task
`add-oracle-guard-assertions`); then the dip recompute to N=40000 (task
`recompute-dip-sparsity-40000`).

**Directive 12 (still queued behind it): the dip-sparsity threshold, on a non-vacuous oracle.**
`code/out/dip_sparsity_monotonic.txt` was a vacuous capture (unfloored
literal-suffix oracle, identically 0) and must not be cited or built on; the
real dip numbers live in `code/out/refuter_dip_sparsity_findings.md`. That
source answers the averaged push's headline: M is NOT monotone (density-0.318
decreases; only bounded-below survives, M ≥ 0.396 on all n ≥ 50), and dips are
sparse for c ≲ 0.45 with the < 0.40 set exactly {53,71,105} — so the density-1
form holds up to c ≈ 0.45 and the threshold to locate is between 0.45 and 0.48.
Recompute the dip tail densities to N=40000 over c = 0.40..0.49 (step 0.01)
with all-ones and Thue-Morse controls, and resolve the c=0.48 tail conflict
(refuter N=3000 tail 0.030 vs corrected N=20000 half/tail 0) — task
`recompute-dip-sparsity-40000`, with the oracle guards of
`add-oracle-guard-assertions` and the file removal of
`retire-vacuous-dip-capture` preceding it.

**Directive 10 next in line: file the fair-model binomial as proved, then measure the
ratio.** Record
`fair-model-exact-binomial` as PROVED from rank n−2 / nullity 2 (the exact-count
table confirms it; do not file it as measured), file the `uniform-random-h-supply-w.h.p.`
Chernoff corollary, and state that the reframing touches none of the five closed
doors (task `establish-fair-model-exact-binomial-proved`). Then add the
`s2_N/(1/(4N))` ratio column to the streamed variance recomputation — that
single column decides whether the primes are behaving like a uniform string or
deviating (task `fair-model-variance-ratio-null`). The rank/surjectivity premise
tasks (`prove-fold-rank-all-n`, `state-fold-full-row-rank-surjectivity`) are
unblocked because they are now the load-bearing premise of the proved result.

**Directive 7 + 8 — search frozen, averaged push only.** Search produced nothing
(52 exa_search calls and 41 downloads since the last check, all discarded;
sources stayed 35, summaries 46) while FRONTIER holds 204 unworked candidates:
stop searching. The remaining gap is not a source gap. The refuter was flailing
on scratch (spray of one-off files in `code/refute/`, three near-identical
runners, run-failed 7→9); consolidate to one parameterised script with one
sweeping capture plus a negative control shown failing. **What is next is the
averaged push and nothing else** — directives 3, 5, 6, 7, 8 open, answered with
captures only, using the 40000-term pipeline:

(a) ANSWERED-IN-PART (directive 12, refuter capture N=50..3000): M is NOT
monotone (density-0.318 decreases; only bounded-below survives, M ≥ 0.396 on
all n ≥ 50); dips sparse for c ≲ 0.45, < 0.40 set exactly {53,71,105}. Next:
recompute dip tail densities to N=40000 over c=0.40..0.49 to locate the
sparsity threshold and resolve the c=0.48 tail conflict (refuter 0.030 vs
corrected N=20000 0) — task `recompute-dip-sparsity-40000`;
(b) ANSWERED (avg_push_capture.txt TASK A): density-matched Bernoulli(p=0.5968) and Bernoulli(0.5) reproduce the rising prime mean — the MEAN is fold-generic, not prime-specific. The POINTWISE dip sparsity is the prime-specific signal;
(c) ANSWERED (directive 9, claim `mean-bounded-not-density1`): a bounded mean gives only positive lower density / infinitely-often, NOT density-1. The density-1 route is now variance-vanishing — s2_N → 0 plus Chebyshev (task `chebyshev-second-moment-density1`, thread `variance-vanishing-density1`);
(d) ANSWERED (avg_push_capture.txt TASK B): prime h's min Hamming distance to the 4 kernel directions is dmin/n ≈ 0.13..0.37 (n=8..128) — not close to any collapse direction; closed door 1 untouched.

The directive-5 follow-ups (`prove-fold-rank-all-n`, `state-fold-full-row-rank-
surjectivity`) and the rw Theorem-9 mismatch (`reconcile-verifier-anomalies`) are
parked behind these captures. Each capture states its range and carries a
negative control shown failing.

## Pointers

- `problem.md` — the full problem, the five doors, the measurement table, the
  asserted facts, the convention warning, and the hierarchy of acceptable
  results.
- `GOAL.md` — the single hypothesis (does the fold `Φ` beat the switch-density
  form?), the priorities, and the streaming rule (one row at a time, never
  materialise the triangle).
- `research/CLAIMS.md` — the claim blocks; `research/THREADS.md` — live and dead
  directions (`frontier-refocus`, `switch-side-gap`, `averaged-mean-structure`);
  `research/BACKWARD.md` — the skeletons and their open gaps. Read ledgers with
  `read_ledger`, never by editing the rendered files.
