# Shared context

This is a **third pass**. Read `research/CONCLUSION-PASS2.md` and this file.
The second pass closed with a negative — **no functional of the fold at
correlation order `1 < K ≲ ⌊n/2⌋` survived pricing against an input weaker
than pointwise mod-4 switch density**. Three results stand from it and are NOT
to be re-derived: linear supply without positive switch density, the ~1/8
weight threshold, and `K*(n)=⌊n/2⌋`. The third pass's single owed computation
is described under **The one computation this pass owes**; everything else is
secondary to it.

## The problem (SUPPLY, `problem.md`)

For the primes `q_1=2,q_2=3,…`, build the absolute-difference triangle
`A_{k+1}(i)=|A_k(i)−A_k(i+1)|`. Along the right diagonal `δ_k(n)=A_k(n−1−k)`,
read **only depths `k∈[2,n−1]`** (this floor is load-bearing) and take the
maximal `{0,2}` suffix; `ν₂(n)` = number of 2s in it. Target: exists `c>0`
with `ν₂(n) ≥ c·n` for all large `n`.

**Convention — do not re-litigate.** Reading from `k=0` makes `ν₂(n)=0` for
every n≥2 (bottom cell `A_{n−1}(0)=1` always), vacuously; `literal_suffix_nu2`
returning 0 is the labelled negative control, not a bug. The floored range
`[2,n−1]` is the operative definition; `wt(Φ_n h)` is a theorem about it.
`problem.md` is **not authoritative** — three imported values were wrong and
computation caught all three; print the stated value beside your own
whenever they disagree.

**Imported-as-proved facts, all grounded in this workspace now:**
1. **Linearisation.** `ν₂(n)=wt(Φ_n h)` over F₂, `h[j]=((q_{j+1}−q_j)/2) mod 2`,
   `Φ_n` the Pascal-mod-2 (Rule-90) fold, entries `C(k−1,j−(n−k)) mod 2`.
2. **Lucas.** `C(d,i) mod 2=1` iff `i` binary-submask of `d`; the depth-`d` cell
   is XOR over submasks of `d`.
3. **Kernel.** Under rows `d=2..n−1` (an `(n−2)×n` matrix) `rank Φ_n=n−2`
   (full row rank), nullity 2, `ker=span(even-alt, odd-alt)`, all-ones their
   XOR; `Φ_n` is surjective onto `F₂^{n−2}`, every image has exactly 4
   preimages. Proved all-n by the unit-lower-triangular submask-XOR argument,
   capture `code/out/fold_alln_theorems.captured.txt`, claim
   `fold-rank-n-minus-2-binomial-proved`. The old "rank n−3, nullity 1" is
   wrong, fits no convention — never re-import it.
4. **Dyadic collapse.** Eventually-periodic `h` with power-of-two period ⇒
   `ν₂(n)=O(1)`.
5. **Primes not eventually periodic.** Conditional on Shiu 2000
   (`shiu-string-theorem`, sourced via the Ethan Yang expository
   `research/sources/shiu_strings_expository.full.md`; the primary is
   Wiley-paywalled, its theorem fully reproduced locally).

## The canonical oracle and guard (mandatory, not advisory)

ONE oracle: `lib.supply_fold.s_sos` (submask-SOS, floored), cross-checked `==
s_direct == s_char_runs`. `code/lib/nu2_guard.py::assert_supply_guard(N)`
asserts on the PRODUCED array — `ν₂(53)=18`, `ν₂(64)=27`, `ν₂(4000)=1975`,
`μ_{4000}≈0.4977` — and every script calls it at entry and asserts on its own
array, not on a fresh oracle call. **1975 is the floored value; 1976 is the
unfloored `k∈[0,n−2]` reading — a floor offset, not a discrepancy.**
Captures write to a temp file and `os.replace` on exit 0 (`code/lib/capture.py`);
a 0-byte `captured.txt` is a failed run, not a missing one. Every capture's
first three lines name sequence, oracle, and range; every verification carries
a negative control shown failing. Stream the triangle row-by-row — never
materialise it (parent run was OOM-killed at depth 4000; `track_smax.py`
streams to 40000).

**Claims renderer caveat (live in this container):** the harness maps
`status: measured` to `asserted` (no `measured` variant in `Status::parse`) —
a harness bug fixed upstream, not present here. Until restart, don't trust the
derived proved/checked/asserted counts and keep writing "measured, not proved".

## The one computation this pass owes

> Does the minimum weight ratio at which **linear supply becomes typical**
> tend to **0**, or plateau near **1/8**?

