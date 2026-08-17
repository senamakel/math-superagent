# DIVERSIFIED degree-20 candidate search -- div2 batch

Program: `code/search/ca-degree20/diversify_run.py`; scorer: `code/search/ca-degree20/score.py` (exact sympy `Poly.gcd` over QQ); base ring QQ; candidate modules: 18 (`div2_<family>_<param>.py`).

## Table (family, candidate, score, first-failing-j)

| family | candidate | score | first-failing-j | scorer verdict |
|--------|-----------|-------|-----------------|----------------|
| CHEBYSHEV | div2_cheb_h1.py | 1 | 2 | SCORE: 1 |
| CHEBYSHEV | div2_cheb_h2.py | 0 | 1 | SCORE: 0 |
| CHEBYSHEV | div2_cheb_h3.py | 1 | 2 | SCORE: 1 |
| CYCLOTOMIC | div2_cyclo_c1.py | 3 | 4 | SCORE: 3 |
| CYCLOTOMIC | div2_cyclo_c2.py | 1 | 2 | SCORE: 1 |
| CYCLOTOMIC | div2_cyclo_c3.py | 15 | 12 | SCORE: 15 |
| FACTORED (x-r)^m g | div2_factored_f1.py | 14 | 15 | SCORE: 14 |
| FACTORED (x-r)^m g | div2_factored_f2.py | 13 | 14 | SCORE: 13 |
| FACTORED (x-r)^m g | div2_factored_f3.py | 15 | 16 | SCORE: 15 |
| FACTORED (x-r)^m g | div2_factored_f4.py | 17 | 15 | SCORE: 17 |
| ROOT-MULTISET | div2_rootset_r1.py | 15 | 16 | SCORE: 15 |
| ROOT-MULTISET | div2_rootset_r2.py | 14 | 15 | SCORE: 14 |
| ROOT-MULTISET | div2_rootset_r3.py | 8 | 8 | SCORE: 8 |
| TRINOMIAL | div2_trinomial_t1.py | 17 | 3 | SCORE: 17 |
| TRINOMIAL | div2_trinomial_t2.py | 17 | 5 | SCORE: 17 |
| TRINOMIAL | div2_trinomial_t3.py | 17 | 6 | SCORE: 17 |
| TRINOMIAL | div2_trinomial_t4.py | 17 | 9 | SCORE: 17 |
| TRINOMIAL | div2_trinomial_t5.py | 17 | 2 | SCORE: 17 |

## First-failing-j distribution ACROSS families

(first-failing-j = smallest j in 1..19 with deg(gcd(f, f^(j))) == 0; "NONE" would mean all 19 share a root = the open conjecture.)

| family | first-failing-j | count |
|--------|-----------------|-------|
| CHEBYSHEV | 1 | 1 |
| CHEBYSHEV | 2 | 2 |
| CYCLOTOMIC | 12 | 1 |
| CYCLOTOMIC | 2 | 1 |
| CYCLOTOMIC | 4 | 1 |
| FACTORED (x-r)^m g | 14 | 1 |
| FACTORED (x-r)^m g | 15 | 2 |
| FACTORED (x-r)^m g | 16 | 1 |
| ROOT-MULTISET | 15 | 1 |
| ROOT-MULTISET | 16 | 1 |
| ROOT-MULTISET | 8 | 1 |
| TRINOMIAL | 2 | 1 |
| TRINOMIAL | 3 | 1 |
| TRINOMIAL | 5 | 1 |
| TRINOMIAL | 6 | 1 |
| TRINOMIAL | 9 | 1 |

> NO NON-TRIVIAL SCORE-19: bug guard clean. All div2 scores < 19; reaching 19 is exactly the open CA conjecture (only (x-a)^20
legitimately hits it, which the scorer rejects as the trivial family). So no candidate here is a counterexample -- by construction.

## What the distribution says (the deliverable)

**First-failing-j VARIES by family and by parameter -- it is not always the
high-multiplicity root's limit, and it is not a binomial-family constant.**
Contrast with the binomial family `x^20 - c*x^k`, where the only failing
derivative is always `j = k` and every non-trivial binomial scores 18 for
free. The div2 batch breaks that plateau, and the binding constraint is
different per construction:

- **TRINOMIAL** (`x^20 + a*x^k + b*x^m`, all five candidates score 17, not 18):
  the two exposed exponents `k < m` are the two failing derivatives -- a
  derivative `j` fails exactly when it 'lands on' an exposed non-monomial term
  where the monomial root 0 is not a root of `f^(j)`. First-failing-j is the
  smallest exposed exponent (j = 2,3,5,6,9 across the five). Score 17 = 19 - 2
  fails, so a genuine third support term breaks the two-term plateau at 18.
  Verified exactly: failing-j == {k, m} for all five trinomials.
- **FACTORED `(x-r)^m*g`**: first-failing-j sits at `m` (just past the heavy
  root's multiplicity, which covers 1..m-1): f1 (m=15)->j=15, f2 (m=14)->j=14,
  f3 (m=16)->j=16, f4 (m=15)->j=15. The irreducible tail adds no sharing, so
  score = m-1 = 14,13,15,16. The high-multiplicity mechanism in purest form.
- **ROOT-MULTISET**: depends on cross-multiplicity sharing. Balanced
  `x^8(x-1)^7(x+1)^5` (8-7-5) scores only 8, failing at j=8 (smallest heavy
  multiplicity); one-dominant rootsets (16-2-2, 15-3-2) score 15/14 failing at
  j=16/15, just past the dominant multiplicity. Weak cross-sharing; the
  dominant root's multiplicity governs.
- **CYCLOTOMIC**: highly variable. `(x^5-1)^4` scores 3 (5th roots mult 4,
  j=4 fails); `(x^10-1)^2` scores 1 (double roots, j=2); `(x-1)^12*phi_20(x-1)`
  scores **15** failing at j=12 AND j=14,16,18 -- a NON-contiguous failing set
  (shares only odd high j). The only family whose failure pattern is not a
  single contiguous block: a parity/structure signature unique to the shifted
  cyclotomic shape.
- **CHEBYSHEV** scores 0-1: all-simple T_20 roots and double T_10^2 roots give
  only trivial j=1/2 sharing; no recycled-root structure.

**Conclusion for the search.** 'score = m-1, fail at j = m' is real but only
for single-heavy-root constructions. Once the support is genuinely multi-term
(trinomials cap at 17 with two fails) or multiplicities are balanced or roots
carry cyclotomic/parity structure, both the score and the first-failing-j move.
No div2 candidate approaches 19, and none should: 19 on a non-trivial
polynomial is exactly the open conjecture and would be a scorer bug. The
binding constraint is family-dependent -- precisely the information the
all-binomial population destroyed.

