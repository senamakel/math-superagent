# Index — code/pattern_hunt

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_lmin.py` | Early probe: compares Lmin to floor(phi^2 k) and A344953 terms; superseded by verify_lmin_formula.py (kept as the refutation record). |
| `gen_sequences.py` | Generate PE1006 integer sequences: Psi(k) exact (1..25), Psi(k) mod 101001001 (1..400), Lmin(k) minimal prefix length (1..400); count/stability self-checks, bit-mask factor extraction. Writes code/out/psi_residues.txt, psi_exact.txt, lmin.txt, counts.txt. |
| `verify_lmin_formula.py` | Check Lmin(k) = k + NextFib(k) - 1 for k=1..2583 with 6765-char prefix, all Fibonacci-boundary checks, matches hardcoded A344953 terms; also refutes Lmin = floor(k phi^2) (992 fails). Writes nothing; prints report. |
