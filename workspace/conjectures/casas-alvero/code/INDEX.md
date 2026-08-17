# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Working rules for code/: one job per file, naive program is the oracle, exact arithmetic, name for what it computes. |
| `brute.py` | Naive cross-check oracle for the Casas-Alvero derivative-sharing hypothesis — rule-9 brute-force verification only, NOT the decision procedure. Public API: `satisfies_hypothesis(f, p=None)`, `is_pure_power(f, p=None)`, `ca_verdict(f, p=None)` where f is a monic coeff list in ASCENDING order and p=None is Q (Fractions), p prime is F_p. Exact Euclid gcd / char-safe radical (no floating point). |
| `roots5/` | First executable step of the five-distinct-roots rung of CA over Q: multipattern.py classifies every 5-part multiplicity pattern n=5..10 by the multiplicity+centroid mechanism and proves none is satisfiable (headline), capturing to code/out/fiveroots_multipattern.captured.txt. See roots5/INDEX.md. |
| `search/` | Scored program search for Casas-Alvero at degree 20: `ca-degree20/score.py` scores a candidate monic degree-20 Q-polynomial by how many of its 19 derivatives share a root (exact sympy gcd over QQ), rejecting the trivia `(x-a)^20`, non-monic/non-degree-20/non-rational, and non-importing modules. See `search/INDEX.md`. |
