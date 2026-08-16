# Index — code/elimination

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `guard_check.py` | Guard set for the S_n elimination machinery: canonical oracle on pure powers, generic random f, char-p witnesses, plus S_n pure-power-locus substitution. Exit 0 iff all pass. Successor of deleted code/casasalvero/guard_check.py (which imported a nonexistent charp_witness and was broken). |
| `test_singular_path.py` | Validates the Singular bridge of lib.casasalvero: _to_singular round-trip (regex parse-back) and Rabinowitsch membership agreement between sympy and Singular engines. Exit 0 iff all pass. Successor of deleted code/casasalvero/test_singular_path.py (whose naive parse-back mangled _to_singular output). |
