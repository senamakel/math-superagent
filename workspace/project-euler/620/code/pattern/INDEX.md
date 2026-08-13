# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `G_sequence.py` | _(undescribed)_ |
| `Qcurves.py` | _(undescribed)_ |
| `aggregate.py` | _(undescribed)_ |
| `boundary_robustness.py` | _(undescribed)_ |
| `closedform.py` | _(undescribed)_ |
| `closedform_check.py` | _(undescribed)_ |
| `closedform_probe.py` | _(undescribed)_ |
| `count_formula_test.py` | _(undescribed)_ |
| `count_formula_test2.py` | _(undescribed)_ |
| `diag.py` | _(undescribed)_ |
| `discrepancy17.py` | _(undescribed)_ |
| `discrete_model_probe.py` | Earlier single-centre least-mesh-angle lattice model (slots k*2pi/(s+c) about O or S). DEAD — returned 0 vs 9/9/205; the off-centre geometry has no such lattice. |
| `endpoint.py` | _(undescribed)_ |
| `endpoint2.py` | _(undescribed)_ |
| `fast_g.py` | _(undescribed)_ |
| `identity_debug.py` | _(undescribed)_ |
| `independent_verify.py` | _(undescribed)_ |
| `levels.py` | _(undescribed)_ |
| `margin.py` | _(undescribed)_ |
| `mpmath_table.py` | _(undescribed)_ |
| `n_integer_count.py` | _(undescribed)_ |
| `phase_grid.py` | Clean re-derivation of the tooth-mesh phase E_m=R*beta - r*gamma - rho*psi and a fine-grid (400k-point) count of valid d. No output on disk yet. |
| `phase_model_probe.py` | Idler-phase model probe: discreteness comes from roots of phase congruences in d (no position lattice); eps=+-1 residual scan. As of this run the test driver is `phase_model_probe.py` parity; the W-invariant model supersedes it. |
| `scholar_verify.py` | Scholar's independent re-verification of the adopted n_t model: mpmath-60 identity check n_p+n_q=c+s at arbitrary d, g(16,5,5,6) and all 22 G(20) values via the endpoint formula, G(16)/G(20) sums, and a grid-resolution diagnostic of the (16,5,5,6) region scan across 2^17..2^22 to retire the on-disk 6-vs-9-vs-0 contradiction. NOT YET RUN (no execution tool in scholar role). |
| `seqgen.py` | _(undescribed)_ |
| `structcheck.py` | _(undescribed)_ |
| `structural_test.py` | _(undescribed)_ |
| `tangency_enum.py` | _(undescribed)_ |
| `w_invariant_test.py` | Numerically tests the off-centre W-invariant meshing model of PE620 (thread research/threads/offcentre-mesh-phase-model.md) on four condition sets A/B/C/D at mpmath 40 dps: float64 scan of the d interval plus endpoint probes locate near-integer anchors of the six congruence numerators, each refined by exact mpmath bisection; a d is valid for a set iff every condition residue <1e-9. Prints valid-d counts and d values and a one-line verdict. Result: none of A/B/C/D reproduces 9/9/205 — g(16,5,5,6) A=0, B=5, C=0, D=0; C is NOT identically satisfied. Correctness established by flagship N=1e7, grid convergence (B=5 at 1e6/4e6/12e6), and an independent cluster-vs-root coverage check; output code/out/w_invariant_test.txt, note code/out/w_invariant_test.md. |
| `winner_refine.py` | _(undescribed)_ |
