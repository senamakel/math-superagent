# Tasks

- [x] Run the oracle test of the lib/gears.py meshing model against PE620 values
  — FAILED (g=0 vs 9).
- [x] Discrete least-mesh-angle lattice model — FAILED (g=0 vs 9).
- [x] Phase-model probe (`phase_model_probe.py`, eps=±1): 2 of 4 chi/gamma sign
  variants tested — both return g(16,5,5,6)=0.
- [ ] **STEP 1 — Probe the remaining 2 of 4 independent sign variants** in the
  idler-phase model (`code/pattern/phase_model_probe.py`). Currently eps=±1 ties
  both gamma and beta coefficients together; extend to independent signs on the
  gamma-term and beta-term coefficients. If any variant gives g(16,5,5,6)=9,
  verify G(16)=9 and G(20)=205.
- [ ] **STEP 2 — If all 4 sign variants still give 0:** stop deriving conditions
  top-down. The thread `offcentre-mesh-phase-model.md` proves tangency forces
  exactly two positions per planet type (mirror pair about the line of centres),
  so an arrangement is determined by d alone. Enumerate candidate configurations
  for (16,5,5,6) directly: place the four planet centres by tangency at a fine
  grid of d values, compute tooth phases numerically (full explicit tooth-mesh
  check, not a phase-congruence shortcut), and print the nine that survive. A
  model that cannot produce a single valid arrangement for the one case you can
  check is not a model to refine — finding what the nine actually look like
  will show which condition is wrong.
- [ ] solution.md: governing theory + efficient method whose cost does not grow
  with 500.
- [ ] code/solution.py: exact arithmetic G(500), agree with brute on all
  reachable cases.
- [ ] Verify G(500) by a second independent route.