Captured column (`code/out/linear_supply_by_weight.txt`, cross-checked
`linear_supply_independent.txt`, both `s_sos == s_direct`, n=8 witness
reproduced, all-ones kernel control clean): the first `w/n` at which, over
weight-`w` strings, mean `ν₂/n ≥ 0.40` AND fraction `(ν₂/n≥0.40) ≥ 0.5`:

```
n      8     10    12    14    16    32     64    128
w/n  0.375  0.300 0.250 0.286 0.188 0.156  0.125 0.125
```

That column is not monotone (n=12→14 rises 0.250→0.286); the exact capture
`code/out/threshold_limit_exact.txt` settled it (ratio declines from n=14
onward, 0.375@8→0.0188@4096), and the independent exact extension
(`code/out/threshold_exact_mean_independent.txt`, both cross-checks PASS)
reaches n=32768 (ratio 0.007294). Directive 45 reframes the two answers:
- **The ratio tends to 0, but that alone wins nothing** — 'positive density
  suffices' IS positive mod-4 switch density, not a weakening. The deliverable
  is the absolute threshold weight `w*(n)=θ(n)·n`, which grows **sublinearly**:
  'about w*(n) switches suffice' is strictly weaker than switch density.
- **Plateaus at a constant** — the constant is real and belongs in the
  statement; the demand does not weaken.

**Head task (directive 48): exponent to be decided by a two-horse residual test.** The fit over n≥256 gives E = 0.55678, se = 0.00225, putting 1/2 more
than twenty-five standard errors away; the fuller per-doubling slope sequence
0.5406, 0.5850, 0.5443, 0.5712, 0.5663, 0.5406, 0.5502, 0.5433 oscillates
about 0.556 rather than drifting. **Directive 48 does not settle the exponent
as 0.557 — it names a bias the directive-47 fit ignored.** Pascal-mod-2
counting functions carry log-periodic fluctuations (leading term n^E times a
bounded function periodic in log₂ n), and a straight log-log fit over the
~7-doubling window is biased by that oscillation, so 0.5568±0.0023 may be
"exponent plus window artifact". The canonical model A006046
(`a(2k)=3a(k)`, `a(2^n)=3^n`) carries exponent log₂3 exactly, and its
natural threshold counterpart log₂3 − 1 = 0.58496 sits inside the measured
local-slope span (the n=256→512 doubling gave 0.5850). Deciding computation:
tabulate **both** `w*(n)/n^0.5568` and `w*(n)/n^0.58496` against log₂(n) side
by side, with residual ranges, and report which residual is the bounded
periodic one with no monotone trend (task `log-periodic-oscillation-test-d47`).
log₂3−1 must beat 0.5568 on the residual, not by prettiness; if neither is
flat, keep 0.557 as fitted. Then the pass conclusion (task
`write-pass3-conclusion-d47`): theta→0, threshold weight sublinear at
whatever exponent the residual test decides, demand strictly weaker than
switch density, claim block n=8..32768 measured-not-proved, open lemmas
G-threshold-asymptotic-zero and G-threshold-concentration, genericity caveat
"typical is not this string".
That write-up is the last thing this pass owes; do not reopen K*,
fold-genericity, or the withdrawn equivalence conclusion.

## Established results and numbers (this run; treat as given, do not recompute)

**Linear supply without switch density (proved, result type 4).** `h=e_{n−2}`
(single 1 at index n−2) has switch density `1/n→0` yet `ν₂(n)=⌈(n−2)/2⌉~n/2`:
depth `d` reaches `n−2` iff `d−1 ⊆ d` iff `d` odd; claim
`enminus2-linear-supply-switch-density-not-necessary`. So positive mod-4 switch
density is NOT necessary for linear supply. Caveat (adversarial, grounded): this
is a per-window family; a FIXED single 1 gives `ν₂(n) ≤ j+1 = O(1)`, and the
natural fixed sparse families (ones at `2^m−2`, `2^m`) have `max|S|/√n`
GROWING 6.25→62.5 over n=8..4000. **The fixed-string strictness witness is
open** and, if it exists, must be growing and boundary-avoiding
(`g-input-strictness` open). The ~1/8 threshold does NOT prove the primes' `h`
has linear supply — "typical is not this string" is the one-sentence gap.

**Fair model is PROVED, not measured.** `rank Φ_n=n−2` ⇒ for `h` uniform,
`wt(Φ_n h)` is **exactly Binomial(n−2,1/2)** (mean `(n−2)/2`, `Var(ν₂/n)=
(n−2)/(4n²)≈1/(4n)`, `E[s2_N]≈log(N)/(4N)`); SUPPLY holds for uniform `h`
w.h.p. by Chernoff. So the decaying `s2_N` is the fair-model prediction, not
prime-specific evidence. The whole remaining difficulty is that the primes are
not known to be non-adversarial for this fold.

