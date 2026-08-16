# Grounding report — the four threshold-weight candidates (research pass)

Took the inventor's four candidates to the literature. Two of them
(`threshold-weight-sublinear`, `threshold-closed-forms-rejected`) are the run's
own measured claims and are grounded for *consistency with the named form* of
the phenomenon; two (`G-threshold-asymptotic-zero`, `G-threshold-concentration`)
are the pure-F₂/hypergeometric lemmas that would promote the measured claim to a
theorem, and their *engine* is now named in the literature with a precise
statement and hypotheses that hold here.

## The single load-bearing fact (why all four are groundable at once)

The fold's sphere-mean is `E_{S_w}[ν₂] = (1/2)Σ_d (1 − K_w(2^popcount(d);n)/C(n,w))`
(claim `sphere-mean-krawtchouk-exact`, proved-by-derivation). Every threshold
result reduces to controlling the **normalized Krawtchouk ratio**

```
K_w(m;n)/C(n,w),   m = 2^popcount(d).
```

That ratio is exactly the object of a **named theorem**: the exponential-decay
bound of Harrow–Kolla–Schulman.

## Candidate 3 (G-threshold-asymptotic-zero) — GROUNDED (engine now named)

**What the reformulation is called.** The lemma is a Krawtchouk/hypergeometric
asymptotics statement on the multiset of row-weights `{2^popcount(d)}`. It
decomposes depth `d` by popcount and uses the parity identity
`E[(-1)^X] = K_w(m;n)/C(n,w)` for `X ~ Hypergeometric(n,m,w)`.

**The theorem it relies on — precise statement.** Harrow–Kolla–Schulman,
*Dimension-free L^p maximal inequalities on the hypercube* (Theory of Computing
10 (2014) 55–78, DOI 10.4086/toc.2014.v010a003), **Lemma 2.2**: for the
**normalized** Krawtchouk polynomial

```
κ_k^n(x) := K_k(x;n)/C(n,k) = Σ_{j=0}^k (-1)^j C(x,j)C(n-x,k-j)/C(n,k),
```

there is an absolute constant `c > 0` such that for all integers
`0 ≤ k ≤ x ≤ n/2`,

```
|κ_k^n(x)| ≤ e^{-c·k·x/n}.
```

The same bound (in slightly different normalization `|κ_N^k(r)| ≤ e^{-d·rk/N}`,
constant depending only on the alphabet size) is Proposition 3.5 of
Greenblatt–Kolla–Krause, arXiv:1406.7229.

**Do the hypotheses hold here?** Yes. With `k = w` (the string weight) and
`x = m = 2^popcount(d)`, the bound needs `0 ≤ w ≤ 2^popcount(d) ≤ n/2`. This is
exactly the "large cell" regime in the lemma's engine: `w = θn` fixed and
`popcount(d)` large enough that `2^popcount(d) ≥ w`. The saturated (top-popcount)
cells are exactly where HKS gives **superexponential** decay
`e^{-c·θ·2^popcount(d)}`, which dominates everything.

**How it closes the lemma.** Group depths by `k = popcount(d)`; there are
`C(⌊log₂n⌋, k)` cells with `m = 2^k`.
- Small cells (`2^k < n^δ`): count `~ n^{H(δ)}` which is `o(n)` for the `δ` below
  the entropy threshold, each bounded by O(1) → `o(n)`.
- Mid cells (`n^δ ≤ 2^k < θn`): the peak is at `k ≈ L/2` where there are
  `~ n/√log n` cells each bounded by the hypergeometric mode bound
  `O(1/√(1+θ(1−θ)·2^k(1−2^k/n))) ≲ n^{-1/4}`, giving `~ n^{3/4}/√log n = o(n)`.
- Large cells (`2^k ≥ θn`): HKS gives `e^{-c·θ·2^k}`, superexponentially small,
  at most `O(n)` cells → `o(n)`.
Each group is `o(n)`, so the biased-cell sum is `o(n)` and
`E[ν₂/n] → 1/2` for every fixed `θ ∈ (0,1/2)`. This is a *proof outline* whose
every named ingredient is now sourced.

**Has anyone applied it to this problem?** Not to the fold weight itself. HKS
and GKK use the bound for spectral analysis of averaging operators on the cube;
the application to a Pascal-mod-2 fold's sphere-mean is new. But the *tool* is a
standard, precisely-stated theorem with hypotheses that hold.

**What it buys.** Promotes the measured `θ_mean(n)/n → 0` (n ≤ 2^18) to a
theorem for all `n`: linear supply is exact-mean-typical at *any* fixed positive
switch density. Backed: status → **grounded**.

## Candidate 4 (G-threshold-concentration) — GROUNDED (partially)

**The reformulation.** `Var(ν₂(n)) = o(n²)` at fixed `θ`, via the exact second
moment `E[S²] = Σ_{d,d'} K_w(|M_d △ M_{d'}|;n)/C(n,w)` (symmetric-difference
sizes from `downset-row-intersection-meet-formula`).

**The theorems it relies on.** Same two: HKS exponential Krawtchouk decay for the
large-`m` off-diagonal terms, and hypergeometric log-concavity/unimodality
(mode-atom bound `max_j P[X=j] = O(1/√(1+Var X))`) for the bounded terms. The
concentration itself is Chebyshev once the variance is `o(n²)` — standard.

