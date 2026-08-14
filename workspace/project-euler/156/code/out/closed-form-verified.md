# Closed-form digit counter verified against the brute-force oracle

`code/lib/digits.py::f_place_value(n, d)` implements the place-value closed
form (the `G1` identity). This note records that the run **computationally
checked** it, not merely that it is sourced.

## What was checked (see `brute-oracle-output.txt` and `verify_brute.py`)

- `f(n,1)` for n = 0..12 equals the statement's table
  `0,1,1,1,1,1,1,1,1,1,2,4,5` (all 13 match; value 3 never occurs there).
- `f(22,2) = 6`.
- The closed form agrees with the brute-force running total `f(n,1)` for
  **every** n in 0..20000 (two independent routes to the same count).
- Every one of the 14 solutions the brute-force scan found in 0..300000
  (`0, 1, 199981..199990, 200000, 200001`) satisfies `f_place_value(n,1) = n`.
- `199981` is the third solution: no n in `2..199980` with `f(n,1)=n`.
- `f(n,1) = 3` never occurs anywhere in 0..300000.
- No solution in `200002..300000`.

Output files: `code/out/brute-oracle-output.txt` (brute.py run), plus the
verify_brute.py transcript in the run log.

```claim
id: G1-checked
statement: >
  The place-value closed form f_place_value(n,d) (O(log n) exact evaluation)
  agrees with the brute-force definition of f(n,d) on the statement's oracle
  table f(n,1) for n=0..12, on f(22,2)=6, on the running total f(n,1) for
  every n in 0..20000, and on all 14 solutions in 0..300000; it also
  reproduces the statement's first solutions 0, 1, 199981.
hypotheses: d in {1,...,9}; f counts digit d in the decimal writings of 0..n.
holds-here: yes
status: checked (computed by the run; oracle code/brute.py and closed-form
  code/lib/digits.py agree, see code/out/brute-oracle-output.txt and
  verify_brute.py)
bearing: >
  Upgrades G1-digit-count-closed-form from "asserted/sourced" to verified;
  the O(log n) digit-count function is sound to use as the evaluator inside
  the skip-search. Remaining unverified pieces are G3's skip-completeness and
  the reproduction of s(1)=22786974071 / the final Σs(d), which need the
  efficient per-interval solver (code/solution.py).
anchor: code/out/closed-form-verified.md (this note)
```

The bound `n ≤ d·10^10` (G2) and the skip lemma (G3) remain the un-computed
pieces; G1 is now verification-backed, not just source-backed.
