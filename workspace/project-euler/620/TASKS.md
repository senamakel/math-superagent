# Tasks

- [x] Run the oracle test of the lib/gears.py meshing model against PE620 values
  — FAILED (g=0 vs 9).
- [x] Discrete least-mesh-angle lattice model — FAILED (g=0 vs 9).
- [x] Phase-model probe (`phase_model_probe.py`, eps=±1): 2 of 4 chi/gamma sign
  variants tested — both return g(16,5,5,6)=0.
- [x] Tangency enumeration (`code/pattern/tangency_enum.py`, residue model with
  independent sigma/eta/theta signs): **g(16,5,5,6)=9 for variant (sigma=-1,
  eta=-1, theta=-1)** — matches oracle. See `code/out/tangency_enum.txt`.
- [ ] **STEP 1 — G(20) verification.** Generalize `code/pattern/tangency_enum.py`
  to accept (c,s,p,q) as arguments and run the (sigma=-1, eta=-1, theta=-1)
  variant over all 22 tuples with s+p+q <= 20 (s>=5, p>=5, p<q). Sum g values
  and check against the oracle G(20)=205. Write per-tuple results to
  `code/out/tangency_G20.txt`. If any tuple disagrees, report which ones.
  **This is the single most urgent task** — one matched value is a coincidence;
  22 independent matches are a method.
- [ ] **STEP 2 — Write the claim.** Add a fenced `claim` block alongside the
  output in `code/out/` documenting: status=checked, holds-here, the exact sign
  convention (sigma=-1, eta=-1, theta=-1), grid resolution (1<<20+1 points),
  both tolerances (COARSE_TOL=1e-4, TIGHT_TOL=1e-9), and anchor it to
  `tangency_enum.txt` (and `tangency_G20.txt` once that exists). Record what the
  residue Q is: Q = sigma*rho*(beta-gamma) - eta*R*beta + theta*r*gamma (mod 1).
  Note the mirror structure: only UU/LL combos survive; UL cross-combos all give
  zero. This claim must appear in research/CLAIMS.md after the next derivation.
- [ ] **STEP 3 — Derive the closed form.** The residue curves dumped in
  `tangency_residue_curves.txt` show Q(d) is monotonic on the valid d-interval.
  The meshing condition Q_p(U) == Q_q(U) mod 1 reduces to finding d where two
  smooth functions cross integer levels. Derive the algebraic equation that
  replaces the 1M-point grid scan — this is the bound-independent method.
- [ ] solution.md: governing theory + efficient method whose cost does not grow
  with 500.
- [ ] code/solution.py: exact arithmetic G(500), agree with brute on all
  reachable cases.
- [ ] Verify G(500) by a second independent route.