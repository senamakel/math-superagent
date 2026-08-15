# Cobeli–Zaharescu, "Promenade around Pascal Triangle – Number Motives"

<!-- source: http://rms.unibuc.ro/bulletin/pdf/56-1/PromenadePascalPart1.pdf | converted from PDF -->
**Bull. Math. Soc. Sci. Math. Roumanie, Tome 56(104) No. 1, 2013, 73–98.**

A survey of the theme of iterated application of the fundamental rule of addition in
Pascal-triangle-like constructions. Key words include Pascal triangle, Sierpinski gasket,
fractals, Collatz, Ducci game, absolute differences, **Gilbreath conjecture**, greatest prime
factor, continued fractions. Part 1 = number motives; a companion part covers geometric
motives.

## What it establishes / corroborates relevant to this run

- **§9 (Z-game and Gilbreath).** The authors introduce a multiplicative-rule triangle
  `Z(a,b) = ab/gcd(a,b)²` whose "genealogical neighbour" is Gilbreath's conjecture. They
  state (p. 87) that Gilbreath's conjecture is "from 1958, for which an incorrect proof was
  given by Proth in 1878" — an **independent primary-source corroboration of the run's
  Proth-1878 retraction finding** (a retraction, not a located error; nothing to prove
  wrong). The triangle from Figure 5 reproduces exactly the run's `A_0..A_5` rows for the
  first 10 primes, and the text cites Odlyzko 1993's verification to `π(10^13)`.
- **§7.3 (Ducci games).** Confirms the cyclic-Ducci mod-2/power-of-2 facts already held from
  the primary Ducci sources: `φ^(n)(a) = (0,...,0)` on `N_{2^k}` for large n; the period of
  the Ducci evolution on `{0,1}^d` is governed by the order of 2 modulo the largest odd
  factor of d; short periods at Mersenne-prime d, long cycles when 2 is primitive mod d
  (Artin). The Pascal-mod-2 additivity `φ^(n)|_{U_d}(a)_j = Σ_k C(n,k)a_{j+k} (mod 2)` is
  exactly the run's proved rule-90-interior-xor in the cyclic setting.
- **§7.2 (gpf sequences).** CZZ'12 is cited for the infinite-order recurrent prime sequence
  `q_j = gpf(q_1+...+q_{j-1})` with growth `q_j = j/2 + O(j^0.525)` — an independent
  appearance of the **same `.525` exponent** (Baker–Harman–Pintz) the run uses as the
  demand side of Granville's ν₂ reduction. Corroboration, not new.
- **§4 (Pascal mod 2).** Sierpinski-gasket / Rule-90 structure via binomial coefficients mod
  2, consistent with the run's block-interior dynamics.
- **Singmaster conjecture** (§3) and continued-fraction p-adic material (§8) are orthogonal.

## What it does NOT add

No new method for the open *regeneration* side; no claim about block-length growth or the
(2,4)-event rate. It is a survey-grade confirmation of facts the library already holds from
primary sources (Ducci restated; Proth-retraction restated; Odlyzko-10^13 restated). The two
Cobeli–Zaharescu primary papers it previews — the Z-game and the divisors/e-exponent game —
are already in the library as `cobeli-prunescu-zaharescu-2016-arithmetic-z-game` and
`cobeli-zaharescu-2014-game-divisors-absolute-differences-exponents`.

## Placement

Full text: `research/sources/cobeli-zaharescu-2013-promenade-pascal-part1.full.md`.
Filed by the librarian on a frontier-driven fetch: this was tied for the most-cited item in
`research/FRONTIER.md` (cited 6× by the library's own sources) and was not on disk before
this cycle.
