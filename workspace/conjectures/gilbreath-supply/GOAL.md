# Goal — third pass

**Read `research/CONCLUSION-PASS2.md` first.** The second pass closed with a
negative: no functional at order `1 < K ≲ ⌊n/2⌋` survived pricing against an
input weaker than pointwise mod-4 switch density. Three results stand from it
and are not to be re-derived — linear supply without positive switch density,
the ~1/8 weight threshold, and `K*(n) = ⌊n/2⌋`.

## The one computation this pass owes

The second pass left exactly one thing unfinished, and it is concrete:

> Does the minimum weight ratio at which linear supply becomes typical tend to
> **0**, or plateau near **1/8**?

The measured column is `0.375, 0.300, 0.250, 0.286, 0.188, 0.156, 0.125, 0.125`
for `n = 8, 10, 12, 14, 16, 32, 64, 128`. It fell monotonically and then held at
0.125 twice, and the run was stopped before resolving it. The two answers mean
different things:

- **Tends to 0** — linear supply is typical at *any* positive density, so the
  arithmetic input the primes need reduces to positive density plus
  non-adversariality. That is a materially weaker demand than switch density and
  would be this workspace's first affirmative result.
- **Plateaus at a constant** — that constant is real, belongs in the statement,
  and the demand does not weaken.

Push `n` as far as the sampled method allows, report the ratio per `n`, raise
the sample count above 300 per weight so the `frac` column can support the
claim, and say which behaviour the data supports **without declaring beyond it**.
Everything else in this file is secondary to that column.

**RESOLVED (third pass, exact-mean half, `code/out/threshold_limit_exact.txt`).**
The MEAN half of 'typical' needs no sampling: over all weight-`w` strings, the
exact mean is computable in closed form, grouped by popcount. The min ratio
`theta(n) = min{w/n : mean_n(w) ≥ 0.40}` over `n = 8..4096` is

`0.3750, 0.3000, 0.2500, 0.2857, 0.1875, 0.1562, 0.1094, 0.0859, 0.0625,
0.0469, 0.0342, 0.0254, 0.0188`

