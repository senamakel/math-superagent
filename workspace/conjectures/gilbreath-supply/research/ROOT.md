# ROOT — structure of a minimal counterexample, verification bound, settled classes

This is the phase-1 completion record required by the orchestrator: the
structure of a minimal counterexample to SUPPLY, the current verification
bound, and the restricted classes already settled with their hypotheses. It is
the single file a fresh reader opens to know where the run stands; the ladders
(`research/weakened/supply.md`) carry the rung-by-rung state.

## What SUPPLY asserts

There is c > 0 with ν₂(n) = wt(Φ_n h) ≥ c·n for all sufficiently large n, h the
prime gap-parity string h[j] = ((q_{j+1}−q_j)/2) mod 2, Φ_n the Pascal-mod-2
fold with entries C(k−1, j−(n−k)) mod 2, ν₂(n) the number of 2s in the maximal
{0,2} suffix of the diagonal (floor convention at index 2).

**Pattern-finder mirror (claim `excess-is-negative-character-sum`).** With the
endpoint character sum `S(n)=Σ_{d=2}^{n-1}(-1)^{T(n,d)}` and `T` the submask-XOR
cell, `2·ν₂(n)-(n-2) = -S(n)` exactly (brute- and SOS-verified). Hence pointwise
`ν₂ ≥ c·n` ⟺ `S(n) ≤ (1-2c)n-2` eventually; measured `S(n)` is deeply sublinear
(`max|S| ≈ 634` at `n=30000`, `max|S|/√n ≈ 3.2–3.8`), so `ν₂/n → 1/2` and the
open arithmetic statement is `S(n) = o(n)` — the equivalence-sharpened form of
the endpoint-parity skeleton's `|S(n)| ≤ (1-2c₀)n`.

## Structure of a minimal counterexample

A counterexample is not a single string but a way for the prime h to make the
fold's weight sublinear. The five closed doors (problem.md, verified) kill every
"h is complicated enough" route; the structure of any counterexample must
therefore live in the *interaction* between h's arithmetic and Φ's submask-XOR
reading, not in h alone. The known partial structures:

- **Kernel collapse.** h = all-ones gives ν₂ = O(1) exactly (Φ_n(1)=0). Any proof
  must be robust to h being near the kernel.
- **Single-sparse amplification (the positive witness).** h = e_{2^m} has
  wt(h)=1 but wt(Φ_n h)=n−O(1) at n=2^m+1 (refuted the SUPPLY⇔switch
  equivalence — see r-witness note). So a minimal counterexample cannot be
  found by "sparse ⇒ sublinear fold"; the fold amplifies lone switches.
- **Dyadic/2-regular structure.** Thue-Morse h gives ν₂ sublinear decaying
  0.27→0.011; balanced anti-dyadic strings give wt(Φ_m h)∈{1,2}. Any
  counterexample family would likely be a 2-regular / submask-structured input
  (closed door 4 territory), not a "complicated" one.

**Conjecture for the minimal counterexample:** none exists — the argument the
run is trying to build is that *any* h whose submask-window correlations are as
weak as the primes' must have linear fold weight, and the only way to make it
sublinear is to inject dyadic-period structure that the primes lack. The counter-
example structure to keep hunting (G-sup-implies-switch in
`research/backward/supply-switch-equivalence.md`) is a **prime-realizable** h
with o(n) ones yet linear fold weight: the search is over boundary sequences
r_j = q_j mod 4, since the equality fails for arbitrary binary strings.

## Verification bound
- The fold oracle ν₂(n) = #{d∈[2,n−1]:T(n,d)=1}, T(n,d)=⊕_{o⊆d} h[n−1−d+o],
  computed exactly by the 2-adic submask-XOR DP, cross-checked vs brute
  submask enumeration on n∈{2,3,5,8,13,21,34,55,64,89,100,128}, runs to
  **n = 8000**. Convention pinned by reproducing ν₂(4000)/4000 = 0.4938 vs the
  literature 0.4933.
