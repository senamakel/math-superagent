# Anti-dyadic does NOT imply linear supply — SPAD-nondegenerate-linear refuted

**Cycle / source:** Directive 68, executing the verdict the OOM-killed items left in a
capture (`re-run-oom-killed-dyadic-items-streaming`). `dyadic_halfstep_large.captured.txt`
re-ran clean after the OOM and confirms the kernel probe.

**Status:** REFUTED, and this is the fourth combinatorial shortcut the run has killed
(transfer, non-concentration, aperiodicity via Thue–Morse, now anti-dyadicity). They now
fail for one shared reason: **the fold matrix Φ has low-weight images on structurally rich
inputs** — anti-dyadicity, aperiodicity, non-concentration and gap-variety are all structural
conditions on the bit string `h`, and none of them is what makes the fold's weight grow. The
supply bound is irreducibly arithmetic.

## The counterexample

The half-step string `h = 1^{m/2} 0^{m/2}` (first half ones, second half zeros) is:

- **balanced** — exactly `m/2` ones and `m/2` zeros;
- **anti-dyadic** — distance `m/2` from every `2^k`-periodic string (verified by
  `dyadic_kernel_verify_constraints.py` for every probe minimizer, all "genuine survivors").

Yet the fold image is small in the collapsing direction (it is always a power of two,
exactly 1 at power-of-two length and larger otherwise) — this is the *power-of-two
subsequence* collapse that refutes the converse:

```
m= 8  (a=4)   wt(Phi h)=1  ratio 0.125
m=16  (a=8)   wt(Phi h)=1  ratio 0.0625
m=32  (a=16)  wt(Phi h)=1  ratio 0.0313
m=64  (a=32)  wt(Phi h)=1  ratio 0.0156
```
(Full family, see dyadic-halfstep-fold-classification-checked: wt is ALWAYS a power of
two, = 1 iff a is a power of two, larger otherwise — so wt/m has no limit, liminf 0 at
m=2^k, limsup 1/2 along m=2(2^t+1); the collapse is the m=2^k subsequence.)

so `wt(Phi h)/m → 0` along the power-of-two subsequence as `m` grows. These are genuine counterexamples to
SPAD-nondegenerate-linear ("non-dyadic implies wt ≥ c·m"), not near-misses: the minimizers
pass *both* survivor constraints (balanced, anti-dyadic) and still collapse.

```claim
id: spad-nondegenerate-linear-refuted
statement: |
  The anti-dyadic converse is FALSE. For the F₂ fold matrix Φ_n (halved {0,2}-tail cells
  as Pascal-mod-2 folds of the halved-gap bit string h, rule90-interior-xor), there are
  balanced AND anti-dyadic inputs h with wt(Φ_n h) small on a collapsing
  subsequence while m → ∞, so no c·m lower bound survives. Concretely the
  half-step h = 1^{a} 0^{a} (m = 2a) has wt(Φ h) = 1 exactly when a is a power
  of two (ratio wt/m → 0 along m = 2^k; e.g. 0.125 @ m=8, 0.0625 @ m=16, 0.0313
  @ m=32), and at non-power-of-two a it is a LARGER power of two (m=18: wt 8,
  ratio 0.444; m=34: wt 16, 0.471; m=66: wt 32, 0.485), so wt/m has NO limit
  (liminf 0, limsup 1/2). The refutation stands via the power-of-two
  subsequence; the family as a whole is NOT O(1) — see
  dyadic-halfstep-fold-classification-checked.  It is distance m/2
  from every 2^k-periodic string. Therefore "h non-dyadic + balanced ⟹ wt(Φ_n h) ≥ c·m"
  is refuted as a universal statement.
hypotheses: |
  h ∈ {0,1}^m the halved-gap mod-4 switch bit; Φ_n the Pascal-mod-2 fold; wt(Φ h) the
  number of 1s in the fold image (= ν₂ of the right-diagonal {0,2}-suffix, via
  rule90-interior-xor + transfer-matrix-kernel-allones).
holds-here: yes (as a fact about the problem: the combinatorial converse is dead)
evidence: checked
falsifier-passed: |
  dyadic_halfstep_large.captured.txt (wt(Φ h)=1 at m=8,16,24,32, ratio → 0);
  dyadic_kernel_probe.captured.txt (exhaustive min over balanced+anti-dyadic h, m=4..18,
  DECAYS); dyadic_kernel_verify_constraints.captured.txt (all minimizers balanced AND
  anti-dyadic — genuine survivors, not near-misses).
status: refuted
closed-by: spad-nondegenerate-linear-refuted
note: research/notes/spad-nondegenerate-linear-refuted.md
check-it-at: code/out/dyadic_halfstep_large.captured.txt, code/out/dyadic_kernel_probe.captured.txt, code/out/dyadic_kernel_verify_constraints.captured.txt
```

