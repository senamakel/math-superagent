# Two capture findings from the uc-coupling STEP 1–4 run

Anchors:
- `code/out/uc_coupling_steps1to4.captured.txt`
- `code/search/uc-coupling/explore_global_inf.py`
- `code/search/uc-coupling/inner_inf_scorer.py`
- `code/search/uc-coupling/true_cross.py`
- `code/out/yugamma_global_sup.captured.txt`

Both findings are real results of this run's harness investigation. Neither is a
UC result; claim 1 is a numerical recovery of the published frontier from the
CORRECT (sup-inf) objective, claim 2 is a measured feasibility boundary of the
generic interval certification method. Neither may drift to "proved".

```claim
id: coupling-true-inf-crossing-0-3824
statement: Over the full 4-parameter two-atom class, the true inf of
  g(P,alpha)/Eh (inf over P taken internally, alpha=0.035) crosses 1 between
  t=0.3824 and t=0.3825, with minimizer a ~= 0.3300622. This recovers the
  published 0.38234 frontier from the correct sup-INF object (sup over alpha,
  inf over the coupling taken inside the scorer), consistent with
  yu-record-0-38234 and Cambie's t_hat_max ~ 0.3823455333667. The crossing is
  bracketed to a 1e-4 t-interval, not pinned exactly.
hypotheses: F union-closed; the 4-param two-atom coupling class; alpha=0.035
holds-here: yes (it is the run's own regression check on the rebuilt objective)
status: verified-numerically (differential evolution + SLSQP in
  explore_global_inf.py; NON-rigorous -- floating point search, not interval/
  symbolic proof); ceiling stated: the crossing is bracketed to a 1e-4 interval
  and the minimization is numerical
bearing: confirms the rebuilt sup-inf scorer lands on the honest frontier
  (Yu/Cambie value) rather than climbing past the proved ceiling; a regression
  check that the objective inversion is fixed
anchor: code/out/uc_coupling_steps1to4.captured.txt, STEP 1;
  code/search/uc-coupling/explore_global_inf.py
follows-from: yu-record-0-38234, cambie-question2-exact-0-3823455
```

```claim
id: coupling-interval-bb-infeasible-10s
statement: The rigorous mpmath.iv interval branch-and-bound cannot certify
  t=0.38234 within a 10s wall: the true inf_P g/Eh at Yu's point is
  1.0000088929 (margin above 1 is only 8.89e-6), the outward enclosure slope is
  C ~ 21, forcing cell width ~4.2e-7 in 4 dimensions, and the minimizer sits ON
  the box boundary b2=1 (the boundary-collapse case generic intervals fail on).
  B&B stalls at ~1100 splits in 10s ("inconclusive (time)"). This is why
  yugamma_global_sup part2 certified 0 boxes.
hypotheses: the generic 4D interval B&B scheme as implemented, 10s budget
holds-here: yes (it is the method's measured behaviour in this run)
status: measured feasibility boundary of the interval certification method --
  a harness/method result, NOT a UC result and NOT a failure of the theorem
  (the inf is genuinely >=1 at Yu's point; only the certification is
  infeasible in the budget)
bearing: states what a rigorous certificate would require -- an exact/analytic
  inf or a tailored interval bound exploiting structure, not a generic 4D B&B;
  stops a later role re-attempting the same generic B&B in the same budget
anchor: code/out/uc_coupling_steps1to4.captured.txt, STEP 1;
  code/out/yugamma_global_sup.captured.txt;
  code/search/uc-coupling/inner_inf_scorer.py
follows-from: yu-record-0-38234 (the point being certified is the real theorem
  point)
```