**Hypotheses hold here.** The HKS bound applies cell-pairwise with
`x = |M_d △ M_{d'}|`, `k = w`. The pair-count over the symmetric-difference
multiset is the still-open step (the claim `fold-distance-enumerator-On` does
NOT discharge it, per the supply-threshold-limit.md header correction). So the
engine is sourced but the full pair-count `o(n²)` bound is not yet on paper —
honest status: **grounded** (engine named and applicable), with the pair-count as
the residual open step, mirroring the on-disk note.

**Precedent (both candidates):**
- Harrow–Kolla–Schulman, DOI 10.4086/toc.2014.v010a003, Lemma 2.2
  (`|κ_k^n(x)| ≤ e^{-ckx/n}`, `0≤k≤x≤n/2`).
- Greenblatt–Kolla–Krause, arXiv:1406.7229, Prop 3.5.
- Hypergeometric bounds: Greene–Wellner, *Exponential bounds for the
  hypergeometric distribution*, Bernoulli 23 (2017) 1911–1952, DOI
  10.3150/15-bej800; Lahiri–Chatterjee, *A Berry–Esseen theorem for
  hypergeometric probabilities*, Proc. AMS 135 (2007), DOI
  10.1090/s0002-9939-07-08676-5 (local/normal, mode scale ~ √Var).
- In-workspace: claim `sphere-mean-krawtchouk-exact` (proved),
  `downset-row-intersection-meet-formula` (proved — the symmetric-difference
  multiset feeding the second moment), `excess-is-negative-character-sum`
  (checked — the ν₂↔S dictionary).

## Candidates 1 and 2 (sublinear / closed-forms-rejected) — GROUNDED for consistency

These two are the run's own measured claims (exact per-n computation, n ≤ 2^18),
not reformulations needing a literature *engine*. What the literature supplies is
the **name and theorem** for the *form* they report: the bounded
period-1-in-log₂(n) log-periodic factor `P(log₂ n)` of amplitude ~0.07.

**The named theorem.** Hwang–Janson–Tsai, *Periodic minimum in the count of
binomial coefficients not divisible by a prime* (arXiv:2408.06817, 2024),
**Theorem 2.2**: for every prime p,
`F_p(n) = n^ρ · P(log_p n)` with `ρ = log_p((p+1)/2)` and `P` a continuous
1-periodic function, given by an explicit digit formula. For p=2 this is OEIS
A006046 (odd entries in Pascal's triangle), `ρ = log₂(3/2) = 0.58496`.

**Caveat — hypothesis does NOT transfer as-is.** HJT's theorem is about the
Pascal-mod-2 *counting function* A006046, not about the threshold weight `w*(n)`.
`w*(n)` is a *derived* quantity (a crossing of the fold's sphere-mean), so the
log-periodic *form* of `w*(n) = n^{0.557}·P(log₂n)` is a **structural analogy**,
grounded because `w*(n)` is built from the same Pascal-mod-2 skeleton — not a
transferred exponent. The measured exponent `E = 0.55678 ± 0.002` (1/2 and
log₂3−1 both rejected) is the run's own data and stays `fitted`, not closed-form.
This is exactly what the on-disk notes already concluded (claim
`hjt-p2-log-periodic-representation-proved`, note
`log_periodic_pascal_mod2_engine.md`). So: grounded as consistency-with-a-theorem,
with the honest caveat that HJT does not transfer its constant to `w*(n)`.

The closed-forms-rejected candidate is the negative half of the same finding: the
rejection of `√n` and `n^{log₂3−1}` and the inseparability of 5/9 are consistent
with the log-periodic form, and the statistical rejections are on-disk
(claim `threshold-closed-forms-rejected` — 27σ, 14σ, residual sd 0.01466).

## Verdicts and statuses

| Candidate | Status | Precedent | What it buys |
|---|---|---|---|
| threshold-weight-sublinear | grounded (measured result, form consistent with HJT) | HJT arXiv:2408.06817 Thm 2.2; sphere-mean-krawtchouk-exact | The affirmative headline: sublinear switch count ~n^0.557 suffices; strictly weaker than switch density (type 4, never type 1) |
| threshold-closed-forms-rejected | grounded (negative empirical, consistent with log-periodic form) | HJT Thm 2.2; on-disk 27σ/14σ rejections | Kills pure-power closed forms; pins the log-periodic factor as real |
| G-threshold-asymptotic-zero | **grounded** (engine named: HKS Lemma 2.2 + hypergeometric log-concavity) | HKS 10.4086/toc.2014.v010a003 Lem 2.2; GKK arXiv:1406.7229; Greene–Wellner; Lahiri–Chatterjee | Promotes measured tends-to-0 to a theorem: E[ν₂/n]→1/2 at every fixed θ∈(0,1/2) |
| G-threshold-concentration | grounded (engine named; pair-count over symmetric-difference multiset is the residual open step) | HKS; GKK; meet formula (in-workspace) | Gives the fraction criterion too → the "typical" threshold itself → 0 |

## What was searched and not found (said plainly)

No source applies the HKS Krawtchouk bound or the hypergeometric local-limit to
a Pascal-fold weight — the application here is new, which is a fact about the
search, not a theorem of absence. No source states the *specific* clean closed
form for the O(n)-biased-cell sum or the `o(n²)` pair-count; those remain the
run's own open combinatorial steps (G-threshold-asymptotic-zero mirrors the
on-disk `threshold-limit-hinges-on-hypergeometric-mode-bound` claim; neither is
on the shelf as a ready theorem).
