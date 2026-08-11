# Tasks

- [x] Task 1: verify brute.py reproduces the 3 worked examples; report float caveats.
- [ ] Task 2: probe_records.py — record b's for ||b sqrt(d)-pi||_Z over several d; test semiconvergent hypothesis.
- [ ] Task 3: d=2, check b=4375636191520 is a semiconvergent denominator of sqrt(2); verify example 4 numerically.
- [x] Derive scalable (CF/Legendre) method; implement solution.py.
- [x] Reproduce example 4 (d=2 n=1e13: a=-6188084046055) and examples 1-3
      (covered by test_method_scale.py oracle checks) with the real method.
- [x] Compute S and verify by independent route (re-sum of results_full.txt,
      b<=L and a==nint(pi-b sd) checks on all 90 rows; S=498809825393729).
