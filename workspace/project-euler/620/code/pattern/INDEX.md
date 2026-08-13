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
| `fast_g.py` | The f-crossing meshing model: Q_t = (c-t)*B + (s+t)*G turns, f = Q_p - Q_q strictly increasing on (DL,DU), g = #{m in Z : f(DL) < m < f(DU)}, each m crossed once, exact bisection at mpmath-60. Run as-is this run: G(16)=9 AGREE, G(20)=213 vs oracle 205 (overcount 8). Do NOT use the plain integer-level form for G(500): the 8 extra roots are f-integer crossings of p-q-odd tuples violating the model's own parity rule (see code/out/fast_g_G20_note.md; the parity-corrected count g = #{m : f(DL)<m<f(DU), 2m=p-q mod 2} reproduces 205). |
| `fast_g_per_tuple.py` | Per-tuple strict f-crossing analysis of all 22 G(20) tuples (mpmath-60). For each tuple prints DL/DU, c+s and p-q parity, the eps-shifted interval endpoints f(DL+1e-9), f(DU-1e-9), the integer level range, and for every crossing root m: root d (bisection), n_p=2Q_p, n_q=2Q_q (identity n_t=2Q_t), residues mod 1, residual n_p-n_q-2m (exact 0 to 60 digits), tangency ordinates y_p,y_q, signed distances to DL/DU, and V/H/E/D flags (n-model valid / half-integer n_p / near endpoint <1e-6 / degenerate <1e-6). Then per tuple g_int vs g_half vs g_fast.py's count vs g_grid (n_integer_count.valid_ds), extra-root analysis, and a 4x-density stability re-scan of differing tuples. Command: python code/pattern/fast_g_per_tuple.py; output code/out/fast_g_G20.txt. Correctness established: g_int reproduces fast_g.py's own counts on all 22 tuples (213 total, matching the run-as-is program), g_grid reproduces the n_integer scan (205), identity n_p+n_q=c+s verified at random d, residual n_p-n_q-2m ≡ 0 at every root, and the 8 differing tuples are stable at 4x grid density/tol 1e-4. |
| `identity_debug.py` | _(undescribed)_ |
| `independent_verify.py` | _(undescribed)_ |
| `levels.py` | _(undescribed)_ |
| `margin.py` | _(undescribed)_ |
| `mpmath_table.py` | _(undescribed)_ |
| `n_integer_count.py` | Grid-scan PE620 meshing model n_t(d) = [(c-t)*beta + (s+t)*mu]/pi with n_p,n_q in Z and cross-parity n_p - n_q == p-q (mod 2), degenerate endpoints excluded; one arrangement per valid d. Reproduces g(16,5,5,6)=9, G(16)=9, G(20)=205 on a 1,048,577-pt grid (tol 1e-3), refreshed this run (code/out/n_integer_model_rerun.txt) and stability-rechecked at 4x density / tol 1e-4 (code/out/fast_g_G20.txt). This is the only on-disk per-tuple split reproducing 205. |
| `n_integer_noparity.py` | Parity-filter test of the PE620 n_t integer meshing model: reruns all 22 G(20) tuples (plus g(16,5,5,6) detail) with and without the n_p-n_q == p-q (mod 2) filter, side by side, prints totals, changed-tuple list vs the c+s-odd set, and min/max of n_p+n_q over all valid d. Reuses n_arrays/valid_ds logic via valid_ds(..., use_parity=...) and n_integer_noparity.g20_tuples. Output code/out/n_integer_parity_test.txt. Established correct: reproduces n_integer_count.py's exact per-tuple values when use_parity=True (all 22, G(20)=205), and the 205 no-parity solutions all satisfy the parity condition (0 rejections). |
| `phase_grid.py` | Clean re-derivation of the tooth-mesh phase E_m=R*beta - r*gamma - rho*psi and a fine-grid (400k-point) count of valid d. No output on disk yet. |
| `phase_model_probe.py` | Idler-phase model probe: discreteness comes from roots of phase congruences in d (no position lattice); eps=+-1 residual scan. As of this run the test driver is `phase_model_probe.py` parity; the W-invariant model supersedes it. |
| `scholar_verify.py` | Scholar's independent re-verification of the adopted n_t model: mpmath-60 identity check n_p+n_q=c+s at arbitrary d, g(16,5,5,6) and all 22 G(20) values via the endpoint formula, G(16)/G(20) sums, and a grid-resolution diagnostic of the (16,5,5,6) region scan across 2^17..2^22 to retire the on-disk 6-vs-9-vs-0 contradiction. NOT YET RUN (no execution tool in scholar role). |
| `seqgen.py` | _(undescribed)_ |
| `sign_scan.py` | _(undescribed)_ |
| `structcheck.py` | _(undescribed)_ |
| `structural_test.py` | _(undescribed)_ |
| `tangency_G20.py` | PE620 tangency enumeration over all 22 G(20) tuples, restricted to the winning sign variant (sigma,eta,theta)=(-1,-1,-1). Same machinery as tangency_enum.py: residue Q = -rho*(beta-gamma)+R*beta-r*gamma mod 1; side combos pp,qq in {UU,LL,UL}; objective = max pairwise circular distance; coarse grid N=2^20+1; runs clustered with COARSE_TOL=1e-4; 3-zoom mpmath refine dps=60, accept objective<1e-9; g = distinct refined valid d over 9 combos. For the oracle tuple (16,5,5,6) also reconciles tangency d's against the n-integer model (n_t=[(c-t)beta+(s+t)gamma]/pi in Z, mpmath bisection roots) printing side-by-side d values and cross-integers. Methods validated against the g(16,5,5,6)=9 claim; aim: total over 22 tuples vs oracle 205. |
| `tangency_enum.py` | _(undescribed)_ |
| `w_invariant_test.py` | Numerically tests the off-centre W-invariant meshing model of PE620 (thread research/threads/offcentre-mesh-phase-model.md) on four condition sets A/B/C/D at mpmath 40 dps: float64 scan of the d interval plus endpoint probes locate near-integer anchors of the six congruence numerators, each refined by exact mpmath bisection; a d is valid for a set iff every condition residue <1e-9. Prints valid-d counts and d values and a one-line verdict. Result: none of A/B/C/D reproduces 9/9/205 — g(16,5,5,6) A=0, B=5, C=0, D=0; C is NOT identically satisfied. Correctness established by flagship N=1e7, grid convergence (B=5 at 1e6/4e6/12e6), and an independent cluster-vs-root coverage check; output code/out/w_invariant_test.txt, note code/out/w_invariant_test.md. |
| `winner_refine.py` | _(undescribed)_ |
