# tool_builder report — dyadic-gap-character route: verification tasks A & B

Scripts in `code/dyadic/`, captured atomically (exit-status guarded) via
`python3 -m lib.capture` into `code/out/`.

## TASK B — corrected character identity: PASS (6868/6868), negative control FAILS as required

`code/dyadic/verify_character_identity.py` →
`code/out/dyadic_verify_character_identity.captured.txt`

Asserted, for every n in 20..120 and every d in [2, n-1] (6868 pairs), against the
literal submask-XOR oracle `t_direct`:

    (-1)^{T(n,d)} == prod over runs R=[u,v] of downset(d) of
                     chi(r[a_R]) * chi(r[b_R])
    a = n-1-d+u,  b = n-1-d+v+1,  chi(x) = -1 if x%4==3 else +1

Result: **6868 / 6868 pass** (0 corrected-form failures).

NEGATIVE CONTROL: a spurious `(-1)^{#runs(d)}` factor (multiply the product by
-1 when the run count is odd) **fails on 449 of the 6868 pairs, including d=3**
(first example (20,3): true −1 vs spurious +1). This proves the
no-extra-sign form is the true one — the corrected identity is distinguished
machine-verifiably. So the sign-correction in the dyadic-gap-character approach
(`research/approaches/dyadic-gap-character-correlation.md`) is now grounded at
n≤120 over the full d-range, not just hand-verified d=2,3.

> Implementation note for future agents: `t_direct(n,d,x)` takes the **switch**
> string h (h = h_from_r(r)), NOT the residue string r. A first run fed r to
> it and failed on 3419 pairs; feeding h fixes it. Worth recording so it is not
> rediscovered.

## TASK A — popcount stratification of S(n): weight is spread, NOT low-popcount-dominated

`code/dyadic/stratify_by_popcount.py` →
`code/out/dyadic_stratify_by_popcount.captured.txt`

Cross-checks: at n=200 the SOS per-term transform sums to the same S and T=1
count as `s_direct` and `s_char_runs` (all three: S=0, ones=99).
`nu2` recurrence cross-check: n=4000 primes S=48 ⇒ nu2=(3998−48)/2=1975,
matching the on-disk floored-convention value 1975.

Real prime residues:

| n | S(n) | \|S\|/n | low-popcount \|S\|-share | max stratum \|sum\|/n |
|---|------|--------|--------------------------|------------------------|
| 400 | −16 | 0.040 | 0.435 (p≤4) | 0.0375 (p=5) |
| 1000 | −2 | 0.002 | 0.676 (p≤4) | 0.0200 (p=4) |
| 4000 | +48 | 0.012 | 0.740 (p≤5) | 0.0080 (p=5) |

Random-{1,3} control (fixed seed): |S|-shares 0.500 / 0.500 / 0.603; the profile
is similar and each stratum's |sum|/n is again tiny (max 0.0225).

### Honest verdict (measured, not proved)

Every single popcount stratum carries a sub-linear share of S(n) — no stratum
(and in particular NO low-popcount/few-run stratum) dominates; the largest
per-stratum magnitude is ≤ 0.0375·n. So the dyadic-gap-character route's
**falsifiable premise does not hold on this input**: the bulk of S(n) does *not*
live in low-popcount strata where a pointwise dyadic-gap correlation bound on
χ(r)=(−1/q) could be applied cheaply. At n=4000 the weight is genuinely spread
across p=4..11. This is consistent with the route collapsing toward switch
density (GOAL priority 3): bounding S(n) needs an input as strong as the mean,
not a weak correlation bound on a few-run subset.

Caveats, stated so nothing over-reads: this is a *measurement on the finite
real prime-residue string up to n=4000* (and one random control). It does not
prove the route dead for all n — but it directly fails the route's specific
"low-popcount strata dominate" amenable-region premise at every n tested, and
the trend (share rising toward n=4000 while per-stratum magnitude shrinks) is
the opposite of what the route needs. A run that pushes n further would only
re-confirm spread; the next decisive move is the Krawtchouk/second-moment
geometry, not more strata counting.

## Files

- `code/lib/supply_fold.py` — added `s_terms_sos(n,h)`: per-depth terms
  `[(-1)^{T(n,d)}]_{d=2..n-1}` via the same O(n log n) SOS; sum & −1-count
  equal those of `s_sos`. Contracts re-checked at n=64, 200.
- `code/dyadic/INDEX.md`, `code/lib/INDEX.md` — updated.
- Captures: `code/out/dyadic_verify_character_identity.captured.txt`,
  `code/out/dyadic_stratify_by_popcount.captured.txt`.
