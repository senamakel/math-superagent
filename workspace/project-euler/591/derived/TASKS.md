# Tasks

All tasks complete. Each item below is backed by an executed program and its
captured output.

- [x] Task 1: brute.py reproduces worked examples 1-3 exactly ((6,-2), (-55,26),
      (560323,-211781)). Float caveats noted (brute is float-only, not scalable).
- [x] Task 2: probe_records.py — record b's for ||b sqrt(d)-pi||_Z over several d;
      semiconvergent hypothesis tested and REJECTED (records are Cabanillas
      candidates, not semiconvergents in general; d=2 n=1e13 oracle b is not a
      semiconvergent denominator of sqrt(2)).
- [x] Task 3: d=2, b=4375636191520 verified as the n=1e13 argmin with
      a=-6188084046055 (example 4 oracle reproduced by both solvers; residual
      a + b sqrt(2) - pi = -4.2930117e-15, consistent with the statement's
      sandwich inequalities).
- [x] Derive the scalable (Cabanillas Prop 9/10) method; state it in solution.md
      with the exact theorem statement in
      research/cabanillas_prop9_10_exact_statement.md.
- [x] Implement solution_bothsides.py (both signs of b) and the fully
      independent solution_ostrowski.py (exact-integer periodic CF +
      Ostrowski/alpha-numeration); both reproduce examples 1-4 and agree with
      brute force on all 90 d at n=1e6 (both signs) and 16 d at n=1e7.
- [x] Compute S at n=1e13 with both solvers and record to
      results_full_bothsides.txt and results_ostrowski_n13.txt;
      S = 526007984625966.
- [x] Verify by a second independent full-scale route: solution_ostrowski.py
      written fresh from the theorem (no code shared with the first solver),
      run at n=1e13 for all 90 d; its file is byte-identical to the first
      solver's file (diff empty, crosscheck_two_routes.py: (b,a) identical on
      all 90 d, both sums 526007984625966).
- [x] Independent audit of the result rows without any solver code
      (audit_results.py): 7/7 checks, 90/90 on every row-level check,
      d=2 oracle residual PASS, exact re-sum S = 526007984625966.
- [x] Mid-scale independent check at n=10^7: brute_n7.py (16 d, mpmath dps=40)
      vs both-sides solver at the same n — exact (b,a) agreement on all 16 d
      (results_brute_n7.txt, results_solver_n7.txt, brute_n7_run.log,
      verify_n7_rerun.py).
- [x] Report the answer, method, and verification in the run summary.