# Index — code/scholar

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_offbyone.py` | Scholar-written analysis confirming the recorded off-by-one in the as-is esym_from_diffs helper of code/rootdiff/verify_rootdiff_identity.py: `Poly(prod((x-b)+y),y).nth(k)` returns e_{n-k} (coefficient of y^k in sum_k e_{n-k} y^k), so checking against n-i gives e_i not e_{n-i}. Verifies that asis(n-i) == e_i and that corr(n-i) == H_i for n=3,4,5. Analytically confirmed by hand; runner provided for an executor. |
| `descent_check.py` | Verifies the Graf-von-Bothmer coefficient-descent hypothesis: (d choose i) ≡ 0 mod p for all 1<=i<=d-1 at d=p^k (Prop 2.5), and confirms the witness-degree pivot (p+1 choose p) ≡ 1 mod p fails to vanish so x^{p+1}-x^p survives. Written for the executor; not yet run. |
| `run_check_offbyone.py` | Launcher for code/scholar/check_offbyone.py (subprocess wrapper). Not run yet (no code-execution role in this scholar pass). |
| `run_descent.py` | Launcher for code/scholar/descent_check.py (subprocess wrapper) so an executor can run the descent check and capture output. Minimal; not run yet. |