**Measured, ceiling N=40000 (all `measured-not-proved` unless marked proved):**
- `ν₂/n` primes, n=50..4000: 0.3396..0.6170; Cesàro mean rising 0.4394@100 →
  0.4973@4000; Thue-Morse falling 0.2255→0.0641; all-ones 0 (kernel).
- `μ_N=0.499658`, `s2_N` decays 0.000783@4000→0.0000934@40000; tail min of
  `ν₂/n` over `[X,N]` rising 0.3396@50→0.4599@1000→0.4850@10000→0.4901@30000
  (evidence for `ν₂/n→1/2` pointwise, no exceptional tail set); over
  `[30000,40000]` every n has `ν₂/n≥0.49`, zero dips below 0.45;
  `[50,40000]` only 1 n below 0.35, 3 below 0.40, 10 below 0.42, 51 below
  0.45. Dip set `<0.40` exactly `{53,71,105}`.
- **Pointwise smax / second-moment route (proved geometry, open arithmetic):**
  `S(n)=(n−2)−2ν₂(n)`, `2ν₂−(n−2)=−S` exactly; downset row meet
  `M_d∩M_{d'}=M_{d∧d'}`, `|M_d△M_{d'}|=2^{pc(d)}+2^{pc(d')}−2^{pc(d∧d')+1}`
  (proved); `F_n(z)=Σ z^{|M_d△M_{d'}|}=O(n)` for `|z|<1` (proved). Density-1
  SUPPLY reduces to exactly ONE open arithmetic input: **`E[S(n)²]=O(n)` for
  the real prime gap-parity string h** → by Chebyshev `ν₂/n→1/2` on a
  density-1 set. `E[S²]=O(n)` alone gives only the density-1 form; the uniform
  subgaussian tail on `Z=S/√n` is what makes every exceptional set finite
  (pointwise). This statement is genuinely open — measurement cannot reach it
  (sixth door below). `walsh-spectral-subset-b904` request stays open.
