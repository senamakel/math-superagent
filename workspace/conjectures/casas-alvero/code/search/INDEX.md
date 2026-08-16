# Index — code/search

Programs for the **scored program search** on Casas–Alvero at degree 20.

The search: given candidate monic degree-20 polynomials over Q (proposed by a
search/inventor role), score them by how many of the 19 derivatives share a
root. Degree 20 is the smallest open degree, so a true counterexample is NOT
expected — the goal is the score distribution and which constraint binds.

| File | Purpose |
| --- | --- |
| `ca-degree20/PROBLEM.md` | The search statement: score = #{ j in 1..19 : deg(gcd(f,f^(j)))>0 over Q[x] }, exact; why it is not about finding a counterexample; the trivial-family exploit and why it is rejected. |
| `ca-degree20/score.py` | THE scorer. `python score.py <module.py>` → exactly one line. `SCORE: k` (k = number of the 19 derivatives sharing a root with f, exact sympy gcd over QQ, no floats) or `INVALID: <reason>` for: (a) f=(x-a)^20 trivial family; (b) not monic / not degree 20 / non-rational coefficients (per-coefficient `is_rational`); (c) module fails to import or exposes no polynomial in x (importlib from literal path; callables/strings ignored so they cannot be sympified into a junk degree-0 poly). Established correct by the 6-case smoke test in `smoketest.txt` (SCORE 18 for x^20-x; INVALID exact reasons for trivial / deg19 / nonmonic / nonrational / no-poly). |
| `ca-degree20/smoketest.txt` | The recorded self-test the tool-builder ran (4 required cases + nonmonic/nonrational variants), each with the observed one-line output and why. |
| `ca-degree20/verify_ceiling.py` | Independent exact re-check of the search's two structural claims (mult-19-root family and `x^20-x`): per-`j` `deg(gcd(f, f^(j)))` over QQ, the identity of the failing derivative, and the score, plus the closed-form root of the linear `f^(19)`. Output `verify_ceiling.txt`. Established correct: every number is an exact sympy `Poly.gcd` over QQ (no floats); asserts make the script fail (`exit≠0`) unless each family scores exactly 18 and fails at exactly the expected `j`. |
| `ca-degree20/verify_ceiling.txt` | The recorded output of `verify_ceiling.py` (exit 0, ALL EXACT CHECKS PASSED): `x^20-x` scores 18 failing only at `j=1` (f′ = 20x¹⁹−1), not j=19 — f^(19)=20!·x shares root 0 with f. `x^19(x−c)` c=1,2,3 each score 18 failing only at `j=19` (the linear f^(19), root c/20, never a root of f). `(x−a)^19(x−b)` for several (a,b) all score 18; the alignment attempt (search's c0068..c0070) cannot reach 19 because f^(19)'s root (19a+b)/20 lies in {a,b} only when a=b, the rejected pure power. |
| `ca-degree20/smoketest/` | The small candidate modules the smoke test drives: `cand_x20_minus_x.py`, `cand_trivial_x_minus_3_pow20.py`, `cand_deg19.py`, `cand_nonmonic.py`, `cand_nonrational.py`, `cand_nopolynomial.py`. |
