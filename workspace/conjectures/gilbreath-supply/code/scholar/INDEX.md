# Index — code/scholar

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `__init__.py` | _(undescribed)_ |
| `_focus_main.py` | Throwaway subprocess launcher for threshold_focus.py; matches the directive-30 underscore-deletion pattern and may be deleted. |
| `_probe_import.py` | Throwaway lib-import probe for the scholar pass; matches the underscore-deletion pattern and may be deleted. |
| `_run_threshold_focus.py` | Throwaway subprocess launcher for threshold_focus.py; matches the underscore-deletion pattern and may be deleted. |
| `_scratch_note.txt` | _(undescribed)_ |
| `capture_threshold_exact_mean.py` | Temp-file-then-move capture runner for the above; writes code/out/scholar_threshold_exact_mean.captured.txt on exit 0. |
| `cell_degree_check.py` | Checks fold cell degree is 2^popcount(d) (correction to O'Donnell digest). |
| `downset_verify.py` | _(undescribed)_ |
| `lacasa_parity_projection_check.py` | _(undescribed)_ |
| `lacasa_projection_check.py` | _(undescribed)_ |
| `mr_gap_correlation_probe.py` | Prior-pass gap-correlation probe. |
| `projection_erasure_check.py` | _(undescribed)_ |
| `run_threshold_verify.py` | Runs all three third-pass threshold verification scripts (threshold_limit_run, threshold_exact_mean_independent, threshold_verify_tail) and captures output. Hand to tool_builder to regenerate/confirm the exact-mean and fraction columns. |
| `threshold_exact_mean.py` | EXACT mean of nu2/n over all weight-w strings via the closed-form parity probability P_d(w) = (C(n,w) − [z^w](1−z)^{2^pc}(1+z)^{n−2^pc}) / (2 C(n,w)); decides the mean half of the 'typical' test without sampling. Handed to tool_builder. |
| `threshold_focus.py` | Focused, cheap discrimination of the plateau question: exact-mean crossing at 64/128/256 plus brute-fraction at past-plateau points, small enough to run fast. Not run in this scholar pass. |
| `threshold_handcheck.md` | Independent hand-arithmetic verification of the exact-mean threshold formula logic (n=8, w=1 gives mean 0.375), matching the capture and exhaustive enumeration; records that the environment cannot execute programs, so the pass's mechanical verification rests on tool_builder's independent code path. |
| `threshold_limit_run.py` | Third-pass limit question: exact mean over all weight-w strings grouped by popcount (part A) + sampled fraction half at n=256,512 (part B). Cross-checked against exhaustive s_sos on small (n,w). |
| `threshold_verify_tail.py` | Independent tail check of the exact-mean threshold: recomputes the crossing and brute-samples the fraction below the would-be 0.125 plateau, to confirm the pass-2 readings were a sampling artifact. Not run in this scholar pass (no execution tool); offered to tool_builder. |
| `verify_intersection_formula.py` | _(undescribed)_ |
| `verify_sphere_mean_formula.py` | Independent brute-force verification of the exact-mean Krawtchouk/parity formula behind the pass-3 threshold result (claim sphere-mean-krawtchouk-exact / threshold-mean-exact-parity-formula): checks formula_mean(n,w) = sum_d (C(n,w)-K_w(2^popcount(d);n))/(2 C(n,w)) against exhaustive weight-w enumeration for n=3..12, all w. Hand-reproduced at the n=4,w=1 anchor (E=3/2). |
| `verify_threshold_column.py` | Redirect stub: the independent threshold verification it once intended is recorded as prose in threshold_handcheck.md; no program is run here. |
