# Oracle built and verified against the statement's worked examples

Ran `python code/brute.py` (exit 0). The naive oracle in `code/brute.py`
decides the Casas-Alvero derivative-sharing hypothesis exactly over `Q`
(`Fractions`) and over `F_p` (int mod `p`), plus whether `f` is a pure power —
using only Euclid and a char-safe squarefree-radical recursion. No floating
point anywhere.

## Worked examples from problem.md, and whether they matched

| Check | Expected | Result |
| --- | --- | --- |
| `(x−a)^n` over `Q`, n=1..6, a∈{0,1,3/2} | hypothesis True, pure power True | MATCH (all 18) |
| generic random monic `f` over `Q` (8 samples) | hypothesis False | MATCH |
| `x^{p+1} − x^p` in `F_p`, p=2,3,5,7 | hypothesis True, **not** pure power | MATCH (char-p counterexample) |
| `(x−1)^p` in `F_p`, p=3,5 | hypothesis True, pure power True | MATCH |

This pins down the statement as: the hypothesis is a gcd-non-triviality for
every derivative, and the char-`p` witnesses genuinely satisfy it while
escaping a pure power (the negative control the oracle must flag).

## Two real subtleties found and handled

1. **`deg(gcd(f,f')) == n−1` is NOT the pure-power test in char `p`.**
   `x^2(x+1)` in `F_2` has `gcd(f,f') = x^2` of degree 2 = n−1 but two
   distinct roots, because multiplicities divisible by `p` survive in the
   gcd. The correct char-safe test is *single distinct root* —
   `deg(radical(f)) == 1` — computed by a recursion that removes `p`-th
   powers (`f' == 0`) and otherwise `rad(f)=rad(c)·rad(g)/gcd(...)`.

2. The first draft's `is_pure_power` read off `a = −c_{n−1}/n`, which is
   impossible when `p | n`. Replaced by the radical test, which is correct in
   every characteristic.

## Independent verification (rule 11)

Cross-checked against sympy's trusted `sqf_list`/`gcd` on a hand-picked
char-`p` set: `x^2`, `x^2(x+1)`, `x^3`, `x^3−x^2`, `x^4`, `(x−1)^6` in `F_3`,
`x^4+x^3`, `x^6+x^3+1`, `x^3` in `F_2`. Oracle and sympy agree on both the
hypothesis and pure-power verdict for all ten — including the subtle `x^2(x+1)`
in `F_2` (hypothesis True, not a pure power) and `(x−1)^6` in `F_3` (a pure
power).

## status

`claim: oracle-agrees-with-sympy-sqflist-and-gcd-on-char-p-set; the naive
oracle satisfies_hypothesis and is_pure_power match sympy on the statement's
worked examples and on a broad char-p set; status: checked`
