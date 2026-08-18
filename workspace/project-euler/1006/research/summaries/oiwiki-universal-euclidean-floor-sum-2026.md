# OI Wiki (2026 fetch) — 万能欧几里得算法 / universal Euclidean algorithm (current page)

<!-- source: https://oi-wiki.org/math/number-theory/euclidean/ | fetched 2026-08-19 -->

Full text: `[[oiwiki-universal-euclidean-floor-sum-2026.full]]` (75 KB, 1680 lines; current OI-wiki page in Chinese, HTML→MD).

## Relationship to the earlier fetch

`research/sources/oi-wiki-universal-euclidean-floor-sum.full.md` (also 75 KB) is the same OI-wiki page from an earlier fetch; the two files are near-duplicates of the current page. The `-2026` file is the one whose fetch date is recorded; keep it as the current reference and treat the older one as the same content.

## What it establishes (read: §万能欧几里得算法, lines 676–1116)

The universal Euclidean algorithm (万能欧几里得), the monoid generalisation of the Euclidean-like floor-sum algorithm:

- **Problem form**: for the segment y = (ax+b)/c, 0 < x ≤ n, build the operation string S with n R's and m = ⌊(an+b)/c⌋ U's, the i-th R preceded by ⌊(ai+b)/c⌋ U's. U and R are monoid elements; the answer is the product of the whole string.
- **Two equivalent monoid models**: (i) 3×3 matrices U = [[1,1,0],[0,1,0],[0,0,1]], R = [[1,0,0],[0,1,1],[0,0,1]] acting on (1, y, Σy); (ii) the tuple (x, y, s) = (number of R's, number of U's, Σy over R-prefixes) with merge (x₁,y₁,s₁)·(x₂,y₂,s₂) = (x₁+x₂, y₁+y₂, s₁+s₂+x₂y₁), associative, identity (0,0,0). Model (ii) is the practical one (less redundant state).
- **The recursion (verbatim, exact integer arithmetic)**:
  - if b ≥ c: F(a,b,c,n,U,R) = U^{⌊b/c⌋} · F(a, b mod c, c, n, U, R)
  - if a ≥ c: F(a,b,c,n,U,R) = F(a mod c, b, c, n, U, U^{⌊a/c⌋}R)
  - else m = ⌊(an+b)/c⌋; if m = 0: return Rⁿ (special case — needed because the flip would use negative powers);
  - else: return R^{⌊(c−b−1)/a⌋} · U · F(c, (c−b−1) mod a, a, m−1, R, U) · R^{n−⌊(cm−b−1)/a⌋}.
- **Complexity (proved in-page)**: each round maps (a,·,c,·) → (c,·,a mod c) and costs O(log(a/c) + log(c/(a mod c))) for the three binary exponentiations; the rounds telescope to **O(log max{a,c} + log(b/c)) total** — O(log) in the parameters, independent of n. This is the go/no-go fact for k=10^18.
- Complete C++ templates for both monoid models plus a Library Checker "Sum of Floor of Linear" solution.

## Why it matters here

This is the current-page statement of the exact primitive `code/lib/ueuclid.py` implements (claim `monoid-composition-formulas-verified`, `governing-universal-euclidean`). It confirms the recursion's index arithmetic — (c−b−1)/a, (c−b−1) mod a, m−1, n−⌊(cm−b−1)/a⌋ — matches the module's own __main__ capture (ALL MONOID TESTS PASSED, 30/30 vs direct). The page's (x,y,s) monoid is the un-weighted prototype; the geometric-weight 10^i moments are the fhq note's contribution.

## Claims anchored here

Corroborates `governing-universal-euclidean`, `monoid-composition-formulas-verified` (S0/S1 merge rules are the s-merge specialised with weights). No new claim block.
