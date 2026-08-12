# Boyer, "A search for 3×3 magic squares having more than six square integers" (2004) — [[boyer-square-of-squares-search-v2.full]]

Computational search paper by Christian Boyer that fixes the actual verification bound and the provenance of the near-misses. Restates the two known near-misses:
- **LS1** (Sallows & Schweitzer, found independently): `[127²,46²,58²; 2²,113²,94²; 74²,82²,97²]`, 7 of 8 sums = 21609, one diagonal = 38307.
- **7-square magic square** (Sallows and Bremner, independently): `[373²,289²,565²; 360721,425²,23²; 205²,527²,222121]`, configuration 7.IV, centre 425² = 180625. This is "the only known example having seven square integers, excluding symmetries, rotations and k² multiples".

## Sums-of-two-squares structure of the four centre lines (D1/D2)
A line through centre C with two square endpoints satisfies x²+y²=2C. Since 4k+3 primes cannot be sums of two squares, only central cells that are products of 4k+1 primes are studied.
- **D1** — C = c² a square with n distinct 4k+1 prime factors: `(3ⁿ−1)/2` solutions of x²+y²=2c², x<y.
- **D2** — C not a square with n distinct 4k+1 prime factors: `2^(n−1)` solutions of x²+y²=2C, x<y.
- A 4k+1 prime is a sum of two squares in one way; (a²+b²)(c²+d²) gives two ways: (ad+bc)²+(ac−bd)² and (ad−bc)²+(ac+bd)²; and 2(a²+b²)=(a+b)²+(a−b)².

## The exhaustive search bounds (with square centre C=c²)
Central cell restricted to types `(main 5^i · product of 4k+1 primes)²`, various prime ranges; **Fig. 6 is the ONLY magic square with more than six square entries** (up to symmetry/k²) among all central cells of these types. Largest square-centre bound covered:
- (5^i·p1·…·p8)² with pj ≤ 29 → central cell < 1.56×10²⁶; and type l) (5^i0·p1^i1·p2^i2·p3^i3)² up to central cell < 2.14×10³⁰.
Because multiplying all cells by the same square factor preserves square-count, results for (5²·...) cover submultiples (5·...)² and (...)² automatically.

## With non-square centre
Types (5^i·p1·…·p7) up to central cell < 3.35×10¹⁷; no magic square with >6 square entries.

## Verdict / implication
Even one more 7-square example resisted a very wide and varied central-cell search. Boyer's stated feeling is that a full square of squares "cannot exist", but **no proof exists** — it is explicit that this is a feeling.

```claim
id: boyer-search-bound
statement: Among all magic squares whose central cell is a square of the listed types (products
  of 4k+1 primes with ranges covering up to 2×10³⁰ for square centres) — or a non-square of the
  listed types (up to 3×10¹⁷) — there is no 3×3 magic square with more than six square entries
  except the single known 7-square example (up to symmetry and k² multiples).
hypotheses: centre of the listed product-of-4k+1-primes types; search exhaustive over the
  stated prime ranges
holds-here: yes
status: asserted (computed by Boyer, not independently reproduced here)
bearing: the true computational frontier; a 7-square (hence any 9-square) solution must have a
  centre outside every listed range, i.e. beyond ~10²⁶–10³⁰
anchor: research/sources/boyer-square-of-squares-search-v2.full.md
contradicts: any claim that a 7- or 9-square magic square appears with a small central cell
```

```claim
id: sum-two-squares-counts
statement: For C=c² with n distinct 4k+1 prime factors there are (3ⁿ−1)/2 solutions of
  x²+y²=2c² (x<y); for non-square C there are 2^(n−1).
hypotheses: C squarefree part only has 4k+1 primes; count of solutions with 0<x<y
holds-here: yes (applies to centre-line structure of any candidate grid)
status: proved (derivation given in source, from the two-squares identity)
bearing: bounds how many distinct centre-lines a candidate can realise, a combinatorics
  constraint on any 7/8/9-square grid
anchor: research/sources/boyer-square-of-squares-search-v2.full.md
```
