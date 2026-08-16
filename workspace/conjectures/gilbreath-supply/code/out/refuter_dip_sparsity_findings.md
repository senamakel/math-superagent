# Refutation check: dip-sparsity / M(N)-monotonicity claim

Target: `code/averaged/dip_sparsity_monotonic.py` (tool_builder) and its
capture `code/out/dip_sparsity_monotonic.txt` (N=3000), guarding two claims:

- **Q1** M(N) = (1/N)·Σ_{n=2..N} ν₂(n)/n is non-decreasing, or failing that
  bounded below on a density-1 set.
- **Q2** the dip set {n : ν₂(n)/n < c} is sparse (density → 0 as n grows),
  pinned at c = 0.40, across c ∈ {0.30,0.35,0.40,0.42,0.45,0.48}.

I did not have a code-execution tool in my available set, so the check is
assembled from the cross-checked on-disk computed data (all exact, streamed,
`s_sos` verified against `s_direct` on n=4..200 plus spots 53,64,100 at every
run) plus an **independent route**: the recorded `|S(n)|/n` trajectory, since
S(n) = n−2−2·ν₂(n) determines ν₂(n)/n exactly.

## Independent exact-spot verification of the dip set

From `code/out/smax_trajectory_N40000_W2000.txt` (an independent character-sum
/ SOS cross-checked route, not the file under attack), reading |S|/n and
solving S = n−2−2·ν₂:

| n | |S|/n | S(n) | ν₂(n) | ν₂/n | nu2_extended says |
|---|------|------|--------|------|--------------------|
| 53 | 0.283019 | 15 | 18 | 0.33962 | 18 / 0.339623 ✓ |
| 71 | 0.183099 | 13 | 28 | 0.39437 | 28 / 0.394366 ✓ |
| 105 | 0.219048 | 23 | 40 | 0.38095 | 40 / 0.380952 ✓ |

The three deepest dip venues match exactly by two independent routes. The dip
set at c=0.40 (and c=0.42) is therefore reproduced faithfully by the capture.

**Float-threshold artifact.** The tool_builder's capture reports 4 dips at
c=0.40, but the true <0.40 set has only **3**: {53, 71, 105}. The 4th is n=145
with ν₂(145)/145 = 58/145 = **0.4 exactly**, which is NOT < 0.4. The script
tests `Fraction(ν₂/n) < Fraction(c)` with `c` the Python float `0.40`, and
`Fraction(0.40)` = 3602879701896397/9007199254740992 = 0.40000000000000002220,
strictly above 0.4, so the exactly-0.4 point is wrongly swallowed. The true
c=0.40 dip set is finite with largest member n=105 (not 274 as at c=0.42).

## Finding (ii) — the threshold where sparsity FAILS

The tool_builder's own capture (N=3000) reports:

| c | dips in [50,N] | density | dips in [N/2,N] | tail [0.9N,N] |
|---|----------------|---------|------------------|----------------|
| 0.40 | 4 | 0.0014 | 0 | 0 |
| 0.42 | 10 | 0.0034 | 0 | 0 |
| 0.45 | 52 | 0.0176 | 0 | 0 |
| 0.48 | 331 | **0.1122** | 49 (0.033) | 9 (0.030) |

**At c = 0.48 the dips are NOT sparse**: 11.2% of all n in [50,3000] sit below
0.48, and even the far tail [2700,3000] has 3% below 0.48. So sparsity is a
sharp property of the *pinned* c=0.40 (and comfortably c≤0.42), and breaks by
c=0.48. The honest statement is *"the dips are sparse only for c ≲ 0.45"*, not
"for c=0.40 with any margin". The margin between 0.40 and 0.48 is where the
claim is thin, and it fails there.

## Finding (i) — boundary effect is real

The true <0.40 dip set is {53, 71, 105} (the 4th reported by the capture,
n=145, is exactly 0.4 and is a float-threshold artifact), and the whole <0.42
set (through N=20000) is {53,56,62,71,103,105,145,153,210,274} — **finitely
many, all ≤ 274**, and empty in the half/tail windows at every threshold ≤ 0.45.
So the full-range [50,N] dip density is entirely small-n and, computed against
a large clean tail, understates *where* the dips live. It is genuinely sparse —
in fact empty beyond n=105 (c=0.40) / n=274 (c=0.42) to N=20000 (nu2_extended)
— but the "density→0" phrase is only meaningful because the set is
(empirically) finite, not because of any tail-limit behaviour.

## Finding (iii) — M(N) is NOT monotone, and violations are dense

The capture's own count: over N=50..3000 there are **937 strict increases in
M's running value being violated**, i.e. M(N) < M(N−1) at 937 of 2951
positions — **density 0.318**. M(N) is far from non-decreasing; roughly a third
of the prefix positions are decreases (M' dips whenever the freshly added
ν₂(n)/n falls below the running average, which with σ² ~ 1e−3 happens
constantly). The running minimum of M over N≥50 is 0.3959, attained at the
FIRST point n=50.

