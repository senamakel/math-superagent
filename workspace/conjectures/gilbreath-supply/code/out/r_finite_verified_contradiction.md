# Contradiction: settled rung R-finite-verified vs exact computation

The ladder `research/weakened/supply.md` rung `R-finite-verified` is marked
**settled** with statement:

> For the real prime string h (floor convention at index 2), ν₂(n)/n ≥ 0.42
> for every n with 50 ≤ n ≤ 4000, c = 0.42 explicit. Numerical evidence, not
> a theorem.

Two independent exact computations contradict this at its stated range. Both
use the submask-product SOS transform, cross-checked against a direct brute
oracle, on the real prime gap-parity string.

- `code/out/pattern_var_note.md` + `research/notes/pattern_finder_nu2_structure.md`
  (exact DP, cross-checked vs brute on {2,3,5,8,13,21,34,55,64,89,100,128}):
  **exactly 10 points in [50,4000] have ν₂/n < 0.42** —
  n = 53(ν₂/n=0.3585), 62, 66, 71, 103, 105, 145, 153, 210, 274. Local means
  around every dip are ~0.48–0.50, so the dips are pointwise minutes, not
  depressions.
- `code/out/g_mean_linear_grounded.md`: "n=53 gives 0.34, min over [200,500)
  is 0.416 at n=274"; min over [500,1000) is 0.443, over [1000,2000) 0.460.

Both agree: the 0.42 bound holds after n=274 (tail min ≥0.443), but not in
[50,274]. The 0.42 value traces to problem.md's table, which
`research/BACKWARD.md` flagged as "ungrounded prose — re-ground it". The mean
and the dying tail (only 10 violations, largest n=274) are unaffected, so the
averaged-form conclusions and the density-1 story stand — but the rung's
pointwise statement as written is FALSE at its full stated range.

## What to do

Re-state the rung as "ν₂(n)/n ≥ 0.42 for all n ≥ 500 (N₀ = 500); the
exceptional set E = {n∈[50,4000] : ν₂/n < 0.42} has size 10 and is contained in
[50,274]". The pointwise-all-n rung was always numerical (not a theorem), and
this correction does not change that — it only fixes what "verified" claims.

```claim
id: r-finite-verified-contradicted
statement: The settled rung R-finite-verified "ν₂(n)/n ≥ 0.42 for all 50≤n≤4000" is false: exactly 10 points in that range have ν₂/n < 0.42, deepest ν₂(53)/53 = 0.3585, all confined to [50,274]. Past n=274 the minimum over computed ranges is ≥ 0.443.
hypotheses: floor convention at index 2, d-range [2,n-1]; prime gap-parity string h[j]=((q_{j+1}-q_j)/2) mod 2; exact integer DP cross-checked vs brute oracle.
holds-here: yes (the claim is about the very range the rung makes its assertion on)
status: checked (two independent exact computations agree)
bearing: R-finite-verified as written overstates its range; must be restated with N₀=500 or the exceptional set named. Averaged/density-1 conclusions are unaffected (tail still ≥0.44, only 10 violations, largest 274).
anchor: code/out/pattern_var_note.md; research/notes/pattern_finder_nu2_structure.md; code/out/g_mean_linear_grounded.md
contradicts: R-finite-verified (research/weakened/supply.md)
```
