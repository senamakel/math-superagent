# uc-coupling scored search — report

## STEP 1..4 outcome (current truth, this pass)

**STEP 1 (true inner-inf, rigorous): NOT certifiable in 10 s.** A new
`inner_inf_scorer.py` takes only alpha and minimises g(P,alpha)/Eh over the
4-param two-atom class internally by mpmath.iv interval branch-and-bound. At
t=0.38234, alpha=0.035 the true `inf_P g/Eh = 1.00000889` (confirmed by the
independent global search `explore_global_inf.py`, minimizer a≈0.3300622, b2=1),
but the enclosure lower bound only crosses 1 at cell width ~4e-7 (margin 8.9e-6,
outward slope ~21), so the B&B needs ~20 bisection levels in 4 dims and stalls
at ~1100 splits in the 10 s wall ("inconclusive (time)"). This reproduces the
`code/out/yugamma_global_sup.py` part2 failure. **The rigorous inner-inf is the
blocker that stops the scored search per the directive.**

**STEP 2 (guards on score.py):** ceiling clamp (T_HAT_MAX=0.3823455334 + slack
1e-6 ⇒ INVALID above), degenerate-atom floor (A_FLOOR=B_MINUS_A_FLOOR=0.1), and
an INVALID self-test block (`python3 score.py __selftest__`). SELF-TEST PASS.

**STEP 3 (re-calibration):** `python3 score.py candidates/c0009.py` (Yu's
certified witness) still prints **SCORE: 0.3823435642**, within the ceiling —
the guard does not break calibration on the certified witness.

**STEP 4 (re-score every candidate):** c0024..c0032 now INVALID (certified score
0.3823610..0.3937600 > ceiling), c0033 INVALID (degenerate-atom a=0.01 < floor);
the Yu witness block (c0000,c0001,c0002,c0005,c0006,c0007,c0009,c0016..c0023)
stays **SCORE: 0.3823435642**.

## Verdict

STEP 1's rigorous inner-inf is **not feasible in 10 s**. That infeasibility is
the blocker: the harness cannot certify `inf_P g/Eh ≥ 1` and so cannot certify
any t. The two-atom class certifies nothing above t̂_max ≈ 0.3823455; only the
argmin (Yu, a≈0.3300622) plateau at 0.3823435642 is genuine.

## What the scorer computes vs. what the theorem needs (historical) (historical)

[original body]

The scorer takes the candidate coupling P (params alpha,a1,a2,b1,b2), sweeps
beta=(t-a)/(b-a) over the t-grid in (a, min(b,1/2)], and certifies the largest t
at which the **single coupling's** ratio g(P,alpha)/E h(p) has a rigorous
interval lower endpoint >= 1.

Yu's theorem (eq 2) requires the **infimum over couplings**:

    Gamma_hat(t) = sup_alpha  inf_{P_pq}  g(P_pq,alpha)/E h(p),

and certificates t only when that inf >= 1. A single P gives an **upper bound**
on the true inf (g(P)/Eh >= inf_P g/Eh), so a non-argmin coupling inflates the
ratio past the genuine certificate.

## The exploit, empirically

I kept the coupling inside Yu's two-atom symmetric class (b2=1, b1=a1=a2=a) and
moved a away from Yu's argmin value ~0.330. The certified t:

  a=0.3300622 -> 0.3823435642  (Yu witness, believable)
  a=0.32      -> 0.3823610000
  a=0.31      -> 0.3824280000
  a=0.30      -> 0.3825300000
  a=0.29      -> 0.3826835000
  a=0.28      -> 0.3828830000
  a=0.25      -> 0.3838000000
  a=0.20      -> 0.3859550000
  a=0.10      -> 0.3937600000
  a=0.01      -> 0.4219920000

It climbs monotonically past the proved ceiling t_hat_max ~ 0.3823455333667,
with no plateau — the missing-inf signature. A genuine certificate is capped at
t_hat_max by the proved Gamma_hat monotonicity.

## Bottom line

- **Believable top score: 0.3823435642** — Yu's certified witness itself
  (a=0.3300622, b2=1, alpha in [0.03,0.05]), reproducing Yu's published 0.38234
  and consistent with Cambie's ceiling. Grid-limited (N=20000, step ~8.5e-6).
- **Apparent top score 0.422 (a=0.01): NOT believable** — it is the scorer's
  missing-inf hole, not mathematics.
- **Plateau / binding constraint (believable):** the binding constraint is t
  (the Gamma_hat(t)>=1 boundary), matching the proved monotonicity; no coupling
  in the two-atom class certifies above ~0.3823455.
- **The finding:** score.py must take the inf over the coupling space at each
  (alpha,t) before certifying. As written it is a search whose score always
  "improves" by moving away from the argmin — the exact verifier-exploit shape
  the directive warned about.

## Truth of the numbers

I did not tune toward the exploit knowingly to get a good score; I pushed a down
as a legitimate structure search and the climb past the ceiling alerted me to
the hole, which I confirmed by reading Yu eq (2) and the run's own
Gamma_hat-nonincreasing claim. I stopped at a=0.01 rather than pushing to
a=0 to make a false 0.5: continuing would only have manufactured an exploit
score. The scored rows are recorded in SCORED_ROWS.md and FINDINGS.md.
