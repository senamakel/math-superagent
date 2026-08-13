# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `G20_overcount.md` | _(undescribed)_ |
| `G_sequence.txt` | _(undescribed)_ |
| `README.md` | _(undescribed)_ |
| `closedform_probe.txt` | _(undescribed)_ |
| `count_formula_test.txt` | _(undescribed)_ |
| `count_formula_test2.txt` | _(undescribed)_ |
| `fast_g_G20.txt` | Full per-tuple strict f-crossing table for all 22 G(20) tuples (mpmath-60): g_int (eps-strict integer-level count, sum 213), g_half (half-integer-level count, sum 205), g_fast.py own counts, g_grid, and every crossing root's n_p/n_q, residues, y_p/y_q, endpoint distance, and V/H/E/D flags; ends with the grid-stability re-scan of the 8 differing tuples at 4x density. Produced by code/pattern/fast_g_per_tuple.py. |
| `fast_g_G20_note.md` | Claim note (status: checked): fast_g.py as-is returns G(20)=213 vs oracle 205, overcount exactly 8; the 8 extra roots are the f-INTEGER crossings of p-q-odd tuples (n_p = 0.5, smallest d, non-degenerate, nearest lower endpoint), which violate the model's own parity admissibility n_p - n_q = p-q (mod 2). The parity-corrected count g = #{m : f(DL)<m<f(DU), 2m=p-q mod 2} reproduces 9/9/205 exactly. |
| `fast_g_as_is.txt` | Raw output of `python code/pattern/fast_g.py` run exactly as-is this run: G(16)=9 AGREE, G(20)=213 DISAGREE (overcount 8) with its 22 per-tuple values. |
| `lattice_test.txt` | _(undescribed)_ |
| `levels.txt` | _(undescribed)_ |
| `mpmath_table.txt` | _(undescribed)_ |
| `n_integer_model.txt` | _(undescribed)_ |
| `n_integer_model_rerun.txt` | Fresh run of code/pattern/n_integer_count.py (1,048,577-pt grid, tol 1e-3, degenerate-excluded): g(16,5,5,6)=9, G(16)=9, G(20)=205, all 22 tuples listed. Establishes the on-disk 205 split is reproduced by the current code, not stale output. |
| `n_integer_parity_test.md` | _(undescribed)_ |
| `n_integer_parity_test.txt` | _(undescribed)_ |
| `oracle-model-broken.md` | Concurrent agent's note (status: checked) independently confirming g(16,5,5,6)=0 from the same lib/gears.py model, with the same diagnosis (residual minimum only at the degenerate endpoint d=1/(2pi)) and the consequence that no trustworthy integer sequence exists until the discrete least-mesh-angle model is implemented. |
| `oracle_test.md` | Claim note (status: checked) recording that the continuous-d phase-elimination meshing model in lib/gears.py fails all three PE620 oracle values; diagnosis (residual O(1) except at the degenerate lower endpoint of the d interval), why the failure is not a resolution artifact, and why the least-mesh-angle lattice model remains the plausible next route. |
| `oracle_test.txt` | _(undescribed)_ |
| `phase_model_test.txt` | _(undescribed)_ |
| `seq_C.txt` | _(undescribed)_ |
| `seq_G.txt` | _(undescribed)_ |
| `tangency_G20.txt` | _(undescribed)_ |
| `tangency_enum.txt` | _(undescribed)_ |
| `tangency_enum_claim.md` | _(undescribed)_ |
| `tangency_residue_curves.txt` | _(undescribed)_ |
| `w_invariant_test.md` | Result note (status: checked) for the W-invariant model test. Documents the four condition sets A/B/C/D, the method (fixed O(N) scan + mpmath bisection, independent coverage check), the g(16,5,5,6) counts (A=0, B=5, C=0, D=0), the convergence evidence at N=1e6/4e6/12e6, the falsification of C's "identically satisfied" hypothesis, and the verdict that no set reproduces 9/9/205. Companion to code/out/w_invariant_test.txt. |
| `w_invariant_test.txt` | _(undescribed)_ |
| `winner_refine.txt` | _(undescribed)_ |
