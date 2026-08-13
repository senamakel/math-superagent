# Tasks

## Completed

- [x] Library audit + scholar pass 2026-08-14 (see research/notes/scholar-pass-library-audit.md)
- [x] `budget-equality-case-impossible` verified from captured output `code/out/equality_case_elimination.captured.txt`:
  (1) a=1 max product = 4/3 exactly, {5,9} is odd part of 90;
  (2) 2^8+1=257 prime, forced when a=8;
  (3) 9=3^2 and 49=7^2 admissible, 3 and 7 are not;
  (4) exclusion runs 2 ≤ a ≤ 28, stops at 29.
  All four confirmed. Thread `a-ge-8-bound` resolved: equality case impossible for 2 ≤ a ≤ 28.

## Next

- [ ] Attack H_even via the divisor-level problem for Φ_{4p}(2). The biquadratic-character approach (research/approaches/biquadratic-character-divisors.md) is the active line. First concrete step: compute Gaussian factorization of 2^p + i for small primes p and tabulate (2/π)_4 against p mod 8 and Aurifeuillean half. Use `code/heven_classify.py` and `code/heven_patterns.py` as entry points.

## Standing

- [ ] Do not fetch any new sources while FRONTIER.md unworked count > 100. The Maciejewski paper (93 KB) is already on disk at `research/sources/maciejewski-bounded-box-subbarao-warren.full.md`. Surveys (Guy B3, Handbook, Goto 2007) are already in the library.
- [ ] The [74:08] "progress no" verdict came from a judge that TIMED OUT. It is not an assessment. H_even is the correct branch.

## Active approaches

The only approach with a program and a verified claim is `biquadratic-character-divisors` (adopted). It attacks Conjecture 29 via quartic reciprocity in Z[i] on the Gaussian factor 2^p + i.

## Don't

- Do not write more approach files. 7 approaches against 4 checked and 1 proved is already lopsided.
- Do not re-derive the 2-adic budget identity, the parity theorem, or the lower bound on a.
- Do not search for a sixth unitary perfect number.
- Do not fetch further sources.