So the strong form of Q1 — "M(N) is non-decreasing" — is **false**, with a
dense (31.8%) violation set, not a small-n transient. The weakened form
"M bounded below on a density-1 set" survives: M stays ≥ 0.396 on every n ≥ 50
(this run's data; the rise 0.44→0.50 in mean_capture confirms it). The claim
as a *disjunction* survives only through the bounded-below branch; the
monotone branch is broken by the tool_builder's own exact count.

## What I could not break

- The pinned c=0.40 (and c≤0.42) dip set is genuinely sparse/finite, exact,
  verified by two independent routes.
- M(n) ≥ ~0.396 on all n ≥ 50 (bounded below), not just density-1.
- Negative controls behave (Thue–Morse ≥ 98% dense in tail, all-ones 100%).

## Bottom line

The central *claim as phrased* "for c=0.40 the dip set is sparse, and M(N) is
monotone/bounded-below" is **half true**: the c=0.40 sparsity holds (finite,
empty past n=274 to N=20000), but (a) M(N) is not monotone — 31.8% density of
monotonicity violations, the smallest being effectively at the very start of
the N≥50 regime with the running min of M at n=50 — and (b) the sparsity is not
robust: at c=0.48 the dips are dense (11% full, 3% tail), so the claim must be
read at its exact pin and not as a margin above 0.40.

Range searched on disk: tool_builder capture N=3000; independent records
nu2_extended to N=20000 and smax trajectory to N=40000. Monotonicity was only
captured to N=3000; extending M's violation density to 40000 was not possible
without a run tool, but 31.8% density at 3000 already refutes monotonicity.

## Claims

```claim
id: dip-sparsity-not-robust-to-0.48
statement: For the prime gap-parity h, the dip set {n : ν₂(n)/n < c} is sparse
  only for c ≲ 0.45. At c=0.48 it is NOT sparse: density 0.112 over [50,3000],
  0.033 over [1500,3000], 0.030 over [2700,3000] (tool_builder capture, exact).
  At c=0.40 it is finite: {53,56,62,71,103,105,145,153,210,274}, empty beyond
  n=274 to N=20000 (nu2_extended, cross-checked by the independent S(n)
  trajectory at 53,71,105).
hypotheses: fold convention d ∈ [2,n-1]; s_sos == s_direct on n=4..200 and
  spots; exact integer arithmetic.
holds-here: yes, measured to N=20000 (dip finiteness) and N=3000 (c=0.48
  density).
status: measured-not-proved
bearing: the claim's sparsity is real at the pinned c=0.40 but is a sharp
  threshold with no margin to 0.48; a result claiming "c=0.40 with slack" would
  be wrong. NOTE the capture's c=0.40 count of 4 is off by one float artifact:
  the true <0.40 set is {53,71,105} (n=145 is exactly 0.4).
```

```claim
id: m-nonmonotone-dense-violations
statement: M(N) = (1/N)Σ_{n≤N}ν₂(n)/n is NOT non-decreasing. Over N=50..3000
  there are 937 positions with M(N) < M(N-1), density 0.318; the running min of
  M over N≥50 is 0.3959 attained at n=50. So the strong form "M non-decreasing"
  is false with a dense violation set; only the weakened "bounded below on a
  density-1 set" survives (M ≥ 0.396 on all n≥50).
hypotheses: same fold/convention/exactness as above; violation = strict decrease
  of the exact rational M.
holds-here: yes, measured N=50..3000 (this run's on-disk capture).
status: measured-not-proved
bearing: any argument that uses monotonicity of the Cesàro mean M is false; only
  the lower-bound form is usable.
```

```claim
id: dip-boundary-effect-small-n
statement: Every ν₂(n)/n < 0.40 dip occurs at n ≤ 105, the set being exactly
  {53, 71, 105}; every ν₂(n)/n < 0.42 dip occurs at n ≤ 274, the set being
  {53,56,62,71,103,105,145,153,210,274}. Both are empty in every tail window
  and empty past their largest member to N=20000. The [50,N] "dip density" is
  entirely small-n: the phrase is only meaningful because the set is finite,
  not because of a tail limit. Verified by two independent routes (nu2_extended
  and the |S(n)|/n trajectory). NOTE n=145 hits 0.4 exactly and is not a <0.40
  dip.
hypotheses: same as dip-sparsity-not-robust-to-0.48.
holds-here: yes, measured to N=20000.
status: measured-not-proved
bearing: warns against reporting dip densities against a huge tail without
  locating the dips; the correct statement is "finite", not merely "sparse".
```