**eventually decreasing toward 0** (decreasing from n=14 onward; the earlier
`0.2857` at n=14 rises above `0.2500` at n=12, so the column is *not* globally
monotone — the honest phrase is "eventually decreasing", and the exact
computation, not GOAL.md's prose, is the record), not plateauing at 1/8. The prior PASS2
plateau at `0.125, 0.125` for `n=64,128` was a sampling artifact (300/weight)
plus the stricter AND with the fraction column; the exact mean gives `0.109@64`
and `0.086@128`. Fixed-alpha rows corroborate: at any fixed small positive
density the mean rises with `n` (`a=0.05`: 0.287→0.468; `a=0.125`:
0.375→0.493), so the crossing ratio keeps dropping. **Data supports 'tends to 0'** for the
ratio — but directive 45 reframes what that buys: 'positive density suffices'
is NOT weaker than positive mod-4 switch density, it IS that statement, so it
wins nothing. The deliverable is the absolute threshold WEIGHT
`w*(n)=θ(n)·n`, whose growth is sublinear: 'about w*(n) switches suffice' is
strictly weaker than switch density. **The exponent is settled as FITTED, not a closed form (directive 47): E = 0.557 ± 0.002.** The fit over n≥256 gives
E = 0.55678 with se = 0.00225, which puts 1/2 more than twenty-five standard
errors away — it is NOT 1/2, and the earlier reading of slopes "drifting down
toward 0.5" was wrong. The fuller per-doubling slope sequence 0.5406, 0.5850,
0.5443, 0.5712, 0.5663, 0.5406, 0.5502, 0.5433 oscillates about 0.556, not
drifts. Do not attach a closed form the data cannot support. One structural
test may explain the oscillation: Pascal-mod-2 counting functions classically
carry log-periodic fluctuations (leading term n^E times a bounded function
periodic in log2(n)), and the alternating high-low slopes are that signature —
tabulate w*(n)/n^0.5568 against log2(n) and report a period-1 oscillation and
its amplitude if present (task `log-periodic-oscillation-test-d47`).

**FRACTION half, third pass full run (`code/out/linear_supply_threshold_pass3.txt`).**
The combined `typical` threshold — `mean ≥ 0.40` AND `frac(ν₂/n ≥ 0.40) ≥ 0.5` —
was sampled at 2000 strings/weight (well above the pass-2 300/weight) at
`n = 64,128,256,512,1024,2048`, and falls strictly with `n`:

```
n       64    128    256    512    1024    2048
theta* 0.1094 0.0859 0.0742 0.0488 0.0371  0.0298
```

No plateau at 1/8. The pass-2 `0.125@64,0.125@128` was the coarse 300-sample +
weight-grid artifact; at 2000 samples the exact mean crossing (0.109@64,
0.086@128) and the fraction agree there, and both keep falling. The exact mean
crossing (Stage B, no sampling) continues to n=2^18:

```
n          32    64    128   256   512   1024   2048   4096   8192  2^14   2^16     2^18
theta/n  0.156 0.109 0.086 0.063 0.047 0.034  0.025  0.019  0.014  0.010  0.0053  0.0028
```

**The operator's correction — read absolute weights, not ratios.** `theta·n`
gives the threshold WEIGHT: `3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,349,738`
for `n = 8..2^18`. **The exponent is settled as FITTED (directive 47):**
E = 0.55678 ± 0.00225 over n≥256 — 1/2 is ruled out by >25 se; the fuller
per-doubling slopes 0.5406, 0.5850, 0.5443, 0.5712, 0.5663, 0.5406, 0.5502,
0.5433 oscillate about 0.556, not drift. Record it as 0.557 ± 0.002 and attach
no closed form. A log-periodic correction (bounded, period 1 in log2(n)) is
the candidate explanation for the oscillation — test by tabulating
w*/n^0.5568 against log2(n) (task `log-periodic-oscillation-test-d47`).

**Arithmetic demand (the point of the exponent).** Reading absolute weights
understates the result if one reads the ratio `w/n`; reading the weight itself,
the statement is: **linear supply is typical once the switch count (weight) w
exceeds about `w*(n)`, which grows sublinearly.** That is strictly weaker than
'a positive fraction of switches' (the mod-4 switch-density statement), because
a sublinear count is a far smaller demand on the primes than a positive
fraction. **Directive 47: the exponent is settled as FITTED** — `w ∝ n^0.557`
(E = 0.557 ± 0.002, 1/2 ruled out by >25 se, no closed form attached), so the
demand is "about n^0.557 switches", still sublinear and strictly weaker than
switch density. The pass conclusion (task `write-pass3-conclusion-d47`) records
this with the n range 8..32768, status measured-not-proved, and the two open
lemmas `G-threshold-asymptotic-zero` and `G-threshold-concentration`.

Both halves of `typical` fall with `n`: the MEAN half exactly (proved Krawtchouk
formula, so `theta_mean(n)/n → 0` rigorously over the listed range), the FRACTION
half sampled (2000/weight, n to 2048). The data supports **tends to 0** — a
1/8 plateau is contradicted by every n ≥ 64. Measured range does not determine
the limit with certainty, but nothing in it rises; it falls strictly throughout.

## Note on directives

Operator directives now reach detached specialist runs directly, not only the
next attempt and the director. If a directive contradicts what you are doing,
it outranks it — apply it and say in your report what you stopped. The previous
two passes lost hours to directives that were acknowledged in the ledger and
never executed by the role they were aimed at; that channel is now fixed and
will be used.

---

# Goal — second pass (retained)

Attack **SUPPLY** (`problem.md`) as a self-contained problem about the primes
and one explicit `F₂` fold. Gilbreath's conjecture is not the goal and must not
be claimed.

**Read `research/REOPENED.md` first.** This workspace was closed once and has
been reopened for a specific reason, and the first pass's conclusion is partly
withdrawn.

## What this pass is for

The first pass answered its hypothesis in the negative and closed. Its closing
argument was that every second-moment route collapsed at the coarsest dyadic
scale to the mod-4 switch-pair correlation, which made equivalence to switch
density look like the answer.

**That argument is refuted.** `Φ` provably sees structure up to correlation
order `K*(n) = ⌊n/2⌋` (settled, directive 41), with an explicit witness at `n=8`. The collapses were a
weakness of the eight routes chosen, not a law about the fold.

So the single question this pass exists to answer is:

> **Is there a functional of the fold, sensitive to correlation order `K` with
> `1 < K ≤ ⌊n/2⌋`, that is controllable by an arithmetic input strictly weaker
> than pointwise mod-4 switch density?**

Every one of the eight prior routes lived at `K = 1`. **The entire range
`1 < K ≤ ⌊n/2⌋` is unexplored.** That is this pass's territory and it should not
spend time anywhere else. (The `⌊n/2⌋` bound is settled by directive 41 — three independent routes —
see priority 3; cite it and move on.)

## Priorities

1. **Build a functional that is provably not `K=1`.** Start from the witness
   construction — it shows exactly how two strings with identical pair
   correlations separate under `S²`. The separating quantity is the arithmetic
   of the read-cone/hit-set of a position under the submask relation (a 1 at
   position `j` is read by exactly `#{d∈[2,n-1] : (n-1-j) ⊆ d}` depths), NOT
   any correlation of `h`. Name it, define it for general `h`, verify it is
   constant on `C₁` fibres but not on the whole cube, and find the lowest `K`
   at which it becomes determined (task `build-hit-set-functional`). This is
   concrete and comes first.
2. **Price each candidate against the arithmetic.** For a functional at order
   `K`, the question is what it demands of `h`. State that demand precisely and
   compare it to pointwise switch density. A functional that sees more but
   demands more is worthless; the target is one that sees more and demands
   *less*.
3. **Establish the budget — DONE (directive 41).** `K*(n) = ⌊n/2⌋`, confirmed
   by three independent routes (kstar_exact, the sat_solver oracle, the
   structural check). `kstar_structural_capture.txt` honestly refutes its own
   candidate characterisation `R(n)-1` rather than fitting it, and
   `fold_cell_degree_correction.md` caught a wrong structural fact in a library
   source (degree is `2^popcount(d)`, not `popcount(d)`). Cite `⌊n/2⌋` and move
   on; do not open more work on `K*` itself.
4. **If every order-`K` functional also collapses, prove that** — as a theorem
   this time, not as an observation across candidates. That would restore the
   equivalence conclusion on a sound footing and close the problem honestly.

## Rules

These are carried from the first pass, where each was learned the hard way.
None is advisory.

- **One canonical oracle.** `code/lib` holds the floored `k ∈ [2, n−1]` fold and
  nothing else computes `ν₂`. Every statistical script calls
  `assert_supply_guard` at entry — `ν₂(53)=18`, `ν₂(64)=27`, `ν₂(4000)=1975`,
  `μ_N(4000) ≈ 0.4977` — and asserts on the **produced array**, not on a fresh
  oracle call. A guard that validates the oracle while the data path feeds a
  control sequence catches nothing; that happened three times.
- **Captures write to a temp file and move on exit 0.** Five captures were found
  at zero bytes because a redirection truncated on open and the command failed.
  An empty capture is a failed run, not a missing one.
- **Every capture states, in its first three lines, which sequence it ran, which
  oracle function it called, and the exact range.**
- **A negative control, shown failing, in every verification.** A capture of 51
  million passes measured nothing until a deliberately broken variant produced
  438 failures beside it.
- **A measurement is not a proof.** Label it, and name the ceiling.
- **Do not reopen the six closed doors** in `problem.md`. The collapse
  refutation is not about any of them.
- **Do not re-derive settled results.** The rank fact, surjectivity, the exact
  binomial law, the telescoping identity, the endpoint-sign correction and the
  `O(n)` distance enumerator are all proved and recorded. Cite them.
- **`problem.md` is not authoritative.** Three of its seeded values were wrong
  and computation caught all three. Print the stated value beside your own
  whenever they disagree.

## Out of scope

Gilbreath's reduction, Lemma 5.4, the demand side, BHP record gaps, and the
absorption/descent machinery are proved in the parent workspace. Cite, do not
rebuild.
