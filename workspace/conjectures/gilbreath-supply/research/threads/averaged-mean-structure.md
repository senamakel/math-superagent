# The averaged mean: monotonicity, dip sparsity, and what the mean implies

Operator directive 3 names this run's capture the most valuable result and says
to push on it. This thread carries that push so the run's next attempts stay on
the averaged form instead of drifting back to the pointwise/switch-density
framing.

```thread
id: averaged-mean-structure
question: For the primes, the Cesàro mean M(n) = (1/n)Σ_{k≤n} ν₂(k)/k rises
  0.4394 → 0.4973 across n = 100..4000 while Thue–Morse falls (0.2255 → 0.0641)
  and the all-ones kernel vector sits at exactly 0.0000. Is M(n) monotone or
  bounded below along a density-1 set of n, are the pointwise dips (min ν₂/n =
  0.3396) sparse rather than merely rare in the sample, does the rise survive a
  model matching only mod-4 switch density, and does M(n) ≥ c imply ν₂(n) ≥ c'n
  on a density-1 set or only infinitely often?
status: dead  (terminus — directive 33: hypothesis refuted by deliverable_3, run closes negative; see research/CONCLUSION.md)
rests-on: nu2-range-measured-wider (measured sweep), G-dict-windowed-zeta
  (ν₂ = wt(Φ_n h)), skeleton supply-averaged-second-moment
blocked-by:
next: Directive 8 — answer with captures, not reading, via the 40000-term
  streamed pipeline (code/nu2_extended/track_smax.py). Five questions: (a)
  M(n) monotone or bounded below on a density-1 set, and sparsity of the
  pointwise dips; (b) does a density-matched surrogate (mod-4 switch density
  only) reproduce the rising mean; (c) does M(n) ≥ c give density-1 or only
  infinitely-often (Chebyshev separation); (d) does the prime switch bit h
  have a component along even-alt or odd-alt (thread kernel-recalibration).
  Each capture states its range and carries a negative control shown failing.
  No new sources without clearing the 204-candidate gate (directive 7).
```

## What the capture establishes (measured, not proved)

`code/out/averaged_mean_capture.txt`, exact sweep, convention d ∈ [2, n−1]:

| input | M(100) | M(500) | M(1000) | M(2000) | M(4000) |
| --- | --- | --- | --- | --- | --- |
| primes | 0.4394 | 0.4832 | 0.4906 | 0.4952 | 0.4973 |
| Thue–Morse | 0.2255 | 0.1378 | 0.1080 | 0.0836 | 0.0641 |
| all-ones (kernel) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

Prime `ν₂(4000)/4000 = 0.4938` (literature 0.4933). The pointwise sweep is
`min 0.3396, max 0.6170` — the corrected range of claim
`nu2-range-measured-wider`; the old `0.42..0.52` was a sampled sub-window and
must not be re-imported.

The three named sub-questions are tasks `attack-averaged-prime-residue-equidistribution`
(umbrella), `density-vs-fold-model-test` (b), and `mean-implies-density1-or-io` (c).

## Directive 12 update — one vacuous capture, one real one

`code/out/dip_sparsity_monotonic.txt` (tool_builder) is a **VACUOUS CAPTURE**:
it ran on the unfloored literal-suffix oracle, which is identically 0 for every
n, so M(N)=0, every dip density = 1.0, and "SUPPLY refuted" would be the
conclusion if it were believed. It is to be DELETED, not cited, and its only
surviving observation (the corrected N=20000 run's c=0.48 half/tail = 0) folded
into the recompute notes. The surviving dip source is
`code/out/refuter_dip_sparsity_findings.md` (task `retire-vacuous-dip-capture`).

**Answered so far (refuter capture, measured N=50..3000):** M(N) is NOT
non-decreasing (density 0.318 of decreases; only bounded-below survives,
M ≥ 0.396 on all n ≥ 50); dips are sparse for c ≲ 0.45 and the < 0.40 set is
exactly {53,71,105}. The density-1 form appears to hold up to c ≈ 0.45 and to
fail at 0.48. **Open conflict:** the refuter's c=0.48 tail [2700,3000] density
0.030 vs the corrected N=20000 capture's c=0.48 half/tail = 0 — resolve by
recomputing to N=40000 (task `recompute-dip-sparsity-40000`), tabulating tail
density against c = 0.40..0.49 step 0.01 with all-ones and Thue-Morse
controls.
