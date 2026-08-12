# Tasks

- [x] Run the oracle test of the lib/gears.py meshing model against PE620 values
  (code/oracle_test.py, output code/out/oracle_test.txt).
- [x] Verdict established: model FAILS all three oracle values — g(16,5,5,6)=0
  vs 9, G(16)=0 vs 9, G(20) per-pair sum at grid 50000 = 0 vs 205. Claim
  `gears_model_fails_oracle` in code/out/oracle_test.md (checked); corroborated
  by concurrent note code/out/oracle-model-broken.md. Diagnosis: the
  continuous-d parameterization has residual O(1) over the valid d interval
  except the degenerate endpoint d=1/(2pi), with interior / boundary valid
  configurations absent.
- [ ] Implement the discrete least-mesh-angle model (planets at multiples of
  beta = 2*pi/(s+c) about S's centre, centres on the two-focus ellipse) as the
  replacement oracle and confirm it reproduces g(16,5,5,6)=9, G(16)=9, G(20)=205.