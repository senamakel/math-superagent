# G4 continuation: verified obstruction (2026-08-18)

## Restatement and governing theory
For `S_0=0`, `S_1=01`, `S_n=S_{n-1}S_{n-2}`, let `F_k` be the distinct length-k factors and `Psi(k)=sum val(x)^2`. The limit is the characteristic Fibonacci Sturmian word (slope `1/phi^2`), so Sturmian factor complexity gives `|F_k|=k+1`; mechanical floor-difference coding gives the exact decimal-value evaluator. The universal-Euclidean monoid evaluates one geometrically weighted affine floor moment in logarithmic coefficient complexity.

## Executed checks
* `python code/brute.py` (bounded exponential oracle, only k=3,10) produced:
  `F3 ['001', '010', '100', '101']`, `Psi(3) 20302`, `Psi(10) mod 101001001 10699667`, and passed.
  Output: `code/out/brute_oracle_rerun.txt`.
* `python code/g4_joint_diagnostic.py` produced the same anchors, `existing O(k) evaluator vs mechanical k=1..150: PASS`, and contiguous-block reproduction `k=1..40: PASS`. Output: `code/out/g4_joint_diagnostic.rerun.txt`.
* The bivariate diagnostic was rerun through k=20: `code/out/investigate_bivariate_diagonal.rerun.txt`.

## Obstruction
The exact mechanical formulation is
`Psi(k)=sum_m (sum_t c_t floor((t-m)a)-c_m)^2`, with geometric `c_t` and a sparse diagonal correction. Expanding the square creates all pairs `(t,t')`; each pair is a distinct shifted product floor-sum. A universal-Euclidean S2 node handles one such affine floor square, but no verified fixed-dimensional state simultaneously retains the absolute-position decimal weights and the moving truncation boundaries. Re-indexing by `h=t-m` does not decouple them: the weight contributes a residual geometric factor in `m`, while the range is `h in [-m,k-m]`. The attempted h-only diagonal closure is mechanically false; the `[t=m]` boundary term supplies distinct local data on one diagonal. The smallest diagnostic obstruction is visible already at k=3 (and the exact block boundary needs k-1 crossing windows for every concatenation split).

Thus existing evaluators are O(k) (or worse if pair-expanded), not valid for `k=10^18`. No structurally justified polylogarithmic evaluator or target residue was obtained. Reporting a number would be fabrication. The unresolved requirement is a proved fixed-dimensional joint-intercept/boundary aggregation; scaling bounded diagnostics would not settle it, so no larger brute run was attempted.
