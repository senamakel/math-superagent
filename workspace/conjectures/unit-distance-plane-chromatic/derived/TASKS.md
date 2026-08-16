# Tasks

## Verified (completed, machine-checked)

- [x] Calibrate the unit-distance graph oracle pair on the Moser spindle
      (exact 11-edge certifier + complete k-colouring test): chi = 4 PASSED,
      k=4 SAT witness [0,1,2,0,1,2,3], k=3 UNSAT. Artifacts in
      code/lib/unitgraph.py, code/lib/coloring.py, code/calibrate_moser.py,
      verified independently in code/verify_calibration_independent.py.
- [x] Forced-pair attack (G-forced-pair-exists, the crux of the spindle lower
      bound): Moser spindle (all 10 qualifying non-edge pairs, k=4) and
      Moser+Moser Minkowski sum (26v, 69e, all 256 qualifying pairs, k=4)
      have NO monochromatic-forced pair. Diamond k=3 base case confirmed
      (tips forced equal). code/out/forced_pair.captured.txt. The spindle
      route needs a richer base graph; dead for these two.
- [x] Size-bound census through N=11: every graph on <= 11 vertices with
      min-deg>=4, K4-free, K2,3-free, nbhd-maxdeg<=2 is 4-colourable. Complete
      enumeration over all 28 residue classes (187,095,840 graphs), 228
      members at n=11 (n=8:1, n=9:4, n=10:16, n=11:228, total 249), all
      4-colourable by Cadical SAT AND independent DSATUR (0 fails). So every
      unit-distance graph on <= 11 vertices is 4-colourable; every
      5-chromatic unit-distance graph has >= 12 vertices.
      code/out/census_kernel_n11_run.captured.txt, ..._test.captured.txt,
      code/out/census-kernel-n11-result.md.
- [x] Kill the Mycielski kernel refutation: the shipped refute_mycielski_kernel.py
      is BROKEN (wrong mirror edges). Correct Mycielski^2(C5) = 23v/71e/chi=5/
      triangle-free/min-deg-4, but its 5-critical core FAILS K2,3-freeness
      (vertices 0,2 share common neighbours 1,6,12). So sharp-kernel-4color is
      NOT refuted; "triangle-free => K2,3-free" is false. The N=11 size bound
      stands. code/out/refute_kernel_verify.md, diag_mycielski.captured.txt,
      verdict_mycielski_core.captured.txt.
- [x] Alon-Tarsi direction refuted (EE!=EO certifies 4-COLORABILITY, not
      non-colourability — direction backwards). Hajos generative grammar
      refuted (join/Hajos not UDP-preserving; realizability oracle
      EXISTENTIAL-R-complete). research/approaches/.
- [x] Close the Mycielski unit-distance realizability question:  M^k(C5) for
      k>=2 is NOT unit-distance realizable, as a direct consequence of the
      K2,3-freeness lemma (sharp_nbhd_cert), independent of any colouring
      oracle.  Built M^0..M^4 with the correct textbook no-mirror Mycielskian
      (3|E|+n; M^2=23v/71e matches verdict; Groetzsch 11v/20e), verified
      M^2,M^3,M^4 each contain an explicit K2,3 on vertices (0,2,{1,6,12,17}),
      robust to construction choice (mirror variant also fails).  So the
      Mycielski kernel cannot supply the run's needed rigid-4-chromatic UDG;
      the family dies to the K2,3-free NECESSARY condition at k>=2.
      code/verify_mycielski_k23_udg.py + _indep.py + _both_variants.py,
      code/out/verify_mycielski_k23_udg.captured.txt.

## In flight

- [ ] Flat-torus periodic upper-bound sub-problem (inventor-adopted): the
      separation graph F(basis, rho, n) on the torus R^2/Lambda; calibration
      is re-deriving the A2 hexagon 7-colouring exactly (same-colour centre
      distance sqrt21*L, window 1/(sqrt21-2) < L < 1/2); then sweep a family
      of sublattices at k=6 for a periodic 6-colouring (would settle chi<=6)
      or accumulate a periodic-impossibility census.
      [x] CALIBRATION EXECUTED, code/out/torus_margin.captured.txt: A2 margin
      re-derived exactly (same-colour centre factor = sqrt21 ~ 4.5826, window
      0.3872 < L < 1/2), chi(F(A2,L)) = 7 in-window machine-verified (6-col
      UNSAT, 7-col SAT on index-7 quotient, K7); independent cross-check
      factor==sqrt21. Sweep census: 30 sublattices (D=7,13), 24 six-colourable
      (sparse), 6 needing 7 (the D=13 rows (1,2),(2,1),(3,-2),(3,-1),(3,1),
      (3,2)). Periodic-6 search NOT closed — census only; no periodic 6-colouring
      found beating 7, but also no impossibility. Forward move: push D (index)
      for sublattices dense enough to be 6-chromatic; a truly dense 6-chromatic
      quotient subgraph would be the target, else accumulate the impossibility
      census. The open forward move is the dense-quotient sweep, not the A2
      calibration (that is done and exact).

## Executed this run

- [x] Hoffman spectral chi-lower-bound on the constructible family (adopted
      lovasz-theta/vector-chromatic approach, first time run; answers the
      REQUESTS value row). Calibrated on C5 (=sqrt5) and Moser (float eig
      matches exact char-poly eigvals). Values: Moser 2.712176, Moser+Moser
      2.864308, diamond 2.640388, triangular disk R=3 2.994973. Max 2.995:
      the Hoffman/spectral relaxation cannot certify chi>=5 on these graphs —
      a precise negative datum that retires the spectral route as a 5-certifier
      over the constructible family (kept only as a cheap progress metric).
      Artifacts: code/hoffman_bounds.py, code/out/hoffman_bounds.captured.txt.

## Dead ends recorded (see research/ and CONTEXT.md)

- Spindle forced-pair route: dead for Moser + Moser+Moser.
- Hajos grammar, Alon-Tarsi: refuted at source.
- Minkowski two-triangle sum: T+T = triangular prism, chi=3 (textbook), dead.

## Stated goal / deliverable

Shift one of 4 <= chi <= 7, with a machine-verified artifact, OR a precise
account of what blocks the pursued route. Working assumption: the N=11 size
bound (every 5-chromatic UDG has >= 12 vertices) is the strongest verified
partial result so far; extending toward N=12+ or a periodic 6-colouring are
the open forward moves.
