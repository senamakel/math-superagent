# Librarian cycle — 2026-08-13 (build/verify pass)

## What this cycle established about the library's state

The library is effectively complete for the run's active threads. Every gap the
brief warns about (invented arXiv IDs, Wikipedia/MathWorld cited without a
download, unrelated papers filed under wanted names) was checked against the
live record and the live arXiv and found **not present** in this library:

- The two Garcia-Fritz–Pasten papers (`arXiv:2604.04850v2` Bremner-conjecture
  note, `arXiv:2605.14962` patterns paper) were verified against the live arXiv
  listing and are real papers with the content the summaries attribute to them.
  Both full texts are on disk as genuine PDFs — NOT wrappers.
- `wikipedia-magic-square-of-squares` and `open-problem-garden-magic-square-of-
  squares` ARE on disk (the two sources the Erdős–Gyárfás run cited without
  downloading). The path is `research/sources/wikipedia-magic-square-of-
  squares.full.md`. This library holds them.
- The run's central adopted approach (`uniform-height-bound-elliptic-ap`) has
  its one recorded gap — the *effective constant* — checked. Two sources address
  it: Garcia-Fritz–Pasten give C ineffective; **Harrison–Mudgal–Schmidt
  (arXiv:2603.06483, Theorem 1.1)** provide an effectively computable C (but
  astronomically large, no explicit value). This is the correct, current state
  of the constant question; the REQUESTS gap "has anyone computed or bounded
  these constants" is answered: **no one has computed an explicit value**.
  Search-verified this cycle.

## Primary-source availability, recorded so nobody retries the dead ends

- **Buell, "A search for a magic hourglass" (preprint 1999).** Full text is a
  garbled/corrupted PDF conversion (`research/sources/buell-search-for-magic-
  hourglass-1999.full.md` is noise). The `25×10²⁴` hourglass bound is captured
  from secondary sources (Bremner II, Zimmermann–Loria) with the crucial
  coprimality caveat, and the correction (Zimmermann–Loria find 10-digit
  hourglass solutions mod 2⁴⁷ under relaxed assumptions) is a claim block. The
  full-text dead end was already recorded; not re-attempted this cycle (would
  re-fetch the same corrupted file).
- **Rabern, "Properties of Magic Squares of Squares" (RHUMJ 2003).** PDF at
  scholar.rose-hulman.edu returns HTTP 403 Forbidden (recorded; not to be
  retried). The abstract page IS on disk, and the full theorem content (all
  entries odd; centre primes ≡1 mod 4 only; no 3-mod-8 anywhere; no 5-mod-8 on
  middle-side) was recovered this cycle from the search-exposed body text and
  cross-checked against the independently-verified `primitive-mss-entry-
  congruences` / `primitive-mss-modular-124-72` claims, which supersede it as
  checked results. Do not cite Rabern's prime-distribution claims as
  proof-checked; cite the checked congruences instead.

## OEIS misses (findings, so nobody re-searches)

- `|Φ(M)|` for M = 10,20,30,40,50,60,70,80(?),... = 22, 86, 331, 737, 1314, 2040,
  2930, 4582, 8156, 32495 — **no OEIS entry matches**. No closed form is
  catalogued; structure must come from the problem.
- Count of `e ≤ 10^k` with `|S(e)| ≥ 4` = 0, 2, 81, 1491, 20806, 254549, 2924760
  (k=1..7) — **no OEIS entry matches**.

## Gap status

- `exact-reduction-magic-507c` (the doubled-point AP question) is **answered**
  by claim `patterns-bremner-2026-no-mismatch-for-2E-Q`: the MSS AP of doubled
  x-coordinates IS an AP of x-coordinates of points in 2E(Q) on the single
  curve E, so Garcia-Fritz–Pasten's bound applies; the surviving obstruction is
  the ineffective constant, now advanced (not closed) by Harrison–Mudgal–Schmidt.
- Nothing further to add this cycle: every canonical tier, the surveys, the
  failed approaches, the adjacent problems, the computational attacks, and the
  counterexample constructions are on disk. Further gathering should only happen
  against a stated, narrower gap in `research/REQUESTS.md`.
