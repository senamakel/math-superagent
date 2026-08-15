# Directive 62/64 corroboration: the dyadic odd-factor infimum was freshly run this attempt

**Corroboration only — this note carries no fenced claim block.** The single
claim row is `dyadic-oddfactor-infimum-bounded` (status: checked) in
`research/notes/dyadic-oddfactor-infimum-measured.md`; do not look for a claim
block here.

This note is a **fresh corroboration** of the existing claim
`dyadic-oddfactor-infimum-bounded` (status: checked) in
`research/notes/dyadic-oddfactor-infimum-measured.md`. Directive 62 asked for
the one number the dyadic supply route turns on — the infimum over n of
nu2(n)/n for the odd-factor minimal periods P=3,5,7,9 out to n=20000 — and
flagged that `code/out/dyadic_oddfactor_density.py` had been drafted but never
run. This attempt ran the operative script fresh and the number is now on disk
with a this-run capture.

## The number (infimum, not trend) — freshly executed this attempt

`dyadic_inf_measure.py`, exact integers, n_max = 20000, EXIT_CODE = 0.
Capture: `code/out/dyadic_inf_measure_THISRUN.captured.txt` (matches the prior
`dyadic_inf_measure.captured.txt` exactly).

| P | inf nu2(n)/n | attaining n | nu2 at that n | nu2 at n=20000 |
|---|---|---|---|---|
| 3 | **0.647059** | 102 | 66 | 13332 |
| 5 | **0.508772** | 114 | 58 | 10664 |
| 7 | **0.266667** | 105 | 28 | 17142 |
| 9 | **0.359223** | 103 | 37 | 8255 |

## The decisive reading

- The infimum is **bounded away from 0**, and it is **set at small n** (attained
  by n=114, never updated to a lower value out to 20000). So on the periodic
  families `nu2(n) >= c(P)*n` holds uniformly with positive `c(P)` — the
  dichotomy's odd-factor half **does NOT decay to 0** and therefore IS
  supply-useful (unbounded growth with positive infimum, not just unbounded).
- The recorded PLATEAUS (P=7 at 284,284; P=15 at 1064,1064) do NOT signal a
  decaying infimum — they are transient; the infimum is already set below them
  at n~100.
- Power-of-2 contrast (P=1,2,4): inf ~ 0.00005 — the degenerate collapse. The
  dichotomy separates power-of-2 (bounded nu2) from odd-factor (linear) sharply.

## Cross-reference and the corrected open question (Directive 66)

Paired with `thue-morse-sublinear-supply-witness`
(`research/notes/thue-morse-sublinear-supply-witness.md`; status proved), the
pair establishes one dichotomy: **sharp on periodic words, silent on aperiodic
ones.** The infimum above is bounded away from 0 on the odd-factor periodic
families, but Thue–Morse — aperiodic, uniformly recurrent, 2-automatic — has
`ν₂ = O(log n)`. So this note must NOT be read as encouraging for the primes:
the prime halved-gap string is aperiodic, and aperiodicity is now known not to
suffice, so the odd-factor linear growth does not bridge to the primes.

The corrected open question is NOT "is the prime bit string aperiodic?" (known,
and known to be insufficient). It is: **which finer invariant separates
Thue–Morse (log) from the odd-factor families (linear), and where do the primes
sit on it?** Candidate: 2-adic linear complexity, refined to the 2-adic
spectral structure of `σ = I + S` ("2-adic non-rigidity"; see
`dyadic-linear-complexity-supply`). The most informative measurement left on
this route compares that invariant on Thue–Morse, one odd-factor periodic word
(P=3), and the real prime halved-gap string — task
`measure-2adic-separating-invariant-three-strings`.

## What this does NOT do (caveats, stated plainly)

- These are **periodic tail-1 words, explicitly NOT the primes** (the prime bit
  string is aperiodic). This measures only whether the dyadic dichotomy is
  supply-*useful* on the periodic families.
- **Numerical evidence, not a proof.** Nothing beyond n = 20000.
- The converse `nu2 >= c(P)*n for ALL n` remains **conjectured**.
- This does **not** close G-supply for the primes (still the named-open two-point
  mod-4 correlation, `abgs-2011-s9-mod4-switch-limit-open`).

This corroborates, it does not duplicate: the id `dyadic-oddfactor-infimum-bounded`
remains the one claim row; this note adds the this-run capture and the exact
attained values. Do not file a second claim row for the same fact.
