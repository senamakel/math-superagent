# Working memory

## Problem

S = sum over non-square d in [2,99] of |I_d(BQA_d(pi, 10^13))|.

BQA_d(x,n) = argmin over (a,b), |a|<=n, |b|<=n of |x-(a+b*sqrt(d))|.
I_d(a+b sqrt(d)) = a.

For fixed b, best a = round(pi - b*sqrt(d)), error = ||b sqrt(d) - pi||_Z.

## Worked examples (test oracle)
1. BQA_2(pi,10)        = 6 - 2 sqrt2        a=6,b=-2
2. BQA_5(pi,100)       = 26 sqrt5 - 55      a=-55,b=26
3. BQA_7(pi,10^6)      = 560323 - 211781 sqrt7  a=560323,b=-211781
4. I_2(BQA_2(pi,10^13))= -6188084046055     a=-6188084046055,b=4375636191520

## Verified (Task 1)
brute.py reproduces examples 1,2,3 exactly (see run output in scratchpad).
solution_bothsides.py reproduces ALL FOUR examples (1-3 plus the d=2 n=1e13 oracle).

## Verified (mid-scale independent check, n=10^7)
brute_n7.py scans all b in [-floor(n/sqrt(d)), floor(n/sqrt(d))] at mpmath
dps=40 for d in [2,13,14,15,18,19,21,22,27,29,41,42,52,59,80,98] with n=10^7,
setting a = nint(pi - b*sqrt(d)) clamped to [-n,n].  Results in
results_brute_n7.txt; run log in brute_n7_run.log.

Comparison vs the corrected both-sides solver (solution_bothsides.py) run at
the SAME n=10^7 (results_solver_n7.txt): exact (b, a) agreement on all 16 d.
So the corrected solver is independently validated at 10^7 — 1000x above the
previously validated 10^6 and 1e6x below the 10^13 target.  NOTE: comparing
brute@1e7 against results_full_bothsides.txt (n=1e13) shows mismatches for
every d, which is expected: the optimum (a,b) changes with n.

## Additional exact laws (verified on corrected both-sign data, n=1e13)
- |I_d| == |nint(b_d sqrt(d) - pi)| for all 90 d (90/90).
- m^2 scaling: |I_{m^2 d0}| == |I_{d0}| iff m | b_{d0} (36/36 pairs); when equal,
  b_{m^2 d0} == b_{d0}/m (18/18).

## Established results
- Cabanillas Prop 9/10 (arXiv:1904.01874) candidate set for record b's of
  ||b alpha - beta||_Z, alpha={sqrt d}, beta={pi}, verified EXACTLY against
  brute force on d in {2,3,5,7,11}, N in {200,1000,5000} AND at full method
  scale n=10^6 for ALL 90 non-square d (both signs of b):
  b_d = Cabanillas candidate with minimum distance; a = nint(pi - b sqrt(d)).
  (toolkits/verify_cabanillas_exact.py, toolkits/validate_all_d.py,
   toolkits/validate_bothsides.py)
- d=2 oracle verified exactly: a+b.sqrt(2)-pi = -4.2930117e-15; b=4375636191520
  is NOT a sqrt(2) semiconvergent denominator (toolkits/verify_oracle_d2.py).