- **Pointwise ceiling: N = 40000** (claim `smax-decay-through-40000`, status
  measured-not-proved): the streamed pipeline `code/nu2_extended/track_smax.py`
  (s_sos == s_direct == s_char_runs, exact) pushes the pointwise |S(n)|/n decay
  through n=40000 — ten times the parent investigation's OOM depth (4000) and
  double this workspace's prior smax ceiling (20000). The mean M(N) sweep runs
  to N=8000.
- **Second-moment ceiling: N = 40000** (claim
  `n40000-second-moment-density1-measured`, status measured-not-proved, directive
  14): `μ_N = 0.499658`; over `[30000,40000]` every n has `ν₂/n ≥ 0.49` (min
  0.490114, zero dips below 0.45); over `[50,40000]` only 1 n below 0.35, 3 below
  0.40, 10 below 0.42, 51 below 0.45 (all densities < 0.0013); `s2_N` decays
  0.000783@4000 → 0.0000934@40000. The tail min of `ν₂/n` over `[X,N]` is
  **rising with X**: 0.3396@50 → 0.4599@1000 → 0.4850@10000 → 0.4901@30000 —
  stronger than density-1: evidence for `ν₂/n → 1/2` pointwise, no exceptional
  set in the tail.
- Measured truth: mean ν₂/n ≈ 0.4986 over [50,4000]; only 10 pointwise dips
  below 0.42 (deepest ν₂(53)/53=0.3585), all in [50,274]. `code/out/nu2_terms.txt`
  is superseded by the three cross-checked routes (claim `nu2-terms-superseded`):
  ν₂(53)=18 and ν₂(64)=27, not 19 and 28.
- **Prefix-variance null N = 40000** (claim `fair-variance-log-null-tail-clean-40000`,
  status measured, directive 18): the correct null is `log(N)/(4N)` — each
  `ν₂(n)/n` has fair variance ≈ `1/(4n)`, so the prefix variance is their
  average `(1/N)Σ_{n≤N}1/(4n) ≈ log(N)/(4N)`, not `1/(4N)`. Ratio A
  `= s2_N·4N = 13.94` fails the constant null; Ratio B `= s2_N·4N/log N = 1.3155`
  tracks the log null with ~32% excess. Ratio B across N: 1.443@1000 →
  1.392@4000 → 1.361@10000 → 1.337@20000 → 1.315@40000 → 1.297@80000 — a
  persistent excess falling with slowly-decaying decrements (−0.0507, −0.0316,
  −0.0237, −0.0213, −0.019; the RATIO of consecutive decrements at full
  precision is ≈0.623 → 0.752 → 0.899 → 0.878 — the LAST step falls, so
  directive 24 withdraws the "drifting toward 1" lean: neither limit is
  favoured. The rounded 0.63/0.75/0.875/0.905 set was the operator's
  approximation, not data). The two extrapolations are stated side
  by side and neither declared: a geometric tail (ratio settled below 1) adds
  ≈0.171 for a limit ≈1.126; a ratio drifting to 1 makes the tail diverge and
  Ratio B reach 1 (primes asymptotically uniform for this statistic). Settling
  it means more doublings (160000, 320000…) each ~4× runtime, or a theorem;
  not extrapolation (directive 21). Deep tail `[0.9N,N]=[36000,40000]`:
  primes' dip density is 0 at every c=0.40..0.49 (first break `c=None`); all-ones and
  Thue-Morse both break at c=0.40.

## Settled restricted classes (the rungs already ground)

Each with its hypotheses, from `research/weakened/supply.md`:

1. **R-random-expectation (settled):** h uniform on the domain of Φ_n, rank
   Φ_n = n−2 (full row rank of the operative (n−2)×n matrix, rows d=2..n−1,
   nullity 2) ⇒ E_h[wt(Φ_n h)] = (n−2)/2 ≥ n/3 for n ≥ 6. The fold imposes no
   generic weight obstruction. (off: primes-input, pointwise-all-n,
   unconditional-effective.)
