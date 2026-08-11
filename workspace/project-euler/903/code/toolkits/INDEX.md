# Index — code/toolkits

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `f_literal.py` | Independent oracle for the F(d) table: literal per-i power-orbit computation of F_i = sum over pi of rank(pi^i), grouped by gcd(i, n!), asserting F_i is constant on each class; returns {g: F(g)}. Cross-checks toolkits/f_table.py in fdtable.py for n=4,5,6. Function: f_by_gcd(n) |
| `f_table.py` | Computes the F(d) table for Q(n) = sum over d dividing n! of phi(n!/d)*F(d): F(d) = sum over pi of rank(pi^d) via cycle decomposition (d-th power read off cycles). Cross-validated against toolkits/f_literal.py for n=4,5,6. Function: f_table(n) |
