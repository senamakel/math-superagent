# Index — code/genus

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `diag_families.sing` | _(undescribed)_ |
| `extend3_4.sing` | Extends k2=3,4,5 to k1=24, confirming the closed forms. |
| `extend_falsifiers.sing` | _(undescribed)_ |
| `extend_k2_6.sing` | _(undescribed)_ |
| `extend_rows_6_8.sing` | _(undescribed)_ |
| `extend_rows_7_10.sing` | _(undescribed)_ |
| `falsify_genus_formula.py` | Out-of-sample falsification of the unified genus formula g(m,n) = ((m-1)(n-1)+1-gcd(m,n))/2 for the projective closure of C(x,m)=C(y,n): predicts g for 17 never-computed pairs (new columns m=13..16, rows 2,3,5,10 past their last n, large-gcd residues), computes them freshly with Singular normal.lib::genus, and compares. Parser is an anchored single-line regex ^PAIR \{(\d+),(\d+)\} genus=\s*(\d+)\s*$ — previously line.split-based and silently dropped rows. Verified: rerun EXIT_CODE=0, 17/17 MATCH, capture code/out/genus_falsify.captured.txt; old and new parsers agree on every real capture line. |
| `famA2.sing` | _(undescribed)_ |
| `famB.sing` | _(undescribed)_ |
| `famC.sing` | _(undescribed)_ |
| `famD.sing` | _(undescribed)_ |
| `full_grid.sing` | Full grid 2<=k1,k2<=12 (Singular). Output matches Sage. |
| `genus_table.py` | **Library**: verified genus table + closed forms for the {2,n},{3,n},{4,n} families; the deliverable's source of exact genus values. |
| `repro_integrality.py` | Independent machine re-check of the genus-closed-form integrality lemma over the full range 1 <= m, n <= 799 with a per-parity-class breakdown, exact integer arithmetic (N(m,n) = (m-1)(n-1)+1-gcd(m,n) even, so g = N/2 always integral), plus agreement of the two algebraic forms on 1..399. Verified: EXIT_CODE=0, 638401 pairs, ZERO odd values in any of the four parity classes, both forms agree 159201/159201; capture code/out/integrality_reproduced.captured.txt closes TASKS.md item 4. |
| `sage_check_k2_6.py` | _(undescribed)_ |
| `small_column_genus_forms.md` | _(undescribed)_ |
| `spotcheck_new_pairs.sing` | Job-2 spot check of the closed genus formula g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2 at three pairs absent from genus_table.py TABLE and all captures: (11,17), (11,20), (12,20). Same incantation as full_grid.sing (ring r=0,(x,y),dp; poly CB; degree-max(m,n) curve; normal.lib genus). All three PASS with Singular genus 80/95/103, cross-verified by an independent Python computation of the formula. |
| `test_range.sing` | Mid-range probe: (4..10,3), (5..9,4), and (k,k) diagonal (shows reducible → nonsense genus, excluded). |
| `test_singular.sing` | First Singular test (failed: `genus` not in `sing.lib`). Kept as the dead-end record. |
| `test_singular2.sing` | Correct Singular recipe: load `normal.lib`, call `genus(ideal)`. Reproduces cubic=1, quartic=3, (3,2)=1. |
| `test_slope_across_rows.py` | _(undescribed)_ |
| `test_slope_hypothesis.py` | _(undescribed)_ |
| `verify_closed.py` | Checks closed forms vs the computed table (k2=2,3,4 all match). |
| `verify_closed2.py` | Attempts a k2=5 pattern; the obvious 2*floor and 2k1-a guesses FAIL — k2=5 has periodic stalls at multiples of 5. |
| `verify_k2_5_row.py` | _(undescribed)_ |
| `verify_riemann_hurwitz.py` | Verifies the Riemann-Hurwitz derivation of g(m,n)=((m-1)(n-1)+1-gcd(m,n))/2 for C(x,m)=C(y,n), including an explicit computation of the fibre at x=infinity. Checks 42 pairs: degree-n x-projection, m(n-1) simple finite ramification points (Rolle-bracketed bisection for critical y-roots — fixed from a polyroots NoConvergence at n=8 — with mirror-pair critical-value coincidences explained by (n-1-y)_n=(-1)^n(y)_n), the exact RH identity, and the infinity structure via chart u=1/x (no finite-y point; Puiseux branches y~c·u^(-m/n), index n/gcd, gcd branches, I_inf=n-gcd) confirmed numerically. Run: timeout 540 python3 code/genus/verify_riemann_hurwitz.py 2>&1 |
| `verify_superelliptic_formula.py` | Cross-check of the run's computed small-column genus rows for C(x,k1)=C(y,k2) against the LITERATURE superelliptic genus formula g=((d-2)(m-1)+m-gcd(m,d))/2 (Sutherland Open Book Series 4 (2020) eq. (1); Wikipedia Superelliptic curve). {2,n} hyperelliptic model (2y-1)^2=1+8C(x,n): 10 values; {3,n} cyclic trigonal model (y-1)^3-(y-1)=6C(x,n) (z^3-z, m=3): 21 values; {4,n} reported as non-superelliptic 2:1 cover (formula shown for the base only). EXECUTED this run: EXIT_CODE=0, ALL literature cross-checks PASS for {2,n} and {3,n}; capture code/out/verify_superelliptic_formula.captured.txt. The closed forms closed_2n and closed_3n and the recorded table agree with the citable primary formula on all 31 values. |
