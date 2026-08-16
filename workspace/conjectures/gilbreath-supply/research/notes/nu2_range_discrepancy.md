# Measured ν₂/n range correction (operator directive 3)

The measured-values table in `problem.md` previously quoted `ν₂(n)/n` over
`n = 50..4000` as `0.420..0.520`. This run's exact sweep found a wider range,
and the operator has corrected the table to match it. This claim records the
discrepancy so the stale figure is not silently re-imported.

```claim
id: nu2-range-measured-wider
statement: For the primes, ν₂(n)/n over n = 50..4000 lies in [0.3396, 0.6170]. The earlier [0.420, 0.520] in problem.md came from a sampled sub-window and is not the full-range figure.
hypotheses: n ∈ [50, 4000]; convention d ∈ [2, n−1] (maximal {0,2} suffix floored at index 2); ν₂ computed exactly as wt(Φ_n h) over F₂.
holds-here: yes — this is this run's own exact computation (code/out/averaged_mean_capture.txt), not an imported figure.
status: checked
bearing: Corrects the imported range and does NOT affect SUPPLY: 0.3396 is still bounded away from 0. The parent investigation independently saw min 0.3273 at n = 55 over n ∈ [50,2000], consistent with this. The corrected problem.md table now reads min 0.3396, max 0.6170.
anchor: code/out/averaged_mean_capture.txt ("prime nu2/n over n=50..4000: min=0.3396 max=0.6170"); problem.md measured-values table (operator-corrected).
```

Note on an internal convention edge: `research/notes/pattern_finder_nu2_structure.md`
quotes the min as `0.3585` at n = 53 (ν₂ = 19), while the capture's `0.3396`
is ν₂(53) = 18 (18/53 ≈ 0.3396). This is the ±1 convention edge `problem.md`
warns about, not a contradiction in the sweep; quote the convention (here
d ∈ [2, n−1]) whenever the min is stated.