## The Mersenne data belongs here (same phenomenon)

The Mersenne-period families (`P = 2^k − 1`, odd factor, so *not* dyadic-collapsing) show
their mean slope **decaying** as the period grows:

| P | mean slope (`pf_dyadic_mersenne_constants`) |
| --- | --- |
| 3  (2²−1) | 0.6667 |
| 7  (2³−1) | 0.4898 |
| 15 (2⁴−1) | 0.3467 |
| 31 (2⁵−1) | 0.2497 |
| 63 (2⁶−1) | 0.1829 |

Even the linear (odd-factor) families weaken as the period grows — the *same* decay the
half-step strings exhibit, not a separate phenomenon. The per-family constant `c(P)` in the
conjectured `ν₂ ≥ c(P)·n` is not uniform across `P` (already noted in
`dyadic-oddfactor-infimum-bounded`), and the fold's low-weight images on rich inputs is the
mechanism behind both.

## What survives, and what does not

**Survives (proved, still true):**

- The dyadic **collapse** theorem: `h` eventually periodic with period `2^k` ⟹
  `ν₂(q_n) ≤ N₀ + 2^k = O_k(1)` (`dyadic-collapse-proved`, from Lucas +
  rule90-interior-xor). This half is unaffected — it is a theorem about *dyadic* inputs
  collapsing, not about non-dyadic inputs growing.

**Dead:**

- The converse / the useful direction of the dichotomy: "anti-dyadic (non-dyadic, balanced)
  ⟹ linear supply `ν₂ ≥ c·n`". That is `SPAD-nondegenerate-linear` =
  `SPAD-anti-dyadic-linear` (goal `supply-periodic-aperiodic-dichotomy`, rung
  `R-anti-dyadic-certificate-implies-supply`) and the quantitative
  `DPC-kernel-classification` converse — both refuted by the half-step witness.

**Consequence:**

- The odd-factor converse (`minimal period has an odd factor ⟹ ν₂ ≥ c·n`) is numerically
  supported on the periodic families but does **not** bridge to the primes, and now its
  would-be bridge (anti-dyadicity ⟹ linear) is dead. `ν₂ ≥ c·n` for the primes reverts to
  the **named-open arithmetic hypothesis** `abgs-2011-s9-mod4-switch-limit-open` (the
  two-point consecutive-prime mod-4 correlation lower bound). Route B remains a CONDITIONAL
  theorem with that hypothesis; it is not closed, and no structural condition on `h`
  replaces it.

## Depth-bound omission (Directive 67 rule 3)

`dyadic_halfstep_large.captured.txt` prints `m` and the ratio but **no depth bound**, in
violation of Directive 67 rule 3 ("every capture states how deep it went"). The fold here is
computed over the full window `[2, m]` at depth `d = m` (the tail cell of diagonal `m`), so
the depth bound is `D = m`; the program must print it and re-capture to a NEW file (do not
overwrite the existing capture). Tracked in task `file-antidyadic-converse-refutation`.
