# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `ca_deg3_char2.p` | TPTP encoding of CA in degree 3 over F_2 as a finite-domain first-order problem; find_counterexample returns refuted via f=x^3+x^2. |
| `ca_deg4_char3.p` | TPTP encoding of CA in degree 4 over F_3 (Hasse formulation); find_counterexample returns refuted via f=x^4+x, the explicit two-root char-p witness that also falsifies the char-free two-roots rung. |
| `ca_deg4_char5.p` | TPTP encoding of CA in degree 4 over F_5 (Hasse formulation, five explicit distinct field elements c0..c4); find_counterexample returns refuted via f=x^4-x^2 = x^2(x-1)(x+1), a three-root char-p witness that is not a pure power — engine-and-hand-verified confirmation that p=5 is a bad prime for n=4. |
| `ca_deg4_char7.p` | TPTP encoding of CA degree 4 over F_7 (Hasse formulation); find_counterexample refutes via f=x^4+x^3+4x (three-root witness {0,4,5}, not a pure power), confirming p=7 as the third bad prime for n=4 ({3,5,7}). |
| `ca_deg5_char2.p` | TPTP encoding of CA in degree 5 over F_2 (Hasse formulation); the first n=5 refutation in the refute set, targeting p=2 a bad prime for n=5. Held witness f=x^5+x^4=x^4(x+1), two distinct roots, not a pure power. |
| `ca_deg6_char2.p` | TPTP encoding of CA in degree 6 over F_2 (Hasse formulation); find_counterexample refutes via f=x^6+x^2=x^2(x+1)^4, confirming p=2 (first published degree-6 bad prime) is bad for n=6. |
| `ca_deg6_char5.p` | TPTP encoding of CA in degree 6 over F_5; the adopted root-difference-coloring approach's collapse step is false in char 5 via per-color Hasse degeneracy (H_2,H_3,H_4 vanish, f=x^6-x^5 has two roots). |
| `ca_deg7_char2.p` | TPTP encoding of CA in degree 7 over F_2 (Hasse formulation); find_counterexample returns refuted via f=x^7+x^3=x^3(x+1)^4, the first n=7 refutation in the refute set, an independent finite-model confirmation that p=2 is a bad prime for degree 7. |
| `check_deg4_char7.py` | Hand-check of the F_7 witness arithmetic for ca_deg4_char7.p: recompute the value tables of f and its Hasse derivatives exactly mod 7 and confirm common roots and non-pure-power status. |
| `check_reformulation_charp.py` | Exact check of whether the regular-sequence/J_T reformulation of CA tracks ordinary or Hasse formal derivatives over F_p, at n=3,4, to locate the char-p break in the G-reformulation-equivalence lemma. |
| `check_reformulation_direct.py` | _(undescribed)_ |
| `verify_rootdiff_identity.py` | Exact sympy verification of the root-difference-coloring first-step identity H_i(f)(x)=e_{n-i}(x-beta) and Res_x(f,H_i)=prod e_{n-i}(differences), over QQ (n=4,5,6) and F_p (n=p+1, p=2,3,5). Draft; the identity itself was not run because the run lacks a Python-execution tool, only find_counterexample. The working refutation lives in ca_deg6_char5.p. |
