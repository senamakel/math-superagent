# Attempt 2 (goals) — status and deliverables

## What this attempt did

This is attempt 2, continuing the SUPPLY investigation. The operator's
directive (18/19) asked for two concrete things, both done:

1. **Record in DIRECTIVES.md which call site fed Thue-Morse under a PRIMES
   header** (directive 17 asked, never stated). Done: added a "Call-site answer"
   block. The data path was NEVER wrong — no wrong h reached STAGE1. The defect
   was a hardcoded default `seq="PRIMES"` in `format_rows` in
   `code/averaged/chebyshev_verify_oracle.py`, so the negative-control (Thue-Morse)
   section's value 0.0641 could print under a "mu_N (Primes)" label. The
   array-level guard (assert on the PRODUCED array: nu2[53]==18, nu2[64]==27,
   nu2[4000]==1975, mu_4000~0.4977) now aborts on any non-prime h. The two
   discredited captures are non-citable because of this LABEL defect, not a
   data-path one.

2. **Extend Ratio B to settle the limit (1 vs constant above 1)** (directive 19,
   task extend-ratio-b-decade). Done to N=80000 (one doubling past 40000), via a
   new exact-s_sos program `code/ratio_b/measure_ratio_b.py` (guards asserted on
   the produced array). Result: Ratio B = 1.297@80000, sequence
   1.443@1000 → 1.392@4000 → 1.361@10000 → 1.337@20000 → 1.315@40000 → 1.297@80000,
   per-doubling decrements 0.051, 0.032, 0.024, 0.021, 0.019. The decrements are
   STILL SHRINKING at the last step (0.019 < 0.021) — evidence for a limit above
   1 (permanent structural excess), but NOT proof. A single extra point cannot
   separate limit=1 from limit>1.

Honest cost note on the directive's "one decade further is affordable": the work
is O(N^2 log N), so a full decade (40000→400000) is ~100x the N=40000 cost, and
each further doubling ~4x the prior. One doubling to 80000 cost 326s (~5.4 min)
and was the affordable new datum. Several more doublings (160000, 320000, each
~4x runtime, ~22 min for 160000) would be needed to actually settle the limit.
160000 was NOT run — over the per-command budget. So the limit is genuinely
UNDETERMINED by the measured range, and the excess PERSISTS. This is stated
honestly rather than settled by extrapolation, exactly as the operator demanded.

## Claim / records updated

- Claim `fair-variance-log-null-tail-clean-40000` in
  `code/out/fair_variance_at_40000.note.md` updated to include 1.297@80000 and
  the still-shrinking decrements; mirrored in `research/ROOT.md` and the derived
  `research/CLAIMS.md`.
- Task `extend-ratio-b-decade` left open with the extended data recorded.
- Durable memory stored (Ratio B extended to 80000, limit undetermined).
- Board posts: the data-path formal label lesson; the Ratio B extension hunch.

## Verification

- The baseline N=1000..40000 was reproduced EXACTLY by the new program,
  independently confirming the reduce convention (denominator N−1) against the
  earlier capture.
- Array-level guards passed on the produced array: nu2[53]=18, nu2[64]=27,
  nu2[4000]=1975, mu_4000(prod)=0.497259 within 0.01 of 0.4977.
- Negative controls (all-ones vacuous, Thue-Morse failing density-1) were
  verified with the SAME oracle in the parent chebyshev capture; this run itself
  had no failing control (stated as a limitation).

## Not claimed

- NOT claimed: SUPPLY proved. NOT claimed: Ratio B limit settled. NOT claimed:
  Gilbreath. Everything is labelled measured-not-proved; the limit question
  explicitly remains open.
