# Index — code/scholar

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_offbyone.py` | Scholar-written analysis confirming the recorded off-by-one in the as-is esym_from_diffs helper of code/rootdiff/verify_rootdiff_identity.py: `Poly(prod((x-b)+y),y).nth(k)` returns e_{n-k} (coefficient of y^k in sum_k e_{n-k} y^k), so checking against n-i gives e_i not e_{n-i}. Verifies that asis(n-i) == e_i and that corr(n-i) == H_i for n=3,4,5. Analytically confirmed by hand; runner provided for an executor. |
| `descent_check.py` | Verifies the Graf-von-Bothmer coefficient-descent hypothesis: (d choose i) ≡ 0 mod p for all 1<=i<=d-1 at d=p^k (Prop 2.5), and confirms the witness-degree pivot (p+1 choose p) ≡ 1 mod p fails to vanish so x^{p+1}-x^p survives. Written for the executor; not yet run. |
| `run_check_offbyone.py` | Launcher for code/scholar/check_offbyone.py (subprocess wrapper). Not run yet (no code-execution role in this scholar pass). |
| `run_descent.py` | Launcher for code/scholar/descent_check.py (subprocess wrapper) so an executor can run the descent check and capture output. Minimal; not run yet. |
| `verify_defrutos_discriminants.py` | Exact sympy recomputation of the de Frutos Marin thesis degree-5 discriminants: delta(5,{1,2,3})=Res(R,N1) with the explicit R,N1 polynomials, and Delta(5,{2,3}) via Teo 5.6.8; checks the factorisations 2^24·3^6·7^3·131·193·599^2·8009 and 2^2·3^2·11·3541, and that D_5's prime divisors equal the published degree-5 bad list. Turns defrutos claims from asserted to checked. NOT yet executed (reserved for a coding role with the execution tool). |
| `verify_deg6_witness.py` | Runs the canonical oracle (lib.casas_alvero.is_ca_hasse/is_pure_power) on the Graf von Bothmer 2007 degree-6 explicit char-p witness quadrinomial over F_7390044713023799 to upgrade claim deg6-explicit-witness-gvb from asserted to checked. Includes guard set. Awaits a code-exec role. |
| `verify_monomial_structure.py` | Queued symbolic-verification script for the resultant-monomials structure: computes R_i=Res_x(f,H_i(f)) over Z[a_1..a_{d-1}] via Hasse derivatives for d=3,4 and checks the (A) unique-pure-power and (B) unique-minimal-degree monomial claims; not yet run (runner's job). |