- uniform exact relation at n=10^4 (90 d's): |I_d| = nint(b_d*sqrt(d) - pi)
  = nint(b_d*sqrt(d)) - 3  (toolkits/analyze_Id_b.py). NOTE: |I_d| != round(sqrt(d)*b)
  (check_rel.py claims were false).
- record-b sequences (probe_records.py, N=2e6) show NO simple linear recurrence,
  no polynomial growth; all are Cabanillas candidates, NOT semiconvergents in general.
- **ALL 90 non-square d validated**: at n=10^6, Cabanillas-candidate b_d equals
  brute-force argmin for every d in [2,99] (toolkits/validate_all_d.py, 47s,
  zero mismatches). This is the uniform cross-check of the method across all d.
- **FINAL two-route cross-check** (crosscheck_two_routes.py): results_full_bothsides.txt
  (Cabanillas candidate) and results_ostrowski_n13.txt (Ostrowski numeration) are
  byte-identical (diff empty, exit 0). Parse: 90 numeric rows each; (b,a) identical
  on every d; |a|,|b| <= 1e13 on all rows; both indicate S=526007984625966, and
  independent exact re-sums of the |a| column both equal 526007984625966. audit_results.py
  passes all 7 checks (90/90 each) with d=2 oracle residual -4.2930117e-15.

## Failed approaches
- "records are semiconvergents of sqrt(d)" hypothesis: FALSE (d=2 oracle b not a
  semiconvergent; most records aren't).
- check_rel.py |I|=round(sqrt(d)*b): FALSE.

## Open questions (all resolved)
- CONFIRMED (all closed): b_d at n=10^13 via Cabanillas candidates reproduces
  d=2 oracle (b=4375636191520, a=-6188084046055).
- **CRITICAL correction**: b may be NEGATIVE. solution.py searched only b>=0 and
  got S=498809825393729, which is WRONG. Corrected both-sign solver
  /workspace/solution_bothsides.py reproduces examples 1-4 (d=2,n=10 has b=-2;
  d=7,n=1e6 has b=-211781) and matches brute force on all 90 d at n=1e6
  (toolkits/validate_bothsides.py). **S (corrected) = 526007984625966**,
  written to /workspace/results_full_bothsides.txt. Positive-only was strictly
  worse on 45 d (negative-b winners), never better.

## Independent full-scale confirmation (solution_ostrowski.py)
Wrote a FULLY INDEPENDENT solver fresh from the theorems in
research/cabanillas_prop9_10_exact_statement.md (Algorithm 3(ii), Prop 9, Prop 10,
irrational-alpha Case 2) — no code imported/copied from solution.py or
solution_bothsides.py. Distinct implementation: sqrt(d) CF via the EXACT integer
periodic (P,Q,a) recurrence so all q_k are exact ints; alpha=sqrt(d)-floor(sqrt(d));
numeration of beta={pi} and 1-beta via Algorithm 3(ii) at mpmath dps=220;
Prop 9+10 candidates kept to n<=L=floor(1e13/sqrt(d)); min distance per side sets
sign of b; a=nint(pi-b sqrt(d)). Margin check confirmed: no ceil(beta/delta) digit
decision within 1e-90 of an integer (flagged decisions occur only at k far beyond
where the numeration prefix exceeds L — no relevant digit is near an integer).
Driver (solution_ostrowski.py) reproduces:
  - all 4 worked examples exactly (d=2 n=10 -> (6,-2); d=5 n=100 -> (-55,26);
    d=7 n=1e6 -> (560323,-211781); d=2 n=1e13 -> a=-6188084046055,b=4375636191520);
  - 0 mismatches vs brute scan (b in [-L,L], a=nint(pi-b sqrt d), dps=50) on ALL
    90 non-square d at n=1e6;
  - 0 mismatches on the 16 d at n=1e7 vs results_brute_n7.txt;
  - full n=1e13 run -> /workspace/results_ostrowski_n13.txt, S=526007984625966;
  - row-by-row (b,a) for all 90 d IDENTICAL to results_full_bothsides.txt
    (0 mismatches);
  - independent exact re-sum of results_ostrowski_n13.txt = 526007984625966 = S.
This is a second, independent full-scale route to the same answer as
solution_bothsides.py, confirming S = 526007984625966.

## Final answer (this attempt, re-verified by execution)
S = 526007984625966. Re-verified fresh on this run: brute.py reproduced examples
1-3 verbatim ((6,-2), (-55,26), (560323,-211781)); solution_bothsides.py
reproduced examples 1-4 (d=2, n=1e13 -> a=-6188084046055, b=4375636191520);
independent exact-int re-sum of results_full_bothsides.txt = 526007984625966;
solver vs brute at n=1e7: exact (b,a) on all 16 d (verify_n7_rerun.py);
solver vs brute at n=1e6, both signs, all 90 d: 0 mismatches (validate_bothsides.py).
Derivation in solution.md; precise theorem statement in
research/cabanillas_prop9_10_exact_statement.md.
