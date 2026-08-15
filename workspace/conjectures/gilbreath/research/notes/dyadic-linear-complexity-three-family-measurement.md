# Directive 66 — separating-invariant comparison, corroboration only

**Corroboration only — this note carries no fenced claim block.** The single
claim row is `dyadic-separating-invariant-three-strings` (status: checked), in
`research/notes/dyadic-separating-invariant-three-strings.md`, anchored at
`code/out/measure_separating_invariant_THISRUN.captured.txt`. Do not look for a
claim block here and do not file a second claim row for this fact.

This note exists because the same Directive-66 comparison was independently
re-ran this attempt and read directly from the capture. It confirms the
canonical note verbatim.

## The three-family comparison (n ≤ 4000, exact integers, real ground truth)

| family | ν₂/n @ n=100 | ν₂/n @ n=4000 | regime |
|---|---|---|---|
| Thue–Morse (h[j]=wt(j) mod 2) | 0.270 | **0.011** | collapses, ν₂/n → 0 |
| odd-factor P=3 periodic [0,0,1] | 0.660 | **0.667** | linear, constant density ≈ 2/3 |
| REAL primes (actual right diagonal) | 0.430 | **0.493** | linear, constant density ≈ 1/2 |

Capture: `code/out/measure_separating_invariant_THISRUN.captured.txt`, EXIT 0.

## The reading

- **The invariant separates.** Thue-Morse (aperiodic, rigid) collapses to
  O(log n); P=3 and the real primes both grow with constant positive density.
- **The primes sit on the linear (non-rigid) side**, ν₂/n ~ 0.49-0.50,
  `ν₂(primes)/ν₂(P3)` ≈ 0.74 at n≥1000 — far from the Thue-Morse collapse.
- **Numerical only** (n ≤ 4000, sieve 4e5 ~33860 primes), does NOT close
  G-supply (`abgs-2011-s9-mod4-switch-limit-open` stays the named-open
  two-point mod-4 hypothesis).
- The 2/4 reconstruction from the primes' mod-4 switch bits is a faithful
  shadow of the true prime diagonal (values within 0-3 at every sampled n), so
  the dyadic-2/4 model is a valid lens on the true dynamics.

This corroborates `dyadic-separating-invariant-three-strings`; it adds nothing
and duplicates nothing.