- **Prefix-variance null settled (directive 18):** null is `log(N)/(4N)`, not
  `1/(4N)`. Ratio B `=s2_N·4N/log N` runs 1.443@1000 → 1.392@4000 →
  1.361@10000 → 1.337@20000 → 1.315@40000 → 1.297@80000 — a persistent excess,
  but the limit (1 vs constant>1) is undetermined on the measured range (both
  extrapolations stated, neither declared; exact last-step decrement ratio
  falls, r_3=0.899404441, r_4=0.877780046 — a thin single-number lean toward a
  limit above 1, don't overclaim). The operator's rounded 0.875/0.905 are
  artifacts, not data.
- **Fold-generic mean, prime-specific sparsity:** Bernoulli(p=0.5968) and
  Bernoulli(0.5) reproduce the rising prime mean 0.4977 — the MEAN is
  fold-generic, not prime-specific; the pointwise dip sparsity `<0.45` is the
  prime-specific signal. Matched iid at p≈0.585 reproduce the dip counts and
  last-dip positions (deliverable_3) — the basis of the sixth door.
- **K*(n)=⌊n/2⌋ settled (six independent implementations, n=2..18).** Φ sees
  structure to correlation order linear in n. No further K* capture — zero
  information gain.

## Ruled out — closed doors and dead routes (do not reopen, do not re-derive)

**Six closed doors** (details and witnesses in `problem.md` §4 and
`research/CONCLUSION.md`): (1) weight alone — all-ones is a kernel vector,
max weight, `ν₂=O(1)`; (2) no long constant runs — false for primes (Shiu);
(3) aperiodicity — Thue-Morse is aperiodic, sublinear; (4) anti-dyadicity —
balanced & anti-dyadic half-step strings have `wt(Φ_m h)∈{1,2}`; (5)
periodicity of primes — proved-conditional & inert since 4 fails the converse;
(6) **no `ν₂` statistic is prime-specific** — matched iid reproduce dip counts
and last-dip positions (`sixth-door-no-nu2-statistic-prime-specific`;
Lemke Oliver–Soundararajan is the strongest known prime-specific mod-4 signal
and it is fold-inert). **Unifying obstruction:** Φ has low-weight images on
structurally rich inputs; full row rank bounds the kernel, not the weight, so
every "h is complicated enough" hypothesis is refuted as a family.

**The known reduction is a dead end:** `ν₂≥c·n` ⇐ positive fraction of
consecutive prime pairs differing mod 4 — the named open ABGS 2011 problem,
behind the parity barrier, "cannot be treated using L-functions". The reason to
attack SUPPLY directly is that the reduction discards Φ (and Lucas, and the
kernel), and the fold may do work the raw frequency form cannot see.

**Second-pass NO recorded:** the hit-set functional (directives 41/42) is
priced out — `frac(|H_j|≥0.4n)` falls like 1/n (0.312,0.188,0.109,0.062,0.035
at n=16..256) while `median|H_j|` stays tiny (4,8,8,16,16), so "switch bits on
high-hit positions often" demands `h` concentrate on density→0 — STRONGER than
positive switch density. Caveat: `ν₂` is an XOR over `M_d`, not a sum of
`|H_j|`; this prices the positional resource, not every hit-set functional.

**Closed approaches** (`research/APPROACHES.md` = the full record, ~40 rows):
the K=1 routes (eight first-pass routes), the Walsh/subset-sum weight lower
bound (`walsh-subset-sum-lower-bound`, gated on a research request), the
second-moment Krawtchouk geometry (proved, but the arithmetic input is the
open `E[S²]=O(n)`), the fairness/density-model route (mean is generic), and
the switch-equivalence for all `h` (broken: `h=e_{2^m}` is sparse yet
`wt(Φ_n h)=n−O(1)`). Do not re-propose any of these.

## What is missing / open (=> `request_research` if it blocks work)

- **The one arithmetic statement:** prove `E[S(n)²]=O(n)` for the prime gap-
  parity string from an input strictly weaker than pointwise mod-4 switch
  density (the surviving open statement; unreachable by measurement — sixth
  door). Sub-case: the fixed-string strictness witness for switch-density-0
  linear supply (must be growing and boundary-avoiding).
- Whether the ~1/8 threshold tends to 0 (this pass's job — in-house, no source
  answers it; the aggregated residue-pair asymptotics behind it are the same
  ABGS open problem). The MEAN half is exact and falls to 0.007294@32768; the
  open item is the **absolute-weight exponent**, now that 1/2 is in range on
  the extended data (directive 46, task `fit-threshold-weight-exponent-d46`).

## Contradictions / honest state worth keeping

- The first pass's closing claim ("equivalence to switch density is the
  indicated answer") is **withdrawn** — refuted by the `n=8` witness
  (`h=00000010` vs `h'=00000100`, identical `C₁=(5,1,1,0)`, `S²=0` vs `4`).
  The second pass's conclusion stands: **no K>1 functional survived pricing.
- `rw-not-the-submask-xor-fold` (Rampersad–Wiebe's run-length transform is NOT
  this fold Φ). `code/out/chebyshev_second_moment_N40000.txt` was once thought
  contaminated — it is correct; the `mu=0.064146` seen was the Thue–Morse
  control section at its own N=4000 ceiling, not the primes. The vacuous
  `dip_sparsity_monotonic.txt` (unfloored oracle, all zeros) was deleted;
  `dip_sparsity_monotonic_fixed.txt` is the real N=40000 capture.
- The endpoint-sign character identity is proved (`endpoint-sign-corrected-identity`:
  the committed `(-1)^#runs` form is false; the corrected character-product
  holds, 6868 (n,d) pairs checked, 449 committed failures).
- `research/ROOT.md` mirrors the pass conclusions (a prior audit found a
  wiring gap — terminus claims absent from ROOT.md; that was fixed in the
  first-pass closure; re-verify only if you rely on it).

## Pointers

- `problem.md` — problem, six doors, measurement table, result hierarchy
  (3=density-1/averaged, 4=weaker arithmetic input, 5=equivalence negative,
  6=new closed door — report 3/4/5/6, never a measurement as a proof, never
  claim Gilbreath).
- `GOAL.md` — the third pass's single owed computation (threshold → 0 vs 1/8),
  then the second-pass question (K>1 functional, weaker input).
- `research/CONCLUSION-PASS2.md` — the closed negative and the three standing
  results. `research/ROOT.md` — minimal-counterexample structure, verification
  bound, settled classes (phase-1 test met; stop gathering against the stated
  gaps).
- `research/CLAIMS.md` / `research/APPROACHES.md` / `research/THREADS.md` /
  `research/BACKWARD.md` — full ledgers (read_ledger, never edit derived files).
- `code/out/linear_supply_by_weight.txt`, `code/weights/linear_supply_by_weight.py`.