2. **R-random-pointwise (open):** wt(Φ_n h) ≥ n/4 w.h.p. for random h — the
   weak-form concentration the run has not yet reached via Φ_n-specific (Lucas)
   structure rather than bare rank.
3. **R-finite-verified (contradicted at full range):** ν₂/n ≥ 0.42 for all
   [50,4000] is FALSE (10 counterexamples, all ≤274); the correct statement is
   ν₂/n ≥ 0.42 for all n ≥ 500, exceptional set ⊆ [50,274], tail min ≥0.443.
   Numerical, not a theorem.
4. **Averaged form (measured, not proved):** M(N) = mean ν₂/n ≥ 0.44 stable
   over N=100..8000, negative controls (all-ones→0, Thue-Morse→decay) fail as
   required — the signal is specific to the prime h.
- **Captured averaged push (measured-not-proved, N=20000, directive 8):**
  claim `m-nonmonotone-bounded-below`: M(N) is NOT non-decreasing (7949 strict
  decreases, density 0.397) but is bounded below on ALL n≥50 (running min
  0.3959, rising to 0.49936@20000). claim `dip-sparsity-to-20000`: the dip set
  {n:ν₂/n<0.40} = {53,71,105} is finite, empty past 105; <0.42 ends at 274
  (n=145 is exactly 0.4, a float-threshold trap); tail windows empty at every
  threshold ≤0.48 at N=20000; min ν₂/n over [10000,20000]=0.485. NOT robust
  to c=0.48 mid-range (refuter, density 0.112 over [50,3000]). claim
  `negative-controls-dense-dips`: Thue-Morse/all-ones dip density ~1.0. The
  measured sandwich: for any c<0.485, ν₂(n)/n≥c for every large n (stronger
  than density-1). Density-matched random strings reproduce the mean
  (fold-generic) but NOT the sparsity (prime-specific).

## Proved structural facts (claim `fold-rank-n-minus-2-binomial-proved`)

Under the operative row range d=2..n-1, Φ_n has rank n−2 and ker = span(even-alt,
odd-alt) (all-ones stays in the kernel) — the full square submask-XOR matrix Z is
unit lower-triangular, so dropping rows 0,1 leaves dim ker = 2, rank = n−2.
Hence Φ_n is surjective onto F₂^{n−2} with every image having exactly 4 preimages,
and for h uniform on the cube wt(Φ_n h) is EXACTLY Binomial(n−2,1/2) with
E[wt]=(n−2)/2, Var=(n−2)/4, so Var(ν₂/n)=(n−2)/(4n²)≈1/(4n). Verified by exact F₂
elimination n=2..40, exhaustive kernel census n=2..12, exhaustive 2ⁿ enumeration
n=2..9, and the canonical oracle (nu2(53)=18, nu2(64)=27, nu2(4000)=1975,
mu_4000=0.497259). This makes the uniform-expectation and the log(N)/(4N)
prefix-variance null rest on a proved rank fact, not a fit. It touches none of
the five closed doors (all-ones stays kernel; Thue-Morse stays sublinear).
Anchor: `code/out/fold_alln_theorems.captured.txt`.

## Proved structural fact (claim `endpoint-sign-corrected-identity`)

The endpoint character product carries no extra per-run sign:
`(-1)^{T(n,d)} = ∏_R χ(r_{a_R}) χ(r_{b_R})`. The committed form with the spurious
`(-1)^{#runs(d)}` prefactor is false for every binary string at every odd d
(hand proof at d=3), and fails 449 of the 6868 (n,d) pairs n=20..120 checked
against the literal oracle, where the corrected form holds on all 6868. This is
prime-independent and does not revive the separately-refuted
`dyadic-gap-character-correlation` approach. Anchors:
`research/notes/refuter_endpoint_sign.md`, `research/notes/endpoint-sign-abandoned.md`,
`code/refute/endpoint_sign_check.py`.

