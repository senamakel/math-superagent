# Filed claims: true-inf crossing and interval B&B feasibility (uc-coupling)

<!-- regenerator-trigger -->

Two results from `code/out/uc_coupling_steps1to4.captured.txt`, produced by the
STEP 1–4 harness-inversion rebuild, filed so the write-up can cite them. Claim 1
is verified-numerically (NON-rigorous; ceiling stated). Claim 2 is a measured
feasibility boundary of the interval method. Neither is a UC result and neither
may drift to `proved`.

```claim
id: coupling-true-inf-crossing-4d
statement: Over the full 4-parameter two-atom coupling class, the true infimum
of g/Eh — with the inf over the coupling P taken internally, i.e. the correct
sup-inf object — crosses 1 between t=0.3824 and t=0.3825 at alpha=0.035, with
minimizer a≈0.3300622 (b2=1). This recovers the published 0.38234 frontier from
the CORRECT object (inf over P internal), consistent with yu-record-0-38234 and
Cambie's t_hat_max ≈ 0.38234553. The crossing is bracketed to a 1e-4 t-interval,
not pinned exactly; the minimizer value is rounded from the capture's
a=0.3300622 to 0.33001 in the directive, and the capture's precision is
recorded here.
hypotheses: Yu's two-atom symmetric coupling family, alpha=0.035, t in
(0.3824, 0.3825), inf over (a1,a2,b1,b2) with b2=1.
holds-here: yes
status: verified-numerically (differential evolution + SLSQP in
code/search/uc-coupling/explore_global_inf.py; NON-rigorous — ceiled, not
proved)
bearing: the published 0.38234 frontier recovered from the correct sup-inf
object after the scorer inversion was fixed; the boundary is the same
t_hat_max ≈ 0.3823455 that Yu/Cambie certify, so this is the run's numeric
recovery of the record from the right object, not a new constant.
anchor: code/out/uc_coupling_steps1to4.captured.txt,
code/search/uc-coupling/explore_global_inf.py
```

```claim
id: coupling-interval-bb-infeasible-10s
statement: The rigorous mpmath.iv interval branch-and-bound CANNOT certify
t=0.38234 within a 10s budget: the margin of the true infimum above 1 is only
8.89e-6 (true inf g/Eh = 1.0000088929 at the Yu minimizer a=0.3300622, b2=1),
and the outward enclosure slope C~21 forces a cell width of ~4.2e-7 across 4
dimensions, with the minimizer on the boundary b2=1. Generic 4D interval B&B
stalls at ~1100 splits in 10s ("inconclusive (time)"), matching
yugamma_global_sup part 2 which certified 0 boxes. The infimum is genuinely
>= 1 at Yu's point; only the rigorous CERTIFICATION is infeasible in budget.
hypotheses: mpmath.iv interval arithmetic; 4-parameter two-atom class; 10s wall.
holds-here: yes
status: measured feasible/not-feasible boundary of the interval method (a
harness/method result, NOT a UC result and NOT a failure of the theorem)
bearing: says what a rigorous certificate would require — an exact/analytic inf
or a tailored interval bound exploiting structure, not generic 4D B&B in a 10s
budget — and stops a later role re-attempting the same generic B&B in the same
budget.
anchor: code/out/uc_coupling_steps1to4.captured.txt,
code/search/uc-coupling/inner_inf_scorer.py, code/out/yugamma_global_sup.captured.txt
```

<!-- the inner-inf conclusion is corroborated independently by
     explore_global_inf.py (agrees on minimizer a≈0.3300622, b2=1, inf≈1.00000889). -->
