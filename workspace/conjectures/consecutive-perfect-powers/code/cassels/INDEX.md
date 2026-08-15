# Index — code/cassels

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `REDUCTION.md` | The elementary reduction of Cassels p\ |
| `descent_probe.py` | Probe for the Cassels descent (L1): symbolic identity Phi_p(a^q+1) = sum C(p,j+1) a^{qj}; descent lemma (never a q-th power) checked for p,q in {3,5,7,11,13}, a<=200; residue pattern (b^q == p mod a^q, b^q == 1 mod p) and near-miss gaps; falsifier calibration. Exact integers. (Other school's probe; a<=200 — elementary_structure.py sweeps the same L1 to a<=20000.) |
| `elementary_structure.py` | Exact-integer elementary structure checks behind Cassels p|y, q|x for x^p-y^q=1: (1) gcd lemma gcd(x-1,Phi_p(x))==gcd(x-1,p) for p in {3,5,7,11,13,17}, x in [2,200000] (1,199,994 cases PASS); (2) Fermat equivalence p|x-1 <=> p|x^p-1, same range PASS; (3) reduced-system sweep (REDUCTION.md L1, spine of p|y): Phi_p(a^q+1) a perfect q-th power? p in {3,5,7,11,13} x q in {3,5,7}, p!=q, a in [1,20000], p∤a — 202,886 cases, ZERO q-th powers; (4) mirror sweep (spine of q|x): Phi_q(-(c^p-1)) a perfect p-th power? c in [1,5000], q∤c — 46,480 cases, ZERO non-degenerate; (5) calibration at (3,2,2,3): p=2 even excluded, gcd(2,4)=2=gcd(2,2), 2|3-1, 3|2+1 PASS; (6) gmpy2.iroot cross-check on 258 sampled roots. Exact integer Newton roots (lib.perfectpow.iroot) + b**q==value, no floats. Run: timeout 540 python3 code/cassels/elementary_structure.py | tee code/out/cassels_elementary.captured.txt — OVERALL ALL CHECKS PASS, 1.17s, EXIT 0. Claim: cassels-reduced-system-sweep in code/out/cassels_elementary.note.md. |
| `lambda_valuation.py` | Exact (1-zeta_p)-adic valuation of x-zeta_p in Z[zeta_p] by iterative division, and exact integer v_p. Verifies two foundational facts for the Cassels step of Catalan: v_lambda(x-zeta)==1 iff p\ |