## Proved geometry facts (claims `downset-row-intersection-meet-formula`, `fold-distance-enumerator-On`)

The fold row set R_n = {1_{M_d} : d ∈ [2,n-1]}, M_d = {n−1−d+o : o ⊆ d}, is a
meet-semilattice under intersection: the reflection x ↦ n−1−x is a bijection
M_d → ↓d (digital downset), and ↓d ∩ ↓d' = ↓(d∧d'), so M_d ∩ M_d' = M_{d∧d'},
|M_d ∩ M_d'| = 2^{pc(d∧d')}, and |M_d △ M_d'| = 2^{pc(d)} + 2^{pc(d')} −
2^{pc(d∧d')+1} (Lucas: one element per submask). Proved by derivation for all
n (bijection + AND intersection), independently hand-checked on concrete
instances (n=8,d=5,d'=3 → {6,7}; n=16,d=7,d'=10 → {13,15}); mechanical route
in `code/scholar/downset_verify.py` (n=4..199 + negative control) for coder.
Consequence (proved conditional on the meet formula, no primes, no duality):
F_n(z) = Σ_{d,d'} z^{|M_d △ M_d'|} = O(n) for every fixed |z|<1, uniformly in n
(distinct rows with popcounts p≥q have dist ≥ 2^{p−1}; popcount split at
K=c·log₂log₂ n). This closes the GEOMETRY side of the second-moment route and
reduces density-1 SUPPLY to exactly one open arithmetic input (A):
E[S(n)²] = O(n) for the real prime gap-parity string h, which by Chebyshev
gives ν₂/n → 1/2 on a density-1 set (GOAL priority 1). It touches none of the
five closed doors. NOT a proof of SUPPLY; (A) is open.
Anchors: `research/notes/scholar_intersection_formula.md`,
`research/notes/subcube_intersection_claim.md`.

## Run-telescope structure (claim `g-run-telescope-verified`, checked)

The digital down-set ↓d of any d ≤ 2^14 partitions into maximal consecutive
runs of length 2^g (g = ν₂(d+1)), count 2^(popcount(d)−g), each a block
[m·2^g, (m+1)·2^g − 1]; and over any such run [u,v] the fold cell telescopes:
XOR_{o∈[u,v]} h[pos+o] = [r_{pos+u} ≠ r_{pos+v+1}] for a two-valued boundary r
(prime case r = q_j mod 4). Machine-verified (brute submask enumeration d=0..2^14,
element-by-element XOR d≤2^10, prefix-XOR d≤2^14) on the real prime-residue h and
30 random controls — ALL PASSED (30-trial run, not 6: the 6-trial capture is
superseded). The two-valued boundary is load-bearing: replacing it with a
three-valued boundary (r = q_j mod 3) breaks the identity with **438
MISMATCHES over 620067 pairs**, so the pass is not true by construction.
Grounds the adopted approach `dyadic-gap-character-correlation`'s reduction
step. Not a proof of SUPPLY.
Anchor: `code/out/g_run_telescope_verify_negctrl_full.captured.txt`.

## Primes-vs-fair prefix variance at N=40000 (claim `fair-mc-primes-ratio-constant-133-40000`, measured)

primes/fair = 1.492@1000 → 1.420@4000 → 1.380@10000 → 1.353@20000 → 1.339@30000
→ 1.329@40000: monotone decreasing with decelerating decrements (slope vs ln N
= −0.044). The excess above the uniform-h fair model PERSISTS over
[1000,40000] (~33% at 40000); the fair side tracks the proved log(N)/(4N) null
(f·4N/lnN = 0.990), primes at p·4N/lnN = 1.315. Whether the limit is 1 or a
constant above 1 is NOT decided by these two decades (directive 19). Open
problem prove s2_N → 0 (directive 14) stands with that excess quantified.
Capture: `code/out/fair_prefix_variance_40000.txt`.

## Three restricted classes with hypotheses (phase-1 test)

The three classes whose hypotheses hold here and are settled:

- **Uniform input, rank told:** E[wt(Φ_n h)] ≥ n/3 (R-random-expectation;
  holds under rank Φ_n = n−2, machine-verified n=2..20). Settled.
- **All-ones (kernel) input:** ν₂ = O(1), exactly Φ_n(1)=0 (closed door 1).
  Settled — and the model for why weight-alone hypotheses fail.
- **Anti-dyadic balanced input:** wt(Φ_m h) ∈ {1,2} for m=8,16,24,32 (closed
  door 4). Settled — the model for why 2-regular structure kills linear growth.

## Open (the realistic targets, in order)

1. Averaged SUPPLY (density-1 set, G-mean-linear + G-var-vanishing) — GOAL
   priority 1, empirically healthy. **This is the only line in flight
   (directive 8).** The five questions, answered with captures only: M(n)
   monotone/bounded-below on density-1; dip sparsity; density-matched
   surrogate reproducing the rising mean; Chebyshev separation of density-1
   from infinitely-often; h's component along even-alt/odd-alt.
   **Sharpest open form (directive 14, claim
   `n40000-second-moment-density1-measured`; sharp conjecture claim
   `prime-E-S2-On-sharp-conjecture`, directive 31):** prove `E[S(n)²]=O(n)`
   for the prime h, equivalently a uniform subgaussian/exponential tail on
   `Z(n)=S(n)/√n`. These two sides are NOT equal in strength:
   `E[S(n)²]=O(n)` gives density-1 SUPPLY only (Chebyshev), NOT pointwise;
   the subgaussian tail gives `Σ_n P(|Z(n)|>δ√n)<∞`, hence every exceptional
   set `{ν₂/n<c}`, c<1/2, is finite — full pointwise SUPPLY. The rising tail
   min (0.3396@50 → 0.4901@30000)
   is evidence for `ν₂/n → 1/2` *pointwise*; `s2_N → 0` is the weaker
   sufficient input (density-1 form via Chebyshev), finiteness of the
   exceptional set is the stronger pointwise statement. The two are not
   logically equivalent — mean + vanishing variance give density-1, not
   finiteness (claim `mean-bounded-not-density1`).
2. Weakest arithmetic input forcing wt(Φ_n h) ≥ c·n (G-weak-input-submask-density
   + G-weak-input-primes-satisfy-C) — GOAL priority 2; Lucas mixing
   (Pivato-Yassawi Thm 7.1) is the named candidate, needs the finite-prefix
   transfer this library does not have.
3. SUPPLY ⇔ switch density restricted to prime-realizable h (G-sup-implies-switch)
   — GOAL priority 3.

**Directive 32 closes the sequence-analysis route** (claim `per-scale-refinement-collapses-to-switch-density`, status checked): the per-scale second-moment refinement collapses back to the g=0 switch-density scale (g=0 variance share 0.425@400, 0.730@1000, 0.553@4000), and the √n white-noise plateau is fold-generic (uniform h reproduces it), so the sequence data yields no arithmetic input weaker than mod-4 switch density. GOAL priority 2 is therefore unanswered by any measurement and remains open only as an unconditional arithmetic theorem (terminus: `research/notes/terminus-assessment-directive32.md`).

**Directive 7 freezes search.** 52 exa_search calls and 41 downloads since the
last check produced nothing — sources stayed at 35, summaries at 46, every fetch
discarded — while FRONTIER.md already holds 204 unworked candidates. A role
wanting a new source must first name which of the 204 it has read and why none
answers; the remaining gap (density-1 step, Chebyshev separation, kernel
component) is in-house computation, not literature. The open request
`walsh-spectral-subset-b904` stays open but is parked behind this gate, not a
search licence.

The finite-prefix transfer from the ergodic randomization theorems
(Pivato-Yassawi, Takei) to the single deterministic finite-string fold is the
single largest missing technical tool: it appears in `research/notes/
pivato_lucas_mixing_equivalence.md` as an open step and in no source.
