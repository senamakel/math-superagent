# Llibre–Zhang, "Limit cycles of the classical Liénard systems: a survey on the Lins Neto, de Melo and Pugh's conjecture"

<!-- source: http://ddd.uab.cat/record/221320 (UAB postprint record); Expo. Math. 35(3):286–299 (2017), DOI 10.1016/j.exmath.2016.12.001 -->

**The correct Liénard-survey anchor.** This replaces the contaminated held file
`llibre-zhang-lienard-conjecture-survey.full.md`, which (Mureddu arXiv:1612.05532)
was an unrelated German-power-grid paper — the exact name-collision failure the
library exists to catch. This is the genuine Llibre–Zhang survey.

## What it establishes

For the classical Liénard system

```
ẋ = y − F(x),  ẏ = −x,   F a real polynomial of degree n,
```

the Lins Neto–de Melo–Pugh conjecture says there are at most ⌊(n−1)/2⌋ limit
cycles, and this is **sharp** (Theorem 1: degree-n systems exist with
⌊(n−1)/2⌋ cycles). The survey (with complete proofs of the known results)
establishes:

- (a) n = 1, 2: **no** limit cycles.
- (b) n = 3, 4: **at most one** limit cycle, and examples with one exist
  (n = 4: Li–Llibre 2012).
- n ≥ 6: the conjecture is **FALSE** — there are systems with at least
  **n − 2** limit cycles (Dumortier–Panazzolo–Roussarie 2007; De Maesschalck–
  Dumortier 2011: two more beyond the conjecture for n ≥ 6; De Maesschalck–
  Huzak 2015: asymptotically n−2 for n ≥ 6).
- **n = 5: OPEN** (unresolved) as of this survey — whether a degree-5 Liénard
  system can have more than ⌊(5−1)/2⌋ = 2 limit cycles.

## Implication for this problem

**The LdMP conjecture is true for n ≤ 4, false for n ≥ 6, and n = 5 is open** —
now anchored on a genuinely held source, correcting the earlier citation.
This is the cornerstone of the slow–fast test (problem.md test 3): the
counterexamples come from **canard / relaxation-oscillation constructions in the
singular limit** (small parameter), exactly the warning that sharp conjectures
die to slow–fast geometry.

**Evidence class**: sourced (UAB postprint record held full
  `research/sources/llibre-zhang-lienard-survey-expmath-2017.uab.full.md`;
  abstract + record content verified; the postprint PDF body on DDD not itself
  fetched).
**Falsifier**: a source closing the n = 5 case (≥ 3 cycles for degree-5 Liénard).
**Holds-here**: yes.

Claims ledger: `h16-lienard-ldmp-survey-2017`.
