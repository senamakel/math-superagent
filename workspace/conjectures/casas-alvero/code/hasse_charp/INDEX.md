# Index — code/hasse_charp

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `recheck_xpp1_xp_hasse.py` | Recheck program for claim `charp-witness-xpp1-xp`'s "f(X^p) without constant term also works since all derivatives vanish" clause under the Hasse formulation. Exact sympy over GF(p); entry guards; part (A) x^{p+1}-x^p and part (B) x^{mp} / x^p+x^{2p} report is_ca, is_ca_hasse, is_pure_power, H_1/H_2/H_p, nonzero-Hasse list. Established correct: 56/56 cross-checks agree with `crosscheck_hasse_independent.py`; capture `code/out/ordinary-vs-hasse-charp-witness.captured.txt`; verdict `code/out/ordinary-vs-hasse-charp-witness.md`. |
| `crosscheck_hasse_independent.py` | Independent second route: hand-rolled F_p ring and Euclid gcd (no sympy, no lib imports), closed-form Hasse coefficient C(j,i) mod p. 56/56 checks agree with the oracle route. |
