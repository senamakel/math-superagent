# Final exact sequence inspection (2026-08-18)

## Scope and method

Inspected all stored integer sequence artifacts relevant to the request: `psi_exact.txt`, `psi_residues.txt`, `c1_terms.txt`, `lmin.txt`, `dj_raw.txt`, `topelitz_defects.txt`, `vr_rungaps.txt`, and the run-related tables. The governing diagnostic was exact rational homogeneous linear-recurrence fitting for orders 1 through 12, with modular Berlekamp--Massey only as a secondary finite diagnostic. No published-answer search was used.

The sequence analyzer was run with:

```sh
python code/pattern_hunt/analyze_exact_new.py
python code/pattern_hunt/analyze_existing_sequences.py
python code/pattern_hunt/check_toeplitz_defect.py
python code/pattern_hunt/check_dj_structure.py
python code/pattern_hunt/check_R_runs.py
```

A separate exact fitting run rechecked every candidate and printed the first falsifier for any surviving fitted recurrence. It found no recurrence of order <=12, so there were no fitted conjectures to extend.

## Exact outputs

- `psi_exact.txt`: 25 terms; no exact homogeneous recurrence of order <=12. BM modulo `101001001` has order 13, only a finite modular diagnostic.
- `psi_residues.txt`: 400 terms; no exact homogeneous recurrence of order <=12. BM modulo `101001001` has order 200.
- `c1_terms.txt`: 400 terms; no exact homogeneous recurrence of order <=12. The established exact formula `c1(k)=1+floor(k(3-sqrt(5))/2)` survives all 400 terms; no falsifier.
- `lmin.txt`: 400 terms; no exact homogeneous recurrence of order <=12. The established exact formula `Lmin(k)=k+NextFib_strict(k)-1` survives all 400 terms; no falsifier (other workspace artifacts extend this check further).
- `dj_raw.txt`: 1145 terms; no exact homogeneous recurrence of order <=12. No new closed form survived inspection.
- `topelitz_defects.txt`: 400 terms; no exact homogeneous recurrence of order <=12. Its zero indices are exactly
  `[1,2,4,7,12,20,33,54,88,143,232,376]`, matching `F_n-1` in the workspace indexing through 400. The universal-zero conjecture is falsified at `k=3`, defect `2`; the first non-Fibonacci-boundary zero after `k=2` is `k=4`.
- `vr_rungaps.txt`: stored gaps are exactly 2 or 3 over the supplied range; this is consistent with the already recorded Wythoff/Sturmian run-start pattern, not a new recurrence.
- Run starts: exact stored check gives `s_j=floor(j*phi^2)` through `j=1146`; no falsifier. This is a finite verification of an already identified structural pattern.

## Decision

**NOTHING FURTHER.** No meaningful new recurrence or closed form survived exact fitting. The only surviving patterns are already structural findings in the workspace (`c1`, `Lmin`, and the finite Fibonacci-boundary Toeplitz-zero pattern). Extending the same scans would only add bounded evidence and would not resolve the missing fixed-dimensional reduction for `Psi(10^18)`; therefore no larger run was made.
