# Agent sequence audit

## Scope

I read the stored artifacts and ran the requested exact sequence audit on the final numeric column of:

- `code/out/psi_exact.txt` (25 terms)
- `code/out/psi_residues.txt` (400)
- `code/out/c1_terms.txt` (400)
- `code/out/lmin.txt` (400)
- `code/out/dj_raw.txt` (1145)
- `code/out/topelitz_defects.txt` (400)

The audit is `code/pattern_hunt/sequence_audit_requested.py`; its rational recurrence fitter is the local exact equivalent of the requested `find_linear_recurrence` diagnostic, and the prefix/difference/formula diagnostics are the `analyze_sequence` portion. It does not enumerate PE1006 candidates at the target bound.

## Command and exact output

```sh
python code/pattern_hunt/sequence_audit_requested.py | tee code/out/pattern_hunt/sequence_audit_requested.out
```

The command exited 0. Key output was:

```text
psi_exact: n=25 prefix=[1, 101, 20302, 2042402, 204252402, 30445654403, 3054587854503, 407470828064704, 40849095449084804, 4085011557551094804]
  rational_recurrence<=12= None
psi_residues: n=400 prefix=[1, 101, 20302, 2042402, 2250400, 44353102, 14581260, 65706380, 21161323, 10699667]
  rational_recurrence<=12= None
c1: n=400 prefix=[1, 1, 2, 2, 2, 3, 3, 4, 4, 4]
  rational_recurrence<=12= None
  c1_formula_first_bad= None
lmin: n=400 prefix=[2, 4, 7, 8, 12, 13, 14, 20, 21, 22]
  rational_recurrence<=12= None
  lmin_formula_first_bad= None
dj: n=1145 prefix=[1, 1, 3, 2, 1, 5, 3, 8, 5, 2]
  rational_recurrence<=12= None
  dj_fib_additive_first_bad= (3, 3)
toeplitz_defects: n=400 prefix=[0, 0, 2, 0, 2, 8, 0, 18, 10, 16]
  rational_recurrence<=12= None
  zero_indices= [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]
  universal_zero_first_bad= (3, 2)
```

## Findings

- **No new low-order linear recurrence:** no sequence has an exact homogeneous rational constant-coefficient recurrence of order 1–12 on all supplied terms. This agrees with, but does not improve, the earlier modular BM reports. The finite `psi_exact` sample is especially too short to support extrapolation.
- **Surviving `c1` law:** `c1(k)=1+floor(k(3-sqrt(5))/2)` survives all 400 stored terms; no falsifier in the supplied range. This is already recorded, not new.
- **Surviving `lmin` law:** `lmin(k)=k+NextFib_strict(k)-1` survives all 400 terms; no falsifier. This is already recorded and has separately been checked farther in the workspace.
- **Toeplitz defects:** exact zero indices through 400 are
  `[1,2,4,7,12,20,33,54,88,143,232,376]`, the recorded Fibonacci-boundary pattern. The tempting universal-zero claim is first falsified at `k=3`, where the defect is exactly `2`; the first later zero is `k=4`.
- **`dj`:** no recurrence through order 12. The tempting Fibonacci-additive rule fails immediately at index 3: `d_3=3`, but `d_1+d_2=1+1=2`.

## Conclusion

No pattern beyond the recorded findings survived this audit. In particular, these sequence tools do not provide the missing fixed-dimensional reduction needed for `Psi(10^18)`. The exact structural regularities remain the `c1` floor law, the strict-next-Fibonacci `lmin` law, and the Fibonacci-boundary zero set for Toeplitz defects; none yields the requested target by itself.
