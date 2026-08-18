# New exact recurrence hunt

Method: `python code/pattern_hunt/analyze_exact_new.py` parses stored integer columns and tests exact rational homogeneous linear recurrences of orders 1..12, plus Berlekamp–Massey over M=101001001 and small moduli. `targeted_relations.py` independently checks selected proposed identities.

## Outputs

- `psi_exact.txt` (25 terms): no exact homogeneous recurrence of order <=12. BM over M has linear complexity 13 on this finite prefix; coefficients begin `[1, 58842762, 25250129, ...]`. This is not a global recurrence.
- `psi_residues.txt` (400 terms): no exact recurrence order <=12 after interpreting its second column as the residue. BM over M has complexity 200, so no low-order relation survives the supplied terms.
- `c1_terms.txt` (400 terms): no ordinary constant-coefficient exact recurrence order <=12. Its exact established relation remains `c1(k)=1+floor(k/phi^2)` on the stored range; first differences printed by the independent check are `0,1,0,0,1,0,1,0,0,1,...`.
- `dj_raw.txt` (1145 two-column rows): using the second column, no exact recurrence order <=12; values are not a simple Fibonacci additive sequence (first bad proposed check at index 3: `d_3=3`, while `d_1+d_2=2`).
- `ext_recurrence.txt` and `extrecur_res.txt`: no exact recurrence order <=12 under their final numeric columns. The final column of `ext_recurrence.txt` starts `0,10,110,110,20210,...`; no new stronger relation was found.
- `lmin.txt`: no constant-coefficient recurrence order <=12; the stored exact formula `k+NextFib_strict(k)-1` is the stronger structural description.

## Targeted falsifiers

`python code/pattern_hunt/targeted_relations.py` output:

```text
psi_exact.txt psi mod100==c1: None
psi_exact.txt psi mod1000==c1: None
psi_residues.txt psi mod100==c1: (2, 101)
psi_residues.txt psi mod1000==c1: (2, 101)
c1 first differences first 20: [0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0]
dj length 1145 values [1, 2, 3, 5, 8, 9, 10, 11, 13, 15, 16, 19, 20, 21, 23, 25, 27, 30, 33, 34] max 1127
dj adjacent Fibonacci recurrence first bad: (3, 3)
```

The `psi_exact` modulo checks are vacuous for `k>1` because the exact parser was intentionally reading the sole column, not the residue table; the meaningful 400-term residue check is the `psi_residues` line, whose first falsifier is `k=2` for both mod 100 and mod 1000.

No new recurrence strong enough to matter was found. The finite regularities that survive remain the already-established floor/Fibonacci-block formulas and the right-extension recurrence; the new exact search did not strengthen them.